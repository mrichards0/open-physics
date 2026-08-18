import random
def generate(data):
 v=random.randrange(30,101)/100; d1=random.randrange(100,401)/100; d2=random.randrange(int(d1*100)+50,int(d1*100)+501)/100; g=random.choice([9.8,9.81]); x1=d1/1000; x2=d2/1000; a1=-v*v/(2*x1); a2=-v*v/(2*x2)
 data["params"].update(v=v,d1=d1,d2=d2,g=g); data["correct_answers"].update(a1=a1,g1=a1/g,time=2*x1/v,g2=a2/g)
