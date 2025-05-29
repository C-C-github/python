class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        node=Node(data)
        if self.rear is None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp=self.front
            self.front=self.front.next
            return temp
    def display(self):
        temp=self.front
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print()

d=queue()
d.enqueue(1)
d.enqueue(2)
d.enqueue(3)
d.enqueue(4)
d.enqueue(5)
d.display()
d.dequeue()
d.display()
d.dequeue()
d.display()