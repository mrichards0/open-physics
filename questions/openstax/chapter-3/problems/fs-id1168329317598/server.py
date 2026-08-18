import random
def generate(data):
 a,b=random.randint(1,20),random.randint(1,20); data["params"].update(above=a,below=b); data["correct_answers"].update(xa=a,xb=-b)
