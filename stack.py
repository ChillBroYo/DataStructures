# Create a stack
from doubly_linked_list import DoublyLinkedList


class Stack():
    def __init__(self,size):
        self.max_size = size
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, val):
        if self.size >= self.max_size:
            raise MemoryError("Stack is full")

        self.storage.add(val)
        self.size += 1
    
    def pop(self):
        if self.size > 0:
            self.storage.remove_end()
            self.size -= 1
            return True
        else:
            return False

    def peek(self):
        if self.size > 0:
            return self.storage.get_at_index(self.size - 1).value

    def __str__(self):
        val = self.storage.print_list(True)
        var = val.split("\n")
        final_val = ""
        for x in range(len(var)):
            final_val += var[len(var) - x - 1]
            if x < len(var) - 1:
                final_val += "\n"
        
        return final_val
        
if __name__ == "__main__":
    var = Stack(3)
    var.push(1)
    print(str(var))
    print("-----")
    print(var.peek())
    print("--+--+--")
    var.push(2)
    print(str(var))
    print("-----")
    print(var.peek())
    print("--+--+--")
    var.push(3)
    print(str(var))
    print("-----")
    print(var.peek())
    print("--+--+--")
    var.pop()
    print(str(var))
    print("-----")
    print(var.peek())
    print("--+--+--")
    var.pop()
    print(str(var))
    print("-----")
    print(var.peek())
    print("--+--+--")
    var.pop()
    print(str(var))
    print("-----")
    print(var.peek())
    print("--+--+--")
    var.pop()
    print(str(var))
    print("-----")
    print(var.peek())
    print("--+--+--")
    var.push(1)
    var.push(2)
    var.push(3)
    try:
        var.push(4)
    except:
        print(var)
