"""BL Agency blog kit: builds a long-form post page from a spec, adds it to /blog and sitemap.xml.

Usage (from the repo root):
    python3 tools/blogkit.py tools/posts/<slug>.py

A spec file defines a dict named POST. See tools/posts/ for examples and tools/BLOG_RULES.md for the rules.
The page shell (head scripts, nav, footer, CSS) is copied from an existing post so every post stays in sync.
"""
import json, re, sys, pathlib, runpy, html as H

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / 'blog' / 'hire-bilingual-sdr-latin-america.html'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'

PETROL, AMBER, MUTED, LINE = '#0d4747', '#c9862b', '#56625f', '#dcd5c7'


# ---------------- charts (single series, site colors, hover titles) ----------------
def bar_chart(title, rows, unit='', vmax=None, highlight=()):
    """rows: [(label, value)]. Horizontal bars, one hue; labels in `highlight` get the accent."""
    vmax = vmax or max(v for _, v in rows) * 1.15
    x0, x1 = 240, 690
    X = lambda v: x0 + v / vmax * (x1 - x0)
    h = 28 + len(rows) * 40
    out = [f'<svg viewBox="0 0 720 {h}" role="img" class="chart"><title>{H.escape(title)}</title>']
    for i, (lab, v) in enumerate(rows):
        y = 10 + i * 40
        c = AMBER if lab in highlight else PETROL
        out.append(f'<text x="0" y="{y + 14}" class="lb">{H.escape(lab)}</text>')
        out.append(f'<rect x="{x0}" y="{y}" width="{max(X(v) - x0, 6):.0f}" height="18" rx="4" fill="{c}"><title>{H.escape(lab)}: {v}{unit}</title></rect>')
        out.append(f'<text x="{X(v) + 8:.0f}" y="{y + 14}" class="vl">{v}{unit}</text>')
    out.append('</svg>')
    return ''.join(out)


def timeline(title, segs, total, unit='min', accent=()):
    """segs: [(start, end, label, sublabel)]."""
    X = lambda m: m / total * 720
    out = [f'<svg viewBox="0 0 720 96" role="img" class="chart"><title>{H.escape(title)}</title>']
    for i, (a, b, t, d) in enumerate(segs):
        last = i == len(segs) - 1
        xa, xb = X(a) + (0 if i == 0 else 1), X(b) - (0 if last else 1)
        c = AMBER if t in accent else PETROL
        out.append(f'<rect x="{xa:.0f}" y="20" width="{xb - xa:.0f}" height="44" rx="4" fill="{c}"><title>{H.escape(t)}</title></rect>')
        out.append(f'<text x="{xa + 10:.0f}" y="47" class="sg">{H.escape(t)}</text>')
        tx, anc = (xb, 'end') if last else (xa + 2, 'start')
        out.append(f'<text x="{tx:.0f}" y="84" text-anchor="{anc}" class="dl">{H.escape(d)}</text>')
        top = f'{a} to {b} {unit}' if last else f'{a} {unit}'
        out.append(f'<text x="{tx:.0f}" y="12" text-anchor="{anc}" class="ax">{top}</text>')
    out.append('</svg>')
    return ''.join(out)


def steps(title, items, accent=()):
    """A left-to-right process: items = [(label, sublabel)]."""
    n = len(items); w = 720 / n
    out = [f'<svg viewBox="0 0 720 100" role="img" class="chart"><title>{H.escape(title)}</title>']
    for i, (t, d) in enumerate(items):
        xa = i * w + (0 if i == 0 else 3); xb = (i + 1) * w - (0 if i == n - 1 else 3)
        c = AMBER if t in accent else PETROL
        out.append(f'<rect x="{xa:.0f}" y="8" width="{xb - xa:.0f}" height="44" rx="4" fill="{c}"><title>{H.escape(t)}</title></rect>')
        out.append(f'<text x="{xa + 10:.0f}" y="35" class="sg">{i + 1}. {H.escape(t)}</text>')
        out.append(f'<text x="{xa + 2:.0f}" y="74" class="dl">{H.escape(d)}</text>')
    out.append('</svg>')
    return ''.join(out)


def table(headers, rows):
    th = ''.join(f'<th>{h}</th>' for h in headers)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def figure(n, svg_or_html, caption):
    return f'<figure class="fig">{svg_or_html}<figcaption><b>Figure {n}.</b> {caption}</figcaption></figure>'


