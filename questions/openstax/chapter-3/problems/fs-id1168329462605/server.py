import random
def generate(data):
 v=random.randrange(100,501)/10; d=random.randrange(50,401)/100; data["params"].update(vcms=v,dcm=d); data["correct_answers"]["time"]=2*d/v
