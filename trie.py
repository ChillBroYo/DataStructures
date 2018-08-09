# create Trie data structure
from trie_node import TrieNode
from collections import deque

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        self.count = 0
    
    def dfs_traversal_print(self):
        if self.root == None:
            print("None")
            return False

        print (self.root.value)
        for child in self.root.children:
            # print(child)
            self.dfs_helper(self.root.children[child])

    
    def dfs_helper(self, node_to_search_through):
        # print(parent.children[node_to_search_through])
        if len(node_to_search_through.children) == 0:
            print (node_to_search_through.value)
            return
        else:
            print (node_to_search_through.value)
            for child in node_to_search_through.children:
                self.dfs_helper(node_to_search_through.children[child])

    def bfs_traversal(self):
        if self.root == None:
            return False
        
        print (self.root.value)
        queue = deque()
        for index in self.root.children:
            queue.append(self.root.children[index])
        
        while len(queue) > 0:
            val = queue.pop()
            print(val.value)
            for child in val.children:
                queue.append(val.children[child])
        
        return True



var = Trie()
# var.root = TrieNode(1)
# print(var.root.value)
val = TrieNode(1)
val.add_child(2)
val.children[2].add_child(6)
val.children[2].children[6].add_child(7)
val.add_child(3)
var.root = val
var.dfs_traversal_print()
print("_____")
var.bfs_traversal()