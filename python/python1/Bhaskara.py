import math 
valor1 = int(input("Digite a variável A: "))
valor2 = int(input("Digite a variável B: "))
valor3 = int(input("Digite a variável C: "))
delta = valor2**2 - 4*valor1*valor3

if delta < 0:
    print("Não tem raízes reais")

elif delta == 0:
    raiz = -valor2 / (2*valor1)
    print(f"Existe uma raiz real: {raiz:.2f}")

else:
    formulax1 = (-valor2+math.sqrt(delta)) / (2*valor1)
    formulax2 = (-valor2-math.sqrt(delta)) / (2*valor1)
    print(f"X1:{formulax1} X2:{formulax2}")