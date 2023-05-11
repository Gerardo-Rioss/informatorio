# Desafío entregable 3: Adivina el número

# Importamos el modulo randon para poder generar el numero aleatorio
import random

# creamos una tupla con los intentos
intentos = ("Primer","Segundo","Tercer","Cuarto","Quinto","Sexto","Septimo","Optavo y ultimo")
# Al iniciar el juego el numero de intentos comienza con el 1 que seria el primer intento
numero_intento = 1
# Generamos el nro aleatorio y lo asignamos a la variable 
numero_aleatorio = random.randint(1,100)
# Mostramos al usuario el msj de bienvenida y explicamos de que se trata el juego
print("Bienvenido al juego.-")
print("Debe adivinar un numero entre 1 y 100.-")
print("Tiene 8 intentos, Buena Suerte !!!")
# msj de que numero de intento y pedimos que eliga un numero 
print(intentos[0], "intento")
numero_elegido = input("Eliga el número: ")

# creamos una estructura pepetitiva que salga cuando se le termine los intentos
while numero_intento < 8:
   #controlamos que el nro ingresado no este vacio
   if numero_elegido!="":
      #controlamos que el caracter ingresado se puede convertir en entero
      if numero_elegido.isdigit() == True:         
         #convertimos el caracter ingresado a entero
         numero_elegido= int(numero_elegido)
         #controlamos que este dentro del rango entre 1 y 100
         if numero_elegido>=1 and numero_elegido<=100: 
            #controlamos si es mayor menor o igual y mostramos los msj correspondientes
            if numero_elegido> numero_aleatorio:
               print("El numero que eligio es MAYOR al que tiene que adivinar.-")
            elif numero_elegido< numero_aleatorio:
               print("El numero que eligio es MENOR al que tiene que adivinar.-")
            else:
               print("FELICITACIONES, adivino el valor en el", intentos[numero_intento-1],"intento.-")
               break   
            # actualizamos el nro de intentos y pedimos un nuevo numero
            numero_intento += 1
            print(intentos[numero_intento-1], "intento")            
            numero_elegido = input("Eliga el número: ")
         else:        
            # actualizamos datos y msj de error porque no esta dentro del rango solicitado
            numero_intento += 1
            print("ERROR, El numero ingresado tiene que ser entre 1 y 100.-")   
            print(intentos[numero_intento-1],"intento")
            numero_elegido = input("Eliga el número: ")
      else:      
         # actualizamos datos y msj de error porque no ingreso un numero que se pueda convertir a entero
         print("ERROR, tiene que ingresar un valor entero.-")
         print(intentos[numero_intento-1], "intento")
         numero_elegido = input("Eliga el número: ")
   else:
      # actualizamos datos y msj de error porque no ingreso ningun valor, esta vacio
      numero_intento += 1
      print("ERROR, Debe ingresar un valor.-")
      numero_elegido = input("Eliga el número: ")
else:   
   # actualizamos datos y msj comunicando que termino la cantidad de intentos y mostramos el valor que tenia que haber adivinado
   print("Se ha terminado la cantidad de intentos.-")
   print("El numero que tenia que adivinar es:", numero_aleatorio)

# Tourn Paula
# Alarcon Jorge
# Morla Lucas
# Bullon Rene
# Romero Benjamin
# Aguirre Mauricio
# Boscarino Juan Esteban
# Sanchez Faby
# Rios Gerardo

