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
        for edge in traversal_order_edges:
            print (edge.value)
        print ("---")
        paths = {}
        heapq.heapify(traversal_order_edges)
        in_order_edges = []
        length = copy.copy(len(traversal_order_edges))
        for x in range(length):
            val = heapq.heappop(traversal_order_edges)
            in_order_edges.append(val)
            print(val.value)


        string_val = ""
        return_value = [False, [], string_val, -1]

        while(len(in_order_edges) > 0):
            # Extract newest item
            val = in_order_edges.pop(0)
            string_val += self.debug_log_helper_child(debug, val.start_node.value, str.format("{}{}",
                        val.end_node.value, "\n"))
            string_val += "yyyyyyyy"
            # If this is the first node, (starting point) push an empty array, that the node has
            # now been visited and 0 distance (since we havent moved yet) 
            # Also load first edge, with all following values being:
            # [0] = Array of nodes traversed to get to this node
            # [1] = Has this node been visited before (multiple paths check)
            # [2] = Total path value 
            if paths == {}:
                paths[val.start_node] = [[], True, 0]
                paths[val.end_node] = [[val.value], False, val.value]
            elif paths.get(val.start_node) != None and paths.get(val.end_node) == None:
                # Ensure to deepcopy and not pass by reference
                paths[val.end_node] = copy.deepcopy(paths[val.start_node])
                paths[val.end_node][0].append(val.value)
                paths[val.end_node][1] = False
                paths[val.end_node][2] += val.value

                # If the node has been visited before mark it
                if paths[val.start_node][1] == True:
                    paths[val.end_node][1] = False
                else:
                    paths[val.start_node][1] = True
            
            #for path in paths:
                #if len(paths[path][0]) > 0:
                    #if paths[path][0][0].start_node == self.root and paths[path][0][0].end_node.value == value_to_find:

                if val.end_node.value == value_to_find:
                    for x in paths:
                        string_val += self.debug_log_helper_child(debug, x, str.format("{}{}",
                            paths[x], "\n"))
                    string_val += "xxxxxx"

                # [0] Boolean is it found, [1] In order array of nodes traversed through, [2] string node path,
                # [3] distance (vertex to vertex addition)s
                    return_value = [True, paths[val.end_node][0], string_val, paths[val.end_node][2]]

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
    var = Trie()
    # val = TrieNode(1)
    # val.add_child(2)
    # val.add_child(3)
    # val.children[2].add_child(25)
    # val.children[2].add_child(5)
    # val.children[3].add_child(6)
    # val.children[3].add_child(7)
    # val.children[2].children[25].add_child(9)
    # val.children[3].children[6].add_child(9)
    # val.add_child(10)
    val = TrieNode(1)
    val.add_child(2)
    val.add_child(3)
    val.children[2].add_child(7)
    val.children[3].add_child(4)
    val.children[3].add_child(6)
    val.children[2].children[7].add_child(6)
    var.root = val
    # print("--DFS traversal--")
    # print(var.dfs_traversal_print(6, True))
    # print(var.dfs_traversal_print(1, True))
    # print(var.dfs_traversal_print(15, True))
    # print(var.dfs_traversal_print(7, True))
    # print(var.dfs_traversal_print(3, True))
    # print("--BFS traversal using built-in Dequeue--")
    # print(var.bfs_traversal_print(6, debug=True))
    # print(var.bfs_traversal_print(1, debug=True))
    # print(var.bfs_traversal_print(15, debug=True))
    # print(var.bfs_traversal_print(7, debug=True))
    # print(var.bfs_traversal_print(3, debug=True))
    # print("--BFS traversal using custom Queue--")
    # print(var.bfs_traversal_print(6, use_custom_queue=True, debug=True))
    # print(var.bfs_traversal_print(1, use_custom_queue=True, debug=True))
    # print(var.bfs_traversal_print(15, use_custom_queue=True, debug=True))
    # print(var.bfs_traversal_print(7, use_custom_queue=True, debug=True))
    # print(var.bfs_traversal_print(3, use_custom_queue=True, debug=True))
    # print("--Full BFS traversal--")
    #print(var.bfs_traversal(True))
    # print("--Custom BFS traversal--")
    # print(var.custom_bfs(True))
    # print("--Shortest Path--")
    s_val = var.shortest_path(6, True)
    if s_val['found'] == True:
        print("String value-------------------")
        print(s_val['string_path'])
        print("Shortest path----------------")
        print(s_val['shortest_path'])
        print("Shortest path value---------------")
        print(s_val['shortest_path_value'])
    else:
        print("Soemthings wrong")
    # nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    # distances = {
    #     'B': {'A': 5, 'D': 1, 'G': 2},
    #     'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    #     'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    #     'G': {'B': 2, 'D': 1, 'C': 2},
    #     'C': {'G': 2, 'E': 1, 'F': 16},
    #     'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    #     'F': {'A': 5, 'E': 2, 'C': 16}}

    # unvisited = {node: None for node in nodes} #using None as +inf
    # visited = {}
    # current = 'B'
    # currentDistance = 0
    # unvisited[current] = currentDistance

    # while True:
    #     for neighbour, distance in distances[current].items():
    #         if neighbour not in unvisited: continue
    #         newDistance = currentDistance + distance
    #         if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
    #             unvisited[neighbour] = newDistance
    #     visited[current] = currentDistance
    #     del unvisited[current]
    #     if not unvisited: break
    #     candidates = [node for node in unvisited.items() if node[1]]
    #     current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    # print(visited)