# Create the graph structure
from graph_node import GraphNode

class Graph():
    def __init__(self):
        self.size = 0
        self.graph_start = None
    
    def add_vertex(self, value, node_to_connect_to):
        pass

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
