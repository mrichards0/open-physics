import random
def generate(data):
 v=random.randint(100,350); ta=random.randrange(20,101)/10; tb=random.randrange(5,31)/10; g=random.choice([9.8,9.81]); au=v/ta; ad=-v/tb
 data["params"].update(v=v,ta=ta,tb=tb,g=g); data["correct_answers"].update(aup=au,adown=ad,gup=au/g,gdown=ad/g)
