import math,random
def generate(data):
 h1,h2=random.randrange(500,2001,50),random.randrange(500,2001,50); r1,r2=random.randrange(100,301)/10,random.randrange(100,301)/10; a1,a2=random.randrange(10,46,5),random.randrange(10,46,5)
 def xy(r,a): t=math.radians(a); return -r*math.cos(t),-r*math.sin(t)
 x1,y1=xy(r1,a1); x2,y2=xy(r2,a2); d=math.sqrt((x1-x2)**2+(y1-y2)**2+((h1-h2)/1000)**2)
 data["params"].update(h1=h1,h2=h2,r1=r1,r2=r2,a1=a1,a2=a2); data["correct_answers"]["distance"]=d
