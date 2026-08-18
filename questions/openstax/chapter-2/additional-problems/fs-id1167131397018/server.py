import math,random
def generate(data):
 d=random.randrange(200,801)/10; a=random.randrange(20,61,5); t=math.radians(a); x=-d*math.cos(t); y=-d*math.sin(t); q=math.sqrt(0.5)
 data["params"].update(distance=d,angle=a); data["correct_answers"].update(south=-y,west=-x,sw45=-q*x-q*y,nw45=-q*x+q*y)
