# 1 
""" palabra = input("Ingrese una palabra: ")
for letra in palabra:
    print(letra) """

# 2
""" numero =int(input("ingrese un numero: "))
i = 1
suma = 0
while i <= numero:
    suma += i
    i += 1
else:
    print("El valor de la suma es:",  suma) """

# 3 
""" numero = int(input("Ingrese un valor: "))
for i in range(11):
    print(i,"x", numero,"=", i*numero) """

# 4
""" for i in range(100):
    if i%2 == 0 and i !=0:
        print(i) """

# 5
""" suma = 0
for i in range(2,101,2):
    suma += i
print ("La suma de todos los numeros pares es: ", suma) """

# 6
""" palabra= input("Ingrese una palabra: ")
print(palabra[::-1]) """

# 7
""" palabra= input("Ingrese una palabra: ")
if palabra == palabra[::-1]:
    print("La palabra es palindrono")
else:
    print("La palabra no es palindrono") """
 
# 8 
""" texto = input("Ingrese el texto: ")
print("Su texto contiene:", len(texto.split()),"palabras.-") """

# 9
""" numero = int(input("Ingrese un numero: "))
fibonacci = [1,2]
for nun in range (2,numero):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci) """

# 10
""" texto = input("Ingrese texto: ")
vocales = "aeiou"
for letra in texto:
    if letra.lower() in vocales:
        texto= texto.replace(letra,letra.upper())
print(texto)         """

# 11
""" numero = int(input("Ingrese el valor a calcular el factorial: "))
factorial = numero
for num in range(numero -1 ,0,-1):
    factorial = factorial * num 
print("El factorial es:", factorial) """

# 12
""" numeros = input("Ingrese la lista de numeros separados por coma: ")
print("El promedio del valor es:", round(sum([float(num) for num in (numeros.split(","))])/ float(len(numeros.split(","))) , 2)) """

# 13
""" numero = int(input("Ingrese un numero: "))
asteriscos = []
for num in range(0,numero):
    asteriscos.append("*")
    print("".join(asteriscos))
 """
#14
""" numero = int(input("Ingrese un valor: "))
valor = 1
for i in range(1,numero+1):
    for n in range(1, i+1):
        print(valor, end="")        
    print()
    valor = valor + 1 """

#15
texto = input("Ingrese un texto: ")
letras_controladas =  [""]
for letra in texto:
    if letra not in letras_controladas:
        print("La letra:",letra,"se repite:", texto.count(letra))
        letras_controladas.append(letra)
  