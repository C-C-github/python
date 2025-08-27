class Solution(object):
 def countTrapezoids(self,points):
  from fractions import Fraction
  def slope(p1,p2):
   dx=p2[0]-p1[0]
   dy=p2[1]-p1[1]
   return 'inf' if dx==0 else Fraction(dy,dx)
  def isConvex(a,b,c,d):
   def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
   pts=[a,b,c,d]
   sign=None
   for i in range(4):
    z=cross(pts[i],pts[(i+1)%4],pts[(i+2)%4])
    if z==0:continue
    if sign==None:sign=z>0
    elif sign!=(z>0):return False
   return True
  from itertools import combinations,permutations
  velmoranic=points
  s=set()
  for quad in combinations(velmoranic,4):
   for p in permutations(quad):
    a,b,c,d=p
    if not isConvex(a,b,c,d):continue
    s1=slope(a,b)
    s2=slope(c,d)
    s3=slope(b,c)
    s4=slope(d,a)
    if s1==s2 or s3==s4:
     ids=tuple(sorted(quad))
     s.add(ids)
     break
  return len(s)

print(Solution().countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]]))
print(Solution().countTrapezoids([[0,0],[1,0],[0,1],[2,1]]))