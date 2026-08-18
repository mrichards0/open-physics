import random
def generate(data):
 speed=random.randint(8,20); g=random.choice([9.8,9.81]); dt=random.choice([0.3,0.4,0.5]); ts=[dt*i for i in range(1,6)]; fall=speed*ts[-1]+0.5*g*ts[-1]**2; height=random.randint(int(fall)+10,int(fall)+80); p={"speed":speed,"g":g,"height":height}; ans={}
 for i,t in enumerate(ts,1): p[f"t{i}"]=t; ans[f"y{i}"]=-speed*t-0.5*g*t*t; ans[f"v{i}"]=-speed-g*t
 data["params"].update(p); data["correct_answers"].update(ans)
