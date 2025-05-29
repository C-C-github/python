class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
        else: 
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=newnode
            newnode.next=self.head
    def display(self):
            if not self.head:
                print("List is Empty")
                return
            if self.head.next == self.head:
                
                print(self.head.data)
                # print('')
                return
            print('')
            cur = self.head
            result = ''
            while True:
                result = result + (str(cur.data))
                if cur.next == self.head:
                    break
                else:
                    result = result + ' -> '
                cur = cur.next
                
            print(result)
s=cll()
s.insert(10)
s.insert(20)
s.insert(30)
s.display()
    