# Create a Doubly Linked list
from doubly_linked_node import DoublyLinkedNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.counter_val = None

    def __iter__(self):
        if self.head:
            self.counter_val = self.head
            return self
        return "Empty List"
    
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

        
        
    
    def add(self, value):
        if self.head == None:
            self.head = DoublyLinkedNode(value)
        else:
            temp_val = self.head
            while temp_val.next != None:
                temp_val = temp_val.next
            
            temp_val.next = DoublyLinkedNode(value)
            temp_val.next.prev = temp_val

    def remove(self, value):
        if self.head == None:
            return False
        elif self.head.value == value and self.head.next == None:
            self.head = None
            return True
        elif self.head.value == value and self.head.next != None:
            self.head.next.prev = None
            self.head = self.head.next
            return True
        else:
            print(str.format("self.head.value = {}",self.head.value))
            temp_val = self.head
            while temp_val.next != None:
                if temp_val.next.value == value and temp_val.next.next != None:
                    next = temp_val.next.next
                    temp_val.next.next.prev = temp_val
                    temp_val.next.prev = None
                    temp_val.next.next = None
                    temp_val.next = next
                elif temp_val.next.value == value and temp_val.next.next == None:
                    temp_val.next.prev = None
                    temp_val.next = None
                temp_val = temp_val.next

    def print_list(self):
        if self.head == None:
            print("Empty List")
            return
        
        temp_val = self.head
        while temp_val.next != None and temp_val.value != None:
            print(temp_val.value)
            temp_val = temp_val.next
            
        print(temp_val.value)


if __name__ == "__main__":
    var = DoublyLinkedList()
    var.add(1)
    var.add(2)
    var.add(3)
    var.add(4)
    var.add(5)
    var.print_list()
    print("-----")
    var.remove(3)
    var.print_list()
    print("-----")
    var.remove(2)
    var.print_list()
    print("-----")
    var.remove(1)
    var.print_list()
    print("-----")
    var.remove(4)
    var.print_list()
    print("-----")
    var.remove(5)
    var.print_list()
    print("-----")
    var.remove(1)
    var.print_list()
    print("-----")
    var.add(1)
    var.print_list()
    print("-----")
    var.remove(1)
    var.print_list()