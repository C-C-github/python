class constructor():
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print("Name: ",self.name)
        print("ID: ",self.id)
cu=constructor("Rohit",420)
cu.display()

# _init_ is directly called when the object is created or class is initialized. It is called a constructor.
# if we dont create a method of _init_ then also it is initialized as _init_(self) without any parameters. 
# This is called as DEFAULT CONSTRUCTOR.
# We dont need to call it, it automaticaly called when class is initialized or object is created.
# the method is useful to intialize the variable of the clas object