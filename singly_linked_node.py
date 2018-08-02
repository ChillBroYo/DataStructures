# Define a singly Linked node

class SinglyLinkedNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def add_next(self, value):
        self.next = SinglyLinkedNode(value)

    def remove_next(self):
        self.next = self.next.next