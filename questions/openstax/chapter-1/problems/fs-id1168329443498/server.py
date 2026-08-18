import random
def generate(data):
    m=random.randrange(45,101); mm=18.0; na=6.022
    data["params"].update(mass_kg=m,molar_mass=mm,avogadro=na); data["correct_answers"]["molecules"]=m*1000/mm*na*1e23
