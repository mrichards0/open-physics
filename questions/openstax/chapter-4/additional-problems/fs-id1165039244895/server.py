import random
def generate(data):
 boat=random.randrange(20,151)/10; current=random.randrange(5,int(boat*10))/10; down=boat+current; up=boat-current; data["params"].update(downstream=down,upstream=up); data["correct_answers"].update(boat=boat,current=current)
