import random
def generate(data):
 f=random.randrange(10,201,5); data["params"]["f"]=f; data["correct_answers"].update(maximum=4*f,minimum=0)
