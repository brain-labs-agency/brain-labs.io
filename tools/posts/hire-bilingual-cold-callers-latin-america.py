# Spec for blog/hire-bilingual-cold-callers-latin-america.html. Build: python3 tools/blogkit.py tools/posts/hire-bilingual-cold-callers-latin-america.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


NEAR = 'https://ktvz.com/stacker-money/2026/01/27/five-trends-shaping-the-rise-in-us-companies-hiring-in-latin-america/'
EF_AR = 'https://www.ef.edu/epi/regions/latin-america/argentina/'
EF_WIKI = 'https://en.wikipedia.org/wiki/EF_English_Proficiency_Index'
GONG = 'https://www.gong.io/blog/the-best-and-worst-cold-call-openers-backed-by-data-from-300m-calls'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
TSR = 'https://todaysgeneralcounsel.com/federal-trade-commission-ftc-expands-telemarketing-rules-impacting-business-to-business-b2b-sales-and-compliance/'
FCC_AI = 'https://www.mayerbrown.com/en/insights/publications/2024/02/fcc-declares-authority-and-intent-to-regulate-ai-generated-calls-under-the-tcpa'

fig1 = figure(1, table(['Country', 'Time zone (UTC)', 'English signal', 'What to know'], [
    ['<b>Colombia</b>', 'UTC-5, no daylight saving', 'EF EPI 2025: 480', 'The top LatAm hiring market for US companies in 2025. Large pool of call center and SaaS sales experience, so screen individuals rather than averages.'],
    ['<b>Argentina</b>', 'UTC-3', 'EF EPI 2025: 575, highest in the region', 'Strong English and a deep pool of sales talent. Ahead of the US East Coast, so late Pacific coverage needs planning.'],
    ['<b>Mexico</b>', 'UTC-6 in most of the country', 'EF EPI 2025: 440', 'Central time overlap and many bilingual reps with US-facing experience, especially in the north and in Mexico City.'],
    ['<b>Costa Rica</b>', 'UTC-6', 'EF EPI 2025: 516', 'Long history of US-facing service and sales operations. Smaller pool, so roles can take longer to fill.'],
    ['<b>Peru and Chile</b>', 'UTC-5 and UTC-3 or UTC-4', 'EF EPI 2025: 519 and 517', 'Solid English averages and growing remote sales communities. Worth including in any search.'],
]), f'Where to look, by time zone and English signal. EF scores are country averages from self-selected test takers, so treat them as a starting point, not a filter. Sources: {a(NEAR, "Near 2026 State of LatAm Hiring Report, via Stacker")}, {a(EF_AR, "EF EPI 2025, Argentina")} and {a(EF_WIKI, "EF EPI 2025 country table")}.')

fig2 = figure(2, bar_chart('Success rate of four cold call openers, Gong analysis of 300M+ calls', [
    ('"Heard the name tossed around?"', 11.24),
    ('Permission-based opener', 11.18),
    ('"How\'s your day going?"', 7.6),
    ('"Did I catch you at a bad time?"', 2.15),
], unit='%', vmax=14, highlight=('"Did I catch you at a bad time?"',)),
    f'The first ten seconds change the outcome by a factor of five. Test openers in your screen, not just accents. Source: {a(GONG, "Gong Labs, cold call openers")}.')

fig3 = figure(3, steps('A cold caller screen that tests the job, not the CV', [
    ('English call', 'unplanned switch'),
    ('Cold open', '10 second opener'),
    ('Objection', 'live roleplay'),
    ('Voicemail', 'recorded, 30 sec'),
    ('References', 'ex-manager call'),
], accent=('Objection',)),
    'Five steps, each testing something the job needs every day. The live objection roleplay (amber) tells you the most, because it shows how the caller thinks in English under pressure.')

