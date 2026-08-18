import random
def generate(data):
    f=random.randint(1,12); n=random.randint(1,5)
    data["params"].update(furlongs=f,fortnights=n); data["correct_answers"]["mm_s"]=f*220*0.9144*1000/(n*14*86400)
