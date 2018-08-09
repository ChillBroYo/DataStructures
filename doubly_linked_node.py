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
            del self
        elif self.next == None:
            self.prev.next = None
            self.prev = None
            del self
        elif self.prev == None:
            self.next.prev = None
            self.next = None
            del self
        # has both sides
        else:
            self.next.prev = self.prev
            self.prev.next = self.next
            self.prev = None
            self.next = None
            del self
