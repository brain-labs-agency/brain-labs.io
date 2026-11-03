"""Build a Lens pipeline preview page at p/<slug>/index.html.

Usage: python3 tools/preview.py tools/previews/<name>.py
The spec file defines P = {...} (see tools/previews/*.py for examples).
Reuses the head and CSS of the Kantiv preview so every page looks the same.
"""
import html, re, sys, os, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'p', 'kantiv-458671', 'index.html')
E = html.escape


def build(P):
    t = open(TEMPLATE, encoding='utf-8').read()
    head = t[:t.index('<body')]
    head = re.sub(r'<title>.*?</title>', f'<title>{E(P["company"])} · Pipeline Preview by BL Agency</title>', head)
    a = P['accounts']
    stats = ''.join(f'<div class="stat"><div class="v">{E(v)}</div><div class="l">{E(l)}</div></div>' for v, l in P['stats'])
    accts = []
    for i, x in enumerate(a, 1):
        badge = '<span class="ok">Verified</span>' if x.get('verified', True) else '<span class="tbc">Confirm before outreach</span>'
        src = f'<a href="{E(x["signal_url"])}" target="_blank" rel="noopener">Signal source</a>'
        if x.get('contact_url'):
            src += f'<a href="{E(x["contact_url"])}" target="_blank" rel="noopener">Contact source</a>'
        accts.append(f'''<article class="acct"><div class="n">{i:02d}</div><div class="body">
<h3>{E(x["company"])}</h3><p class="sig">{E(x["signal"])}</p><p class="why">{E(x["why"])}</p>
<div class="who"><div><strong>{E(x["contact"])}</strong><span>{E(x["title"])}</span></div>{badge}</div>
<div class="src">{src}</div></div></article>''')
    em = P['sample_email']
    body = f'''<body>
<div class="wrap">
<div class="eyebrow">Pipeline preview · prepared for {E(P["company"])}</div>
<h1>{E(P["h1"])}</h1>
<p class="lede">{E(P["lede"])}</p>
<div class="meta"><span>Prepared by <b>BL Agency</b></span><span>Research date <b>{E(P["date_label"])}</b></span><span>Sources linked on every account</span></div>
<div class="stats">{stats}</div>
<section><h2>Who we looked for</h2><div class="grid2">
<div class="box"><h4>Your buyer</h4><p>{E(P["buyer"])}</p></div>
<div class="box"><h4>Signals that mean "now"</h4><p>{P["signals_html"]}</p></div>
</div></section>
<section><h2>The accounts</h2>
{"".join(accts)}
</section>
<section><h2>Sample first email</h2><div class="email">
<div class="hd"><b>To:</b> {E(em["to"])} &nbsp;·&nbsp; <b>Subject:</b> {E(em["subject"])}</div>
<pre>{E(em["body"])}</pre></div>
<p class="note">Every email is written for one person and one signal, then reviewed by a person before it is sent.</p></section>
<section><h2>How this was put together</h2><div class="flow">
<div class="step"><div class="t">Agent</div><h4>Research</h4><p>Reads your site, defines the ICP and scans news, deals and job boards for signals.</p></div>
<div class="step"><div class="t">Agent</div><h4>Contacts</h4><p>Finds the person who owns the problem and links the source.</p></div>
<div class="step"><div class="t">Agent</div><h4>Drafting</h4><p>Writes a first email tied to that account's signal.</p></div>
<div class="step human"><div class="t">Your dedicated Agent Base manager</div><h4>Review</h4><p>Checks every account and email, handles replies and books meetings.</p></div>
</div><p class="note">For clients this runs every week, and you can watch each agent's work live on a shared dashboard.</p></section>
<div class="cta"><h3>Want this running for {E(P["company"])}?</h3><p>{E(P["cta_text"])}</p>
<a class="btn" href="https://cal.com/vero-grados-bl-agency/bl-meetings" target="_blank" rel="noopener">Book 15 minutes with Vero</a>
<span class="url">cal.com/vero-grados-bl-agency/bl-meetings</span></div>
<footer><a href="https://www.brain-labs.io" style="color:inherit">BL Agency (Brain Labs)</a> · Prepared from public sources on {E(P["date_label"])}. Signals can change, so we recheck before outreach.</footer>
</div>
</body>
</html>
'''
    out = head + body
    assert '—' not in out, 'em dash found'
    d = os.path.join(ROOT, 'p', P['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
    return d


if __name__ == '__main__':
    ns = {}
    exec(open(sys.argv[1], encoding='utf-8').read(), ns)
    print(build(ns['P']))
