def agregar_inmueble(lista, inmueble):
    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("El inmueble ha sido agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def editar_inmueble(lista, indice, datos_actualizados):
    if indice >= 0 and indice < len(lista):
        inmueble = lista[indice]
        inmueble.update(datos_actualizados)
        if validar_inmueble(inmueble):
            lista[indice] = inmueble
            print("El inmueble ha sido editado correctamente.")
        else:
            print("El inmueble actualizado no cumple con las reglas de validación.")
    else:
        print("El índice del inmueble a editar es inválido.")

def eliminar_inmueble(lista, indice):
    if indice >= 0 and indice < len(lista):
        del lista[indice]
        print("El inmueble ha sido eliminado correctamente.")
    else:
        print("El índice del inmueble a eliminar es inválido.")

def cambiar_estado(lista, indice, nuevo_estado):
    if indice >= 0 and indice < len(lista):
        inmueble = lista[indice]
        inmueble["estado"] = nuevo_estado
        lista[indice] = inmueble
        print("El estado del inmueble ha sido cambiado correctamente.")
    else:
        print("El índice del inmueble es inválido.")

def buscar_inmuebles_por_presupuesto(lista, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista:
        if inmueble["estado"] in ["Disponible", "Reservado"]:
            precio = calcular_precio(inmueble)
            if precio <= presupuesto:
                inmueble_con_precio = inmueble.copy()
                inmueble_con_precio["precio"] = precio
                inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados

def validar_inmueble(inmueble):
    if inmueble["zona"] not in ["A", "B", "C"]:
        return False
    if inmueble["estado"] not in ["Disponible", "Reservado", "Vendido"]:
        return False
    if inmueble["año"] < 2000:
        return False
    if inmueble["metros"] < 60:
        return False
    if inmueble["habitaciones"] < 2:
        return False
    return True

def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble["año"]
    metros = inmueble["metros"]
    habitaciones = inmueble["habitaciones"]
    garaje = 1 if inmueble["garaje"] else 0
    zona = inmueble["zona"]
    
    
