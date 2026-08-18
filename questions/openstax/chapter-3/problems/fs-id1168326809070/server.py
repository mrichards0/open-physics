import random
def generate(data):
 c=random.randint(5,30); k=random.randint(1,6); t1=random.randint(1,5); t2=t1+random.randint(1,5); pos=lambda t:c*t-k*t*t; v1=c-2*k*t1; v2=c-2*k*t2
 data["params"].update(c=c,k=k,t1=t1,t2=t2); data["correct_answers"].update(v1=v1,v2=v2,s1=abs(v1),s2=abs(v2),average=(pos(t2)-pos(t1))/(t2-t1))
