import math,random
def generate(data):
 ans={}; p={}
 for n in "gh":
  m=random.randint(3,20); az=random.randrange(0,360,15); el=random.randrange(-60,61,10); ar,er=map(math.radians,(az,el)); p.update({n+"mag":m,n+"az":az,n+"el":el}); ans.update({n+"x":m*math.cos(er)*math.cos(ar),n+"y":m*math.cos(er)*math.sin(ar),n+"z":m*math.sin(er)})
 data["params"].update(p); data["correct_answers"].update(ans)
