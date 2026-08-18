# Mastery metadata

This directory is the versioned skill/mastery layer for the imported OpenStax
University Physics Volume 1 Chapters 1–4 question bank. PrairieLearn remains
responsible for question generation, rendering, submission, and grading.

Files:

- `skills.v1.json`: stable mastery areas and skill identifiers.
- `prerequisites.v1.json`: required and recommended prerequisite edges.
- `question-map.v1.jsonl`: one mapping record per PrairieLearn question,
  including response-level skill mappings.
- `pools.v1.json`: derived question pools indexed by primary skill and role.
- `question-map-report.v1.json`: coverage and content-gap summary.

The question map is deliberately separate from PrairieLearn `info.json` files.
This avoids coupling the adaptive layer to unsupported PrairieLearn metadata
and permits the mastery algorithm to evolve independently of question content.

`primarySkill` explains why the adaptive selector chooses a question. The
`skills` array records supporting competencies, while `responseSkills` maps
each PrairieLearn `answers-name` to the skill directly evidenced by that
graded response. Supporting-skill tags alone must not be treated as negative
evidence after an incorrect whole-question result.

Question roles are `diagnostic`, `concept`, `practice`, `mastery`,
`remediation`, and `challenge`. Existing OpenStax conceptual questions are
normally diagnostic questions, not scaffolded concept instruction. Empty
concept and remediation pools are expected until dedicated instructional
questions are authored later.

Skill IDs are API/data identifiers. Once learner evidence refers to an ID, do
not rename or reuse it. Future taxonomy changes should increment the taxonomy
version and provide explicit migrations or deprecation aliases.

Supporting-only mathematics appears only on recommended prerequisite edges in
version 1. These skills may guide remediation, but cannot block readiness until
dedicated diagnostics provide independent mastery evidence.
