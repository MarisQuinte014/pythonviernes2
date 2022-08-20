nivelAgua = int(input("Digita el nivel de agua"))

if(nivelAgua >= 0 and nivelAgua < 20):
    print(f'Peligro el nivel de agua es de {nivelAgua} y es muy bajo')
elif(nivelAgua >= 20 and nivelAgua < 400):
    print(f'El nivel de agua esta {nivelAgua} y es bueno')
elif(nivelAgua >= 400):
    print(f'Peligro el nivel de agua es de {nivelAgua} y es muy alto')
else:
    print(f'Digita una opción valida')