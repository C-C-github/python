#car right and left side of the road as input and output the car direction
def maxdistance(n,a):
    max_distance=0
    current=0
    for i in a:
            current+=i
            max_distance=max(max_distance,abs(current))
    return max_distance

a=list(map(int,input().split()))
n=len(a)
print(maxdistance(n,a))