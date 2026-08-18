import random
def generate(data):
 d=random.randrange(1000,4501,100); t1=random.randrange(30,81)/10; delay=random.randrange(2,int(t1*10)-5)/10; v1=d/t1; v2=d/(t1-delay); data["params"].update(distance=d,t1=t1,delay=delay); data["correct_answers"].update(v1=v1,v2=v2,ratio=v2/v1)
