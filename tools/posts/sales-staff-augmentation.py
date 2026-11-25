# Spec for blog/sales-staff-augmentation.html. Build: python3 tools/blogkit.py tools/posts/sales-staff-augmentation.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


OYSTER = 'https://www.oysterhr.com/glossary/staff-augmentation'
AMS = 'https://www.weareams.com/knowledge-base/cws/what-is-the-difference-between-staff-augmentation-and-outsourcing/'
ASHBY = 'https://www.ashbyhq.com/talent-trends-report/reports/recruiting-operations-benchmarks-talent-trends?view=full'
SIA = 'https://www.staffingindustry.com/news/global-daily-news/us-businesses-take-35-days-to-fill-job-roles-study-finds'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'

fig1 = figure(1, table(['', 'Direct hire', 'Sales staff augmentation', 'Outsourced SDR program'], [
    ['<b>Who finds the person</b>', 'You', 'The partner, you choose from a short list', 'The vendor'],
    ['<b>Who manages the daily work</b>', 'You', 'You', 'The vendor'],
    ['<b>Who owns the results</b>', 'You', 'You', 'The vendor, against agreed targets'],
    ['<b>Whose processes and tools</b>', 'Yours', 'Yours', 'Usually the vendor\'s'],
    ['<b>How fast you can start</b>', 'Slowest: full hiring cycle plus notice period', 'Fast: candidates are already screened', 'Fast: the team already exists'],
    ['<b>How easy to scale down</b>', 'Hardest', 'Easier, per the contract terms', 'Easier, per the contract terms'],
]), 'Three ways to add sales capacity. Augmentation sits in the middle: someone else finds and screens the person, but the rep works inside your team, on your process. Based in part on the comparison in '
    + a(OYSTER, 'Oyster\'s staff augmentation glossary') + '.')

fig2 = figure(2, bar_chart('Median days to first fill a role, by seniority', [
    ('Junior roles', 52),
    ('Mid-level roles', 63),
    ('Senior roles', 71),
], unit=' days', vmax=85, highlight=('Junior roles',)),
    'Median days from opening a role to the first hire, across all functions, from Ashby customer data covering January 2021 to March 2026. Sales development roles usually sit in the junior band. Source: '
    + a(ASHBY, 'Ashby 2026 Talent Trends Report') + '.')

fig3 = figure(3, steps('How a BL Agency talent placement runs', [
    ('Brief', '30 minute call'),
    ('Profiles', 'within 72 hours'),
    ('You interview', 'and you decide'),
    ('Start', 'contract via BL'),
    ('First 30 days', 'replacement window'),
], accent=('Profiles',)),
    'From brief to first call with candidates in under two weeks. Every candidate has already been interviewed in English and has done a live cold call roleplay before you meet them.')

