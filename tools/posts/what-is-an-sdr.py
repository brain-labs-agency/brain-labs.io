# Spec for blog/what-is-an-sdr.html. Build: python3 tools/blogkit.py tools/posts/what-is-an-sdr.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
ROSS = 'https://www.forentrepreneurs.com/predictable-revenue/'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2021-06-17-gartner-identifies-fours-ways-sales-leaders-can-boost'
ZOOM = 'https://pipeline.zoominfo.com/sales/sdr-ae-alignment'
IBM = 'https://www.ibm.com/think/topics/ai-sdr'

fig1 = figure(1, table(['', 'SDR', 'BDR', 'Account executive'], [
    ['<b>Main job</b>', 'Create and qualify new opportunities', 'Same job, title often used for outbound focus', 'Close the deal'],
    ['<b>Where leads come from</b>', 'Inbound, outbound or both', 'Mostly outbound', 'Meetings from SDRs, marketing and their own network'],
    ['<b>Closes deals?</b>', 'No', 'No', 'Yes'],
    ['<b>Measured on</b>', 'Qualified meetings and pipeline created', 'Qualified meetings and pipeline created', 'Closed revenue and win rate'],
    ['<b>Typical day</b>', 'Research, calls, emails, LinkedIn, booking', 'Research, calls, emails, LinkedIn, booking', 'Discovery calls, demos, proposals, negotiation'],
]), 'How the SDR compares with the BDR and the account executive. Many companies use SDR and BDR interchangeably; what matters is whether the role creates opportunities or closes them. Based in part on '
    + a(ZOOM, 'ZoomInfo\'s SDR and AE guide') + '.')

fig2 = figure(2, bar_chart('Median monthly SDR meeting quota, by how qualified the meeting must be', [
    ('Introductory meeting', 16.0),
    ('Semi-qualified meeting', 10.4),
    ('Fully qualified meeting', 9.0),
], vmax=20, highlight=('Fully qualified meeting',)),
    'The stricter the definition of a meeting, the lower the monthly quota. The global median across all models is 10 held meetings a month. Source: '
    + a(BRIDGE, 'The Bridge Group, 2025 SDR Metrics Report') + ', 351 B2B companies.')

fig3 = figure(3, timeline('The average SDR tenure, in months', [
    (0, 3, 'Ramp', 'learning product, buyer, tools'),
    (3, 23, 'Productive months', 'about 20 months at full speed, then promotion or exit'),
], 23, unit='mo', accent=('Ramp',)),
    'Average ramp is 3.0 months and average tenure is 1.9 years, so a typical SDR spends a little under two years in the seat, the first three of them ramping. Source: '
    + a(BRIDGE, 'The Bridge Group, 2025') + '.')

