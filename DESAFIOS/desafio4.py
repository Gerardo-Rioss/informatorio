lista_inmuebles = [
{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]

# INGRESO Y VALIDACION DE DATOS:

# AÑO
def ingresar_validar_anio():
    correcto = False
    while correcto== False:
        anio =input('Ingrese el año: ')
        if anio =='' or anio.isspace()== True:
            print('ERROR, no puede contener espacios en blanco!!!')
        elif anio.isdigit() == False:
            print('ERROR, tiene que ser un numero entero!!!')    
        elif len(anio)!=4: 
            print('ERROR, tiene que ser un numero de cuatro digitos!!!')
        elif int(anio)<2000:
            print('ERROR, el inmueble debe ser mayor al año 2000!!!')
        else:
            correcto=True
            return int(anio)

# METROS
def ingresar_validar_metros():
    correcto = False
    while correcto==False:
        metros =input('Ingrese metros cuadrados: ')
        if metros == '' or metros.isspace()==True:
            print('ERROR, no puede contener espacios en blanco...')
        elif metros.isdigit()==False: 
            print('ERROR, tiene que ser un numero entero!!!')
        elif int(metros)<60:
            print('ERROR, el inmueble no puede tener menos de 60 metros cuadrados...')
        else:
            correcto=True
            return int(metros)

# HABITACIONES
def ingresar_validar_habitaciones():
    correcto = False
    while correcto==False:
        habitaciones =input('Ingrese la cantidad de habitaciones: ')
        if habitaciones =='' or habitaciones.isspace()==True:
            print('ERROR, no puede contener espacios en blanco!!!')
        elif habitaciones.isdigit() == False:
            print('ERROR, tiene que ser un numero entero!!!')
        elif int(habitaciones)<2:
            print('ERROR, el inmueble no puede tener menos de dos habitaciones!!!')
        else:
            correcto=True
            return int(habitaciones)

# GARAJE
def ingresar_validar_garaje():
    correcto = False
    while correcto == False:
        garaje =input('Tiene garaje? ( 1 = SI / 2 = NO): ')
        if garaje =='' or garaje.isspace() == True:
            print('ERROR, no puede contener espacios en blanco!!!')
        elif garaje not in ('1','2'):
            print('ERROR, los valores que debe ingresar son: 1 = SI / 2 = NO !!!')
        else:
            correcto = True
            if garaje=='1':
                return True
            else:
                return False

# ZONA
def ingresar_validar_zonas():
    correcto = False
    while correcto== False:
        zona =input('Ingrese la zona (A,B,C): ')
        if zona =='' or zona.isspace()==True:
            print('ERROR, no puede contener espacios en blanco!!!')
        elif zona.upper() not in ('A','B','C'):
            print('ERROR, tiene que elegir unas de las zonas: A - B - C !!!' )
        else:
            correcto = True
            return zona.upper()

# ESTADO
def ingresar_validar_estado():
    correcto = False
    while correcto == False:
        estado = input('Ingresa el valor segun correponda al estado del inmueble: 1 - Disponible / 2 - Reservado / 3 - Vendido : ')
        if estado =='' or estado.isspace():
            print('ERROR, no puede contener espacios en blanco!!!')
        elif estado not in ('1','2','3'):
            print('ERROR, Ingresa el valor segun correponda al estado del inmueble: 1 - Disponible / 2 - Reservado / 3 - Vendido!!!')
        else:
            correcto= True
            if estado=='1':
                return 'Disponible'
            elif estado=='2':
                return 'Reservado'
            else:
                return 'Vendido'

# FUNCION PARA INGRESO DE DATOS DEL INMUEBLE
def ingresar_inmueble():    
    inmueble_ingresado={}
    inmueble_ingresado['año'] = ingresar_validar_anio()
    inmueble_ingresado['metros'] = ingresar_validar_metros()
    inmueble_ingresado['habitaciones'] = ingresar_validar_habitaciones()
    inmueble_ingresado['garaje'] = ingresar_validar_garaje()
    inmueble_ingresado['zona'] = ingresar_validar_zonas()
    inmueble_ingresado['estado'] = ingresar_validar_estado()
    return inmueble_ingresado

# FUNCION PARA IMPRIMIR LA LISTA COMPLETA DE INMUEBLES
def imprimir_lista():
    for inmueble in lista_inmuebles:
        print(inmueble)

# FUNCION AGREGAR UN INMUEBLE
def agregar_inmueble(nuevo_inmueble):
    lista_inmuebles.append(nuevo_inmueble)

# FUNCION EDITAR INMUEBLE
def editar_inmueble(inmueble_a_editar):
    if inmueble_a_editar in lista_inmuebles:
        print('        Ingrese los datos del inmueble con las modificaciones correspondientes:')
        index_del_inmueble = lista_inmuebles.index(inmueble_a_editar)
        inmueble_modificado = ingresar_inmueble()
        lista_inmuebles.index(index_del_inmueble)==inmueble_modificado
    else:
        print('ERROR - El inmueble ingresado no se encuentra ingresado al sistema!!!')


# PROGRAMA:
imprimir_lista()
agregar_inmueble(ingresar_inmueble())
imprimir_lista()

















