print("bienvenido a rappid, cuantas hamburguesas quieres?")
hamburguesas = int(input())
subTotal = 0
for i in range (1,hamburguesas+1):

    print("selecciona el tipo de pan")
    print("1) avena ----- $1000")
    print("2) centeno ----- $1500")
    opc = int(input())

    if opc == 1:
        subTotal = subTotal + 1000
    elif opc == 2:
        subTotal = subTotal + 1500

    print("selecciona el tipo de carne")
    print("1) 250G ----- $5000")
    print("2) 350G ----- $7000")
    opc = int(input())

    if opc == 1:
        subTotal = subTotal + 5000
    elif opc == 2:
        subTotal = subTotal + 7000

    print("selecciona el tipo de pollo")
    print("1) 250G ----- $4500")
    print("2) 350G ----- $5500")
    opc = int(input())

    if opc == 1:
        subTotal = subTotal + 4500
    elif opc == 2:
        subTotal = subTotal + 5500

    print("selecciona el tipo de pollo desmechado")
    print("1) 250G ----- $5000")
    print("2) 350G ----- $7000")
    opc = int(input())

    if opc == 1:
        subTotal = subTotal + 5000
    elif opc == 2:
        subTotal = subTotal + 7000

    print("selecciona el tipo de tocineta")
    print("1) lonja de tocineta ----- $1500")
    print("2) lonjas de tocinetas ----- $2500")
    opc = int(input())

    if opc == 1:
        subTotal = subTotal + 1500
    elif opc == 2:
        subTotal = subTotal + 2500

    print("selecciona el tipo de papitas")
    print("1) Francesas ----- $5000")
    print("2) Cascos ----- $6000")
    opc = int(input())

    if opc == 1:
        subTotal = subTotal + 5000
    elif opc == 2:
        subTotal = subTotal + 6000

    print("selecciona el tipo de bebidas")
    print("1) Gaseosa ----- $5000")
    print("2) Cervezas ----- $8000")
    print("3) Naranjada ----- $9000")
    opc = int(input())

    if opc == 1:
        subTotal = subTotal + 5000
    elif opc == 2:
        subTotal = subTotal + 8000
    elif opc == 3:
        subTotal = subTotal + 9000

    Servicio = subTotal * 0.9
    totalPagar = subTotal + Servicio

    print("el subtotal es: ", subTotal)
    print("mas el servicio es de: ", Servicio)
    print(" el servicio mas el subtotal da un total de: ", totalPagar)
