inmuebles = [
{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]
zonas=('A','B','C')

#                             DECLARACION  DE FUNCIONES:

# VALIDACION DE DATOS INGRESADOS:

# funcion para validad que los datos ingresados en AÑO sea un valor entero de 4 digitos y controle que no ingrese vacios 
def validar_anio(anio):
    if len(anio)!=4 or not anio.isdigit() or anio == '' or anio.isspace() or int(anio)<2000:
        return False
    return True
# funcion para validad que los datos ingresados en los METROS que sean enteros y que no ingrese vacios 
def validar_metros(metros):
    if not metros.isdigit() or metros == '' or metros.isspace() or int(metros)<60:
        return False
    return True
# funcion para validad que los datos ingresados en HABITACIONES que sean enteros y que no ingrese vacios 
def validar_habitaciones(habitaciones):
    if not habitaciones.isdigit() or habitaciones =='' or habitaciones.isspace() or int(habitaciones)<2:
        return False
    return True
# funcion para validad que los datos ingresados en GARAJE que sean enteros y que no ingrese vacios (solo puede ingresar 1 o 2) 
def validar_garaje(garaje):
    opciones ='12'
    if not garaje.isdigit() or garaje =='' or garaje.isspace() or garaje not in opciones:
        return False
    return True
# funcion para validar que las ZONAS no sean numeros, espacios vacios...solo puede ingresar A,B o c
def validar_zonas(zona):
    opciones ='ABC'    
    if zona.isdigit() or zona =='' or zona.isspace() or zona.upper() not in opciones:
        return False
    return True
# funcion para validar que los ESTADOS sean numeros, no espacios vacios...solo puede ingresar 1 2 3
def validar_estado(estado):
    opciones ='123'    
    if not estado.isdigit() or estado =='' or estado.isspace() or estado not in opciones:
        return False
    return True

# AGREGAR INMUEBLE
def agregar_inmueble():
    print(inmuebles)
    print('--------        DATOS DEL INMUEBLE        --------')
    anio =input('Año: ')
    while validar_anio(anio)==False:
        anio = input('ERROR en datos ingresados en AÑOS, intentelo nuevamente: ')
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
                        inmuebles['año'] = int(anio)
                        inmuebles['metros'] = metros
                        inmuebles['habitaciones'] = habitaciones
                        if garaje =='1':
                            inmuebles['garaje'] = True
                        else:
                            inmuebles['garaje'] = False
                        inmuebles['zona'] = zona.upper()
                        inmuebles['estado'] = 'Disponible'
    print(inmuebles)



