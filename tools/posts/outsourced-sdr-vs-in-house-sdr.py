# Spec for blog/outsourced-sdr-vs-in-house-sdr.html. Build: python3 tools/blogkit.py tools/posts/outsourced-sdr-vs-in-house-sdr.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


SAASTR = 'https://www.saastr.com/only-7-of-you-have-really-gotten-outsourced-sdrs-to-work'
BRIDGE = 'https://bridgegroupinc.com/research/sdr-tenure-and-ramp-time'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
G2 = 'https://learn.g2.com/outsourced-sales-development'

fig1 = figure(1, bar_chart('SaaStr poll: has an outsourced SDR team worked for you?', [
    ('Really worked', 7),
    ('Sort of worked', 26),
    ('All other answers', 67),
], unit='%', vmax=80, highlight=('Really worked',)),
    f'Share of more than 1,200 respondents to a SaaStr poll run by Jason Lemkin. Only 7% said outsourced SDRs had really worked; another 26% said they had sort of worked. Source: {a(SAASTR, "SaaStr, Only 7% of You Have Really Gotten Outsourced SDRs to Work")}.')

fig2 = figure(2, table(['What you care about', 'In-house SDR', 'Outsourced SDR agency', 'Hybrid model'], [
    ['<b>Time to first meetings</b>', 'Slowest. Recruiting, then a ramp of about three months.', 'Faster start, but still needs a learning period on your market.', 'Fast start; research and drafting run from day one, a person approves.'],
    ['<b>Control over messaging</b>', 'Full. You coach every call and email.', 'Indirect. Changes go through an account manager.', 'High if you can see and approve what goes out.'],
    ['<b>Product depth</b>', 'Highest once ramped.', 'Lowest. The rep splits attention across clients.', 'Depends on the brief and the manager reviewing each message.'],
    ['<b>Your management time</b>', 'High. Hiring, coaching, tooling, turnover.', 'Lower day to day, but someone must own the relationship.', 'Low to medium. One weekly review with one person.'],
    ['<b>What you learn</b>', 'Everything stays inside, including objections and buyer language.', 'Often lost unless you require call notes and reply logs.', 'Visible if every reply and meeting brief is logged where you can read it.'],
    ['<b>Flexibility</b>', 'Hard to scale down. Hiring again takes months.', 'Easy to start or stop, often with a minimum term.', 'Easy to change volume and segments.'],
]), 'How the three models compare on the questions founders and sales leaders actually ask. None of them is free of trade offs; the right one depends on your stage and how well you already know your buyer.')

fig3 = figure(3, steps('Month one of any SDR program, outsourced or not', [
    ('ICP', 'who and why now'),
    ('Meeting rule', 'what counts, in writing'),
    ('Message', 'you approve it'),
    ('Pilot', 'one segment'),
    ('Weekly review', 'replies and notes'),
], accent=('Meeting rule',)),
    'Five things to settle in the first month. The written definition of a qualified meeting (amber) is the one most programs skip, and it causes most disputes later.')

