import math,random
def generate(data):
 kmh=random.randint(25,60); v=kmh/3.6; a=random.randint(40,75); g=random.choice([9.8,9.81]); possible=v*v/(2*g); target=random.randrange(10,max(11,int(possible*80)))/100; needed=math.degrees(math.asin(math.sqrt(2*g*target)/v)); height=v*v*math.sin(math.radians(a))**2/(2*g)
 data["params"].update(kmh=kmh,angle=a,g=g,target=target); data["correct_answers"].update(height=height,needed=needed)