POST = {
    'slug': 'sales-staff-augmentation',
    'title': 'Sales staff augmentation: adding reps without a long hiring cycle',
    'h1': 'Sales staff augmentation: adding reps without a <em>long</em> hiring cycle',
    'description': 'What sales staff augmentation is, how it differs from direct hiring and outsourced SDR programs, when it makes sense, and how to vet a partner so the reps you add actually sell.',
    'category': 'Hiring',
    'date': '2026-11-25',
    'date_label': 'November 25, 2026',
    'hero_img': 'cover-sales-staff-augmentation',
    'card_img': 'cover-sales-staff-augmentation',
    'card_title': 'Sales staff augmentation: adding reps without a long hiring cycle',
    'card_text': 'You keep the process and the management. A partner finds, screens and contracts the reps, so you can add capacity in weeks instead of months.',
    'takeaways': [
        'Sales staff augmentation means adding reps who are found, screened and contracted by a partner but work inside your team, on your process, managed by you.',
        'It is faster than a direct hire because the slowest parts of hiring (sourcing, first screens and paperwork) are already done when you meet the candidates.',
        'It is not a way to outsource sales management. If you do not have someone to onboard, coach and measure the rep, an outsourced program or a managed service fits better.',
        'Judge a partner on how they screen for selling skill, not on how many CVs they send, and agree the contract model, hours and replacement terms before you interview anyone.',
    ],
    'intro': (
        '<p>Most sales leaders know the feeling. The pipeline target went up this quarter, the team did not, and opening a new role means weeks of sourcing, screening and interviews, then a notice period, then ramp. By the time the new rep is productive, the quarter that needed them is over.</p>'
        '<p>Sales staff augmentation is one answer to that timing problem. This guide explains what it is and is not, how it compares with direct hiring and with outsourcing your outbound, when it makes sense, what you still have to own, and how to vet a partner. It is written for US companies adding SDRs, account executives or sales support roles, including nearshore reps from Latin America.</p>'
    ),
    'cta': {
        'inline_lead': 'Need sales reps who can start soon?',
        'inline_text': 'Tell us the role and the hours you need covered. We come back with interviewed, bilingual candidates from Latin America within 72 hours, or we tell you we do not have the right fit.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Add sales reps who work <em>your</em> hours.',
        'band_text': 'Vetted bilingual SDRs, account executives, sales ops and customer success professionals from Latin America, screened by people who run revenue operations every day. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('what-it-is', 'What sales staff augmentation is', (
            '<p>Sales staff augmentation is a way to add sales reps to your existing team through a partner who finds, screens and usually contracts them, while you direct their daily work. The rep sells your product, follows your process, uses your tools and reports to your manager. The partner handles the parts of hiring and employment you do not want to build yourself.</p>'
            '<p>The key line is ownership. As ' + a(OYSTER, 'Oyster puts it') + ', augmentation brings in outside professionals without handing over project ownership, while in outsourcing a third party owns delivery. ' + a(AMS, 'AMS describes the same split') + ': with augmentation, ownership of the work stays with your organization and the added people are supervised by your managers.</p>'
            + fig1 +
            '<p>In sales, that difference is large. An outsourced SDR program usually comes with its own playbook, its own managers and targets the vendor is accountable for. An augmented rep is closer to a new team member who arrived faster. You decide what they work on, how they work and whether they are doing well.</p>'
            '<p>The term covers several roles. The most common are:</p>'
            '<ul><li><b>SDRs and BDRs</b> who research accounts, run outreach and qualify meetings for your closers.</li>'
            '<li><b>Account executives</b> who run deals from discovery to close.</li>'
            '<li><b>Sales operations</b> people who keep the CRM, data and reporting clean.</li>'
            '<li><b>Customer success and account managers</b> who own onboarding, renewals and expansion.</li></ul>'
            '<p>If you are still deciding which of the first two to add, our guide on <a href="/blog/hire-sdr-or-ae-first">whether to hire an SDR or an AE first</a> covers that choice.</p>'
        )),
        ('why-hiring-is-slow', 'Why the normal sales hiring cycle is slow', (
            '<p>The normal hiring cycle is slow because it has several steps that run one after another, and each one has its own delays: writing the role, sourcing, screening, interviews, offer, notice period and then ramp. Augmentation shortens the first half of that chain. It cannot remove the second half.</p>'
            '<p>The published numbers show how long the first half takes. ' + a(ASHBY, 'Ashby\'s 2026 Talent Trends Report') + ', based on customer data from 2021 to 2026, puts the median time to first fill a role at 52 days for junior roles, 63 for mid-level and 71 for senior, and 60 days for business roles overall. A ' + a(SIA, 'SmartRecruiters dataset reported by Staffing Industry Analysts') + ' found that US businesses take an average of 35 days to fill vacancies, and that only 79% of offers are accepted, so some searches start again near the end.</p>'
            + fig2 +
            '<p>Then the second half begins. Many candidates need to give notice at their current job. And once they start, they need time to become productive. ' + a(BRIDGE, 'The Bridge Group\'s 2025 SDR report') + ', a survey of 351 B2B companies, puts average SDR ramp time at 3.0 months, the lowest it has recorded since 2010.</p>'
            '<p>Put together, a new SDR opened today may not be fully productive for a good part of a year. For a team that needs pipeline this quarter, that is the real problem augmentation is meant to solve.</p>'
            '<ul><li><b>What augmentation shortens:</b> sourcing, first screens, skill checks, paperwork and, often, the notice period, because partners keep a pool of people who are available.</li>'
            '<li><b>What it does not shorten:</b> your own interviews, onboarding and ramp. A rep who joins faster still has to learn your product and your buyers.</li></ul>'
        )),
        ('when-it-fits', 'When augmentation makes sense, and when it does not', (
            '<p>Augmentation makes sense when you already know how to sell, you have someone to manage the rep, and your problem is capacity or speed. It does not make sense when you are still working out who your buyer is or when nobody on your side has time to coach a new rep.</p>'
            '<p>Good fits:</p>'
            '<ul><li><b>A proven motion that needs more hands.</b> Your current reps book meetings, and you need more of the same.</li>'
            '<li><b>Coverage gaps.</b> You need people working specific US hours or a time zone your current team cannot cover.</li>'
            '<li><b>A new segment or language.</b> You want to test a market, for example Spanish-speaking buyers, without building a full team first.</li>'
            '<li><b>Uncertain headcount.</b> You need reps now but are not ready to commit to permanent hires, for example before a funding round closes.</li>'
            '<li><b>Backfills.</b> A rep left, and the territory cannot wait out a full hiring cycle.</li></ul>'
            '<p>Poor fits:</p>'
            '<ul><li><b>No sales process yet.</b> A rep cannot follow a playbook that does not exist. Founder-led sales usually needs to produce a repeatable story first.</li>'
            '<li><b>No manager.</b> If the founder is the only person who could coach the rep and has no time to do it, the rep will struggle no matter how good they are.</li>'
            '<li><b>You want outcomes, not people.</b> If what you actually want is meetings on the calendar and you do not want to manage the people who book them, an outsourced program is a better match. We compare the two in <a href="/blog/outsourced-sdr-vs-in-house-sdr">outsourced SDR vs in-house SDR</a>.</li></ul>'
            '<p>Some teams combine both: an outbound system that finds and contacts accounts, plus augmented reps who take the conversations from there. The question to ask is simple. Do you need more people in your process, or do you need someone else to run the process?</p>'
        )),
        ('what-you-own', 'What you still own after the rep starts', (
            '<p>You still own everything that makes a rep productive: onboarding, the ideal customer profile, the messaging, the tools, the targets and the weekly coaching. Augmentation moves the hiring work to a partner. It does not move the management work.</p>'
            '<p>Teams that get the most out of augmented reps treat them like any other new hire from day one:</p>'
            '<ul><li><b>A real onboarding plan.</b> Product, buyer, process and tools, in that order, with clear milestones. Our <a href="/blog/sdr-onboarding-plan">SDR onboarding plan for the first 30, 60 and 90 days</a> is a good template.</li>'
            '<li><b>The same tools and access as everyone else.</b> CRM, sequencing tool, call recording, shared channels. A rep who has to ask for access every week is a rep who is not selling.</li>'
            '<li><b>A named manager and a weekly one to one.</b> Call reviews, email reviews and a look at the pipeline together.</li>'
            '<li><b>Clear activity and outcome targets,</b> agreed in the first week and reviewed against the ramp you expect.</li>'
            '<li><b>A place in the team.</b> Invite them to the team meetings, the wins channel and the planning sessions. People who feel like outsiders leave like outsiders.</li></ul>'
            '<p>That last point matters more than it looks. The Bridge Group found a ' + a(BRIDGE, 'median annual SDR attrition of 40%') + ' in 2024, counting promotions as well as departures. Sales roles turn over quickly in every hiring model. The way you manage and include the rep has more influence on whether they stay than the contract they are on.</p>'
        )),
        ('vet-partner', 'How to vet a sales staff augmentation partner', (
            '<p>Vet a partner on one thing above all: can they tell whether someone can sell? Many staffing firms match keywords on a CV, and a CV says very little about how a person handles a cold call or an objection.</p>'
            '<p>Questions worth asking before you sign:</p>'
            '<ul><li><b>Who screens the candidates?</b> Recruiters, or people who have run sales teams and outbound themselves?</li>'
            '<li><b>How do you test selling skill?</b> Look for a live roleplay, such as a cold call or a discovery call, not just a conversation about past results.</li>'
            '<li><b>How do you test English?</b> For nearshore reps selling to US buyers, ask how English is checked and whether you can hear it yourself before deciding. We cover this in <a href="/blog/native-english-sales-team-latin-america">building a native-level English sales team from Latin America</a>.</li>'
            '<li><b>How many profiles will I see?</b> A short list with honest notes on each person is more useful than thirty CVs.</li>'
            '<li><b>Do I interview them myself?</b> You should always meet the person you are adding to your team, and make the final decision.</li>'
            '<li><b>What hours will they work?</b> Make sure the rep works inside your buyers\' business day, not a shifted schedule.</li>'
            '<li><b>What happens if it does not work out?</b> Ask about the replacement window and the notice terms after it.</li>'
            '<li><b>Can we hire them directly later?</b> Ask whether conversion to a direct hire is possible and on what terms.</li></ul>'
            '<p>A good partner will also tell you when they do not have the right person, rather than sending the closest match they have. That answer is a better sign of quality than any number of profiles.</p>'
        )),
        ('contract-model', 'Contractor, employee or EOR: agree the model first', (
            '<p>Agree how the rep will be engaged before you interview anyone, because it affects compliance, onboarding and how quickly they can start. The common options are a contractor arrangement through the partner, a hire through an employer of record (EOR), or a direct hire by your company.</p>'
            '<ul><li><b>Contractor through the partner.</b> The rep invoices through the partner and you receive one bill. This is usually the fastest option and keeps payroll off your side.</li>'
            '<li><b>Employer of record.</b> An ' + a(OYSTER, 'EOR lets you employ people') + ' in a country where you do not have a legal entity. The EOR is the legal employer, and you direct the work.</li>'
            '<li><b>Direct hire.</b> You employ the person yourself, which requires a local entity or a structure that fits the country.</li></ul>'
            '<p>Each model has trade-offs. ' + a(OYSTER, 'Oyster notes') + ' that worker classification risk is higher in augmentation than in outsourcing, because you direct the work. If a contractor works like an employee, with fixed hours, your tools and your manager, some countries may treat them as one. Ask the partner how they handle this in each country they place from, and check with your own legal or HR adviser. This guide is not legal advice.</p>'
            '<p>At BL Agency, most talent engagements run as contractors invoicing through us, and we structure a direct hire instead when a company prefers it. We agree the model before any interviews, so nobody is surprised once a candidate says yes. For a wider view of the options, see our guide on <a href="/blog/hire-sales-reps-colombia-argentina-mexico">hiring sales reps in Colombia, Argentina or Mexico</a>.</p>'
        )),
        ('realistic-timeline', 'A realistic timeline, from brief to first meetings', (
            '<p>With a good partner, you can be interviewing screened candidates within days and have a rep starting within a few weeks, but plan for ramp after that. The speed gain is real. It just happens at the start of the process, not at the end.</p>'
            + fig3 +
            '<p>Here is how the steps break down when you work with us:</p>'
            '<ul><li><b>Brief.</b> One 30 minute call about what you sell, who you sell to, the hours you need covered and your timeline.</li>'
            '<li><b>Profiles within 72 hours.</b> Three candidates who have already been interviewed in English by our sales team and roleplayed a cold call, with honest notes on each.</li>'
            '<li><b>You interview.</b> You meet the candidates directly and decide. There is no candidate you never get to speak to.</li>'
            '<li><b>Contract and start.</b> The agreement, invoicing and payment run through us.</li>'
            '<li><b>The first 30 days.</b> If the rep does not work out, we replace them at no additional cost. After that, the engagement runs month to month with 30 days\' notice on either side.</li></ul>'
            '<p>After the start date, your onboarding plan takes over. Use the ramp you expect from any new rep as the baseline, track activity in the first weeks and outcomes after that, and review honestly at 30, 60 and 90 days. If you want to test candidates more deeply before deciding, our <a href="/blog/sdr-interview-process">20 minute SDR interview</a> is a quick, structured way to do it.</p>'
        )),
    ],
    'conclusion': (
        '<p>Sales staff augmentation is a speed tool. It removes the slowest, least valuable part of hiring, which is finding and screening people, and lets you spend your time on the part that matters, which is choosing the right person and making them productive.</p>'
        '<ol><li><b>Know what you are buying.</b> People who join your process, not a team that runs its own.</li>'
        '<li><b>Use it when the motion works.</b> Capacity, coverage, new segments and backfills are the strong cases.</li>'
        '<li><b>Keep owning the management.</b> Onboarding, coaching, tools and targets stay with you.</li>'
        '<li><b>Vet for selling skill.</b> Live roleplays and English you can hear beat CVs and keyword matches.</li>'
        '<li><b>Agree the model early.</b> Contractor, EOR or direct hire, decided before interviews.</li>'
        '<li><b>Plan for ramp.</b> Faster hiring does not mean instant results.</li></ol>'
        '<p>Get those right and you can add reps in weeks instead of months, with people who work your hours and fit your team.</p>'
    ),
    'faq': [
        ('What is sales staff augmentation?',
         'It is a way to add sales reps to your team through a partner who finds, screens and usually contracts them, while you manage their daily work. The reps follow your process, use your tools and report to your manager.'),
        ('How is staff augmentation different from outsourcing sales?',
         'With augmentation you keep ownership of the work and manage the reps yourself. With outsourcing, the vendor owns delivery, usually with its own managers, process and targets. ' + a(OYSTER, 'Oyster') + ' and ' + a(AMS, 'AMS') + ' both draw the line at who owns and supervises the work.'),
        ('How fast can an augmented sales rep start?',
         'Much faster than a direct hire, because candidates are already screened and often available. Industry data puts typical time to fill in the range of five to ten weeks for a direct hire, while an augmentation partner can usually put screened candidates in front of you within days.'),
        ('Do augmented sales reps need onboarding?',
         'Yes, the same onboarding as any new hire. Augmentation speeds up hiring, not ramp. The Bridge Group puts average SDR ramp time at about three months.'),
        ('Are augmented reps contractors or employees?',
         'It depends on the model you agree. Many work as contractors through the partner, some are employed through an employer of record, and some are hired directly. Agree the model before interviews and check classification rules with your own adviser.'),
        ('Can I hire an augmented rep directly later?',
         'Often yes. Ask the partner at the start whether conversion to a direct hire is possible and what the terms are, so it is written into the contract.'),
        ('Which sales roles can be augmented?',
         'SDRs and BDRs are the most common, followed by account executives, sales operations and customer success or account management roles.'),
    ],
}
