lista_inmuebles = [
{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]


#                             DECLARACION  DE FUNCIONES:

# VALIDACION DE DATOS INGRESADOS:

# funcion para validad que los datos ingresados en AÑO sea un valor entero de 4 digitos y controle que no ingrese vacios 
def validar_anio(anio):
    if anio == '' or anio.isspace()== True:
        print('ERROR, no puede contener espacios en blanco...')
        return False
    elif anio.isdigit() == False:
        print('ERROR, tiene que ser un numero entero...')    
        return False
    elif len(anio)!=4: 
        print('ERROR, tiene que ser un numero de cuatro digitos...')
        return False
    elif int(anio)<2000:
        print('ERROR, el inmueble debe ser mayor al año 2000...')
        return False
    return True

# funcion para validad que los datos ingresados en los METROS que sean enteros y que no ingrese vacios 
def validar_metros(metros):
    if metros == '' or metros.isspace()==False:
        print("ERROR, no puede contener espacios en blanco...")
    elif metros.isdigit()==False: 
        print("ERROR, tiene que ser un numero entero...")
    elif int(metros)<60:
        print("ERROR, el inmueble no puede tener menos de 60 metros cuadrados...")
        return False
    return True

# funcion para validad que los datos ingresados en HABITACIONES que sean enteros y que no ingrese vacios 
def validar_habitaciones(habitaciones):
    if habitaciones =='' or habitaciones.isspace()==False:
        print("ERROR, no puede contener espacios en blanco...")
    elif habitaciones.isdigit() == False:
        print("ERROR, tiene que ser un numero entero...")
    elif int(habitaciones)<2:
        print("ERROR, el inmueble no puede tener menos de dos habitaciones...")
        return False
    return True

# funcion para validad que los datos ingresados en GARAJE que sean enteros y que no ingrese vacios (solo puede ingresar 1 o 2) 
def validar_garaje(garaje):
    if not garaje.isdigit() or garaje =='' or garaje.isspace() or garaje not in ('1','2'):
        return False
    return True
# funcion para validar que las ZONAS no sean numeros, espacios vacios...solo puede ingresar A,B o c
def validar_zonas(zona):
    if zona.isdigit() or zona =='' or zona.isspace() or zona.upper() not in ('A','B','C'):
        return False
    return True
# funcion para validar que los ESTADOS sean numeros, no espacios vacios...solo puede ingresar 1(Disponible) 2(Reservado) 3(Vendido)
def validar_estado(estado):
    if not estado.isdigit() or estado =='' or estado.isspace() or estado not in ('1','2','3'):
        return False
    return True

# AGREGAR INMUEBLE
def agregar_inmueble():
    print('--------        DATOS DEL INMUEBLE        --------')
    anio =input('Año: ')
    while validar_anio(anio)==False:
        anio = input('Año: ')
    else:    
        metros =input('Metros cuadrados: ')
        while validar_metros(metros) == False:
            metros = input('ERROR en datos ingresados en METROS, intentelo nuevamente: ')
        else:
            habitaciones =input('Cantidad de habitaciones: ')
            while validar_habitaciones(habitaciones) == False:
                input('ERROR en datos ingresados en HABITACIONES, intentelo nuevamente: ')
            else:
                garaje =input('Tiene garaje ( 1=SI / 2=NO): ')
                while validar_garaje(garaje) == False:
                    input('ERROR en datos ingresados en GARAJE, intentelo nuevamente ( 1=SI / 2=NO): ')
                else:
                    zona =input('Ingrese la zona (A,B,C): ')
                    while validar_zonas(zona) == False:
                        input('ERROR en datos ingresados en ZONA, intentelo nuevamente (A,B,C): ')
                    else:
                        nuevo_inmueble={}
                        nuevo_inmueble['año'] = int(anio)
                        nuevo_inmueble['metros'] = int(metros)
                        nuevo_inmueble['habitaciones'] = int(habitaciones)
                        if garaje =='1':
                            nuevo_inmueble['garaje'] = True
                        else:
                            nuevo_inmueble['garaje'] = False
                        nuevo_inmueble['zona'] = zona.upper()
                        nuevo_inmueble['estado'] = 'Disponible'
                        lista_inmuebles.append(nuevo_inmueble)

print(validar_anio('2001'))
#print(validar_anio('1900'))
