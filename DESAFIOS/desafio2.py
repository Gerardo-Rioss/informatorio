# Se pide al usuario que ingrese los datos
texto = input("Ingrese el texto, articulo o frase: ")
tres_letras = input("Ingrese tres letras separadas por coma: ")

# PARTE 1
# se crea la lista de las tres letras ingresadas 
lista_tres_letras = (tres_letras.lower()).split(",")

# se controla la cantidad de veces que se repite las letras en el texto
print("La letra",lista_tres_letras[0],"se repite",(texto.lower()).count(lista_tres_letras[0]),"veces.-")
print("La letra",lista_tres_letras[1],"se repite",(texto.lower()).count(lista_tres_letras[1]),"veces.-")
print("La letra",lista_tres_letras[2],"se repite",(texto.lower()).count(lista_tres_letras[2]),"veces.-")

# PARTE 2
# Cantidad de palabras en el texto
print("En el texto hay", len(texto.split()),"palabras.-")

# PARTE 3
# Con que letra empieza y termina
print("La primer letra del texto es:", texto[0],"y la ultima es", texto[-1])

# PARTE 4 
# Orden inverso del texto 
print("El texto en orden inverso es:", texto[::-1])

# PARTE 5
#Diccionario para controlar si se encuentra la palabra python en el texto
palabra_python ={
    "estado" : False
}
# Cambia el estado en el diccionario si encuentra la palabra
if "python" in texto.lower():
    palabra_python["estado"]= True
# Muestra el msj
if palabra_python["estado"] ==True:
    print("La frase contiene la palabra PYTHON")
