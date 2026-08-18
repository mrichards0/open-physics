import random
def generate(data):
 vx=random.randrange(50,201)/10; vy=random.randrange(10,101)/10; g=random.choice([9.8,9.81]); data["params"].update(vx=vx,vy=vy,g=g); data["correct_answers"].update(c1=vy/vx,c2=-g/(2*vx*vx),height=vy*vy/(2*g),xapex=vx*vy/g)
