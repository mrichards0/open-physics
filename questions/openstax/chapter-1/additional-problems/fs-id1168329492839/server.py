import math,random
def generate(data):
    d=random.choice([5.0,6.0,7.0,7.5,8.0,9.0]); dd=random.choice([0.001,0.002,0.005]); length=random.choice([2.5,3.0,3.25,3.5,4.0]); dl=random.choice([0.001,0.002,0.005]); v=math.pi*(d/2)**2*length
    data["params"].update(diameter=d,ddiameter=dd,travel=length,dtravel=dl); data["correct_answers"].update(volume=v,uncertainty=v*(2*dd/d+dl/length))
