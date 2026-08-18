import random
def generate(data):
 a1=random.randrange(3,21)/100; t1=random.randrange(10,41)/10; t2=random.randrange(20,81)/10; t3=random.randrange(10,51)/10; s1,s2,s3=[60*x for x in (t1,t2,t3)]; vp=a1*s1
 data["params"].update(a1=a1,t1=t1,t2=t2,t3=t3); data["correct_answers"].update(a3=-vp/s3,distance=0.5*vp*s1+vp*s2+0.5*vp*s3)
