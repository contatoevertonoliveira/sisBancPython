import os

class style():
  BLACK = '\033[30m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  MAGENTA = '\033[35m'
  CYAN = '\033[36m'
  WHITE = '\033[37m'
  UNDERLINE = '\033[4m'
  RESET = '\033[0m'
  
def Clear_Screen():
	sistema = os.name
	if sistema == 'nt':
		os.system('cls')
	else:
		os.system('clear')

menu = f"""{style.YELLOW}
-----------------------------------------------------------
==== Bem Vindo ao Banco SEU, escolha uma opção abaixo: ====
-----------------------------------------------------------
{style.RESET}
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
-----------------------------------------------------------
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
valor = 0
LIMITE_SAQUES = 3

Clear_Screen()
while True:
  opcao = input(menu)
  print(f"{style.YELLOW}-----------------------------------------------------------{style.RESET}")
  
  if opcao == "d":
    print("=== Depositando... ===")
    valor = float(input("Informe o valor de depósito: "))
    
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: {style.GREEN}R$ {valor:.2f}{style.RESET}\n"
    else:
      print("Operação final falhou! O valor informado é inválido!")
  elif opcao == "s":
    print("=== Sacando... ===")
    valor = float(input("Informe o valor do saque: "))
    
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saques >= LIMITE_SAQUES
    
    if saldo_excedido:
      print("Operação falhou! Você não tem saldo suficiente!")
    elif limite_excedido:
      print("Operação falhou! O valor do saque excede o limite!")
    elif saque_excedido:
      print("Operação falhou! Você já excedeu o número máximo de saques!")
    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: {style.RED}R$ {valor:.2f}{style.RESET}\n"
      numero_saques += 1
    else:
      print("Operação falhou! O valor informado é inválido!")
     
  elif opcao == "e":
    print("\n========================== Extrato ============================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    
    if valor > 0:
      print(f"\nSaldo: {style.GREEN}R$ {saldo:.2f}{style.RESET}")
    elif valor < 0:
      print(f"\nSaldo: {style.RED}R$ {saldo:.2f}{style.RESET}")
    else:
      print(f"\nSaldo: R$ 0")
    print("=================================================================")
  elif opcao == "q":
    break
  else:
    print("Opção inválida! Por favor, tente novamente.")