import random
import Utils
import Validaciones

def cargar_notas(matriz_notas: list) -> list:
    """
    Carga una matriz con notas.
    
    Args:
        matriz_notas: Matriz donde va a cargar las notas.
    """
    for i in range(len(matriz_notas)):
        for j in range(len(matriz_notas[i])):
            calificacion = 0
            while not Validaciones.validar_calificacion(calificacion):
                # calificacion = int(input(f"Ingresar nota del alumno: "))
                calificacion = random.randint(1, 10)
            matriz_notas[i][j] = calificacion
    return matriz_notas


def cargar_alumnos(lista_nombres: list) -> list:
    """
    Carga una lista con los nombres de los alumnos.
    
    Args:
        lista_nombres: Lista donde van a estar los nombres.
    """
    for i in range(len(lista_nombres)):
        nombre = ""
        while not Validaciones.validar_nombre(nombre):
            # nombre = input(f"Ingresar nombre del alumno: ")
            nombre = f"Alumno_{i+1}"
        lista_nombres[i] = nombre
    return lista_nombres


def cargar_generos(lista_generos: list) -> list:
    """
    Carga una lista con los generos de los alumnos.
    
    Args:
        lista_generos: Lista donde van a estar los generos.
    """
    for i in range(len(lista_generos)):
        genero = ""
        while not Validaciones.validar_genero(genero):
            # genero = input(f"Ingresar genero (F/M/X): ")
            genero = random.choice(['F', 'M', 'X'])
        lista_generos[i] = genero
    return lista_generos


def cargar_legajos(lista_legajos: list) -> list:
    """
    Carga una lista con los legajos de los alumnos.
    
    Args:
        lista_legajos: lista donde van a estar los legajos.
    """
    for i in range(len(lista_legajos)):
        legajo = 0
        while not Validaciones.validar_legajo(legajo):
            # legajo = int(input(f"Ingresar legajo: (debe ser de 5 digitos)"))
            legajo = random.randint(10000, 99999)
        lista_legajos[i] = legajo
    return lista_legajos

def calcular_promedios_por_alumnos(matriz_notas:list, )-> list:
    """
    Calcula el promedio de notas de cada alumno
    
    Args:
        matriz_notas: Matriz donde van a estar las notas.
    
    Returns:
        list: Retorna una lista de promedios.
    """
    lista_promedios = [0] * 30
    for i in range(len(matriz_notas)):
        suma = 0
        for j in range(len(matriz_notas[i])):
            suma = suma + matriz_notas[i][j]        

        promedio = suma / len(matriz_notas[i])
        lista_promedios[i] = promedio
        
    return lista_promedios

def calcular_promedios_por_materia(matriz_notas: list)->list:
    """
    Calcula el promedio de notas de cada materia.
    
    Args:
        matriz_notas: Matriz donde van a estar las notas.
    Returns:
        list: Retorna una lista de promedios.
    """
    cantidad_alumnos = len(matriz_notas)
    cantidad_materias = len(matriz_notas[0])
    lista_promedios_materias = [0] * cantidad_materias 

    for j in range(cantidad_materias):
        suma = 0
        for i in range(cantidad_alumnos):
            suma += matriz_notas[i][j]
        promedio = suma / cantidad_alumnos
        lista_promedios_materias[j] = promedio

    return lista_promedios_materias

def generar_lista_nombres_materias(lista_promedios_materias: list)->list:
    """
    Genera una lista de nombres para cada materia.
    
    Args:
        lista_promedios_materias: lista con los promedios de cada materia.
    Returns:
        list: Retorna una lista de promedios.
    """
    cantidad_materias = len(lista_promedios_materias)
    lista_nombres_materias = [0] * cantidad_materias
    for i in range(cantidad_materias):
        lista_nombres_materias[i] = f"Materia_{i+1}"
    
    return lista_nombres_materias

def obtener_materia_mayor_promedio(lista_promedios_materias: list, lista_nombres_materias: list) -> str:
    """
    Busca en una lista de promedios, cual es la o las materias con mayor promedio
    
    Args:
        lista_promedios_materias: lista con los promedios de cada materia.
        lista_nombres_materias: lista con los nombres de las materias.
    Returns:
        str: Retorna un string con el resultado de la busqueda.
    """
    mayor_promedio = lista_promedios_materias[0]
    posicion_mayor = 0

    for i in range(1, len(lista_promedios_materias), 1):
        if lista_promedios_materias[i] > mayor_promedio:
            mayor_promedio = lista_promedios_materias[i]
            posicion_mayor = i

    return lista_nombres_materias[posicion_mayor]


def promedios_de_materias(matriz_notas: list):
    """
    Calcula y ordena de mayor a menor y muestra la lista de promedio de las materias.
    
    Args:
        matriz_notas: Matriz donde van a estar las notas.
    """
    lista_promedios_materias = calcular_promedios_por_materia(matriz_notas)    
    lista_nombres_materias = generar_lista_nombres_materias(lista_promedios_materias)

    Utils.ordenar_promedios_materias_desc(lista_promedios_materias, lista_nombres_materias)
    Utils.imprimir_promedios_materias(lista_promedios_materias, lista_nombres_materias)

    Utils.imprimir_materia_mayor_promedio(lista_promedios_materias, lista_nombres_materias)



def buscar_alumno_por_legajo(lista_nombres:list, lista_legajos:list, lista_generos:list, matriz_notas:list, lista_promedios:list):
    """
    Busca la informacion de cada alumno en base a su legajo
    
    Args:
        matriz_notas: Matriz donde van a estar las notas.
        lista_nombres: Lista con los nombres de los alumnos.
        lista_legajos: Lista con los legajos de los alumnos.
        lista_generos: Lista con los generos de los alumnos.
        lista_promedios: Lista con los promedios de los alumnos.
        
    """
    
    legajo = int(input("Ingrese el legajo q desea buscar: "))
    print("")

    lista_datos_del_alumno = Utils.buscar_estudiante_por_legajo(legajo, lista_legajos, lista_nombres, lista_generos, matriz_notas, lista_promedios)
    
    if len(lista_datos_del_alumno) > 0:
        Utils.imprimir_datos_alumno(lista_datos_del_alumno)

    else:
        print(f"No se encontro el legajo {legajo}.")

def cantidad_de_notas_por_materia(matriz_notas:list):
    """
    Busca la cantidad de cada nota que tiene una materia.
    
    Args:
        matriz_notas: Matriz donde van a estar las notas.
    """
    nro_materia = int(input("Ingrese el numero de materia: "))
    lista_notas_de_materia = Utils.buscar_cantidad_de_notas(matriz_notas, nro_materia)
    Utils.imprimir_datos_materia(lista_notas_de_materia)