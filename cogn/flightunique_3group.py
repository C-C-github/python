#input 12 as ABCZABCADDAC and ouput 3 because, abc,zab,cad,dac--- take only unique as output abc,zab,cad
def unique_number(n,flight_ticket):
    # t=[]
    # for i in range(0,n,3):
    #     temp=''.join(set(flight_ticket[i:i+3]))
    #     t.append(temp)
    # u=set(t)
    # t=list(u)
    # t.sort()    
    # return len(t)
    uc=set()
    for i in range(0,n,3):
        code=''.join(sorted(flight_ticket[i:i+3]))
        uc.add(code)
    return len(uc)

n=int(input())
flight_ticket=input()
print(unique_number(n,flight_ticket))