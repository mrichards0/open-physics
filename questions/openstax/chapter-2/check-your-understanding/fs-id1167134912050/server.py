import random
def generate(data):
 vals=[random.randint(-12,12) for _ in range(8)]; ax,ay,bx,by,fx,fy,cx,cy=vals
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by,fx=fx,fy=fy,cx=cx,cy=cy); data["correct_answers"].update(ab=ax*bx+ay*by,fc=fx*cx+fy*cy)
