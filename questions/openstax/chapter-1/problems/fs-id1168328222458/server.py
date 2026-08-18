import random
def generate(data):
    feet=random.choice([4,5,6,7]); inches=random.randint(0,11); total=12*feet+inches
    data["params"].update(feet=feet,inches=inches,total_inches=total); data["correct_answers"]["meters"]=total*0.0254
