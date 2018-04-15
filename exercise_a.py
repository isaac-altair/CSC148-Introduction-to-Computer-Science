stack = []
queue = []
item = ''


def queue_create() -> list:
    '''Return a new object representing a queue.'''

    return []


def queue_enqueue(queue: list, item: object) -> None:
    '''Add item to the end of queueu.'''

    return queue.append(item)


def queue_dequeue(queue: list) -> object:
    '''Return and remove the element at the front of the queue.'''

    return queue.pop(0)


def queue_front(queue: list) -> object:
    '''Return the element at the front of the queue.'''

    return queue[0]


def stack_create() -> list:
    '''Return a new object representing a stack'''

    return []


def stack_push(stack: list, item: object) -> None:
    '''Return and remove the item at the top of the stack.'''

    return stack.append(item)


def stack_pop(stack: list) -> None:
    '''return and remove the item at the top of the stack'''

    return stack.pop()


def stack_peek(stack: list) -> object:
    '''Return the object at the top of the stack.'''

    if len(stack) == 1:
        return stack[0]
    else:
        return stack[-1]
    

def determine_adt_type(create: object, add: object, remove: object) -> str:
    '''
    create, add, and remove are all function objects for a single data type.
    Only store integers using this data type.
    
    Return 'stack' iff the three functions produce the behaviour of a stack,
    'queue' iff the three functions produce the behaviour of a queue,
    and 'other', otherwise.
    
    For example, if stack_create, stack_push, and stack_pop are all defined,
    determine_adt_type(stack_create, stack_push, stack_pop) == 'stack'
    
    Similarly,
    determine_adt_type(queue_create, queue_enqueue, queue_dequeue) == 'queue'
    '''
    
    # adt = create()          # Create an instance of this data type
    # add(adt, 3)             # Add something to it

    # return

    adt = create()
    add(adt, 10)
    add(adt, -100)
    var = remove(adt)
    add(adt, 50)
    add(adt, -7)
    add(adt, 25)
    var = remove(adt)

    if var == 25:
        return 'stack'
    elif var == -100:
        return 'queue'
    else:
        return 'other'
    
      
def square_root(x: float, eps: float) -> float:
    """
    Return the square root of x, a positive number, to within an accuracy of
    eps, or -1.0 if more than 10 iterations are required.
    
    >>> square_root(9, 2)
    3.4
    """

    i = 0
    TG = 1.0
    NG = 1.0
    if x == 0:
        return 0
    while i <= 10:
        TG = NG
        NG = 0.5 * (TG + abs(x) / TG)
        if abs(NG - TG) < eps:
            return NG
        i = i + 1
    if i >= 10.0:
        return -1.0


    
