import math,random
def generate(data):
 while True:
  a,b,c,d=[random.randint(-20,20) for _ in range(4)]
  if (a or b) and (c or d):
   cosine=(a*c+b*d)/(math.hypot(a,b)*math.hypot(c,d))
   if abs(cosine)<0.98: break
 angle=math.degrees(math.acos(max(-1,min(1,cosine))))
 data["params"].update(f1x=a,f1y=b,f3x=c,f3y=d); data["correct_answers"]["angle"]=angle
