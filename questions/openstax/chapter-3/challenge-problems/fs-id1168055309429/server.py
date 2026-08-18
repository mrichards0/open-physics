import random
def generate(data):
 d=random.choice([60,100,200,400]); tw=random.randrange(80,201)/10; tl=tw+random.randrange(2,21)/10; data["params"].update(d=d,tw=tw,tl=tl); data["correct_answers"]["behind"]=d*(1-tw/tl)
