# Create a singly linked list
from singly_linked_node import SinglyLinkedNode

class SinglyLinkedList:
    def __init__(self):
       self.head = None
    
    def add(self, value):
        if self.head.value == None:
            self.head.value = value
        else:
            temp_val = self.head
            while temp_val.next != None:
                temp_val = temp_val.next
        
            temp_val.add_next(value)
    
    def remove(self, value):
        if self.head == None:
            print("No head")
            return False
        elif self.head.next == None and self.head.value == value:
            self.head = None
            print("remove only item from head")
            return True
        elif self.head.value == value:
            self.head = self.head.next
            print("remove item from head")
            return True
        else:
            temp_val = self.head
            while temp_val.next != None:
                if temp_val.next.value == value:
                    temp_val.remove_next()
                    print("Remove item")
                    return True
                temp_val = temp_val.next

            print("Didn't find it")
            return False

    def print_list(self):
        temp_val = self.head
        if temp_val != None:
            print(temp_val.value)
            while temp_val.next != None:
                temp_val = temp_val.next
                print(temp_val.value)
        

if __name__ == "__main__":
    singly_list = SinglyLinkedList()
    singly_list.add(1)
    singly_list.add(2)
    singly_list.add(3)
    singly_list.print_list()
    singly_list.remove(3)
    singly_list.print_list()
    singly_list.remove(2)
    singly_list.print_list()
    singly_list.remove(1)
    singly_list.print_list()
