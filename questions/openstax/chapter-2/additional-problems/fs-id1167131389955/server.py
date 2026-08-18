import random
def generate(data):
 k=random.randint(2,6); ax,ay,bx,by=[random.randint(-20,20) for _ in range(4)]; data["params"].update(k=k,ax=ax,ay=ay,bx=bx,by=by); data["correct_answers"].update(cx=(bx-ax)/k,cy=(by-ay)/k)
