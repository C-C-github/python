class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        if self.IsEmpty():
            return 'Stack Is Empty'
        return self.stack.pop()
    
    def IsEmpty(self):
        return len(self.stack) == 0

    def balanceSymbols(self,exp):
        self.stack = []
        for i in exp:
            if i =='(':
                self.push(i)
            elif i == ')':
                if self.IsEmpty():
                    return False
                else:
                    self.pop()
        if self.IsEmpty():
            return True
        else:
            return False
    
    
s = Stack()
ans = s.balanceSymbols('(2+3*(4-2)')
print(ans)
ans2 = s.balanceSymbols('(4+1)')
print(ans2)