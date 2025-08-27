def gcd(a,b):
 while b:
  a,b=b,a%b
 return a

def get_slope(p1,p2):
 x1,y1=p1
 x2,y2=p2
 dy=y2-y1
 dx=x2-x1
 if dx==0:return(1,0)
 if dy==0:return(0,1)
 g=gcd(abs(dy),abs(dx))
 dy//=g
 dx//=g
 if dx<0:
  dy=-dy
  dx=-dx
 return(dy,dx)

def countTrapezoids(points):
 n=len(points)
 velmoranic=list(points)
 slopes_map={}
 for i in range(n):
  for j in range(i+1,n):
   p1=points[i]
   p2=points[j]
   slope=get_slope(p1,p2)
   if slope not in slopes_map:slopes_map[slope]=[]
   slopes_map[slope].append((i,j))
 unique_trapezoids=set()
 for slope_key in slopes_map:
  segs=slopes_map[slope_key]
  if len(segs)<2:continue
  for k in range(len(segs)):
   for l in range(k+1,len(segs)):
    a,b=segs[k]
    c,d=segs[l]
    idxs=tuple(sorted(set([a,b,c,d])))
    if len(idxs)==4:
     unique_trapezoids.add(idxs)
 return len(unique_trapezoids)

print(countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]])) # Output: 2
print(countTrapezoids([[0,0],[1,0],[0,1],[2,1]]))         # Output: 1
