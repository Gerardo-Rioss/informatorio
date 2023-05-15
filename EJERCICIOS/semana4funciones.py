# 1
""" def suma(num1, num2):
    suma= num1+num2
    return suma

print("La suma es",suma(3,5)) """

# 2
""" def saludo(nombre):
    return "Hola "+nombre+" como estas?"
    
print(saludo("Gera")) """

# 3
""" def invertir_cadena(texto):
    return texto[::-1]
print(invertir_cadena("Gerardo")) """

# 4
""" def es_capicua(numero):
    if numero == numero[::-1]:
        return True
    else:
        return False    

print(es_capicua("232"))
 """
# 5
""" def es_divisible(num1,num2):
    if num1%num2 ==0 :
        return "Es divisible"
    else:
        return "No es divisible"
print(es_divisible(4,2))
 """
# 6
""" def es_par(numero):
    if numero%2==0:
        return "ES PAR"
    else:
        return "NO ES PAR"
    
print(es_par(11)) """

# 7
""" def imprimir_pares(numero):
    for i in range(1,numero+1):
        if i %2 ==0:
            return i
print(imprimir_pares(20)) """

# 8
""" def es_palindromo(texto):
    if texto == texto[::-1]:
        return "ES PALINDROMO"
    else:
        return "NO ES PALINDROMO"
print(es_palindromo("ror")) """

# 9
""" def promedio(lista_numeros):
    suma =0
    for i in range(0,len(lista_numeros)):
        suma+= lista_numeros[i]     
    return suma / len(lista_numeros) 
print(promedio([10,30,45])) """

# 10
""" def calcular_factorial(numero):
    factorial= numero
    for i in range(numero -1,0,-1):
        factorial = factorial * i
    return factorial
print(calcular_factorial(5)) """

# 11
""" def contar_vocales(texto):
    vocales = "aeiou"
    suma = 0
    for letra in texto:
        if letra.lower() in vocales:
            suma += 1
    return suma

print(contar_vocales("Gerardo German Rios"))
 """

 # 12
""" def convertir_temperatura(temperatura):
    return (temperatura*9/5)+32
print(convertir_temperatura(30)) """

# 13
""" def calcular_descuento(precio, porcentaje_descuento):
    return precio-(precio*porcentaje_descuento)/100
print(calcular_descuento(300,20)) """

# 14
""" def encontrar_maximo(lista_numeros):
    return max(lista_numeros)
print(encontrar_maximo([10,5,2,40,100]))     """

# 15
""" def contar_palabras(texto):
    return len(texto.split())
print(contar_palabras("Hola como estas")) """

# 16
""" def eliminar_duplicados(lista):
    lista_nueva=[]
    for elemento in lista:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva
print(eliminar_duplicados([100,30,50,100,300,350,40,350])) """

# 17
""" def es_anagramas(texto1,texto2):
    lista_texto1 = list(texto1)
    lista_texto2 = list(texto2)
    lista_texto1.sort()
    lista_texto2.sort()
    if lista_texto1 == lista_texto2:
        return True
    else:
        return False """

# 18
""" def calcular_mayor_diferencia(numeros):
    return max(numeros)-min(numeros)
print(calcular_mayor_diferencia([100,30,15,150,2])) """

# 19
def es_bisiesto(anio):
    if (anio % 4 ==0 and not anio % 100 ==0 ) :
        return ("ES BISIESTO")
        if not anio % 100 == 0 and anio % 400 == 0:
            return ("ES BISIESTO")
    else:
        return ("NO ES BISIESTO")

print(es_bisiesto(2023))