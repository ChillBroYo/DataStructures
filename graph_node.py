# Graph Node Structure
from graph_node_connection import GraphNodeConnection

class GraphNode:
    def __init__(self, value, name):
        self.connections = []
        self.value = value
        self.name = name

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def add_connection(self, node_to_connect_to, value_of_connection, end_node_name, new_node=False, directed=False):
        if new_node == True:
            node_to_connect_to = GraphNode(node_to_connect_to, end_node_name)

        exists = False
        for conn in self.connections:
            if conn.end_node.value == node_to_connect_to.value:
                exists = True
        
        if exists == False and directed == False:
            #print("falsefalse")
            self.connections.append(GraphNodeConnection(self, node_to_connect_to, value_of_connection))
            node_to_connect_to.connections.append(GraphNodeConnection(node_to_connect_to, self, value_of_connection))
        elif exists == False and directed == True:
            #print("falsetrue")
            self.connections.append(GraphNodeConnection(self, node_to_connect_to, value_of_connection, is_directed=True))
        elif exists == True and directed == False:
            #print("truefalse")
            exists = False
            for conn in node_to_connect_to.connections:
                if conn.end_node == self:
                    exists = True
                
            if not exists:
                node_to_connect_to.connections.append(GraphNodeConnection(node_to_connect_to, self, value_of_connection))
        

            
    def remove_connection(self, value, remove_all=False):
        for x in range(len(self.connections)):
            if self.connections[x].end_node.value == value:
                del self.connections[x]
                if remove_all == True:
                    return True
        
        return True

    def print_connections(self, return_string_val=False):
        return_string = ""
        for conn in self.connections:
            if conn.is_directed == True:
                return_string += str.format("{}  --{}--> {}", conn.start_node.value, conn.value, conn.end_node.value)
            else:
                return_string += str.format("{} <--{}--> {}", conn.start_node.value, conn.value, conn.end_node.value)
            
            return_string += "\n"
        
        if return_string_val == True:
            return return_string
        print (return_string)


if __name__ == "__main__":
    var = GraphNode(1, "A")
    var.add_connection(2,5,"B", new_node=True)
    var.add_connection(3,6, "C", new_node=True)
    var.add_connection(4,6, "D", new_node=True, directed=True)
    var.add_connection(5,6, "E", new_node=True, directed=True)
    val = GraphNode(10, "F")
    var.add_connection(val, 7, "G")
    var.print_connections()