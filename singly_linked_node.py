# Define a singly Linked node
import copy

class SinglyLinkedNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    # Adds a node to the next slot
    def add_after(self, value):
        if self.next == None:
            self.next = SinglyLinkedNode(value)
        else:
            val = copy.deepcopy(self.next)
            self.next = SinglyLinkedNode(value)
            self.next.next = val

    # Removes the next item
    def remove_after(self):
        if self.next == None:
            raise Exception("Attempting to remove a non-existent item")

        removed_value = None

        # If the target item exists and has a following item, connect the prev to the following
        if self.next and self.next.next:
            removed_value = copy.copy(self.next.value)
            self.next = self.next.next
        # If there is no following item, null out next value
        elif self.next:
            removed_value = copy.copy(self.next.value)
            self.next = None

        return removed_value

        