import html
import math


def two_vector_3d_svg(vectors):
    """Render magnitude/azimuth/elevation vectors from authoritative parameters."""
    panels = []
    for index, (name, magnitude, azimuth, elevation) in enumerate(vectors):
        az = math.radians(azimuth); el = math.radians(elevation)
        x = math.cos(el) * math.cos(az); y = math.cos(el) * math.sin(az); z = math.sin(el)
        ox, oy, scale = 210, 250, 125
        tx = ox + scale * (-0.55 * x + 0.9 * y); ty = oy + scale * (0.35 * x + 0.2 * y - z)
        panels.append(f'''<g transform="translate({index * 360},0)"><rect x="8" y="8" width="344" height="304" rx="14" fill="#f7fafc" stroke="#cbd5df"/><line x1="{ox}" y1="{oy}" x2="82" y2="296" class="axis"/><line x1="{ox}" y1="{oy}" x2="330" y2="250" class="axis"/><line x1="{ox}" y1="{oy}" x2="{ox}" y2="42" class="axis"/><text x="66" y="303">x</text><text x="334" y="256">y</text><text x="216" y="38">z</text><line x1="{ox}" y1="{oy}" x2="{tx:.1f}" y2="{ty:.1f}" class="projection"/><line x1="{tx:.1f}" y1="{ty:.1f}" x2="{tx:.1f}" y2="{oy}" class="projection"/><line x1="{ox}" y1="{oy}" x2="{tx:.1f}" y2="{ty:.1f}" class="vector" marker-end="url(#arrow)"/><text x="20" y="34" class="title">Vector {html.escape(name)}</text><text x="20" y="58">|{html.escape(name)}| = {magnitude:g}</text><text x="20" y="80">azimuth = {azimuth:g}°</text><text x="20" y="102">elevation = {elevation:g}°</text></g>''')
    description = "; ".join(f"vector {name} has magnitude {magnitude:g}, azimuth {azimuth:g} degrees, and elevation {elevation:g} degrees" for name, magnitude, azimuth, elevation in vectors)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" role="img" aria-label="{html.escape(description)}"><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#e65336"/></marker></defs><style>.axis{{stroke:#17324d;stroke-width:2.5}}.vector{{stroke:#e65336;stroke-width:6}}.projection{{stroke:#7b8792;stroke-width:2;stroke-dasharray:6 5}}text{{font:16px system-ui,sans-serif;fill:#17324d}}.title{{font-weight:700;font-size:19px}}</style>{''.join(panels)}</svg>'''
