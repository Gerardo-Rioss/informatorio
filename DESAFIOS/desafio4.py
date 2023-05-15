lista_inmuebles = {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}

datos_correctos = {"correcto" : False}
zonas=(A,B,C)

def agregar(anio,metros,habitaciones,garaje,zona):
    while datos_correctos['correcto'] ==False:

        # Pedimos al usuario los datos del nuevo inmueble
        print("--------------------------------------------------")
        print("       Ingrese los datos del inmueble:            ")
        
        anio = input("Año: ")
        if not anio.isdigit() and len(anio) >4:
            print("Los datos ingresados son incorrectos!!! --tiene que ser un numero de cuatro digitos--")
        else:
            metros = input("Metros cuadrados: ")
            if not metros.isdigit():
                print("Los datos ingresados son incorrectos!!! --Debe ingresar solo numeros en los metros")
            else:
                habitaciones = input("Cantidad de habitaciones: ")
                if not habitaciones.isdigit():
                    print("Los datos ingresados son incorrectos!!! --Debe ingresar solo numeros en la cantidad de habitaciones")
                else:
                    garaje = input("ingrese la opcion correspontiente,     1 = SI    2 = NO ")
                    if garaje not in range(1,2):
                        print("Los datos ingresados son incorrectos!!! --Debe ingresar solo el valor 1 o 2")
                    else:
                        zona = input("Zona")
                        if zona.upper() not in zonas:
                            print("Los datos ingresados son incorrectos!!! --Debe ingresar solo A, B o C")
                        else:
                            lista_inmuebles["año"]= anio
                            lista_inmuebles["habitaciones"] = habitaciones
                            if habitaciones==1:
                                lista_inmuebles[garaje] = True
                            else:
                                lista_inmuebles[garaje] = False
                            lista_inmuebles["zona"] = zona.upper()
                            lista_inmuebles["estado"] = "Disponible"
                            print(lista_inmuebles)
                            datos_correctos["correcto"]=True
                        






        
        
        
        
        
        