import random
def generate(data):
 ax=random.randint(1,15); ay=random.choice([i for i in range(-15,16) if i]); data["params"].update(ax=ax,ay=ay); data["correct_answers"].update(bx=-ay,by=ax)
