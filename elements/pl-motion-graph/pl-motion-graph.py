import html
import re

import lxml.html
import prairielearn as pl


SAFE_PARAM = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def _config(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(
        element,
        ["initial-velocity-param", "final-velocity-param", "duration-param"],
        ["title"],
    )
    names = [
        pl.get_string_attrib(element, "initial-velocity-param"),
        pl.get_string_attrib(element, "final-velocity-param"),
        pl.get_string_attrib(element, "duration-param"),
    ]
    if not all(SAFE_PARAM.fullmatch(name) for name in names):
        raise ValueError("motion graph parameter names must be safe PrairieLearn identifiers")
    try:
        vi, vf, duration = (float(data["params"][name]) for name in names)
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("motion graph parameters must exist and be numeric") from error
    if duration <= 0:
        raise ValueError("motion graph duration must be positive")
    title = pl.get_string_attrib(element, "title", "Velocity–time graph")
    return vi, vf, duration, title


def render(element_html, data):
    if data["panel"] == "answer":
        return ""
    vi, vf, duration, title = _config(element_html, data)
    low, high = min(0, vi, vf), max(0, vi, vf)
    span = max(high - low, 1)
    y = lambda value: 154 - 112 * (value - low) / span
    y_zero, y_vi, y_vf = y(0), y(vi), y(vf)
    acceleration = (vf - vi) / duration
    label = html.escape(
        f"{title}. Velocity changes linearly from {vi:g} meters per second at zero seconds "
        f"to {vf:g} meters per second at {duration:g} seconds."
    )
    return f'''<section class="sf-motion-graph" data-vi="{vi}" data-vf="{vf}" data-duration="{duration}" aria-label="{label}">
<h4>{html.escape(title)}</h4>
<svg viewBox="0 0 460 210" role="img" aria-labelledby="sf-graph-title sf-graph-desc">
<title id="sf-graph-title">{html.escape(title)}</title><desc id="sf-graph-desc">{label}</desc>
<rect width="460" height="210" rx="14" fill="#f4fbfa"/>
<line x1="62" y1="{y_zero:.2f}" x2="425" y2="{y_zero:.2f}" class="sf-axis"/><line x1="62" y1="174" x2="62" y2="24" class="sf-axis"/>
<line x1="82" y1="{y_vi:.2f}" x2="398" y2="{y_vf:.2f}" class="sf-velocity-line"/>
<circle cx="82" cy="{y_vi:.2f}" r="6"/><circle cx="398" cy="{y_vf:.2f}" r="6"/>
<line class="sf-cursor" x1="82" y1="24" x2="82" y2="174"/><circle class="sf-cursor-dot" cx="82" cy="{y_vi:.2f}" r="7"/>
<text x="12" y="25">v (m/s)</text><text x="405" y="198">t (s)</text><text x="72" y="195">0</text><text x="383" y="195">{duration:g}</text>
</svg>
<p class="sf-graph-reading" aria-live="polite">At t = 0 s, v = {vi:g} m/s.</p>
<p class="small text-muted">Move across the graph to inspect time and velocity. Its slope is the constant acceleration.</p>
<table class="table table-sm sf-graph-table"><caption class="visually-hidden">Graph endpoint values</caption><thead><tr><th>Time</th><th>Velocity</th></tr></thead><tbody><tr><td>0 s</td><td>{vi:g} m/s</td></tr><tr><td>{duration:g} s</td><td>{vf:g} m/s</td></tr></tbody></table>
<span class="visually-hidden">The slope is {acceleration:g} meters per second squared.</span>
</section>'''
