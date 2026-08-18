import random
def generate(data):
 v=random.randint(30,100); d=random.randrange(10,101)/100; a=v*v/(2*d); data["params"].update(v=v,d=d); data["correct_answers"].update(acceleration=a,time=v/a)
