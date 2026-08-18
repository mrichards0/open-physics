import random
def generate(data):
 d1,d2,d3=[random.randint(5,25) for _ in range(3)]; u1,u2=[random.randint(1,8) for _ in range(2)]; displacement=-d1+u1-d2+u2-d3
 data["params"].update(d1=d1,d2=d2,d3=d3,u1=u1,u2=u2); data["correct_answers"].update(displacement=displacement,distance=abs(displacement))
