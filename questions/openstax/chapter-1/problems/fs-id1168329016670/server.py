import random
def generate(data):
    c=random.choice([2.5,4.0,5.0,5.97,7.5,9.0]); e=random.choice([23,24,25]); mm=random.choice([20,25,30,35,40]); na=6.022
    data["params"].update(mass_coeff=c,mass_exp=e,molar_mass=mm,avogadro=na); data["correct_answers"]["molecules"]=c*10**e*1000/mm*na*1e23
