import math,random
def generate(data):
 def rv(n):
  while True:
   v=tuple(random.randint(-7,7) for _ in range(n))
   if any(v): return v
 def angle(a,b):
  c=sum(x*y for x,y in zip(a,b))/math.sqrt(sum(x*x for x in a)*sum(y*y for y in b)); return math.degrees(math.acos(max(-1,min(1,c))))
 D,A,U,B=rv(2),rv(2),rv(3),rv(3); p={}
 for name,v in zip(("d","a","u","b"),(D,A,U,B)):
  for axis,x in zip("xyz",v): p[name+axis]=x
 data["params"].update(p); data["correct_answers"].update(angle2=angle(D,A),angle3=angle(U,B))
