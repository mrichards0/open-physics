import math,random
def generate(data):
 h=random.randint(60,180); g=random.choice([9.8,9.81]); total=math.sqrt(2*h/g); delay=random.randrange(5,int((total-0.5)*10))/10; data["params"].update(h=h,g=g,delay=delay); data["correct_answers"].update(height=h-0.5*g*delay*delay,remaining=total-delay)
