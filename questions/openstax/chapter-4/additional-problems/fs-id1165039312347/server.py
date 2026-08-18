import math,random
def generate(data):
 best=random.randrange(40,121)/10; angle=random.choice(list(range(15,41))+list(range(50,76))); r=best*math.sin(math.radians(2*angle)); data["params"].update(best=best,angle=angle); data["correct_answers"].update(range=r,loss=best-r)
