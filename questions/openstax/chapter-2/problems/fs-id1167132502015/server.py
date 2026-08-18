import math,random
def generate(data):
 while True:
  x,y,z=[random.randint(-10,10) for _ in range(3)]
  if x or y or z: break
 mag=math.sqrt(x*x+y*y+z*z); data["params"].update(x=x,y=y,z=z,magnitude=mag,unit=random.choice(["N","m","m/s"])); data["correct_answers"].update(ux=x/mag,uy=y/mag,uz=z/mag)
