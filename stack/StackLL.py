class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
        self.top = -1
    def push(self,val):
        newNode = Node(val)
        if self.top == -1:
            self.head = newNode
            self.top+=1
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        self.top+=1
    def pop(self):
        if self.top == -1:
            print("Stack is Empty")
            return
        
        
        