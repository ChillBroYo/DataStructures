# Create a queue
import sys
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self, size=sys.maxsize):
        self.max_size = size
        self.storage = DoublyLinkedList()
        self.size = 0
        self.counter_val = None
    
    def __str__(self):
        return self.storage.print_list(True)
    
    def __len__(self):
        return self.size

    def __iter__(self):
        if self.size < 1:
            return None

        self.counter_val = self.storage.get_at_index(0)
        return self.storage.get_at_index(0)

    
    def __next__(self):
        if self.counter_val == None:
            raise StopIteration
        if self.counter_val.next != None:
            self.counter_val = self.counter_val.next
            return self.counter_val.prev
        else:
            temp_val = self.counter_val
            self.counter_val = self.counter_val.next
            return temp_val

    def enqueue(self, val):
        if self.size >= self.max_size:
            raise MemoryError("Queue is full")
        
        self.storage.add(val)
        self.size += 1
    
    def dequeue(self):
        if self.size < 1:
            raise MemoryError("Queue is empty")
        
        val = self.storage.get_at_index(0)
        self.storage.remove_at_index(0)
        self.size -= 1
        return val.value
    
    def peek(self):
        if self.size < 1:
            return "None"

        return self.storage.get_at_index(0).value


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
