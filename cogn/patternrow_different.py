'''paypalishiring input .
output: pahnaplsiigyir
n=3
p  a  h    n
a p l s i i g
y   i   r
n=5
p     s       
a    s  i 
y   i   r
p  l    i  g
a       n 
'''
def zikzak(row,str):
    if row==1 or row>=len(str):
        print(str)
        return
    l=0
    l=len(str)
    arr=['']*row
    print(arr)
    m=0
    for i in range(l):
        arr[m]+=str[i]
        if m==row-1:
            down=False
        elif m==0:
            down=True
        if down:
            m+=1
        else:
            m-=1
        print(arr)
    print(arr)
    for i in range(row):
        print(arr[i],end="")
        
row=int(input())
str=input()
zikzak(row,str)
