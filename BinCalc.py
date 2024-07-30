#Opção 1 - Programa de conversões de bases
def convert():
  print("\n---FAÇA A CONVERSÃO DESEJADA--- ")
  print("\n1 - Binário para decimal")
  print("2 - Binário para hexadecimal")
  print("3 - Binário para octal")
  print("4 - Decimal para binário")
  print("5 - Decimal para hexadecimal")
  print("6 - Decimal para octal")
  print("7 - Hexadecimal para decimal")
  print("8 - Hexadecimal para binário")
  print("9 - Hexadecimal para octal")
  wel = input("\nDigite a opção sobre o tipo de conversão desejada (Digite somente o número, exemplo: 1): ")

#Subopção 1 - "Binário para decimal"
  def bindec():
    def is_binary(value):
      # Verifica se o valor contém apenas 0s e 1s
      return all(char in '01' for char in value)

    def binary_to_decimal(binary_value):
      if not is_binary(binary_value):
          return "\n***O valor digitado NÃO está em formato binário.***"

      decimal_value = int(binary_value, 2)
      return decimal_value

    # Exemplo de uso
    valor_binario = input("\nDigite um valor binário: ")
    resultado = binary_to_decimal(valor_binario)
    print(f"\n---Valor em decimal: {resultado}---")  
#Fim da subopção 1 - "Binário para decimal

#Subopção 2 - "Binário para hexadecimal"
  def binhex():
    def is_binary(value):
      # Verifica se o valor contém apenas 0s e 1s
      return all(char in '01' for char in value)

    def binary_to_hexadecimal(binary_value):
      if not is_binary(binary_value):
          return "\n***O valor NÃO está em formato binário.***"

      decimal_value = int(binary_value, 2)
      hexadecimal_value = hex(decimal_value)[2:] 
      return hexadecimal_value.upper()  

    # Exemplo de uso
    valor_binario = input("Digite um valor binário: ")
    resultado = binary_to_hexadecimal(valor_binario)
    print(f"\n---Valor em hexadecimal: {resultado}---")

#Fim da subopção 2 - "Binário para hexadecimal"

#Subopção 3 - Binário para octal
  def binoc():
    def is_binary(value):
      # Verifica se o valor contém apenas 0s e 1s
      return all(char in '01' for char in value)

    def binary_to_octal(binary_value):
      if not is_binary(binary_value):
          return "\n***O valor digitado NÃO está em formato binário***"

      decimal_value = int(binary_value, 2)
      octal_value = oct(decimal_value)[2:]
      return octal_value

    valor_binario = input("\nDigite um valor binário: ")
    resultado = binary_to_octal(valor_binario)
    print(f"\n---Valor em octal: {resultado}---")
#Fim da subopção 3 - Binário para octal  

#Subposição 4 -  Decimal para binário
  def decbin():
    def is_decimal(value):
      try:
          int(value)  
          return True
      except ValueError:
          return False

    def decimal_to_binary(decimal_value):
      if not is_decimal(decimal_value):
          return "\n***O valor inserido NÃO está em formato decimal***"

      decimal_value = int(decimal_value)
      binary_value = bin(decimal_value)[2:]  
      return binary_value

    # Exemplo de uso
    valor_decimal = input("\nDigite um valor decimal: ")
    resultado = decimal_to_binary(valor_decimal)
    print(f"\n---Valor em binário: {resultado}---")
#Fim da subopção 4 - Decimal para binário
  
#Subopção 5 - Decimal para hexadecimal
  def dechex():
    def is_decimal(value):
      try:
          int(value)  
          return True
      except ValueError:
          return False

    def decimal_to_hexadecimal(decimal_value):
      if not is_decimal(decimal_value):
          return "\n***O valor inserido NÃO está em formato decimal***"

      decimal_value = int(decimal_value)
      hexadecimal_value = hex(decimal_value)[2:]  
      return hexadecimal_value.upper()  

    valor_decimal = input("Digite um valor decimal: ")
    resultado = decimal_to_hexadecimal(valor_decimal)
    print(f"\n---Valor em hexadecimal: {resultado}---")
#Fim da subopção 5 - Decimal para hexadecimal

#Subopção 6 - Decimal para octal
  def decoctal():
    def is_decimal(value):
      try:
          int(value) 
          return True
      except ValueError:
          return False

    def decimal_to_octal(decimal_value):
      if not is_decimal(decimal_value):
          return "\n***O valor inserido NÃO está em formato decimal***"

      decimal_value = int(decimal_value)
      octal_value = oct(decimal_value)[2:] 
      return octal_value

    valor_decimal = input("Digite um valor decimal: ")
    resultado = decimal_to_octal(valor_decimal)
    print(f"\n---Valor em octal: {resultado}---")
#Fim da subopção 6 - Decimal para octal 
  
#Subopção 7 - Hexadecimal para decimal
  def hexdec():
    def is_hexadecimal(value):
      
      return all(char in '0123456789ABCDEFabcdef' for char in value)

    def hexadecimal_to_decimal(hex_value):
      if not is_hexadecimal(hex_value):
          return "\n***O valor inserido NÃO está em formato hexadecimal***"

      decimal_value = int(hex_value, 16)
      return decimal_value

    valor_hexadecimal = input("Digite um valor hexadecimal: ")
    resultado = hexadecimal_to_decimal(valor_hexadecimal)
    print(f"\n---Valor em decimal: {resultado}---")
#Fim da subopção 7 - Hexadecimal para decimal

