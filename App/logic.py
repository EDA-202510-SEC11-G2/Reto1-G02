import time
import csv
import os 
import datetime as dt
from copy import deepcopy
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl

from DataStructures import Stack as st


csv.field_size_limit(2147483647)

data_dir = os.path.dirname(os.path.realpath(__file__)) + '/Data/' + '/agricultural-20.csv'


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {}
    
    catalog["fuente"] = lt.new_list()
    catalog["commodity"] = lt.new_list()
    catalog["categoria_estadistica"] = lt.new_list()
    catalog["unidad_medida"] = lt.new_list()
    catalog["departamento"] = lt.new_list()
    catalog["ubicacion"] = lt.new_list()
    catalog["anio_recoleccion"] = lt.new_list()
    catalog["freq_recoleccion"] = lt.new_list()
    catalog["periodo_referencia"] = lt.new_list()
    catalog["fecha_carga"] = lt.new_list()
    catalog["valor"] = lt.new_list()
    
    return catalog
    
    


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    with open("Data/agricultural-" + filename + ".csv", newline="", encoding="utf-8") as csvfile:
        datos = csv.DictReader(csvfile)
        num_columnas = len(datos.fieldnames)
        
        count = 0
        min_anio = 9999
        max_anio = 0
        for registro in datos:
            if count > 1000:
                break
            for i in range(num_columnas):
                if(i == 0):
                    lt.add_last(catalog['fuente'], registro['source'])
                elif(i == 1):
                    lt.add_last(catalog['commodity'], registro['commodity'])
                elif(i == 2):
                    lt.add_last(catalog['categoria_estadistica'], registro['statical_category'])
                elif(i == 3):
                    lt.add_last(catalog['unidad_medida'], registro['unit_measurement'])
                elif(i == 4):
                    lt.add_last(catalog['departamento'], registro['state_name'])
                elif(i == 5):
                    lt.add_last(catalog['ubicacion'], registro['location'])
                elif(i == 6):
                    lt.add_last(catalog['anio_recoleccion'], registro['year_collection'])
                    anio = int(registro['year_collection'])
                    if anio > max_anio:
                        max_anio = anio
                    if anio < min_anio:
                        min_anio = anio
                elif(i == 7):
                    lt.add_last(catalog['freq_recoleccion'], registro['freq_collection'])
                elif(i == 8):
                    lt.add_last(catalog['periodo_referencia'], registro['reference_period'])
                elif(i == 9):
                    lt.add_last(catalog['fecha_carga'], registro['load_time'])
                elif(i == 10):
                    lt.add_last(catalog['valor'], registro['value'])
            count += 1
    
    return (catalog, (min_anio, max_anio))

    
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog, anio_interes):
    """
    Retorna el resultado del requerimiento 1
    """
    tiempo_inicial = get_time()
    lt_anios_agricultura = deepcopy(catalog["fecha_carga"])
    for i in range(len(lt_anios_agricultura['elements'])):
        lt_anios_agricultura['elements'][i] = lt_anios_agricultura['elements'][i][:4]
    pos = lt.is_present(lt_anios_agricultura, anio_interes)
    
    if pos != -1:
        elemento = []
        elemento.append(catalog['anio_recoleccion']['elements'][pos])
        elemento.append(catalog['fecha_carga']['elements'][pos])
        elemento.append(catalog['fuente']['elements'][pos])
        elemento.append(catalog['freq_recoleccion']['elements'][pos])
        elemento.append(catalog['departamento']['elements'][pos])
        elemento.append(catalog['commodity']['elements'][pos])
        elemento.append(catalog['unidad_medida']['elements'][pos])
        elemento.append(catalog['valor']['elements'][pos])
        tiempo_final = get_time()
        tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
        return elemento, tiempo_ejecucion
    else:
        return "No se logro encontrar informacion del año seleccionado"
    
    


def req_2(catalog, departamento_interes):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    
    tiempo_inicial = get_time()
    lt_departamento = catalog["departamento"]
    pos = lt.is_present(lt_departamento, departamento_interes)
    
    if pos != -1:
        elemento = []
        elemento.append(catalog['anio_recoleccion']['elements'][pos])
        elemento.append(catalog['fecha_carga']['elements'][pos])
        elemento.append(catalog['fuente']['elements'][pos])
        elemento.append(catalog['freq_recoleccion']['elements'][pos])
        elemento.append(catalog['departamento']['elements'][pos])
        elemento.append(catalog['commodity']['elements'][pos])
        elemento.append(catalog['unidad_medida']['elements'][pos])
        elemento.append(catalog['valor']['elements'][pos])
        tiempo_final = get_time()
        tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
        return elemento, tiempo_ejecucion
    else:
        return "No se logro encontrar informacion del año seleccionado"
    
def req_3(catalog, departamento, anio_inicial, anio_final):
    tiempo_inicial = get_time()
    if not departamento or anio_inicial > anio_final:
        raise Exception ("Error, parametros invalidos")
    
    num_registros = len(catalog['valor']['elements'])
    registros_filtrados = []
    num_survey = 0
    num_census = 0
    for i in range(num_registros):
        if (catalog['departamento']['elements'][i] == departamento
            and int(catalog['anio_recoleccion']['elements'][i]) >= anio_inicial
            and int(catalog['anio_recoleccion']['elements'][i]) <= anio_final):
            if catalog['fuente']['elements'][i] == 'SURVEY':
                num_survey += 1
            else:
                num_census +=1
            elemento = []
            elemento.append(catalog['fuente']['elements'][i])
            elemento.append(catalog['anio_recoleccion']['elements'][i])
            elemento.append(catalog['fecha_carga']['elements'][i])
            elemento.append(catalog['freq_recoleccion']['elements'][i])
            elemento.append(catalog['commodity']['elements'][i])
            elemento.append(catalog['unidad_medida']['elements'][i])
            registros_filtrados.append(elemento)
    
    
    if len(registros_filtrados) > 20:
        while len(registros_filtrados) > 10:
            if registros_filtrados[5][0] == 'SURVEY':
                num_survey -= 1
            else:
                num_census -= 1
            registros_filtrados.pop(5)

    tiempo_final = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
    
    
    return {
        "Tiempo_ejecucion": tiempo_ejecucion,
        "total_registros": len(registros_filtrados),
        "num_survey" : num_survey,
        "num_census" : num_census,
        "registros": registros_filtrados
    }
    
    




