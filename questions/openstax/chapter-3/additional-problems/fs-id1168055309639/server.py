import math,random
def generate(data):
 h=random.randint(30,180); g=random.choice([9.8,9.81]); T=math.sqrt(2*h/g); data["params"].update(h=h,g=g); data["correct_answers"].update(first=0.5*g,velocity=-g*T,last=h-0.5*g*(T-1)**2)
