import math,random
def generate(data):
 h1=random.randrange(100,251)/100; h2=random.randrange(90,241)/100; ms=random.randrange(40,151)/1000; g=random.choice([9.8,9.81]); vi=-math.sqrt(2*g*h1); vf=math.sqrt(2*g*h2); a=(vf-vi)/(ms*1e-3)
 data["params"].update(hdrop=h1,hrebound=h2,ms=ms,g=g); data["correct_answers"].update(before=vi,after=vf,acceleration=a,compression=vi*vi/(2*a))
