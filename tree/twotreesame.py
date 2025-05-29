class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def bothtrees(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.data==root2.data and self.bothtrees(root1.left,root2.left) and self.bothtrees(root1.right,root2.right))

    def display(self,level=0,prefix="Root->"):
        #inorder
        print(" "*level+prefix+str(self.data))
        if self.left:
            self.left.display(level+1,"L--")
        if self.right:
            self.right.display(level+1,"R--")
            
t1=node(0)
t2=node(0)
# r1=[1,2,3,4]
# r2=[1,2,3,4]
# for i in r1:
#     t1.insert(i)
# for i in r2:
#     t2.insert(i)
    
    
# t1.display()
# t2.display()
# print(t1.bothtrees(t1,t2))

while True:
    print("1.Enter Tree 1 2.Enter Tree 2 3.t1 display 4.t2 display 5.both trees 8.exit")
    ch=input("Enter the choice: ")
    if ch=="1":
        print("Enter Tree 1")
        # n=int(input("Enter the node: "))
        while True:
            print("1.left 2.right 3.left.left 4.left.right 5.right.left 6.right.right 8.exit")
            ch1=input("Enter the choice: ")
            if ch1=="1":
                n=int(input("Enter the node: "))
                t1.left=node(n)
                break
            elif ch1=="2":
                n=int(input("Enter the node: "))
                t1.right=node(n)
                break
            elif ch1=="3":
                n=int(input("Enter the node: "))
                t1.left.left=node(n)
                break
            elif ch1=="4":
                n=int(input("Enter the node: "))
                t1.left.right=node(n)
                break
            elif ch1=="5":
                n=int(input("Enter the node: "))
                t1.right.left=node(n)
                break
            elif ch1=="6":
                n=int(input("Enter the node: "))
                t1.right.right=node(n)
                break
            elif ch1=="8":
                break
            else:
                print("Invalid choice")
                break
    elif ch=="2":
        print("Enter Tree 2")
        # n=int(input("Enter the node: "))
        while True:
            print("1.left 2.right 3.left.left 4.left.right 5.right.left 6.right.right 8.exit")
            ch1=input("Enter the choice: ")
            if ch1=="1":
                n=int(input("Enter the node: "))
                t2.left=node(n)
                break
            elif ch1=="2":
                n=int(input("Enter the node: "))
                t2.right=node(n)
                break
            elif ch1=="3":
                n=int(input("Enter the node: "))
                t2.left.left=node(n)
                break
            elif ch1=="4":
                n=int(input("Enter the node: "))
                t2.left.right=node(n)
                break
            elif ch1=="5":
                n=int(input("Enter the node: "))
                t2.right.left=node(n)
                break
            elif ch1=="6":
                n=int(input("Enter the node: "))
                t2.right.right=node(n)
                break
            elif ch1=="8":
                break
            else:
                print("Invalid choice")
                break
    elif ch=="3":
        t1.display()
    elif ch=="4":
        t2.display()
    elif ch=="5":
        print(t1.bothtrees(t1,t2))
    else:
        break