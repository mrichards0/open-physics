import math,random
def generate(data):
 v0=random.randint(4,15); g=random.choice([9.8,9.81]); minimum=2*v0/g+0.5; tup=random.randrange(int(minimum*10)+1,int(minimum*10)+41)/10; h=0.5*g*tup*tup-v0*tup; td=(-v0+math.sqrt(v0*v0+2*g*h))/g
 data["params"].update(v0=v0,g=g,tup=tup); data["correct_answers"].update(height=h,tdown=td)
