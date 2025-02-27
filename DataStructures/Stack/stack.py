def new_stack():
    #Esta funcion crea la nueva pila. 
    #Se crea tipo diccionario  con los elemntos del curso,la primera parte es una llave "elements que contiene la lista de la pila " Y tambien tiene otra llave que es size que nos dice el numero de elemntos de la pila.
    return {"elements": [],"size":0}

def push(stack, element):
    #Con esta funcion le agrego un elemento a la pila.
    #Aca cojo el dic stack abro la llave elements y le agrego al final un elemento por lo que last in first out
    stack["elements"].append(element)
    #Aca abro la llave size y le agrego 1
    stack["size"] += 1

def pop(stack):
    #Primero miro si la lista esta vacia para que no genere un error
    if is_empty(stack):
        return None
    #Y aca el pop lo que hace es que coje el ultimo elemnto y lo elimina. Es decir el ultimo que entro el primero en salir.Y retorna esa elemento
    else:
        #Aca quito 1
        stack["size"] -= 1
        return stack["elements"].pop()

def is_empty(stack):
    #Aca miro si la pila esta vacia. 
    #Aca abro con la llave size y miro si esta vacia o no
    return stack["size"] == 0

def top(stack):
    #Voy a deovolver el ultimo elemnto de la pila osea el ultimo en entrar
    #Primero miro si esta vacia o no
    if is_empty(stack):
        return None
    #Aca retorno el elemnto ultimo es decir el ultimo entrar. Uso -1 porque es como si fuera inverso. 
    return stack["elements"][-1]

def size(stack):
    return stack["size"]
