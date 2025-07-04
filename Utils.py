# -------------- Inicializadores
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """
    Crea una matriz.
    
    Args:
        cantidad_filas: Es la cantidad de filas q tendra la matriz.
        cantidad_columnas: Es la cantidad de columnas q tendra la matriz.
        valor_inicial: Es el valor de cada elemento de la matriz.
    Returns:
        list: Retorna una lista de listas (matriz).
    """

    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz



# -------------- Prints
def imprimir_menu():
    """
    Imprime el menu de opciones.
    """
    print("Menú de opciones:")
    print("1 - Cargar notas de estudiantes.")
    print("2 - Mostrar estudiantes.")
    print("3 - Calcular promedio de alumnos.")
    print("4 - Ordenar promedios DESC.")
    print("5 - Calcular promedios de materias.")
    print("6 - Buscar datos de un estudiante por legajo.")
    print("7 - Buscar cantidad de notas por materia.")
    print("8 - Salir.")
    print("")

def imprimir_todos_los_datos(matriz_notas:list, lista_nombres:list, lista_generos:list, lista_legajos:list, lista_promedios:list):
    """
    Imprime tdos los datos de los alumnos.
    
    Args:
        matriz_notas: Son las notas de las materias de los alumnos.
        lista_nombres: Es la lista de nombres de los alumnos.
        lista_generos: Es la lista con los generos de cada alumno.
        lista_legajos: Es la lista con los legajos de cada alumno.
    Returns:
        None.
    """

    print(f"{'ESTUDIANTE':<17}{'|LEGAJO':<10}{'|GENERO':<10}{'|NOTAS':<30}{'|PROMEDIO'}")
    for i in range(len(matriz_notas)):
        print(f"{lista_nombres[i]:<17}", end="| ")
        print(f"{lista_legajos[i]:<8}", end="| ")
        print(f"{lista_generos[i]:<8}",  end="| ")

        for j in range(len(matriz_notas[i])):
            print(f"{matriz_notas[i][j]:<4}", end="| ")
        
        print(f"{lista_promedios[i]:<8}", end="| ")
        print("")
    print("")
    

def imprimir_datos_alumno(lista_datos_del_alumno:list):
    """
    Imprime la informacion de un alumno.
    
    Args:
        lista_datos_del_alumno: Lista con los datos de cada alumno.
    """
    print(f"{'ESTUDIANTE':<11}{'|LEGAJO':<13}{'|GENERO':<13}{'|NOTAS':<65}{'|PROMEDIO'}")
    for i in range(len(lista_datos_del_alumno)):
        print(f"{lista_datos_del_alumno[i]:<11}", end="| ")
    print("")

def imprimir_datos_materia(lista_notas_de_materia:list):
    """
    Imprime la cantidad de las distintas notas de una materia.
    
    Args:
        lista_notas_de_materia: Lista con la cantidad de las distintas notas.
    """
    for i in range(len(lista_notas_de_materia)):
        print(f"Notas_con_{i+1}: {lista_notas_de_materia[i]}")
    print("")

def imprimir_promedios_materias(lista_promedios_materias:list, lista_nombres_materias:list):
    """
    Imprime la o las materias con mayor promedio.
    
    Args:
        lista_promedios_materias: Lista con los promedios de los alumnos.
        lista_nombres_materias: Lista con los nombres de las materias.
    """
    print("Promedios de cada materia:")
    for i in range(len(lista_promedios_materias)):
        print(f"{lista_nombres_materias[i]}:   {lista_promedios_materias[i]}")
    print("")

def imprimir_materia_mayor_promedio(lista_promedios_materias:list, lista_nombres_materias:list):
    """
    Imprime la materia con mayor promedio.
    
    Args:
        lista_promedios_materias: Lista con los promedios de los alumnos.
        lista_nombres_materias: Lista con los nombres de las materias.
    """
    
    mayor_promedio = lista_promedios_materias[0]

    print("Materia/s con mayor promedio:")
    for i in range(0, len(lista_promedios_materias), 1):
        if lista_promedios_materias[i] == mayor_promedio:
            nombre = lista_nombres_materias[i]
            promedio = lista_promedios_materias[i]
            print(f"{nombre}: {promedio}")
        else:
            break 
    print("")

# -------------- Helpers
def to_upper(cadena: str) -> str:
    """
    Convierte una cadena a mayusculas.
    
    Args:
        cadena: Es la cadena q se va a convertir a mayusculas

    Returns:
        str: Retorna la cadena en mayusculas.
    """
    resultado = ""
    
    for caracter in cadena:
        codigo = ord(caracter)
        if codigo >= ord('a') and codigo <= ord('z'):
            mayuscula = chr(codigo - 32)
            resultado += mayuscula
        else:
            resultado += caracter 
    
    return resultado

def to_lower(cadena: str) -> str:
    """
    Convierte una cadena a minusculas.
    
    Args:
        cadena: Es la cadena q se va a convertir a minusculas

    Returns:
        str: Retorna la cadena en minusculas.
    """
    resultado = ""

    for caracter in cadena:
        codigo = ord(caracter)
        if codigo >= ord('A') and codigo <= ord('Z'):
            minuscula = chr(codigo + 32)
            resultado += minuscula
        else:
            resultado += caracter

    return resultado


