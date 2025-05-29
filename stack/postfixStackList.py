class Stack:
    def __init__(self):
        self.stack = []
    
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
    
    def PostFix(self, expression):
        opers = ['+','-','*','/','%']
        for i in expression:
            if i not in opers:
                self.push(i)
            else:
                b,a = self.pop(),self.pop()
                expr = a+i+b
                self.push(str(eval(expr)))
    
    
s = Stack()
s.PostFix('432*+5-')
s.display()