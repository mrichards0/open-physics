import random
def generate(data):
    ounces=random.choice([6,8,10,12,16,20,24,32]); data["params"]["fl_oz"]=ounces; data["correct_answers"]["m3"]=ounces*30e-6
