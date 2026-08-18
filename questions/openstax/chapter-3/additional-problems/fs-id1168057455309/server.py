import random
def generate(data):
 a=random.randrange(-30,31)/10
 if a==0:a=1.2
 tk=random.randint(3,7); vk=random.randrange(-100,101)/10; t1=random.randrange(0,tk*10)/10; t2=random.randrange(tk*10+1,(tk+5)*10)/10; data["params"].update(a=a,tk=tk,vk=vk,t1=t1,t2=t2); data["correct_answers"].update(v1=vk+a*(t1-tk),v2=vk+a*(t2-tk))
