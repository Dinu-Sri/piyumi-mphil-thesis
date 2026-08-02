# Scientific Writing Style Guide

This file defines the preferred writing style for the thesis. Use it when drafting, editing, reviewing, or polishing chapter Markdown.

## Core Style

- Write in clear formal scientific prose.
- Prefer precise claims over broad claims.
- Keep the argument traceable: problem, gap, method, result, interpretation, limitation.
- Use the student's existing explanatory style as the base, but improve grammar, flow, and scientific precision.
- Keep the writing human: vary sentence length, avoid mechanical transitions, and do not over-polish into generic AI prose.
- Do not make the writing sound like marketing material.

## Voice

- Use objective academic language.
- Prefer "this study" when referring to the thesis work.
- Use active voice when it improves clarity: "This study evaluated..." is often better than "It was evaluated..."
- Passive voice is acceptable for methods when the actor is unimportant: "Diffuse reflectance was measured at 550 nm."
- Do not use first person unless the supervisor explicitly allows it.

## Scientific Claim Discipline

- Do not invent results, references, data, instruments, or interpretations.
- If evidence is missing, write `<!-- TODO: citation needed -->` or `<!-- TODO: verify with data -->`.
- Distinguish clearly between observed results, expected behavior, literature claims, and interpretation.
- Do not say a result "proves" something unless it genuinely does.
- Prefer "indicates", "suggests", "supports", or "is consistent with" when evidence is limited.
- Include limitations where they matter, especially for glass-substrate coating tests versus direct CsI(Tl) application.

## Project Terminology

Use these forms consistently:

- CsI(Tl)
- scintillation detector
- scintillation photon
- photon propagation loss
- reflective coating
- diffuse reflectance
- absorbance
- transmittance
- TiO2, MgO, Al2O3, ZnO, BaSO4
- PVP, PVAc, CMC
- Personal Radiation Detector (PRD)
- Central Alarm Station (CAS)
- Silicon Photomultiplier (SiPM)
- XBee3

Define abbreviations at first use in each major chapter unless already defined in front matter.

## Avoid Common AI-Sounding Wording

Avoid or replace these phrases unless they are genuinely the best technical wording:

- "plays a crucial role"
- "pivotal"
- "robust" when you mean reliable, stable, or high-sensitivity
- "seamless"
- "delves into"
- "landscape"
- "realm"
- "underscores"
- "showcases"
- "cutting-edge"
- "state-of-the-art" unless supported by citation
- "in today's world"
- "rapidly evolving"
- "comprehensive solution" unless the scope truly is comprehensive
- "significant" without statistical or practical support
- "novel" unless novelty is defended against literature
- "optimized" before optimization has been shown

Better replacements:

- Instead of "plays a crucial role", say exactly what the component does.
- Instead of "robust", say "stable after gamma irradiation", "reliable under field conditions", or the measured property.
- Instead of "significant", say "higher", "lower", "measurable", "statistically significant", or give the value.
- Instead of "enhanced" everywhere, alternate with exact outcomes: "higher diffuse reflectance", "lower absorbance at 550 nm", "improved adhesion", or "more uniform coating".

## Human Nuance

Good thesis prose should not sound like every sentence has the same rhythm. Use:

- Short sentences for key findings.
- Longer sentences only when connecting method, condition, and interpretation.
- Transitional phrases that carry logic, not decoration.
- Concrete nouns instead of abstract filler.

Example:

Weak: "This study provides a comprehensive and robust solution for the rapidly evolving radiation monitoring landscape."

Better: "This study links a higher-reflectance TiO2 + PVP coating with a PRD-CAS monitoring concept, addressing both photon collection and real-time reporting."

## Methods Style

- State material, concentration, instrument, condition, and purpose when available.
- Keep chronological order when describing procedures.
- Avoid unnecessary drama.
- Use past tense for completed experiments.
- Use present tense for established facts and chapter structure.

Example:

"Diffuse reflectance was measured at 550 nm because CsI(Tl) emits near this wavelength."

## Results And Discussion Style

- Start with what was measured.
- Report the pattern.
- Interpret only after reporting the pattern.
- Link interpretation to the objective.
- Mention practical limitations.

Preferred structure:

1. Measurement or observation.
2. Main result.
3. Comparison among materials or conditions.
4. Scientific explanation.
5. Consequence for detector performance.
6. Limitation or next step where needed.

## Editing Checklist

Before marking a section improved:

- The research claim is clear.
- The paragraph has one main purpose.
- Citations are present where needed.
- Results are not exaggerated.
- Terms are consistent.
- AI-sounding filler is removed.
- Grammar is improved without changing scientific meaning.

