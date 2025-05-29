class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class solution:
    def issymmetric(self,root):
        def ismirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val==t2.val 
                    and ismirror(t1.left,t2.right) 
                    and ismirror(t1.right,t2.left))
        return ismirror(root,root)
tree=Node(1)
# ----------------------false case-----------------------
# tree.left=Node(1,Node(2))
# tree.right=Node(1,Node(2))
# tree.left.left=Node(1,Node(0))
# tree.left.right=Node(1,Node(3))
# tree.right.left=Node(1,Node(0))
# tree.right.right=Node(1,Node(3))
tree.left = Node(2)
tree.right = Node(2)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.left = Node(4)
tree.right.right = Node(3)

print(solution().issymmetric(tree))