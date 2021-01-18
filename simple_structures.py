# Array backed queue

class SimpleStringStack:
    arr_back = []

    def GetLength(self):
        return len(self.arr_back)

    def Push(self, item):
        self.arr_back.append(item)

    def Pop(self):
        if self.GetLength() == 0:
            raise Exception("No Items to pop")
        
        item_to_remove = self.arr_back[0]
        self.arr_back = self.arr_back[1:]
        return item_to_remove
    
    def Print(self):
        print(self.arr_back)


class SimpleStringQueue:
    arr_back = []

    def GetLength(self):
        return len(self.arr_back)

    def Enqueue(self, item):
        self.arr_back.append(item)

    def Dequeue(self):
        if len(self.arr_back) == 0:
            raise Exception("No items to dequeue")

        item_to_remove = self.arr_back[len(self.arr_back) - 1]
        self.arr_back = self.arr_back[:len(self.arr_back) - 1]
        return item_to_remove

    def Print(self):
        print(self.arr_back[::-1])

class IntegerBinarySearchTree:
    root = None
    count = 0
    class BinaryNode:
        Left = None
        Right = None
        Parent = None
        Value = None

        def __init__(self, value):
            self.Value = value
        
        # Insert to prevent duplicates with non-unique values, also to maximize unique nodes
        def Insert(self, node_to_add):
            if self.Value == node_to_add.Value:
                pass
            elif self.Value < node_to_add.Value:
                if self.Right != None:
                    self.Right.Insert(node_to_add)
                else:
                    self.Right = node_to_add
                    self.Right.parent = self
            elif self.Value > node_to_add.Value:
                if self.Left != None:
                    self.Left.Insert(node_to_add)
                else:
                    self.Left = node_to_add
                    self.Left.Parent = self
        
        # Cannot remove nodes without a parent, always assumes a parent exists
        def Remove(self):
            if self.Left == None and self.Right == None:
                if self.Parent.Left == self:
                    self.Parent.Left = None
                elif self.Parent.Right == self:
                    self.Parent.Right = None
                self.Parent = None
            elif self.Left == None:
                if self.Parent.Left == self:
                    self.Parent.Left = self.Right
                elif self.Parent.Right == self:
                    self.Parent.Right = self.Right
                self.Parent = None
            elif self.Right == None:
                if self.Parent.Left == self:
                    self.Parent.Left = self.Left
                elif self.Parent.Right == self:
                    self.Parent.Right = self.Left
                self.Parent = None
            else:
                # If a node has 2 children, pick the left one and insert
                if self.Parent.Left == self:
                    self.Parent.Left = self.Left
                elif self.Parent.Right == self:
                    self.Parent.Right = self.Left
                temp_node = self.Left.Right
                self.Left.Right = None
                self.Insert(temp_node)
                self.Left.Parent = self.Parent
                self.Parent = None


    def Insert(self, value):
        if self.root == None:
            self.root = self.BinaryNode(value)
            return
        
        new_node_to_add = self.BinaryNode(value)
        self.root.Insert(new_node_to_add)
    
    def Remove(self, value):
        item, does_exist = self.Find(value)
        if not does_exist:
            raise Exception("Value does not exist")

        if item == self.root:
            copy_root = self.root
            self.root = self.root.Left
            copy_right = self.root.Right
            self.root.Right = copy_root.right
            if copy_right != None:
                self.root.Insert(copy_right)
            return

        item.Remove()

    def Find(self, value):
        if self.root == None:
            return None, False
        
        return self.recursive_find(self.root, value)
    
    def recursive_find(self, iter_node, value):
        if iter_node == None:
            return None, False
        if iter_node.Value == value:
            return iter_node, True
        elif iter_node.Value < value:
            return self.recursive_find(iter_node.Right, value)
        else:
            return self.recursive_find(iter_node.Left, value)
    
    def Print(self):
        if self.root == None:
            raise Exception("No items in tree")

        self.print_helper(self.root)
        
    def print_helper(self, iter_node):
        if iter_node:
            if iter_node.Left:
                self.print_helper(iter_node.Left)
            print(iter_node.Value)
            if iter_node.Right:
                print(iter_node.Right.Value)


class SimpleCharacterTrie:
    root = None
    class TrieNode:
        children = []
        def Insert(self, string_val):
            pass

def test_stack_queue():
    stack = SimpleStringStack()
    queue = SimpleStringQueue()
    stack.Push("1")
    stack.Push("2")
    stack.Push("3")
    stack.Print()
    stack.Pop()
    stack.Print()
    stack.Pop()
    stack.Print()
    stack.Pop()
    stack.Print()
    queue.Enqueue("1")
    queue.Enqueue("2")
    queue.Enqueue("3")
    queue.Print()
    queue.Dequeue()
    queue.Print()
    queue.Dequeue()
    queue.Print()
    queue.Dequeue()
    queue.Print()

if __name__ == "__main__":
    tree = IntegerBinarySearchTree()
    tree.Insert(1)
    tree.Print()
    print("-----")
    tree.Insert(2)
    tree.Print()
    print("-----")
    tree.Insert(0)
    tree.Insert(-2)
    tree.Insert(-1)
    tree.Print()
    print("-----")
    print(tree.Find(-1)[1])
    print(tree.Find(-2)[1])
    print(tree.Find(-3)[1])
    print("-----")
    tree.Remove(0)
    tree.Print()