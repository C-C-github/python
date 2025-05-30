''' s= ab ,t = acb output: true, s=" ",t=" " output: false
        car     cxr        true
        all      all       false
        abc      abcd      true
'''
def replace(s,t):
    if s==t or abs(len(s)-len(t))>1:
        return False
    else:
        i=0
        while i < min(len(s),len(t)) and s[i]==t[i]:
            i+=1
        return s[i:] == t[i+1:] or s[i+1:] == t[i:] or s[i+1:] == t[i+1:]
    # if len(s)<len(t):
    #     c=len(s1-ss)
    # else:
    #     c=len(ss-s1)
    # if c==1:
    #     return False
    # return True
s=input()
t=input()
print(replace(s,t))