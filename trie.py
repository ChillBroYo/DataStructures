# create Trie data structure
# STD Library workaround for same name values
import heapq
from custom_queue import CustomQueue
from trie_node import TrieNode
from collections import deque
from graph_node_connection import GraphNodeConnection # TODO: Remove from this as incorrect scope

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        self.count = 0
    
    def debug_log_helper_root(self, debug, val):
        if debug == True:
            return str.format("{} --> ", val)
        else:
            return str.format("{} \n ", val)

    def debug_log_helper_child(self, debug, val1, val2):
        if debug == True:
            return str.format("{} --> {}", val1, val2)
        else:
            return str.format("{} \n ", val1)

    def debug_log_helper_childless(self, debug, val):
        if debug == True:
            return str.format("{} <<< \n ", val)
        else:
            return str.format("{} \n ", val)


    def shortest_path(self, value_to_find, debug=False):
        string_to_return = ""
        if self.root == None:
            raise TypeError("There is no root to the Trie")
        elif self.root.value == value_to_find:
            return {
                    "shortest_path_value" : self.root.value,
                    "shortest_path" : self.root,
                    "string_path" : ""
            }
        
        # [0] Boolean is it found, [1] In order array of nodes traversed through, [2] string node path,
        # [3] distance (vertex to vertex addition)
        return_val = self.shortest_path_bfs(value_to_find, debug)
        return {
                "shortest_path_value" : return_val[3],
                "shortest_path" : return_val[1],
                "string_path" : return_val[2]
        }
        
    # will Only work with connections (not in correct scope) TODO: Move TO graph
    def shortest_path_bfs(self, value_to_find, debug):
        return_value = [False, [], "", 0]
        paths = {}
        prev_node = self.root
        min_heap = self.custom_bfs()[0]
        heapq.heapify(min_heap)
        
        while len(min_heap) > 0:
            val = min_heap.pop()
            return_value[2] += self.debug_log_helper_root(debug, val.start_node.value)

            if paths == {}:
                paths[val.end_node] = [val.end_node, val.value, [val.start_node]]
            else:
                if paths.get(val.end_node) == None:
                    var = paths[val.start_node][2]
                    var.append(val.start_node)
                    path_val = paths[val.start_node][1]
                    path_val += val.start_node.value 
                    paths[val.end_node] = [val.end_node, path_val, var]
                else:

            
            if val.end_node.value == value_to_find and paths[val._node]:
                return_value[0] = True
                return_value[1] = paths[val.end_node][2]
                return_value[2] += self.debug_log_helper_root(debug, val.end_node.value)
                return_value[3] = paths[val.end_node][1]
                break
            
            for path in paths:
                if paths[path][0] != val.start_node:
                    paths[path] = -1
        
        return return_value

        
        


    # Traversal distance counts as each node it touches
    def dfs_traversal_print(self, value_to_find, debug=False):
        string_to_return = ""
        if self.root == None:
            raise TypeError("There is no root to the Trie")
        elif self.root.value == value_to_find:
            return {
                    "distance_to_value" : self.root.value,
                    "value_object" : self.root,
                    "string_path" : ""
            }
        
        # [0] Boolean is it found, [1] node found, [2] string node path, [3] distance (vertex to vertex addition)
        return_val = self.dfs_traversal_find(value_to_find, debug)
        string_to_return += return_val[2]
        if return_val[0] == False:
            return {
                "distance_to_value" : -1,
                "value_object" : None,
                "string_path" : string_to_return
            }
        else:
            return {
                "distance_to_value" : return_val[3] + self.root.value,
                "value_object" : return_val[1],
                "string_path" : string_to_return
            }



    def dfs_traversal_find(self, value_to_find, debug):
        return_value = [False, None, "", 0]
        for child in self.root.children:
            return_value[2] += self.debug_log_helper_root(debug, self.root.value)
            val = self.dfs_helper(self.root.children[child], debug, value_to_find)

            # [0] Boolean is it found, [1] node found, [2] string node path, [3] distance (vertex to vertex addition)
            return_value[0] = val[0]
            return_value[1] = val[1]
            return_value[2] += val[2]
            return_value[3] += val[3]
            if return_value[0] == True:
                break
        
        return return_value

    
    def dfs_helper(self, node_to_search_through, debug, value_to_find):
        return_value = [False, node_to_search_through, "", node_to_search_through.value]

        # Priority: If value matches --> If the child is childless --> Check Children
        if node_to_search_through.value == value_to_find:
            return_value[2] += self.debug_log_helper_child(debug, node_to_search_through.value, "<< Item Found")
            return_value[0] = True
            return return_value
        elif len(node_to_search_through.children) == 0:
            # [0] Boolean is it found, [1] node found, [2] string node path, [3] distance (vertex to vertex addition)
            return_value[2] = self.debug_log_helper_childless(debug, node_to_search_through.value)
            return return_value
        else:
            for child in node_to_search_through.children:
                return_value[2] += self.debug_log_helper_root(debug, node_to_search_through.value)
                val = self.dfs_helper(node_to_search_through.children[child], debug, value_to_find)
                return_value[0] = val[0]
                return_value[1] = val[1]
                return_value[2] += val[2]
                return_value[3] += val[3]
                if return_value[0] == True:
                    break

            return return_value


    # Traversal distance counts as each node it touches
    def bfs_traversal_print(self, value_to_find, **kwargs):
        if self.root == None:
            raise TypeError("There is no root to the Trie")
        elif self.root.value == value_to_find:
            return {
                    "distance_to_value" : self.root.value,
                    "value_object" : self.root,
                    "string_path" : ""
            }
        
        # [0] Boolean is it found, [1] node found, [2] string node path, [3] distance (vertex to vertex addition)
        if kwargs.get("use_custom_queue") == None:
            return_val = self.bfs_traversal_find(value_to_find, kwargs.get("debug"))
        else:
            return_val = self.bfs_traversal_find_custom_queue(value_to_find, kwargs.get("debug"))
        if return_val[0] == False:
            return {
                "distance_to_value" : -1,
                "value_object" : None,
                "string_path" : return_val[2]
            }
        else:
            return {
                "distance_to_value" : return_val[3],
                "value_object" : return_val[1],
                "string_path" : return_val[2]
            }



    def bfs_traversal_find(self, value_to_find, debug):
        return_value = [False, None, "", 0]
        queue = deque()

        queue.append(self.root)
        while len(queue) > 0:
            val = queue.popleft()
            return_value[1] = val
            return_value[3] += val.value

            if val.value == value_to_find:
                return_value[0] = True
                return_value[2] += self.debug_log_helper_child(debug, val.value, "<< Item Found")
                break

            return_value[2] += self.debug_log_helper_root(debug, val.value)
            for child in val.children:
                queue.append(val.children[child])
        return return_value
    
    def bfs_traversal(self, debug=False):
        return_value = [[],""]
        queue = deque()

        queue.append(self.root)
        while len(queue) > 0:
            val = queue.popleft()
            return_value[0].append(val)
            return_value[1] += self.debug_log_helper_root(debug, val.value)
            for child in val.children:
                queue.append(val.children[child])

        return return_value
    
    # Builds and returns connections between nodes
    def custom_bfs(self, debug=False):
        return_value = [[],""]
        queue = deque()

        queue.append(self.root)
        while len(queue) > 0:
            val = queue.popleft()
            return_value[1] += self.debug_log_helper_root(debug, val.value)
            for child in val.children:
                return_value[0].append(GraphNodeConnection(val, val.children[child],
                    val.value + val.children[child].value))
                queue.append(val.children[child])

        return return_value


    def bfs_traversal_find_custom_queue(self, value_to_find, debug):
        return_value = [False, None, "", 0]
        queue = CustomQueue()

        queue.enqueue(self.root)
        while len(queue) > 0:
            val = queue.dequeue()
            return_value[1] = val
            return_value[3] += val.value

            if val.value == value_to_find:
                return_value[0] = True
                return_value[2] += self.debug_log_helper_child(debug, val.value, "<< Item Found")
                break

            return_value[2] += self.debug_log_helper_root(debug, val.value)
            for child in val.children:
                queue.enqueue(val.children[child])
        
        return return_value


