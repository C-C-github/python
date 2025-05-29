class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        self.head2=None
    def insert(self,data):
        newnode=node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
        newnode.prev=current
    def insert_b(self,data):
        newnode=node(data)
        if not self.head2:
            self.head2=newnode
            return
        current=self.head2
        while current.next:
            current=current.next
        current.next=newnode
        newnode.prev=current
    def length(self,head):
        if head is None:
            return 0
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        return count
    def len1(self):
        return self.length(self.head)
    def len2(self):
        return self.length(self.head2)
    def moveforward(self,n):
        current=self.head
        for _ in range(n):
            if not current:
                return None
            current=current.next
        return current
    def moveforward2(self,n):
        current=self.head2
        for _ in range(n):
            if not current:
                return None
            current=current.next
        return current
    
    def find_intersection(self):
        if self.head is None or self.head2 is None:
            print("List is empty")
            return
        l1=self.len1()
        l2=self.len2()
        t1=self.head
        t2=self.head2
        diff=abs(l1-l2)
        if l1>l2:
            t1=self.moveforward(diff)
        elif l2>l1:
            t2=self.moveforward2(diff)
        while t1 and t2:
            if t1.data==t2.data:
                return t1.data
            t1=t1.next
            t2=t2.next
        return None
        
    def intersection(self):
        res=self.find_intersection()
        print("Intersection is:",res if res is not None else "None")
    
    def display(self,head):
        if self.head is None:
            print("List is empty")
            return
        result=[]
        current=head
        while current:
            result.append(str(current.data))
            current=current.next
        print(" -> ".join(result))
        
    def display1(self):
        self.display(self.head)
    def display2(self):
        self.display(self.head2)
dll=dll()
while True:
    ch=int(input("Enter your choice (1: Insert, 2: Display, 3: Intersection, 4: Exit): "))
    if ch==1:
        data1=int(input("Enter the data for list 1: "))
        dll.insert(data1)
        data2=int(input("Enter the data for list 2: "))
        dll.insert_b(data2)
    elif ch==2:
        print("-------------------------RESULT--------------------------")
        dll.display1()
        dll.display2()
        print("---------------------------------------------------------")
    elif ch==3:
        dll.len1()
        dll.len2()
        dll.intersection()
        
    else:
        break