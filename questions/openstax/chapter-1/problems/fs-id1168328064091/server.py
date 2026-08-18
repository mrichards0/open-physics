import random
def generate(data):
    initial=random.randrange(250,1001); removed=random.randrange(50,initial)
    data["params"].update(initial=initial,removed=removed); data["correct_answers"]["remaining"]=initial-removed
