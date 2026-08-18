import math,random
def generate(data):
 def rv():
  while True:
   v=tuple(random.randint(-10,10) for _ in range(3))
   if any(v): return v
 g,h=rv(),rv(); data["params"].update(gx=g[0],gy=g[1],gz=g[2],hx=h[0],hy=h[1],hz=h[2]); data["correct_answers"]["component"]=sum(x*y for x,y in zip(g,h))/math.sqrt(sum(x*x for x in h))
