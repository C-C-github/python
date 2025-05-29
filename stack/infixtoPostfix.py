class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)
        return
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return ''
    def isEmpty(self):
        return len(self.stack) == 0
    def infixToPostfix(self,exp):
        res = ''
        precedence = {'+':1,'-':1,'*':2,'/':2}
        for i in exp:
            if i.isalnum():
                res+=i
            elif i =='(':
                self.push(i)
            elif i == ')':
                while self.stack[-1]!='(' and not self.isEmpty():
                    res += self.pop()
                self.pop()
            elif i in precedence:
                while not self.isEmpty() and self.stack[-1] != '(' and precedence[i] <= precedence[self.stack[-1]]:
                    res+=self.stack.pop()
                self.push(i)
        while len(self.stack) !=0:
            res+= self.pop()
        return  res

s =Stack()
postexp = s.infixToPostfix('(4+6)*6/(2+1)')
print(postexp)