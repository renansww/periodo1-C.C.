de0_25 = 0
de26_60 = 0
maisde60 = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    if idade <= 25:
        de0_25 += 1
    elif idade <= 60:
        de26_60 += 1
    else:
        maisde60 += 1

    sn = input("Deseja cadastrar outra idade? (s) ou (n): ")
    if sn == 'n':
        break

print("----------------------------------------")
print(f"Total de pessoas entre 0 e 25 anos: {de0_25}")
print(f"Total de pessoas entre 26 e 60 anos: {de26_60}")
print(f"Total de pessoas com mais de 60 anos: {maisde60}")