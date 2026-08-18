import math,random
def generate(data):
 kmh=random.randint(250,700); h=random.randint(300,1500); g=random.choice([9.8,9.81]); t=math.sqrt(2*h/g); data["params"].update(kmh=kmh,h=h,g=g); data["correct_answers"].update(time=t,distance=(kmh/3.6)*t)
