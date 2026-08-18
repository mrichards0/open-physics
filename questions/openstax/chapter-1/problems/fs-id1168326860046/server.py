import math,random
def generate(data):
    m=random.choice([1.0,1.5,2.0,2.5,3.0]); rho=random.choice([800,1000,1200,1400,1600]); angle=random.choice([0.4,0.45,0.5,0.55,0.6])
    radius=(3*m*1e30/(4*math.pi*rho))**(1/3); diameter_km=2*radius/1000; distance_km=diameter_km/math.radians(angle)
    data["params"].update(mass_coeff=m,density=rho,angle_deg=angle); data["correct_answers"].update(diameter_km=diameter_km,distance_km=distance_km)
