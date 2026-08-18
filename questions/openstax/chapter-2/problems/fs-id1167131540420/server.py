import random
def generate(data):
 def rv():
  while True:
   v=tuple(random.randint(-6,6) for _ in range(3))
   if any(v): return v
 def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
 dot=lambda a,b:sum(x*y for x,y in zip(a,b)); A,F,D,B=[rv() for _ in range(4)]; af=cross(A,F); db=cross(D,B); scale=dot(A,F); p={}
 for name,v in zip("AFDB",(A,F,D,B)):
  for axis,x in zip("xyz",v): p[name.lower()+axis]=x
 data["params"].update(p); data["correct_answers"].update(triple=dot(af,D),crossdot=dot(af,db),cx=scale*db[0],cy=scale*db[1],cz=scale*db[2])
