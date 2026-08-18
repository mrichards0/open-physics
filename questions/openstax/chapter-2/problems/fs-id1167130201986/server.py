import math,random
def generate(data):
 def rv():
  while True:
   v=(random.randint(-8,8),random.randint(-8,8),0)
   if v[0] or v[1]: return v
 A,C,F,B,D=[rv() for _ in range(5)]; cz=lambda u,v:u[0]*v[1]-u[1]*v[0]; p={}
 for name,v in zip("ACFBD",(A,C,F,B,D)):
  for axis,x in zip("xyz",v): p[name.lower()+axis]=x
 data["params"].update(p); data["correct_answers"].update(ac=cz(A,C),af=cz(A,F),dc=cz(D,C),combo=cz(A,(F[0]+2*C[0],F[1]+2*C[1],0)),ib=B[1],jb=-B[0],gb=3*B[1]+B[0],bhatb=0)
