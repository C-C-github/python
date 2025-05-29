class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push1(self, val):
        self.stack1.append(val)

    def push2(self, val):
        self.stack2.append(val)

    def pop1(self):
        return self.stack1.pop() if self.stack1 else 0

    def pop2(self):
        return self.stack2.pop() if self.stack2 else 0

    def create_stack1(self, n1):
        for digit in str(n1):
            self.push1(int(digit))

    def create_stack2(self, n2):
        for digit in str(n2):
            self.push2(int(digit))

    def digitwise_diff(self):
        result = []
        borrow = 0

        while self.stack1 or self.stack2:
            d1 = self.pop1()
            d2 = self.pop2()

            d1 -= borrow
            if d1 < d2:
                d1 += 10
                borrow = 1
            else:
                borrow = 0

            result.append(d1 - d2)
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result.reverse()
        return ''.join(map(str, result))
n1 = 789
n2 = 876

s = Stack()

if n1 >= n2:
    s.create_stack1(n1)
    s.create_stack2(n2)
    print(s.digitwise_diff())
else:
    s.create_stack1(n2)
    s.create_stack2(n1)
    print("-", end="")
    print(s.digitwise_diff())
