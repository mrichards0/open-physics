import random
def generate(data):
 kmh=random.randrange(400,1210,10)/10; v=kmh/3.6; a1=random.randrange(80,251)/100; a2=random.randrange(100,301)/100; te=random.randrange(40,151)/10; data["params"].update(kmh=kmh,a1=a1,a2=a2,te=te); data["correct_answers"].update(ta=v/a1,tb=v/a2,ae=-v/te)
