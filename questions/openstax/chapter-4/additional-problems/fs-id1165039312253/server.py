import math,random
def generate(data):
 x=random.randint(15,80); drop=random.randrange(5,101)/100; g=random.choice([9.8,9.81]); t=math.sqrt(2*drop/g); data["params"].update(distance=x,drop_cm=drop*100,g=g); data["correct_answers"].update(time=t,speed=x/t)
