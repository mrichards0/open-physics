import random
def generate(data):
    beats=random.randrange(25,61); bu=random.choice([1,2]); time=random.choice([15,20,30,40,60]); tu=random.choice([0.2,0.5,1.0])
    rate=60*beats/time; data["params"].update(beats=beats,beat_uncertainty=bu,time=time,time_uncertainty=tu)
    data["correct_answers"].update(rate=rate,rate_uncertainty=rate*(bu/beats+tu/time))
