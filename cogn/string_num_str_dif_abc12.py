#input: 9k1xv2s3 output kxs .v should not print.
s=input()
ns=[s[0]]
print("printing the digit after alpha v should not print beacuse of 2 next s")
for i in range(1,len(s)):
    if s[i-1].isdigit() and s[i].isalpha():
        print(s[i],end="")

print("\n")

for i in range(1,len(s)):
    if s[i-1].isdigit() and s[i].isalpha() or s[i-1].isalpha() and s[i].isdigit():
        ns.append(s[i])
        
    l=[i for i in ns if i.isalpha()] 
    d=[i for i in ns if i.isdigit()] 
print("letters: ",l)
print("digits: ",d)
print("total list: ",l,d)
print("These the Final string: ","".join(l)+"".join(d))