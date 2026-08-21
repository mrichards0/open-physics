import math,random
from spiritsfire_physics.vector_diagrams import two_vector_3d_svg
def generate(data):
 ans={}; p={}
 for n in "gh":
  m=random.randint(3,20); az=random.randrange(0,360,15); el=random.randrange(-60,61,10); ar,er=map(math.radians,(az,el)); p.update({n+"mag":m,n+"az":az,n+"el":el}); ans.update({n+"x":m*math.cos(er)*math.cos(ar),n+"y":m*math.cos(er)*math.sin(ar),n+"z":m*math.sin(er)})
 data["params"].update(p); data["correct_answers"].update(ans)

def file(data):
 if data["filename"] != "vectors.svg": raise FileNotFoundError(data["filename"])
 p=data["params"]
 return two_vector_3d_svg((("G",p["gmag"],p["gaz"],p["gel"]),("H",p["hmag"],p["haz"],p["hel"])))
