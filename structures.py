class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, val):
        if self.head == None:
            self.head = SinglyLinkedNode(val)
            self.size += 1
            return
        
        iter_node = self.head
        while iter_node.next != None:
            iter_node = iter_node.next
        
        iter_node.next = SinglyLinkedNode(val)
        self.size += 1

    def remove(self, val):
        if self.head == None:
            return False
        
        if self.head.value == val and self.head.next == None:
            self.head = None
        elif self.head.value == val and self.head.next != None:
            self.head = self.head.next
        else:
            iter_node = self.head
            while iter_node.next != None:
                if iter_node.next.value == val:
                    iter_node.remove_next()
                    self.size -= 1
                    return True
            return False
        self.size -= 1
        return True

    def remove_all(self, val):
        while self.remove(val) == True:
            pass
    
    def print(self):
        if self.head == None:
            print("Empty")
            return
        
        iter_node = self.head
        while iter_node != None:
            print(iter_node.value)
            iter_node = iter_node.next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, val):
        if self.head == None:
            self.head = DoublyLinkedNode(val)

class SinglyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def remove_next(self):
        self.next = self.next.next

class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
    def remove_next(self):
        if self.next.next != None:
            self.next.next.prev = self
        self.next = self.next.next
        return True
    
    def remove_before(self):
        self.next.prev = self.prev
        self.prev.next = self.next

if __name__ == "__main__":
    sllist = SinglyLinkedList()
    sllist.add(1)
    sllist.add(2)
    sllist.print()
    sllist.remove(1)
    sllist.print()
    sllist.add(2)
    sllist.add(2)
    print(sllist.size)
    sllist.print()
    sllist.remove_all(2)
    sllist.print()
