
def merge(p1,p2):
    res=[]
    i,j=0,0
    # res=p1+p2
    # for i in range(len(res)):
    #     for j in range(i+1,len(res)):
    #         if res[i]>res[j]:
    #             res[i],res[j]=res[j],res[i]
    while i<len(p1) and j<len(p2):
        if p1[i]<p2[j]:
            res.append(p1[i])
            i+=1
        else:
            res.append(p2[j])
            j+=1
    while i<len(p1):
        res.append(p1[i])
        i+=1
    while j<len(p2):
        res.append(p2[j])
        j+=1
    return res
p1=[1,3,5,6,2]
p2=[2,5,6,9,10]
print(merge(p1,p2))