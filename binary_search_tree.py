# Create a Binary search tree
from binary_node import BinaryNode
from custom_queue import custom_queue

class BinarySeachTree:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def add(self, value):
        if self.root == None:
            self.root = BinaryNode(value)
            return
        
        val = find(value)
        if val.value == value:
            pass
        elif val.value > value:
            val.left = BinaryNode(value, val)
        else:
            val.right = BinaryNode(value, val)
        
    def remove(self, value):
        if self.root == None:
            return False
        elif self.root.value == value:
            self.root = None
            return value
        
        val = find(value)
        return_value = None
        if val.value == value:
            return_value = value
            if val.left and val.right and val.parent and val.parent.right == val:
                val.parent.right = val.right
                all__left_values = self.get_all_nodes_bfs(val.left, True)
                # del val.left
                del val
                for value in all_left_values:
                    self.add(value)
                return value
            elif val.left and val.right and val.parent and val.parent.left == val:
                val.parent.left = val.left
                all__right_values = self.get_all_nodes_bfs(val.right, True)
                # del val.right
                del val
                for value in all_right_values:
                    self.add(value)
                return value
        return False


    def get_all_nodes_bfs(self, start_node, values):
        if start_node == None:
            return []

        queue = custom_queue()
        visited = []
        queue.enqueue(start_node)
        while queue.count != 0:
            val = queue.dequeue()
            visited.append(val)
            if val.left:
                unvisited.enqueue(val.left)
            if val.right:
                unvisited.enqueue(val.right)
        
        if values:
            return_val = []
            for item in visited:
                return_val.append(item.value)
            return return_val
        return visited
        
    
    def find(self, value, curr_node):
        if curr_node.value == value:
            return curr_node
        
        if curr_node.left == None and curr_node.right == None:
            return curr_node
        elif curr_node.value > value:
            if curr_node.left != None:
                return curr_node.left
            else:
                return curr_node
        else:
            if curr_node.right != None:
                return curr_node.right
            else:
                return curr_node