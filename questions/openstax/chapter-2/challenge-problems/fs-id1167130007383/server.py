import math,random
def generate(data):
 while True:
  a,b=random.randint(2,15),random.randint(2,15); lo=abs(a-b)+0.25; hi=a+b-0.25
  if lo<hi: r=random.uniform(lo,hi); break
 c=(r*r-a*a-b*b)/(2*a*b); data["params"].update(a=a,b=b,r=r); data["correct_answers"]["angle"]=math.degrees(math.acos(max(-1,min(1,c))))
