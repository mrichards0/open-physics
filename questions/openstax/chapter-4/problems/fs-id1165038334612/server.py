import random
def generate(data):
 v0x,v0y,vTx,vTy=[random.randint(-20,20) for _ in range(4)]; T=random.randint(2,10); ax=(vTx-v0x)/T; ay=(vTy-v0y)/T; data["params"].update(v0x=v0x,v0y=v0y,vTx=vTx,vTy=vTy,T=T); data["correct_answers"].update(ax=ax,ay=ay,c1=v0x,c2=ax/2,d1=v0y,d2=ay/2,e0=v0x,e1=ax,f0=v0y,f1=ay)
