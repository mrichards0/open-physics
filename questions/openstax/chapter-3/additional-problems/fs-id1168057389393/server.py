import random
def generate(data):
 while True:
  d=random.randrange(170,201)/10; kmh=random.randint(130,180); reaction=random.randrange(20,36)/100; t=d/(kmh/3.6)
  if t>reaction: break
 data["params"].update(distance=d,kmh=kmh,reaction=reaction); data["correct_answers"].update(time=t,ratio=t/reaction)
