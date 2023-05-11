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
def contar_vocales(texto):
    vocales = "aeiou"
    suma = 0
    for letra in texto:
        if letra.lower() in vocales:
            suma += 1
    return suma

print(contar_vocales("Gerardo German Rios"))
