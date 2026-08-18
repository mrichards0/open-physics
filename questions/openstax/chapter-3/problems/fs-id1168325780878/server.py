import math,random
def generate(data):
 h=random.randint(100,400); sound=random.randint(325,350); reaction=random.randrange(20,61)/100; g=random.choice([9.8,9.81]); fall=math.sqrt(2*h/g); data["params"].update(h=h,sound=sound,reaction=reaction,g=g); data["correct_answers"].update(speed=math.sqrt(2*g*h),available=fall-h/sound-reaction)
