numero1= int(input("Digite um valor: "))
numero2= int(input("Digite outro valor: "))
numero3= int(input("Digite o ultimo valor: "))

numeros= [numero1, numero2, numero3] #professor dei uma pesquisada nas linhas 5,6 pois nao sabia criar isso
ordenados = sorted(numeros) 
print(f"Números em ordem crescente {ordenados}")