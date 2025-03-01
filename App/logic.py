import time
import csv
import os 
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Queue import queue as queue
from DataStructures import Stack as st


csv.field_size_limit(2147483647)

data_dir = os.path.dirname(os.path.realpath(__file__)) + '/Data/' + '/agricultural-20.csv'


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {
        "source": None,
        "commodity": None,
        "statical_category": None,
        "unit_measurement": None,
        "state_name": None,
        "location": None,
        "year_collection": None,
        "freq_collection": None,
        "reference_period":None,
        "load_time": None,
        "value": None,
        
    }
    
    catalog["source"] = lt.new_list()
    catalog["commodity"] = lt.new_list()
    catalog["statical_category"] = lt.new_list()
    catalog["unit_measurement"] = lt.new_list()
    catalog["state_name"] = lt.new_list()
    catalog["location"] = lt.new_list()
    catalog["year_collection"] = lt.new_list()
    catalog["freq_collection"] = lt.new_list()
    catalog["reference_period"] = lt.new_list()
    catalog["load_time"] = lt.new_list()
    catalog["value"] = lt.new_list()
    

    return catalog
    


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    with open("Data/agricultural-" + filename + ".csv", newline=",", encoding="utf-8") as csvfile:
        datos = csv.DictReader(csvfile)
        
        for elemento in datos:
            lt.add_last(catalog["dato_agricultural"], elemento)
    
    

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
    
    last_date = -10000
    
    for i in catalog["year_collection"]:
        if i == anio_interes:
            catalog["load_time"][i]
    
    
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, departamento, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 3
    """
    if not departamento or anio_inicial > anio_final:
        return {"error"}
    
    registros_filtrados = [
        for r in catalog["registros"]
        if r.departamento.strip().upper() == departamento.strip().upper()
        and start_year <= r.año_recopilacion <= end_year 
        ]
    
    conteo = {"SURVEY": 0, "CENSUS": 0}
    for i in registros_filtrados
    if i.tipo_fuente in conteo:
        conteo[r.tipo_fuente] += 1

    survey = conteo["SURVEY"]
    census = conteo["CENSUS"]
    
    registros_mostrados = registros_filtrados
    if len(registros_filtrados) > 20:
        registros_mostrados = registros_filtrados[:5] + registros_filtrados[-5:]

    datos = []
    for r in registros_mostrados:
       registro_nuevo = {
        "fuente": r.tipo_fuente,
        "año": r.año_recopilacion,
        "carga": r.fecha_carga,  
        "producto": r.producto
        }
        
    datos.append(registro_nuevo)
    
    
def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


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
    elapsed = float(end - start)
    return elapsed
