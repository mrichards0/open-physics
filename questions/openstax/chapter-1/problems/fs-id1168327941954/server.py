import math, random
def generate(data):
    degrees=random.choice([1,5,10,15,20,30,45,60,75,90,120,135,150,180,225,270,315])
    data["params"]["degrees"]=degrees; data["correct_answers"]["radians"]=degrees*math.pi/180
