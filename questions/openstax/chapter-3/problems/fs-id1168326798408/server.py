import random
def generate(data):
 r,l=random.randint(5,40),random.randint(5,40); tr,tl=random.randint(2,12),random.randint(2,12); total=tr+tl; data["params"].update(right=r,left=l,tr=tr,tl=tl); data["correct_answers"].update(velocity=(r-l)/total,speed=(r+l)/total)
