import math,random
def generate(data):
 def rv():
  while True:
   v=tuple(random.randint(-7,7) for _ in range(3))
   if any(v): return v
 A,C,F,B,D=[rv() for _ in range(5)]; dot=lambda u,v:sum(x*y for x,y in zip(u,v))
 p={};
 for name,v in zip("ACFBD",(A,C,F,B,D)):
  for axis,x in zip("xyz",v): p[name.lower()+axis]=x
 data["params"].update(p); data["correct_answers"].update(ac=dot(A,C),af=dot(A,F),dc=dot(D,C),combo=dot(A,tuple(F[i]+2*C[i] for i in range(3))),ib=B[0],jb=B[1],gb=3*B[0]-B[1],bhatb=math.sqrt(dot(B,B)))
