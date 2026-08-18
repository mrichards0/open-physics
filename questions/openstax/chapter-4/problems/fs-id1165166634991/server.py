import random
def generate(data):
 e=random.randrange(30,121)/10; f=random.randint(2,8); data["params"].update(earth=e,factor=f); data["correct_answers"]["range"]=e*f
