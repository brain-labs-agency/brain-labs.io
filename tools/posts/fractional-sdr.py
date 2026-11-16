# Spec for blog/fractional-sdr.html. Build: python3 tools/blogkit.py tools/posts/fractional-sdr.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


CLEVERLY = 'https://www.cleverly.co/blog/fractional-sdr'
BRIDGE = 'https://bridgegroupinc.com/research/sdr-tenure-and-ramp-time'
SAASTR = 'https://www.saastr.com/only-7-of-you-have-really-gotten-outsourced-sdrs-to-work'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
GOOGLE = 'https://support.google.com/a/answer/14229414'

fig1 = figure(1, table(['Model', 'Hours on your account', 'Who directs the work', 'Best for'], [
    ['<b>Fractional SDR</b>', 'Part of the week, shared with a few other clients', 'You, with the SDR\'s experience', 'Testing outbound, a small market, building a first playbook'],
    ['<b>Dedicated SDR</b> (employee or contractor)', 'Full working week, on your team only', 'You or your sales manager', 'A proven motion that needs steady capacity and continuity'],
    ['<b>Outsourced SDR agency</b>', 'A team shared across the agency\'s clients', 'The agency, within an agreed scope', 'Volume and infrastructure without hiring'],
    ['<b>AI agents with a human reviewer</b>', 'Agents run every day; a person approves each email', 'A dedicated reviewer, with your approval of the brief', 'Researched email outbound at a steady pace'],
]), 'Four ways to staff the top of the funnel. The real differences are how much of someone\'s week you get, who directs the work and what stays when the engagement ends.')

fig2 = figure(2, timeline('A 12 week fractional SDR test', [
    (0, 2, 'Setup', 'brief, list, domains'),
    (2, 6, 'First sequences', 'two segments'),
    (6, 10, 'Iterate', 'replies drive changes'),
    (10, 12, 'Decide', 'stop, keep, or hire'),
], 12, unit='wk', accent=('Decide',)),
    'A suggested shape for a fractional SDR test. Agree the decision point (amber) before you start, so the engagement ends with a clear call: stop, keep it fractional, or hire a dedicated rep.')

fig3 = figure(3, steps('From fractional SDR to a dedicated hire', [
    ('Test', 'fractional SDR'),
    ('Write it down', 'playbook'),
    ('Hire', 'dedicated SDR'),
    ('Hand over', 'overlap weeks'),
    ('Scale', 'more reps'),
], accent=('Write it down',)),
    'The handover most teams skip is the written playbook (amber). Without it, what the fractional SDR learned leaves with them.')

