import math,random
def generate(data):
    m=random.choice([5.0,6.0,7.0,7.35,8.0,9.0]); r=random.randrange(1400,2201,50); angle=random.choice([0.4,0.45,0.5,0.55,0.6])
    density=m*1e22/(4*math.pi*(r*1000)**3/3); diameter=2*r; distance=diameter/math.radians(angle)
    data["params"].update(mass_coeff=m,radius_km=r,angle_deg=angle); data["correct_answers"].update(density=density,diameter=diameter,distance=distance)
