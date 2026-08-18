import math,random
def generate(data):
 m=random.randint(3,15); ratio=random.choice([0.5,0.75,1,1.25,1.5,math.sqrt(2),math.sqrt(3)]); r=m*ratio; c=(r*r-2*m*m)/(2*m*m)
 data["params"].update(magnitude=m,resultant=r); data["correct_answers"]["angle"]=math.degrees(math.acos(max(-1,min(1,c))))
