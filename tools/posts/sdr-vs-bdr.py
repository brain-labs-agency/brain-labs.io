# Spec for blog/sdr-vs-bdr.html. Build: python3 tools/blogkit.py tools/posts/sdr-vs-bdr.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


ZOOMINFO = 'https://pipeline.zoominfo.com/sales/sdr-vs-bdr-difference'
BRAVADO = 'https://bravado.co/blog/sdr-vs-bdr/'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
BRIDGE_RAMP = 'https://bridgegroupinc.com/research/sdr-tenure-and-ramp-time'
GONG = 'https://www.gong.io/resources/labs/the-hidden-power-of-cold-calling-insights-from-300m-calls/'

fig1 = figure(1, table(['', 'SDR (sales development representative)', 'BDR (business development representative)'], [
    ['<b>Usual focus</b>', 'Inbound: people who already raised a hand', 'Outbound: people who have not engaged yet'],
    ['<b>Where leads come from</b>', 'Demo requests, sign ups, downloads, webinar attendees', 'Target account lists, buying signals, research'],
    ['<b>Main job</b>', 'Respond fast, qualify, book the right ones', 'Find the right person, start a conversation, book a meeting'],
    ['<b>Main channels</b>', 'Email and phone follow up on a form fill', 'Cold call, cold email and LinkedIn'],
    ['<b>Often reports to</b>', 'Marketing or sales', 'Sales'],
    ['<b>Measured on</b>', 'Speed to lead, qualified meetings, conversion', 'Meetings held, opportunities created'],
    ['<b>Key trait</b>', 'Organized, quick, good at qualifying', 'Resilient, curious, comfortable with rejection'],
]), 'The most common way companies split the two titles. Many teams use them the other way round, or use one title for both, so read the job, not the label. Definitions follow ' + a(ZOOMINFO, 'ZoomInfo') + ' and ' + a(BRAVADO, 'Bravado') + '.')

fig2 = figure(2, steps('Which one do you need?', [
    ('Count inbound', 'leads per week'),
    ('Check response', 'how fast, by whom'),
    ('Size the market', 'accounts worth calling'),
    ('Pick the motion', 'in, out or both'),
    ('Write the job', 'motion first'),
], accent=('Pick the motion',)),
    'A five-step way to decide. The answer comes from your lead flow and your market, not from the title (amber step).')

fig3 = figure(3, timeline('A new rep\'s first three months', [
    (0, 1, 'Learn', 'product, buyer, tools'),
    (1, 2, 'First meetings', 'partial target'),
    (2, 3, 'Near full pace', 'most of target'),
    (3, 4, 'Full target', 'judge on results'),
], 4, unit='mo', accent=('Full target',)),
    'Average SDR ramp time is about 3.0 months, the lowest since 2010, according to ' + a(BRIDGE_RAMP, 'The Bridge Group') + '. Outbound reps often need the longer end of that range, because they must learn the market as well as the product.')

