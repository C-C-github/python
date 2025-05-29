class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def insertlast(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
        else: 
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=newnode
            newnode.next=self.head
    def insertbegin(self,data):
        newnode=node(data)
        if not self.head:
            self.head=newnode
            newnode.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            newnode.next=self.head
            current.next=newnode
        #     newnode.next=self.head
        #     temp=self.head
        #     while temp.next!=self.head:
        #         temp=temp.next
        #     temp.next=newnode
            self.head=newnode
    def deletebegin(self):
        if self.head is None:
            print("list is empty")
        elif self.head.next==self.head:
            print(self.head.data,"deleted,list is now empty")
            self.head=None
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            temp=self.head
            self.head=self.head.next
            current.next=self.head
            print(temp.data,": Deleted")
            del temp
    def countElems(self):
        if not self.head:
            return 0
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
            if current==self.head:
                break
        return count
    def deletelast(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next==self.head:
            print(self.head.data,"deleted,list is now empty")
            self.head=None
        else:
            prev=None
            current=self.head
            while current.next!=self.head:
                prev=current
                current=current.next
            prev.next=self.head
            print(current.data,": Deleted")
            del current
    def display(self):
            if not self.head:
                print("List is Empty")
                return
            if self.head.next == self.head:
                
                print(self.head.data)
                # print('')
                return
            print('')
            cur = self.head
            result = ''
            while True:
                result = result + (str(cur.data))
                if cur.next == self.head:
                    break
                else:
                    result = result + ' -> '
                cur = cur.next
                
            print(result)
      
s=cll()
while True:
    print("1.insertlast 2.display 3.insertbegin 4.delete begin 5.delete last")
    print("6.count ")
    ch=int(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter the data: "))
        s.insertlast(data)
        print("---------------------------------------------------------")
    elif ch==2:
        print("-------------------------RESULT--------------------------")
        s.display()
        print("---------------------------------------------------------\n")
    elif ch==3:
        data=int(input("Enter the data: "))
        s.insertbegin(data)
        print("---------------------------------------------------------")
    elif ch==4:
        s.deletebegin()
    elif ch==5:
        s.deletelast()
    elif ch==6:
        print("Number of elements are: ",s.countElems())
        print("---------------------------------------------------------")
    # elif ch==6:
    #     data=int(input("Enter the data: "))
    #     target=int(input("Enter the target: "))
    #     s.InsertBeforeAnElem(data,target)
    #     print("---------------------------------------------------------")
    # elif ch==7:
    #     data=int(input("Enter the data: "))
    #     target=int(input("Enter the target: "))
    #     s.insertAfterAnElem(data,target)
    #     print("---------------------------------------------------------")
    # elif ch==8:
    #     s.deletefirst()
    #     print("---------------------------------------------------------")
    # elif ch==9:
    #     s.deletelast()
    #     print("---------------------------------------------------------")
    # elif ch==10:
    #     data=int(input("Enter the data: "))
    #     ele,index=s.search(data)
    #     if ele is True:
    #         print("Element found: ",index)
    #     else:
    #         print("Element not found")
    #     print("---------------------------------------------------------")
    # elif ch==11:
    #     pos=int(input("Enter the position: "))
    #     data=int(input("Enter the data: "))
    #     s.specificatposition(pos,data)
    #     print("---------------------------------------------------------")
    # elif ch==12:
    #     data=int(input("Enter the data: "))
    #     key=int(input("Enter the key: "))
    #     s.insertbeforenode(data,key)
    #     print("---------------------------------------------------------")
    # elif ch==13:
    #     data=int(input("Enter the data: "))
    #     key=int(input("Enter the key: "))
    #     s.insertafternode(data,key)
    #     print("---------------------------------------------------------")
    # elif ch==14:
    #     data=int(input("Enter the data: "))
    #     s.delbeforenode(data)
    #     print("---------------------------------------------------------")
    # elif ch==15:
    #     data=int(input("Enter the data: "))
    #     s.delafternode(data)
    #     print("---------------------------------------------------------")
    # elif ch==16:
    #     s.reverselist()
    #     print("---------------------------------------------------------")
    else:
        break
        
# 
# s.insert(10)
# s.insert(20)
# s.insert(30)
# s.display()
    