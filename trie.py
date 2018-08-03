# create Trie data structure
from trie_node import TrieNode

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
            self.dfs_helper(self.root, child)

    
    def dfs_helper(self, parent, node_to_search_through):
        # print(parent.children[node_to_search_through])
        if len(parent.children[node_to_search_through].children) == 0:
            print (parent.children[node_to_search_through].value)
            return
        else:
            print (parent.children[node_to_search_through].value)
            for child in parent.children[node_to_search_through].children:
                self.dfs_helper(parent.children[node_to_search_through], child)

var = Trie()
# var.root = TrieNode(1)
# print(var.root.value)
val = TrieNode(1)
val.add_child(2)
val.children[2].add_child(6)
val.add_child(3)
var.root = val
var.dfs_traversal_print()