POST = {
    'slug': 'sdr-vs-bdr',
    'title': 'SDR vs BDR: the difference and which one you need',
    'h1': 'SDR vs BDR: the difference and which one you <em>need</em>',
    'description': 'The difference between an SDR and a BDR, why companies use the titles differently, what each role does day to day, how to decide which one to hire and what to test for in each.',
    'category': 'Hiring',
    'date': '2026-11-18',
    'date_label': 'November 18, 2026',
    'hero_img': 'cover-sdr-vs-bdr',
    'card_img': 'cover-sdr-vs-bdr',
    'card_title': 'SDR vs BDR: the difference and which one you need',
    'card_text': 'SDRs usually work inbound leads and BDRs usually go outbound. Hire for the motion, not the title.',
    'takeaways': [
        'In most companies an SDR works inbound leads (people who already showed interest) and a BDR works outbound (people who have not engaged yet). Both book meetings for account executives.',
        'The titles are not standard. Some companies flip them, and many use "SDR" for both, so always read the job description, not the label.',
        'Decide by your lead flow: if inbound leads wait too long for a reply, start with an inbound SDR; if inbound is thin and your market is defined, start with an outbound BDR.',
        'The two jobs need different strengths. Test inbound reps on speed and qualification, and outbound reps on a live cold call and a researched first email.',
    ],
    'intro': (
        '<p>SDR and BDR are two of the most confusing titles in sales. Both are entry-level roles that book meetings for account executives, both are measured on pipeline, and many companies use the words as if they meant the same thing. Then a founder posts a "BDR" job, gets candidates who expect to answer demo requests, and realizes the label did not say what the job was.</p>'
        '<p>This guide explains the usual difference between the two roles, why companies disagree on it, what each one does day to day, and how to decide which one your team needs first. We place bilingual sales professionals from Latin America with US companies, so we also cover what to test for in each role before you hire.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring an SDR or a BDR?',
        'inline_text': 'Tell us the motion (inbound, outbound or both) and the US hours you need covered. We send three interviewed, bilingual profiles from Latin America within 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'The right rep for <em>your</em> motion, on your hours.',
        'band_text': 'Vetted bilingual sales professionals from Latin America, interviewed in English and roleplayed on a cold call before you meet them. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('difference', 'The short answer: inbound vs outbound', (
            '<p>In most companies, an SDR (sales development representative) qualifies inbound leads, and a BDR (business development representative) prospects outbound. The SDR answers people who already raised a hand; the BDR starts conversations with people who have not.</p>'
            '<p>That is the most common convention, not a rule. ' + a(ZOOMINFO, 'ZoomInfo compared eight well-known sources') + ' and found that six of them define SDR as inbound and BDR as outbound, while two define them the other way round. Its summary is a useful one-liner: SDRs qualify inbound demand, BDRs create outbound pipeline.</p>'
            + fig1 +
            '<p>What the two roles share matters as much as what separates them:</p>'
            '<ul><li><b>Both sit at the top of the funnel.</b> Neither usually closes deals. They hand qualified meetings to an account executive.</li>'
            '<li><b>Both are measured on meetings and pipeline,</b> not revenue.</li>'
            '<li><b>Both are usually entry-level</b> and a common path into an account executive role.</li>'
            '<li><b>Both need clear spoken and written English</b> if your buyers are in the US.</li></ul>'
            '<p>So the useful question is not "SDR or BDR?" but "who is this person going to talk to, and did those people ask to hear from us?"</p>'
        )),
        ('titles', 'Why companies use the titles differently', (
            '<p>Companies use the titles differently because there is no industry standard, and because small teams rarely split the work. ' + a(BRAVADO, 'Bravado notes') + ' that on smaller and startup sales teams the two roles often work as one, and that the terms are often used interchangeably.</p>'
            '<p>You will see a few patterns in job posts:</p>'
            '<ul><li><b>The common split:</b> SDR for inbound, BDR for outbound.</li>'
            '<li><b>The flipped split:</b> BDR for inbound or partner leads, SDR for outbound. Some companies use BDR for anything labeled "business development", including partnerships.</li>'
            '<li><b>One title for both:</b> "SDR" with "inbound" or "outbound" in front of it. This is now very common, and The Bridge Group\'s ' + a(BRIDGE, '2025 SDR research') + ' uses "SDR" as the umbrella term for the whole function.</li>'
            '<li><b>Seniority labels:</b> a few companies use BDR for a more senior or enterprise-focused version of the role. There is no wide agreement on this.</li></ul>'
            '<p>This matters for hiring in two ways. First, candidates read titles through their last job. Someone who was a "BDR" answering demo requests may never have made a cold call. Second, if your post says one thing and the job is another, the best candidates for the real job may never apply.</p>'
            '<p>The fix is simple: put the motion in the first line of the job description. "You will spend most of your day calling and emailing operations leaders at logistics companies who have not heard of us" tells a candidate more than either title.</p>'
        )),
        ('sdr-day', 'What an inbound SDR does all day', (
            '<p>An inbound SDR responds to people who already showed interest, works out which of them are a real fit, and books the good ones with an account executive. Speed and judgment matter more than persistence.</p>'
            '<p>A typical day includes:</p>'
            '<ul><li><b>Answering new leads fast.</b> Demo requests, trial sign ups and contact forms. The longer a lead waits, the more likely it has moved on to a competitor.</li>'
            '<li><b>Qualifying.</b> Short calls or emails to confirm fit, need and timing. Not every hand raised is a buyer: students, competitors and people researching for later all fill in forms.</li>'
            '<li><b>Booking and handing over.</b> Scheduling the meeting, writing notes for the account executive and making sure the right people attend.</li>'
            '<li><b>Following up on warm leads that are not ready.</b> Webinar attendees and content downloads often need a few touches before a conversation.</li>'
            '<li><b>Feeding marketing.</b> Telling marketing which sources bring real buyers and which bring noise.</li></ul>'
            '<p>Because inbound SDRs work leads that marketing creates, they often sit close to the marketing team, and in some companies report to it. They are usually measured on response time, the share of leads contacted, qualified meetings held and how many of those become opportunities.</p>'
            '<p><b>Who does well:</b> organized people who can switch quickly between many conversations, ask direct qualifying questions without sounding like a form, and say no to a lead politely. A great inbound SDR protects the account executive\'s calendar as much as they fill it.</p>'
        )),
        ('bdr-day', 'What an outbound BDR does all day', (
            '<p>An outbound BDR finds the right people at target accounts, researches them, and starts conversations through cold calls, emails and LinkedIn. Most of the job is earning attention from people who did not ask for it.</p>'
            '<p>A typical day includes:</p>'
            '<ul><li><b>Research.</b> Picking accounts, finding the person who owns the problem and looking for a reason to reach out now, such as a new leader or a hiring push.</li>'
            '<li><b>Cold calling.</b> Blocks of dials to verified numbers, with objection handling and a clear ask.</li>'
            '<li><b>Writing.</b> First emails and follow ups that say something specific about the buyer, not a template with a merge field.</li>'
            '<li><b>LinkedIn.</b> Connecting, commenting and messaging where the buyer is active.</li>'
            '<li><b>Booking and handing over.</b> Same as an SDR: confirm the meeting and brief the account executive.</li></ul>'
            '<p>The phone is still a big part of good outbound. In Gong\'s analysis of more than ' + a(GONG, '300 million cold calls') + ', top-quartile reps reached a live person on 13.3% of dials, against 5.4% for the average rep, and booked meetings from far more of those conversations. The gap between an average and a strong outbound rep is large, which is why hiring for this role deserves a real test.</p>'
            '<p><b>Who does well:</b> curious, resilient people who are comfortable hearing no many times a day, can open a call with something relevant in the first ten seconds, and keep following up without being annoying. Outbound BDRs also need to understand the market well enough to know who to call before they know what to say.</p>'
        )),
        ('which-one', 'Which one does your team need first?', (
            '<p>Hire an inbound SDR first if leads already come in and wait too long for a reply, or if account executives spend hours qualifying people who will never buy. Hire an outbound BDR first if inbound is thin, your ideal customer is clear, and you need pipeline you can control.</p>'
            + fig2 +
            '<p>Questions that settle it:</p>'
            '<ul><li><b>How many inbound leads come in each week, and who answers them?</b> If the answer is "the founder, when they get to it", an inbound SDR will pay off quickly.</li>'
            '<li><b>How fast are they answered?</b> If good leads wait a day or more, you are losing some of them.</li>'
            '<li><b>Can you name the accounts you want?</b> Outbound needs a defined market. If you cannot describe your best customer in a sentence, fix that before hiring a BDR.</li>'
            '<li><b>Does the offer already sell?</b> Outbound scales an offer that works. It rarely finds product-market fit on its own.</li>'
            '<li><b>Who will coach the rep?</b> A first outbound hire needs someone who has done outbound to review calls and emails in the first months.</li></ul>'
            '<p>Many early teams need both but can afford one. In that case, hire for the main motion and give the rep a clear split, for example inbound first every morning and outbound in the afternoon, so neither gets dropped. If you are still deciding whether your first sales hire should book meetings or close them, see <a href="/blog/hire-sdr-or-ae-first">should you hire an SDR or an AE first</a>.</p>'
        )),
        ('hiring', 'How to hire for each role', (
            '<p>Hire an inbound SDR for speed, organization and qualification judgment, and an outbound BDR for phone skill, writing and resilience. Test each one on the work they will actually do, not on general confidence in an interview.</p>'
            '<p><b>For an inbound SDR, test:</b></p>'
            '<ul><li><b>A qualification roleplay.</b> Play a lead who filled in a demo form but is not a fit. See whether they find out quickly and close the call politely.</li>'
            '<li><b>A written reply.</b> Give them a real form submission and ask for the first email back. Look for speed, clarity and a specific question.</li>'
            '<li><b>Prioritization.</b> Show five new leads and ask which to call first, and why.</li></ul>'
            '<p><b>For an outbound BDR, test:</b></p>'
            '<ul><li><b>A live cold call roleplay</b> with a real objection. Five minutes tells you more than the CV.</li>'
            '<li><b>A researched first email</b> to one of your target accounts. Look for a reason to write that is about the buyer.</li>'
            '<li><b>Account selection.</b> Give them a short list and ask who they would call and what they would say first.</li></ul>'
            '<p>Then plan the ramp. Average SDR ramp time is about three months, according to The Bridge Group, and average tenure has risen to about 1.9 years.</p>'
            + fig3 +
            '<p>Our guides to <a href="/blog/sdr-interview-process">the 20 minute SDR screen</a> and the <a href="/blog/sdr-onboarding-plan">SDR onboarding plan</a> cover both steps in detail.</p>'
        )),
        ('latam', 'Hiring SDRs and BDRs from Latin America', (
            '<p>Both roles work well from Latin America for US companies, because reps there work inside the US business day and can call buyers when they answer. What changes is what to test: inbound reps need fast, clear written English, and outbound reps need confident spoken English on a cold call.</p>'
            '<p>A few things to get right:</p>'
            '<ul><li><b>Hours.</b> Latin America sits within a few hours of US time zones, so a rep works your hours, not a night shift. That matters most for outbound, where calls go out when buyers are at their desks.</li>'
            '<li><b>English for the motion.</b> An inbound rep writes and answers all day; an outbound rep opens calls with strangers. Test the skill the job uses most. Our guide to building a <a href="/blog/native-english-sales-team-latin-america">native-level English sales team</a> explains how.</li>'
            '<li><b>Bilingual reach.</b> A rep who sells in English and Spanish can also cover Spanish-speaking buyers in the US and Latin America.</li>'
            '<li><b>Clear title, clear job.</b> Titles vary across markets too, so describe the motion in the job post and in the first interview.</li></ul>'
            '<p><b>How we help.</b> Our <a href="/talent">talent team</a> places vetted bilingual SDRs, BDRs and account executives from Latin America with US companies. Every candidate is interviewed in English by our sales team and roleplayed on a live cold call before you meet them. Tell us the motion and the hours you need covered, and you get three profiles within 72 hours. You interview them yourself, and if the rep does not work out in the first 30 days, we replace them.</p>'
        )),
    ],
    'conclusion': (
        '<p>SDR and BDR are two names for close cousins. The useful difference is the motion: answering people who asked, or reaching people who did not. Hire for the motion and the title takes care of itself.</p>'
        '<ol><li><b>Know the usual split:</b> SDR for inbound, BDR for outbound, both booking meetings for account executives.</li>'
        '<li><b>Expect different labels:</b> some companies flip the titles or use SDR for both.</li>'
        '<li><b>Put the motion first</b> in the job post, so candidates know what the job is.</li>'
        '<li><b>Decide from your lead flow:</b> slow replies to inbound point to an SDR; thin inbound and a clear market point to a BDR.</li>'
        '<li><b>Test the real work:</b> qualification and written replies for SDRs, a live cold call and a researched email for BDRs.</li>'
        '<li><b>Plan a ramp</b> of about three months before judging the full number.</li></ol>'
        '<p>When you are ready to hire, <a href="/talent">request profiles</a> and we will send three interviewed, bilingual reps within 72 hours.</p>'
    ),
    'faq': [
        ('What is the difference between an SDR and a BDR?',
         'In most companies an SDR qualifies inbound leads, people who already showed interest, and a BDR prospects outbound, reaching people who have not engaged yet. Both book meetings for account executives. Some companies flip the titles or use one title for both.'),
        ('Is a BDR higher than an SDR?',
         'Usually not. Both are entry-level roles at a similar level, and both commonly lead to an account executive role. A few companies use BDR for a more senior or enterprise-focused version, but there is no wide agreement on that.'),
        ('Do SDRs make cold calls?',
         'Outbound SDRs do, and in many companies "SDR" covers both inbound and outbound. A purely inbound SDR mostly calls people who already filled in a form. If cold calling is part of the job, say so clearly in the job post.'),
        ('Should my first sales development hire be an SDR or a BDR?',
         'If inbound leads already come in and wait too long for a reply, start with an inbound SDR. If inbound is thin and you can clearly name the accounts you want, start with an outbound BDR. Many early teams hire one person to do both with a clear daily split.'),
        ('What skills does a BDR need compared with an SDR?',
         'A BDR needs strong phone skills, research, persuasive writing and resilience, because most of the job is earning attention from people who did not ask for it. An SDR needs speed, organization and good qualification judgment, because the job is sorting real buyers from everyone else.'),
        ('How long does it take an SDR or BDR to ramp?',
         'About three months on average, according to The Bridge Group\'s research. Outbound reps often need the longer end, because they must learn the market and the buyer as well as the product.'),
        ('Can I hire an SDR or BDR from Latin America for a US team?',
         'Yes. Reps in Latin America work inside the US business day, so they can answer leads and call buyers on your hours. Test the English skill the role uses most: written replies for inbound, live cold calls for outbound.'),
    ],
}