#Subopção 8 - Hexadecimal para binário
  def hexbin():
    def is_hexadecimal(value):
  
      return all(char in '0123456789ABCDEFabcdef' for char in value)

    def hexadecimal_to_binary(hex_value):
      if not is_hexadecimal(hex_value):
          return "\n***O valor inserido NÃO está em formato hexadecimal***"

      decimal_value = int(hex_value, 16)
      binary_value = bin(decimal_value)[2:]  
      return binary_value

    valor_hexadecimal = input("Digite um valor hexadecimal: ")
    resultado = hexadecimal_to_binary(valor_hexadecimal)
    print(f"\n---Valor em binário: {resultado}---")
#Fim da Subopção 8 - Hexadecimal para binário

#Subopção 9 - Hexadecimal para octal
  def hexoctal():
    def is_hexadecimal(value):
  
      return all(char in '0123456789ABCDEFabcdef' for char in value)

    def hexadecimal_to_octal(hex_value):
      if not is_hexadecimal(hex_value):
          return "\n***O valor inserido NÃO está em formato hexadecimal***"

      decimal_value = int(hex_value, 16)
      octal_value = oct(decimal_value)[2:]  
      return octal_value

    valor_hexadecimal = input("Digite um valor hexadecimal: ")
    resultado = hexadecimal_to_octal(valor_hexadecimal)
    print(f"\n---Valor em octal: {resultado}---")
#Fim da Subopção 9 - Hexadecimal para octal
  
  if wel == "1":
    bindec()
  elif wel == "2":
    binhex()
  elif wel == "3":
    binoc()
  elif wel == "4":
    decbin()
  elif wel == "5":
    dechex()
  elif wel == "6":
    decoctal()
  elif wel == "7":
    hexdec()
  elif wel == "8":
    hexbin()
  elif wel == "9":
    hexoctal()
  else:
    print("\n--OPÇÃO INVÁLIDA-- insira o valor correspondente a opção desejada")
 #Fim da Opção 1 - Programa de conversões de bases

#Opcção 2 - Operações aritméticas binárias
def operations():
  print("\n--FAÇA O CÁLCULO DESEJADO--")
  print("\n1 - Adição")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  choice = input("\nDigite a opção para a operação aritmética desejada (Digite somente o número, exemplo: 1): ")

#Subopção 1 - Adição  
  def soma():
    def is_binary(value):
      return all(char in '01' for char in value)

    def binary_addition(a, b):
      if not is_binary(a) or not is_binary(b):
          return "\n***Os valores inseridos NÃO estão em formato binário***"

      decimal_sum = int(a, 2) + int(b, 2)
      binary_sum = bin(decimal_sum)[2:]  
      return binary_sum


    valor_binario1 = input("\nDigite o primeiro valor binário: ")
    valor_binario2 = input("Digite o segundo valor binário: ")
    resultado = binary_addition(valor_binario1, valor_binario2)
    print(f"\n---Resultado da soma em binário: {resultado}---")
#Fim da Subopção 1 - Adição  

#Subopção 2 - Subtração
  def sub():
    def is_binary(value):
      return all(char in '01' for char in value)

    def binary_subtraction(a, b):
      if not is_binary(a) or not is_binary(b):
          return "\n***Os valores inseridos NÃO estão em formato binário***"

      int_a = int(a, 2)
      int_b = int(b, 2)
    
      result = int_a - int_b
      binary_result = bin(result)[2:]  

      return f"\n---O resultado é: {binary_result}---"

    valor1 = input("\nDigite o primeiro valor binário: ")
    valor2 = input("Digite o segundo valor binário: ")

    print(binary_subtraction(valor1, valor2))
#Fim da subopção 2 - Subtração

#Subopção 3 - Multiplicação
  def multi():
    def is_binary(value):
      return all(char in '01' for char in value)

    def binary_multiplication(a, b):
      if not is_binary(a) or not is_binary(b):
          return "\n***Os valores inseridos NÃO estão em formato binário***"

      int_a = int(a, 2)
      int_b = int(b, 2)
      
      result = int_a * int_b

      binary_result = bin(result)[2:]  

      return f"\n---O resultado é: {binary_result}---"

    valor1 = input("\nDigite o primeiro valor binário: ")
    valor2 = input("Digite o segundo valor binário: ")
    print(binary_multiplication(valor1, valor2))
#Fim da subopção 3 - Multiplicação

#Subopção 4 - Divisão
  def div():
    def is_binary(value):
      
      return all(char in '01' for char in value)

    def binary_division(a, b):
      if not is_binary(a) or not is_binary(b):
          return "\n***Os valores inseridos NÃO estão em formato binário***"

      decimal_a = int(a, 2)
      decimal_b = int(b, 2)

      if decimal_b == 0:
          return "\n***Não é possível dividir por zero***"

      quotient = decimal_a // decimal_b
      remainder = decimal_a % decimal_b

      quotient_binary = bin(quotient)[2:]  
      remainder_binary = bin(remainder)[2:]

      return f"\nQuociente em binário: {quotient_binary}\nResto em binário: {remainder_binary}"

    valor_binario1 = input("\nDigite o primeiro valor binário: ")
    valor_binario2 = input("Digite o segundo valor binário: ")
    resultado = binary_division(valor_binario1, valor_binario2)
    print(resultado)
#Fim da subopção 4 - Divisão

  if choice == "1":
    soma()
  elif choice == "2":
    sub()
  elif choice == "3":
    multi()
  elif choice == "4":
    div()

def main():
  while True:
    print("\n***SEJA BEM VINDO(A)***")
    print("\n1 - Conversão de bases")
    print("2 - Operações aritméticas binárias")
    print("3 - Encerrar programa")
    choose = input("\nDigite a opção desejada ou 0 para finalizar: ")

    if choose == "1":
      convert()
    elif choose == "2":
      operations()
    elif choose == "3":
      print("\nPrograma encerrado")
      break
    else:
      print("\n--OPÇÃO INVÁLIDA--")

if __name__ == "__main__":
  main()


      
    