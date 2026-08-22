import html
import json
import re

import lxml.html
import prairielearn as pl


SAFE_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def _options(element_html):
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(element, ["answers-name", "numerator", "denominator", "units"], [])
    name = pl.get_string_attrib(element, "answers-name")
    if not SAFE_NAME.fullmatch(name):
        raise ValueError("answers-name must be a safe PrairieLearn response name")
    numerator = pl.get_string_attrib(element, "numerator")
    denominator = pl.get_string_attrib(element, "denominator")
    units = [unit.strip() for unit in pl.get_string_attrib(element, "units").split(",")]
    if not numerator or not denominator or any(not unit for unit in units):
        raise ValueError("numerator, denominator, and units must be nonempty")
    if numerator not in units or denominator not in units or len(set(units)) != len(units):
        raise ValueError("units must be unique and contain both correct units")
    return name, numerator, denominator, units


def prepare(element_html, data):
    name, numerator, denominator, _ = _options(element_html)
    data["correct_answers"][name] = json.dumps([numerator, denominator])


def render(element_html, data):
    name, numerator, denominator, units = _options(element_html)
    submitted = data["submitted_answers"].get(name, "")
    selected = ["", ""]
    try:
        candidate = json.loads(submitted)
        if isinstance(candidate, list) and len(candidate) == 2:
            selected = [value if value in units else "" for value in candidate]
    except (TypeError, ValueError):
        pass
    if data["panel"] == "answer":
        return f'<p><strong>Conversion factor:</strong> <span class="sf-factor-answer">{html.escape(numerator)} / {html.escape(denominator)}</span></p>'
    buttons = "".join(
        f'<button type="button" class="sf-unit-token" draggable="true" data-unit="{html.escape(unit)}">{html.escape(unit)}</button>'
        for unit in units
    )
    return f'''<section class="sf-unit-factor" data-answer-name="{html.escape(name)}">
<p class="sf-unit-instructions">Choose a unit, then choose a fraction box—or drag the unit into the box.</p>
<div class="sf-unit-bank" aria-label="Available units">{buttons}</div>
<div class="sf-factor" role="group" aria-label="Conversion factor">
  <button type="button" class="sf-unit-slot" data-position="0" aria-label="Numerator unit">{html.escape(selected[0]) or "Drop numerator unit here"}</button>
  <span class="sf-factor-line" aria-hidden="true"></span>
  <button type="button" class="sf-unit-slot" data-position="1" aria-label="Denominator unit">{html.escape(selected[1]) or "Drop denominator unit here"}</button>
</div>
<input type="hidden" name="{html.escape(name)}" value="{html.escape(json.dumps(selected))}">
<p class="sf-unit-status visually-hidden" aria-live="polite"></p>
</section>'''


def parse(element_html, data):
    name, _, _, units = _options(element_html)
    raw = data["raw_submitted_answers"].get(name, "")
    try:
        values = json.loads(raw)
    except (TypeError, ValueError):
        return
    if isinstance(values, list) and len(values) == 2 and all(value in units for value in values):
        data["submitted_answers"][name] = json.dumps(values)


def grade(element_html, data):
    name, numerator, denominator, _ = _options(element_html)
    expected = json.dumps([numerator, denominator])
    score = 1 if data["submitted_answers"].get(name) == expected else 0
    data["partial_scores"][name] = {"score": score, "weight": 1}
