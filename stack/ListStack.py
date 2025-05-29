class Stack:
    def __init__(self):
        self. stack = []
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        if self.IsEmpty():
            return 'Stack Is Empty'
        return self.stack.pop()

    def peek(self):
        if self.IsEmpty():
            return 'Stack Is Empty'
        return self.stack[-1]

    def display(self):
        print(self.stack)
    
    def IsEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
s = Stack()
s.push(10)
s.push(15)
s.push(20)
s.push(25)
s.pop()
print('Top ELement : ',s.peek())
print('Size : ', s.size())
print('IsEmpty : ',s.IsEmpty())

s.display()