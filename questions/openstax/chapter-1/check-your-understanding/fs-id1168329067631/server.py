import math, random

def generate(data):
    radius_km = random.choice([5500, 6000, 6370, 6500, 7000])
    mass_sci = random.choice([3.0, 4.0, 5.0, 6.0, 7.0])
    mass_exp = 18
    density = random.choice([0.8, 1.0, 1.2])
    height_m = mass_sci * 10 ** mass_exp / (density * 4 * math.pi * (radius_km * 1000) ** 2)
    data["params"].update(radius_km=radius_km, mass_sci=mass_sci, mass_exp=mass_exp, density=density)
    data["correct_answers"]["height_km"] = height_m / 1000
