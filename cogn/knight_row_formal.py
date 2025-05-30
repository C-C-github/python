#strong number left is strictly greater ,the no stronger to their right.  input n=5 4 3 5 2 1 output 2
def strong_number(n,knight):
    spl=0
    for i in range(n):
        left_c=0
        right_c=0
        for j in range(0,i):
            if knight[i]<knight[j]:
                left_c+=1
        for k in range(i+1,n):
            if knight[i]<knight[k]:
                right_c+=1
        if left_c>right_c:
            spl+=1
    return spl

n=int(input())
knight=list(map(int,input().split()))
print(strong_number(n,knight))