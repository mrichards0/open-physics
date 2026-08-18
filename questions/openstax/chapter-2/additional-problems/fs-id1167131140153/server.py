import random
def generate(data):
 while True:
  a,b,c=[tuple(random.randint(-6,6) for _ in range(3)) for _ in range(3)]; bc=(b[1]*c[2]-b[2]*c[1],b[2]*c[0]-b[0]*c[2],b[0]*c[1]-b[1]*c[0]); triple=sum(x*y for x,y in zip(a,bc))
  if triple: break
 p={}
 for n,v in zip("abc",(a,b,c)):
  for axis,x in zip("xyz",v): p[n+axis]=x
 data["params"].update(p); data["correct_answers"]["volume"]=abs(triple)
