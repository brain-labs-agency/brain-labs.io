# Spec for blog/how-many-meetings-should-an-sdr-book.html. Build: python3 tools/blogkit.py tools/posts/how-many-meetings-should-an-sdr-book.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
BRIDGE_BLOG = 'https://blog.bridgegroupinc.com/sdr-metrics'
REVENUEHERO = 'https://revenuehero.io/reports/no-show-benchmark-december-02-2024'
QUOTAPATH = 'https://www.quotapath.com/blog/study-overview-bridging-the-gap-to-understanding-your-sdrs/'
DANISH = 'https://danishleadco.io/blog/how-many-sales-meetings-should-your-outbound-team-generate'

fig1 = figure(1, bar_chart('Median monthly SDR quota by meeting definition', [
    ('Introductory meetings', 16.0),
    ('Semi-qualified meetings', 10.4),
    ('Fully qualified meetings', 9.0),
    ('Converted to opportunity (all)', 6.0),
], highlight=('Semi-qualified meetings',)),
    'Median monthly quota per SDR, by how strictly the meeting is defined. The stricter the definition, the lower the number. Source: ' + a(BRIDGE, 'The Bridge Group, SDR Models, Motions and Metrics 2025') + ', a study of 351 B2B companies.')

fig2 = figure(2, table(['Factor', 'Pushes the monthly number up', 'Pushes it down'], [
    ['<b>Meeting definition</b>', 'Introductory calls, light qualification', 'Budget, authority and need confirmed before booking'],
    ['<b>Deal size and buyer</b>', 'Smaller, faster deals; one decision maker', 'Large enterprise deals; buying committees'],
    ['<b>Market size</b>', 'Thousands of companies that fit', 'A few hundred accounts worth contacting'],
    ['<b>Lead source</b>', 'Inbound leads and warm signals', 'Pure cold outbound to unaware buyers'],
    ['<b>Channels</b>', 'Phone plus email plus LinkedIn', 'A single channel'],
    ['<b>Rep tenure</b>', 'Fully ramped, knows the objections', 'First three months on the job'],
    ['<b>Support</b>', 'Clean data, researched accounts, clear messaging', 'The rep builds lists and copy alone'],
]), 'Why two SDRs at different companies can both be doing well on very different numbers. Compare a rep with a target built from the same conditions, not with a number from someone else\'s team.')

fig3 = figure(3, timeline('A new SDR\'s first three months', [
    (0, 1, 'Learn', 'product, buyer, tools'),
    (1, 2, 'First meetings', 'partial target'),
    (2, 3, 'Near full pace', 'most of target'),
    (3, 4, 'Full target', 'judge on results'),
], 4, unit='mo', accent=('Full target',)),
    'A ramped target matches the average ramp time of about three months reported by ' + a(BRIDGE, 'The Bridge Group') + '. Judge a new rep on activity quality and learning in the first months, and on the full number only once ramp is over (amber).')

