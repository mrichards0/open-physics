import random
def generate(data):
 x,y,z=[random.randint(-12,12) for _ in range(3)]; data["params"].update(x=x,y=y,z=z,unit=random.choice(["m","cm","km"])); data["correct_answers"].update(rx=x,ry=y,rz=z)
