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
            if count > 9:
                break
            print(f'{count} / 10')
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
    lt_anios_agricultura = catalog["anio_recoleccion"]
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
    
    lt_departamentos_agricultura = catalog["departamentos_agricultura"]
    datos_aux = lt.remove_first(lt_departamentos_agricultura)
    pos = lt.is_present(datos_aux, departamento_interes)
    
    if pos != -1:
        lt_anio = lt.get_element(lt_departamentos_agricultura, pos)
        elemento = lt.last_element(lt_anio)
        tiempo_final = get_time()
        tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
        return elemento, tiempo_ejecucion
    else:
        return "No se logro encontrar informacion del departamento seleccionado"
    
    
def req_3(catalog, departamento, anio_inicial, anio_final):
    # esto para revisar si los parametros estan
    tiempo_inicial = get_time()
    if not departamento or anio_inicial > anio_final:
        raise Exception ("Error, parametros invalidos")

# aca se obtiene la lista del catalogo de registros
    lt_registros = catalog["departamentos_agricultura"]
    datos_aux = lt.remove_first(lt_registros)
    pos = lt.is_present(datos_aux, departamento)

    if pos != -1:
        lt_anio = lt.get_element(lt_registros, pos)

#se obtiene los registros filtrados por departamento y anio en rangos 
    registros_filtrados = lt.new_list()
    for r in lt_anio:
        if (anio_inicial <= int(r["year_collection"]) <= anio_final):
            lt.add_last(registros_filtrados, r)

# se contea por tipo de fuente
    conteo = {"SURVEY": 0, "CENSUS": 0}
    for r in registros_filtrados["elements"]:
        if r["source"] in conteo:
            conteo[r["source"]] += 1

# aca es para que se muestre  solamento los primeros 5 y los ultimos 5 registros 
    if lt.size(registros_filtrados) > 20:
        primeros_5 = lt.sub_list(registros_filtrados, 1, 5)
        ultimos_5 = lt.sub_list(registros_filtrados, lt.size(registros_filtrados) - 4, 5)
        registros_mostrados = primeros_5 + ultimos_5
    else:
        registros_mostrados = registros_filtrados
# prepara los datos para la muestra
    datos = lt.new_list()
    for r in registros_mostrados["elements"]:
        registro_nuevo = {
            "fuente": r["source"],
            "año": r["year_collection"],
            "carga": r["load_time"],
            "frecuencia": r["freq_collection"],
            "producto": r["commodity"],
            "unidad_medicion": r["unit_measurement"]
        }
        lt.add_last(datos, registro_nuevo)

#retorna resultados 

    tiempo_final = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
    
    
    return {
        "Tiempo_ejecucion": tiempo_ejecucion,
        "total_registros": lt.size(registros_filtrados),
        "total_survey": conteo["SURVEY"],
        "total_census": conteo["CENSUS"],
        "registros": datos["elements"]
    }
    
    




def req_4(catalog, producto, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    tiempo_inicial = get_time()
   # esto para revisar si los parametros estan
    if not producto or anio_inicial > anio_final:
        raise Exception ("Error, parametros invalidos")

# aca se obtiene la lista del catalogo de registros
    lt_registros = catalog["departamentos_agricultura"]
    datos_aux = lt.remove_first(lt_registros)
    pos = lt.is_present(datos_aux, producto)

    if pos != -1:
        lt_anio = lt.get_element(lt_registros, pos)

#se obtiene los registros filtrados por producto y anio en rangos 
    registros_filtrados = lt.new_list()
    for r in lt_anio:
        if (anio_inicial <= int(r["year_collection"]) <= anio_final):
            lt.add_last(registros_filtrados, r)

# se contea por tipo de fuente
    conteo = {"SURVEY": 0, "CENSUS": 0}
    for r in registros_filtrados["elements"]:
        if r["source"] in conteo:
            conteo[r["source"]] += 1

# aca es para que se muestre  solamento los primeros 5 y los ultimos 5 registros 
    if lt.size(registros_filtrados) > 20:
        primeros_5 = lt.sub_list(registros_filtrados, 1, 5)
        ultimos_5 = lt.sub_list(registros_filtrados, lt.size(registros_filtrados) - 4, 5)
        registros_mostrados = primeros_5 + ultimos_5
    else:
        registros_mostrados = registros_filtrados
# prepara los datos para la muestra
    datos = lt.new_list()
    for r in registros_mostrados["elements"]:
        registro_nuevo = {
            "fuente": r["source"],
            "año": r["year_collection"],
            "carga": r["load_time"],
            "frecuencia": r["freq_collection"],
            "producto": r["commodity"],
            "unidad_medicion": r["unit_measurement"]
        }
        lt.add_last(datos, registro_nuevo)
    
    tiempo_final  = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)

