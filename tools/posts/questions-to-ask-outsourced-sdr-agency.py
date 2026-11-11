# Spec for blog/questions-to-ask-outsourced-sdr-agency.html. Build: python3 tools/blogkit.py tools/posts/questions-to-ask-outsourced-sdr-agency.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


SAASTR = 'https://www.saastr.com/only-7-of-you-have-really-gotten-outsourced-sdrs-to-work'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
GOOGLE = 'https://support.google.com/a/answer/14229414'
FTC = 'https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business'
DLC = 'https://danishleadco.io/blog/red-flags-in-outbound-sales-agency-contracts-2026-guide'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'

fig1 = figure(1, table(['#', 'Question', 'What a good answer sounds like'], [
    ['1', '<b>How do you define a qualified meeting?</b>', 'A written definition you agree on before launch: title, company fit, the problem, and what must be confirmed.'],
    ['2', '<b>What happens when a meeting no-shows or is not a fit?</b>', 'A clear rule for what counts, agreed in advance, and a log you can audit.'],
    ['3', '<b>Who will these meetings be with?</b>', 'Named target accounts and titles you approve, not "decision makers" in general.'],
    ['4', '<b>Who writes the messaging, and do I approve it?</b>', 'You see and approve the first sequence before anything is sent.'],
    ['5', '<b>Can I read every email and every reply?</b>', 'Yes, in a shared inbox, dashboard or CRM you can open at any time.'],
    ['6', '<b>How do you learn my product and my buyer?</b>', 'A structured onboarding with your calls, wins, losses and objections.'],
    ['7', '<b>Who works my account, and on how many others?</b>', 'Named people, and an honest number of clients per rep.'],
    ['8', '<b>What do you report, and how often?</b>', 'A weekly review of replies, objections and meetings, not only activity counts.'],
    ['9', '<b>Whose domains and inboxes do you send from?</b>', 'Secondary domains you own, set up and monitored for deliverability.'],
    ['10', '<b>How do you stay within sender rules and the law?</b>', 'Authentication, spam rate monitoring, opt outs honored, and a person accountable.'],
    ['11', '<b>What are the term, notice period and exit rights?</b>', 'A pilot or short first term, a reasonable notice period, no silent auto renewal.'],
    ['12', '<b>What do I keep if we stop?</b>', 'Your lists, messaging, reply history, meeting notes and domains, in writing.'],
]), 'The 12 questions in one place. Print it and bring it to every agency call. If a provider cannot answer one of them clearly, ask why before you sign.')

fig2 = figure(2, bar_chart('Gartner survey of 632 B2B buyers', [
    ('Avoid suppliers with irrelevant outreach', 73),
    ('Prefer a rep-free buying experience', 61),
], unit='%', vmax=100, highlight=('Avoid suppliers with irrelevant outreach',)),
    f'Share of B2B buyers in a Gartner survey of 632 buyers. Nearly three in four actively avoid suppliers whose outreach feels irrelevant, which is why the quality of every message an agency sends in your name matters. Source: {a(GARTNER, "Gartner, June 2025")}.')

fig3 = figure(3, steps('How to evaluate an outsourced SDR agency', [
    ('Shortlist', 'three providers'),
    ('12 questions', 'same list for all'),
    ('Sample work', 'emails for your ICP'),
    ('Pilot', 'one segment'),
    ('Review', 'quality, not volume'),
], accent=('Sample work',)),
    'A simple evaluation path. Asking each provider to write sample emails for your real buyer (amber) shows more about their quality than any sales deck.')

