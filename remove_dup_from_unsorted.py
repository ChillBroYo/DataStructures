# Remove duplicates from an Unsorted Doubly Linked List. Bonus: Do not use a intermittent buffer
from doubly_linked_list import DoublyLinkedList

# First soultion use a hashtable buffer to do one sweep
def dedup(unsorted_list):
    char_store = {}
    for x in unsorted_list:
        if char_store.get(x.value) == None:
            print("unique")
            char_store[x.value] = 1
        else:
            print("remove")
            unsorted_list.remove(x.value)

    return unsorted_list

var = DoublyLinkedList()
var.add(1)
var.add(2)
var.add(3)
var.add(2)
var.print_list()
print("-----")
var = dedup(var)
print("-----")
var.print_list()

var = DoublyLinkedList()
var.add(1)
var.add(2)
var.add(2)
var.add(2)
var.print_list()
print("-----")
var = dedup(var)
print("-----")
var.print_list()