import math,random
def generate(data):
 r=random.randrange(100,2001)/100; data["params"]["r"]=r; data["correct_answers"].update(halfdisp=2*r,halfdist=math.pi*r,fulldisp=0)
