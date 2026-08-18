import math,random
def generate(data):
 v0=random.randint(12,25); g=random.choice([9.8,9.81]); maxh=v0*v0/(2*g); h=random.randrange(10,int(maxh*100)-10)/100; data["params"].update(v0=v0,h=h,g=g); data["correct_answers"]["interval"]=2*math.sqrt(v0*v0-2*g*h)/g
