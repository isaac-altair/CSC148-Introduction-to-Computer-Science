### Queue ###

def queue_create() -> list:
    '''Return a new object representing a queue.'''

    return []

def queue_size(queue: list) -> int:
    '''Return the length of queue.'''

    return len(queue)

def queue_is_empty(queue: list) -> bool:
    '''Return True iff queue contains no elements.'''

    return queue_size(queue) == 0

def queue_enqueue(queue: list, item: object) -> None:
    '''Add item to the end of queueu.'''

    return queue.append(item)


def queue_dequeue(queue: list) -> object:
    '''Return and remove the element at the front of the queue.'''

    return queue.pop(0)

def queue_front(queue:list) -> object:
    '''Return the element at the front of the queue.'''

    return queue[0]

### Stack ###

def stack_create() -> list:
    '''Return a new object representing a stack'''

    return []

def stack_size(stack: list) -> int:
    '''Return the length of stack'''

    return len(stack)

def stack_is_empty(stack: list) -> bool:
    '''Return True iff stack contains no elements.'''

    return stack_size(stack) == 0


def stack_push(stack: list, item: object) -> None:
    '''Return and remove the item at the top of the stack.'''

    return stack.append(item)

def stack_peek(stack: list) -> object:
    '''Return the object at the otp of the stack.'''

    return stack[-1]

def stack_pop(stack: list) -> None:
    '''return and remove the item at the top of the stack'''

    return stack.pop()

### Implementation of stack code ###

def brackets_matched(text: str) -> bool:
    '''Return True iff text has no brackets mismatching.

     The text has a mismatched bracket if an opening bracket is unclosed, a closing
     bracket does not closed at opening bracket, or a closing bracket is not of the same
     "type" as the opening bracket (for excample, curly with curly).

     Valid pairs are {}, [], and ().

     >>>Brackets_mismatched('(3 + 1 * [2]')
     True
     >>>brackets_mismatched('Hello :)')
     False

    '''

    # Initiate an empty stack for our bracket matching.
    # For each level of brackets we close, we want to make asure there is a
    # corresponding opening bracket.

    stack = stack_create()

    # The keys contain opening bracket symbols; the corresponding values are
    # the matching closing bracket symbol.

    open_bracket_to_close = {
                                '{': '}',
                                '[': ']',
                                '{': '}'
                            }
    # Loop theough each characther in the intput string...

    for ch in text:

        # and if it is the opening bracket chracthers, store the opening
        # chracter on the stack

        if ch in open_brack_to_close:
            stack_push(stack, ch)

        # If, isntead, it is one of the closing bracket characters, check to see
        # that it is clsoing the appropriate opening bracket.

        if ch in open_bracket_to_close.values():
            if stack_is_empty(stack) or ch != open_bracket_to_close[stack_pop(stack)]:
                return False

        # If there are any extra brackets on the stack, some brackets were unclosed.

        return stack_is_empty()

    # This implementation of the brackets_matched function has repetitious  code.
    # BAD!!! *wrist slap*

def brackets_matched_bad(text: str) -> bool:
    '''
    Return True iff text has no brackets mismatching.

    The text has a mismatched bracket if an opening bracket is unclosed, a closing
    brackets does not close an opening bracket, or closing bracket is not fo the same
    "type" as the opening bracket (for example, curly with curly).

    Valid pairs are {}, [], ().

    >>>Brackets_mismatched('(3 + 1 * [2]')
    True
    >>>brackets_mismatched('Hello :)')
    False

    '''

    # Initialize an empty stack for our bracket matching.
    # For each level of brackets we close, we want to make sure there is 
    # a corresponding opening bracket.

    stack = stack_create()

    # Loop through each character in input string...
    for ch in text:
        # and store any symbols on the stack.
        if ch in '{[(':
            stack_push(stack, ch)

        # If it is a closing bracket,
        if ch in '{[(':
            # make sure there is something on the stack
            if stack_is_empty(stack):
                return False

            # and that the top of the stack matches the closing symbol just
            # encountered.

            opening_symbol = stack_pop(stack)

            # BAD BAD BAD! This is too much copying-and-pasting.

            if opening_symbol == '{' and ch != '}':
                return False
            if opening_symbol == '[' and ch != ']':
                return False
            if opening_symbol == '(' and ch != ')':
                return False

        # If therea re any extra brackets on the stack, some brackets were unclosed.

        return stack_is_empty(stack)
    