POST = {
    'slug': 'outsourced-sdr-vs-in-house-sdr',
    'title': 'Outsourced SDR vs in-house SDR: what actually works',
    'h1': 'Outsourced SDR vs in-house SDR: what <em>actually</em> works',
    'description': 'Outsourced SDR or in-house SDR? When each model works, why most outsourced programs disappoint, how a hybrid model changes the trade off and how to decide for your stage.',
    'category': 'Outbound',
    'date': '2026-11-06',
    'date_label': 'November 6, 2026',
    'hero_img': 'cover-outsourced-sdr-vs-in-house-sdr',
    'card_img': 'cover-outsourced-sdr-vs-in-house-sdr',
    'card_title': 'Outsourced SDR vs in-house SDR: what actually works',
    'card_text': 'When each model works, why most outsourced programs disappoint, and where a hybrid fits.',
    'takeaways': [
        'In-house SDRs work best when you already know your buyer and can coach the team every week. Outsourced SDRs work best for a defined, short-term job like testing a new segment.',
        'Most outsourced SDR programs disappoint: in a SaaStr poll of more than 1,200 people, only 7% said outsourced SDRs had really worked.',
        'The failures share causes you can control: no written definition of a qualified meeting, messaging the client never approved and no visibility into replies.',
        'A hybrid model, with AI agents doing research and drafting and a dedicated person approving every message, keeps most of the control of in-house with the speed of outsourcing.',
    ],
    'intro': (
        '<p>Every founder who needs pipeline hits the same fork. Hire SDRs and build the function yourself, or pay an agency to run outbound for you. Search for the answer and you find two kinds of content: agencies explaining why outsourcing wins, and operators on Reddit and SaaStr explaining why it did not work for them.</p>'
        '<p>This guide sets out what actually decides the outcome. It covers when each model works, why most outsourced programs disappoint, what in-house really asks of you, how a hybrid model changes the trade off, and a simple way to decide for your stage. We run one of the hybrid options, so we say where it fits and where it does not.</p>'
    ),
    'cta': {
        'inline_lead': 'Weighing in-house against outsourced?',
        'inline_text': 'Book a 30 minute call and we will walk through the Agent Base: AI agents do the research and drafting, and a dedicated Agent Base manager approves every email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound you can <em>see</em>, approved by a person.',
        'band_text': 'Scout finds the accounts, Lens researches them and Quill drafts the email. Your dedicated Agent Base manager approves every message before it reaches a buyer, and you watch it all on a live dashboard.',
    },
    'sections': [
        ('short-answer', 'The short answer: it depends on what you already know', (
            '<p>In-house SDRs work best when you already know who buys, why they buy and what a good first conversation sounds like, and you have someone who will coach the team every week. Outsourced SDRs work best for a defined job with an end date, such as testing a new segment or covering a region, run by a team that treats the agency as part of its own.</p>'
            '<p>The hard part is that most companies looking at outsourcing are trying to skip the first step. They have not yet found the message that works, and they hope an agency will find it for them. That is the case where outsourcing fails most often.</p>'
            '<p>Jason Lemkin made this point when he shared a ' + a(SAASTR, 'SaaStr poll on outsourced SDRs') + '. His own outsourcing successes came only after his team had already done the function well internally, and only when the outsourced people were treated as part of the core team. In his words, it is hard to outsource your core.</p>'
            '<p>So the question is less "outsourced or in-house?" and more "what do we already know, and who will own the learning?" Three situations come up again and again:</p>'
            '<ul><li><b>No proven message yet.</b> Someone close to the product needs to find it. That is usually the founder, an early in-house SDR or a hybrid setup where you approve every message.</li>'
            '<li><b>A proven message and a manager who can coach.</b> In-house scales well here, because the playbook exists and can be taught.</li>'
            '<li><b>A proven message but no time to hire, or a side bet.</b> An outsourced team or a hybrid model can run it, as long as you keep visibility.</li></ul>'
        )),
        ('why-outsourcing-disappoints', 'Why most outsourced SDR programs disappoint', (
            '<p>Most outsourced SDR programs disappoint because the agency is asked to do the part of sales development that depends most on knowing the product and the buyer. In the SaaStr poll, only 7% of more than 1,200 respondents said outsourced SDRs had really worked, and 26% said they had sort of worked.</p>'
            + fig1 +
            '<p>Polls like this are not a controlled study, and the people who answer are mostly SaaS operators. Still, the pattern matches what buyers describe in community threads. The comments under the SaaStr piece point to the same causes:</p>'
            '<ul><li><b>Product depth.</b> Commenters selling complex, high value products said customers expect real knowledge from the first conversation, and a rep who splits attention across clients rarely has it.</li>'
            '<li><b>No internal model to copy.</b> One commenter noted that companies paying to outsource have often not made the SDR model work internally first, so there is no playbook to hand over.</li>'
            '<li><b>Short commitments.</b> Lemkin wrote that two startups he knew got some results by micromanaging their agencies, and neither kept them past four to six months.</li></ul>'
            '<p>There is also a structural issue. An agency rep often works several client accounts at once, and the agency is paid on activity or meetings, not on revenue. That pushes toward volume and toward a loose definition of a meeting. Neither side is acting in bad faith; the incentives simply drift apart unless the contract and the weekly review pull them back together.</p>'
            '<p>The last cause is learning. A G2 article written by an outsourced SDR founder makes the point fairly: SDRs are part of the feedback loop, and an outside team is ' + a(G2, 'not always incentivized to pass learnings back') + '. If you cannot read the replies, you lose the most valuable output of outbound: what buyers actually say.</p>'
        )),
        ('what-in-house-asks', 'What in-house really asks of you', (
            '<p>In-house SDRs give you the most control and the deepest product knowledge, but they ask for something most early teams underestimate: a manager\'s time for hiring, coaching and replacing people. The Bridge Group\'s ' + a(BRIDGE25, '2025 SDR Metrics Report') + ' puts average ramp at 3.0 months and found that only 60% of SDRs reached quota, the lowest share in the study\'s history.</p>'
            '<p>Tenure matters as much as ramp. The Bridge Group\'s ' + a(BRIDGE, 'research on SDR tenure and ramp') + ' puts average tenure at about 1.9 years. Put those numbers together and a typical SDR spends a meaningful slice of their time with you learning the job, and then often moves on or up. That is normal for the role, but it means the program needs a system, not a star.</p>'
            '<p>What in-house needs to work:</p>'
            '<ul><li><b>A manager who coaches.</b> Someone who listens to calls, reads emails and gives one specific note at a time. Without that, a new SDR repeats the same mistakes at higher volume.</li>'
            '<li><b>A hiring process that tests the job.</b> A structured screen with a live roleplay beats a conversation about a CV. Our guide to the ' + '<a href="/blog/sdr-interview-process">20-minute SDR interview</a>' + ' lays one out.</li>'
            '<li><b>Data and tools.</b> Contact data, a sequencer, a dialer, a CRM and domains that are warmed up and monitored. Someone has to own deliverability.</li>'
            '<li><b>An onboarding plan.</b> Ramp shrinks when the first 90 days are planned week by week, with clear milestones.</li></ul>'
            '<p>What drives the cost of in-house is not just pay. It is ramp time before meetings arrive, a manager\'s hours, tools and data, and the price of a hire that does not work out. Count all of those when you compare options, even if you do not put a number on each one.</p>'
            '<p>When it works, in-house is hard to beat. The team learns your buyer in depth, every objection stays inside the company and the best SDRs become your next account executives.</p>'
        )),
        ('when-outsourcing-works', 'When outsourcing does work', (
            '<p>Outsourcing works when the job is narrow, the message is already proven and you treat the agency as an extension of your team rather than a vendor you check on monthly. The successful cases in the SaaStr thread shared those traits.</p>'
            '<p>Situations where an outside team tends to do well:</p>'
            '<ul><li><b>Testing a new segment or region.</b> You want to know whether a market responds before you hire for it. A fixed pilot with a clear question fits outsourcing well.</li>'
            '<li><b>Inbound qualification or event follow up.</b> The buyer has already raised a hand, so product depth matters less in the first touch.</li>'
            '<li><b>Simple, transactional offers.</b> When the value is easy to explain, a rep does not need months of product knowledge.</li>'
            '<li><b>Bridging a gap.</b> While you hire, an outside team keeps the pipeline from going quiet.</li></ul>'
            '<p>The common thread is ownership. The companies that make outsourcing work keep someone inside who owns the program: they approve the messaging, read the replies, attend the weekly call and adjust the target list. Lemkin described inviting outsourced staff to team meetings and making a long term commitment. That is closer to managing a remote team than to buying a service.</p>'
            '<p>If no one inside can own it, outsourcing becomes a black box. You see a meeting count each month, but you cannot tell whether the meetings were good, what the market said or why the numbers moved. Our longer explainer on ' + '<a href="/blog/sdr-as-a-service">SDR as a Service</a>' + ' covers what a provider should show you.</p>'
        )),
        ('comparison', 'Outsourced, in-house and hybrid compared', (
            '<p>The real choice in 2026 is between three models, not two: in-house SDRs, an outsourced SDR agency and a hybrid where AI agents do the research and drafting while a person approves every message. Each wins on different questions.</p>'
            + fig2 +
            '<p>A few notes on reading the table:</p>'
            '<ul><li><b>Speed is not the same as results.</b> An agency starts faster than a new hire, but if the message is wrong, faster only means you learn it sooner. That is useful if you are watching; it is wasted if you are not.</li>'
            '<li><b>Control is about visibility.</b> The question to ask any provider is simple: can I see every email before it goes out and every reply after it comes back? If the answer is no, you are buying meetings, not a program.</li>'
            '<li><b>Fully autonomous AI is a fourth option, and a risky one.</b> Tools that write and send without review promise volume, but generic emails hurt your domain and your brand. We cover that trade off in ' + '<a href="/blog/ai-sdr-vs-human-sdr">AI SDR vs human SDR</a>' + '.</li></ul>'
            '<p>The hybrid model exists because both classic options leave a gap. In-house is slow and management heavy. Outsourced is fast but opaque. Putting AI on the repetitive work and a named person on judgment aims to close both gaps, as long as the person really reviews every message and the client can see the work.</p>'
        )),
        ('hybrid', 'Where a hybrid model like the Agent Base fits', (
            '<p>A hybrid model fits teams that want outbound running now, want to stay close to the message and do not yet want to build an SDR team. At BL Agency, that model is the Agent Base: a set of AI agents with one job each, and a dedicated Agent Base manager who reads and approves every email before it reaches a buyer.</p>'
            '<p>How the work is split:</p>'
            '<ul><li><b>Scout</b> finds companies in your market that show a reason to buy right now, and the person who decides.</li>'
            '<li><b>Lens</b> researches each account so the first email says something specific to them.</li>'
            '<li><b>Quill</b> drafts the first email and the follow ups in your voice.</li>'
            '<li><b>Your dedicated Agent Base manager</b> edits or approves every draft. Nothing is sent on autopilot.</li>'
            '<li><b>Relay</b> sends approved emails at a safe pace, <b>Echo</b> sorts replies and drafts answers, and <b>Atlas</b> writes a short brief for each booked meeting.</li></ul>'
            '<p>This answers the main reasons outsourced programs disappoint. You can see the work on a live dashboard, so learning does not disappear. A named person owns quality, so the message does not drift toward volume. And the research step runs on every account, which is what makes a first email relevant.</p>'
            '<p>Where it fits less well: if your sale depends on live phone conversations from day one, or if you already have a strong SDR manager and a proven playbook, building in-house may serve you better. In that case, our <a href="/talent">talent team</a> can help you hire bilingual SDRs from Latin America instead. The honest answer is that the right model depends on your stage.</p>'
        )),
        ('how-to-decide', 'How to decide, and what to set up in month one', (
            '<p>Decide by answering three questions: do you have a proven message, do you have someone who will coach and review every week, and do you need meetings this quarter or a team for the next two years? Your answers point to a model, and the first month looks similar whichever you choose.</p>'
            '<ul><li><b>No proven message, no coach, need results soon:</b> a hybrid model where you approve the messaging, or the founder selling with support.</li>'
            '<li><b>Proven message, a coach, a long horizon:</b> in-house SDRs.</li>'
            '<li><b>Proven message, no time to hire, a defined test:</b> an outsourced pilot with full visibility, or a hybrid model.</li></ul>'
            + fig3 +
            '<p>Whatever the model, set up these five things in the first month:</p>'
            '<ol><li><b>Your ideal customer profile</b>, with the signals that make an account worth contacting now.</li>'
            '<li><b>A written definition of a qualified meeting.</b> Title, company size, the problem they must have and what must be confirmed before the meeting counts. Most disputes with agencies start here.</li>'
            '<li><b>Messaging you approve</b>, not a template you see after launch.</li>'
            '<li><b>A pilot on one segment</b>, small enough to learn from and large enough to read.</li>'
            '<li><b>A weekly review</b> of replies, objections and meeting notes, not just counts.</li></ol>'
            '<p>Give any model a fair window to show results, then judge it on meeting quality and what you learned, not on activity.</p>'
        )),
    ],
    'conclusion': (
        '<p>Outsourced and in-house SDRs both work, but under different conditions, and most failures come from choosing a model for the wrong reason.</p>'
        '<ol><li><b>Start with what you know.</b> If the message is not proven, keep someone close to the product in charge of it.</li>'
        '<li><b>Go in-house</b> when you have a proven playbook, a manager who coaches and a long horizon.</li>'
        '<li><b>Use outsourcing</b> for defined jobs, and manage the team as your own.</li>'
        '<li><b>Consider a hybrid</b> when you want speed and control without building a team yet.</li>'
        '<li><b>Write down what a qualified meeting is</b> and review replies every week, whatever you choose.</li></ol>'
        '<p>If you want to see what the hybrid option looks like on your market, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will walk through the Agent Base with you.</p>'
    ),
    'faq': [
        ('Is it better to outsource SDRs or hire in-house?',
         'It depends on what you already know. In-house works best when you have a proven message and a manager who coaches every week. Outsourcing works best for a defined job, such as testing a new segment, run by a team that treats the agency as part of its own.'),
        ('Why do outsourced SDR programs fail?',
         'The usual causes are thin product knowledge, no proven message to hand over, no written definition of a qualified meeting and no visibility into replies. In a SaaStr poll of more than 1,200 people, only 7% said outsourced SDRs had really worked.'),
        ('How long does it take an in-house SDR to ramp?',
         'The Bridge Group 2025 SDR Metrics Report puts average ramp at 3.0 months. A planned 30, 60 and 90 day onboarding with clear milestones helps a new rep reach that point.'),
        ('What should I ask an outsourced SDR agency before signing?',
         'Ask whether you approve the messaging before launch, whether you can read every reply, how they define a qualified meeting, how many clients each rep works on and what happens to your data and domains if you stop.'),
        ('What is a hybrid SDR model?',
         'A hybrid model uses AI agents for repetitive work like account research, drafting and reply sorting, and a person for judgment. In the BL Agency Agent Base, a dedicated Agent Base manager approves every email before it is sent.'),
        ('Can AI SDRs replace outsourced or in-house SDRs?',
         'Fully autonomous AI SDRs can send a lot of email, but without review they tend to produce generic messages that hurt replies and domain health. Most teams get better results when a person reviews what the AI writes.'),
        ('How do I measure an SDR program in the first months?',
         'Track qualified meetings against a written definition, meeting show rate and what the replies tell you about the market. Activity counts alone do not show whether the program is working.'),
    ],
}
