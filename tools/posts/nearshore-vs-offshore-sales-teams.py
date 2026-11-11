# Spec for blog/nearshore-vs-offshore-sales-teams.html. Build: python3 tools/blogkit.py tools/posts/nearshore-vs-offshore-sales-teams.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


TT = 'https://www.techtarget.com/it-strategy/definition/What-is-nearshore-outsourcing-and-how-does-it-work'
HOWDY = 'https://www.howdy.com/blog/nearshoring-vs-offshoring-time-zone-overlap'
EF25 = 'https://www.ef.com/ca/about-us/press/articles/2025/ef-english-proficiency-index-2025-launched/'
EF_AR = 'https://www.ef.com/assetscdn/cefcom-epi-site/fact-sheets/2025/ef-epi-fact-sheet-argentina-english.pdf'
EPI_TABLE = 'https://worldpopulationreview.com/country-rankings/ef-english-proficiency-index-by-country'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
FTC = 'https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'

fig1 = figure(1, bar_chart('Hours of difference from New York during US summer time', [
    ('Bogota, Colombia', 1),
    ('Buenos Aires, Argentina', 1),
    ('Mexico City, Mexico', 2),
    ('Warsaw, Poland', 6),
    ('Bengaluru, India', 9.5),
    ('Manila, Philippines', 12),
], unit=' h', vmax=14, highlight=('Bogota, Colombia', 'Buenos Aires, Argentina', 'Mexico City, Mexico')),
    f'Time difference from New York, in either direction, while US daylight saving time is in effect. Nearshore cities (amber) sit within about two hours of the US East Coast; offshore hubs are six to twelve hours away, which pushes live selling into night shifts. Based on {a(HOWDY, "Howdy, nearshoring vs offshoring time zone overlap")} and standard UTC offsets.')

fig2 = figure(2, table(['What you care about', 'Onshore (US)', 'Nearshore (Latin America)', 'Offshore (Asia, Eastern Europe)'], [
    ['<b>Live calls in buyer hours</b>', 'Native fit.', 'Daytime work for the rep, with most or all of the US day covered.', 'Usually a night shift for the rep.'],
    ['<b>Same-day replies and handoffs</b>', 'Immediate.', 'Immediate within shared hours.', 'Often the next morning.'],
    ['<b>English for live conversation</b>', 'Native.', 'Varies widely by person; test speaking live.', 'Varies widely by person; test speaking live.'],
    ['<b>Familiarity with US buyers</b>', 'Highest.', 'Often strong in reps with US-facing experience.', 'Strong in reps from US-facing support or sales teams.'],
    ['<b>Management overlap</b>', 'Full.', 'Full or near full.', 'Limited; needs async habits.'],
    ['<b>Best suited to</b>', 'Any role.', 'Cold calling, SDR, AE and account management roles.', 'Research, list building, data work and async support.'],
]), 'How the three models compare for sales roles specifically. For work that does not need live conversation, the time zone gap matters much less.')

fig3 = figure(3, steps('Hiring a nearshore sales rep', [
    ('Hours', 'which US hours'),
    ('English', 'live, unscripted'),
    ('Roleplay', 'a real cold call'),
    ('Model', 'agency or contractor'),
    ('Onboard', '30, 60, 90 days'),
], accent=('Roleplay',)),
    'Five steps for a nearshore sales hire. The live roleplay (amber) tells you more about how a rep will sound to a US buyer than any CV or test score.')

