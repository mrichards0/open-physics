import random
def generate(data):
 d1,d2,d3=[random.randrange(20,161)/10 for _ in range(3)]; t1,t2,t3=[random.randrange(5,46) for _ in range(3)]; dx=d1-d2+d3; total=t1+t2+t3
 data["params"].update(d1=d1,d2=d2,d3=d3,t1=t1,t2=t2,t3=t3); data["correct_answers"].update(displacement=dx,velocity=dx/(total/60))
