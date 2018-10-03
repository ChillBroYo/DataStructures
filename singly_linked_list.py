# Create a singly linked list
from singly_linked_node import SinglyLinkedNode
import copy

class SinglyLinkedList:
    def __init__(self):
       self.head = None
       self.count = 0
    
    # Add new node to the end of the list
    def append(self, value):
        # Special head insertion
        if self.head == None:
            self.head = SinglyLinkedNode(value)
        else:
            # Move to end of list and add value
            temp_val = self.head
            while temp_val.next != None:
                temp_val = temp_val.next
        
            temp_val.add_after(value)
        self.count += 1
    
    # Insert a new value at the specified location in the list if it exists
    def insert(self, value, location):
        if location > self.count or location < 0:
            return False
        
        # Sepcial head insertion
        if location == 0:
            if self.head == None:
                self.head = SinglyLinkedNode(value)
            else:
                val = copy.deepcopy(self.head)
                self.head = SinglyLinkedNode(value)
                self.head.next = val
        else:
            # Since adding elements is based on the next node, move to the node before target
            # location and add element after
            temp_val = self.head
            for x in range(location - 1):
                temp_val = temp_val.next
            
            temp_val.add_after(value)

        self.count += 1
        return True
    
    # Remove a value from the list
    def remove(self, value):
        if self.head == None:
            return False
        
        # Specialized head removal
        elif self.head.value == value:
            if self.head.next != None:
                var = copy.deepcopy(self.head.next)
                del self.head
                self.head = var
            else:
                self.head = None
            
            self.count -= 1
            return True

        
        temp_val = self.head
        success = False

        # Go through entire list and if the element exists remove it
        for x in range(self.count - 1):
            if temp_val.next != None and temp_val.next.value == value:
                temp_val.remove_after()
                success = True
                break

            temp_val = temp_val.next
        
        # Return true if the remove was successful, false if not
        if success == False:
            return False
        else:
            self.count -= 1
            return True

    # Removes every instance of specificed value
    def bulk_remove(self, value):
        if self.head == None:
            return False
        
        # Remove every instance of specified value after the head
        temp_val = self.head
        while temp_val != None and temp_val.next != None:

            # Removal step to skip the elements that are removed, essentially removing them
            while temp_val.next != None and temp_val.next.value == value:
                self.count -= 1
                temp_val.next = temp_val.next.next

            temp_val = temp_val.next
        
        # If the head is matching the specified value as well, remove it
        if self.head.value == value and self.head.next != None:
            self.count -= 1
            self.head = self.head.next
        elif self.head.value == value:
            self.count -= 1
            self.head = None
        
        return True

    # Removes a value at the index specified, if the index exists in the currrent set
    def remove_at_index(self, location):
        if location < 0 or location > self.count or self.head = None:
            return False
        
        temp_val = self.head
        if location == 0:
            self.head = self.head.next
        for x in range(location - 1):
            temp_val = temp_val.next
        
        temp_val.remove_after()
        return True

    # Empties list
    def empty(self):
        self.head = None

    # Prints out the singly linked list in head-first order
    def print_list(self):
        temp_val = self.head
        count = 0
        print(">>")
        while temp_val != None:
            count += 1
            if count == 1:
                print(str.format("{}", temp_val.value), end="")
            else:
                print(str.format(",{}", temp_val.value), end="")
            temp_val = temp_val.next
            if count % 10 == 0:
                print("")   
        if count + 1 % 10 == 0:
            print("<<")
        else:
            print("\n<<")

if __name__ == "__main__":
    singly_list = SinglyLinkedList()
    singly_list.append(1)
    singly_list.append(2)
    singly_list.append(3)
    singly_list.print_list()
    singly_list.remove(3)
    singly_list.print_list()
    singly_list.remove(2)
    singly_list.print_list()
    singly_list.remove(1)
    singly_list.print_list()
    for x in range(25):
        singly_list.append(x)
    singly_list.print_list()
    for x in range(25):
        singly_list.append(1)
    singly_list.print_list()
    singly_list.bulk_remove(1)
    singly_list.print_list()
    singly_list.insert("xx", 23)
    singly_list.print_list()
    singly_list.insert("xxz", 0)
    singly_list.print_list()
    singly_list.empty()
    singly_list.print_list()