# -------------- Ordenamiento
def ordenar_promedios(lista_nombres:list, lista_legajos:list, lista_generos:list, matriz_notas:list, lista_promedios:list, modo_ordenamiento = "desc") -> None:
    """
    Ordena los promedios de manera ascendente o descendente
    
    Args:
        lista_promedios: Es la lista con los promedios de cada alumno.
        lista_nombres: Es la lista de nombres de los alumnos.
        modo_ordenamiento: Modo de ordenamiento, puede ser ASC para ascendente o DESC para descendente
    Returns:
        None.
    """
    for i in range(0, len(lista_promedios) - 1, 1):

        for j in range(i + 1, len(lista_promedios), 1):

            # criterio 1: ordenar por promedio ascendente o descendente
            if (lista_promedios[i] > lista_promedios[j] and modo_ordenamiento == "asc") or (lista_promedios[i] < lista_promedios[j] and modo_ordenamiento == "desc"):
                
                aux_nombre = lista_nombres[i]
                lista_nombres[i] = lista_nombres[j]
                lista_nombres[j] = aux_nombre

                aux_legajos = lista_legajos[i]
                lista_legajos[i] = lista_legajos[j]
                lista_legajos[j] = aux_legajos

                aux_generos = lista_generos[i]
                lista_generos[i] = lista_generos[j]
                lista_generos[j] = aux_generos

                aux_notas = matriz_notas[i]
                matriz_notas[i] = matriz_notas[j]
                matriz_notas[j] = aux_notas

                aux_promedio = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = aux_promedio

            # criterio 2: ordenar por nombre ascendente
            elif lista_promedios[i] == lista_promedios[j]:
                if lista_nombres[i] > lista_nombres[j]:

                    aux_nombre = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux_nombre

                    aux_legajos = lista_legajos[i]
                    lista_legajos[i] = lista_legajos[j]
                    lista_legajos[j] = aux_legajos

                    aux_generos = lista_generos[i]
                    lista_generos[i] = lista_generos[j]
                    lista_generos[j] = aux_generos
                    
                    aux_notas = matriz_notas[i]
                    matriz_notas[i] = matriz_notas[j]
                    matriz_notas[j] = aux_notas

                    aux_promedio = lista_promedios[i]
                    lista_promedios[i] = lista_promedios[j]
                    lista_promedios[j] = aux_promedio

def ordenar_promedios_materias_desc(lista_promedios_materias: list, lista_nombres_materias: list):
    for i in range(0, len(lista_promedios_materias) - 1, 1):
        for j in range(i + 1, len(lista_promedios_materias), 1):
            if lista_promedios_materias[i] < lista_promedios_materias[j]:

                aux_prom = lista_promedios_materias[i]
                lista_promedios_materias[i] = lista_promedios_materias[j]
                lista_promedios_materias[j] = aux_prom

                aux_nombre = lista_nombres_materias[i]
                lista_nombres_materias[i] = lista_nombres_materias[j]
                lista_nombres_materias[j] = aux_nombre


def buscar_materias_con_mayor_promedio(lista_promedios_materias: list, lista_nombres_materias: list):
    ordenar_promedios_materias_desc(lista_promedios_materias, lista_nombres_materias)




#buscar_estudiante_por_legajo.
def buscar_estudiante_por_legajo(legajo:int, lista_legajos, lista_nombres, lista_generos, matriz_notas, lista_promedios_alumnos)->list:
    """
    Realiza una busqueda de estudiante mediantes un numero de legajo asociado.
    
    Args:
        legajo:        
        lista_legajos: Es la lista con los legajos de cada alumno.        
        lista_nombres: Es la lista de nombres de los alumnos.
        lista_generos: Es la lista con los generos de cada alumno.
        matriz_notas: Son las notas de las materias de los alumnos.
        lista_promedios_alumnos: Es la lista con los promedios de los alumnos.
    Returns:
        list: retorna una lista con los datos de cada alumno.
    """
    indice_legajo = -1
    retorno_datos = []

    for i in range(len(lista_legajos)):
        if lista_legajos[i] == legajo:
            indice_legajo = i
            break

    if indice_legajo > -1:        
        retorno_datos += [lista_nombres[indice_legajo]]
        retorno_datos += [legajo]
        retorno_datos += [lista_generos[indice_legajo]]

        for i in range(len(matriz_notas[indice_legajo])):
            retorno_datos += [matriz_notas[indice_legajo][i]]

        retorno_datos += [lista_promedios_alumnos[indice_legajo]]

    return retorno_datos

def buscar_cantidad_de_notas(matriz_notas:list, numero_materia:int)->list:
    """
    Realiza una busqueda de la cantidad de cada nota que tiene la materia elegida.
    
    Args:
        legajo:        
        matriz_notas: Son las notas de las materias de los alumnos.
        numero_materia: Numero de materia a consultar.
    Returns:
        list: retorna una lista con la cantidad de cada nota de la materia.
    """
        
    lista_cantidad_notas = [0] * 10

    for i in range(len(matriz_notas)):        
        nota = matriz_notas[i][numero_materia - 1]

        if nota >= 1 and nota <= 10:
            lista_cantidad_notas[nota - 1] += 1

    return lista_cantidad_notas    
