def verificar_par(numero):
    return numero % 2 == 0


numero = int(input("Digite um número: "))
if verificar_par(numero):
    print("O número é par.")
else:
    print("O número é ímpar.")