POST = {
    'slug': 'nearshore-vs-offshore-sales-teams',
    'title': 'Nearshore vs offshore sales teams: what changes for US buyers',
    'h1': 'Nearshore vs offshore sales teams: what <em>changes</em> for US buyers',
    'description': 'Nearshore vs offshore for sales roles: what each term means, why time zones matter more for selling than for other work, how to judge English, and which model fits SDRs, AEs and research roles.',
    'category': 'Hiring',
    'date': '2026-11-11',
    'date_label': 'November 11, 2026',
    'hero_img': 'cover-nearshore-vs-offshore-sales-teams',
    'card_img': 'cover-nearshore-vs-offshore-sales-teams',
    'card_title': 'Nearshore vs offshore sales teams: what changes for US buyers',
    'card_text': 'What each term means, why time zones matter more for selling, and which model fits which role.',
    'takeaways': [
        'Nearshore means hiring in a nearby country with a similar time zone, which for US companies usually means Latin America. Offshore means a distant country, often six to twelve hours away.',
        'For sales roles, the time zone is the biggest difference. A nearshore rep sells during their own working day; an offshore rep calling US buyers usually works nights.',
        'English varies more by person than by country. National averages are a starting signal, so test spoken English live in every interview.',
        'Offshore works well for research, list building and async work. Live selling roles (cold callers, SDRs, AEs) usually fit nearshore or onshore better.',
    ],
    'intro': (
        '<p>If you are building a sales team outside the US, you will hear two words constantly: nearshore and offshore. Most of what is written about them comes from software development, where the main question is how many hours a team can collaborate. Sales is different. Your reps talk to buyers, live, during the buyer\'s working day, and that changes which trade offs matter.</p>'
        '<p>This guide explains what each term means, then looks at the five things that actually change for a US company hiring sales talent: time zones, spoken English, familiarity with US buyers, management and compliance. At the end, you will find a simple way to decide which model fits which role, and a hiring path for nearshore reps.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring sales reps outside the US?',
        'inline_text': 'Tell us the hours you need covered and who you sell to. We come back with three interviewed profiles from Latin America in 72 hours, each roleplayed on a live call in English.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Bilingual reps who work <em>your</em> hours.',
        'band_text': 'Vetted SDRs, cold callers and AEs from Latin America, interviewed in English and roleplayed on a sales call before you meet them.',
    },
    'sections': [
        ('definitions', 'Nearshore, offshore and onshore: what the terms mean', (
            '<p>Nearshore means hiring people in a nearby country with a similar time zone; offshore means hiring in a distant country, often on the other side of the world. TechTarget\'s ' + a(TT, 'definition of nearshore outsourcing') + ' describes it as work performed by people in neighboring countries, while offshoring means contracting services in countries that are farther away.</p>'
            '<p>For a US company, the three options usually look like this:</p>'
            '<ul><li><b>Onshore.</b> People in the US, either employees or an outside provider based in the US.</li>'
            '<li><b>Nearshore.</b> People in Latin America and sometimes Canada. Mexico, Colombia, Argentina, Chile, Peru, Costa Rica and Brazil are the most common sources for sales roles.</li>'
            '<li><b>Offshore.</b> People in Asia or Europe. The Philippines and India are the best known hubs for customer-facing work, and Eastern Europe for technical work.</li></ul>'
            '<p>The terms describe geography, not quality. There are excellent sales professionals in every one of these places and weak ones too. What changes with distance is how the work fits into your buyer\'s day, how easily you can manage it, and which roles it suits.</p>'
            '<p>One more distinction worth making early: "nearshore" can describe both how you hire (directly, through a staffing agency, or through an employer of record) and where the person sits. This guide is about where the person sits. We cover the hiring models briefly in section six.</p>'
        )),
        ('time-zones', 'Time zones: the biggest difference for sales', (
            '<p>Time zones are the biggest practical difference between nearshore and offshore for sales roles. A nearshore rep in Colombia or Mexico sells during their normal working day because it overlaps almost fully with the US; an offshore rep in Manila or Bengaluru calling US buyers usually works through the night.</p>'
            '<p>According to ' + a(HOWDY, 'Howdy\'s comparison of time zone overlap') + ', Mexico shares time zones with much of the US, and Latin American hubs stay within a couple of hours of the East Coast all year. Using standard UTC offsets, Colombia matches US Eastern time from November to March and sits one hour behind the rest of the year, Argentina is one to two hours ahead and Mexico City is one to two hours behind. India sits 9.5 to 10.5 hours ahead of US Eastern time and the Philippines 12 to 13, leaving about an hour or less of overlap in a normal working day.</p>'
            + fig1 +
            '<p>For an engineering team, a big gap can be managed with handoffs and written updates. For a sales team, it is harder to work around:</p>'
            '<ul><li><b>Cold calls happen in the buyer\'s day.</b> Buyers answer the phone during business hours in their own time zone. An offshore caller has to shift their whole schedule to match.</li>'
            '<li><b>Replies need fast answers.</b> When a prospect replies at 11 a.m. with a question, a same-day answer keeps the conversation alive. A next-morning reply often does not.</li>'
            '<li><b>Handoffs happen live.</b> An SDR passing a warm prospect to an AE, or joining the first few minutes of a meeting, needs both people awake.</li>'
            '<li><b>Coaching happens in real time.</b> Listening to calls, running roleplays and giving quick feedback is much easier when the manager and the rep share most of the day.</li></ul>'
            '<p>Night shifts are workable, and many offshore teams run them well. But they are harder to sustain, and they narrow the pool to people willing to work them long term. For roles built around live conversation, that is a real cost even if it never shows up on an invoice.</p>'
        )),
        ('english', 'Spoken English: judge the person, not the country', (
            '<p>Spoken English varies more by person than by country, so national rankings are a starting signal and nothing more. Every candidate for a US-facing sales role should be tested on live, unscripted English in the interview, whatever country they live in.</p>'
            '<p>The ' + a(EF25, 'EF English Proficiency Index 2025') + ', which covers 123 countries and regions, is the most cited benchmark. In it, Argentina ranked 26th in the world and first in Latin America, according to ' + a(EF_AR, 'EF\'s Argentina fact sheet') + '. The Philippines also sits in the high proficiency band, while Colombia, Mexico, Brazil and India sit lower, according to a ' + a(EPI_TABLE, 'summary of the 2025 results') + '.</p>'
            '<p>Two details in the EF findings matter for sales hiring:</p>'
            '<ul><li><b>Speaking is often the weakest skill.</b> EF reports that speaking was the weakest of the measured skills in more than half the countries assessed. A candidate who writes well may still struggle on a fast cold call.</li>'
            '<li><b>Averages hide the people you want.</b> A country with a modest average can still have a large pool of excellent speakers, especially among people who have worked in US-facing sales, support or education. You are hiring one person, not a national average.</li></ul>'
            '<p>What to test instead of trusting a score: a short live conversation about the candidate\'s last role, a cold call roleplay where you play a busy and slightly skeptical buyer, and a written follow up email. Our guide to ' + '<a href="/blog/native-english-sales-team-latin-america">building a native-level English sales team</a>' + ' goes deeper on how to judge spoken English, and our ' + '<a href="/blog/sdr-interview-process">20-minute SDR screen</a>' + ' shows how to fit it into one interview.</p>'
        )),
        ('buyer-context', 'Familiarity with US buyers and business culture', (
            '<p>Familiarity with how US buyers talk and decide matters as much as grammar, and it comes from experience rather than geography. A rep who has spent years selling to or supporting US companies will usually sound more natural to your buyer than one with better test scores and no US exposure, in any country.</p>'
            '<p>Your buyers are protective of their time. A ' + a(GARTNER, 'Gartner survey of 632 B2B buyers') + ' found that 73% actively avoid suppliers whose outreach feels irrelevant. In practice, that means a rep has seconds to show they understand the buyer\'s world: the tools they use, the problems common in their industry, the way they expect a short and direct conversation.</p>'
            '<p>What to look for, whatever the location:</p>'
            '<ul><li><b>US-facing experience.</b> Previous roles selling to, or supporting, US customers. Ask about specific buyers and industries.</li>'
            '<li><b>Comfort with directness.</b> US B2B buyers tend to value a short, clear ask. Roleplays show quickly whether a rep can get to the point and handle a blunt "not interested".</li>'
            '<li><b>Industry vocabulary.</b> Reps who have sold software, staffing or professional services before need less time to sound credible in those markets.</li>'
            '<li><b>Calendar awareness.</b> US holidays, quarter ends and budget cycles affect when buyers respond. Reps who have worked US hours tend to know these rhythms already.</li></ul>'
            '<p>Nearshore candidates often have an advantage here simply because working US hours is normal in their market, so many have years of direct exposure to US teams and customers. But it is not automatic. Ask about it and test it, as you would anywhere.</p>'
        )),
        ('management', 'Management, coaching and ramp', (
            '<p>A sales rep ramps faster when the manager can coach them during the day, so management overlap is a quiet but important difference between the models. Nearshore reps share most or all of the US working day with their manager; offshore reps often share an hour or less unless someone works off hours.</p>'
            '<p>Ramp is already the longest hidden cost in sales hiring. The Bridge Group\'s ' + a(BRIDGE25, '2025 SDR Metrics Report') + ' puts average SDR ramp at about three months, even for in-house teams. Anything that slows feedback stretches that period further. The habits that shorten ramp all depend on overlap:</p>'
            '<ul><li><b>Call reviews.</b> Listening to recorded calls together the same day, while the details are fresh.</li>'
            '<li><b>Live roleplays.</b> Practicing a new objection before the next call block, not the next morning.</li>'
            '<li><b>Quick questions.</b> A rep who can message a manager mid-call block and get an answer in minutes learns faster than one who waits a day.</li>'
            '<li><b>Team rituals.</b> Daily standups, pipeline reviews and deal debriefs work best when the whole team can attend.</li></ul>'
            '<p>Offshore teams can make this work with strong local team leads and well documented playbooks, and many large operations do. For a small US company hiring its first one to five reps, though, the manager is usually the founder or a sales leader in the US. For them, a rep in a nearby time zone is simply easier to coach. A week by week plan like our ' + '<a href="/blog/sdr-onboarding-plan">30, 60 and 90 day SDR onboarding plan</a>' + ' helps either way.</p>'
        )),
        ('compliance-hiring', 'Hiring models and compliance: what stays with you', (
            '<p>Whatever model you choose, responsibility for how your company sells stays with you. Hiring abroad changes the employment paperwork, not the rules your outreach must follow in the US.</p>'
            '<p>On the outreach side, the FTC\'s ' + a(FTC, 'CAN-SPAM compliance guide') + ' says the law makes no exception for business-to-business email and that you cannot contract away your legal responsibility. The same logic applies to calling rules and to data protection: a rep in another country selling to US buyers on your behalf is still selling as your company. Make sure every rep, wherever they are, is trained on the rules that apply to your outreach. This guide is not legal advice.</p>'
            '<p>On the hiring side, US companies usually choose one of three routes:</p>'
            '<ul><li><b>Direct contractor.</b> You find, vet and contract the person yourself. Most control, most work, and you carry the risk of classification and local rules.</li>'
            '<li><b>Employer of record.</b> A provider employs the person locally on your behalf and handles payroll, benefits and local compliance. You still find and manage the person.</li>'
            '<li><b>Staffing or recruiting partner.</b> A partner finds and vets candidates for you, often with interviews and roleplays done before you meet anyone. You choose and manage the person.</li></ul>'
            '<p>Two practical checks for any route: make sure the rep uses your tools and accounts (CRM, dialer, email) so your data stays in your systems, and agree how customer data is handled on personal devices. These matter equally for nearshore and offshore hires.</p>'
        )),
        ('how-to-decide', 'How to decide: match the model to the role', (
            '<p>Decide by role, not by region. Roles built around live conversation with US buyers (cold callers, SDRs, AEs, account managers) usually fit nearshore or onshore best; roles that can be done asynchronously (account research, list building, data hygiene, some support) can work well offshore.</p>'
            + fig2 +
            '<p>Some teams combine both: offshore or automated research builds the account lists overnight, and nearshore reps work them during the US day. That split follows the same logic as the table: put live conversation where the buyer\'s hours are, and put async work wherever it is done best.</p>'
            '<p>If you decide on nearshore for a sales role, a simple hiring path looks like this:</p>'
            + fig3 +
            '<ol><li><b>Set the hours.</b> Decide which US hours you need covered, East Coast mornings, West Coast afternoons or both. That narrows the countries that fit.</li>'
            '<li><b>Test English live.</b> A short, unscripted conversation in the first interview.</li>'
            '<li><b>Roleplay a real call.</b> Use your actual buyer, your actual offer and a realistic objection.</li>'
            '<li><b>Choose the hiring model.</b> Direct, employer of record or a recruiting partner, depending on how much of the process you want to own.</li>'
            '<li><b>Plan the first 90 days</b> with clear milestones and daily coaching time.</li></ol>'
            '<p>We help US companies with step two through four: our ' + '<a href="/talent">talent team</a>' + ' interviews bilingual sales professionals from Latin America in English and roleplays each one on a live sales call before you meet them.</p>'
        )),
    ],
    'conclusion': (
        '<p>Nearshore and offshore are both legitimate ways to build a sales team. The difference that matters most for selling is not cost or culture in the abstract; it is whether your rep can talk to your buyer during the buyer\'s day, and whether you can coach that rep during yours.</p>'
        '<ol><li><b>Know the terms.</b> Nearshore is nearby with a similar time zone, usually Latin America for US companies. Offshore is distant, often six to twelve hours away.</li>'
        '<li><b>Weigh time zones first</b> for any role built on live conversation.</li>'
        '<li><b>Test spoken English live</b> for every candidate, wherever they are. Country averages are only a signal.</li>'
        '<li><b>Look for US-facing experience</b>, and give new reps the daily coaching overlap that shortens ramp.</li>'
        '<li><b>Match the model to the role</b>: live selling near your buyers, async work wherever it is done best.</li></ol>'
        '<p>If you are hiring sales reps who need to work US hours, <a href="/talent">tell us what you need</a> and we will send interviewed profiles from Latin America.</p>'
    ),
    'faq': [
        ('What is the difference between nearshore and offshore?',
         'Nearshore means hiring in a nearby country with a similar time zone, which for US companies usually means Latin America. Offshore means hiring in a distant country, such as the Philippines or India, often six to twelve hours away from US time.'),
        ('Which countries count as nearshore for US companies?',
         'Mostly Latin America: Mexico, Colombia, Argentina, Chile, Peru, Costa Rica and Brazil are common choices, and Canada is sometimes included. Colombia shares US Eastern time and Mexico shares time zones with much of the US.'),
        ('Is nearshore or offshore better for sales roles?',
         'For roles built on live conversation, such as cold callers, SDRs and AEs, nearshore usually fits better because reps can sell during their own working day while US buyers are at work. Offshore works well for research, list building and other async work.'),
        ('Can offshore reps cold call US buyers?',
         'Yes, and many teams do, but the rep usually has to work a night shift to match US business hours. That is harder to sustain and makes daily coaching with a US manager more difficult.'),
        ('Which Latin American country has the best English?',
         'In the EF English Proficiency Index 2025, Argentina ranked first in Latin America and 26th in the world. Country averages are only a signal, though: test each candidate\'s spoken English live, since speaking is often the weakest skill.'),
        ('Does hiring abroad change my compliance obligations?',
         'No. Your outreach to US buyers still has to follow US rules. The FTC says you cannot contract away responsibility under CAN-SPAM, so train every rep on the rules that apply, wherever they are. This is not legal advice.'),
        ('How do I hire a nearshore sales rep?',
         'Decide which US hours you need covered, test spoken English live, roleplay a real call with your buyer and offer, choose a hiring model (direct, employer of record or a recruiting partner) and plan the first 90 days with daily coaching.'),
    ],
}
