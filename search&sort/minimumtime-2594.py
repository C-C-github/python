'''You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.'''
from math import sqrt
def repaire(ranks,cars):
    l,r=1,max(ranks)*cars*cars
    def canrepaire(time):
        tot=0
        for i in ranks:
            tot+=int(sqrt(time//i))
        return tot>=cars
    while l<=r:
        mid=(l+r)//2
        if canrepaire(mid):
            r=mid-1
        else:
            l=mid+1
    return l

rank=list(map(int,input().split()))    
car=int(input())
print(repaire(rank,car))