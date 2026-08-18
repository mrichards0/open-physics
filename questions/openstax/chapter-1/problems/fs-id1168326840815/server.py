import random
def generate(data):
    cc=random.choice([1,2,5,8]); ce=random.choice([-12,-11,-10]); small=random.choice([0.002,0.003,0.004,0.005,0.01]); human=random.randrange(50,101,5); cell=cc*10**ce
    data["params"].update(cell_coeff=cc,cell_exp=ce,small_mass=small,human_mass=human); data["correct_answers"].update(small_cells=small/cell,human_cells=human/cell)
