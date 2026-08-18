import math,random
def generate(data):
 def rv():
  while True:
   v=tuple(random.randint(-8,8) for _ in range(3))
   if any(v): return v
 A,C,F=rv(),rv(),rv(); dot=lambda u,v:sum(x*y for x,y in zip(u,v)); mag=lambda v:math.sqrt(dot(v,v)); p={}
 for name,v in zip("ACF",(A,C,F)):
  for axis,x in zip("xyz",v): p[name.lower()+axis]=x
 data["params"].update(p); data["correct_answers"].update(aconc=dot(A,C)/mag(C),cona=dot(C,A)/mag(A),ionf=F[0]/mag(F),foni=F[0])