POST = {
    'slug': 'fractional-sdr',
    'title': 'Fractional SDR: what it is and when it makes sense',
    'h1': 'Fractional SDR: what it is and when it makes <em>sense</em>',
    'description': 'What a fractional SDR is, how it differs from a dedicated SDR or an agency, when a part-time shared rep makes sense, when it does not, and how to move from fractional to a dedicated hire.',
    'category': 'Hiring',
    'date': '2026-11-16',
    'date_label': 'November 16, 2026',
    'hero_img': 'cover-fractional-sdr',
    'card_img': 'cover-fractional-sdr',
    'card_title': 'Fractional SDR: what it is and when it makes sense',
    'card_text': 'A part-time, shared SDR can test outbound fast. Here is when it fits and when you need a dedicated rep.',
    'takeaways': [
        'A fractional SDR is an experienced sales development rep who works part of the week on your account and the rest for a few other clients.',
        'It fits best as a test: proving outbound works for your offer, freeing a founder from daily prospecting, or working a small market slowly and carefully.',
        'It fits poorly when you need steady volume, several channels at once, or continuity, because hours cap output and the knowledge leaves with the contractor.',
        'Treat it as a bridge. Set a decision point, ask for a written playbook, and plan the handover to a dedicated rep if the test works.',
    ],
    'intro': (
        '<p>"Fractional" started with executives: a part-time CFO or head of marketing for companies not ready for a full-time one. The same idea has reached sales development. Founders who are not ready to hire an SDR, or who tried and were burned, now see offers for a fractional SDR: an experienced rep who gives you part of their week.</p>'
        '<p>It can be a smart first step. It can also be a slow, blurry one that leaves you unsure whether outbound works at all. This guide explains what a fractional SDR is, how it compares with a dedicated rep, an agency and AI agents, when it makes sense, when it does not, and how to run one so you learn something either way. We place dedicated bilingual SDRs from Latin America, so we also cover when to graduate from fractional to a full-time rep.</p>'
    ),
    'cta': {
        'inline_lead': 'Ready for a dedicated rep?',
        'inline_text': 'Tell us the role and the US hours you need covered. We send three interviewed, bilingual SDR profiles from Latin America within 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'A dedicated SDR who works <em>your</em> hours.',
        'band_text': 'Vetted bilingual sales professionals from Latin America, interviewed in English and roleplayed on a cold call before you meet them. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('what-is-a-fractional-sdr', 'What a fractional SDR is', (
            '<p>A fractional SDR is an experienced sales development rep who works part-time on your outbound and splits the rest of the week across a small number of other clients.</p>'
            '<p>One provider\'s ' + a(CLEVERLY, 'guide to fractional SDRs') + ' describes the usual arrangement as about 10 to 25 hours a week, split across two to five clients. At that level the realistic scope is focused outreach on one or two channels, same-day reply handling and booking meetings. Building lists from scratch, setting up domains and inboxes, or owning the whole outbound strategy usually fall outside it.</p>'
            '<p>It helps to compare the fractional model with the other ways to staff the top of your funnel:</p>'
            + fig1 +
            '<p>Three things set the fractional SDR apart:</p>'
            '<ul><li><b>Experience over hours.</b> You usually get someone who has done the job before, often for several companies, rather than a junior rep you need to train.</li>'
            '<li><b>Shared attention.</b> Your account is one of a few. That is the trade for the lower commitment.</li>'
            '<li><b>You still direct the work.</b> Unlike an agency, which runs a program within a scope, a fractional SDR usually expects you to supply the target profile, the offer and someone to take the meetings.</li></ul>'
            '<p>The title is also used loosely. Some agencies call a shared rep "fractional"; some freelancers use it for any part-time work. Before comparing offers, ask how many hours you actually get, how many other clients the person works for and what is in scope.</p>'
        )),
        ('when-it-makes-sense', 'When a fractional SDR makes sense', (
            '<p>A fractional SDR makes sense when your main question is "does outbound work for us?" rather than "how do we do more of it?" It fits teams that want to test an offer, free a founder from daily prospecting, work a small market carefully, or write down a first playbook before committing to a hire.</p>'
            '<p><b>You are testing outbound before adding headcount.</b> If you have never run outbound, you do not know yet which segment answers, which message lands or whether meetings turn into deals. A fractional SDR lets you find out with an experienced hand and a short commitment, instead of hiring a full-time rep into an unproven motion.</p>'
            '<p><b>The founder is out of time.</b> Founder-led outbound often works until it does not, because the founder is also closing, hiring and building. A fractional SDR can take daily prospecting and reply handling while the founder stays on the sales calls.</p>'
            '<p><b>Your market is small.</b> If there are only a few hundred companies that could buy from you, you do not need high volume. You need careful, well-researched outreach at a slower pace, which suits part-time hours.</p>'
            '<p><b>Your gap is know-how, not capacity.</b> If you have someone who could do outreach but nobody who knows how to target and write it, an experienced fractional SDR can set up the approach and coach your team on it.</p>'
            '<p><b>You want a playbook for your first hire.</b> A good fractional engagement ends with a written record of who you targeted, what you said, what buyers replied and what you would change. That document makes your first dedicated SDR far easier to onboard.</p>'
        )),
        ('when-it-does-not', 'When a fractional SDR does not make sense', (
            '<p>A fractional SDR is the wrong choice when you need steady meeting volume, several channels at once, long-term continuity, or when nobody on your side has time to direct the work. In those cases the part-time hours and shared attention become the bottleneck, however skilled the person is.</p>'
            '<ul><li><b>Your motion is proven and you need capacity.</b> If you already know who buys and what to say, the constraint is hours. Part-time hours cap output no matter how good the rep is.</li>'
            '<li><b>You need several channels.</b> Running email, phone and LinkedIn properly takes daily time on each. Sustained multichannel work is rarely realistic inside a part-time week.</li>'
            '<li><b>You need someone on your hours.</b> If buyers answer the phone between 9 and 11 in the morning in your time zone, you need a rep who is available then, every day, not on the days your account is scheduled.</li>'
            '<li><b>You have no infrastructure.</b> Domains, inboxes, data and a CRM need setting up and monitoring. Google\'s ' + a(GOOGLE, 'sender guidelines') + ' expect authenticated mail and a low spam complaint rate, and someone has to watch that. If you expect the fractional SDR to build all of it, most of their hours go to setup instead of selling.</li>'
            '<li><b>Nobody can direct the work.</b> A fractional SDR still needs a brief, feedback on messaging and someone to take the meetings. If nobody on your team has time for that, the engagement drifts.</li>'
            '<li><b>You need continuity.</b> Over a year, a dedicated rep builds deep product knowledge and relationships with accounts. A contractor who works for several clients, and may move on, keeps less of that.</li></ul>'
            '<p>If several of these apply, look at a dedicated SDR, an agency or an agent-based program instead.</p>'
        )),
        ('hidden-tradeoffs', 'The trade-offs nobody mentions on the first call', (
            '<p>The biggest trade-offs of a fractional SDR are slower learning in calendar time, divided attention, knowledge that leaves with the contractor, and blurry accountability when results are weak. None of them are reasons to avoid the model, but each one should shape how you set it up.</p>'
            '<p><b>Learning takes longer in calendar time.</b> The Bridge Group\'s ' + a(BRIDGE, 'research on SDR ramp') + ' puts average ramp for a full-time SDR at about three months. An experienced fractional SDR starts faster than a new hire, but they still need to learn your product, your buyer and your objections, and they do it in fewer hours per week. Expect the learning curve to stretch across more weeks than the hours alone suggest.</p>'
            '<p><b>Attention is shared.</b> Your account competes with others for the same person\'s focus. Ask how many clients they work with and how their week is split. The same concern comes up often in buyer discussions about outsourced SDRs, such as the ' + a(SAASTR, 'SaaStr thread') + ' where only 7% of respondents said outsourced SDRs had really worked for them.</p>'
            '<p><b>Knowledge walks out.</b> What the fractional SDR learns about which segments answer and which messages fail lives in their head unless you make them write it down. When the engagement ends, it goes with them.</p>'
            '<p><b>Accountability is blurry.</b> If meetings are slow, is the problem your offer, your data, your message or the rep\'s limited time? With a part-time, shared rep it is harder to tell. A clear brief and a weekly review of actual replies make it easier.</p>'
            '<p><b>Your brand is still on every email.</b> A ' + a(GARTNER, 'Gartner survey of 632 B2B buyers') + ' found that 73% actively avoid suppliers who send irrelevant outreach. A rushed part-time rep writing generic messages can do more harm than no outreach at all, so approve the messaging before it goes out.</p>'
        )),
        ('how-to-run-it', 'How to run a fractional SDR engagement', (
            '<p>Run a fractional SDR engagement as a time-boxed test with a written brief, a clear meeting definition, a weekly review of real replies and a decision date agreed at the start. The goal is to end with an answer, not just a few meetings.</p>'
            + fig2 +
            '<p>Before the first email:</p>'
            '<ul><li><b>Write the brief.</b> Target companies and titles, the problem you solve, the proof you can share and the words you never use.</li>'
            '<li><b>Define a qualified meeting.</b> Role, company fit, the problem the buyer must have and what must be confirmed before booking. Most disputes about outbound are really disputes about this definition.</li>'
            '<li><b>Settle the infrastructure.</b> Decide who owns and sets up the sending domains, inboxes, data and CRM. Get it in writing that domains, lists and reply history are yours.</li>'
            '<li><b>Agree the hours and the split.</b> How many hours a week, on which days and in which time zone, and how many other clients the person carries.</li></ul>'
            '<p>While it runs:</p>'
            '<ul><li><b>Approve the first sequences.</b> Read every email in the first sequence before it is sent.</li>'
            '<li><b>Review replies weekly.</b> Look at what buyers actually wrote, positive and negative. Replies tell you more about your market than activity counts.</li>'
            '<li><b>Change one thing at a time.</b> With limited hours, testing many changes at once makes it impossible to see what worked.</li>'
            '<li><b>Keep a shared log.</b> Segments tried, messages sent, objections heard and meetings booked, in a document or CRM you own.</li></ul>'
            '<p>At the decision point, choose one of three outcomes: stop because outbound does not fit your offer, keep the fractional SDR because a slow pace suits your market, or hire a dedicated rep because the test worked and hours are now the limit.</p>'
        )),
        ('fractional-to-dedicated', 'When to move from fractional to a dedicated SDR', (
            '<p>Move to a dedicated SDR when the test has shown which segment and message work and the only thing holding back more meetings is the number of hours. Other signs are that you need daily coverage on your time zone, more than one channel, or someone who will still be there in a year.</p>'
            + fig3 +
            '<p>Signs you have outgrown the fractional model:</p>'
            '<ul><li><b>Good replies arrive faster than they can be worked.</b> Positive replies wait a day or two because the rep is on another client.</li>'
            '<li><b>You want to add phone or LinkedIn.</b> A second channel needs daily time that a part-time week cannot cover.</li>'
            '<li><b>The playbook is stable.</b> You are no longer changing the target or the message every week. You need execution.</li>'
            '<li><b>You want the knowledge to stay.</b> Product depth and account relationships are worth more when they belong to someone on your team.</li></ul>'
            '<p>Make the handover deliberate. Ask the fractional SDR to write the playbook before the engagement ends: segments, messages, objections, the meeting definition and what did not work. If possible, overlap the two for a few weeks so the new rep can see how replies are handled. The Bridge Group data puts average SDR tenure at about 1.9 years, so a written playbook also protects you the next time the seat changes.</p>'
            '<p>When you hire, look for the qualities that made the test work: clear written English, comfort on the phone with US buyers, curiosity about the customer\'s business and the discipline to follow up. Our guide to <a href="/blog/sdr-interview-process">the 20 minute SDR screen</a> covers how to test for them.</p>'
        )),
        ('how-we-help', 'How BL Agency fits in', (
            '<p>We help at the two points around a fractional test: placing a dedicated bilingual SDR from Latin America once you are ready for one, and running email outbound with AI agents and a person approving every message if you want a program without hiring.</p>'
            '<p><b>A dedicated SDR on your hours.</b> Our <a href="/talent">talent team</a> places vetted bilingual sales professionals from Latin America with US companies. Latin America sits inside the US business day, so your rep works your hours, not a night shift. Every candidate is interviewed in English by our sales team and roleplayed on a live cold call before you meet them. You get three profiles within 72 hours, you interview them yourself, and if the rep does not work out in the first 30 days we replace them.</p>'
            '<p><b>An agent-based program.</b> If you want outbound without hiring yet, the Agent Base uses AI agents for research and drafting, and a dedicated Agent Base manager approves every email before it is sent. It is built for steady, researched email outreach, and you can see all the work on a live dashboard.</p>'
            '<p>Where neither fits: if you are still unsure whether outbound suits your offer at all and want an experienced person to test it for a few weeks, a well-scoped fractional SDR can be the right first step. Use the brief, meeting definition and decision point above, and come back to us when the test shows you need a dedicated rep.</p>'
        )),
    ],
    'conclusion': (
        '<p>A fractional SDR is a practical way to test outbound with an experienced rep and a short commitment. It is not built for volume or continuity, so treat it as a bridge, not a destination.</p>'
        '<ol><li><b>Know what you are buying:</b> part of an experienced rep\'s week, shared with a few other clients, usually on one or two channels.</li>'
        '<li><b>Use it to learn:</b> testing an offer, freeing a founder, working a small market or writing a first playbook.</li>'
        '<li><b>Avoid it when hours are the limit:</b> steady volume, several channels, daily coverage or long-term continuity need a dedicated rep.</li>'
        '<li><b>Run it as a test:</b> a written brief, a meeting definition, weekly reply reviews and a decision date.</li>'
        '<li><b>Plan the handover:</b> a written playbook and, if possible, a few weeks of overlap with your first dedicated SDR.</li></ol>'
        '<p>When you are ready for a rep who works your hours, <a href="/talent">request profiles</a> and we will send three interviewed, bilingual SDRs within 72 hours.</p>'
    ),
    'faq': [
        ('What is a fractional SDR?',
         'A fractional SDR is an experienced sales development rep who works part-time on your outbound and splits the rest of the week across a few other clients. They prospect, write to buyers, handle replies and book meetings, usually on one or two channels.'),
        ('How many hours does a fractional SDR work?',
         'It varies by provider. A common arrangement is roughly 10 to 25 hours a week, split across two to five clients. Ask exactly how many hours you get, on which days, and how many other clients the person works with.'),
        ('Is a fractional SDR the same as an outsourced SDR agency?',
         'Not quite. A fractional SDR is usually one experienced person you direct, while an agency runs a program with its own team, tools and infrastructure within an agreed scope. Both share attention across clients.'),
        ('When should I hire a fractional SDR?',
         'When you want to test whether outbound works for your offer, free a founder from daily prospecting, work a small market carefully or build a first playbook before committing to a full-time hire.'),
        ('When should I hire a full-time SDR instead?',
         'When your target and message are proven and the limit is hours, when you need daily coverage on your time zone or more than one channel, or when you want product knowledge and account relationships to stay on your team.'),
        ('What should I ask a fractional SDR before hiring them?',
         'Ask how many hours you get, how many other clients they work with, what is in scope, who sets up and owns domains, inboxes and data, how they define a qualified meeting and whether they will write a playbook you keep.'),
        ('How long should a fractional SDR test run?',
         'Long enough to get real replies from at least two segments and see whether meetings turn into opportunities. A practical length is about 12 weeks, ending with a decision: stop, keep the fractional SDR, or hire a dedicated rep. Agree the date before you start.'),
    ],
}
