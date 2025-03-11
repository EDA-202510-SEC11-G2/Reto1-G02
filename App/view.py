import sys
from DataStructures.List import array_list as lt
from App import logic
default_time = 1000

sys.setrecursionlimit(default_time*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    catalog = logic.new_logic()
    
    return catalog
    
    

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control, filesize):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    
    if filesize == 1:
        path = "20"
    
    elif filesize == 2:
        path = "40"
    
    elif filesize == 3:
        path = "60"
    
    elif filesize == 4:
        path = "80"
        
    elif filesize == 5:
        path = "100"
    else:
        raise Exception ("Opcion Invalida")
    
    data = logic.load_data(control, path)
    
    return data

def print_reporte_carga(catalogo, anio_menor_y_mayor):
    print_size_registros(catalogo)
    print(f'Menor año de recoleccion de registro: {anio_menor_y_mayor[0]}')
    print(f'Mayor año de recoleccion de registro: {anio_menor_y_mayor[1]}')
    primeros_registros = []
    num_registros = len(catalogo['fuente']['elements'])
    i = 0
    while(i < num_registros and i < 5):
        registro = []
        registro.append(catalogo['anio_recoleccion']['elements'][i])
        registro.append(catalogo['fecha_carga']['elements'][i])
        registro.append(catalogo['departamento']['elements'][i])
        registro.append(catalogo['fuente']['elements'][i])
        registro.append(catalogo['unidad_medida']['elements'][i])
        registro.append(catalogo['valor']['elements'][i])
        primeros_registros.append(registro)
        i += 1
    
    print('info de los primeros 5 registros:')
    for r in primeros_registros:
        print(r)
        num_registros = len(catalogo['fuente']['elements'])


    i = num_registros - 1
    ultimos_registros = []
    while(i > 0 and i > num_registros - 6):
        registro = []
        registro.append(catalogo['anio_recoleccion']['elements'][i])
        registro.append(catalogo['fecha_carga']['elements'][i])
        registro.append(catalogo['departamento']['elements'][i])
        registro.append(catalogo['fuente']['elements'][i])
        registro.append(catalogo['unidad_medida']['elements'][i])
        registro.append(catalogo['valor']['elements'][i])
        ultimos_registros.append(registro)
        i -= 1
    
    print('info de los ultimos 5 registros:')
    for r in ultimos_registros:
        print(r)




def print_size_registros(control):
    size = lt.size(control["valor"])
    print(f"Se cargaron {size} registros del archivo seleccionado")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, anio_interes):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    data_encontrada = logic.req_1(control, anio_interes)
    print(f'{data_encontrada[0]}\nTiempo de busqueda: {data_encontrada[1]}ms')


def print_req_2(control, departamento_interes):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    data_encontrada = logic.req_2(control, departamento_interes)
    print(f'{data_encontrada[0]}\nTiempo de busqueda: {data_encontrada[1]} ms')
    


def print_req_3(control, departamento_interes, anio_inicial, anio_final):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    data_encontrada = logic.req_3(control, departamento_interes, anio_inicial, anio_final)
    
    print(data_encontrada)
    


def print_req_4(control, producto_interes, anio_inicial, anio_final):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    
    data_encontrada = logic.req_4(control, producto_interes, anio_inicial, anio_final)
    
    print(data_encontrada)
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    pass


def print_req_6(control, departamento_interes, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    
    data_encontrada = logic.req_6(control, departamento_interes, fecha_inicial, fecha_final)
    
    print(data_encontrada)



def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    
    
    data_encontrada = logic.req_7(control, departamento_interes, anio_inicial, anio_final)
    
    print(data_encontrada)



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Seleccione cuanta informacion desea importar: \n")
            print("1. Archivo 20%\n")
            print("2. Archivo 40%\n")
            print("3. Archivo 60%\n")
            print("4. Archivo 80%\n")
            print("5. Archivo 100%\n")
            archivo = int(input())
            print("Cargando información de los archivos ....\n")
            data, min_max_anios = load_data(control, archivo)
            print_reporte_carga(data, min_max_anios)
            
        elif int(inputs) == 2:
            anio_interes = input("Ingrese el anio de interes: ")
            print_req_1(control, anio_interes)

        elif int(inputs) == 3:
            departamento_interes = input("Ingresa el departamento de interes: ")
            print_req_2(control, departamento_interes)

        elif int(inputs) == 4:
            departamento_interes = input("Ingrese el departamento de interes: ")
            anio_inicial = int(input("Ingrese el año inicial: "))
            anio_final = int(input("Ingrese el año final: "))
            
            print_req_3(control, departamento_interes, anio_inicial, anio_final)

        elif int(inputs) == 5:
            producto_interes = input("Ingrese el producto de interes: ")
            anio_inicial = int(input("Ingrese el año inicial: "))
            anio_final = int(input("Ingrese el año final: "))
            
            print_req_4(control, producto_interes, anio_inicial, anio_final)
        

        elif int(inputs) == 6:
            print_req_5(control)
    

        elif int(inputs) == 7:
            departamento_interes = input("Ingrese el departamento de interes: ")
            fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")
            
            print_req_6(control, departamento_interes, fecha_inicial, fecha_final)

        elif int(inputs) == 8:
            departamento_interes = input("Ingrese el departamento de interes: ")
            anio_inicial = int(input("Ingrese el año inicial: "))
            anio_final = int(input("Ingrese el año final: "))
            
            print_req_7(control, departamento_interes, anio_inicial, anio_final)
            

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
