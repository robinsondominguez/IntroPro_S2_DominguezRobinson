###############
##### Di2 #####
###############

#ingreso de los valores

print('bienvenido, ingrese el primer valor')

#verifacion de los numeros

verificarNumero=int(input())

divisores=0

for i in range (1,verificarNumero,1):

    divisores = divisores +1

    resultado = verificarNumero % divisores

    if resultado == 0:
        cantidadDivisores = cantidadDivisores+1
        
if cantidadDivisores > 2:
       
else:
    print('el numero es primo')


# Creado por : Dominguez Ulloa Robinson      -       T.I: 1.104.128.994
