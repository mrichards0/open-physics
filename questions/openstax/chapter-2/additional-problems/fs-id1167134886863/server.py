import math,random
from spiritsfire_physics.vector_diagrams import two_vector_3d_svg

def generate(data):
 def vector():
  magnitude=random.randint(4,20); azimuth=random.randrange(0,360,15); elevation=random.randrange(-60,61,10)
  az,el=map(math.radians,(azimuth,elevation))
  components=(magnitude*math.cos(el)*math.cos(az),magnitude*math.cos(el)*math.sin(az),magnitude*math.sin(el))
  return magnitude,azimuth,elevation,components
 while True:
  gm,gaz,gel,g=vector(); hm,haz,hel,h=vector()
  c=(g[1]*h[2]-g[2]*h[1],g[2]*h[0]-g[0]*h[2],g[0]*h[1]-g[1]*h[0])
  if math.sqrt(sum(value*value for value in c))>1: break
 data["params"].update(gmag=gm,gaz=gaz,gel=gel,hmag=hm,haz=haz,hel=hel)
 data["correct_answers"].update(cx=c[0],cy=c[1],cz=c[2],cmag=math.sqrt(sum(x*x for x in c)),dot=sum(x*y for x,y in zip(g,h)))

def file(data):
 if data["filename"] != "vectors.svg": raise FileNotFoundError(data["filename"])
 p=data["params"]
 return two_vector_3d_svg((("G",p["gmag"],p["gaz"],p["gel"]),("H",p["hmag"],p["haz"],p["hel"])))
