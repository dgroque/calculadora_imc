peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = peso/(altura**2)

print("O seu imc é: {:.1f}".format(imc))