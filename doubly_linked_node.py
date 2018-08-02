# Create a doubly linked list node

class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __iter__(self):
        return self.value

    def remove(self):
        if self.next == None and self.prev == None:
            self.value = None
        elif self.next == None:
            self.value == None
            self.prev.next = None
            self.prev = None
        else:
            self.value == None
            self.next.prev = None
            self.prev.next = None
            self.prev = None
            self.next = None
