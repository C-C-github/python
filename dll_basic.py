class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
        return
    def deletestart(self):
        if self.head is None:
            print("List is empty")
        else:
            print(self.head.data,"deleted")
            self.head=self.head.next
            self.head.prev=None
            return
        
    def display(self):
        if self.head is None:
            print("List is empty")
        current=self.head
        while current:
            print(current.data)
            current=current.next
        return
dll=dll()


dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)
dll.insert(50)
dll.display()
dll.deletestart()
dll.display()