#retorna resultados 

    return {
        "Tiempo_ejecucion": tiempo_ejecucion,
        "total_registros": lt.size(registros_filtrados),
        "total_survey": conteo["SURVEY"],
        "total_census": conteo["CENSUS"],
        "registros": datos["elements"]
    }



def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, departamento, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    
    tiempo_inicial = get_time()
    
    fecha_inicial = fecha_inicial.split("-")
    fecha_final = fecha_final.split("-")
    
    fecha_inicial = int(fecha_inicial[0] + fecha_inicial[1] + fecha_inicial[2])
    fecha_final = int(fecha_final[0] + fecha_final[1] + fecha_final[2])

    fecha_mayor = False

    if not departamento or fecha_inicial > fecha_final:
        raise Exception ("Error, parametros invalidos")
        
    lt_registros = catalog["departamentos_agricultura"]
    datos_aux = lt.remove_first(lt_registros)
    pos = lt.is_present(datos_aux, departamento)
    
    if pos != -1:
        lt_fecha = lt.get_element(lt_registros, pos)
        
    registros_filtrados = lt.new_list()
    
    for r in lt_fecha:
        
        fecha = r["load_time"].split("-")
        fecha = int(fecha[0] + fecha[1] + fecha[2])
        
        
        if (fecha_inicial <= fecha <= fecha_final):
            lt.add_last(registros_filtrados, r)
    
    conteo = {"SURVEY": 0, "CENSUS": 0}
    for r in registros_filtrados["elements"]:
        if r["source"] in conteo:
            conteo[r["source"]] += 1
            
    
    if lt.size(registros_filtrados) > 20:
        primeros_5 = lt.sub_list(registros_filtrados, 1, 5)
        ultimos_5 = lt.sub_list(registros_filtrados, lt.size(registros_filtrados) - 4, 5)
        registros_mostrados = primeros_5 + ultimos_5
    else:
        registros_mostrados = registros_filtrados
    
    datos = lt.new_list()
    
    for r in registros_mostrados["elements"]:
        registro_nuevo = {
            "fuente": r["source"],
            "año": r["year_collection"],
            "carga": r["load_time"],
            "frecuencia": r["freq_collection"],
            "producto": r["commodity"],
            "unidad_medicion": r["unit_measurement"]
        }
        lt.add_last(datos, registro_nuevo)
    
    tiempo_final = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial, tiempo_final)
    
    return {
        "Tiempo_ejecucion": tiempo_ejecucion,
        "total_registros": lt.size(registros_filtrados),
        "total_survey": conteo["SURVEY"],
        "total_census": conteo["CENSUS"],
        "registros": datos["elements"]
    }
    



def req_7 (catalog, departamento, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 7
    """
    tiempo_inicial = get_time()
    
    if not departamento or anio_inicial > anio_final:
        raise Exception ("Error, parametros invalidos")
    
    lt_registros = catalog["departamentos_agricultura"]
    datos_aux = lt.remove_first(lt_registros)
    pos = lt.is_present(datos_aux, departamento)

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
    elapsed = float(end - start)
    return elapsed
