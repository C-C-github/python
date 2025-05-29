class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def insert(self,root,key):
        if not root:
            return AVLNode(key)
        elif key<root.key:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance=self.getBalance(root)
        if balance>1 and key<root.left.key:
            return self.rightRotate(root)
        if balance<-1 and key>root.right.key:
            return self.leftRotate(root)
        if balance>1 and key>root.left.key:
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance<-1 and key<root.right.key:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        return root 
    def leftRotate(self,y):
        x=y.right
        T2=x.left
        x.left=y
        y.right=T2
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        x.height=1+max(self.getHeight(x.left),self.getHeight(x.right))
        return x
    def rightRotate(self,x):
        y=x.left
        T2=y.right
        y.right=x
        x.left=T2
        x.height=1+max(self.getHeight(x.left),self.getHeight(x.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)
tree=AVLTree()
root=None
root=tree.insert(root,10)
root=tree.insert(root,20)
root=tree.insert(root,30)
root=tree.insert(root,40)
root=tree.insert(root,50)
root=tree.insert(root,25)
print(root.key)