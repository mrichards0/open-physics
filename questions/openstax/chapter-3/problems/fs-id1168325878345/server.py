import random
def generate(data):
 a=random.randrange(5,31)/10; v=random.randrange(10,61)/10; tb=random.randrange(4,21)/10; data["params"].update(a=a,v=v,tb=tb); data["correct_answers"].update(time=v/a,braking=-v/tb)
