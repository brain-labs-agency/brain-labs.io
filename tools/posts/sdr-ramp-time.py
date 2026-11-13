# Spec for blog/sdr-ramp-time.html. Build: python3 tools/blogkit.py tools/posts/sdr-ramp-time.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
BRIDGE_RAMP = 'https://bridgegroupinc.com/research/sdr-tenure-and-ramp-time'
RAIN = 'https://www.rainsalestraining.com/blog/sales-rep-onboarding-how-long-does-it-really-take'
SAASTR_TENURE = 'https://www.saastr.com/the-average-tenure-of-your-sdrs-about-14-months/'

fig1 = figure(1, bar_chart('Average SDR ramp time in months, Bridge Group', [
    ('2014 (peak)', 3.8),
    ('2025', 3.0),
], unit=' mo', vmax=5, highlight=('2025',)),
    f'Average time for a new SDR to reach full productivity, as reported by the Bridge Group. The 2025 figure of 3.0 months is the lowest the study has recorded since 2010. Source: {a(BRIDGE_RAMP, "Bridge Group, SDR tenure and ramp time")}.')

fig2 = figure(2, timeline('How long sales hires take to get good, RAIN Group survey of 423 sales leaders', [
    (0, 3, 'Ready for buyers', 'about 3 months'),
    (3, 9, 'Competent', 'about 9 months'),
    (9, 15, 'Top performer', 'about 15 months'),
], total=15, unit='mo', accent=('Ready for buyers',)),
    f'Sales leaders surveyed by RAIN Group said a new seller takes about three months to be ready for buyers, nine to be competent and fifteen to become a top performer. These are for sellers in general, not SDRs only. Source: {a(RAIN, "RAIN Group")}.')

fig3 = figure(3, table(['Checkpoint', 'What to measure', 'A healthy sign'], [
    ['<b>Week 2</b>', 'Product and buyer knowledge', 'Can explain who buys, why, and the three most common objections, in their own words.'],
    ['<b>Day 30</b>', 'Activity and message quality', 'Hitting the agreed activity level on a real segment, with messages you would send yourself.'],
    ['<b>Day 45</b>', 'Conversations and replies', 'Getting real replies and conversations, and handling first objections without help.'],
    ['<b>Day 60</b>', 'Meetings booked', 'Booking meetings that pass your written definition, on a ramped target.'],
    ['<b>Day 90</b>', 'Full target', 'At or near full target, with a pipeline you can see building week to week.'],
]), 'A ramp scorecard. Each checkpoint measures a leading indicator before the next one, so you can see a stalled ramp in week six instead of month four.')

