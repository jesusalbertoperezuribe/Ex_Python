#importe los dos otros que tengo en la carpeta
import caja_de_herramientas
import caja_de_policia

# llamo a los datos del json 
lista_materias = caja_de_herramientas.cargar_datos()

#aqui empece un ciclo para el menu
activo = True
while activo: 
    print("1. Registrar materia o actividad")
    print("2. Ver el horario semanal")
    print("3. Modificar una materia o actividad")
    print("4. Eliminar una materia o actividad")
    print("5. Generar reporte del horario")
    print("6. Salir")

    # si el usuario pone texto y no el numero genera error
    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        continue

#aqui empece con el menu de registro
    if opcion == 1:
        nombremateriaoactividad = input("Ingrese el nombre de la materia o actividad: ")
        diadelasemana = input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes): ")
        horadeinicio = input("Ingrese la hora de inicio (Formato 24H - Ejemplo: 14:00): ")
        horadefin = input("Ingrese la hora de fin (Formato 24H - Ejemplo: 16:00): ")
        
        # estas lineas son para que si queda vacio genere un error y le diga al usuario
        if len(nombremateriaoactividad.strip()) == 0 or len(diadelasemana.strip()) == 0 or len(horadeinicio.strip()) == 0 or len(horadefin.strip()) == 0:
            print("\nError: El nombre, el día y las horas son obligatorios. Debes colocar algo válido y no solo espacios.")
            continue 

        decirubicacion = input("Ingrese la ubicación (opcional, presione ENTER para omitir): ")
        if decirubicacion.strip() == "":
            decirubicacion = "sin ubicación"
#aqui llamo a las validaciones
        if caja_de_policia.datoscorrectos(nombremateriaoactividad, diadelasemana, horadeinicio, horadefin, decirubicacion, lista_materias):
            nueva_materia = {
                "materia": nombremateriaoactividad,
                "dia": diadelasemana,
                "hora_inicio": horadeinicio,
                "hora_fin": horadefin,
                "ubicacion": decirubicacion
            }
            lista_materias.append(nueva_materia)
            caja_de_herramientas.guardar_datos(lista_materias)
            print(f"\nMateria '{nombremateriaoactividad}' registrada exitosamente el {diadelasemana} de {horadeinicio} a {horadefin} en {decirubicacion}.")
        else:
            print("\nLos datos no son correctos. No se puede registrar la materia.")
#se empiesa a imprimir el horario
    elif opcion == 2:
        caja_de_herramientas.ver_horario_semanal(lista_materias)
#la opcion tres es para modificar lo que el usuario ingreso en el horario
    elif opcion == 3:
        nombre_modificar = input("Ingrese el nombre de la materia o actividad a modificar: ")
        
        if len(nombre_modificar.strip()) == 0:
            print("\nError: Debes ingresar el nombre de la materia a modificar.")
            continue

        materia_encontrada = None
        
        #se hace un cliclo para recorrer materias y buscar la que el usuario quiere modificar
        for m in lista_materias:
            if m["materia"].lower() == nombre_modificar.lower():
                materia_encontrada = m
                break
                
        if materia_encontrada:
            nuevo_dia = input("Ingrese el nuevo día de la semana: ")
            nueva_inicio = input("Ingrese la nueva hora de inicio: ")
            nueva_fin = input("Ingrese la nueva hora de fin: ")
            
            if len(nuevo_dia.strip()) == 0 or len(nueva_inicio.strip()) == 0 or len(nueva_fin.strip()) == 0:
                print("\nError: El día y las horas nuevas no pueden quedar vacías.")
                continue

            nueva_ubicacion = input("Ingrese la nueva ubicación (ENTER para mantener la misma): ")
            if nueva_ubicacion.strip() == "":
                nueva_ubicacion = materia_encontrada["ubicacion"]
#vuelvo a traer validaciones ya que aqui el usuario tambien ingresa datos
            if caja_de_policia.datoscorrectos(nombre_modificar, nuevo_dia, nueva_inicio, nueva_fin, nueva_ubicacion, lista_materias, materia_ignorada=nombre_modificar):
                materia_encontrada["dia"] = nuevo_dia
                materia_encontrada["hora_inicio"] = nueva_inicio
                materia_encontrada["hora_fin"] = nueva_fin
                materia_encontrada["ubicacion"] = nueva_ubicacion
                #si todo es correto traigo para guardar en la lista de materias
                caja_de_herramientas.guardar_datos(lista_materias)
                print(f"\nMateria '{nombre_modificar}' modificada exitosamente a {nuevo_dia} de {nueva_inicio} a {nueva_fin} en {nueva_ubicacion}.")
            else:
                print("\nNo se pudo modificar debido a conflictos de horario.")
        else:
            print(f"\nError: No se encontró la materia '{nombre_modificar}' en el horario.")
#la opcion cuatro es eliminar una materia
    elif opcion == 4:
        nombre_eliminar = input("Ingrese el nombre de la materia o actividad que desea eliminar: ")
        dia_eliminar = input("Ingrese el día de la semana: ")
        
        if len(nombre_eliminar.strip()) == 0 or len(dia_eliminar.strip()) == 0:
            print("\nError: Debes colocar un nombre y un día válidos.")
            continue
        #ya el usuario habiendo ingresado lo que quiere eliminar hacemos el bucle para esta accion
        encontrado = False
        for i in range(len(lista_materias)):
            if lista_materias[i]["materia"].lower() == nombre_eliminar.lower() and lista_materias[i]["dia"].lower() == dia_eliminar.lower():
                lista_materias.pop(i) 
                caja_de_herramientas.guardar_datos(lista_materias)
                print(f"\nLa materia '{nombre_eliminar}' ha sido eliminada del horario del día {dia_eliminar}.")
                encontrado = True
                break
                
        if not encontrado:
            print("\nError: No se encontró esa materia en el día especificado.")
#la ocpcion 5 es para generar el formato json
    elif opcion == 5:
        caja_de_herramientas.generar_reporte(lista_materias)
#aqui el activo lo vuelvo negativo
    elif opcion == 6:
        print("\nSaliendo del programa...")
        activo = False
        
    else:
        print("\nOpción no válida. Por favor, ingrese una opción del 1 al 6.")