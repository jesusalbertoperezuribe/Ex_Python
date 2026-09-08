#en este archivo quise solo poner las validaciones


def datoscorrectos(nombremateriaoactividad, diadelasemana, horadeinicio, horadefin, decirubicacion, lista_materias, materia_ignorada=None):
#la validacion de la hora para no tener conflitos y lo importante ser logicos 
    if horadeinicio >= horadefin:
        print("Error: La hora de inicio no puede ser igual ni más tarde que la hora de fin.")
        return False
#este es un buqle para los datos del ususario de la materia 
    for materia_guardada in lista_materias:
        #aqui hacemos que no haya problema con las materias modificadas y se mira lo del mismo dia
        if materia_ignorada and materia_guardada["materia"].lower() == materia_ignorada.lower() and materia_guardada["dia"].lower() == diadelasemana.lower():
            continue
        #aqui hacemos lo mismo pero no para modificar sino para cuando se esta creando y asi no repetir nombre el mismo dia
        if materia_guardada["materia"].lower() == nombremateriaoactividad.lower() and materia_guardada["dia"].lower() == diadelasemana.lower():
            print(f"Error: La materia '{nombremateriaoactividad}' ya está registrada el {diadelasemana}.")
            return False
#en esta ultima miramos las horas sirve para registro nuevo y moficaciones miramos que en el mismo dia no haya materias con el mismo horario
        if materia_guardada["dia"].lower() == diadelasemana.lower():
            if horadeinicio < materia_guardada["hora_fin"] and horadefin > materia_guardada["hora_inicio"]:
                print(f"Error: El horario choca con {materia_guardada['materia']} de {materia_guardada['hora_inicio']} a {materia_guardada['hora_fin']}.")
                return False

    return True