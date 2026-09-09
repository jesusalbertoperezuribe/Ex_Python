#sin esta linea no funciona nada jajaja solo la traigo a la caja que hice que tuviera las operaciones con los datos
import json

#con esta funcion el json me da su contenido y para que no se caiga el programa , por eso el encoding se utiliza para que no haya problemas con acentos y ñ el try except es para que no se caiga el programa y si no hay archivo que lo cree vacio 
def cargar_datos():
    try:
        with open("horario.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return []

#la funcion de guardar datos me sirve para modificaciones y llevarlos al json
def guardar_datos(lista_materias):
    try:
        with open("horario.json", "w", encoding="utf-8") as archivo:
            datos_json = json.dumps(lista_materias, indent=4, ensure_ascii=False)
            archivo.write(datos_json)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

#esta funcion es impresion del horario 
def ver_horario_semanal(lista_materias):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horas_set = set()
    for m in lista_materias:
        horas_set.add(m["hora_inicio"])
    horas = sorted(list(horas_set))

    if not horas:
        print("\nEl horario está vacío. Registre materias primero.")
        return
# el codigo la gran mayoria es estetica,espacios y tratando de hacer un cuadro bonito para que se vea mejor el horario
    print("\n========================================================================================================")
    print(f"| {'Hora':<10} | {'Lunes':<15} | {'Martes':<15} | {'Miércoles':<15} | {'Jueves':<15} | {'Viernes':<15} |")
    print("========================================================================================================")
#este bucle recorre toda la informacion del json para imprimierla en orden
    for hora in horas:
        fila = f"| {hora:<10} |"
        for dia in dias:
            encontrado = False
            for m in lista_materias:
                if m["dia"].lower() in [dia.lower(), dia.lower().replace('é', 'e')] and m["hora_inicio"].upper() == hora.upper():
                    fila += f" {m['materia'][:14]:<15} |"
                    encontrado = True
                    break
            if not encontrado:
                fila += f" {'Libre':<15} |"
        print(fila)

    print("========================================================================================================\n")
#la funcion para reportes que es la opcion 5
def generar_reporte(lista_materias):
    #traigo los datos
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    #creo la lista donde pondre los reportes
    reporte = []
#lujo
    print("\n==========================================")
    print("REPORTE DEL HORARIO SEMANAL")
    print("==========================================")
#se crea un bucle que recorra los dias y busque las materias que correspondan a ese dia, si encuentra alguna la agrega a la lista de eventos del dia, luego ordena los eventos por hora de inicio y los agrega al reporte, finalmente imprime el reporte en consola y lo guarda en un archivo json
#el for de abajo hace el reporte ordenado
    for dia in dias:
        eventos_dia = []
        for m in lista_materias:
            if m["dia"].lower() in [dia.lower(), dia.lower().replace('é', 'e')]:
                eventos_dia.append({
                    "materia": m["materia"],
                    "hora_inicio": m["hora_inicio"],
                    "hora_fin": m["hora_fin"],
                    "ubicacion": m["ubicacion"]
                })
        #este if es para que si no hay eventos en ese dia no lo agregue al reporte y no lo imprima
        if eventos_dia:
            eventos_dia = sorted(eventos_dia, key=lambda x: x["hora_inicio"])
            reporte.append({
                "dia": dia,
                "eventos": eventos_dia
            })

            print(f"{dia}:")
            for e in eventos_dia:
                print(f" - {e['materia']} ({e['hora_inicio']}-{e['hora_fin']}) en {e['ubicacion']}")
            
            input("Presione ENTER para continuar...")
#este try except es para que no se caiga el programa y si no hay archivo que lo cree vacio
    try:
        with open("reporte_horario.json", "w", encoding="utf-8") as archivo:
            archivo.write(json.dumps(reporte, indent=4, ensure_ascii=False))
        print("\n¡Reporte JSON generado exitosamente como 'reporte_horario.json'!")
    except Exception as e:
        print(f"Error al guardar el reporte: {e}")

# --- FUNCIONALIDAD NUEVA: BUSCADOR ---
# def buscar_en_horario(lista_materias, tipo_busqueda, valor_buscado):
#     print(f"\n==========================================")
#     print(f"RESULTADOS DE BÚSQUEDA: {valor_buscado.upper()}")
#     print(f"==========================================")
#     encontrado = False
#     for m in lista_materias:
#         # Comparamos ignorando mayúsculas/minúsculas
#         if valor_buscado.lower() in m[tipo_busqueda].lower():
#             print(f" - {m['materia']} | {m['dia']} | {m['hora_inicio']} a {m['hora_fin']} | {m['ubicacion']}")
#             encontrado = True
#     
#     if not encontrado:
#         print(f"No se encontraron resultados para su búsqueda.")
#     print("==========================================\n")
# --- FUNCIONALIDAD: VACIAR HORARIO ---
# def vaciar_horario(lista_materias):
#     # El método .clear() vacía la lista por completo
#     lista_materias.clear() 
#     guardar_datos(lista_materias)
#     print("\n==========================================")
#     print("¡El horario ha sido borrado por completo!")
#     print("==========================================\n")
# import csv # (NO OLVIDES QUITARLE EL # Y PONERLO AL INICIO DEL ARCHIVO)

# --- FUNCIONALIDAD: EXPORTAR A EXCEL (CSV) ---
# def exportar_a_csv(lista_materias):
#     if len(lista_materias) == 0:
#         print("\nEl horario está vacío, no hay nada que exportar.")
#         return
#     
#     # Definimos los encabezados (keys del diccionario)
#     encabezados = ["materia", "dia", "hora_inicio", "hora_fin", "ubicacion"]
#     
#     try:
#         # newline='' evita saltos de línea extra en Windows
#         with open("horario_excel.csv", "w", newline='', encoding="utf-8") as archivo_csv:
#             escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
#             escritor.writeheader() # Escribe la primera fila con los títulos
#             for m in lista_materias:
#                 escritor.writerow(m) # Escribe cada materia
#         print("\n¡Exportación exitosa! Busca el archivo 'horario_excel.csv' y ábrelo con Excel.")
#     except Exception as e:
#         print(f"Error al exportar a CSV: {e}")
# --- FUNCIONALIDAD: ESTADÍSTICAS SIMPLES ---
# def mostrar_estadisticas(lista_materias):
#     total_clases = len(lista_materias)
#     if total_clases == 0:
#         print("\nNo tienes materias registradas para mostrar estadísticas.")
#         return
#
#     # Diccionario para agrupar cuántas clases hay por día
#     conteo_por_dia = {}
#     for m in lista_materias:
#         dia = m["dia"].capitalize()
#         if dia in conteo_por_dia:
#             conteo_por_dia[dia] += 1
#         else:
#             conteo_por_dia[dia] = 1
#
#     print("\n==========================================")
#     print(f"ESTADÍSTICAS DEL HORARIO")
#     print("==========================================")
#     print(f"Total de clases registradas: {total_clases}")
#     print("\nClases por día:")
#     # iteramos el diccionario usando .items()
#     for dia, cantidad in conteo_por_dia.items():
#         print(f" - {dia}: {cantidad} clase(s)")
#     print("==========================================\n")