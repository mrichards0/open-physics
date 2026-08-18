import random
def generate(data):
    bc=random.choice([1,2,5,8]); be=random.choice([-16,-15,-14]); multiple=random.choice([8,10,12,15,20]); pc=1.67
    data["params"].update(b_coeff=bc,b_exp=be,multiple=multiple,p_coeff=pc); data["correct_answers"]["atoms"]=bc*10**be/(multiple*pc*1e-27)
