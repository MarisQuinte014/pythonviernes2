mes = input("Digite un mes")

if(mes == 'enero' or mes == 'febrero' or mes == 'marzo'):
    print(f'Estas en el mes de {mes} y es Invierno')
elif(mes == 'julio' or mes == 'agosto' or mes == 'septiembre'):
    print(f'Estas en el mes de {mes} y es Verano')
elif(mes == 'abril' or mes == 'mayo' or mes == 'junio'):
    print(f'Estas en el mes de {mes} y es Primavera')
elif(mes == 'otoño' or mes == 'noviembre' or mes == 'diciembre'):
    print(f'Estas en el mes de {mes} y es Otoño')
else:
    print(f'Esto no es valido')