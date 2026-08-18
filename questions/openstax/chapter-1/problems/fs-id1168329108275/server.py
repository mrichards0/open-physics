import math,random
def generate(data):
    c=random.choice([1.1,1.5,2.0,2.8,3.2,4.0,5.1,6.5,8.0,9.5]); e=random.randint(-31,30); unit=random.choice(["kg","m","s","J"])
    data["params"].update(coefficient=c,exponent=e,unit=unit); data["correct_answers"]["order_exponent"]=e+(1 if c>=math.sqrt(10) else 0)
