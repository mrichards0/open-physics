import random
def generate(data):
 while True:
  e1,e2,e3=[random.randrange(50,201)/10 for _ in range(3)]; w1,w2=[random.randrange(50,301)/10 for _ in range(2)]; dx=e1-w1+e2-w2+e3
  if dx<0: break
 avg=random.randint(10,35); data["params"].update(e1=e1,e2=e2,e3=e3,w1=w1,w2=w2,average=avg); data["correct_answers"].update(displacement=dx,time=dx/avg)
