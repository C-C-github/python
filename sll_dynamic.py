class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            print("List is empty now added,first node",newnode.data)
            self.head=newnode
            newnode.next=None
            return 
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
        newnode.next=None
    def traverse(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
        return 
    def inserlast(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next!=None:
                current=current.next    
            current.next=newnode
    def insertbegin(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def countElems(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    def insertAfterAnElem(self,val,target):
        if not self.head:
            print("This is an Empty List")
            return
        newNode = node(val)
        current = self.head
        count=0
        while current:
            if current.data == target:
                newNode.next = current.next
                current.next = newNode
                break
            current = current.next
            count+=1
        if count == self.countElems():
            print("Target is not found")
            return
            
    def InsertBeforeAnElem(self,val,target):
        if not self.head:
            print("This is an Empty List")
            return
        newNode = node(val)
        count = 0
        current = self.head
        while current:
            if current.next.data == target:
                newNode.next = current.next
                current.next = newNode
                break
            current = current.next
            count+=1
        if count == self.countElems():
            print("Target is not Found")
            return
    def deletefirst(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
        
    def deletelast(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            print(f"List is empty element deleted {self.head.data}")
            self.head=None
            return
        # current=self.head
        # while current.next.next:
        #     current=current.next
        # current.next=None
        prev=self.head
        current=self.head.next
        while current.next!=None:
            prev=current
            current=current.next
        prev.next=None
    def search(self,data):
        if self.head is None:
            print("List is empty")
            return None,None
        current=self.head
        index=1
        while current!=None:
            if current.data==data:
                return True,index
            current=current.next
            index+=1
        return False
    def insertbeforenode(self,value,key):
        if self.head is None:
            print("List is empty")
            return
        else:
            newnode=node(value)
            current=self.head
            if current.data==key:
                newnode.next=current
                self.head=newnode
            else:
                current=self.head
                while current.next and current.next.data!=key:
                    current=current.next
                if current.next:
                    newnode.next=current.next
                    current.next=newnode
                else:
                    print("Key not found: ",key)
    
    def insertafternode(self,value,key):
        if self.head is None:
            print("List is empty")
            return
        else:
            newnode=node(value)
            current=self.head
            # while current and current.data!=key:
            #     current=current.next
            # if current:
            #     newnode.next=current.next
            #     current.next=newnode
            while current:
                if current.data==key:
                    newnode.next=current.next
                    current.next=newnode
                    break
                current=current.next
            else:
                print("Key not found: ",key)
    def specificatposition(self,pos,val):
        if not self.head:
            print("List is Empty")
            return
        if pos > self.countElems() or pos<0:
            print("Index Doesnot Exist")
            return
        newNode = node(val)
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return
        position = 1
        current = self.head
        while current.next:
            if position == pos:
                newNode.next = current.next
                current.next = newNode
                break
            position+=1
            current = current.next
        if pos == position:
            current.next = newNode
            return
        else:
            print("Index is not found")
    def delbeforenode(self,val):
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
    def delafternode(self,val):
        if self.head is None:
            print("List is Empty")
        else:
            if self.head.next is None:
                print("List has only one element,not possible")
            else:
                current=self.head
                while current and current.data!=val:
                    current=current.next
                if current and current.next:
                    print(current.next.data,"deleted")
                    current.next=current.next.next
                else:
                    print("value element not found")
    def reverselist(self):
        if self.head is None:
            print("List is empty")
        
        else:
            prev=None
            current=self.head
            while (current is not None):
                next=current.next
                current.next=prev
                prev=current
                current=next  
            self.head=prev 
            
    def display(self):
        if self.head is None:
            print("List is empty from display function")
            return
        print("---------------------------------------------------------")
        current=self.head
        while current:
            print(current.data,end=" ->")
            current=current.next
        print("None")
n=sll()

while True:
    print("1.insert 2.Display 3.insert@begin 4.Insert@last 5.count")
    print("6.addbefore 7.addafter 8.deletefirst 9.deletelast 10.search")
    print("11.specific position(1-n) 12.insert before node 13.insert after node 14.delete before node 15.delete after node")
    print("16.Reverse List 17.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter the data: "))
        n.insert(data)
        print("---------------------------------------------------------")
    elif ch==2:
        n.display()
        print("---------------------------------------------------------")
    elif ch==3:
        data=int(input("Enter the data: "))
        n.insertbegin(data)
        print("---------------------------------------------------------")
    elif ch==4:
        data=int(input("Enter the data: "))
        n.inserlast(data)
        print("---------------------------------------------------------")
    elif ch==5:
        print("Number of elements are: ",n.countElems())
        print("---------------------------------------------------------")
    elif ch==6:
        data=int(input("Enter the data: "))
        target=int(input("Enter the target: "))
        n.InsertBeforeAnElem(data,target)
        print("---------------------------------------------------------")
    elif ch==7:
        data=int(input("Enter the data: "))
        target=int(input("Enter the target: "))
        n.insertAfterAnElem(data,target)
        print("---------------------------------------------------------")
    elif ch==8:
        n.deletefirst()
        print("---------------------------------------------------------")
    elif ch==9:
        n.deletelast()
        print("---------------------------------------------------------")
    elif ch==10:
        data=int(input("Enter the data: "))
        ele,index=n.search(data)
        if ele is True:
            print("Element found: ",index)
        else:
            print("Element not found")
        print("---------------------------------------------------------")
    elif ch==11:
        pos=int(input("Enter the position: "))
        data=int(input("Enter the data: "))
        n.specificatposition(pos,data)
        print("---------------------------------------------------------")
    elif ch==12:
        data=int(input("Enter the data: "))
        key=int(input("Enter the key: "))
        n.insertbeforenode(data,key)
        print("---------------------------------------------------------")
    elif ch==13:
        data=int(input("Enter the data: "))
        key=int(input("Enter the key: "))
        n.insertafternode(data,key)
        print("---------------------------------------------------------")
    elif ch==14:
        data=int(input("Enter the data: "))
        n.delbeforenode(data)
        print("---------------------------------------------------------")
    elif ch==15:
        data=int(input("Enter the data: "))
        n.delafternode(data)
        print("---------------------------------------------------------")
    elif ch==16:
        n.reverselist()
        print("---------------------------------------------------------")
    else:
        break
    
#                       |-------------------------TESTING --------------------------------|
# n.insert(10)
# n.insert(20)
# n.insert(30)
# # n.traverse(40)
# # n.traverse(50)
# # n.traverse(60)
# # n.inserlast(70)
# # n.inserlast(80)
# # n.inserlast(90)
# print(n.addafter(40))
# n.display()