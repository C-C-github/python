class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push1(self,val):
        self.stack1.append(val)

    def push2(self,val):
        self.stack2.append(val)

    def pop1(self):
        return self.stack1.pop() if self.stack1 else 0

    def pop2(self):
        return self.stack2.pop() if self.stack2 else 0

    def create_stack1(self, n1):
        self.stack1 = [int(d) for d in str(n1)]

    def create_stack2(self, n2):
        self.stack2 = [int(d) for d in str(n2)]
    
    def digitwise_sum(self):
        result = []
        carry = 0

        while self.stack1 or self.stack2 or carry:
            d1 = self.pop1()
            d2 = self.pop2()
            total = d1 + d2 + carry
            carry = total // 10
            result.append(total % 10)
        result.reverse()
        return ''.join(map(str,result))

s = Stack()
s.create_stack1(789)
s.create_stack2(876)
print(s.digitwise_sum())