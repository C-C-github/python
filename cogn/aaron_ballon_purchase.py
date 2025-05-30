#n1 4 n2 8 arr1 4 6 27 arr2 5 3 1 6 he can get purchase any 2 packet in buget x ouput 10
class aaron:
    def __init__(self,n1,budget,purchase1,purchase2):
        self.n1=n1
        self.budget=budget
        self.purchase1=purchase1
        self.purchase2=purchase2
        self.total=0
    def calculate_2packet(self):
        for i in range(self.n1):
            for j in range(i+1,self.n1):
                tt=self.purchase2[i]+self.purchase2[j]
                ttlbs=self.purchase1[i]+self.purchase1[j] 
                # print(f'purchase 1[i]: {self.purchase1[i]}, purchase 1[j]: {self.purchase1[j]}, ttlbs: {ttlbs}')
                # print(f'purchase 2[i]: {self.purchase2[i]}, purchase 2[j]: {self.purchase2[j]}, tt: {tt}')
                # print(f'tt:{tt},ttlbs:{ttlbs},total:{self.total}')
                if tt<=self.budget:
                    self.total=max(self.total,ttlbs)
                    
    def display(self):
        print(self.total)
n1=int(input())
budget=int(input())
purchase1=list(map(int,input().split()))
purchase2=list(map(int,input().split()))
obj=aaron(n1,budget,purchase1,purchase2)
obj.calculate_2packet()
obj.display()