POST = {
    'slug': 'how-many-meetings-should-an-sdr-book',
    'title': 'How many meetings should an SDR book per month?',
    'h1': 'How many meetings should an SDR book <em>per month?</em>',
    'description': 'The benchmark for SDR meetings per month, why it depends on how you define a meeting, what pushes the number up or down, how to ramp a new rep and how to set a fair target for your team.',
    'category': 'Hiring',
    'date': '2026-11-17',
    'date_label': 'November 17, 2026',
    'hero_img': 'cover-how-many-meetings-should-an-sdr-book',
    'card_img': 'cover-how-many-meetings-should-an-sdr-book',
    'card_title': 'How many meetings should an SDR book per month?',
    'card_text': 'The median is about 10, but your meeting definition, market and ramp change the right number for your team.',
    'takeaways': [
        'The median SDR quota is about 10 held meetings a month, and about 6 that convert into a real opportunity, according to The Bridge Group\'s 2025 study of 351 B2B companies.',
        'The number depends on what you call a meeting: teams that book introductory calls set higher targets than teams that only count fully qualified meetings.',
        'Count meetings that were held and accepted by the account executive, not meetings booked. A full calendar of no-shows is not pipeline.',
        'Give a new SDR about three months to ramp, and set the target from your own funnel, not from a benchmark built on someone else\'s market.',
    ],
    'intro': (
        '<p>"How many meetings should my SDR be booking?" is one of the first questions founders ask after hiring their first sales development rep, and one of the hardest to answer from the outside. Ask ten sales leaders and you will hear numbers from 5 to 50, all of them correct for somebody.</p>'
        '<p>This guide gives you the benchmark first, from the most cited research on sales development, and then explains why your number may be very different. We cover how the meeting definition changes the target, which factors push it up or down, how to ramp a new rep, and how to set a fair, useful target for your own team. We place bilingual SDRs from Latin America with US companies, so we also cover what to look for in a rep who can hit it.</p>'
    ),
    'cta': {
        'inline_lead': 'Need an SDR who can hit your number?',
        'inline_text': 'Tell us the role, your meeting definition and the US hours you need covered. We send three interviewed, bilingual SDR profiles from Latin America within 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'An SDR who books <em>your</em> meetings, on your hours.',
        'band_text': 'Vetted bilingual sales professionals from Latin America, interviewed in English and roleplayed on a cold call before you meet them. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('benchmark', 'The benchmark: about 10 held meetings a month', (
            '<p>A typical SDR quota is about 10 held meetings a month. In The Bridge Group\'s ' + a(BRIDGE, '2025 SDR Metrics report') + ', the global median monthly quota was 10 meetings held, and 6 meetings that converted into a qualified opportunity.</p>'
            '<p>The Bridge Group has surveyed sales development teams for more than a decade, and its 2025 edition covers ' + a(BRIDGE_BLOG, '351 B2B companies') + '. Two findings frame every conversation about meeting targets:</p>'
            '<ul><li><b>Targets have come down.</b> The median quota for held meetings is down about 40% since 2018, and the quota for converted meetings is down about 43%. Teams now ask for fewer, better meetings rather than more first calls.</li>'
            '<li><b>Many reps still miss.</b> Only 60% of SDRs were at quota, the lowest share in the study\'s history. That suggests many targets are set from hope rather than from the team\'s actual funnel.</li></ul>'
            + fig1 +
            '<p>The same report shows how much the number moves with the meeting definition. Teams whose SDRs book introductory meetings had a median quota of 16 a month. Teams that expect semi-qualified meetings sat at about 10, and teams that only count fully qualified meetings at 9.</p>'
            '<p>Other benchmark roundups land in a similar range. ' + a(DANISH, 'One agency\'s summary of published benchmarks') + ' puts enterprise-focused reps at roughly 8 to 15 qualified meetings a month and high-velocity, small-deal teams far higher. So if someone tells you "10 a month", the right reply is: "10 of what kind of meeting, in what market?"</p>'
        )),
        ('meeting-definition', 'Why your meeting definition decides the number', (
            '<p>The meeting definition is the biggest single driver of the target. An SDR who books any interested contact into a first call will book more meetings than one who must confirm role, need and timing first, and both can be doing excellent work.</p>'
            '<p>Most teams fall into one of three models:</p>'
            '<ul><li><b>Introductory meetings.</b> The SDR confirms basic fit and interest, and the account executive does the discovery. Higher volume, lower conversion to opportunity.</li>'
            '<li><b>Semi-qualified meetings.</b> The SDR confirms fit and a real problem before booking. A middle ground, and the most common model.</li>'
            '<li><b>Fully qualified meetings.</b> The SDR confirms the problem, the decision maker and a reason to act now. Fewer meetings, but most of them become opportunities.</li></ul>'
            '<p>None of these is right for every company. Introductory meetings suit a team with spare account executive time and a short sales cycle. Fully qualified meetings suit complex deals where an account executive\'s hour is precious.</p>'
            '<p>What matters is that the definition is written down and agreed by the SDR, the account executive and whoever reads the numbers. Write down:</p>'
            '<ul><li>the titles and company profile that count</li>'
            '<li>the problem the buyer must confirm</li>'
            '<li>what the SDR must learn before booking</li>'
            '<li>who decides whether a meeting was qualified, and by when</li></ul>'
            '<p>Without that, "how many meetings" becomes an argument. The SDR counts every booking, the account executive counts the ones worth their time, and nobody trusts the number. With it, you can pick a model, then use the benchmark for that model as a starting point.</p>'
        )),
        ('what-changes-it', 'What pushes the number up or down', (
            '<p>Beyond the meeting definition, the monthly number depends mostly on deal size, the number of accounts in your market, how warm the leads are, how many channels the rep uses and how much support they get. Two SDRs on very different numbers can both be performing well.</p>'
            + fig2 +
            '<p>A few of these deserve a closer look:</p>'
            '<ul><li><b>Market size.</b> If only a few hundred companies can buy from you, every account matters and the right pace is slower and more researched. Pushing for volume burns the market you have.</li>'
            '<li><b>Channels.</b> The Bridge Group found that phone-centric teams average about 4.6 quality conversations a day, against 3.4 for email-centric teams. Reps who call as well as write tend to have more chances to book.</li>'
            '<li><b>Activity is not the goal.</b> The median SDR logs about 112 activities a day across phone, email, LinkedIn and text, yet has only about 4 quality conversations. A target built on meetings, not activities, keeps attention on conversations that count.</li>'
            '<li><b>Support.</b> A rep who must build lists, research accounts and write every sequence alone will book fewer meetings than one who starts each day with researched accounts and approved messaging.</li></ul>'
            '<p><b>Inbound versus outbound.</b> An SDR who follows up on demo requests and content downloads works with buyers who already raised a hand, so more of their conversations turn into meetings. An SDR doing pure cold outbound starts every conversation from zero. If your rep does both, track the two sources separately, or a good inbound month will hide a weak outbound one and the other way round.</p>'
            '<p>Use the table to adjust the benchmark up or down for your situation. A rep selling a large, committee-driven deal into a small market should not be compared with a rep selling a quick, single-buyer product to thousands of companies.</p>'
        )),
        ('ramp', 'How many meetings to expect from a new SDR', (
            '<p>A new SDR will not book a full month of meetings in their first month. The Bridge Group puts average SDR ramp time at about 3 months, so plan for a reduced target in months one and two and the full number from about month three or four.</p>'
            + fig3 +
            '<p>Ramp time has improved: the 2025 report shows the shortest average ramp since 2010, and average SDR tenure has risen to about 1.9 years. That still leaves a short window. If ramp takes a quarter of a year and tenure is under two years, every week saved in ramp is a week of full productivity gained.</p>'
            '<p>How to set targets during ramp:</p>'
            '<ul><li><b>Month one: learning targets.</b> Product knowledge, buyer research, call practice and the first sequences approved. Count conversations and feedback, not meetings.</li>'
            '<li><b>Month two: a partial meeting target.</b> Enough to show the rep can turn conversations into meetings. Review each booked meeting with the account executive.</li>'
            '<li><b>Month three: most of the target.</b> The rep should be close to full pace on a stable segment and message.</li>'
            '<li><b>After ramp: the full target.</b> Now the number is a fair test of the rep, not of your onboarding.</li></ul>'
            '<p>A structured first 90 days shortens ramp. Our <a href="/blog/sdr-onboarding-plan">SDR onboarding plan</a> walks through it week by week.</p>'
        )),
        ('held-not-booked', 'Count held, accepted meetings, not bookings', (
            '<p>The meeting that counts is the one that was held and accepted by the account executive as fitting your definition. Booked meetings that never happen, or happen with the wrong person, look good on a dashboard and add nothing to pipeline.</p>'
            '<p>That is why The Bridge Group measures quota as meetings held and meetings converted, not meetings set. It also changes behavior. A rep paid on bookings has every reason to fill the calendar. A rep measured on held and accepted meetings has every reason to confirm the meeting, send a short agenda and make sure the right person attends.</p>'
            '<p>No-shows are the gap between the two. A ' + a(REVENUEHERO, 'RevenueHero benchmark of 6,428 B2B meetings') + ' found an overall no-show rate of 6.5%, but it ranged from almost zero in some industries to 15% or more in others. If your no-show rate is well above your industry\'s, look at how meetings are being booked before you look at volume.</p>'
            '<p>A simple monthly scorecard for an SDR:</p>'
            '<ul><li><b>Meetings held</b> that match the written definition.</li>'
            '<li><b>Meetings accepted</b> by the account executive after the call.</li>'
            '<li><b>Opportunities created</b> from those meetings.</li>'
            '<li><b>No-show rate,</b> as a quality check on how meetings are booked.</li>'
            '<li><b>Quality conversations</b> per day, as an early signal before meetings move.</li></ul>'
            '<p>The 2025 median of 6 converted meetings a month is a useful second benchmark. If your rep books plenty of meetings but very few convert, the problem is usually targeting or qualification, not effort.</p>'
        )),
        ('set-your-target', 'How to set the right target for your team', (
            '<p>Set the target by working backwards from the pipeline your sales team needs, then check it against the benchmark for your meeting definition. If the two numbers are far apart, change the plan or the number of reps rather than asking one SDR to close the gap.</p>'
            '<ol><li><b>Start from pipeline.</b> How many new opportunities does the sales team need each month to hit its goals?</li>'
            '<li><b>Use your own conversion.</b> What share of held meetings turn into opportunities today? If you have no history, start with the benchmark ratio of 6 converted from 10 held and replace it with your own data after a quarter.</li>'
            '<li><b>Work out held meetings.</b> Divide needed opportunities by the conversion rate to get the held meetings you need.</li>'
            '<li><b>Compare with one rep\'s capacity.</b> If the answer is far above what one fully ramped rep books in your model, you need more reps, better targeting or more inbound, not a bigger quota.</li>'
            '<li><b>Ramp it.</b> Apply the ramped target for new reps.</li>'
            '<li><b>Review quarterly.</b> As data replaces assumptions, adjust the target and the definition.</li></ol>'
            '<p>The ' + a(QUOTAPATH, 'QuotaPath summary of earlier Bridge Group research') + ' notes that real SDR quotas range from two highly qualified opportunities a month to dozens of introductory demos. Both can be right. A target that comes from your own funnel will be fairer to the rep and far more useful to you than any number borrowed from another company.</p>'
            '<p>Finally, watch the trend more than the single month. One slow month after a holiday or a market change is noise. Three slow months in a row on a stable segment is a signal to look at targeting, messaging, the rep or the definition.</p>'
        )),
        ('hire-for-it', 'Hiring an SDR who can hit the number', (
            '<p>The SDRs who reach target reliably share a few traits: clear spoken and written English, comfort on the phone with US buyers, curiosity about the customer\'s business and the discipline to follow up. Test for those in the interview, not just for confidence.</p>'
            '<p>What to look for, and how to check it:</p>'
            '<ul><li><b>Phone skill.</b> Run a short cold call roleplay with a real objection. You learn more in five minutes than from the whole CV.</li>'
            '<li><b>Writing.</b> Ask for a first email to one of your target accounts. Look for a specific reason to write, not a template.</li>'
            '<li><b>Qualification judgment.</b> Describe a borderline prospect and ask whether they would book the meeting. Their answer shows whether they understand your definition.</li>'
            '<li><b>Hours.</b> A rep who works your business day can call buyers when they answer. Latin America sits inside the US business day, so a rep there works your hours, not a night shift.</li></ul>'
            '<p>Our guide to <a href="/blog/sdr-interview-process">the 20 minute SDR screen</a> covers the full process.</p>'
            '<p><b>How we help.</b> Our <a href="/talent">talent team</a> places vetted bilingual sales professionals from Latin America with US companies. Every candidate is interviewed in English by our sales team and roleplayed on a live cold call before you meet them. Tell us your meeting definition and the hours you need covered, and you get three profiles within 72 hours. You interview them yourself, and if the rep does not work out in the first 30 days, we replace them.</p>'
        )),
    ],
    'conclusion': (
        '<p>There is a useful benchmark for SDR meetings, but there is no universal number. The right target comes from your meeting definition, your market and your own funnel.</p>'
        '<ol><li><b>Start from the benchmark:</b> a median of about 10 held meetings and 6 converted meetings a month per SDR.</li>'
        '<li><b>Write the meeting definition down</b> and pick the benchmark for that model: introductory, semi-qualified or fully qualified.</li>'
        '<li><b>Adjust for your situation:</b> deal size, market size, lead source, channels and support.</li>'
        '<li><b>Ramp new reps</b> over about three months before judging them on the full number.</li>'
        '<li><b>Count held, accepted meetings,</b> and watch no-shows and conversion to opportunity.</li>'
        '<li><b>Set the target from pipeline backwards,</b> and review it every quarter.</li></ol>'
        '<p>When you are ready to add a rep, <a href="/talent">request profiles</a> and we will send three interviewed, bilingual SDRs within 72 hours.</p>'
    ),
    'faq': [
        ('How many meetings should an SDR book per month?',
         'A typical target is about 10 held meetings a month. The Bridge Group\'s 2025 study of 351 B2B companies found a median quota of 10 meetings held and 6 converted into qualified opportunities. Your number depends on how strictly you define a meeting.'),
        ('Is 10 meetings a month good for an SDR?',
         'For a semi-qualified meeting definition, 10 held meetings a month is right at the median. For introductory meetings it is below the median of 16, and for fully qualified meetings it is slightly above the median of 9.'),
        ('Should SDR quota be based on meetings booked or meetings held?',
         'Meetings held, and ideally accepted by the account executive. Booked meetings that never happen or do not fit your definition add nothing to pipeline, and measuring bookings encourages reps to fill the calendar instead of qualifying.'),
        ('How long before a new SDR books a full month of meetings?',
         'Usually about three months. The Bridge Group puts average SDR ramp time at about 3 months, so set learning goals in the first month, a partial meeting target in the second and most of the full target in the third.'),
        ('What is a good meeting to opportunity conversion rate for SDRs?',
         'There is no single standard. As a rough guide, The Bridge Group medians are 10 held and 6 converted meetings a month, which suggests teams expect a bit more than half of held meetings to become opportunities. Replace that with your own data once you have a quarter of history.'),
        ('Why are my SDRs missing their meeting quota?',
         'Common causes are a target not based on your own funnel, a vague meeting definition, a list that is too broad, weak messaging or a rep still ramping. Only 60% of SDRs were at quota in the 2025 Bridge Group study, so check the target before blaming the rep.'),
        ('How many calls and emails does an SDR need to book a meeting?',
         'It varies widely by market and channel. The median SDR logs about 112 activities a day for about 4 quality conversations, according to The Bridge Group. Track quality conversations and held meetings rather than raw activity counts.'),
    ],
}
