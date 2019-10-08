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
            self.tail = self.head
            self.size += 1
            return
        
        iter_node = self.head
        while iter_node.next != None:
            iter_node = iter_node.next
        iter_node.next = DoublyLinkedNode(val)
        self.tail = iter_node.next
        self.size += 1
    
    def remove(self, val):
        if self.head == None:
            return False

        if self.head.value == val and self.head.next == None:
            self.head = None
            self.tail = None
        elif self.head.value == val and self.head.next != None:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            iter_node = self.head
            while iter_node.next != None:
                if iter_node.next.value == val:
                    if iter_node.next == self.tail:
                        self.tail = iter_node
                    iter_node.remove_next()
                    self.size -= 1
                    return True
            return False
        self.size -= 1
        return True
    
    def remove_all(self, val):
        while self.remove(val) == True:
            pass
    
    def remove_index(self, index):
        if index < 0 or index > self.size - 1:
            return False
        
        if index == 0 and self.head.next == None:
            self.head = None
            self.tail = None
        elif index == 0 and self.head.next != None:
            self.head.next.prev = None
            self.head = self.head.next
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.remove_next()
        else:
            count = 0
            iter_node = self.head
            while count != index:
                iter_node = iter_node.next
                count += 1
            iter_node.prev.remove_next()
            self.size -= 1
        self.size -= 1
        return True

    def print(self):
        if self.head == None:
            print("Empty")
        
        iter_node = self.head
        while iter_node != None:
            print(iter_node.value)
            iter_node = iter_node.next

class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.i_list = DoublyLinkedList()

    def push(self, val):
        if self.size == self.max_size:
            print("Stack is full")
            return False

        self.i_list.add(val)
        self.size += 1
        return True
    
    def pop(self):
        if self.size == 0:
            print("Stack is empty")
            return False
        
        self.i_list.remove(self.i_list.head.value)
        self.size -= 1
        return True
    
    def print(self):
        self.i_list.print()

class Queue:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.i_list = DoublyLinkedList()
    
    def enqueue(self, val):
        if self.size == self.max_size:
            print("Queue is full")
            return False
        
        self.i_list.add(val)
        self.size += 1
        return True
    
    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return False
        
        self.i_list.remove_index(self.size - 1)
        self.size -= 1
        return True

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

    dllist = DoublyLinkedList()
    dllist.add(1)
    dllist.add(2)
    dllist.print()
    dllist.remove(1)
    dllist.print()
    dllist.add(2)
    dllist.add(2)
    print(dllist.tail.value)
    print(dllist.size)
    dllist.print()
    dllist.remove_all(2)
    dllist.print()

    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.print()
    stack.pop()
    print(stack.size)
    stack.print()