if __name__ == "__main__":
    var = Trie()
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
    print("--DFS traversal--")
    print(var.dfs_traversal_print(6, True))
    print(var.dfs_traversal_print(1, True))
    print(var.dfs_traversal_print(15, True))
    print(var.dfs_traversal_print(7, True))
    print(var.dfs_traversal_print(3, True))
    print("--BFS traversal using built-in Dequeue--")
    print(var.bfs_traversal_print(6, debug=True))
    print(var.bfs_traversal_print(1, debug=True))
    print(var.bfs_traversal_print(15, debug=True))
    print(var.bfs_traversal_print(7, debug=True))
    print(var.bfs_traversal_print(3, debug=True))
    print("--BFS traversal using custom Queue--")
    print(var.bfs_traversal_print(6, use_custom_queue=True, debug=True))
    print(var.bfs_traversal_print(1, use_custom_queue=True, debug=True))
    print(var.bfs_traversal_print(15, use_custom_queue=True, debug=True))
    print(var.bfs_traversal_print(7, use_custom_queue=True, debug=True))
    print(var.bfs_traversal_print(3, use_custom_queue=True, debug=True))
    print("--Full BFS traversal--")
    print(var.bfs_traversal(True))
    print("--Custom BFS traversal--")
    print(var.custom_bfs(True))
    print("--Shortest Path--")
    print(var.shortest_path(7, True))