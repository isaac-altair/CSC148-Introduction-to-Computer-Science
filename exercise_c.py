class Node(object):
    def __init__(self):
        self.next = None
        self.value = None

class CircularBuffer(object):
    '''A circular buffer data structure.'''

    def __init__(self: 'CircularBuffer', size: int) -> None:
        '''Initialize a new circular buffer for size elements.
        
        Precondition: size is at least 1.'''

        self._size = size
        # TODO: Complete this method!

    def read(self: 'CircularBuffer') -> object:
        '''Return the element at the front of self.
        
        Raise BufferEmptyError if self is empty.'''

        # TODO: Complete this method!
        return None         # You'll need to delete this line

    def write(self: 'CircularBuffer', data: object) -> None:
        '''Write data to the end of self.
        
        Raise BufferFullError if self is full.'''

        # TODO: Complete this method!

    def __len__(self: 'CircularBuffer') -> int:
        '''Return the number of elements in the buffer.'''
        
        # TODO: Complete this method!
        return 0            # You'll need to delete this line

    def __str__(self: 'CircularBuffer') -> str:
        '''Starting from the current front of self, return a string
        containing the contents of each slot in the buffer. Elements are 
        separated by ' -- '.
        '''

        # TODO: Complete this method!        
        return ''           # You'll need to delete this line
