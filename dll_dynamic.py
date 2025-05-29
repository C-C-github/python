import statistics
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
    def deletestart(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            print(self.head.data,"First deleted")
            self.head=None
        else:
            print(self.head.data,"deleted")
            self.head=self.head.next
            self.head.prev=None
            return
    def deletelast(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            print(self.head.data,"deleted,list is now empty")
            self.head=None
        else:
            prev=self.head
            current=prev.next
            while current.next:
                prev=current
                current=current.next
            print(current.data,": Deleted")
            prev.next=None
            
            del current
    def displayforward(self):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        result=''
        while current:
            result=result+(str(current.data))
            result=result+' ->'
            # print(current.data)
            current=current.next
        result=result[:-2]
        print(result)
    def displaybackward(self):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        while current.next:
            current=current.next
        while current:
            print(current.data,end=" ")
            current=current.prev
        print()
    
    def insertbegin(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insertlast(self,data):
        if self.head is None:
            print("List is empty")
            self.head=node(data)
            return
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
            newnode.prev=current
            
    def insertafternode(self,value,key):
        if self.head is None:
            print("List is empty")
            return
        else:
            newnode=node(value)
            current=self.head
            while current and current.data!=key:
                current=current.next
            if current:
                newnode.next=current.next
                current.next=newnode
                newnode.prev=current
            else:
                print("Key not found: ",key)
    def sort_all(self):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        while current:
            next=current.next
            while next:
                if current.data>next.data:
                    current.data,next.data=next.data,current.data
                next=next.next
            current=current.next
        return
    
    def cal_median(self):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        l=[]
        while current:
            l.append(current.data)
            current=current.next
        print(l)
        return statistics.median(l)
    def insert_medianposition(self,data):
        if self.head is None:
            print("List is empty")
            self.head=node(data)
        else:
            newnode=node(data)
            current=self.head
            median=self.cal_median()
            while current and current.data<median:
                current=current.next
            if current:
                newnode.next=current
                newnode.prev=current.prev
                current.prev.next=newnode
                current.prev=newnode
            else:
                print("Key not found: ",key)   
    def deletebegin(self,val):
        if self.head is None:
            print("List is Empty")
        else:
            if self.head.next is None:
                print("List has only one element,not possible")
            elif self.head.next.data==val:
                self.head=self.head.next
            else:
                prev=self.head
                current=prev.next
                while current.next and current.next.data!=val:
                    prev=current
                    current=current.next
                if current.next:
                    print(current.data,"deleted")
                    prev.next=current.next
                else:
                    print("value element not found")
    def deleteend(self,val):
        if self.head is None:
            print("List is Empty")
        else:
            if self.head.next is None:
                print("List has only one element,not possible")
            else:
                current=self.head
                while current.next and current.next.data!=val:
                    current=current.next
                if current.next:
                    print(current.next.data,"deleted")
                    current.next=current.next.next
                else:
                    print("value element not found")
    def count(self):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count
    def insertpos(self,data):
        # insert n-2 insert each elemnat element postion
        if self.head is None:
            print("List is empty")
            self.head=node(data)
        else:
            newnode=node(data)
            current=self.head
            for i in range(self.count()-2):
                current=current.next
            newnode.next=current.next
            current.next=newnode
            newnode.prev=current
            return
    def odd_even(self):
        if self.head is None and self.head.next is None:
            print("List is empty")
            return
        odd=self.head
        even=self.head.next
        even_head=even
        while even!=None and even.next!=None:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return
    def prime(self,n):
        if n<2:
            return False
        for i in range(2,n//2):
            if n%i==0:
                return False
        return True
    def noprime(self):
        if self.head is None and self.head.next is None:
            print("List is empty")
            return
        temp=self.head
        pos=1
        while temp!=None:
            if not self.prime(pos):
                print("not prime",temp.data,"at index",pos,end=' ->')
            # if dll.prime(temp.data):
                # print(f"{temp.data} ,is prime at position {pos}")
            # else:               
                # print(f"{temp.data} ,is not prime at position {pos}")  
                print("")  
            temp=temp.next
            pos+=1   
        del temp
        return
    def primeall(self):
        if self.head is None and self.head.next is None:
            print("List is empty")
            return
        temp=self.head
        pos=1
        while temp!=None:
            if self.prime(pos):
                print("prime",temp.data,"at index",pos,end='->')  
                print("")
            temp=temp.next
            pos+=1
        del temp  
        return
    def reverse(self,head=None,head2=None):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        prev=None
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
        if self.head2 is None:
            print("List is empty")
        else:
            current=self.head2
            prev=None
            while current:
                next=current.next
                current.next=prev
                prev=current
                current=next
            self.head2=prev
        if head:
            return self.head
        if head2:
            return self.head2
    def inserthead2(self,data):
        newnode=node(data)
        if not self.head2:
            self.head2=newnode
            return
        current=self.head2
        while current.next:
            current=current.next
        current.next=newnode
        newnode.prev=current
    def sumtwolist(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.reverse(self.head)
        self.head2=self.reverse(self.head2)
        carry=0
        temp1=self.head
        temp2=self.head2
        result=[]
        while temp1 or temp2 or carry:
            tot=carry
            if temp1:
                tot+=temp1.data
                temp1=temp1.next
            if temp2:
                tot+=temp2.data
                temp2=temp2.next
            carry=tot//10
            result.append(tot%10)
        
        self.head=self.reverse(self.head)
        self.head2=self.reverse(self.head2)
        print(result[::-1])
        
        
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        result=''
        current=self.head
        while current:
            result=result+(str(current.data))
            result=result+' ->'
            # print(current.data)
            current=current.next
        result=result[:-2]
        print(result)
    def displayhead2(self):
        if self.head2 is None:
            print("List is empty")
            return
        result=''
        current=self.head2
        while current:
            result=result+(str(current.data))
            result=result+' ->'
            current=current.next
        result=result[:-2]
        print(result)
        
dll=dll()
while True:
    print("1.Insert 2.Display 3.Delete 4.delete last 5.insert forward")
    print("6.insert backward 7.insert begin 8.insert last 9.insert after node 10.median insert")
    print("11.sort all 12.before delete begin 13.delete that element 14.n-1 pos(bugs) 15.count ")
    print("16.odd even 17.noprime/prime ")
    print("18.insert head2 19.sum of two numders(bug) 20.reverse 21.display head2  25.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter the data: "))
        dll.insert(data)
    elif ch==2:
        print("-------------------------RESULT--------------------------")
        dll.display()
        print("---------------------------------------------------------")
    elif ch==3:
        dll.deletestart()
    elif ch==4:
        dll.deletelast()
    elif ch==5:
        print("----------------------Foward display----------------------")
        dll.displayforward()
    elif ch==6:
        print("----------------------Backward display--------------------")
        dll.displaybackward()
    elif ch==7:
        data=int(input("Enter the data: "))
        dll.insertbegin(data)
    elif ch==8:
        data=int(input("Enter the data: "))
        dll.insertlast(data)
    elif ch==9:
        data=int(input("Enter the data: "))
        key=int(input("Enter the key: "))
        dll.insertafternode(data,key)
    elif ch==10:
        data=int(input("Enter the data: "))
        dll.insert_medianposition(data)
    elif ch==11:
        dll.sort_all()
    elif ch==12:
        data=int(input("Enter the data: "))
        dll.deletebegin(data)
    elif ch==13:
        data=int(input("Enter the data: "))
        dll.deleteend(data)
    elif ch==14:
        data=int(input("Enter the data: "))
        dll.insertpos(data)
    elif ch==15:
        print("Number of elements are: ",dll.count())
    elif ch==16:
        dll.odd_even()
    elif ch==17:
        # dll.display()
        print('------------------Non prime numbers---------------------')
        dll.noprime()
        print('\n------------------Prime numbers-------------------------')
        dll.primeall()
        print('--------------------------------------------------------')
    elif ch==18:
        head2=int(input("Enter the data: "))
        dll.inserthead2(head2)
        # dll.displayhead2()
    elif ch==19:
        dll.sumtwolist()
    elif ch==20:
        dll.reverse()
    elif ch==21:
        dll.displayhead2()
    elif ch==25:
        break
    else:
        print("Invalid choice 404 error")
        break