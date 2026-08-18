import math,random
def generate(data):
 h1=random.randrange(50,201)/100; h2=random.randrange(20,151)/100; g=random.choice([9.8,9.81]); t1=2*math.sqrt(2*g*h1)/g; t2=2*math.sqrt(2*g*h2)/g
 data["params"].update(h1=h1,h2=h2,g=g); data["correct_answers"].update(t1=t1,t2=t2,ratio=t1/t2)
