import math,random
def generate(data):
 h=random.randrange(100,401)/10; sec=random.randrange(60,301,10); angle=random.randrange(5,31,5); sound=random.choice([340,343,345]); speed=h*1000/math.sin(math.radians(angle))/sec
 data["params"].update(altitude=h,seconds=sec,angle=angle,sound=sound); data["correct_answers"].update(speed=speed,ratio=speed/sound)
