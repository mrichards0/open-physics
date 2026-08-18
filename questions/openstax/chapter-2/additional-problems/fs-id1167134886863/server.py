import math,random
def generate(data):
 def rv():
  while True:
   v=tuple(random.randint(-8,8) for _ in range(3))
   if any(v): return v
 g,h=rv(),rv(); c=(g[1]*h[2]-g[2]*h[1],g[2]*h[0]-g[0]*h[2],g[0]*h[1]-g[1]*h[0]); data["params"].update(gx=g[0],gy=g[1],gz=g[2],hx=h[0],hy=h[1],hz=h[2]); data["correct_answers"].update(cx=c[0],cy=c[1],cz=c[2],cmag=math.sqrt(sum(x*x for x in c)),dot=sum(x*y for x,y in zip(g,h)))
