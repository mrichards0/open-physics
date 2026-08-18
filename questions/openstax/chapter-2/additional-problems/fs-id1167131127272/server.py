import math,random
def generate(data):
 x,y,z=[random.randint(10,150) for _ in range(3)]; m=math.sqrt(x*x+y*y+z*z); data["params"].update(x=x,y=y,z=z); data["correct_answers"].update(magnitude=m,angle=math.degrees(math.acos(z/m)))
