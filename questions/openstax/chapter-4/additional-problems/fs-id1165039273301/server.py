import random
def generate(data):
 v=random.randrange(300,1001)/10; r=random.randint(80,400); g=random.choice([9.8,9.81]); a=v*v/r
 data["params"].update(speed=v,radius=r,g=g); data["correct_answers"].update(accel=a,multiple=a/g)
