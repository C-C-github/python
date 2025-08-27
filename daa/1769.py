def balls(boxes):
    n=len(boxes)
    ball=[0]*n
    moves=[0]*n
    cnt=0
    for i in range(1,n):
        if boxes[i-1]=='1':
            cnt+=1
        ball[i]=ball[i-1]+cnt
        cnt=0
        for i in range(n-2,-1,-1):
            if boxes[i+1]=='1':
                cnt+=1
            moves[i]=moves[i+1]+cnt
    return [a+b for a ,b in zip(ball,moves)]
    
b="001011"
# i=int(input())
print(balls(b))