POST = {
    'slug': 'hire-bilingual-cold-callers-latin-america',
    'title': 'Where to hire bilingual LatAm cold callers for US B2B outbound',
    'h1': 'Where to hire bilingual LatAm cold callers for US B2B <em>outbound</em>',
    'description': 'Where to find bilingual cold callers in Latin America who can sell to US B2B buyers: which countries to look in, which channels work, how to screen for the phone and what to set up before the first dial.',
    'category': 'Hiring',
    'date': '2026-11-04',
    'date_label': 'November 4, 2026',
    'hero_img': 'hero-careers',
    'card_img': 'hero-careers',
    'card_title': 'Where to hire bilingual LatAm cold callers for US B2B outbound',
    'card_text': 'Which countries, which channels, how to screen for the phone and what to set up before the first dial.',
    'takeaways': [
        'Look in Colombia, Argentina and Mexico first. Colombia became the top Latin American hiring market for US companies in 2025, and SDRs and BDRs were the most-filled roles.',
        'You can hire through a sales-specialist nearshore firm, a job board, an employer of record or a freelance marketplace. Speed and screening quality vary a lot between them.',
        'Screen for the phone, not the CV: an unplanned English switch, a cold open, a live objection roleplay and a recorded voicemail.',
        'Before the first dial, align on call rules with counsel, set up local numbers and a script the caller can make their own, and plan for a ramp of a few months.',
    ],
    'intro': (
        '<p>Cold calling still works in B2B, but only when the person on the line sounds like they belong in the buyer\'s day. That is why so many US teams are looking south: Latin America shares the US working day, has a deep pool of bilingual sales talent and has become the default nearshore market for sales roles.</p>'
        '<p>The hard part is not finding people who speak English. It is finding people who can open a call with a stranger in Chicago, hold their ground on an objection and book a meeting your closer actually wants. This guide covers where to look, which hiring channels work, how to screen for the phone and what to put in place before the first dial.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring cold callers now?',
        'inline_text': 'Tell us the hours you need covered and who you sell to. We come back with three interviewed profiles in 72 hours, each roleplayed on a live cold call in English.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Bilingual callers who can hold a <em>US buyer</em>.',
        'band_text': 'Vetted SDRs, cold callers and AEs from Latin America, interviewed in English and roleplayed on a cold call before you meet them.',
    },
    'sections': [
        ('short-answer', 'The short answer: where to look', (
            '<p>The best places to hire bilingual cold callers for US B2B outbound are Colombia, Argentina and Mexico, reached through a nearshore firm that specializes in sales roles or through your own search on LinkedIn and regional job boards. Which channel fits depends on how many callers you need, how fast and who on your team can screen them.</p>'
            '<p>Demand has moved in this direction quickly. Near\'s ' + a(NEAR, '2026 State of LatAm Hiring Report') + ', based on more than 2,000 placements by US companies, found that BDRs and SDRs were the most-filled role type for the second year running, and that Colombia rose from third to first place with 23% of placements. Argentina and Brazil followed.</p>'
            '<p>Three reasons drive it:</p>'
            '<ul><li><b>Time zones.</b> Latin America sits inside the US business day. A caller in Bogotá is on Eastern time for part of the year and one hour off for the rest, which is exactly when your buyers pick up the phone.</li>'
            '<li><b>Experience.</b> Many cities have years of US-facing call center, customer success and SaaS sales operations, so you can find people who have already sold to US buyers.</li>'
            '<li><b>Speed.</b> The same Near report puts average placement time at 28 days, against three to six months for comparable domestic searches.</li></ul>'
            '<p>One caution up front: "bilingual" on a CV covers a wide range. A caller who is comfortable in English on a support ticket is not automatically comfortable being interrupted by a busy VP in the first five seconds. The rest of this guide is about telling those apart.</p>'
        )),
        ('countries', 'Which countries to look in', (
            '<p>Start with Colombia, Argentina and Mexico, then add Costa Rica, Peru and Chile for depth. Pick based on the US time zones you need covered and the strength of the individual candidate, not the country average.</p>'
            + fig1 +
            '<p><b>Colombia</b> is the volume market: large cities, a long history of US-facing call operations and, per Near, the most placements of any Latin American country in 2025. Its country-average English score is below the global average, which tells you to screen carefully, not to skip it. The strong speakers are there, and they are in demand.</p>'
            '<p><b>Argentina</b> has the highest English score in the region on the EF English Proficiency Index and a deep sales community in Buenos Aires and Córdoba. Its time zone runs ahead of the US, which works well for East Coast mornings and needs planning if you call the West Coast late in the day.</p>'
            '<p><b>Mexico</b> lines up with US Central time and has many reps who already sell into the US, especially in Monterrey, Guadalajara and Mexico City. Cultural familiarity with US buyers is often high.</p>'
            '<p><b>Brazil</b> is a major hiring market, but its first language is Portuguese. If you need English and Spanish, focus on the Spanish-speaking countries; if you sell into Brazil too, a Brazilian caller with strong English can cover both.</p>'
            '<p>Whatever country you choose, decide on the hours first. A cold caller who works a split shift to match your Pacific buyers will burn out. Staff the role to the hours your buyers keep and look where those hours are a normal working day.</p>'
        )),
        ('channels', 'Four ways to hire, compared', (
            '<p>There are four main channels: a sales-specialist nearshore firm, your own search on job boards, an employer of record with your own recruiting, and freelance marketplaces. The trade-off is between speed and screening on one side and control and effort on the other.</p>'
            '<p><b>Sales-specialist nearshore firm.</b> A firm that only places sales roles screens candidates on the phone before you see them and usually handles contracts and payments. It is the fastest route to interviewable candidates and the best fit when nobody on your team has time to screen dozens of calls. Ask who does the screening: a recruiter matching keywords, or someone who has run outbound.</p>'
            '<p><b>Your own search.</b> LinkedIn, regional job boards and local sales communities give you full control and the widest pool. The cost is time. Expect a high volume of applicants who list "bilingual" and a lot of screening to find the few who can open a call well.</p>'
            '<p><b>Employer of record.</b> An EOR legally employs the person in their country while they work for you. It solves contracts, payroll and local compliance, but not finding or screening. Pair it with your own search or a recruiter.</p>'
            '<p><b>Freelance marketplaces.</b> Useful for short tests or a part-time caller. Harder for a full-time seat, because commitment, availability and quality vary, and many profiles are built for appointment setting volume rather than consultative B2B calls.</p>'
            '<p>For most US teams hiring their first one to three callers, a specialist firm or a direct search with a strong screening process works best. Marketplaces suit tests; EORs suit companies that already know how to recruit in the region.</p>'
            '<p>Whichever route you choose, insist on meeting every candidate yourself before an offer. A caller is your company\'s voice to strangers. You should hear that voice before anyone else does.</p>'
        )),
        ('what-good-looks-like', 'What a good B2B cold caller sounds like', (
            '<p>A good B2B cold caller earns the next thirty seconds with a clear, relevant opener, stays calm when interrupted and asks questions instead of reciting a script. Accent matters far less than clarity, pace and confidence.</p>'
            '<p>The opener is where most calls are won or lost. Gong analyzed ' + a(GONG, 'more than 300 million cold calls') + ' and found large differences between openers. "Did I catch you at a bad time?" succeeded 2.15% of the time, while a permission-based opener and "Heard the name tossed around?" both cleared 11%.</p>'
            + fig2 +
            '<p>The point for hiring is that a caller\'s approach to the first ten seconds is learnable but not universal. Some candidates default to apologetic openers because that is what they did in support roles. Test it.</p>'
            '<p><b>Traits to look for:</b></p>'
            '<ul><li><b>Clarity over polish.</b> Short sentences, a steady pace and no filler. A buyer forgives an accent; they do not forgive confusion.</li>'
            '<li><b>Comfort with silence and no.</b> Good callers let a pause sit and treat "not interested" as the start of a question, not the end of the call.</li>'
            '<li><b>Business curiosity.</b> They ask what the buyer is working on and listen to the answer. In B2B, the meeting comes from relevance, not persistence.</li>'
            '<li><b>Resilience with structure.</b> Calling is repetitive. Look for people who track their own numbers and talk about what they changed when a week went badly.</li>'
            '<li><b>US B2B context.</b> Experience calling US businesses, ideally in a similar market, shortens ramp considerably.</li></ul>'
        )),
        ('screen', 'How to screen cold callers before you hire', (
            '<p>Screen cold callers by making them do the job: switch to English without warning, ask for a cold open, roleplay a live objection and request a recorded voicemail. A CV and a general English test tell you very little about how someone performs on a call.</p>'
            + fig3 +
            '<ol><li><b>Unplanned English switch.</b> Start the interview in Spanish and move to English mid-conversation. You learn how they think in English, not how well they rehearsed.</li>'
            '<li><b>Cold open.</b> Give them a one-paragraph brief on your offer and a buyer persona, five minutes to prepare, then ask for the first ten seconds of the call. Listen for a reason to stay on the line.</li>'
            '<li><b>Live objection roleplay.</b> Play a busy buyer who interrupts, says "send me an email" and then "we already have a vendor". This is the most predictive step. Watch whether they ask a question or retreat.</li>'
            '<li><b>Recorded voicemail.</b> Ask for a thirty-second voicemail. It shows pace, clarity and whether they can be specific without a live prompt.</li>'
            '<li><b>Reference with a former manager.</b> Ask how they handled a bad week and how they responded to coaching on recorded calls.</li></ol>'
            '<p>Keep the whole screen short. Twenty to thirty minutes is enough to see everything above, and it respects strong candidates who have several offers.</p>'
            '<p>At BL Agency, every candidate is interviewed in English by our sales team and roleplayed on a live cold call before they enter the pool. You still interview them yourself before you decide.</p>'
        )),
        ('before-first-dial', 'What to set up before the first dial', (
            '<p>Before your new caller makes a single call, align on the rules with counsel, set up the phone stack, write a script they can adapt and define what a qualified meeting is. Missing any of these turns the first month into cleanup.</p>'
            '<p><b>Call rules.</b> US telemarketing law treats business calls differently from consumer calls, but not as a free pass. In March 2024 the FTC ' + a(TSR, 'amended the Telemarketing Sales Rule') + ' so that its ban on misrepresentations applies to business-to-business calls for the first time. In February 2024 the FCC ' + a(FCC_AI, 'ruled that AI-generated voices count as "artificial"') + ' under the TCPA, which matters if you plan to mix in AI voice tools. State rules on calling and call recording vary, so review your setup with a lawyer. This article is not legal advice.</p>'
            '<p><b>Phone stack.</b> A dialer integrated with your CRM, local US numbers for the regions you call, call recording where consent rules allow it, and a clean list with direct dials where possible. Wrong numbers waste more caller time than anything else.</p>'
            '<p><b>Script and talk track.</b> Give them a written opener, three discovery questions, answers to the five most common objections and a clear close for the meeting. Then let them put it in their own words. A script read verbatim sounds read.</p>'
            '<p><b>Meeting definition.</b> Agree in writing what makes a meeting qualified: title, company fit and a stated reason to talk. Your caller should know exactly what a good outcome is before the first call.</p>'
            '<p><b>Hours and handoff.</b> Set the calling blocks around your buyers\' best answer times and decide who takes the booked meeting. A caller who books meetings nobody runs will not stay motivated for long.</p>'
        )),
        ('first-90-days', 'Making them productive in the first 90 days', (
            '<p>Plan for a ramp of about three months, with daily call reviews in the first weeks and a clear set of activity and quality measures. The Bridge Group\'s ' + a(BRIDGE25, '2025 SDR Metrics Report') + ' puts average SDR ramp at 3.0 months, and remote callers need the same structure as in-house ones.</p>'
            '<p><b>Weeks one and two.</b> Product, market and persona training. Listen to recorded calls from your best closers. Practice the opener and the top objections until they sound natural. Start live calling on a narrow, high-fit list.</p>'
            '<p><b>Weeks three to six.</b> Full calling blocks. Review two or three recorded calls together every day, focusing on one skill at a time. Track connects, conversations and meetings booked, but coach on the quality of the conversations.</p>'
            '<p><b>Weeks seven to twelve.</b> Widen the list, add new segments and let the caller test their own openers. Move call reviews to a few times a week. By the end of the quarter you should know whether this person can carry a number.</p>'
            '<p>Two habits make the biggest difference with nearshore callers. First, include them in the same team rituals as everyone else: the pipeline meeting, the win announcements, the deal reviews. Callers who feel like a vendor act like one. Second, close the loop on meeting quality. When your closer says a meeting was great or a waste of time, the caller should hear it within a day.</p>'
        )),
    ],
    'conclusion': (
        '<p>Hiring bilingual cold callers in Latin America works when you choose the right market, the right channel and a screen that tests the job itself.</p>'
        '<ol><li><b>Look in Colombia, Argentina and Mexico first,</b> and pick based on the hours you need covered.</li>'
        '<li><b>Choose a channel that matches your capacity to screen:</b> a sales-specialist firm if your team is stretched, a direct search if you have time.</li>'
        '<li><b>Screen for the phone:</b> unplanned English, a cold open, a live objection and a voicemail.</li>'
        '<li><b>Set up before the first dial:</b> call rules reviewed with counsel, the phone stack, a script and a meeting definition.</li>'
        '<li><b>Coach through a three-month ramp</b> and treat the caller as part of the team.</li></ol>'
        '<p>If you would rather start from callers who have already passed that screen, <a href="/talent">request profiles</a> and we will send three interviewed candidates within 72 hours.</p>'
    ),
    'faq': [
        ('Where can I hire bilingual LatAm cold callers experienced in US B2B outbound?',
         'Look in Colombia, Argentina and Mexico first, through a nearshore firm that specializes in sales roles or your own search on LinkedIn and regional job boards. Colombia was the top Latin American hiring market for US companies in 2025, and SDRs and BDRs were the most-filled roles.'),
        ('Which Latin American country has the best English for sales calls?',
         'Argentina has the highest country average on the EF English Proficiency Index in the region, but every country has strong speakers. Screen the individual on a live call rather than relying on country averages.'),
        ('Do LatAm cold callers work US hours?',
         'Yes. Most of Latin America is between UTC-3 and UTC-6, so a normal local working day overlaps most of the US business day. Staff the role to the hours your buyers keep so the caller is not working a night shift.'),
        ('How do I test a cold caller\'s English?',
         'Switch to English without warning during the interview, then ask for a cold open, run a live objection roleplay and request a recorded voicemail. These show how the person performs on a real call far better than a written test.'),
        ('Do US Do Not Call rules apply to B2B cold calls?',
         'Business calls are treated differently from consumer calls under the FTC Telemarketing Sales Rule, but since 2024 its ban on misrepresentations applies to B2B calls too, and state rules vary. Review your calling setup with a lawyer before you start.'),
        ('How long until a new cold caller books meetings?',
         'A caller with a solid list and script can book early meetings, but full productivity takes longer. The Bridge Group puts average SDR ramp at about three months.'),
        ('Should I hire a cold caller as a contractor or an employee?',
         'Either can work. Many US companies engage LatAm callers as contractors, often invoicing through a staffing partner, while others hire through an employer of record. Agree the model before you interview.'),
    ],
}
