import random
def generate(data):
 p=random.randrange(10,101)/10; q=random.randrange(5,51)/10; t=random.randrange(5,31)/10; v=(p/3)*t**3-(q/4)*t**4; x=(p/12)*t**4-(q/20)*t**5
 data["params"].update(p=p,q=q,t=t); data["correct_answers"].update(c3=1/3,c4=-1/4,d4=1/12,d5=-1/20,velocity=v,position=x)
