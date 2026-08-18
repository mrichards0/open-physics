import math,random
def generate(data):
 while True:
  x,y,z=[random.randint(-5,5) for _ in range(3)]
  if x or y or z: break
 mag=random.randrange(100,1001,50); norm=math.sqrt(x*x+y*y+z*z); ex,ey,ez=[mag*v/norm for v in (x,y,z)]
 data["params"].update(magnitude=mag,x=x,y=y,z=z); data["correct_answers"].update(ex=ex,ey=ey,ez=ez,angle=math.degrees(math.acos(ex/mag)))
