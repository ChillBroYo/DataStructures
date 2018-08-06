# Create a stack
from doubly_linked_list import DoublyLinkedList


class Stack():
    def __init__(self,size):
        self.max_size = size
        self.size = 0
        self.storage = DoublyLinkedList()

    def add(self, val):
        if self.size < self.max_size:
            pass
    