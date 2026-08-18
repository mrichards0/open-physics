import random
def generate(data):
    length=random.randrange(90,121,5); width=random.randrange(55,91,5)
    data["params"].update(length_m=length,width_m=width); data["correct_answers"]["area_ft2"]=length*width*3.281**2
