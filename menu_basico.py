#menu
def menu():
    print("""**********************************************
===BIENVENIDO A RECYLIFE===""")
    print("\n1. Registrar Institucion")
    print("-> 2. Lista de Registro")
    print("-> 3. Consultar Institucion")
    print("-> 4. Modificar Institucion")
    print("-> 5. Eliminar Institucion")
    print("\n6. Registrar Estudiante")
    print("-> 7. Lista de Registro")
    print("-> 8. Consultar Estudiante")
    print("-> 9. Modificar Estudiante")
    print("-> 10. Eliminar Estudiante")
    print("""\nLema:
===Let's work together to breathe freely===
**********************************************""")
    
##################################################################################################################

#funciones de registro (instituciones)
def registro_instituciones():
    print("===INFORMACION DE LA INSTITUCION EDUCATIVA===")
    institucion={}
    continuar="s"
    while continuar=="s":
        id=int(input("\nIngrese ID: "))
        nombre=input("\nIngrese Nombre de la Institucion: ")
        direccion=input("\nIngrese la direccion: ")
        celular=input("\nIngrese el numero de celular: ")
        email=input("\nIngrese el email: ")
        institucion[id]=(nombre,direccion,celular,email)
        continuar=input("Si desea registrar otra Institucion Educativa escriba 's' y si no escriba 'n': ")
    return institucion

#funcion de lista (instituciones)
def listar_instituciones(institucion):
    print("\n===INSTITUCIONES REGISTRADAS===")
    for id in institucion:
        print(id,institucion[id][0],institucion[id][1],institucion[id][2],institucion[id][3])

#funcion de consultar (instituciones)
def consultar_instituciones(institucion):
    id=int(input("Ingrese el ID de la institucion que quiere consultar: "))
    print("\n===CONSULTAR INSTITUCIONES===")
    if id in institucion:
        print("Nombre:",institucion[id][0])
        print("Direccion:",institucion[id][1])
        print("Celular:",institucion[id][2])
        print("Email:",institucion[id][3])

#funcion de modificar (instituciones)
def modificar_instituciones(institucion):
    print("\n===MODIFICAR INSTITUCIONES===")
    cd=int(input("Ingrese el ID de la institucion que quiere modificar: "))
    if cd in institucion:
        c=int(input("""\nSeleccione la categoria que quiere modificar
0. Nombre
1. Direccion
2. Celular
3. Email
\nIngresar numero: """))
        institucion_lista=list(institucion[cd])
        if c==1 or c==3 or c==5:
            mod=input("\nIngrese el nuevo texto: ")
        else:
            mod=input("\nIngrese el nuevo texto: ")
        institucion_lista[c]=mod
        cd1=institucion_lista
        institucion[cd]=cd1
        print("\n===!!TEXTO ACTUALIZADO!!===")
    return institucion

#funcion de eliminacion (institucion)
def eliminar_instituciones(institucion):
    print("\n===ELIMINAR INSTITUCION===")
    cd2=int(input("Ingrese el ID de la institucion que quiere eliminar: "))
    if cd2 in institucion:
        del(institucion[cd2])
        print("\n===!!INSTITUCION ELIMINADA!!===")
        
##################################################################################################################

#funciones de registro (estudiante)
def registro_estudiante():
    print("===INFORMACION DEl ESTUDIANTE===")
    estudiante={}
    continuar="s"
    while continuar=="s":
        id=int(input("\nIngrese ID: "))
        nombre=input("\nIngrese Nombres: ")
        apellido=input("\nIngrese Apellidos: ")
        tipo=input("\nIngrese el tipo de documento T.I o C.C: ")
        n_documento=int(input("\nIngrese el Numero de Documento de Identidad: "))
        email=input("\nIngrese el Email: ")
        grado=int(input("\nIngrese el Grado: "))
        estudiante[id]=(nombre,apellido,tipo,n_documento,email,grado)
        continuar=input("Si desea registrar otro Estudiante escriba 's' y si no escriba 'n': ")
    return estudiante

#funcion de lista (estudiantes)
def listar_estudiantes(estudiante):
    print("\n===ESTUDIANTES REGISTRADOS===")
    for id in estudiante:
        print(id,estudiante[id][0],estudiante[id][1],estudiante[id][2],estudiante[id][3],estudiante[id][4],estudiante[id][5])

#funcion de consultar (estudiantes)
def consultar_estudiantes(estudiante):
    id=int(input("Digite el codigo de la institucion a consultar: "))
    print("\n===CONSULTAR ESTUDIANTES===")
    if id in estudiante:
        print("Nombre:",estudiante[id][0])
        print("Apellido:",estudiante[id][1])
        print("Tipo:",estudiante[id][2])
        print("N# Documento:",estudiante[id][3])
        print("Email:",estudiante[id][4])
        print("Grado:",estudiante[id][5])
        
#funcion de modificar (estudiantes)
def modificar_estudiantes(estudiante):
    print("\n===MODIFICAR ESTUDIANTES===")
    cd=int(input('Ingrese el ID del estudiante que quiere modificar: '))
    if cd in estudiante:
        c=int(input("""\nSelecciona la categoria que quiere modificar
0. Nombre
1. Apellido
2. Tipo de Documento
3. N# Documento
4. Email
5. Grado
\nIngrese numero: """))
        estudiante_lista=list(estudiante[cd])
        if c==1 or c==3 or c==5:
            mod=input('\nIngrese el nuevo texto: ')
        else:
            mod=input('\nIngrese el nuevo texto: ')
        estudiante_lista[c]=mod
        cd1=estudiante_lista
        estudiante[cd]=cd1
        print("\n===!!!TEXTO ACTUALIZADO!!===")
    return estudiante

#funcion de eliminacion (estudiantes)
def eliminar_estudiantes(estudiante):
    print("\n===ELIMINAR ESTUDIANTES===")
    cd2=int(input("Ingrese el ID del estudiante que quiere eliminar: "))
    if cd2 in estudiante:
        del(estudiante[cd2])
        print("\n===!!ESTUDIANTE ELIMINADO!!===")
        
menu()

##################################################################################################################

while True:
    opc=int(input("\nSeleccion la categoria que desea ejecutar:  "))
    
    #instituciones
    if opc==1:
        institucion=registro_instituciones()     
    elif opc==2:
        listar_instituciones(institucion)
    elif opc==3:
        consultar_instituciones(institucion)     
    elif opc==4:
        modificar_instituciones(institucion)  
    elif opc==5:
        eliminar_instituciones(institucion)
        
    #estudiantes
    if opc==6:
        estudiante=registro_estudiante() 
    elif opc==7:
        listar_estudiantes(estudiante)      
    elif opc==8:
        consultar_estudiantes(estudiante)  
    elif opc==9:
        modificar_estudiantes(estudiante)  
    elif opc==10:
        eliminar_estudiantes(estudiante)
        
    opc=input("\nSelecciona S para salir: ")   
    if opc=="S":
        menu()
                