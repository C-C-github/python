# 5 3 2 8,5 3 2=10 that means output count =3.
   
def calculate(a,hours,l):
    a.sort() # 2 3 5 8
    count=0
    max_c=0
    for i in a:
        # print(f'max_c={max_c}, i={i}')
        max_c+=i   #0+2=2 | 2+3=5 | 5+5=10 | 10+8=18
        
        if max_c<=hours:  
            count+=1
        else:
            break
    return count
    
kailasharr=list(map(int,input().split()))
hours=int(input())
size=int(input())
print(calculate(kailasharr,hours,size))