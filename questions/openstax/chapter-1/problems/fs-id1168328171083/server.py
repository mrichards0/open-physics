import random
def generate(data):
    rate=random.choice([1.5,2,2.5,3,4,5,6,7.5,8]); data["params"]["cm_per_year"]=rate
    data["correct_answers"].update(meters_per_second=rate/100/(365.25*86400),km_per_myr=rate/100*1e6/1000)
