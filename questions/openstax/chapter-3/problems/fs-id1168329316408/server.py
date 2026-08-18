import math,random
def generate(data):
 v=random.randint(100,170); t=random.randrange(30,61)/10; avg_distance=0.5*v*t; d=random.randrange(int(avg_distance)+30,int(avg_distance)+250); a=v/t
 data["params"].update(v=v,t=t,d=d); data["correct_answers"].update(acceleration=a,predicted=math.sqrt(2*a*d))
