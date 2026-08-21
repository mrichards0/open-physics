import html
import re

import lxml.html
import prairielearn as pl


SAFE_PARAM = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def render(element_html, data):
    if data["panel"] == "answer":
        return ""
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(
        element,
        ["initial-velocity-param", "final-velocity-param", "duration-param"],
        ["title"],
    )
    names = [pl.get_string_attrib(element, name) for name in (
        "initial-velocity-param", "final-velocity-param", "duration-param"
    )]
    if not all(SAFE_PARAM.fullmatch(name) for name in names):
        raise ValueError("motion simulation parameter names must be safe PrairieLearn identifiers")
    try:
        vi, vf, duration = (float(data["params"][name]) for name in names)
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("motion simulation parameters must exist and be numeric") from error
    if duration <= 0:
        raise ValueError("motion simulation duration must be positive")
    title = pl.get_string_attrib(element, "title", "Constant-acceleration motion")
    acceleration = (vf - vi) / duration
    distance = vi * duration + 0.5 * acceleration * duration * duration
    return f'''<section class="sf-motion-sim" data-vi="{vi}" data-vf="{vf}" data-duration="{duration}" data-distance="{distance}">
<h4>{html.escape(title)}</h4>
<fieldset><legend>Predict before running: how will the velocity change?</legend>
<label><input type="radio" name="sf-sim-prediction" value="increase"> Increase</label>
<label><input type="radio" name="sf-sim-prediction" value="decrease"> Decrease</label>
<label><input type="radio" name="sf-sim-prediction" value="same"> Stay the same</label></fieldset>
<div class="sf-sim-stage" role="img" aria-label="A cart moving horizontally with constant acceleration from {vi:g} to {vf:g} meters per second over {duration:g} seconds.">
<div class="sf-sim-track"></div><div class="sf-sim-cart" aria-hidden="true">●</div></div>
<div class="sf-sim-controls"><button class="btn btn-primary sf-sim-run" type="button" disabled>Run simulation</button><button class="btn btn-outline-secondary sf-sim-reset" type="button">Reset</button></div>
<p class="sf-sim-reading" aria-live="polite">Choose a prediction to enable the simulation.</p>
<noscript><p>The cart changes from {vi:g} m/s to {vf:g} m/s in {duration:g} s with acceleration {acceleration:g} m/s².</p></noscript>
</section>'''
