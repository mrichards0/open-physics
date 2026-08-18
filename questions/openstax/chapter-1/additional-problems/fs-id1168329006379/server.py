import random
def generate(data):
    reading=random.randrange(50,131,5); pct=random.choice([1,2,3,4,5,6,8,10]); delta=reading*pct/100; lo=reading-delta; hi=reading+delta
    data["params"].update(reading=reading,percent=pct); data["correct_answers"].update(low_kmh=lo,high_kmh=hi,low_mph=lo*0.6214,high_mph=hi*0.6214)
