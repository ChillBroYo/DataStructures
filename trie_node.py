# Trie Node: implemented to be as versitile as possible, with unique children

class TrieNode:
    def __init__(self,value=None,parent=None):
        self.children = {}
        self.parent = parent
        self.value = value
        self.times_added = 0

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
            
    def recursion_helper(self, value, pass_value=None, pass_node=None):
        if self.value == value:
            return True
        else:
            for node in pass_node.children:
                return self.recursion_helper(value, None, node)
        
        return False


    def add_child(self, value):
        if self.children.get(value) == None:
            self.children[value] = TrieNode(value, self)
        else:
            self.children[value].times_added += 1

    def remove_child(self, value, remove_sub_children=False):
        if self.children.get(value) == None:
            return False
        else:
            return self.remove(value)

            
    def remove(self, remove_sub_children=False):
        # Full family with keeping children
        if self.parent and len(self.children) > 0 and remove_sub_children == False:
            temp_val = self.children
            parent = self.parent
            del self.parent.children[self.value]
            parent.children.update(temp_val)
        # Full family with children removal
        elif self.parent and len(self.children) > 0 and remove_sub_children == True:
            del self.parent.children[self.value]
        # Parent with no children (removing sub children is irrelevant here)
        elif self.parent and len(self.children) == 0:
            del self.parent.children[self.value]
        # Removing root that has children with no children removal
        elif self.parent and len(self.children) > 0 and remove_sub_children == False:
            new_root = TrieNode(self.children[0].value)
            del self.children[0]
            new_root.children = self.children
            self.children = None
            del self
        # Only case left should be remove all
        else:
            del self
        
        return True
