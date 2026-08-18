import random
def generate(data):
    years=random.randrange(60,101,5); bpm=random.randrange(55,86,5); data["params"].update(years=years,bpm=bpm); data["correct_answers"]["beats"]=bpm*years*365.25*24*60