POST = {
    'slug': 'sdr-ramp-time',
    'title': 'SDR ramp time: how long until a new rep books meetings',
    'h1': 'SDR ramp time: how long until a new rep <em>books meetings</em>',
    'description': 'How long SDR ramp time really is (3.0 months on average), when a new rep should book a first meeting, what makes ramp slower or faster, and a 90-day scorecard to track it.',
    'category': 'Hiring',
    'date': '2026-11-13',
    'date_label': 'November 13, 2026',
    'hero_img': 'cover-sdr-ramp-time',
    'card_img': 'cover-sdr-ramp-time',
    'card_title': 'SDR ramp time: how long until a new rep books meetings',
    'card_text': 'The benchmark, what slows a new rep down, what speeds them up and a scorecard for the first 90 days.',
    'takeaways': [
        'The average SDR takes about 3.0 months to reach full productivity, according to the Bridge Group\'s 2025 research, the shortest ramp the study has recorded since 2010.',
        'Ramp to full target and time to first meeting are different numbers. A well prepared rep often books a first meeting within the first month or two.',
        'Ramp is short compared with tenure, but it matters: with average tenure around 1.9 years, every month of ramp is a month less of full productivity.',
        'The biggest levers are who you hire and what is ready on day one: a defined buyer, a working message, a clean list and a manager who gives feedback daily.',
    ],
    'intro': (
        '<p>Every founder who hires an SDR asks the same question in week two: when will this person start booking meetings? It is a fair question. Until a new rep ramps, you are paying for learning, not pipeline, and the gap between hiring and results is where many sales hires quietly fail.</p>'
        '<p>This guide answers the question with the best benchmarks we could find, explains the difference between ramp time and time to first meeting, and walks through what makes ramp slower or faster. It ends with a simple scorecard for the first 90 days, so you can tell a normal ramp from a stalled one early.</p>'
    ),
    'cta': {
        'inline_lead': 'Want a rep who ramps faster?',
        'inline_text': 'Start with someone who has already passed an English interview and a live cold call roleplay. Tell us the role and get three interviewed profiles in 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'SDRs who arrive <em>ready to ramp</em>.',
        'band_text': 'Vetted SDRs, cold callers and AEs from Latin America, interviewed in English and roleplayed on a live cold call by people who sell, working your US business hours.',
    },
    'sections': [
        ('short-answer', 'The short answer: about three months to full productivity', (
            '<p>A new SDR takes about three months on average to reach full productivity. The Bridge Group, which has surveyed sales development teams since 2010, reports an average ramp of ' + a(BRIDGE_RAMP, '3.0 months in its 2025 research') + ', the lowest it has recorded, down from a peak of 3.8 months in 2014.</p>'
            '<p>The Bridge Group suggests the drop may reflect better, AI-assisted onboarding or tighter expectations from managers about time to productivity. Either way, three months is now the reasonable planning number for a typical B2B SDR: shorter for simple products and experienced hires, longer for technical products and first-time reps.</p>'
            + fig1 +
            '<p>Two cautions before you put three months in your plan. First, it is an average across many kinds of companies in the ' + a(BRIDGE25, '2025 SDR Metrics Report') + ', which surveyed 351 B2B companies, and the sample leans toward teams with experienced sales development leaders. A startup hiring its first SDR, with no playbook and no SDR manager, should expect to be on the slower side unless it prepares well.</p>'
            '<p>Second, "ramped" means reaching full target, not booking a first meeting. Those are different milestones, and mixing them up is the most common source of frustration in the first weeks. The next section separates them.</p>'
        )),
        ('measure', 'Ramp time vs time to first meeting: measure both', (
            '<p>Ramp time is how long a new rep takes to reach full target; time to first meeting is how long until they book a single qualified meeting. Track both. The first tells you when the hire pays off, the second tells you early whether the ramp is on track.</p>'
            '<p>A rep who is well prepared often books a first meeting within the first month or two, well before they are fully ramped. If you only measure full ramp, you have no signal for three months. If you only measure the first meeting, one lucky reply can hide a slow ramp. Together they give you a reading at week six and a reading at month three.</p>'
            '<p>To make ramp measurable, write three things down before the rep starts:</p>'
            '<ul><li><b>What full target means.</b> Usually a number of qualified meetings per month, defined the same way your account executives define a good meeting.</li>'
            '<li><b>The ramped target for each month.</b> A common pattern is a reduced target in month one, a higher one in month two and the full target in month three. The exact steps matter less than agreeing them in advance.</li>'
            '<li><b>The leading indicators.</b> Activity, replies and conversations come before meetings. If they are on track, meetings usually follow.</li></ul>'
            '<p>Also write down what counts as a qualified meeting. A rep can "ramp" quickly by booking meetings that your account executives do not want. Our guide to <a href="/blog/sdr-onboarding-plan">an SDR onboarding plan for the first 30, 60 and 90 days</a> shows how to build these targets into the first three months week by week.</p>'
        )),
        ('why-it-matters', 'Why ramp time matters more than it looks', (
            '<p>Ramp matters because it eats into a short window. The Bridge Group puts average SDR tenure at ' + a(BRIDGE_RAMP, '1.9 years in 2025') + ', the highest since the early 2010s. Take three months of ramp out of roughly 23 months of tenure and a typical rep spends about one month in eight learning rather than producing.</p>'
            '<p>That is the average. Many teams see shorter stays. Jason Lemkin of SaaStr ' + a(SAASTR_TENURE, 'has written') + ' that average SDR tenure is closer to 14 months, and that more than half of respondents to his poll did not see SDRs last a full year. On a 14 month tenure, a three month ramp is more than a fifth of the time the rep is with you.</p>'
            '<p>Turnover multiplies the effect. The Bridge Group\'s ' + a(BRIDGE25, '2025 report') + ' found median annual SDR attrition of 40% in 2024, counting promotions as well as departures. Each time a seat turns over, the ramp starts again. A team that loses two reps a year and takes four months to ramp each replacement spends a large part of the year below capacity, even if every rep is good.</p>'
            '<p>That is why shortening ramp by even a few weeks is worth real effort. It adds productive months to every hire, and it makes each replacement less painful. It also changes how you should judge a hire: a rep who ramps in two months and stays two years is worth far more than a slightly stronger rep who takes five months to get going and leaves after a year.</p>'
        )),
        ('slower', 'What makes ramp slower', (
            '<p>Ramp is slowest when the rep has to discover the job while doing it. A complex product, a buyer nobody has defined, no proven message, weak lists and a manager with no time are the usual causes, and most of them are about the company, not the rep.</p>'
            '<p>Research on sellers in general shows how long full competence takes. In a ' + a(RAIN, 'RAIN Group survey of 423 sales leaders') + ', respondents said a new seller takes about three months to be ready to interact with buyers, about nine months to be competent and about fifteen months to become a top performer. SDRs work a narrower job than account executives, which is part of why their ramp is shorter, but the pattern holds: readiness comes first, mastery much later.</p>'
            + fig2 +
            '<p>The common causes of a slow ramp:</p>'
            '<ul><li><b>A complex or technical product.</b> The rep needs time to explain it simply and handle informed objections.</li>'
            '<li><b>No defined buyer.</b> If you cannot say who buys and why, the rep has to find out by trial and error.</li>'
            '<li><b>No message that works yet.</b> Writing the first sequences and finding the first replies is real work. A rep who inherits a proven sequence ramps much faster than one who starts from a blank page.</li>'
            '<li><b>Weak lists and data.</b> Bounced emails and wrong numbers waste the first weeks and destroy confidence.</li>'
            '<li><b>Too little manager time.</b> The fastest learning comes from listening to calls and reviewing emails with someone experienced, daily at first.</li>'
            '<li><b>Long sales cycles.</b> When buyers take weeks to respond, the feedback loop is slow and the rep learns slowly too.</li></ul>'
        )),
        ('faster', 'What makes ramp faster', (
            '<p>Ramp is fastest when you hire for skills that are already proven and prepare the job before day one. A rep who has done outbound before, speaks your buyer\'s language and walks into a defined buyer, a working message and a clean list can book meetings early and reach target within the normal three months, sometimes sooner.</p>'
            '<p>RAIN Group reports that companies that improved their onboarding and enablement ' + a(RAIN, 'cut ramp-up time by more than half') + '. That is one firm\'s observation rather than a controlled study, but it matches what most sales leaders see: the biggest gains come from preparation, not from pushing the rep harder.</p>'
            '<p><b>Before day one:</b></p>'
            '<ul><li><b>Hire for proven skills.</b> Prior outbound experience, strong written and spoken English for US buyers, and a cold call roleplay in the interview. Our <a href="/blog/sdr-interview-process">20-minute SDR interview</a> is built to test exactly this.</li>'
            '<li><b>Write the buyer down.</b> A one-page profile of who buys, why, and what triggers the search.</li>'
            '<li><b>Prepare a starting list</b> of well-researched accounts, so the rep does not spend week one building data.</li>'
            '<li><b>Collect your best material:</b> recorded calls, recent wins and losses, the objections that repeat and the emails that got replies.</li></ul>'
            '<p><b>In the first weeks:</b></p>'
            '<ul><li><b>Start on one segment</b>, the one where you understand the buyer best.</li>'
            '<li><b>Review every email and listen to calls daily</b> for the first two weeks, then taper.</li>'
            '<li><b>Roleplay objections</b> before the rep meets them live.</li>'
            '<li><b>Celebrate the first meeting</b> and study it: who replied, to which message, and why.</li></ul>'
        )),
        ('remote', 'Ramping a remote or nearshore SDR', (
            '<p>A remote SDR in Latin America can ramp as fast as a local hire if three things are true: they work your business hours, their English is strong enough for US buyers from day one, and they get the same daily feedback a rep in your office would. Ramp slows down when any of those is missing, not because the rep is remote.</p>'
            '<p><b>Hours.</b> Latin America sits inside the US business day, with 1 to 4 hours of extra overlap with any US time zone. That means your new rep can join your team calls, get same-day feedback on emails and call buyers during their working hours. Daily feedback is the single biggest driver of fast ramp, and it only works when your days overlap. Our guide to <a href="/blog/nearshore-vs-offshore-sales-teams">nearshore vs offshore sales teams</a> covers why this matters.</p>'
            '<p><b>English.</b> A rep who is still building confidence in English has to learn the language of your market and the language itself at the same time. Test it before you hire: a live conversation and a cold call roleplay, not a CV line. Our article on <a href="/blog/native-english-sales-team-latin-america">building a native-level English sales team from Latin America</a> explains what to look for.</p>'
            '<p><b>US buyer context.</b> A strong rep from Latin America may know outbound well and still need time on the specific habits of US buyers in your industry: how direct to be, which titles matter, which references they recognize. Put this in the onboarding plan explicitly. Sharing recorded calls with your best US customers is the fastest way to teach it.</p>'
            '<p><b>Inclusion.</b> Remote reps ramp slower when they are left out of the informal learning that happens in an office. Invite them to deal reviews, pair them with an account executive and give them a named person to ask questions every day.</p>'
            '<p>This is how we screen at BL Agency: every candidate we present has already been interviewed in English and roleplayed on a live cold call by people who run outbound, and works US business hours. That does not replace your onboarding, but it removes the two most common reasons a nearshore hire ramps slowly.</p>'
        )),
        ('scorecard', 'A 90-day ramp scorecard', (
            '<p>The easiest way to manage ramp is to check a leading indicator at each stage instead of waiting for meetings. By week two the rep should know the buyer, by day 30 the activity and message quality should be right, by day 45 replies should be coming in, by day 60 meetings should be booking and by day 90 the rep should be at or near full target.</p>'
            + fig3 +
            '<p>If a checkpoint slips, ask why before you ask the rep to work harder. A rep who cannot explain the buyer at week two needs more onboarding, not more activity. A rep with good activity but no replies by day 45 usually has a message or list problem, which is often yours to fix. A rep with replies but no meetings by day 60 may need help with qualification or call skills.</p>'
            '<p>When the scorecard shows a real problem with the person rather than the setup, it usually shows it between day 45 and day 60. That is the time for an honest conversation about fit, while there is still time to fix it or to replace the hire without losing a whole quarter.</p>'
        )),
    ],
    'conclusion': (
        '<p>SDR ramp time is about three months on average, and the difference between a fast ramp and a slow one is mostly preparation and the person you hire.</p>'
        '<ol><li><b>Plan on about three months</b> to full target, based on the Bridge Group\'s 3.0 month average, and adjust for your product and your playbook.</li>'
        '<li><b>Measure first meeting and full ramp separately</b>, with ramped targets agreed before day one.</li>'
        '<li><b>Remember the window</b>: with tenure around two years or less and high turnover, every month of ramp counts.</li>'
        '<li><b>Hire for proven skills</b> and prepare the buyer, the message, the list and your best calls before the rep starts.</li>'
        '<li><b>Use a scorecard</b> with leading indicators at week two, day 30, 45, 60 and 90, and act on the first missed checkpoint.</li></ol>'
        '<p>If you want to start from a rep who has already proven their English and their cold call, <a href="/talent">tell us the role</a> and we will send three interviewed profiles in 72 hours.</p>'
    ),
    'faq': [
        ('What is the average SDR ramp time?',
         'About three months. The Bridge Group reports an average SDR ramp time of 3.0 months in its 2025 research, the lowest it has recorded since 2010, down from a peak of 3.8 months in 2014.'),
        ('How long until a new SDR books their first meeting?',
         'Often within the first month or two for a well prepared rep with a defined buyer, a working message and a clean list. Time to first meeting is earlier than full ramp, so track both.'),
        ('What is the difference between ramp time and time to first meeting?',
         'Ramp time is how long until the rep reaches full target. Time to first meeting is how long until they book one qualified meeting. The first tells you when the hire pays off; the second is an early sign the ramp is on track.'),
        ('How can I shorten SDR ramp time?',
         'Hire reps with proven outbound skills, define the buyer in writing, give them a working message and a clean starting list, share recorded calls, and review their emails and calls daily in the first weeks.'),
        ('Why does SDR ramp time matter so much?',
         'Because SDR tenure is short. With average tenure around 1.9 years according to the Bridge Group, and median annual attrition of 40%, every month of ramp is a month less of full productivity, and every replacement starts the ramp again.'),
        ('Do remote or nearshore SDRs take longer to ramp?',
         'Not if they work your business hours, have strong English for US buyers from day one and get daily feedback. Ramp slows down when any of those is missing, not because the rep is remote.'),
        ('When should I worry that a new SDR is not ramping?',
         'When they miss a leading indicator: cannot explain the buyer by week two, have no replies by day 45, or no qualifying meetings by day 60. Find out whether the cause is the setup or the person, and act early.'),
    ],
}
