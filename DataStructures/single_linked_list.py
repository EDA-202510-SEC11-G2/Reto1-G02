def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0 
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    
    return count
def add_first(lista, elemento):
    #Agrega un elemento al inicio de la lista enlazada.
    nuevo_nodo = {"info": elemento, "next": lista["first"]}
    lista["first"] = nuevo_nodo

    if lista["size"] == 0:  # Si la lista estaba vacía, el nuevo nodo es también el último
        lista["last"] = nuevo_nodo

    lista["size"] += 1
    
def add_last(lista, elemento):

    #Agrega un elemento al final de la lista enlazada.
    
    nuevo_nodo = {"info": elemento, "next": None}

    if lista["size"] == 0:
        lista["first"] = nuevo_nodo
        lista["last"] = nuevo_nodo
    else:
        lista["last"]["next"] = nuevo_nodo
        lista["last"] = nuevo_nodo

    lista["size"] += 1
def is_empty(lista):
    #Retorna True si la lista está vacía, False en caso contrario.
    return lista["size"] == 0

def size(lista):
    # Retorna el número de elementos en la lista.
    return lista["size"]
def first_element(lista):
    #Retorna el primer elemento de la lista o None si está vacía.
    if lista["first"] is None:
        return None
    return lista["first"]["info"]
def last_element(lista):
    #Retorna el último elemento de la lista o None si está vacía.
    if lista["last"] is None:
        return None
    return lista["last"]["info"]
def get_element(lista, index):
    #Retorna el elemento en la posición index.
    if index < 0 or index >= lista["size"]:
        return None

    actual = lista["first"]
    for _ in range(index):
        actual = actual["next"]
    
    return actual["info"]
def remove_first(lista):
    # Elimina el primer elemento de la lista y lo retorna.
    
    if lista["first"] is None:
        return None

    eliminado = lista["first"]["info"]
    lista["first"] = lista["first"]["next"]

    if lista["first"] is None:  # Si eliminamos el último nodo solo 
        lista["last"] = None

    lista["size"] -= 1
    return eliminado
def remove_last(lista):
    
    # Elimina el último elemento de la lista y lo retorna.
    
    if lista["first"] is None:
        return None

    if lista["size"] == 1:
        eliminado = lista["first"]["info"]
        lista["first"] = None
        lista["last"] = None
        lista["size"] -= 1
        return eliminado

    actual = lista["first"]
    while actual["next"] != lista["last"]:
        actual = actual["next"]

    eliminado = lista["last"]["info"]
    lista["last"] = actual
    lista["last"]["next"] = None
    lista["size"] -= 1
    return eliminado

def insert_element(lista, index, elemento):
   
    # Inserta un elemento en la posición index dentro de la lista enlazada.
    
    if index < 0:  
        return None  

    if index == 0:  
        add_first(lista, elemento)
        return lista  

    if index >= lista["size"]:  
        add_last(lista, elemento)
        return lista  

    
    nuevo_nodo = {"info": elemento, "next": None}
    actual = lista["first"]

    for _ in range(index - 1): 
        actual = actual["next"]

    nuevo_nodo["next"] = actual["next"]  
    actual["next"] = nuevo_nodo 

    lista["size"] += 1 
    return lista  



def delete_element(lista, index):
    """
    Elimina un elemento en la posición index de la lista enlazada.
    """
    if index < 0 or index >= lista["size"]:
        return None

    if index == 0:  
        remove_first(lista)
        return lista 
    actual = lista["first"]
    for _ in range(index - 1):
        actual = actual["next"]

    eliminado = actual["next"]["info"]
    actual["next"] = actual["next"]["next"]

    if actual["next"] is None:  
        lista["last"] = actual

    lista["size"] -= 1
    return lista  

def change_info(lista, index, elemento):
    
    # Cambia el valor de un nodo en la posición index.
    
    if index < 0 or index >= lista["size"]:  
        return None

    actual = lista["first"]
    for _ in range(index):  
        actual = actual["next"]

    actual["info"] = elemento  
    return lista  
def exchange(lista, index1, index2):
    
   #  Intercambia los valores de dos nodos en las posiciones index1 e index2.
    
    if index1 < 0 or index1 >= lista["size"] or index2 < 0 or index2 >= lista["size"]:
        return None  

    if index1 == index2:
        return lista  

    actual1 = lista["first"]
    for _ in range(index1):
        actual1 = actual1["next"]

    actual2 = lista["first"]
    for _ in range(index2): 
        actual2 = actual2["next"]

    actual1["info"], actual2["info"] = actual2["info"], actual1["info"] 
    return lista  


def sub_list(lista, start, length):
    """
    Retorna una sublista de tamaño length desde la posición start.
    """
    if start < 0 or start >= lista["size"] or length < 0:
        return None  

    sub_lista = {"first": None, "last": None, "size": 0}  

    if length == 0:  
        return sub_lista

    actual = lista["first"]

    for _ in range(start):  
        actual = actual["next"]

    for _ in range(length):  
        if actual is None:
            break
        add_last(sub_lista, actual["info"]) 
        actual = actual["next"]

    return sub_lista 