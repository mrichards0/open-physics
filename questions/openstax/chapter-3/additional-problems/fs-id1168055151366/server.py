import random
def generate(data):
 lt=random.randrange(60,181)/10; lc=random.randrange(25,61)/10; vc=random.randint(50,100); vt=vc+random.randint(10,40); data["params"].update(lt=lt,lc=lc,vt=vt,vc=vc); data["correct_answers"]["time"]=(lt+lc)/((vt-vc)/3.6)
