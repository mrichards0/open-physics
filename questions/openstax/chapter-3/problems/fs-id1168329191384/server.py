import random
def generate(data):
 v1,v2,v3=[random.randint(-7,7) for _ in range(3)]; d1,d2,d3=[random.randint(2,7) for _ in range(3)]; x0=random.randint(-15,15); dx1,dx2,dx3=v1*d1,v2*d2,v3*d3
 data["params"].update(v1=v1,v2=v2,v3=v3,dt1=d1,dt2=d2,dt3=d3,x0=x0); data["correct_answers"].update(dx1=dx1,dx2=dx2,dx3=dx3,xf=x0+dx1+dx2+dx3)
