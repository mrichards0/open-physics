import random
def generate(data):
 f1x,f1y,f2x,f2y=[random.randint(-20,20) for _ in range(4)]; dx,dy=random.randint(-5,5),random.randint(-5,5)
 if dx==dy==0: dx=2
 data["params"].update(f1x=f1x,f1y=f1y,f2x=f2x,f2y=f2y,dx=dx,dy=dy); data["correct_answers"].update(w1=f1x*dx+f1y*dy,w2=f2x*dx+f2y*dy)
