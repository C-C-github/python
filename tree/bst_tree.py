
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def isbst(self,left=float('-inf'),right=float('inf')):
        if self is None:
            return True
        if not (left< self.data <right):
            return False
        return (self.left.isbst(left, self.data) if self.left else True) and \
               (self.right.isbst(self.data, right) if self.right else True)
s=Node(10)
#-----------true case----------------------
s.left=Node(5)
s.right=Node(15)
s.left.left=Node(2)
s.left.right=Node(7)
#-----------false case----------------------
# s.left=Node(5)
# s.right=Node(8)
# s.left.left=Node(2)
# s.left.right=Node(7)
print(s.isbst())