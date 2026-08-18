import random
def generate(data):
 t1=random.randint(2,12); t2=t1+random.randint(5,15); v1=random.randint(2,15); s2=random.randint(2,15); v2=-s2; a=(v2-v1)/(t2-t1); v0=v1-a*t1
 data["params"].update(t1=t1,t2=t2,v1=v1,speed2=s2); data["correct_answers"].update(acceleration=a,initial=v0,zero=-v0/a)
