import random
def generate(data):
 w,e=random.randint(2,12),random.randint(1,10); d=e-w; data["params"].update(west=w,east=e); data["correct_answers"].update(displacement=d,distance=w+e,magnitude=abs(d))
