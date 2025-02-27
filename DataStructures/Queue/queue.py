def new_queue():
    queue = {"size": 0, 
             "elements":[]}
    
    return queue

def enqueue(my_queue, element):
    
    my_queue["elements"].append(element)
    my_queue["size"] += 1
    
    return my_queue
    
def dequeue(my_queue):
    if my_queue["size"] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    
    return my_queue["elements"].pop(0)


def peek(my_queue):
    if my_queue["size"]== 0:
        raise Exception('EmptyStructureError: queue is empty')
    else:
        return my_queue["elements"][0]
    
def is_empty(queue):
    if not queue["elements"]:
        return True
    else:
        return False

def size(my_queue):
    return len(my_queue["elements"])
        

    
