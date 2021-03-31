# Create a queue class with sys
import sys
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self, size=sys.maxsize):
        self.max_size = size
        self.storage = DoublyLinkedList()
        self.size = 0
    
    def enqueue(self, val):
        if self.size >= self.max_size:
            raise MemoryError("Queue is full")
        
        self.storage.add(val)
        self.size += 1
    
    def dequeue(self):
        if self.size < 1:
            raise MemoryError("Queue is empty")
        
        self.storage.remove_at_index(0)
        self.size -= 1
    
    def peek(self):
        if self.size < 1:
            return "None"

        return self.storage.get_at_index(0).value
    
    def __str__(self):
        return self.storage.print_list(True)


if __name__ == "__main__":
    var = Queue()
    var.enqueue(1)
    var.enqueue(2)
    var.enqueue(3)
    print(var)
    print("-----")
    var.dequeue()
    var.dequeue()
    print(var)
    print("-----")
    print(var.peek())
