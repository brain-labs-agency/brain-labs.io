# Spec for blog/hire-appointment-setters.html. Build: python3 tools/blogkit.py tools/posts/hire-appointment-setters.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


HBR = 'https://scholarsarchive.byu.edu/facpub/9711'
HBR_SUMMARY = 'https://www.smartcompany.com.au/marketing/20110704-are-you-letting-online-leads-go-cold/'
GONG = 'https://www.gong.io/blog/cold-call-stats'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
TSR = 'https://hunton.com/insights/legal/telemarketing-sales-rule-changes-remove-exception-for-business-to-business-calls-and-impose-new-recordkeeping-requirements'
GARTNER_2025 = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'

fig1 = figure(1, table(['', 'Appointment setter', 'SDR', 'Closer or AE'], [
    ['<b>Main job</b>', 'Turn leads and lists into booked, confirmed meetings', 'Find, research and open new accounts, then qualify', 'Run the sales conversation and close'],
    ['<b>Starts from</b>', 'Inbound leads, event lists, a list you provide', 'An ideal customer profile and research', 'A qualified meeting'],
    ['<b>Main channel</b>', 'Phone first, plus email and text follow up', 'Email, phone and LinkedIn together', 'Video calls and demos'],
    ['<b>Measured on</b>', 'Meetings held and show rate', 'Qualified pipeline created', 'Revenue closed'],
    ['<b>Key skill</b>', 'Speed, phone presence, follow through', 'Research, writing, judgment on fit', 'Discovery, negotiation'],
]), 'How an appointment setter differs from an SDR and a closer. Many companies blur the titles; decide which job you need before you write the ad.')

fig2 = figure(2, bar_chart('How fast US companies responded to a new web lead', [
    ('Within an hour', 37),
    ('1 to 24 hours', 16),
    ('More than 24 hours', 24),
    ('Never responded', 23),
], unit='%', vmax=50, highlight=('Within an hour',)),
    'An audit of 2,241 US companies that received a test lead through their website. Fewer than 4 in 10 called back within an hour, and almost a quarter never responded. Source: '
    + a(HBR, 'Harvard Business Review, "The Short Life of Online Sales Leads"') + ', as summarized by ' + a(HBR_SUMMARY, 'SmartCompany') + '.')

fig3 = figure(3, steps('A hiring process for appointment setters', [
    ('Scope', 'job, hours, leads'),
    ('Written test', 'one follow up email'),
    ('Phone screen', '20 minutes, live'),
    ('Roleplay', 'a real call, recorded'),
    ('You decide', 'meet the finalists'),
], accent=('Roleplay',)),
    'Five steps that test the job itself, not the CV. The roleplay (amber) is the step most teams skip and the one that predicts performance best.')

