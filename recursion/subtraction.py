def subtraction(A,B):
    if B==0:
        return A
    return subtraction(A-1,B-1) 

print(subtraction(5,3))