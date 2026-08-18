import random
def generate(data):
 a=random.randrange(200,901)*1000; t=random.randrange(300,1201)*1e-6; data["params"].update(a=a,t=t); data["correct_answers"]["velocity"]=a*t
