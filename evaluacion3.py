#Listas
lista_tipo = ["encomienda"]
lista_nombre = ["benjamin"]
lista_rut = ["20179020-4"]
lista_peso = [3455]
lista_precio = [454]
lista_destino = ["cancun"]

#Funciones

def mostrar_menu():
    print("""
    Menu:
    1- Grabar
    2- Buscar
    3- Listart encomiendas
    4- Salir
    """)

def grabar():
    def ingresar_tipo():
        tipo = int(input("que tipo de de encomienda es 1 = sobre 2 = paquete"))
        if tipo == 1 :
            lista_tipo.append("sobre")
        elif tipo == 2:
            lista_tipo.append("encomienda")
        else:
            print("debe ingresar una opcion valida")
            ingresar_tipo()
       

    def ingresar_nombre():
        nombre_destinatario = input("ingrese el nombre del destinatario")
        if len(nombre_destinatario) <= 2 and len(nombre_destinatario) > 30:
            print("debe ingresar un nombre mayor a 2 caracteres y menor a 30")
            ingresar_nombre()
        else:
            lista_nombre.append(nombre_destinatario.capitalize()) 
    
    def ingresar_rut():
        rut_destinatario = (input("ingrese el rut del destinatario"))
        if rut_destinatario[-2] != "-":
            print("Este es un rut invalido, vuelva a ingresar")
            ingresar_rut()
        else:
            lista_rut.append(rut_destinatario)

    def ingresar_peso():
        peso_kg = float(input("ingrese el peso de la encomienda"))
        if peso_kg < 0.1:
            print("debe ingresar un peso mayor")
            ingresar_peso()
        else:
            lista_peso.append(peso_kg)

    def ingresar_precio():
        precio = int(input("ingrese el precio"))
        if precio < 2000:
            print("el precio minimo es 2000")
            ingresar_peso()
        else:
            lista_precio.append(precio)
    def ingresar_destino():
        ciudad_destino = input("ingrese la ciudad de destino")
        if len(ciudad_destino) < 3 :
            print("debe ingresar una ciudad con mas de 3 caracteres")
            ingresar_destino()
        else:
            lista_destino.append(ciudad_destino.capitalize())
    
    ingresar_tipo()
    ingresar_rut()
    ingresar_nombre()
    ingresar_peso()
    ingresar_precio()
    ingresar_destino()

def buscar():
    rut = input("ingrese el rut")
    def validar_rut(rut):
        if rut[-2] != "-":
                print("Este es un rut invalido, vuelva a ingresar")
                buscar()
        else:
            print("rut invalido")
    def buscador(rut):
        for i in range(lista_rut):
            if i == rut:
                index = lista_rut.index(i)
                print(f"{lista_nombre[index],lista_rut[index], lista_destino[index], lista_tipo[index], lista_peso[index], lista_precio[index]}")
            else:
                return print("no se encontro")
    validar_rut(rut)
    buscador(rut)
    

while True:
    try:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion"))
        if opcion == 1:
            grabar()
        elif opcion == 2:
            buscar()
        """
        elif opcion == 3:
            listar_encomiendas()
        elif opcion == 4
            break"""
    except:
        print("ocurrio un error")
