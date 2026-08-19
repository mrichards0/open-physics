import html
import random

from spiritsfire_physics.kinematics import acceleration_case


def generate(data):
    case = acceleration_case(random, "guided")
    data["params"].update(case.params())
    data["params"].update(
        motion_alt=f"Velocity arrows increase from {case.initial_velocity} meters per second initially to {case.final_velocity} meters per second finally.",
        graph_alt=f"Velocity-time graph is a straight line from {case.initial_velocity} meters per second at zero seconds to {case.final_velocity} meters per second at {case.elapsed_time} seconds.",
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
    if data["filename"] == "velocity-graph.svg":
        x2 = 350
        y1 = 140 - 90 * p["vi"] / p["vf"]
        y2 = 50
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="180" viewBox="0 0 420 180" role="img" aria-label="{html.escape(p['graph_alt'])}">
<rect width="420" height="180" rx="12" fill="#f5f8fb"/><line x1="55" y1="145" x2="385" y2="145" stroke="#17324d" stroke-width="3"/><line x1="55" y1="145" x2="55" y2="25" stroke="#17324d" stroke-width="3"/>
<line x1="75" y1="{y1:.1f}" x2="{x2}" y2="{y2}" stroke="#087e8b" stroke-width="6"/><circle cx="75" cy="{y1:.1f}" r="6" fill="#d1495b"/><circle cx="{x2}" cy="{y2}" r="6" fill="#1b6f5a"/>
<text x="10" y="28" font-family="sans-serif" font-size="16">v (m/s)</text><text x="365" y="170" font-family="sans-serif" font-size="16">t (s)</text>
<text x="62" y="165" font-family="sans-serif" font-size="14">0</text><text x="340" y="165" font-family="sans-serif" font-size="14">{p['dt']}</text>
<text x="82" y="{y1-8:.1f}" font-family="sans-serif" font-size="14">{p['vi']}</text><text x="325" y="42" font-family="sans-serif" font-size="14">{p['vf']}</text></svg>'''
