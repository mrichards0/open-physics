import random
def generate(data):
 T1=random.randint(3,7); T2=T1+random.randint(4,8); k1=random.randrange(20,51)/10; vp=k1*T1; k2=random.randrange(5,int(vp/(T2-T1)*10)+1)/10; vf=vp-k2*(T2-T1); ta=random.randrange(10,T1*10)/10; tb=random.randrange(T1*10+1,T2*10)/10; tc=T2+random.randrange(5,31)/10
 def pos(t):
  if t<=T1:return 0.5*k1*t*t
  x1=0.5*k1*T1*T1
  if t<=T2:
   u=t-T1; return x1+vp*u-0.5*k2*u*u
  u=T2-T1; x2=x1+vp*u-0.5*k2*u*u; return x2+vf*(t-T2)
 data["params"].update(T1=T1,T2=T2,k1=k1,k2=k2,vpeak=vp,vfinal=vf,ta=ta,tb=tb,tc=tc); data["correct_answers"].update(a1=k1,a2=-k2,a3=0,xa=pos(ta),xb=pos(tb),xc=pos(tc))
