import math,random
def generate(data):
 A=random.choice([i for i in range(-7,8) if i]); B=random.choice([i for i in range(-5,6) if i]); C=random.choice([i for i in range(-10,11) if i]); te=random.randrange(10,41)/10; s1=random.randrange(5,21)/10; s2=random.randrange(22,51)/10; ta=random.randrange(5,20)/10; tb=random.randrange(int(ta*10)+5,41)/10
 def vel(t):return (2*A*t,3*B*t*t,-2*C*t**-3)
 def pos(t):return (A*t*t,B*t**3,C*t**-2)
 ve=vel(te); vv1=vel(s1); vv2=vel(s2); pa,pb=pos(ta),pos(tb); avg=[(pb[i]-pa[i])/(tb-ta) for i in range(3)]
 data["params"].update(A=A,B=B,C=C,te=te,ts1=s1,ts2=s2,ta=ta,tb=tb); data["correct_answers"].update(v1=2*A,v2=3*B,v3=-2*C,a0=2*A,a1=6*B,a2=6*C,vex=ve[0],vey=ve[1],vez=ve[2],speed1=math.sqrt(sum(x*x for x in vv1)),speed2=math.sqrt(sum(x*x for x in vv2)),avgx=avg[0],avgy=avg[1],avgz=avg[2])
