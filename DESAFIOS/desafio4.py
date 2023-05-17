lista_inmuebles = [
{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]

# VALIDACION DE DATOS INGRESADOS:
# AÑO
def validar_anio(anio):
    # si el dato de entrada es anio
    if anio =='' or anio.isspace()== True:
        print('ERROR, no puede contener espacios en blanco!!!')
        return False
    elif anio.isdigit() == False:
        print('ERROR, tiene que ser un numero entero!!!')    
        return False
    elif len(anio)!=4: 
        print('ERROR, tiene que ser un numero de cuatro digitos!!!')
        return False
    elif int(anio)<2000:
        print('ERROR, el inmueble debe ser mayor al año 2000!!!')
        return False
    return True

# METROS
def validar_metros(metros):
    if metros == '' or metros.isspace()==True:
        print('ERROR, no puede contener espacios en blanco...')
        return False
    elif metros.isdigit()==False: 
        print('ERROR, tiene que ser un numero entero!!!')
        return False
    elif int(metros)<60:
        print('ERROR, el inmueble no puede tener menos de 60 metros cuadrados...')
        return False
    return True

# HABITACIONES
def validar_habitaciones(habitaciones):
    if habitaciones =='' or habitaciones.isspace()==True:
        print('ERROR, no puede contener espacios en blanco!!!')
        return False
    elif habitaciones.isdigit() == False:
        print('ERROR, tiene que ser un numero entero!!!')
        return False
    elif int(habitaciones)<2:
        print('ERROR, el inmueble no puede tener menos de dos habitaciones!!!')
        return False
    return True

# GARAJE
def validar_garaje(garaje):
    if garaje =='' or garaje.isspace() == True:
        print('ERROR, no puede contener espacios en blanco!!!')
        return False
    elif garaje not in ('1','2'):
        print('ERROR, los valores que debe ingresar son: 1 = SI / 2 = NO !!!')
        return False
    return True

# ZONA
def validar_zonas(zona):
    if zona =='' or zona.isspace()==True:
        print('ERROR, no puede contener espacios en blanco!!!')
        return False
    elif zona.upper() not in ('A','B','C'):
        print('ERROR, tiene que elegir unas de las zonas: A - B - C !!!' )
        return False
    return True

# ESTADO
def validar_estado(estado):
    if estado =='' or estado.isspace():
        print('ERROR, no puede contener espacios en blanco!!!')
    elif estado not in ('1','2','3'):
        print('ERROR, Ingresa el valor segun correponda al estado del inmueble: 1 - Disponible / 2 - Reservado / 3 - Vendido!!!')
        return False
    return True

# FUNCION PARA INGRESO DE DATOS DEL INMUEBLE
# Esta funcion es para ingresar los datos del inmueble, controla que ingrese los valores correctos y retorna un diccionario con dichos datos
def ingresar_inmueble():    
    anio =input('Año: ')
    while validar_anio(anio)==False:
        anio = input('Año: ')
    else:    
        metros =input('Metros cuadrados: ')
        while validar_metros(metros) == False:
            metros =input('Metros cuadrados: ')
        else:
            habitaciones =input('Cantidad de habitaciones: ')
            while validar_habitaciones(habitaciones) == False:
                habitaciones =input('Cantidad de habitaciones: ')
            else:
                garaje =input('Tiene garaje ( 1=SI / 2=NO): ')
                while validar_garaje(garaje) == False:
                    garaje =input('Tiene garaje? ( 1=SI / 2=NO): ')
                else:
                    zona =input('Ingrese la zona (A,B,C): ')
                    while validar_zonas(zona) == False:
                        zona =input('Ingrese la zona (A,B,C): ')
                    else:
                        estado = input('Ingresa el valor segun correponda al estado del inmueble: 1 - Disponible / 2 - Reservado / 3 - Vendido : ')
                        while validar_estado(estado) == False:
                            estado = input('Ingresa el valor segun correponda al estado del inmueble: 1 - Disponible / 2 - Reservado / 3 - Vendido : ' )
                        else:
                            inmueble_ingresado={}
                            inmueble_ingresado['año'] = int(anio)
                            inmueble_ingresado['metros'] = int(metros)
                            inmueble_ingresado['habitaciones'] = int(habitaciones)
                            if garaje =='1':
                                inmueble_ingresado['garaje'] = True
                            else:
                                inmueble_ingresado['garaje'] = False
                            inmueble_ingresado['zona'] = zona.upper()
                            if estado == '1':
                                inmueble_ingresado['estado'] = 'Disponible'
                            elif estado == '2':
                                inmueble_ingresado['estado'] = 'Reservado'
                            else:
                                inmueble_ingresado['estado'] = 'Vendido'
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

    

imprimir_lista()
print(editar_inmueble(ingresar_inmueble()))
imprimir_lista()


















