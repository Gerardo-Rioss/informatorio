lista_inmuebles = {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}

datos_correctos = {"correcto" : False}
zonas=("A","B","C")


def anio_correcto():
    while true:
        anio = input("Año: ")
        if len(anio) !=4:
            print("El año tiene que tener cuatro digitos, intentelo de nuevo")
            continue
        if not anio.isdigit():
            print("El año debe ser solo numeros. Intetelo de nuevo")
            continue
        break

print (anio_correcto())