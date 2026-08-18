import random
def generate(data):
 a,b=random.randint(1,8),random.randint(1,15); data["params"].update(a=a,b=b); data["correct_answers"]["minimum"]=b
