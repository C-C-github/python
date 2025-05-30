#string ABC120PME0000LZ3MB1Y3C45 ouput: APLMYC103134.
# def solution(n):
#     new=[]
#     alpha=[]
#     num=[]
#     for i in n:
#         if i.isalpha():
#             alpha.append(i)
#         else:
#             num.append(i)
#     new=alpha+num
#     return ("".join(new))
def logic(s):
    ns=[s[0]]
    for i in range(1,len(s)):
        if (s[i-1].isdigit() and s[i].isalpha()) or (s[i-1].isalpha() and s[i].isdigit()):
            ns.append(s[i])
            
    print("actual string",ns)
    # print("sorted string",solution(ns))
    alphabets = [ch for ch in ns if ch.isalpha()]
    digits = [dig for dig in ns if dig.isdigit()]
    
    return "".join(alphabets) + "".join(digits)
n=input()
print(logic(n))