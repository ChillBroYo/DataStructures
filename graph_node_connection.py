# Create connection class

class GraphNodeConnection():
    def __init__(self, start_node, end_node, value, is_directed=False):
        self.is_directed = is_directed
        self.start_node = start_node
        self.end_node = end_node
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value