POST = {
    'slug': 'questions-to-ask-outsourced-sdr-agency',
    'title': '12 questions to ask an outsourced SDR agency before you sign',
    'h1': '12 questions to ask an outsourced SDR agency <em>before</em> you sign',
    'description': 'The 12 questions to ask an outsourced SDR agency before you sign: meeting definitions, message approval, visibility, domains, compliance, contract terms and what you keep if you stop.',
    'category': 'Outbound',
    'date': '2026-11-11',
    'date_label': 'November 11, 2026',
    'hero_img': 'cover-questions-to-ask-outsourced-sdr-agency',
    'card_img': 'cover-questions-to-ask-outsourced-sdr-agency',
    'card_title': '12 questions to ask an outsourced SDR agency before you sign',
    'card_text': 'Meeting definitions, message approval, domains, contract terms and what you keep if you stop.',
    'takeaways': [
        'Most disputes with outsourced SDR agencies start with a loose definition of a qualified meeting. Agree on it in writing before anything is sent.',
        'Ask to approve the messaging before launch and to read every reply after it. If you cannot see the work, you are buying a number, not a program.',
        'Deliverability and compliance stay your problem even when someone else sends: the FTC is clear that you cannot contract away responsibility under CAN-SPAM.',
        'Settle the exit before the start: term, notice period, and in writing that your domains, lists, messaging and reply history stay with you.',
    ],
    'intro': (
        '<p>Choosing an outsourced SDR agency is hard because every provider sounds the same on the first call. They all book meetings, they all have a process and they all have a case study. The differences show up later, in month two or three, when you find out what a "meeting" meant, who was writing the emails and whether you can leave.</p>'
        '<p>This guide gives you the 12 questions that bring those differences forward, grouped by what they protect: the meeting, the message, the people, your domains, and your exit. For each one we explain why it matters and what a good answer sounds like. We run an outbound service ourselves, so at the end we answer the same questions about our own model, and say where it is not the right fit.</p>'
    ),
    'cta': {
        'inline_lead': 'Comparing outbound providers?',
        'inline_text': 'Book a 30 minute call and ask us all 12 questions. We will show you the Agent Base, where AI agents research and draft and a dedicated Agent Base manager approves every email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound you can <em>see</em>, approved by a person.',
        'band_text': 'Scout finds the accounts, Lens researches them and Quill drafts the email. Your dedicated Agent Base manager approves every message before it reaches a buyer, and you watch it all on a live dashboard.',
    },
    'sections': [
        ('why-ask', 'Why the questions matter more than the pitch', (
            '<p>The questions matter because most outsourced SDR programs disappoint, and the reasons are usually visible before you sign if you ask. In a ' + a(SAASTR, 'SaaStr poll of more than 1,200 people') + ', only 7% said outsourced SDRs had really worked for them, and another 26% said they had sort of worked.</p>'
            '<p>The causes that come up in that thread and in buyer forums are consistent: a meeting definition nobody wrote down, messaging the client never approved, reps spread across too many accounts, and no way to read what buyers actually replied. None of these are hidden. They are simply not discussed on the first call, because the sales conversation is about outcomes and the problems live in the details.</p>'
            '<p>There is also more at stake than one quarter of pipeline. An agency sends email in your name to the exact people you want as customers. A ' + a(GARTNER, 'Gartner survey of 632 B2B buyers') + ' found that 73% actively avoid suppliers who send irrelevant outreach. A careless program does not just fail to book meetings; it can make your best prospects less likely to talk to you later.</p>'
            + fig1 +
            '<p>Use the table as a checklist. Ask every provider the same 12 questions, in the same order, and write down the answers. Comparing three agencies on the same list is far more useful than comparing three sales decks.</p>'
        )),
        ('the-meeting', 'Questions 1 to 3: what counts as a meeting', (
            '<p>Start with the meeting, because it is what you are paying for and it is where most disputes begin. Ask how the agency defines a qualified meeting, what happens when a meeting does not show or turns out not to be a fit, and exactly who the meetings will be with.</p>'
            '<p><b>1. How do you define a qualified meeting?</b> A good provider will want to write this down with you before launch. The definition should cover the title or role, company fit (industry, size, region), the problem the person must have, and what the SDR must confirm before booking. A ' + a(DLC, 'guide to agency contract red flags') + ' from an outbound agency makes the same point: vague definitions let unqualified meetings and no-shows count as wins.</p>'
            '<p><b>2. What happens when a meeting no-shows or is not a fit?</b> Ask for the rule before you need it. Does a no-show count? Is there a rebooking attempt? Who decides that a meeting was not a fit, and how quickly must you flag it? The specifics matter less than having them agreed in advance and logged where both sides can see them.</p>'
            '<p><b>3. Who will these meetings be with?</b> "Decision makers at mid-market companies" is not an answer. Ask to see the target account list, or at least the filters and signals used to build it, and approve the titles. If you sell to heads of operations at logistics companies, a meeting with a junior analyst at a retailer is not the same product.</p>'
            '<p>An agency confident in its quality has no reason to avoid a written definition. One that prefers to keep it loose is telling you how month three will go.</p>'
        )),
        ('the-message', 'Questions 4 to 6: who writes, who approves, who reads', (
            '<p>The next group protects your voice and your learning. Ask who writes the messaging and whether you approve it, whether you can read every email and reply, and how the team will learn your product and buyer.</p>'
            '<p><b>4. Who writes the messaging, and do I approve it?</b> You should see the first sequence, including follow ups, before anything goes out. Ask how changes are made after launch and whether you see them too. Messaging written by someone who has never spoken to your customers, and sent without your review, is the single most common complaint about outsourced programs.</p>'
            '<p><b>5. Can I read every email and every reply?</b> This is the question that separates a program from a black box. Replies are the most valuable thing outbound produces: they tell you which problems buyers recognize, which objections repeat and which segments respond. If you only receive a monthly meeting count, you lose that learning entirely. Ask for access to a shared inbox, a dashboard or your CRM, with every send and every reply visible.</p>'
            '<p><b>6. How do you learn my product and my buyer?</b> A good answer involves your material: recorded sales calls, recent wins and losses, the objections your team hears, and a session with someone who sells today. A weak answer is a questionnaire and a template. For reference, the Bridge Group\'s ' + a(BRIDGE25, '2025 SDR Metrics Report') + ' puts average in-house SDR ramp at about three months. An outside team will not know your product better in two weeks unless the onboarding is serious.</p>'
            + fig2 +
            '<p>These three questions also tell you about the agency\'s incentives. Providers paid on volume tend to resist approval steps because they slow sending down. Providers who care about meeting quality usually welcome them, because they protect the result.</p>'
        )),
        ('the-people', 'Questions 7 and 8: who does the work, and how you will know', (
            '<p>This group is about attention. Ask who will work your account and how many other clients they handle, and what the agency reports and how often.</p>'
            '<p><b>7. Who works my account, and on how many others?</b> Ask for names and roles: the SDR or SDRs, the person who manages them, and the person you call when something is wrong. Then ask how many client accounts each rep works at the same time. A rep splitting attention across many clients will rarely build the product depth a complex sale needs, a point raised repeatedly in the ' + a(SAASTR, 'SaaStr discussion') + '. There is no correct number, but there should be an honest one.</p>'
            '<p>Also ask what happens when your rep leaves. SDR turnover is normal across the industry, so a good provider will describe how knowledge is kept: written playbooks, logged replies, call notes, and a handover plan that does not restart the ramp from zero.</p>'
            '<p><b>8. What do you report, and how often?</b> Activity counts (emails sent, calls made, open rates) are easy to report and easy to inflate. Ask for a weekly review that covers:</p>'
            '<ul><li><b>Replies</b>, positive and negative, with the actual text.</li>'
            '<li><b>Objections</b> that repeat, and what the team changed in response.</li>'
            '<li><b>Meetings booked</b> against the written definition, with notes for each one.</li>'
            '<li><b>Segments</b> that respond and segments that do not.</li>'
            '<li><b>Deliverability health</b>: bounce rates, spam complaints and inbox placement.</li></ul>'
        )),
        ('domains-compliance', 'Questions 9 and 10: your domains and your legal exposure', (
            '<p>These two questions protect your brand and your email reputation, which outlast any contract. Ask whose domains and inboxes the agency sends from, and how it stays within sender rules and the law.</p>'
            '<p><b>9. Whose domains and inboxes do you send from?</b> Cold email should not go out from your main company domain, because a deliverability problem there can affect your everyday email. Most providers use secondary domains that look like yours. Ask who registers and owns those domains, who sets up authentication, who warms them up and who monitors their health. Then ask, in writing, that the domains are yours and transfer to you if you stop.</p>'
            '<p><b>10. How do you stay within sender rules and the law?</b> Google\'s ' + a(GOOGLE, 'email sender guidelines') + ' ask senders to authenticate their mail with SPF and DKIM, publish a DMARC record, and keep the user-reported spam rate below 0.1%, never reaching 0.3%. Ask how the agency tracks this and what it does when a domain starts to slip. On the legal side, the FTC\'s ' + a(FTC, 'CAN-SPAM compliance guide') + ' says the law makes no exception for business-to-business email, requires a working opt out and a valid postal address, and states that you cannot contract away your legal responsibility. Both the company being promoted and the company sending can be held liable.</p>'
            '<p>That last point is why this question belongs on your list even if it feels technical. You are not hiring someone to take the risk off your hands. You are hiring someone to manage it well while it stays yours. A provider who answers with specifics (authentication, monitoring, opt out handling, sending limits per inbox) is managing it. A provider who answers with "we have never had a problem" is not. This guide is not legal advice; when in doubt, ask your own counsel.</p>'
        )),
        ('the-exit', 'Questions 11 and 12: the contract and the exit', (
            '<p>Settle the exit before the start. Ask what the term, notice period and exit rights are, and what you keep if you stop.</p>'
            '<p><b>11. What are the term, notice period and exit rights?</b> Outbound needs time to show results, so a reasonable first term is fair. What you want to avoid is a long commitment with no checkpoints. Ask whether there is a pilot or a shorter first period, whether the contract renews automatically, how much notice you must give and whether you can leave early if agreed quality standards are not met. The ' + a(DLC, 'Danish Lead Co contract guide') + ' flags automatic renewals and long notice periods as common traps, and suggests exit rights tied to agreed measures.</p>'
            '<p><b>12. What do I keep if we stop?</b> This is the question most buyers forget. Over a few months, an outbound program builds valuable assets: researched account lists, messaging that works, reply history, meeting notes and warmed sending domains. Ask, in writing, that all of it stays with you. If the agency keeps the lists and domains, you start again from zero when you leave, and you lose most of what you paid to learn.</p>'
            '<p>Two more things to read carefully in the contract:</p>'
            '<ul><li><b>What is included.</b> Data, tools, domains, inboxes and setup work should be listed clearly, so nothing appears later as an extra.</li>'
            '<li><b>Liability language.</b> Broad disclaimers on deliverability and compliance shift all the risk to you. Ask the provider what they are willing to be accountable for.</li></ul>'
        )),
        ('how-to-decide', 'How to score the answers, and how we answer them', (
            '<p>Score each provider on how specific its answers are, not how confident they sound. A strong provider answers every question with a concrete process and offers to put it in the contract; a weak one answers with reassurance. Then ask the finalists for sample work on your real buyer before you sign.</p>'
            + fig3 +
            '<p>A simple scoring method: for each of the 12 questions, mark the answer as clear and written, clear but verbal, or vague. Anything vague on questions 1, 5, 9 or 12 is a reason to walk away, because those are the ones that decide whether you can judge quality, learn from the market and leave with your assets.</p>'
            '<p>Since we ask you to hold providers to this list, here is how our own model answers it. The Agent Base is a set of AI agents, each with one job, and a dedicated Agent Base manager who reads and approves every email:</p>'
            '<ul><li><b>Scout</b> finds accounts that match your profile and show a reason to buy now, and <b>Lens</b> researches each one. You approve the target profile and the meeting definition before launch.</li>'
            '<li><b>Quill</b> drafts the emails in your voice. Your dedicated Agent Base manager edits or approves every draft. Nothing is sent on autopilot.</li>'
            '<li><b>Relay</b> sends approved emails at a safe pace, <b>Echo</b> sorts replies and drafts answers, and <b>Atlas</b> writes a brief for each booked meeting.</li>'
            '<li>You see the work on a live dashboard: accounts, drafts, sends, replies and meetings.</li></ul>'
            '<p>Where we are not the right fit: if your sale depends on live phone calls from day one, or you already have a strong SDR manager and a proven playbook, building an in-house team may serve you better. Our ' + '<a href="/talent">talent team</a>' + ' can help you hire bilingual SDRs from Latin America instead. Whichever way you go, ask us the 12 questions too.</p>'
        )),
    ],
    'conclusion': (
        '<p>An outsourced SDR agency can work well, but only if you find out before signing how it defines success, how much you will see and what you keep. The 12 questions bring those answers forward.</p>'
        '<ol><li><b>Define the meeting in writing</b>, including no-shows and fit, before launch.</li>'
        '<li><b>Approve the messaging</b> and keep access to every email and reply.</li>'
        '<li><b>Know who works your account</b> and get a weekly review of replies and objections, not just activity.</li>'
        '<li><b>Own your domains</b> and confirm how sender rules and CAN-SPAM are handled, since the responsibility stays with you.</li>'
        '<li><b>Agree the exit</b>: a fair term, a reasonable notice period, and your lists, messaging and history in your hands.</li></ol>'
        '<p>If you want to see how the Agent Base answers these questions on your market, <a href="' + CAL + '"' + EXT + '>book a call</a> and bring the list.</p>'
    ),
    'faq': [
        ('What should I ask an outsourced SDR agency before signing?',
         'Ask how they define a qualified meeting, whether you approve the messaging, whether you can read every reply, who works your account and on how many others, whose domains they send from, how they handle sender rules and CAN-SPAM, and what you keep if you stop.'),
        ('What is the most important question to ask an SDR agency?',
         'How they define a qualified meeting. Most disputes with agencies start with a loose definition, so agree in writing on the role, company fit, problem and what must be confirmed before a meeting counts.'),
        ('Should an outsourced SDR agency send from my main domain?',
         'Usually not. Most providers send cold email from secondary domains so a deliverability problem cannot affect your everyday email. Make sure those domains are registered in your name or transfer to you if you stop.'),
        ('Am I responsible if an agency breaks email rules on my behalf?',
         'Yes. The FTC CAN-SPAM guide says you cannot contract away your legal responsibility, and both the company promoted and the company sending can be held liable. Ask how the agency handles opt outs, authentication and spam rates. This is not legal advice.'),
        ('What red flags should I watch for in an SDR agency contract?',
         'Vague meeting definitions, long terms with automatic renewal, long notice periods, unclear ownership of domains and data, extras not listed in the scope and broad disclaimers on deliverability and compliance.'),
        ('How do I test an SDR agency before committing?',
         'Ask finalists to write sample emails for your real buyer, then run a pilot on one segment with a written meeting definition and a weekly review of replies. Judge the pilot on meeting quality and what you learned, not on activity.'),
        ('How is the Agent Base different from a typical SDR agency?',
         'AI agents handle account research, drafting, sending and reply sorting, and a dedicated Agent Base manager approves every email before it goes out. You approve the meeting definition and messaging and can see all the work on a live dashboard.'),
    ],
}
