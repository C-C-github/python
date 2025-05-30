# n= 4,input 2 : 1 2 3 4 ,input 3 : 10 output : (9,8,7,6)
product_n=int(input())
weight=list(map(int,input().split()))
max_threshold=int(input())
class busyfactory:
    def __init__(self,product_n,weight,max_threshold):
        self.product_n=product_n
        self.weight=weight
        self.max_threshold=max_threshold
        self.impactsum=0
    def calculate(self):
        # tot=sum(self.weight)
        # for i in self.weight:
        #     if tot-i<=self.max_threshold:
        #         self.impactsum.append(tot-i)
        #     else:
        #         self.impactsum.append(self.max_threshold)
        tot=sum(self.weight)
        rslt=[]
        for i in self.weight:
            impct=tot-i
            rslt.append(min(impct,self.max_threshold))
        self.impactsum=rslt
        return self.impactsum
    def display(self):
        print(self.impactsum)
obj=busyfactory(product_n,weight,max_threshold)
print(obj.calculate())