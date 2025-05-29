class indexqueue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
        self.front=-1
        self.rear=-1
    def is_empty(self):
        return self.front==-1
    def is_full(self):
        return self.rear==self.maxsize-1
    def enqueue(self,item):
        if self.is_full():
            print("queue is empty")
            return
        if self.is_empty():
            self.front=0
        self.rear+=1
        self.queue[self.rear]=item
        
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        item=self.queue[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front+=1
        return item
    def getfront(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.queue[self.front]
    def getrear(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.queue[self.rear]
    def display(self):
        if self.is_empty():
            print("queue is empty")
            return
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=" ")
d=indexqueue(5)
d.enqueue(1)
d.enqueue(2)
d.enqueue(3)
d.enqueue(4)
d.enqueue(5)
d.display()
print()
print("Dequeued:", d.dequeue())
d.display()
print()
print("Front:", d.getfront())
print("Rear:", d.getrear())