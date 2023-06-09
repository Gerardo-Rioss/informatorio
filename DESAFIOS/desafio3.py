# Desafío entregable 3: Adivina el número

# Importamos el modulo randon para poder generar el numero aleatorio
import random
# creamos una tupla con los intentos
intentos = ("Primer","Segundo","Tercer","Cuarto","Quinto","Sexto","Septimo","Octavo y ultimo")
# Al iniciar el juego el numero de intentos comienza con el 1 que seria el primer intento
numero_intento = 0
lista_numeros_elegidos = []
# Generamos el nro aleatorio y lo asignamos a la variable 
numero_aleatorio = random.randint(1,100)
# Mostramos al usuario el msj de bienvenida y explicamos de que se trata el juego
print("---------------------------------------")
print("        Bienvenido al juego")
print("Debe adivinar un numero entre 1 y 100.-")
print("  Tiene 8 intentos, Buena Suerte !!!")
print("---------------------------------------")
# Pedimos que ingrese su nombre
nombre = input("Ingrese su nombre: ")
# En este while controlamos que siga pidiendo que ingrese el nombre mientras ingrese no ingrese el nombre o ingrese solo numeros
while nombre.isspace() or nombre =="" or nombre.isdigit():
   # Mensaje de error y pide que vuelva a ingresar su nombre hasta que ingrese los datos correctos
   print("-------------------------------------------------")
   print("##########  ERROR, datos incorrectos  ##########")
   print("-------------------------------------------------")
   nombre = input("Ingrese su nombre:")
else:
# creamos una estructura pepetitiva que salga cuando se le termine los intentos
   while numero_intento <= 7:
      # msj de que numero de intento restantes, intento actual y pedimos que eliga un numero 
      print("                                                                               ")
      print("======== Intentos restantes:",7-numero_intento, "========")
      print("--------------------------------------------")
      print("         ",intentos[numero_intento], "intento         ")
      # contamos el intento
      numero_intento +=1
      numero_elegido = input("Eliga el número: ")            
      #controlamos que el caracter ingresado se puede convertir en entero
      if numero_elegido.isdigit() == True:
         #convertimos el caracter ingresado a entero
         numero_elegido= int(numero_elegido)
         #controlamos que este dentro del rango entre 1 y 100
         if numero_elegido>=1 and numero_elegido<=100: 
            # Controla si volvio a repetir el numero ingresado
            if numero_elegido in lista_numeros_elegidos:
               print("                                                                               ")
               print("============      ESTE NUMERO YA LO ELIGIO, INGRESE NUEVAMENTE      ============")
               print("-------------------------------------------------------------------------------")
               numero_intento -= 1
            else:
               # Si es un numero nuevo lo agregamos en la lista para el control si repite el valor
               lista_numeros_elegidos.append(numero_elegido)
               #controlamos si es mayor menor o igual y mostramos los msj correspondientes
               if numero_elegido> numero_aleatorio:
                  print("El numero que eligio es MAYOR al que tiene que adivinar.-")
               elif numero_elegido< numero_aleatorio:
                  print("El numero que eligio es MENOR al que tiene que adivinar.-")
               else:
                  print("                                                                               ")
                  print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                  print("         FELICITACIONES",nombre,"adivinaste el valor en el", intentos[numero_intento-1],"intento.         ")
                  print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                  break
         else:     
            # Mensaje de error si ingresa un valor fuera del rango pedido   
            print("ERROR, El numero ingresado tiene que ser entre 1 y 100.-")                         
      else:
         # Mensaje de error porque no ingreso un numero que se pueda convertir a entero
         print("ERROR, tiene que ingresar un valor entero.-")
         # como no debemos descontar el intento lo volvimos al valor con el cual inicio el bucle
         numero_intento -=1         
   else:   
      # Mensaje comunicando que termino la cantidad de intentos y mostramos el valor que tenia que haber adivinado con su nombre ingresado
      print("                                                                          ")
      print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print("          ",nombre,", se te ha terminado la cantidad de intentos.-")
      print("                El numero que tenia que adivinar es:", numero_aleatorio,"         ")
      print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   

# Tourn Paula
# Alarcon Jorge
# Morla Lucas
# Bullon Rene
# Romero Benjamin
# Aguirre Mauricio
# Boscarino Juan Esteban
# Sanchez Faby
# Rios Gerardo

