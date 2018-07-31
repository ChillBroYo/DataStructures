# Create a doubly linked list node

class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __iter__(self):
        return self.value
