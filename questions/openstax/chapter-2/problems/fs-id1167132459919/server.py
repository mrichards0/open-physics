import math,random
def generate(data):
 vals=[random.randint(-9,9) for _ in range(9)]; a=vals[:3]; b=vals[3:6]; c=vals[6:]; r=[a[i]+b[i]+c[i] for i in range(3)]
 if r==[0,0,0]: r[0]=1; a[0]+=1
 data["params"].update(a1=a[0],a2=a[1],a3=a[2],b1=b[0],b2=b[1],b3=b[2],c1=c[0],c2=c[1],c3=c[2]); data["correct_answers"].update(x=r[0],y=r[1],z=r[2],magnitude=math.sqrt(sum(v*v for v in r)),path=sum(math.sqrt(sum(v*v for v in q)) for q in (a,b,c)))
