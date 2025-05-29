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
    def inorder(self,Node):
        if Node is None:
            return []
        else:
            return Node.inorder(Node.left)+[Node.data]+Node.inorder(Node.right)
    def display(self,level=0,prefix="Root->"):
        #inorder
        print(" "*level+prefix+str(self.data))
        if self.left:
            self.left.display(level+1,"L--")
        if self.right:
            self.right.display(level+1,"R--")
#n=input("Enter the root node: ")
tree=Node(11)
# tree.left=Node(12)
# tree.right=Node(13)
# tree.left.left=Node(14)
# tree.left.right=Node(15)
# tree.right.left=Node(16)
# tree.right.right=Node(17)
# res=tree.inorder(tree)
# print(res)
while True:
    ch=input("Enter the choice: ")
    if ch=="1":
        # n=int(input("Enter the node: "))
        while True:
            print("1.left 2.right 3.left.left 4.left.right 5.right.left 6.right.right 8.exit")
            ch1=input("Enter the choice: ")
            if ch1=="1":
                n=int(input("Enter the node: "))
                tree.left=Node(n)
                break
            elif ch1=="2":
                n=int(input("Enter the node: "))
                tree.right=Node(n)
                break
            elif ch1=="3":
                n=int(input("Enter the node: "))
                tree.left.left=Node(n)
                break
            elif ch1=="4":
                n=int(input("Enter the node: "))
                tree.left.right=Node(n)
                break
            elif ch1=="5":
                n=int(input("Enter the node: "))
                tree.right.left=Node(n)
                break
            elif ch1=="6":
                n=int(input("Enter the node: "))
                tree.right.right=Node(n)
                break
            elif ch1=="8":
                break
        # tree.insert(n)
        
    elif ch=="2":
        tree.display()
    elif ch=="3":
        res=tree.inorder(tree)
        print(res)
    elif ch=="4":
        break
    else:
        break