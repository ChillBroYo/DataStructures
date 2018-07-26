# Define a singly Linked node

class SinglyLinkedNode:
    next = None
    value = None

    def __init__(self, value=None):
        self.value = value
    
    def add_next(self, value):
        self.next = SinglyLinkedNode(value)

    def remove_next(self):
        self.next = self.next.next