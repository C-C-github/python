def genrate_binary_num(n):
    queue=[]
    queue.append("1")
    for i in range(n):
        x=queue.pop(0)
        print(i+1,'-',x)
        queue.append(x+"0")
        queue.append(x+"1")
    return queue

n=int(input())
print(genrate_binary_num(n))