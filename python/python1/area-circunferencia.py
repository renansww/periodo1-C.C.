raio= int(input("Qual o raio do circunferência? "))
pi= (input("Deseja selecionar o valor de π? se sim digite o valor, se não digite N "))

if pi == "N" or pi == "n":
    formula=(f"a área dessa circunferência é: {(raio*raio)}π")
    print(formula)

else:
    pi=float(pi)
    formulacompi=(f"a área dessa circunferência é: {raio*raio*pi}")
    print(formulacompi)