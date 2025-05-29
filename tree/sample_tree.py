class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    
    def display(self):
        print(self.data)
tree=Node(12)
tree.display()