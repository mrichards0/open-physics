import random
def generate(data):
 p={}; ans={}
 for i in range(1,5):
  while True:
   a=tuple(random.randint(-7,7) for _ in range(3)); c=tuple(random.randint(-7,7) for _ in range(3))
   if any(a) and any(c): break
  v=(a[1]*c[2]-a[2]*c[1],a[2]*c[0]-a[0]*c[2],a[0]*c[1]-a[1]*c[0])
  for axis,x,y,z in zip("xyz",a,c,v): p[f"a{i}{axis}"]=x; p[f"c{i}{axis}"]=y; ans[f"p{i}{axis}"]=z
 data["params"].update(p); data["correct_answers"].update(ans)
