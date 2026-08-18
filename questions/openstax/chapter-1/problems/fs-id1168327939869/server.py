import random
def generate(data):
    feet=random.randrange(10000,30001,250); data["params"]["feet"]=feet; data["correct_answers"]["kilometers"]=feet/3.281/1000
