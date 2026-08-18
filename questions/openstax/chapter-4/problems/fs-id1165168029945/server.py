import math,random
def generate(data):
 h=random.randrange(50,401)/10; r=random.randrange(500,4001)/10; g=random.randrange(20,101)/10; H=h*1000; R=r*1000; t=math.sqrt(2*H/g); data["params"].update(h=h,r=r,g=g); data["correct_answers"].update(speed=R/t,time=t,vy=-g*t)
