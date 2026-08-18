import random
def generate(data):
    feet=random.choice([0.5,1,2,3,5,10,12]); data["params"]["feet"]=feet; data["correct_answers"]["light_ns"]=feet*0.3048/2.998e8*1e9
