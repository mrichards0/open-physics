import html
import random

from spiritsfire_physics.kinematics import acceleration_case


def generate(data):
    case = acceleration_case(random, "guided")
    data["params"].update(case.params())
    data["params"].update(
        motion_alt=f"Velocity arrows increase from {case.initial_velocity} meters per second initially to {case.final_velocity} meters per second finally.",
    )
    data["correct_answers"].update(case.answers())


def file(data):
    p = data["params"]
    if data["filename"] == "motion.svg":
        initial = 45 + 80 * p["vi"] / p["vf"]
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="180" viewBox="0 0 420 180" role="img" aria-label="{html.escape(p['motion_alt'])}">
<rect width="420" height="180" rx="12" fill="#f5f8fb"/><line x1="35" y1="145" x2="390" y2="145" stroke="#52606d" stroke-width="3"/>
<circle cx="80" cy="122" r="16" fill="#087e8b"/><circle cx="300" cy="122" r="16" fill="#087e8b"/>
<line x1="80" y1="85" x2="{initial:.1f}" y2="85" stroke="#d1495b" stroke-width="7"/><polygon points="{initial:.1f},85 {initial-14:.1f},76 {initial-14:.1f},94" fill="#d1495b"/>
<line x1="300" y1="85" x2="390" y2="85" stroke="#1b6f5a" stroke-width="7"/><polygon points="390,85 376,76 376,94" fill="#1b6f5a"/>
<text x="60" y="55" font-family="sans-serif" font-size="18">vᵢ = {p['vi']} m/s</text><text x="275" y="55" font-family="sans-serif" font-size="18">v_f = {p['vf']} m/s</text>
<text x="150" y="172" font-family="sans-serif" font-size="17">elapsed time = {p['dt']} s</text></svg>'''
