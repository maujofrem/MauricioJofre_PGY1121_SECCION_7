#PRUEBA3


import datetime





#VALIDAR NUMERO

def validarNum(tipo,texto,rMin=None, rMax=None):
    while True:
        try:
            nro=tipo(input(texto))
            if rMin!=None and rMax!=None:
                if rMin<=nro<=rMax:
                    break
                else:
                    print("Fuera de rango")
            elif rMin!=None:
                if rMin>=nro:
                    break
                else:
                    print(f"El valor minimo es {rMin}")
            elif rMax!=None:
                if nro<=rMax:
                    break
                else:
                    print(f"El valor máx. es {rMax}")
            else:
                break
                
        except:
            print("Debe ser un número")
    return nro

#MENU

def menu():
    print("#"*30)
    print("\t Yari Villagrande")
    print("#"*30)
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir Parejas")
    print("4.- Salir")
    return (validarNum(int,"opcion: ", 1,4))

#VALIDAR LARGO

def validarLen(texto,large,estricto):
    while True:
        entrada=input(texto)
        if estricto:
            if len(entrada)==large:
                break
            else:
                print(f"El largo debe ser de {large}")
        else:
            if len(entrada)>=large:
                break
            else:
                print(f"El largo minimo debe ser de {large}")
    return entrada

#VALIDAR CORREO

def validarEmail():
    while True:
        mail=validarLen("Ingrese el email: ",6,False)
        if '@' in mail:
            if "." in mail:
                break
            else:
                print("Falta un . en el email ")
        else:
            print("Falta el @ en el email")
    return mail

#VALIDAR NOMBRE
def validarNombre():
    while True:
        nombre=validarLen("Ingrese el nombre: ",2,True)
        if len(nombres) == 0:
            existe=False
            if nombre in nombres:
                existe=True
            if existe:
                print("El jugador ya ha sido registrado anteriormente")
            else:
                break
        else:
            break
    return nombre


'''def validarEdad():
    while True:
        edad=0
        if edad>80:
            compite=False
        else:
            compite=True
    return edad'''

def validarEdad():
    fActual=datetime.date.today()
    fechaNac=datetime.datetime.strptime(fechaNac, '%d-%m-%Y').date()
    if fechaNac.year<=1943:
        return True
    else:
        return False
        print("No cumple con la edad")
fechaNac=input("Ingrese su fecha de nacimiento(dd-mm-yyyy:)")

#BUSCAR RUT
def buscarRut(ruts):
    rut=validarLen(" Ingrese su rut: ",6,True)
    for r in range(len(ruts)):
        if rut==ruts[r]:
            return r
    return -1   #NO ENCUENTRA EL RUT


#CATEGORIAS

def validarCat(categorias):
    while True:
        categoria=("Ingrese una categoria (Oro: O, Plata: P o Bronce: B) ")
        if categoria == 'O' or categoria == 'P' or categoria == 'B':
            break
        else:
            print("Categoria incorrecta")
    return categoria


#REGISTRAR
def regJugador(jugadores,nombres,ruts,fechaNac,categorias,celular,idParejas,email):
    jugadores.append(validarNombre(("Ingrese su nombre y apellido: ")))
    ruts.append(input("Ingrese su RUT: "))
    fechaNac.append(validarEdad(jugadores,nombres,ruts,fechaNac,categorias,celular,idParejas,email))
    categorias.append(validarCat(jugadores,nombres,ruts,fechaNac,categorias,celular,idParejas,email))
    celular.append(input("Ingrese su numero de celular: "))
    email.append(validarEmail(jugadores,nombres,ruts,fechaNac,categorias,celular,idParejas,email))


#MOSTRAR PAREJAS

def mostrarParejas(jugadores,nombres,ruts,fechaNac,categorias,celular,idParejas,email):
    print(nombres,idParejas)



#MENU
op=0
jugadores = []
nombres = []
ruts = []
fechaNac = []
categorias = []
celular = []
idParejas = []
email = []



while op!=4:
    op=menu()
    if op==1: #Registrar
        jugadores,nombres,ruts,fechaNac,categorias,celular,idParejas,email, validarNombre(jugadores,nombres,ruts,fechaNac,categorias,celular,idParejas,email)
    elif op==2: #Buscar
        buscarRut
    elif op==3: #Imprimir Parejas
        mostrarParejas




