import random
def generate(data):
 ax=random.choice([i for i in range(-10,11) if i]); ay=random.choice([i for i in range(-10,11) if i]); data["params"].update(ax=ax,ay=ay); data["correct_answers"].update(cx=ax/2,cy=ay/2,dx=ax,dy=ay,slope=ay/ax)
