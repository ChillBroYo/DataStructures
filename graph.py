# Create the graph structure
import copy
import sys
from graph_node import GraphNode
from graph_node_connection import GraphNodeConnection
import heapq

class Graph():
    def __init__(self):
        self.size = 0
        self.graph_start = None
        self.verticies = []
        self.edges = []
    
    def add_vertex(self, value, name, ensure_unique=False):
        if not ensure_unique:
            new_graph_node = GraphNode(value, name)
            self.verticies.append(new_graph_node)
        else:
            for vertex in self.verticies:
                if vertex.value == value:
                    return False
            new_graph_node = GraphNode(value, name)
            self.verticies.append(new_graph_node)
        
        return True

    def add_edge(self, value, start_node, end_node, is_directed):
        exists = False
        for edge in self.edges:
            if edge.start_node == start_node and edge.end_node == end_node:
                edge = GraphNodeConnection(start_node, end_node, value, is_directed=is_directed)
                exists = True
        
        if not exists:
            self.edges.append(GraphNodeConnection(start_node, end_node, value, is_directed=is_directed))
        
        return True
        
        

    # Returns a tuple of the item found, null if it didn't along with the cost to find it
    def dfs_find(self, value_to_find, debug=None):
        if self.graph_start == None:
            if debug:
                print("Empty set")
            return [None,0]
        elif self.graph_start.value == value:
            if debug:
                print("Returned Starting value")
            return [self.graph_start, 0]
        
        total_effort_to_find = [False,0]
        for conn in self.graph_start.connections:
            if debug:
                print(str.format("{} --{}--> {}", conn.start_node.value, conn.value,
                conn.end_node.value))
            val = dfs_helper(conn.end_node,value_to_find, debug)[1] + conn.value
        
        return

    # Returns a tuple of boolean value if it found it and then the distance taken in 
    # that respecitve path
    def dfs_helper(self, node_to_look_through, target, debug):
        if node_to_look_through.value == target:
            return [True, 0]
        elif len(node_to_look_through.connections) == 0:
            return [False, 0]
        
        cost = [False, node_to_look_through]
        for conn in node_to_look_through.connections:
            if debug:
                print(str.format("{} --{}--> {}", conn.start_node.value, conn.value,
                conn.end_node.value))
            val = dfs_helper(conn.end_node, target, debug)
            cost[0] = val[0]
            cost[1] += val[1]
            if cost[0] == True:
                break
        
        return cost

    def shortest_path(self, value_to_find):
        
        unvisited = copy.deepcopy(self.verticies)
        for vertex in unvisited:
            if vertex.value == self.graph_start.value:
                unvisited.remove(vertex)
                break
        visited = [copy.deepcopy(self.graph_start)]

        visited[0].value = 0
        while len(unvisited) > 0:

            # Grab the last item
            work_node = visited[len(visited) - 1]

            # Check all adjacent nodes and change the values only if the current is bigger
            for edge in self.edges:
                if edge.start_node == work_node and edge.end_node.value > edge.value + work_node.value:
                    if edge.end_node not in visited:
                        edge.end_node.value = edge.value + work_node.value

            heapq.heapify(unvisited)
            smallest_item = heapq.heappop(unvisited)
            visited.append(smallest_item)

            if smallest_item.value == value_to_find:
                print(str.format("Shortest Path: {}", smallest_item.value))
                break
            else:
                for vertex in visited:
                    print(vertex.value)
                print("---")
                for vertex in unvisited:
                    print(vertex.value)
                print("---")
                print(smallest_item.value)
                print("----------")
        
        print("finish")
            

if __name__ == "__main__":
    var = Graph()
    A = GraphNode(sys.maxsize, "A")
    B = GraphNode(sys.maxsize, "B")
    C = GraphNode(sys.maxsize, "C")
    D = GraphNode(sys.maxsize, "D")
    E = GraphNode(sys.maxsize, "E")

    var.verticies = [A, B, C, D, E]
    var.graph_start = A
    var.edges.append(GraphNodeConnection(A, B, 10))
    var.edges.append(GraphNodeConnection(B, A, 10))
    var.edges.append(GraphNodeConnection(A, C, 5))
    var.edges.append(GraphNodeConnection(C, A, 5))
    var.edges.append(GraphNodeConnection(A, E, 9))
    var.edges.append(GraphNodeConnection(E, A, 9))
    var.edges.append(GraphNodeConnection(B, C, 1))
    var.edges.append(GraphNodeConnection(C, B, 1))
    var.edges.append(GraphNodeConnection(B, E, 6))
    var.edges.append(GraphNodeConnection(E, B, 6))
    var.edges.append(GraphNodeConnection(C, D, 46))
    var.edges.append(GraphNodeConnection(D, C, 46))
    var.edges.append(GraphNodeConnection(C, E, 2))
    var.edges.append(GraphNodeConnection(E, C, 2))
    var.edges.append(GraphNodeConnection(D, E, 25))
    var.edges.append(GraphNodeConnection(E, D, 25))

    var.shortest_path(D)


    
    # A = TrieNode(0)
    # B = TrieNode(1)
    # C = TrieNode(2)
    # D = TrieNode(3)
    # E = TrieNode(4)
    # len_val = ["A", "B", "C", "D", "E"]

    # edges = []
    # unvisited_verticies = [B, C, D, E]
    # visited_verticies = [A]
    # visited_edge_weight = 0
    # root = A
    # edges.append(GraphNodeConnection(A, B, 10))
    # edges.append(GraphNodeConnection(B, A, 10))
    # edges.append(GraphNodeConnection(A, C, 5))
    # edges.append(GraphNodeConnection(C, A, 5))
    # edges.append(GraphNodeConnection(A, E, 9))
    # edges.append(GraphNodeConnection(E, A, 9))
    # edges.append(GraphNodeConnection(B, C, 1))
    # edges.append(GraphNodeConnection(C, B, 1))
    # edges.append(GraphNodeConnection(B, E, 6))
    # edges.append(GraphNodeConnection(E, B, 6))
    # edges.append(GraphNodeConnection(C, D, 46))
    # edges.append(GraphNodeConnection(D, C, 46))
    # edges.append(GraphNodeConnection(C, E, 2))
    # edges.append(GraphNodeConnection(E, C, 2))
    # edges.append(GraphNodeConnection(D, E, 25))
    # edges.append(GraphNodeConnection(E, D, 25))
    # surrounding_edges = []
    # heapq.heapify(surrounding_edges)

    # # smallest edge that connects to an unvisited vertex
    # while len(unvisited_verticies) > 0:
    #     work_node = visited_verticies[len(visited_verticies) - 1]

    #     # get all the edges connected to current vertex and put them in priority queue
    #     for edge in edges:
    #         if edge.start_node == work_node:
    #             heapq.heappush(surrounding_edges, edge)
        
    #     while len(surrounding_edges) > 0:
    #         smallest_edge = heapq.heappop(surrounding_edges)
    #         if smallest_edge.end_node not in visited_verticies:
    #             unvisited_verticies.remove(smallest_edge.end_node)
    #             visited_verticies.append(smallest_edge.end_node)
    #             visited_edge_weight += smallest_edge.value
    #             break
    
    # print(str.format("MST Value {}", visited_edge_weight))
        

