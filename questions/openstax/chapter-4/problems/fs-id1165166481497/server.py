import math, random
def generate(data):
    while True:
        v = random.randrange(160, 301) / 10
        u = random.randrange(60, 121) / 10
        start = random.randrange(50, 151) / 10
        finish = start + random.randrange(50, 151) / 10
        g = random.choice([9.8, 9.81])
        t = (finish-start)/u
        s = g*t/(2*v)
        if 0.15 < s < 0.85:
            break
    angle = math.degrees(math.asin(s))
    ball_x = v*math.cos(math.radians(angle))*t
    caught = abs(ball_x-finish) <= 0.25
    data["params"].update(ball_speed=v, run_speed=u, start=start, finish=finish, g=g,
                          catch_yes=str(caught).lower(), catch_no=str(not caught).lower())
    data["correct_answers"].update(time=t, angle=angle, ball_x=ball_x)
