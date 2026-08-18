import random
def generate(data):
 a=random.randrange(100,501)*100; ms=random.randrange(50,301)/100; t=ms*1e-3; data["params"].update(a=a,ms=ms); data["correct_answers"]["speed"]=a*t