def req_4(catalog, producto, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 4
    """
    tiempo_inicial = get_time()
    if not producto or anio_inicial > anio_final:
        raise Exception ("Error, parametros invalidos")
    
    num_registros = len(catalog['valor']['elements'])
    registros_filtrados = []
    num_survey = 0
    num_census = 0
    for i in range(num_registros):
        if (catalog['commodity']['elements'][i] == producto
            and int(catalog['anio_recoleccion']['elements'][i]) >= anio_inicial
            and int(catalog['anio_recoleccion']['elements'][i]) <= anio_final):
            if catalog['fuente']['elements'][i] == 'SURVEY':
                num_survey += 1
            else:
                num_census +=1
            elemento = []
            elemento.append(catalog['fuente']['elements'][i])
            elemento.append(catalog['anio_recoleccion']['elements'][i])
            elemento.append(catalog['fecha_carga']['elements'][i])
            elemento.append(catalog['freq_recoleccion']['elements'][i])
            elemento.append(catalog['departamento']['elements'][i])
            elemento.append(catalog['unidad_medida']['elements'][i])
            registros_filtrados.append(elemento)
    
    
    if len(registros_filtrados) > 20:
        while len(registros_filtrados) > 10:
            if registros_filtrados[5][0] == 'SURVEY':
                num_survey -= 1
            else:
                num_census -= 1
            registros_filtrados.pop(5)

    tiempo_final = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
    
    
    return {
        "Tiempo_ejecucion": tiempo_ejecucion,
        "total_registros": len(registros_filtrados),
        "num_survey" : num_survey,
        "num_census" : num_census,
        "registros": registros_filtrados
    }



def req_6(catalog, departamento, fecha_inicial: str, fecha_final:str):
    """
    Retorna el resultado del requerimiento 6
    """
    tiempo_inicial = get_time()
    y1, m1, d1 = [int(x) for x in fecha_inicial.split('-')]
    anio_inicial = dt.datetime(y1, m1, d1)
    y2, m2, d2 = [int(x) for x in fecha_final.split('-')]
    anio_final = dt.datetime(y2, m2, d2)
    if not departamento or anio_inicial > anio_final:
        raise Exception ("Error, parametros invalidos")
    
    num_registros = len(catalog['valor']['elements'])
    registros_filtrados = []
    num_survey = 0
    num_census = 0
    for i in range(num_registros):
        string = catalog['fecha_carga']['elements'][i][:10]
        y1, m1, d1 = [int(x) for x in string.split('-')]
        fecha = dt.datetime(y1, m1, d1)
        if (catalog['departamento']['elements'][i] == departamento
            and fecha >= anio_inicial
            and fecha <= anio_final):
            if catalog['fuente']['elements'][i] == 'SURVEY':
                num_survey += 1
            else:
                num_census +=1
            elemento = []
            elemento.append(catalog['fuente']['elements'][i])
            elemento.append(catalog['anio_recoleccion']['elements'][i])
            elemento.append(catalog['fecha_carga']['elements'][i])
            elemento.append(catalog['freq_recoleccion']['elements'][i])
            elemento.append(catalog['departamento']['elements'][i])
            elemento.append(catalog['unidad_medida']['elements'][i])
            registros_filtrados.append(elemento)
    
    
    if len(registros_filtrados) > 20:
        while len(registros_filtrados) > 10:
            if registros_filtrados[0] == 'SURVEY':
                num_survey -= 1
            else:
                num_census -= 1
            registros_filtrados.pop(5)

    tiempo_final = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
    
    
    return {
        "Tiempo_ejecucion": tiempo_ejecucion,
        "total_registros": len(registros_filtrados),
        "num_survey" : num_survey,
        "num_census" : num_census,
        "registros": registros_filtrados
    }



def req_7 (catalog, departamento, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 7
    """
    tiempo_inicial = get_time()
    
    if not departamento or anio_inicial > anio_final:
        raise Exception ("Error, parametros invalidos")
    
    lt_registros = catalog["departamentos"]
    pos = lt.is_present(lt_registros, departamento)

    ingresosmayores = 0
    ingresosmenores = 0
    if pos != -1:
        lt_departamento = lt.get_element(lt_registros, pos)

    registros_filtrados = lt.new_list()
    for r in lt_departamento:
        if (anio_inicial <= int(r["year_collection"]) <= anio_final):
            lt.add_last(registros_filtrados, r)

    registro_menor = None
    registro_mayor = None

    for r in registros_filtrados:
        if  r["value"] > ingresosmayores :
            ingresosmayores = r["value"]
            registro_mayor = r
        if r["value"] < ingresosmenores:
            ingresosmenores = r["value"]
            registro_menor = r
    
    tiempo_final = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
    
    return registro_mayor, registro_menor, tiempo_ejecucion

    


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = round(float(end - start), 3)
    return elapsed
