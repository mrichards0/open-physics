import random
def generate(data):
 w,e=random.randint(1,10),random.randint(1,15); t=random.randint(2,15); data["params"].update(west=w,east=e,time=t); data["correct_answers"].update(x0=-w,xf=e,displacement=e+w)
