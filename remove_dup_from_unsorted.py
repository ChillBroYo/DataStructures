# Remove duplicates from an Unsorted Doubly Linked List. Bonus: Do not use a intermittent buffer
from doubly_linked_list import DoublyLinkedList

# First soultion use a hashtable buffer to do one sweep
def dedup(unsorted_list):
    char_store = {}
    for x in unsorted_list:
        if char_store.get(x.value) == None:
            char_store[x.value] = 1
        else:
            unsorted_list.remove(x.value)

    return unsorted_list

# O(1) memory usage solution
def dedup_smaller(unsorted_list):
    for x in range(unsorted_list.count):
        unsorted_list[x:].remove(unsorted_list[x])
    
    return unsorted_list

if __name__ == "__main__":
    # var = DoublyLinkedList()
    # var.add(1)
    # var.add(2)
    # var.add(3)
    # var.add(2)
    # var.print_list()
    # print("-----")
    # var = dedup(var)
    # var.print_list()
    # print("-----")
    # print("-----")

    # var = DoublyLinkedList()
    # var.add(1)
    # var.add(2)
    # var.add(2)
    # var.add(2)
    # var.print_list()
    # print("-----")
    # var = dedup(var)
    # var.print_list()
    # print("-----")
    # print("-----")

    var = DoublyLinkedList()
    var.add(1)
    var.add(2)
    var.add(2)
    var.add(2)
    var.print_list()
    print("-----")
    var = dedup_smaller(var)
    var.print_list()