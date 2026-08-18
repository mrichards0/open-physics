import random
def generate(data):
    l=random.choice([3.005,3.505,3.955,4.205,4.505]); w=random.choice([2.505,3.005,3.050,3.505,4.005]); dl=random.choice([0.002,0.005,0.01]); dw=random.choice([0.002,0.005,0.01]); area=l*w
    data["params"].update(length=l,width=w,dlength=dl,dwidth=dw); data["correct_answers"].update(area=area,uncertainty=area*(dl/l+dw/w))
