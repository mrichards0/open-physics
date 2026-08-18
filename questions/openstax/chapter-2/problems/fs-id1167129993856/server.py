import math,random
def generate(data):
 while True:
  x,y,z=[random.randint(-9,9) for _ in range(3)]
  if x or y or z: break
 m=math.sqrt(x*x+y*y+z*z); data["params"].update(x=x,y=y,z=z); data["correct_answers"].update(ax=math.degrees(math.acos(x/m)),ay=math.degrees(math.acos(y/m)),az=math.degrees(math.acos(z/m)))
