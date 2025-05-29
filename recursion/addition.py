def addition(a,b):
    if b==0:
        return a
    else:
        return addition(a+1,b-1)
print(addition(3,4))