import random
def generate(data):
 a,b=random.randint(5,40),random.randint(2,35); data["params"].update(a=a,b=b); data["correct_answers"].update(maximum=a+b,minimum=abs(a-b))
