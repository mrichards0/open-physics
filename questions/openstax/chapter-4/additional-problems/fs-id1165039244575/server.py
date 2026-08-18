import random
def generate(data):
 while True:
  va=random.randrange(50,251)/10; vb=random.randrange(50,251)/10; ra=random.randint(40,200); rb=random.randint(40,200); aa=va*va/ra; ab=vb*vb/rb
  if abs(aa-ab)>0.05: break
 data["params"].update(va=va,vb=vb,ra=ra,rb=rb,a_correct=str(aa>ab).lower(),b_correct=str(ab>aa).lower(),equal_correct="false"); data["correct_answers"].update(aa=aa,ab=ab)