# ---------------- page build ----------------
def build(P):
    slug, url = P['slug'], f"https://www.brain-labs.io/blog/{P['slug']}"
    s = TEMPLATE.read_text()
    title, desc, img = P['title'], P['description'], P['hero_img']

    # head
    s = re.sub(r'<title>.*?</title>', f'<title>{H.escape(title)} | BL Agency</title>', s, 1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(desc)}">', s, 1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', s, 1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{H.escape(title)}">', s, 1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{H.escape(desc)}">', s, 1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', s, 1)
    s = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="https://www.brain-labs.io/img/{img}.jpg">', s, 1)
    post = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": title, "description": desc,
            "author": {"@type": "Organization", "name": "BL Agency team", "url": "https://www.brain-labs.io"},
            "publisher": {"@type": "Organization", "name": "BL Agency", "url": "https://www.brain-labs.io"},
            "datePublished": P['date'], "image": f"https://www.brain-labs.io/img/{img}.jpg", "mainEntityOfPage": url}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in P['faq']]}
    s = re.sub(r'(<script type="application/ld\+json">.*?</script>\s*){2}',
               '<script type="application/ld+json">\n' + json.dumps(post, indent=2) + '\n</script>\n<script type="application/ld+json">\n' + json.dumps(faq, indent=2) + '\n</script>\n', s, 1, flags=re.S)

    # hero image + header text
    s = re.sub(r'<div class="ph-img" aria-hidden="true">.*?</div>',
               f'<div class="ph-img" aria-hidden="true"><picture><source srcset="/img/{img}.webp" type="image/webp"><img src="/img/{img}.jpg" alt=""></picture></div>', s, 1, flags=re.S)
    hero = f'''  <div class="wrap hero-body article">
    <p class="label"><a href="/blog" style="text-decoration:none">Blog</a> · {P['category']}</p>
    <h1>{P['h1']}</h1>
    <div class="meta"><span>By the BL Agency team</span><span>READTIME</span><span>{P['date_label']}</span></div>
  </div>
</header>'''
    s = re.sub(r'  <div class="wrap hero-body article">.*?</header>', hero, s, 1, flags=re.S)

    # body
    secs = P['sections']
    n = len(secs)
    toc = ''.join(f'<a href="#{sid}"><span>{i + 1:02d}</span>{t}</a>' for i, (sid, t, _) in enumerate(secs))
    toc += f'<a href="#conclusion"><span>{n + 1:02d}</span>Bringing it together</a><a href="#faq"><span>{n + 2:02d}</span>Frequently asked questions</a>'
    body = ''.join(f'<h2 id="{sid}"><span class="num">{i + 1:02d}</span>{t}</h2>{h}' for i, (sid, t, h) in enumerate(secs))
    tk = '<div class="takeaways"><p class="label">Key takeaways</p><ul>' + ''.join(f'<li>{x}</li>' for x in P['takeaways']) + '</ul></div>'
    cta = P['cta']
    inline = f'<div class="callout cta-inline"><p><b>{cta["inline_lead"]}</b> {cta["inline_text"]}</p><a class="btn btn-fill" href="{cta["href"]}"{cta.get("target", "")}>{cta["button"]}</a></div>'
    concl = f'<h2 id="conclusion"><span class="num">{n + 1:02d}</span>Bringing it together</h2>{P["conclusion"]}'
    faqh = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in P['faq'])
    about = ('<div class="about-box"><p class="label">About the author</p><p><b>The BL Agency team</b> builds and runs outbound for US B2B companies '
             'with a base of AI agents and a dedicated Agent Base manager, and places bilingual sales professionals from Latin America with US teams. '
             '<a href="/">See the Agent Base</a> · <a href="/talent">Hire sales talent</a></p></div>')
    main = f'''<main>
  <section>
    <div class="wrap article prose">
      {tk}
      {P['intro']}
      {inline}
      <nav class="toc" aria-label="On this page"><b>On this page</b>{toc}</nav>
      {body}
      {concl}
      <h2 id="faq"><span class="num">{n + 2:02d}</span>Frequently asked questions</h2>
      <div class="faq-list">{faqh}</div>
      {about}
    </div>
  </section>
  <section class="invite">
    <div class="wrap invite-grid">
      <div class="head"><p class="label">{cta['band_label']}</p><h2>{cta['band_h2']}</h2><p class="lede">{cta['band_text']}</p></div>
      <div class="cta"><a class="btn btn-fill" href="{cta['href']}"{cta.get('target', '')}>{cta['button']}</a><a class="btn btn-line" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div>
    </div>
  </section>
</main>'''
    s = re.sub(r'<main>.*?</main>', main, s, 1, flags=re.S)
    text = re.sub(r'<[^>]+>', ' ', main)
    words = len(re.findall(r"[A-Za-z0-9$']+", text))
    s = s.replace('READTIME', f'{max(1, round(words / 230))} min read')

    # checks
    problems = []
    if '—' in s: problems.append('em dash found')
    if re.search(r'\$\s?\d', main): problems.append('price or dollar figure found (no prices rule)')
    if words < 2000: problems.append(f'only {words} words (target 2,200 to 2,800)')
    if problems:
        raise SystemExit('NOT BUILT: ' + '; '.join(problems))

    out = ROOT / 'blog' / f'{slug}.html'
    out.write_text(s)

    # blog index card (newest first, after the featured card)
    b = (ROOT / 'blog.html').read_text()
    if f'href="/blog/{slug}"' not in b:
        card = (f'<a class="post" href="/blog/{slug}"><div class="thumb"><picture><source srcset="/img/{P["card_img"]}.webp" type="image/webp">'
                f'<img src="/img/{P["card_img"]}.jpg" alt="" loading="lazy"></picture></div><div class="pb"><p class="label">{P["category"]}</p>'
                f'<h3>{P["card_title"]}</h3><p>{P["card_text"]}</p></div></a>')
        m = re.search(r'(<a class="post featured"[^>]*>.*?</a>)', b, re.S)
        b = b[:m.end()] + card + b[m.end():]
        (ROOT / 'blog.html').write_text(b)

    sm = (ROOT / 'sitemap.xml').read_text()
    if url not in sm:
        sm = sm.replace('</urlset>', f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{P["date"]}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n</urlset>')
        (ROOT / 'sitemap.xml').write_text(sm)
    print(f'built blog/{slug}.html ({words} words)')


if __name__ == '__main__':
    spec = runpy.run_path(sys.argv[1], init_globals={'bar_chart': bar_chart, 'timeline': timeline, 'steps': steps, 'table': table, 'figure': figure})
    build(spec['POST'])
