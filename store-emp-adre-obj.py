class Emp:
    def st_stls(self,name,id):
        self.name=name
        self.id=id
        
    def display(self):
        print("Name: ",self.name)
        print("ID: ",self.id)


e1=Emp()

e1.st_stls("Rohit",420)
# call outside the fn 
# print(e1.name,e1.id) 
e1.display()
e2=Emp()

e2.st_stls("Rahul",202)
e2.display()

# print("Employ sore:",Emp)
# print("Employ 1 address: ",e1)
# print("Employ 2 address: ",e2)