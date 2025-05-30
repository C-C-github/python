class string_consecutive():
    def consecutive(self,a):
        result=[]
        i=0
        n=len(a)
        while i<n:
            count=1
            while i+1<n and a[i]==a[i+1]:
                count+=1
                i+=1
            if count>1:
                result.append("#")
            else:
                result.append(a[i])
            i+=1
        result="".join(result)
        while '##' in result:
            result=result.replace("##","#")
        return result
    def simple_method (self,a):
        res,i='',0
        while i<len(a):
            j=i
            while j<len(a) and a[i]==a[j]:
                j+=1
            res+='#' if j-i>1 else a[i]
            i=j
        final,i='',0
        while i<len(res):
            final+='#' if res[i]=='#' else res[i]
            if res[i]=='#':
                while i<len(res) and res[i]=='#':
                    i+=1
            else:
                i+=1
        return final
n= input()
s=string_consecutive()
# print(s.consecutive(n)) #using string concepts while loop.
print(s.simple_method(n))
