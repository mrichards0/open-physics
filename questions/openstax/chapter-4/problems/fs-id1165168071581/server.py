import math,random
def generate(data):
 while True:
  v=random.randint(50,100); la=random.randint(45,70); sl=random.randint(10,30); b=random.randint(50,180); g=random.choice([9.8,9.81]); k=g/(2*v*v*math.cos(math.radians(la))**2); m=math.tan(math.radians(la))-math.tan(math.radians(sl)); disc=m*m+4*k*b; x=(m+math.sqrt(disc))/(2*k); y=math.tan(math.radians(sl))*x-b; xb=b/math.tan(math.radians(sl))
  if x>xb and y>0: break
 along=math.hypot(x-xb,y); data["params"].update(v0=v,launch=la,slope=sl,intercept=b,g=g); data["correct_answers"].update(x=x,y=y,along=along)
