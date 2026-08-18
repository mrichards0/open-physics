import math,random
def generate(data):
 px,py,qx,qy=[random.randint(-12,12) for _ in range(4)]; phi=random.randrange(10,351,10); c=math.cos(math.radians(phi)); s=math.sin(math.radians(phi)); rot=lambda x,y:(x*c+y*s,-x*s+y*c); pp=rot(px,py); qp=rot(qx,qy); op2=px*px+py*py; pq2=(px-qx)**2+(py-qy)**2
 data["params"].update(px=px,py=py,qx=qx,qy=qy,phi=phi); data["correct_answers"].update(pxp=pp[0],pyp=pp[1],qxp=qp[0],qyp=qp[1],op2=op2,op2p=pp[0]**2+pp[1]**2,pq2=pq2,pq2p=(pp[0]-qp[0])**2+(pp[1]-qp[1])**2)
