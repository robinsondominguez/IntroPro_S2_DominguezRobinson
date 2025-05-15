# ##################
# ##### Dia 6 ######
# ##################

##Diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,"numero":3023019865,"tipo":"trabajo"}
                 ,{"codigo":1,"numero":3983054625,"tipo":"personal"}]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                 ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)
print("")
print("")
print(listaRobusta)
print("")
print("")
#print(listaRobusta[0]["telefonos"][1]['numero'])

for i in range(len(listaRobusta[0]["telefonos"])):
    if(listaRobusta[0]["telefonos"][i]['tipo']=="trabajo"):
        print(listaRobusta[0]["telefonos"][i]['numero'])
print("")
print("")
numeroPrimeraPersona=listaRobusta[0]["telefonos"][1]['numero']
tipoNumeroPP=listaRobusta[0]["telefonos"][1]['tipo']
print(str(numeroPrimeraPersona)+ tipoNumeroPP)

booleanito = True
while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        diccionarioVacio={}

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")

    elif opcionUsuario==3:

     def mostrar_persona(id_busqueda):
      encontrado = False  # Variable para verificar si encontramos la persona

     for persona in listaRobusta:
        if persona["id"]==id_busqueda:
            print("\n##############################")
            print(f"### Persona: {persona['nombre']} {persona['apellido']} ###")
            print("##############################")
            print(f"ID: {persona['id']}")
            print(f"Edad: {persona['edad']} años")

            print("\n Teléfonos:")
            for telefono in persona["telefonos"]:
                print("---------------------------")
                print(f"Código: {telefono['codigo']}")
                print(f"Número: {telefono['numero']}")
                tipo = "Personal" if telefono['tipo'] == "personal" else "Trabajo"
                print(f"Tipo: {tipo}")
                print("---------------------------")

            encontrado = True  # Se encontro a la persona
            break  # Salimos del bucle para optimizar la búsqueda

     if not encontrado:
        print("\n La persona con ese ID no existe.")

    elif opcionUsuario == 5:
     print ("#################")
     print ("entraste a la opcion de eliminacion de cuentas")
     print ("Eliminar Persona")
     print ("#################")
    
     id_eliminar = int(input("ingresar el id de la persona que quiere eliminar: "))
    
     encontrado = False  # Verificacion si se ha encontrado a la persona a eliminar

     for i in range(len(listaRobusta)):  # Recorremos la lista
        if listaRobusta[i]["id"] == id_eliminar:
            del listaRobusta[i]  # Eliminamos la persona
            print(f" Persona con ID {id_eliminar} eliminada exitosamente.")
            encontrado = True
            break  # Salimos del bucle al eliminar la persona
        elif not encontrado:
         print(" Error, No se encontro la persona que buscabas a eliminar")

            
            
    elif(opcionUsuario==6):
        print("Adios")
        booleanito=False
    else:
        print("No es una opción válida")

    
    
    
#Desarrollado por Dominguez  Ulloa Robinson - T.I: 1104128994