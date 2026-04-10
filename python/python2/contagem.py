valor=int(input("Digite um valor: "))
if valor %2 == 0:
    for i in range(0,valor,2):
        print(i)
else:
    for n in range(1, valor,2):
        print(n)