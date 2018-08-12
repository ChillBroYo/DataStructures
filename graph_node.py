# Graph Node Structure

class GraphNode:
    def __init__(self, value):
        self.connections = {}
        self.value = value

    def add_connection(self, value, new_node=False):
        if new_node == True:
            value = GraphNode(value)
        
        for conn in self.connections:
            if self.connections[conn].end.value == value.value:
                for connection in self.connections[conn].end.connections:
                    pass