POST = {
    'slug': 'hire-appointment-setters',
    'title': 'Hiring appointment setters: what to look for and what to avoid',
    'h1': 'Hiring appointment setters: what to look for and what to <em>avoid</em>',
    'description': 'How to hire an appointment setter for a US B2B team: what the role is and is not, when you need one, the skills that predict success, red flags in candidates and offers, a five-step screening process and how to set up the first 30 days.',
    'category': 'Hiring',
    'date': '2026-11-20',
    'date_label': 'November 20, 2026',
    'hero_img': 'cover-hire-appointment-setters',
    'card_img': 'cover-hire-appointment-setters',
    'card_title': 'Hiring appointment setters: what to look for and what to avoid',
    'card_text': 'The skills that predict booked meetings that actually happen, the red flags to screen out, and a five-step process.',
    'takeaways': [
        'An appointment setter turns leads and lists into confirmed meetings for your closers. The job is speed, phone presence and follow through, which is different from an SDR who researches and opens new accounts.',
        'Hire for listening and clarity on the phone, strong written English, reliability with a CRM and the habit of confirming every meeting. Confidence alone is not enough.',
        'Avoid candidates who only talk about volume, offers built on booked meetings rather than meetings held, and anyone who is comfortable stretching the truth to get a yes.',
        'Test the job, not the CV: a short written task, a live phone screen and a recorded roleplay of a real call, followed by a clear first 30 days measured on show rate and fit.',
    ],
    'intro': (
        '<p>"Hire appointment setters" is one of the most common searches from US companies that have more leads than their closers can call. It is also one of the easiest roles to hire badly. The job looks simple from the outside, and plenty of candidates are confident on the phone. The difference between a setter who fills calendars with real buyers and one who fills them with no-shows only becomes clear a month in.</p>'
        '<p>This guide covers what an appointment setter actually does, when you need one, the skills that predict success, the red flags to avoid in both candidates and offers, a five-step screening process and how to set the role up so the meetings it books are worth taking.</p>'
    ),
    'cta': {
        'inline_lead': 'Need a setter who sounds right on a US call?',
        'inline_text': 'Tell us your market, your leads and the US hours you need covered. We send three bilingual sales professionals from Latin America, interviewed in English and roleplayed on a live call, within 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Setters who book meetings that <em>actually happen</em>.',
        'band_text': 'Vetted bilingual sales professionals from Latin America, working your US hours. Every candidate is interviewed in English and roleplayed on a live call before you meet them. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('what-they-do', 'What an appointment setter does (and what they do not)', (
            '<p>An appointment setter contacts leads, qualifies them against a few simple criteria and books a confirmed meeting with someone on your team who can sell. Their output is a meeting that happens with the right person, not a sale and not a long list of calls made.</p>'
            '<p>In practice, most of the day goes to four things:</p>'
            '<ul><li><b>Calling new leads fast,</b> whether they came from your website, an event, a webinar or a list.</li>'
            '<li><b>Asking a short set of qualifying questions,</b> such as role, company size, timing and the problem they want to solve.</li>'
            '<li><b>Booking and confirming the meeting,</b> with a calendar invite, a reminder and a short note for the closer.</li>'
            '<li><b>Following up</b> with everyone who did not answer, asked to be called later or missed their slot.</li></ul>'
            '<p>The title gets used loosely, so it helps to compare it with the roles next to it:</p>'
            + fig1 +
            '<p>The main difference with an SDR is where the work starts. A setter usually works leads that already exist. An SDR builds pipeline from scratch: picking accounts, researching them and writing outreach that gives each buyer a reason to reply. If what you need is new accounts from an ideal customer profile, read our guide to <a href="/blog/hire-bilingual-sdr-latin-america">hiring an SDR</a> instead. Many teams hire a setter, then find they need an SDR, because the lead flow dried up.</p>'
            '<p>The difference with a closer is just as important. A setter should not be selling the product. Their job is to find out whether a conversation is worth everyone\'s time and to make it happen. When setters start pitching, meetings get longer to book and buyers arrive with the wrong expectations.</p>'
        )),
        ('when-to-hire', 'When you need an appointment setter', (
            '<p>You need an appointment setter when leads are arriving faster than your team can call them, or when your closers spend a large part of their day chasing people to get on a call. In both cases the cost of waiting is lost buyers, not just lost time.</p>'
            '<p>Speed to lead is the clearest reason. A widely cited ' + a(HBR, 'Harvard Business Review study') + ' audited 2,241 US companies by sending each one a test lead through its website. Only 37% responded within an hour, and the average response time among those that replied was 42 hours. A related analysis of 1.25 million leads found that firms that contacted a lead within an hour were nearly seven times as likely to qualify it as firms that waited even one hour longer.</p>'
            + fig2 +
            '<p>The study is from 2011 and buyers have changed since, but the logic has not: interest fades quickly, and the first company to have a real conversation has the advantage.</p>'
            '<p>Other signs you are ready for a setter:</p>'
            '<ul><li><b>Closers are doing their own scheduling.</b> Every hour they spend chasing a reply is an hour they are not closing.</li>'
            '<li><b>Leads sit unworked over weekends or outside office hours,</b> or in time zones your team does not cover.</li>'
            '<li><b>You run events or webinars</b> and the attendee list gets a single email that nobody follows up.</li>'
            '<li><b>No-shows are high</b> because nobody confirms meetings the day before.</li></ul>'
            '<p>If none of these are true and the real problem is that you do not have enough leads, a setter will not fix it. You need outbound pipeline generation first, either an SDR or a service built to find and open new accounts.</p>'
        )),
        ('what-to-look-for', 'What to look for in an appointment setter', (
            '<p>Look for someone who listens well, sounds clear and calm on the phone, writes short and correct follow ups, and never lets a lead or a booked meeting slip. Those four habits predict meetings held far better than charm or years of experience.</p>'
            '<p><b>Listening on the phone.</b> Good setters ask a question and then stop talking. They pick up on what the buyer said and respond to it, instead of reading the next line of a script. Gong\'s ' + a(GONG, 'analysis of cold calls') + ' found that successful calls last nearly twice as long as unsuccessful ones, which usually means the setter earned a real conversation.</p>'
            '<p><b>A clear reason for the call.</b> The same Gong research found that calls where the rep stated the reason for calling had a 2.1x higher success rate, while opening with "Did I catch you at a bad time?" made a meeting 40% less likely. Listen for whether a candidate gets to the point in the first sentence.</p>'
            '<p><b>Strong written English.</b> Half the job is written: confirmation emails, follow ups, notes for the closer, text reminders. A setter whose emails are long, vague or full of mistakes will lose meetings they won on the phone.</p>'
            '<p><b>Follow through.</b> The best setters are organized. They log every call in the CRM, keep a clean callback list, confirm every meeting the day before and tell the closer anything useful they learned.</p>'
            '<p><b>Resilience without pushiness.</b> Most calls end in voicemail or a no. You want someone who stays steady through that and keeps quality up on call fifty, without pressuring people into meetings they do not want.</p>'
            '<p><b>Judgment on fit.</b> A setter who books anyone who says yes fills your closers\' calendars with the wrong people. Ask candidates when they would choose not to book a meeting. A good answer shows they understand who the meeting is for.</p>'
        )),
        ('what-to-avoid', 'Red flags: what to avoid in candidates and offers', (
            '<p>Avoid setters who measure themselves only by volume, offers that pay for meetings booked rather than meetings held, and anyone comfortable bending the truth to get a yes. These are the patterns behind full calendars and empty pipelines.</p>'
            '<p><b>In candidates:</b></p>'
            '<ul><li><b>Volume bragging.</b> "I made 200 dials a day" says nothing about results. Ask how many of the meetings they booked actually happened and how many turned into opportunities.</li>'
            '<li><b>Talking over the buyer.</b> In the roleplay, candidates who pitch for a full minute before asking anything will do the same with your leads.</li>'
            '<li><b>Vague answers about tools.</b> If they cannot describe how they kept track of callbacks and follow ups, they probably did not.</li>'
            '<li><b>Stretching the truth.</b> Watch for candidates who suggest saying the buyer "requested a call" when they did not, or implying an existing relationship. Beyond the damage to your reputation, the FTC\'s 2024 changes to the Telemarketing Sales Rule ' + a(TSR, 'extended its ban on misrepresentations to business-to-business calls') + '. Your setter\'s words are your company\'s words.</li></ul>'
            '<p><b>In offers and setups:</b></p>'
            '<ul><li><b>Paying for meetings booked.</b> If a setter or a provider is rewarded for bookings, you will get bookings. Tie results to meetings held with people who match your criteria.</li>'
            '<li><b>No qualifying criteria.</b> If you have not written down what makes a lead worth a meeting, the setter will guess, and every guess will be different.</li>'
            '<li><b>No hours overlap.</b> A setter calling US leads from a time zone that only overlaps a couple of hours with your buyers will miss the moments that matter. We compare the options in <a href="/blog/nearshore-vs-offshore-sales-teams">nearshore vs offshore sales teams</a>.</li>'
            '<li><b>Irrelevant outreach.</b> Gartner found that ' + a(GARTNER_2025, '73% of B2B buyers actively avoid suppliers who send irrelevant outreach') + '. A setter calling a stale list with no context can cost you buyers you will want later.</li></ul>'
        )),
        ('how-to-screen', 'How to screen appointment setters: a five-step process', (
            '<p>Screen appointment setters by testing the job itself: a short written task, a live phone screen and a recorded roleplay of a real call. CVs and job titles tell you very little about whether someone can book a meeting that happens.</p>'
            + fig3 +
            '<ol><li><b>Scope the role.</b> Write down where the leads come from, the qualifying questions, the hours that need coverage, the tools and what a good week looks like. This becomes both the job ad and the scorecard.</li>'
            '<li><b>Written test.</b> Send a short scenario: a lead who downloaded a guide and did not answer two calls. Ask for the follow up email. You learn more about their English and judgment in five sentences than in a cover letter.</li>'
            '<li><b>Phone screen.</b> Twenty minutes, on the phone, not video. You are hiring someone to sound good on a call, so judge them on one. Our <a href="/blog/sdr-interview-process">20-minute SDR screen</a> works for setters with small changes.</li>'
            '<li><b>Roleplay.</b> Play a real lead from your market: a little busy, a little skeptical, with one honest objection. Record it if the candidate agrees. Score how quickly they state the reason for the call, whether they ask before they pitch, how they handle the objection and whether they confirm the next step clearly.</li>'
            '<li><b>You decide.</b> Meet the finalists yourself. Ask each one what they would change about your qualifying questions after hearing about your buyers. The good ones will have an opinion.</li></ol>'
            '<p>If you are hiring for US buyers from outside the US, add one more check: listen for how the candidate handles fast, informal American English, interruptions and names they have not heard before. We cover this in detail in <a href="/blog/native-english-sales-team-latin-america">building a native-level English sales team</a>.</p>'
            '<p>On the BL Agency talent side, every candidate is interviewed in English by our sales team and put through a live cold call roleplay before they reach a client, and you interview them yourself before deciding.</p>'
        )),
        ('first-30-days', 'Setting up the first 30 days', (
            '<p>Set up the first 30 days around a written definition of a qualified meeting, a short call guide, clean lead routing and one number that matters: meetings held with the right people. A good setter with a vague setup will still fail.</p>'
            '<p><b>Week one: context.</b> Who you sell to, the problems you solve, the three most common objections and how your closers like to receive meetings. Have the setter listen to recorded calls from your best closers.</p>'
            '<p><b>Week two: supervised calls.</b> Start with real leads at a lower volume, with a manager listening to a sample each day and giving feedback the same day.</p>'
            '<p><b>Weeks three and four: full volume.</b> Track a short list of numbers weekly: speed to first call, contact rate, meetings booked, show rate and how many meetings the closers say fit the criteria. When show rate drops, look at confirmations first.</p>'
            '<p>Expect a learning curve. The ' + a(BRIDGE, 'Bridge Group\'s 2025 SDR report') + ', based on 351 B2B companies, puts average SDR ramp time at about three months and average tenure at 1.9 years. Setters working warm leads can ramp faster than SDRs building pipeline from scratch, but plan for coaching rather than instant results. For a fuller plan, see our <a href="/blog/sdr-onboarding-plan">SDR onboarding plan for the first 30, 60 and 90 days</a>.</p>'
            '<p>Finally, close the loop with your closers. Ask them every week which meetings were worth it and why. That feedback is how a setter learns your buyer faster than any script can teach.</p>'
        )),
        ('where-to-hire', 'Where to hire appointment setters', (
            '<p>You can hire appointment setters in house in the US, as freelancers, through an appointment setting company, or as dedicated reps through a nearshore talent partner. The right choice depends on how much control you want, how many hours you need covered and who will manage them day to day.</p>'
            '<ul><li><b>In-house, US based.</b> The most control and the closest cultural fit, with the longest hiring cycle and the full management load on your team.</li>'
            '<li><b>Freelancers.</b> Quick to start and flexible, but quality varies widely and they often split their time across several clients.</li>'
            '<li><b>Appointment setting companies.</b> They bring a team and a process. Check whether you get dedicated people, how meetings are counted and whether they work your leads or their own lists.</li>'
            '<li><b>Nearshore reps from Latin America.</b> Dedicated people who work inside your team and your tools, during US business hours. Latin America sits inside the US business day, so setters can call leads while they are still warm. Read more in <a href="/blog/hire-bilingual-cold-callers-latin-america">where to hire bilingual LatAm cold callers</a>.</li></ul>'
            '<p>Whichever route you choose, keep the same bar: test the job before you hire, define a qualified meeting in writing and measure meetings held. If you hire through a partner, ask how they screen. "We check English" is not the same as hearing the candidate on a live call with a skeptical buyer.</p>'
            '<p>BL Agency places bilingual sales professionals from Latin America with US companies. You tell us the role, the leads and the hours, and we send three candidates already interviewed in English and roleplayed on a call, within 72 hours.</p>'
        )),
    ],
    'conclusion': (
        '<p>A good appointment setter is one of the fastest ways to give closers more real conversations. A bad one fills calendars with meetings that never happen. The difference is almost always in how you define the role and how you test for it.</p>'
        '<ol><li><b>Know the job:</b> turn existing leads into confirmed meetings with the right people. It is not an SDR building pipeline from scratch, and it is not a closer.</li>'
        '<li><b>Hire when speed matters:</b> leads waiting hours or days, closers scheduling their own calls, high no-show rates.</li>'
        '<li><b>Look for the right habits:</b> listening, a clear reason for the call, strong written English, follow through and judgment on fit.</li>'
        '<li><b>Avoid the traps:</b> volume bragging, paying for bookings, no written criteria and anyone who bends the truth.</li>'
        '<li><b>Test the job:</b> a written follow up, a phone screen and a recorded roleplay.</li>'
        '<li><b>Set up the first month:</b> context, supervised calls, then full volume measured on show rate and fit.</li>'
        '<li><b>Pick the right source:</b> in house, freelance, agency or nearshore, with the same bar for all.</li></ol>'
        '<p>If you want setters who are already tested on a live call, <a href="/talent">request profiles</a> and we will send three within 72 hours.</p>'
    ),
    'faq': [
        ('What does an appointment setter do?',
         'An appointment setter contacts leads, asks a few qualifying questions and books confirmed meetings with someone on your team who can sell. They also follow up with leads who did not answer and confirm meetings so they actually happen.'),
        ('What is the difference between an appointment setter and an SDR?',
         'An appointment setter usually works leads that already exist, such as website leads or event lists, and focuses on booking meetings. An SDR builds pipeline from scratch by choosing accounts, researching them and writing outreach, then qualifies the replies.'),
        ('What skills should I look for in an appointment setter?',
         'Listening and clarity on the phone, a clear reason for every call, strong written English for follow ups, reliable CRM habits, steady resilience and good judgment about which leads deserve a meeting.'),
        ('How do I test an appointment setter before hiring?',
         'Use a short written test, such as a follow up email to a lead who did not answer, a 20-minute phone screen and a recorded roleplay of a real call from your market. These show more than a CV.'),
        ('Should I pay appointment setters per meeting booked?',
         'Rewarding bookings tends to produce bookings, including meetings that do not happen or do not fit. Tie results to meetings held with people who match your written criteria.'),
        ('How long does it take a new appointment setter to ramp?',
         'Setters working warm leads often get productive faster than SDRs building pipeline from scratch. Still, plan for a few weeks of context and supervised calls, and coaching after that. The Bridge Group puts average SDR ramp time at about three months.'),
        ('Can I hire appointment setters from Latin America for US buyers?',
         'Yes. Latin America shares most of the US business day, so setters can call leads while they are warm. Test spoken English on a live call and written English with a follow up email before you hire.'),
    ],
}
