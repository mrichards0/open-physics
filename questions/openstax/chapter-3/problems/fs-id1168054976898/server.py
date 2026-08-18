import math,random
def generate(data):
 A=random.randrange(10,51)/10; B=random.randrange(5,51)/20; t1=random.randrange(15,41)/10; t2=random.randrange(int(t1*10)+5,81)/10; data["params"].update(A=A,B=B,t1=t1,t2=t2); data["correct_answers"].update(a1=-B/t1**2,x1=A*(t1-1)+B*math.log(t1),a2=-B/t2**2,x2=A*(t2-1)+B*math.log(t2))
