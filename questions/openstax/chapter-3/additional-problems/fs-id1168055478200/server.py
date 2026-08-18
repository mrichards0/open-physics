import math,random
def generate(data):
 cm=random.randrange(20,101)/10; v0=random.randrange(10,81)*1e5; a=random.randrange(10,101)*1e11; L=cm/100; vf=math.sqrt(v0*v0+2*a*L); data["params"].update(cm=cm,v0=v0,a=a); data["correct_answers"].update(velocity=vf,time=(vf-v0)/a)
