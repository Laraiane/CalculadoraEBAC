while True:
  a = float(input("Insira o primeiro número: "))
  b = float(input("Insira o segundo número: "))
  c = input("Qual operação deseja fazer?\n1 = Soma,\n2 = Subtração,\n3 = Divisão e/ou\n4 = Multiplicação\n")

  if c == '1':
    print("O resultado é igula a :", a + b)
  elif c == '2':
    print("O resultado é igula a :", a - b)
  elif c == '3':
    if b == 0:
      print("Não é possível dividir por zero")
    else:
      print("O resultado é igula a :", a / b)
  elif c == '4':
    print("O resultado é igula a :", a * b)
  else:
    print("Operação inválida")
  if (input("Deseja realizar outra operação? s/n\n")).lower() != 's':
    break
