class Node(object):
    def __init__(self: 'Node', value: object) -> None:
        self._value = value
        self.next = None
    
    def get_value(self: 'Node') -> object:
        return self._value    

class Queue(object):
    '''An implementation of the queue abstract data type.'''

    def __init__(self: 'Queue') -> None:
        '''Initialize self as an empty queue.'''
        
        self._front = None
        self._tail = None
        self._size = 0          # We need to manually track size
    
    def __len__(self: 'Queue') -> int:
        '''Return the length of this queue.'''
        
        return self._size
    
    def is_empty(self: 'Queue') -> bool:
        '''Return True iff self contains no elements.'''

        return self._front is None

    def enqueue(self: 'Queue', item: object) -> None:
        '''Add item to the end of self.'''

        self._size = self._size + 1
        
        if self._tail:
            self._tail.next = Node(item)    # Wrap item in a Node
            self._tail = self._tail.next
            return
            
        self._front = Node(item)
        self._tail = self._front

    def front(self: 'Queue') -> object:
        '''Return the element at the front of self.
        
        Precondition: self is not empty.
        '''
    
        return self._front.get_value()

    def dequeue(self: 'Queue') -> object:
        '''Return and remove the element at the front of self.
        
        Precondition: self is not empty.'''

        old_front = self._front
        self._front = old_front.next
        if not self._front:         # Just emptied the queue?
            self._tail = None

        self._size = self._size - 1
        
        return old_front.get_value()


class Stack(object):
    '''An implementation of the stack abstract data type.'''

    def __init__(self: 'Stack') -> None:
        '''Initialize self as an empty stack.'''
        
        self._top = None
        self._size = 0

    def __len__(self: 'Stack') -> int:
        '''Return the length of self.'''

        return self._size
    
    def is_empty(self: 'Stack') -> bool:
        '''Return True iff self contains no elements.'''
        return self._top is None

    def push(self: 'Stack', item: object) -> None:
        '''Add item to the top of self.'''

        old_top = self._top
        
        self._top = Node(item)
        self._top.next = old_top
        
        self._size = self._size + 1

    def peek(self: 'Stack') -> object:
        '''Return the element at the top of self.
        
        Precondition: self is not empty.'''

        return self._top.get_value()

    def pop(self: 'Stack') -> object:
        '''Return and remove the element at the top of self.
        
        Precondition: self is not empty.'''

        old_top = self._top
        self._top = self._top.next
        self._size = self._size - 1
        return old_top.get_value()
