import math,random
def generate(data):
 dx=random.choice([i for i in range(-8,9) if i]); dy=random.choice([i for i in range(-8,9) if i]); mag=math.hypot(dx,dy); k=random.randint(2,6)
 data["params"].update(dx=dx,dy=dy,dmag=mag,multiple=k); data["correct_answers"].update(rx=-dx,ry=-k*mag-dy)
