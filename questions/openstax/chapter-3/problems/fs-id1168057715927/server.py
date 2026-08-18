import random
def generate(data):
 A=random.randrange(100,401)/10; B=random.randrange(10,101)/10; t=random.randrange(10,61)/10; data["params"].update(A=A,B=B,t=t); data["correct_answers"].update(velocity=A*t-(2/3)*B*t**1.5,position=0.5*A*t*t-(4/15)*B*t**2.5)
