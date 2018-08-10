# create Trie data structure
from trie_node import TrieNode
from collections import deque
from queue import Queue

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

    def bfs_traversal_custom_queue(self):
        if self.root == None:
            return False
        
        print (self.root.value)
        queue = Queue()
        for index in self.root.children:
            queue.enqueue(self.root.children[index])
        
        while len(queue) > 0:
            val = queue.dequeue()
            print(val.value)
            for child in val.children:
                queue.enqueue(val.children[child])
        
        return True


if __name__ == "__main__":
    var = Trie()
    # var.root = TrieNode(1)
    # print(var.root.value)
    val = TrieNode(1)
    val.add_child(2)
    val.add_child(3)
    val.children[2].add_child(4)
    val.children[2].add_child(5)
    val.children[3].add_child(6)
    val.children[3].add_child(7)
    val.children[2].children[4].add_child(8)
    val.children[3].children[6].add_child(9)
    val.add_child(10)
    var.root = val
    var.dfs_traversal_print()
    print("-----")
    var.bfs_traversal()
    print("-----")
    var.bfs_traversal_custom_queue() 