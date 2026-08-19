import re

import lxml.etree
import lxml.html
import prairielearn as pl


SAFE_ID = re.compile(r"^[a-z][a-z0-9_-]*$")


def _element(element_html):
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(element, ["step-id", "title"], ["response-names"])
    step_id = pl.get_string_attrib(element, "step-id")
    if not SAFE_ID.fullmatch(step_id):
        raise ValueError("step-id must start with a letter and contain only lowercase letters, digits, _ or -")
    return element, step_id


def _hints(element, step_id):
    hints = []
    for child in element:
        if child.tag != "pl-learning-hint":
            continue
        pl.check_attribs(child, ["hint-id", "title"], [])
        hint_id = pl.get_string_attrib(child, "hint-id")
        if not SAFE_ID.fullmatch(hint_id):
            raise ValueError("hint-id must start with a letter and contain only lowercase letters, digits, _ or -")
        hints.append({
            "id": hint_id,
            "title": pl.get_string_attrib(child, "title"),
            "content": pl.inner_html(child),
            "trace_name": f"_sf_hint__{step_id}__{hint_id}",
        })
    if len({hint["id"] for hint in hints}) != len(hints):
        raise ValueError(f"Duplicate hint-id in learning step {step_id}")
    return hints


def prepare(element_html, data):
    element, step_id = _element(element_html)
    for hint in _hints(element, step_id):
        data["correct_answers"][hint["trace_name"]] = "opened"


def render(element_html, data):
    element, step_id = _element(element_html)
    hints = _hints(element, step_id)
    for child in list(element):
        if child.tag == "pl-learning-hint":
            element.remove(child)
    content = pl.inner_html(element)
    title = pl.get_string_attrib(element, "title")
    responses = pl.get_string_attrib(element, "response-names", "")
    if data["panel"] == "answer":
        return ""
    hint_html = "".join(
        f'''<details class="sf-learning-hint" data-hint-id="{hint['id']}">
<summary>{hint['title']}</summary><div class="sf-learning-hint-body">{hint['content']}</div>
</details><input type="hidden" name="{hint['trace_name']}" value="">'''
        for hint in hints
    )
    return f'''<section class="sf-learning-step" data-step-id="{step_id}" data-response-names="{responses}" aria-labelledby="sf-step-{step_id}-title">
<h4 id="sf-step-{step_id}-title">{title}</h4>
<div class="sf-learning-step-content">{content}</div>
<div class="sf-learning-hints" aria-label="Hints for {title}">{hint_html}</div>
</section>'''


def parse(element_html, data):
    element, step_id = _element(element_html)
    for hint in _hints(element, step_id):
        name = hint["trace_name"]
        if data["raw_submitted_answers"].get(name) == "opened":
            data["submitted_answers"][name] = "opened"


def grade(element_html, data):
    element, step_id = _element(element_html)
    for hint in _hints(element, step_id):
        name = hint["trace_name"]
        if data["submitted_answers"].get(name) == "opened":
            # Telemetry only: the zero weight cannot change PrairieLearn's grade.
            data["partial_scores"][name] = {"score": 1, "weight": 0}
