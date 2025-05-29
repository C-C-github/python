class sll:
    def __init__(self,data):
        self.data=data
        self.next=None
    def logic(self):
        pass
    def display(self):
        print(self.data)
        
# id(a) number of the object address in memory | hash(a) hexai data adress
n1=sll(105)
n2=sll(106)
n3=sll(107)
n1.next=n2
n2.next=n3
# n3.next=None
# print(n1.data)
# print(n1.next.data)
# print(n1.next.next.data)
# print(n1.next.next.next)
current=n1
while current:
    print(current.data,end=" ->")
    current=current.next
print("None")