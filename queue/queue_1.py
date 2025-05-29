# from queue import Queue
class queue:
    def __init__(self):
        self.queue=[]
    def isempty(self):
        return len(self.queue)==0
    def enqueue(self,ele):
        self.queue.append(ele)
    def dequeue(self):
        if self.isempty()==None:
            print("queue is empty")
            return 
        return self.queue.pop(0)
    def display(self):
        if self.isempty()==None:
            print("queue is empty")
            return
        print(self.queue)
    def getfront(self):
        if self.isempty()==None:
            print("queue is empty")
            return
        return self.queue[0]
    def getrear(self):
        if self.isempty()==None:
            print("queue is empty")
            return
        return self.queue[-1]

q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()
print(q.getfront())
print(q.getrear())
print(q.dequeue())
q.display()
print(q.getfront())
print(q.getrear())