import math,random
def generate(data):
 v0=random.randint(7,16); person=random.randrange(150,201)/100; release=person+random.randrange(20,101)/100; g=random.choice([9.8,9.81]); delta=release-person; t=(v0+math.sqrt(v0*v0+2*g*delta))/g
 data["params"].update(v0=v0,person=person,release=release,g=g); data["correct_answers"]["time"]=t
