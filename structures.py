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
        iter_node.next.prev = iter_node
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
    
    def print(self):
        self.i_list.print()

class BinarySearchTree:
    def __init__(self, self_balancing):
        self.head = None
        self.size = 0
    
    def insert(self, val):
        if self.head == None:
            self.head = BinaryNode(None, val)
            self.size += 1
            return
        
        iter_node = self.head
        while iter_node != None:
            if iter_node.value == val:
                pass
            elif iter_node.value < val and iter_node.right == None:
                iter_node.right = BinaryNode(iter_node, val)
                self.size += 1
                break
            elif iter_node.value > val and iter_node.left == None:
                iter_node.left = BinaryNode(iter_node, val)
                self.size += 1
                break
            elif iter_node.value < val:
                iter_node = iter_node.right
            elif iter_node.value > val:
                iter_node = iter_node.left
        
    def remove(self, val):
        if self.head == None:
            return False
        
        if self.head.value == val and self.head.left == None and self.head.right == None:
            self.head = None
        elif self.head.value == val and self.head.left == None and self.head.right != None:
            self.head = self.head.right
        elif self.head.value == val and self.head.left != None and self.head.right == None:
            self.head = self.head.left
        else:
            l_path = False
            iter_node = self.head
            while iter_node != None:
                if iter_node.value != val and iter_node.left == None and iter_node.right == None:
                    return False
                elif iter_node.value < val and iter_node.right == None:
                    return False
                elif iter_node.value > val and iter_node.left == None:
                    return False
                
                if iter_node.value == val and iter_node.left == None and iter_node.right == None:
                    if l_path == True:
                        iter_node.parent = None
                        iter_node.parent.left = None
                    else:
                        iter_node.parent = None
                        iter_node.parent.right = None
                elif iter_node.value == val and iter_node.left != None and iter_node.right == None:
                    if l_path == True:
                        iter_node.left.parent = iter_node.parent
                        iter_node.parent.left = iter_node.left
                    else:
                        iter_node.left.parent = iter_node.parent
                        iter_node.parent.right = iter_node.left
                elif iter_node.value == val and iter_node.left == None and iter_node.right != None:
                    if l_path == True:
                        iter_node.right.parent = iter_node.parent
                        iter_node.parent.left = iter_node.right
                    else:
                        iter_node.right.parent = iter_node.parent
                        iter_node.parent.right = iter_node.left
                elif iter_node.value == val and iter_node.left != None and iter_node.right != None:
                    if l_path == True:
                        lr_val = iter_node.right
                        iter_node.left.parent = iter_node.parent
                        iter_node.parent.left = iter_node.left
                        farthest_rl = iter_node.parent.right
                        if farthest_rl == None:
                            iter_node.parent.right = lr_val
                            lr_val.parent = iter_node.parent.right
                        else:
                            while farthest_rl.left == None:
                                farthest_rl = farthest_rl.left
                            farthest_rl.left = lr_val
                            lr_val.parent = farthest_rl.left
                    else:
                        lr_val = iter_node.right
                        iter_node.left.parent = iter_node.parent
                        iter_node.parent.right = iter_node.left
                        farthest_rl = iter_node.parent.right
                        if farthest_rl == None:
                            iter_node.parent.right = lr_val
                            lr_val.parent = iter_node.parent.right
                        else:
                            while farthest_rl.left == None:
                                farthest_rl = farthest_rl.left
                            farthest_rl.left = lr_val


                    



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
    
class BinaryNode:
    def __init__(self, parent, val):
        self.parent = parent
        self.value = val
        self.right = None
        self.left = None

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

    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print()
    queue.dequeue()
    print(queue.size)
    queue.print()