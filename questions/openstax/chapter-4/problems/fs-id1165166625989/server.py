import math,random
def generate(data):
 h=random.randint(50,200); down=random.randrange(5,51)/10; horizontal=random.randint(10,35); g=random.choice([9.8,9.81]); t=(-down+math.sqrt(down*down+2*g*h))/g
 data["params"].update(h=h,down=down,horizontal=horizontal,g=g); data["correct_answers"].update(time=t,distance=horizontal*t,vy=-down-g*t)