POST = {
    'slug': 'what-is-an-sdr',
    'title': 'What is an SDR? The role explained for founders',
    'h1': 'What is an SDR? The role <em>explained</em> for founders',
    'description': 'What a sales development representative does, how the role differs from a BDR and an account executive, how SDRs are measured, and when a founder should hire one.',
    'category': 'Hiring',
    'date': '2026-11-26',
    'date_label': 'November 26, 2026',
    'hero_img': 'cover-what-is-an-sdr',
    'card_img': 'cover-what-is-an-sdr',
    'card_title': 'What is an SDR? The role explained for founders',
    'card_text': 'The person who opens doors for your closers. What an SDR does all day, how to measure one, and when your company is ready for its first.',
    'takeaways': [
        'An SDR (sales development representative) creates and qualifies new sales opportunities, then hands them to an account executive to close. SDRs do not close deals.',
        'The role exists because prospecting and closing are different jobs. Splitting them, as Aaron Ross did at Salesforce, lets each person focus on one.',
        'SDRs are measured on qualified meetings and pipeline created, not revenue. Agree what counts as a qualified meeting before the first day.',
        'Hire an SDR once you have a repeatable story that closes and someone to manage and coach them. Without those two, even a great SDR struggles.',
    ],
    'intro': (
        '<p>If you are a founder, you have probably been told you need an SDR. Investors mention it, sales advisors recommend it, and half the job posts in your market seem to be for one. But the title is jargon, and the role is easy to misunderstand. Hire one at the wrong time, or for the wrong job, and you will spend months wondering why the pipeline did not move.</p>'
        '<p>This guide explains the role in plain terms: what an SDR does, where the role came from, how it differs from a BDR and an account executive, how to measure one and when you are ready to hire. It is written for founders and first-time sales leaders at US B2B companies.</p>'
    ),
    'cta': {
        'inline_lead': 'Ready to add an SDR?',
        'inline_text': 'Tell us who you sell to and the hours you need covered. We come back with three bilingual SDR candidates from Latin America within 72 hours, already interviewed in English and tested on a live cold call roleplay.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Find an SDR who works <em>your</em> hours.',
        'band_text': 'Vetted bilingual SDRs, account executives, sales ops and customer success professionals from Latin America, screened by people who run outbound every day. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('definition', 'What an SDR is', (
            '<p>An SDR, or sales development representative, is the person on a sales team who finds and qualifies new potential customers and books meetings for the people who close deals. The SDR opens the door; the account executive walks the buyer through it.</p>'
            '<p>The clearest way to understand the role is by what it does not do. In the words of Aaron Ross, who built one of the best-known sales development teams at Salesforce, efficient outbound reps "do NOT close deals, but create &amp; qualify new sales opportunities and then pass them to Account Executives to close," as he explained in an ' + a(ROSS, 'interview with David Skok') + '.</p>'
            '<p>In practice, an SDR spends the day on four kinds of work:</p>'
            '<ul><li><b>Research.</b> Finding companies that fit your ideal customer profile and the right person to contact at each one.</li>'
            '<li><b>Outreach.</b> Calls, emails and LinkedIn messages to start a conversation, usually across several touches.</li>'
            '<li><b>Qualification.</b> Checking that a prospect has the problem you solve, the authority to act and a reason to talk now.</li>'
            '<li><b>Handoff.</b> Booking the meeting and passing the account executive what they learned, so the first call starts in the right place.</li></ul>'
            '<p>Gartner summarizes the job the same way: ' + a(GARTNER, 'SDR teams') + ' "specialize in identifying prospective buyers, performing outreach to new prospects and qualifying incoming leads." Some SDRs work only inbound leads, some only outbound, and many do both. The constant is the goal: turn a name into a qualified conversation.</p>'
        )),
        ('why-it-exists', 'Why the SDR role exists', (
            '<p>The SDR role exists because finding new buyers and closing deals are different skills, and one person doing both usually does neither well. When closers also prospect, prospecting stops whenever deals get busy, and the pipeline runs dry a quarter later.</p>'
            '<p>The modern version of the role is often traced to Salesforce in the early 2000s. In the ' + a(ROSS, 'Skok interview') + ', Ross describes splitting sales into four functions: inbound lead qualification, outbound prospecting, account executives who close, and account management after the sale. The outbound reps, "commonly called Sales Development Reps," focused only on creating opportunities.</p>'
            '<p>His rule of thumb for when to split a role is still useful: when your reps, as a group, spend more than 20% of their time on a secondary function, break that function out into a new role. For a founder, the translation is simple. If you or your closer are spending a large part of the week hunting for people to talk to, prospecting may be ready to become its own job.</p>'
            '<p>Specialization helps in three ways:</p>'
            '<ul><li><b>Consistency.</b> Prospecting happens every day, not only when the calendar is empty.</li>'
            '<li><b>Focus.</b> Closers spend their time on qualified conversations instead of cold lists.</li>'
            '<li><b>Measurement.</b> You can see exactly how many opportunities are being created, and fix the top of the funnel separately from the bottom.</li></ul>'
            '<p>The trade-off is a handoff. Every time a buyer passes from one person to another, context can be lost. Teams that do this well agree clear criteria and keep the SDR and account executive talking every week, a point ' + a(ZOOM, 'ZoomInfo\'s guide') + ' makes strongly.</p>'
        )),
        ('sdr-bdr-ae', 'SDR vs BDR vs account executive', (
            '<p>An SDR and a BDR (business development representative) do essentially the same job, creating and qualifying opportunities, and many companies use the titles interchangeably. An account executive is different: they own the deal from the first real meeting to the signed contract.</p>'
            '<p>Where companies do draw a line between SDR and BDR, it is usually about lead source. ' + a(ZOOM, 'ZoomInfo puts it this way') + ': in the cleanest version, SDRs work warm inbound leads and BDRs hunt cold outbound prospects. Other companies use the opposite convention, or none at all. Read the job description, not the title.</p>'
            + fig1 +
            '<p>For a founder, the important distinction is between creating opportunities and closing them:</p>'
            '<ul><li><b>Hire an SDR or BDR</b> if you can close well but do not have enough qualified conversations.</li>'
            '<li><b>Hire an account executive</b> if you have more conversations than you can handle, or if you need someone to run deals so you can step back.</li></ul>'
            '<p>We go deeper on that choice in <a href="/blog/hire-sdr-or-ae-first">should a founder hire an SDR or an AE first</a>. The ratio between the two roles also matters once you grow. The ' + a(BRIDGE, 'Bridge Group\'s 2025 report') + ' found a median of one SDR for every 2.4 account executives, with one SDR to two AEs the most common setup.</p>'
        )),
        ('how-measured', 'How an SDR is measured', (
            '<p>An SDR is measured mainly on qualified meetings held and the pipeline those meetings create, not on revenue. Activity numbers such as calls and emails matter as leading indicators, but they are inputs, not results.</p>'
            '<p>The ' + a(BRIDGE, 'Bridge Group\'s 2025 SDR Metrics Report') + ', based on a survey of 351 B2B companies, gives useful reference points. The global median quota is 10 held meetings a month, down 40% since 2018. The median SDR runs 112 activities a day for about 4.1 quality conversations. And only 60% of SDRs hit quota, the lowest share in the study\'s history.</p>'
            + fig2 +
            '<p>The chart shows why the definition of a meeting matters so much. Teams that count any introductory meeting set higher quotas than teams that require a fully qualified one. Neither is wrong, but a number without a definition is meaningless. Before your SDR starts, write down:</p>'
            '<ul><li><b>What counts as qualified.</b> The fit, role and interest a prospect must show before a meeting counts.</li>'
            '<li><b>When a meeting counts.</b> Booked, or held. Most teams count held meetings.</li>'
            '<li><b>Who decides.</b> Usually the account executive confirms the meeting was real.</li>'
            '<li><b>Which activities you track.</b> Calls, emails, LinkedIn touches and conversations, as a health check.</li>'
            '<li><b>What pipeline the meetings create.</b> Over time, the opportunities that move forward are the truest measure.</li></ul>'
            '<p>Gartner has warned that ' + a(GARTNER, 'SDRs suffer productivity issues') + ' because of "unrealistic quota setting and limited operational guidance." Set targets against your own conversion data as soon as you have it, and review them honestly in the first quarter.</p>'
        )),
        ('skills', 'What makes a good SDR', (
            '<p>A good SDR combines curiosity about the buyer, resilience under rejection, clear writing and speaking, and the discipline to do the same work well every day. Experience helps, but these traits predict success more reliably than a long CV.</p>'
            '<p>What to look for:</p>'
            '<ul><li><b>Curiosity.</b> They want to understand a buyer\'s business before writing to them, and they ask good questions on calls.</li>'
            '<li><b>Resilience.</b> Most outreach gets no reply or a no. Good SDRs treat that as part of the job, not a judgment on them.</li>'
            '<li><b>Clear communication.</b> Short, specific emails and calm, natural calls. For roles selling to US buyers, that means strong spoken English.</li>'
            '<li><b>Coachability.</b> They take feedback from call reviews and apply it the next day.</li>'
            '<li><b>Organization.</b> They keep the CRM clean and follow up on time, because pipeline is lost in the gaps.</li></ul>'
            '<p>The best way to test these is to see them, not ask about them. A short live roleplay of a cold call tells you more than an hour of questions about past results. Our <a href="/blog/sdr-interview-process">20 minute SDR interview</a> shows a structure you can run in one call.</p>'
            '<p>Many companies now hire SDRs outside the US to cover more hours or reach a deeper talent pool. If you go that route, test spoken English directly and make sure the rep works inside your buyers\' business day. We cover how in <a href="/blog/hire-bilingual-sdr-latin-america">how to hire a bilingual SDR from Latin America</a> and <a href="/blog/native-english-sales-team-latin-america">building a native-level English sales team from Latin America</a>.</p>'
        )),
        ('ramp-tenure', 'Ramp, tenure and the SDR career path', (
            '<p>A new SDR typically takes about three months to ramp and stays in the role for a little under two years, often moving up to an account executive role. Plan for both: the ramp delays results, and the short tenure means you will be hiring again.</p>'
            '<p>The ' + a(BRIDGE, 'Bridge Group\'s 2025 data') + ' puts average ramp at 3.0 months, the lowest since 2010, and average tenure at 1.9 years. Median annual attrition was 40% in 2024, and that number includes promotions, which made up 16 of those 40 points.</p>'
            + fig3 +
            '<p>Three things follow for a founder:</p>'
            '<ul><li><b>Onboard properly.</b> A clear plan for product, buyer, process and tools shortens ramp. Our <a href="/blog/sdr-onboarding-plan">SDR onboarding plan for the first 30, 60 and 90 days</a> is a ready template.</li>'
            '<li><b>Build a path.</b> SDRs who can see a route to an account executive role stay longer and work harder. Promotion is a good outcome, not a loss.</li>'
            '<li><b>Document everything.</b> Messaging, objection notes and target lists should live in shared documents and the CRM, so the next SDR does not start from zero.</li></ul>'
            '<p>The Gartner release makes the same point from the other side: with ' + a(GARTNER, 'short tenure and a three month ramp') + ', an SDR may have less than a year at full productivity. Every week you cut from ramp is a week of pipeline you keep.</p>'
        )),
        ('when-to-hire', 'When a founder should hire an SDR', (
            '<p>Hire an SDR when you have a sales story that already closes, a clear ideal customer, and someone with time to manage and coach the new rep. If any of those three is missing, fix it first, or the SDR will be guessing.</p>'
            '<p>Signs you are ready:</p>'
            '<ul><li><b>You can close.</b> You or a closer win a good share of the qualified meetings you take.</li>'
            '<li><b>You know your buyer.</b> You can describe the companies and roles that buy, and why they buy.</li>'
            '<li><b>Prospecting is crowding out selling.</b> Finding people to talk to takes a large part of your week.</li>'
            '<li><b>Someone can coach.</b> A founder, closer or sales leader can review calls and emails every week.</li></ul>'
            '<p>Signs you are not ready yet:</p>'
            '<ul><li><b>You are still finding product market fit.</b> An SDR can create conversations, but not a story that does not exist yet.</li>'
            '<li><b>Nobody can manage them.</b> An SDR without coaching tends to send more activity, not better activity.</li>'
            '<li><b>You need pipeline next week.</b> With ramp, a new hire will not change this month\'s numbers.</li></ul>'
            '<p>There are also alternatives to a direct hire. Some companies place a vetted SDR through a talent partner to skip the slowest part of hiring. Others outsource the outbound function entirely, and some now use AI tools for research and drafting, which we explain in <a href="/blog/what-is-an-ai-sdr">what is an AI SDR</a>. ' + a(IBM, 'Even AI vendors frame') + ' the strongest setups as AI for volume and people for judgment. Whichever route you take, the human role of turning names into qualified conversations does not go away.</p>'
        )),
    ],
    'conclusion': (
        '<p>An SDR is the person who keeps your pipeline full so your closers can close. The role is simple to describe and hard to do well, and it works best when the company around it is ready: a story that sells, a clear buyer and someone to coach.</p>'
        '<ol><li><b>Know the job.</b> Create and qualify opportunities, then hand them off. No closing.</li>'
        '<li><b>Know why it exists.</b> Prospecting and closing are different skills; splitting them keeps both moving.</li>'
        '<li><b>Ignore title confusion.</b> SDR and BDR are often the same role. Read the job description.</li>'
        '<li><b>Measure meetings and pipeline.</b> And define a qualified meeting before day one.</li>'
        '<li><b>Hire for traits.</b> Curiosity, resilience, clear English and coachability, tested live.</li>'
        '<li><b>Plan for ramp and tenure.</b> Onboard well and build a path to the next role.</li>'
        '<li><b>Hire when ready.</b> A closing story and a coach come first.</li></ol>'
        '<p>When you are ready, we can put three interviewed, bilingual SDR candidates in front of you within 72 hours.</p>'
    ),
    'faq': [
        ('What does SDR stand for?',
         'SDR stands for sales development representative. It is the sales role that finds and qualifies new potential customers and books meetings for account executives, who close the deals.'),
        ('Do SDRs close deals?',
         'No. SDRs create and qualify opportunities and hand them to an account executive. Keeping prospecting and closing separate is the point of the role.'),
        ('What is the difference between an SDR and a BDR?',
         'Often nothing. Many companies use the titles interchangeably. Where they differ, one title usually covers inbound leads and the other outbound prospecting, but conventions vary by company.'),
        ('How many meetings should an SDR book per month?',
         'It depends on how strictly you define a qualified meeting. The Bridge Group\'s 2025 report puts the global median quota at 10 held meetings a month, higher for introductory meetings and lower for fully qualified ones.'),
        ('How long does it take for a new SDR to ramp?',
         'About three months on average, according to the Bridge Group\'s 2025 data. A structured onboarding plan can shorten it.'),
        ('Who should an SDR report to?',
         'Most SDR teams report to sales. The Bridge Group found 60% report to sales, 26% to marketing and 10% to an executive. In a small company, the SDR usually reports to the founder or the first sales leader.'),
        ('Can AI replace an SDR?',
         'AI can take over much of the research, drafting and follow up, but judgment, real conversations and qualification still need a person. Most teams use AI to make SDRs faster, not to remove the role.'),
    ],
}
