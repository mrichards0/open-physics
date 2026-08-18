import math,random
def generate(data):
 f=random.randint(2,7); g=random.choice([9.8,9.81]); T=f+math.sqrt(f*f-f); data["params"].update(f=f,g=g); data["correct_answers"].update(time=T,height=0.5*g*T*T)
