# create Trie data structure
# STD Library workaround for same name values
import heapq
from custom_queue import CustomQueue
from trie_node import TrieNode
from collections import deque
from graph_node_connection import GraphNodeConnection # TODO: Remove from this as incorrect scope
import copy

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
        if return_val[0] == True:
            var = []
            # for x in return_val[1]:
            #     var.append(x.value)
            return {
                    "found" : True,
                    "shortest_path_value" : return_val[3],
                    "shortest_path" : return_val[1],
                    "string_path" : return_val[2]
            }
        else:
            return {"found" : False}
        
    # will Only work with connections (not in correct scope) TODO: Move to graph
    def shortest_path_bfs(self, value_to_find, debug):
        # Load all edges into array, create paths dictionary and minheap array
        traversal_order_edges = self.custom_bfs()[0]
        paths = {}

        heapq.heapify(traversal_order_edges)
        in_order_edges = []
        processed_edges = []
        length = copy.copy(len(traversal_order_edges))
        for x in range(length):
            val = heapq.heappop(traversal_order_edges)
            in_order_edges.append(val)
        
        for edge in in_order_edges:
            processed_edges.append(in_order_edges.pop())
            for processed in processed_edges:
                val = None
                if processed.start_node == edge.start_node and processed.end_node == edge.end_node:
                    print("pass")
                    pass
                elif processed.start_node != edge.start_node and processed.end_node == edge.end_node:
                    print(str.format("not start {}--{}-->{}", processed.start_node.value, edge.start_node.value, processed.value + edge.value))
                    val = GraphNodeConnection(processed.start_node, edge.start_node, processed.value + edge.value)
                elif processed.start_node == edge.start_node and processed.end_node != edge.end_node:
                    print(str.format("not end {}--{}-->{}", processed.end_node.value, edge.end_node.value, processed.value + edge.value))
                    val = GraphNodeConnection(processed.end_node, edge.end_node, processed.value + edge.value)

                if val and val.start_node == self.root and val.end_node.value == value_to_find:
                    return [str.format("{} --> {}", val.start_node, val.end_node), val.value]
                elif val:
                    processed_edges.append(val)
                    processed_edges.append(GraphNodeConnection(val.end_node, val.start_node, val.value))


        return ["", None]

        
        


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
        queue = []

        heapq.heappush(queue, self.root)
        while len(queue) > 0:
            val = heapq.heappop(queue)
            return_value[1] += self.debug_log_helper_root(debug, val.value)
            for child in val.children:
                # HACK TO CHECK IF SHORTEST PATH WORKS
                if val.value == 3 and val.children[child].value == 6:
                    return_value[0].append(GraphNodeConnection(val, val.children[child],
                        26))
                elif val.value == 1 and val.children[child].value == 2:
                    return_value[0].append(GraphNodeConnection(val, val.children[child],
                        9))
                elif val.value == 2 and val.children[child].value == 7:
                    return_value[0].append(GraphNodeConnection(val, val.children[child],
                        3))
                else:
                    return_value[0].append(GraphNodeConnection(val, val.children[child],
                        val.value + val.children[child].value))
                        
                heapq.heappush(queue, val.children[child])

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
    import sys
    var = Trie()
    A = TrieNode(sys.maxsize)
    B = TrieNode(sys.maxsize)
    C = TrieNode(sys.maxsize)
    D = TrieNode(sys.maxsize)
    E = TrieNode(sys.maxsize)
    len_val = ["A", "B", "C", "D", "E"]

    edges = []
    verticies = [A, B, C, D, E]
    root = A
    target = D
    edges.append(GraphNodeConnection(A, B, 10))
    edges.append(GraphNodeConnection(B, A, 10))
    edges.append(GraphNodeConnection(A, C, 5))
    edges.append(GraphNodeConnection(C, A, 5))
    edges.append(GraphNodeConnection(A, E, 9))
    edges.append(GraphNodeConnection(E, A, 9))
    edges.append(GraphNodeConnection(B, C, 1))
    edges.append(GraphNodeConnection(C, B, 1))
    edges.append(GraphNodeConnection(B, E, 6))
    edges.append(GraphNodeConnection(E, B, 6))
    edges.append(GraphNodeConnection(C, D, 46))
    edges.append(GraphNodeConnection(D, C, 46))
    edges.append(GraphNodeConnection(C, E, 2))
    edges.append(GraphNodeConnection(E, C, 2))
    edges.append(GraphNodeConnection(D, E, 25))
    edges.append(GraphNodeConnection(E, D, 25))

    unvisited = [B, C, D, E]
    visited = [A]

    visited[0].value = 0
    while len(unvisited) > 0:

        # Grab the last item
        work_node = visited[len(visited) - 1]

        # Check all adjacent nodes and change the values only if the current is bigger
        for edge in edges:
            if edge.start_node == work_node and edge.end_node.value > edge.value + work_node.value:
                if edge.end_node not in visited:
                    edge.end_node.value = edge.value + work_node.value

        heapq.heapify(unvisited)
        smallest_item = heapq.heappop(unvisited)
        visited.append(smallest_item)

        if smallest_item == target:
            print(str.format("Shortest Path: {}", smallest_item.value))
            break
    
    A = TrieNode(0)
    B = TrieNode(1)
    C = TrieNode(2)
    D = TrieNode(3)
    E = TrieNode(4)
    len_val = ["A", "B", "C", "D", "E"]

    edges = []
    unvisited_verticies = [B, C, D, E]
    visited_verticies = [A]
    visited_edge_weight = 0
    root = A
    edges.append(GraphNodeConnection(A, B, 10))
    edges.append(GraphNodeConnection(B, A, 10))
    edges.append(GraphNodeConnection(A, C, 5))
    edges.append(GraphNodeConnection(C, A, 5))
    edges.append(GraphNodeConnection(A, E, 9))
    edges.append(GraphNodeConnection(E, A, 9))
    edges.append(GraphNodeConnection(B, C, 1))
    edges.append(GraphNodeConnection(C, B, 1))
    edges.append(GraphNodeConnection(B, E, 6))
    edges.append(GraphNodeConnection(E, B, 6))
    edges.append(GraphNodeConnection(C, D, 46))
    edges.append(GraphNodeConnection(D, C, 46))
    edges.append(GraphNodeConnection(C, E, 2))
    edges.append(GraphNodeConnection(E, C, 2))
    edges.append(GraphNodeConnection(D, E, 25))
    edges.append(GraphNodeConnection(E, D, 25))
    surrounding_edges = []
    heapq.heapify(surrounding_edges)

    # smallest edge that connects to an unvisited vertex
    while len(unvisited_verticies) > 0:
        work_node = visited_verticies[len(visited_verticies) - 1]

        # get all the edges connected to current vertex and put them in priority queue
        for edge in edges:
            if edge.start_node == work_node:
                heapq.heappush(surrounding_edges, edge)
        
        while len(surrounding_edges) > 0:
            smallest_edge = heapq.heappop(surrounding_edges)
            if smallest_edge.end_node not in visited_verticies:
                unvisited_verticies.remove(smallest_edge.end_node)
                visited_verticies.append(smallest_edge.end_node)
                visited_edge_weight += smallest_edge.value
                break
    
    print(str.format("MST Value {}", visited_edge_weight))
        



 #   print(str.format("Smallest edge = {} --{}--> {}", len_val[smallest_edge.start_node.value], smallest_edge.value, len_val[smallest_edge.end_node.value]))
#    print(str.format("MST Value {} number of edges {}", val, len(visited_edges)))