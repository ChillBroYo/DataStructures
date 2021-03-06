# Create a Doubly Linked list
from doubly_linked_node import DoublyLinkedNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.counter_val = None
        self.count = 0

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

    def get(self, val):
        if self.head == None:
            return -1
        else:
            count = 0
            temp_val = self.head
            while temp_val.next != None:
                if temp_val.value == val:
                    return count
                else:
                    temp_val = temp_val.next
                count += 1
            
            return -1
        
    def get_at_index(self, index):
        # print("11111" + str(index))
        if self.head == None:
            return IndexError("No values exist")
        elif index == 0:
            return self.head
        else:
            count = 0
            temp_val = self.head
            while count != index:
                if temp_val.next == None:
                    raise IndexError(str.format("Index {} doesn't exist", index))
                temp_val = temp_val.next
                count += 1
            
            if count != index:
                raise IndexError(str.format("Index {} doesn't exist", index))
            
        return temp_val
    
    def remove_duplicates(self, val):
        if self.head == None:
            return False
        
        count = 0
        has_appeared = False
        temp_val = self.head
        while temp_val != None or temp_val.next != None:
            if temp_val.value == val and has_appeared:
                pass
                # TODO
        
    
    def add(self, value):
        if self.head == None:
            self.head = DoublyLinkedNode(value)
        else:
            temp_val = self.head
            while temp_val.next != None:
                temp_val = temp_val.next
            
            temp_val.next = DoublyLinkedNode(value)
            temp_val.next.prev = temp_val
        self.count += 1
    
    def add_at_front(self, value):
        if self.head == None:
            self.head = DoublyLinkedNode(value)
        else:
            temp_val = DoublyLinkedNode(value)
            temp_val.next = self.head
            self.head = temp_val
        self.count += 1

    def remove_end(self):
        if self.head == None:
            raise IndexError("Empty List")
        if self.count == 1:
            self.head = None
            self.count -= 1
            return

        temp_val = self.head
        for x in range(1, self.count):
            temp_val = temp_val.next

        temp_val.remove()
        self.count -= 1

    def remove_at_index(self, index):
        if index >= self.count:
            return False
        
        if index == 0 and self.count > 1:
            temp_val = self.head
            self.head = self.head.next
            temp_val.remove()
            self.count -= 1
            return True
        elif index == 0:
            temp_val = self.head
            self.head = None
            temp_val.remove()
            self.count -= 1
            return True

        temp_val = self.head
        for x in range(1, index):
            temp_val = temp_val.next
        
        temp_val.remove()
        self.count -= 1
        return True

    def remove(self, value, remove_all=False):
        if self.head == None:
            return False
        elif self.head.value == value and self.head.next == None:
            self.head = None
            self.count -= 1
            return True
        elif self.head.value == value and self.head.next != None:
            self.head.next.prev = None
            self.head = self.head.next
            self.count -= 1
            return True
        else:
            temp_val = self.head
            while temp_val.next != None:
                #print(str.format("self.tv.value = {}",temp_val.value))
                #print(str.format("self.tvn.value = {}",temp_val.next.value))
                if temp_val.next.value == value and temp_val.next.next != None:
                    #print(str.format("Entered here"))
                    next = temp_val.next.next
                    temp_val.next.next.prev = temp_val
                    temp_val.next.prev = None
                    temp_val.next.next = None
                    temp_val.next = next
                    if remove_all == False:
                        break
                elif temp_val.next.value == value and temp_val.next.next == None:
                    #print(str.format("Entered there"))
                    temp_val.next.prev = None
                    temp_val.next = None
                    if remove_all == False:
                        break
                else:
                    temp_val = temp_val.next
            self.count -= 1

    def print_list(self, return_string=False):
        val = ""
        if self.head == None:
            val += "Empty List"
            return val
        
        temp_val = self.head
        while temp_val.next != None and temp_val.value != None:
            val += str(temp_val.value)
            val += "\n"
            temp_val = temp_val.next
            
        val += str(temp_val.value)
        if return_string == True:
            return val
        print(val)


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