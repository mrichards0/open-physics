import random
def generate(data):
 a=random.randrange(15,101)/100; v=random.randrange(30,101)/10; data["params"].update(a=a,v=v); data["correct_answers"].update(distance=v*v/(2*a),time=v/a)
