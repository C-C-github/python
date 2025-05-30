#aabbbccdeeeea output ###d#a
import re
def consecutive(a):
    return re.sub(r"(.)\1+",lambda match :'#' * len(match.group(1)),a)
a=input()
result=consecutive(a)
result="".join(result)
while '##' in result:
    result=result.replace("##","#")
print(result)