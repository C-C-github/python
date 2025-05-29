#Binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def display(self,level=0,prefix="Root->"):
        #inorder
        print(" "*level+prefix+str(self.data))
        if self.left:
            self.left.display(level+1,"L--")
        if self.right:
            self.right.display(level+1,"R--")
                         
tree=Node(10)
tree.insert(15)
tree.insert(20)
tree.insert(25)
tree.display()