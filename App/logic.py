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
    
    catalog = {}
    
    catalog["data_agricultura"] = lt.new_list()
    catalog["anios_agricultura"] = lt.new_list()
    catalog["departamentos_agricultura"] = lt.new_list()
    
    return catalog
    
    


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    with open("Data/agricultural-" + filename + ".csv", newline="", encoding="utf-8") as csvfile:
        datos = csv.DictReader(csvfile)
        
        for elemento in datos:
            lt.add_last(catalog["data_agricultura"], elemento)
    
    return catalog

def load_anios(catalog):
    
    datos_completos = catalog["data_agricultura"]
    
    datos_aux = lt.new_list()
    
    for diccionario in datos_completos["elements"]:
        anio = str(diccionario["coleccion_anio"])
        pos = lt.is_present(datos_aux, anio)
        if pos == -1:
            lt.add_last(datos_aux, anio)
            data_de_anio = lt.new_list()
            lt.add_last(data_de_anio, diccionario)
            lt.add_last(catalog["anios_agricultura"], data_de_anio)
        else: 
            lt_anio_seleccionado = lt.get_element(catalog["anios_agricultura"], pos)
            lt.add_last(lt_anio_seleccionado, diccionario)
            
    lt.add_first(catalog["anios_agricultura"], datos_aux)
    
    return catalog
        
        
    
    
    

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
    
    lt_anios_agricultura = catalog["anios_agricultura"]
    datos_aux = lt.remove_first(lt_anios_agricultura)
    pos = lt.is_present(datos_aux, anio_interes)
    
    if pos != -1:
        lt_anio = lt.get_element(lt_anios_agricultura, pos)
        elemento = lt.last_element(lt_anio)
        return elemento
    else:
        return "No se logro encontrar informacion del año seleccionado"
    
    
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


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
