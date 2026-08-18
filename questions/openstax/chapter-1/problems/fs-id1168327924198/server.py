import random
def generate(data):
    yards=random.randrange(80,131,5); data["params"]["yards"]=yards; data["correct_answers"]["meters"]=yards*3/3.281
