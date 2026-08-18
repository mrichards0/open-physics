import random
def generate(data):
    d=random.choice([5.0,10.0,21.0975,42.195]); h=random.choice([0,1,2,3]); minutes=random.randrange(0,60); seconds=random.randrange(0,60)
    if h==0 and minutes<15: minutes=15
    du=random.choice([5,10,20,25,50]); tu=random.choice([0.5,1,2]); dm=d*1000; ts=h*3600+minutes*60+seconds; v=dm/ts
    data["params"].update(distance_km=d,hours=h,minutes=minutes,seconds=seconds,distance_uncertainty=du,time_uncertainty=tu)
    data["correct_answers"].update(distance_percent=100*du/dm,time_percent=100*tu/ts,speed=v,speed_uncertainty=v*(du/dm+tu/ts))
