menu=0
while menu !=2:
    menu= int(input("1-Continuar 2-SAIR "))
    
    if menu == 1:
        print("Você entrou no sistema")
    elif menu == 2:
        print("Você parou! ")
    else:
        print("número inválido")