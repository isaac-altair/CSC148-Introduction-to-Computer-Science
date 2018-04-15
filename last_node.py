class LLNode(object):
    def __init__(self: 'LLNode', value: object, next: 'LLNode') -> None:
        self.value = value
        self.next = next

def last_node(start_node: 'LLNode') -> 'LLNode':
    front_node = start_node
    if front_node.next:
        while front_node.next:
            front_node = front_node.next
    if not front_node.next:
        return front_node.value
    else:
        return start_node.value

