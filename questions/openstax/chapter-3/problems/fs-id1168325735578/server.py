import random
def generate(data):
 v0=random.randint(10,25); g=random.choice([9.8,9.81]); dt=random.choice([0.4,0.5,0.6,0.75]); ts=[dt*i for i in range(1,5)]; p={"v0":v0,"g":g}; ans={}
 for i,t in enumerate(ts,1): p[f"t{i}"]=t; ans[f"y{i}"]=v0*t-0.5*g*t*t; ans[f"v{i}"]=v0-g*t
 data["params"].update(p); data["correct_answers"].update(ans)
