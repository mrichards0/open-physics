import math,random
def generate(data):
 while True:
  ax,ay,bx,by=[random.randint(-10,10) for _ in range(4)]; cx,cy=random.randint(-10,10),random.randint(-10,10); cz=random.choice([i for i in range(-10,11) if i]); z=ax*by-ay*bx
  if z and (ax or ay) and (bx or by): break
 cos_ab=(ax*bx+ay*by)/(math.hypot(ax,ay)*math.hypot(bx,by)); angle_ab=math.degrees(math.acos(max(-1,min(1,cos_ab))))
 c_mag=math.sqrt(cx*cx+cy*cy+cz*cz); cos_cross_c=z*cz/(abs(z)*c_mag); angle_c=math.degrees(math.acos(max(-1,min(1,cos_cross_c))))
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by,cx=cx,cy=cy,cz=cz); data["correct_answers"].update(cross_z=z,cross_mag=abs(z),ab_angle=angle_ab,cross_c_angle=angle_c)
