opcion = 0    #Variable para el menú 
calificaciones = []  #lista vacía


while opcion != 5:  #bucle while para navegar en el menú. 

    print (" ")
    print ("Bienvenido al menú de cálculo de notas.")
    print ("1. Determinar el estado de aprobación.")
    print ("2. Calcular el promedio.")
    print ("3. Contar calificaciones mayores.")
    print ("4. Verificar y contar calificaciones específicas.")
    print ("5. Salir.")
    print (" ")
    
    try: #usamos el Try para el manejo de errores y/o exepciones que se encuentren en la digitación de la navegación 
        opcion = int(input ("Por favor digite una de las opciones del menú: ")) # ingreso de variantes para navegar en el menú
    except ValueError:  
        print (" ")
        print("Error, ingrese un número válido.") # Expone un valor diferente dentro de las posibilidades de navegación. 
        continue #posibilita navegación 
    
    if (opcion == 1): #el usuario marcó 1
        calificacion = int(input("Ingrese por favor la calificación: "))
        if (calificacion >= 75): #condición de aprobación. para aprobar la calificación debe ser mayor o igual a 75
            print("Estudiante aprobó la materia, su calificación fue de: ",calificacion)
        else: #De lo contrario pierde la materia.
            print("Estudiante perdió la materia, su calificación fue de: ",calificacion)

    if (opcion == 2): #el usuario marcó 2
        entrada = input("Ingrese sus calificaciones separadas por comas (,): ")
        calificaciones = [float(x.strip()) for x in entrada.split(',')]  #el .strip: divide la cadena en una lista. #.split: elimina los espacios en blanco
        for i in calificaciones: 
                if i < 0 or i > 100: #se le asigna un limite mínimo y máximo a la variable.
                    print("Calificación no válida")
        promedio= sum(calificaciones) / len(calificaciones) #función sum me ayuda a ahorrar código #len para hacer el conteo dentro de la lista.
        promedio = round(promedio, 2) #round: ayuda a redondear a dos números décimales.
        print("Su promedio es: ", promedio)
        print (" ")

    if (opcion == 3): #el usuario marcó 3
        if not calificaciones: #el if not: Si NO cumple con la condición, entonces: 
            print (" ")
            print("La lista está vacía, es obligatorio realizar la opción 2.")
        else:    
            print (" ")
            valorEspecifico = int(input("Ingrese el valor específico que está buscando: "))
            contador = 0
            for calificacion in calificaciones:
                if calificacion > valorEspecifico:   #en esta iteración busca un valor especifico
                    contador += 1 #y muestra/cuenta los números mayores a x  (num ingresado)
            print (" ") 
            print("Las calificaciones mayores a",valorEspecifico, "son:",contador)


    if opcion == 4: #el usuario marcó 4
        if not calificaciones:
            print (" ")
            print("La lista está vacía, es obligatorio realizar la opción 2.")
        else:
            print(" ")
            buscar = int(input("Ingresa la calificación que deseas buscar: "))
            contador = 0
            for i in calificaciones:
                if i == buscar:
                    contador += 1 #cuenta cuantas veces se encuentra x en la lista y lo agrega a la variable contador:
            print(" ")
            if contador > 0:
                print(f"La calificación {buscar} aparece {contador} veces.")
            else:
                print(f"La calificación {buscar} no está en la lista.")

    if (opcion == 5):  #finaliza con el programa 
        print(" ")
        print("Adiós!")
        print(" ")
        break