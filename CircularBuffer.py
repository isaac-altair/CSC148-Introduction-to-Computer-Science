class Node(object):
    def __init__(self):
        self.next = None
        self.value = None

class BufferFullError(Exception):
    '''Raise BufferFullError if buffer is full, len = size'''
    pass

class BufferEmptyError(Exception):
    '''Raise BufferEmptyError if buffer is empty, len = 0'''
    pass

class CircularBuffer(object):
    '''A circular buffer data structure.'''

    def __init__(self: 'CircularBuffer', size: int) -> None:
        '''Initialize a new circular buffer for size elements.
        
        Precondition: size is at least 1.'''
        self._front = Node()
        self._end = Node()
        self._size = size
        self._len = 0
        c_node = self._front
        for i in range(self._size + 1):
            c_node.next = Node()
            c_node = c_node.next
        c_node = self._front
        # TODO: Complete this method!

    def read(self: 'CircularBuffer') -> object:
        '''Return the element at the front of self.
        
        Raise BufferEmptyError if self is empty.'''

        if self._len == 0:
            raise BufferEmptyError
        # Case with just 1 element and everything else is empty
        if self._size == 1:
            self._len = self._len - 1   
            return self._front.value
        if self._len > 1:
            if self._front:
                new_node = self._front
                self._end.next = new_node
                self._end = new_node
                new_node.next = None
                self._len = self._len - 1   
                return new_node.value

    def write(self: 'CircularBuffer', data: object) -> None:
        '''Write data to the end of self.
        
        Raise BufferFullError if self is full.'''
        if self._len == self._size:
                raise BufferFullError
        if self._len == 0: 
            if self._front:
##                pointing = self._front.next
                self._front.value = data
##                self._front.next = pointing
            else:
                self._front.value = data
        else:
            counter = 1
            c_node = self._front
            while counter < self._len:
                counter += 1
                c_node = c_node.next
            c_node.next.value = data
        # TODO: Complete this method!
        self._len += 1

    def __len__(self: 'CircularBuffer') -> int:
        '''Return the number of elements in the buffer.'''
        
        # TODO: Complete this method!
        return self._len            

    def __str__(self: 'CircularBuffer') -> str:
        '''Starting from the current front of self, return a string
        containing the contents of each slot in the buffer. Elements are 
        separated by ' -- '.
        '''

        buffer = ''
        c_node = self._front
        k = 1
        for k in range(self._size):
            if c_node:
                if k < self._size - 1:
                    buffer = buffer + str(c_node.value) + ' -- '
                else:
                    buffer = buffer + str(c_node.value)
                c_node = c_node.next
            else:
                if k < self._size - 1:
                    buffer = buffer + "None -- "
                else:
                    buffer = buffer + "None"
            
            
        # TODO: Complete this method!        
        return buffer

'''
if __name__ == '__main__':
   buffer = CircularBuffer(3)
   print(len(buffer), str(buffer))
   buffer.write("Hi!")
   print(len(buffer), str(buffer))
   buffer.write("Bye!")
   print(len(buffer), str(buffer))
   buffer.write(17)
   print(len(buffer), str(buffer))
## buffer.write(21)
   print(len(buffer), str(buffer))
   print(buffer.read())
   print(len(buffer), str(buffer))
   print(buffer.read())
   print(len(buffer), str(buffer))
   print(buffer.read())
   print(len(buffer), str(buffer))
## print(buffer.read())
   print(len(buffer), str(buffer))
   buffer.write("Blah")
   print(len(buffer), str(buffer))
'''
