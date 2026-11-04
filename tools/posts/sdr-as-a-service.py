# Spec for blog/sdr-as-a-service.html (long-form rewrite at the same URL). Build: python3 tools/blogkit.py tools/posts/sdr-as-a-service.py
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
G_REPFREE = 'https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience'
G_VALIDATE = 'https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights'
G_AGENTIC = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027'
GOOGLE = 'https://support.google.com/a/answer/81126'

fig1 = figure(2, bar_chart('Bridge Group 2025: ramp versus average tenure for an in-house SDR (months)', [
    ('Ramp to full productivity', 3.0),
    ('Average SDR tenure', 22.8),
], unit=' mo', vmax=26, highlight=('Ramp to full productivity',)),
    f'The average SDR spends about 3 of roughly 23 months ramping, and 60% of SDRs reached quota in 2025, the lowest share in the study\'s history. Tenure of 1.9 years shown in months. Survey of 351 B2B companies. Source: {a(BRIDGE25, "The Bridge Group, 2025 SDR Metrics Report")}.')

fig2 = figure(3, table(['', 'In-house SDR', 'AI SDR tool', 'SDR as a Service'], [
    ['<b>Who builds the system</b>', 'You', 'You configure the software', 'The provider'],
    ['<b>Who writes and approves messages</b>', 'Your rep, coached by you', 'The software, often unreviewed', 'The provider, ideally with a named reviewer'],
    ['<b>Time to first outreach</b>', 'Hiring plus ramp', 'Fast to start, slow to tune', 'Weeks, once domains are warm'],
    ['<b>Who manages day to day</b>', 'A sales leader on your team', 'Whoever has time', 'The provider'],
    ['<b>What you keep if you stop</b>', 'The person and their knowledge', 'The tool and its settings', 'The lists, messaging and data, if the contract says so'],
    ['<b>Best fit</b>', 'Proven outbound motion you want to scale', 'Large markets and a reviewer in house', 'Testing or running outbound without building a team'],
]), 'Three ways to get outbound done. The right one depends on whether you already have a working system and someone to own quality.')

fig3 = figure(1, steps('How an SDR as a Service program runs, from brief to booked meeting', [
    ('Brief', 'offer and ICP'),
    ('Setup', 'domains, warm-up'),
    ('Research', 'accounts, signals'),
    ('Outreach', 'drafted, approved'),
    ('Replies', 'sorted, answered'),
    ('Meeting', 'booked, briefed'),
], accent=('Outreach',)),
    'Six stages every program goes through. The outreach stage (amber) is where quality is won or lost, so ask who approves each message before it is sent.')

POST = {
    'slug': 'sdr-as-a-service',
    'title': 'What is SDR as a Service? How the model works in 2026',
    'h1': 'What is SDR as a <em>Service</em>? How the model works in 2026',
    'description': 'SDR as a Service means an outside team builds and runs your outbound and books meetings for your closers. What it includes, how it compares to hiring in house or buying an AI SDR, and how to choose a provider.',
    'category': 'Guide',
    'date': '2026-11-04',
    'date_label': 'November 4, 2026',
    'hero_img': 'blog-sdr',
    'card_img': 'blog-sdr',
    'card_title': 'What is SDR as a Service? How the model works in 2026',
    'card_text': 'What it includes, how it compares to hiring in house or buying an AI SDR, and what to ask a provider.',
    'takeaways': [
        'SDR as a Service means an outside team builds and runs your outbound, from list to booked meeting, and your own team only shows up for the sales call.',
        'It replaces the slowest part of hiring an SDR: recruiting, ramp and building the system. The Bridge Group puts average SDR ramp at about three months.',
        'In 2026 there are three versions: a human team, an AI tool sold as a service, and a hybrid where AI agents do the volume work and a person approves every message.',
        'Before you sign, ask who approves each email, what counts as a qualified meeting, how volume is set and what you keep if you stop.',
    ],
    'intro': (
        '<p>Most B2B companies grow on referrals and founder networks until those slow down. At that point the usual answer is to hire a sales development rep, someone whose whole job is to find new buyers and book first meetings. SDR as a Service is the other answer: instead of hiring that person and building the system around them, you hand the outbound function to a team that already runs it.</p>'
        '<p>The term covers very different offers, from a few offshore callers to fully automated AI tools. This guide explains what the model actually is, what a good program includes, how it compares to hiring in house, the three versions you will be pitched in 2026, and the questions that separate a real partner from a list vendor.</p>'
    ),
    'cta': {
        'inline_lead': 'Thinking about outsourcing outbound?',
        'inline_text': 'Book a 30 minute call and we will show you how the Agent Base runs outbound with six AI agents and a dedicated Agent Base manager who approves every email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound done for you, with a person <em>signing off</em>.',
        'band_text': 'Six AI agents research, draft, send and sort. Your dedicated Agent Base manager approves every email before it reaches a buyer, and you watch it all on a live dashboard.',
    },
    'sections': [
        ('definition', 'What SDR as a Service means', (
            '<p>SDR as a Service means an outside team builds and runs your outbound prospecting and delivers booked meetings to your sales team. You get the research, outreach, reply handling and scheduling as a service, instead of hiring, training and managing SDRs yourself.</p>'
            '<p>It helps to start with the role it replaces. A sales development rep sits at the top of the funnel. They find companies that fit your ideal customer, research the right person, reach out by email, phone or LinkedIn, handle the replies and hand qualified meetings to an account executive who runs the sales process. The Bridge Group\'s ' + a(BRIDGE25, '2025 SDR Metrics Report') + ' found the most common setup is one SDR supporting about two account executives.</p>'
            '<p>SDR as a Service takes that whole function and moves it outside your company. The provider brings the people or the agents, the tools, the sending infrastructure and the process. You bring three things: a clear offer, a definition of who you sell to and someone to take the meetings.</p>'
            '<p>The model goes by several names. You will see outsourced SDR, outsourced sales development, appointment setting and lead generation agency used almost interchangeably. They overlap, but they are not the same:</p>'
            '<ul><li><b>Lead generation</b> often stops at a list of contacts or a set of replies. You do the rest.</li>'
            '<li><b>Appointment setting</b> books meetings, usually by phone, often with a looser definition of who qualifies.</li>'
            '<li><b>SDR as a Service</b> owns the full outbound motion: targeting, messaging, sending, replies and the handoff, and it is judged on qualified meetings, not activity.</li></ul>'
            '<p>The difference matters when you compare offers, because two providers using the same label can be selling very different amounts of work.</p>'
        )),
        ('included', 'What a good program includes', (
            '<p>A complete SDR as a Service program covers six things: targeting, infrastructure, research, outreach, reply handling and the meeting handoff. If a proposal is missing one of them, you will end up doing that part yourself.</p>'
            '<p><b>Targeting.</b> A clear ideal customer profile and a list built against it. Good providers push back here, because a vague target produces vague emails. Expect questions about your best current clients and why they bought.</p>'
            '<p><b>Sending infrastructure.</b> Separate domains and mailboxes set up for outreach and warmed before anything goes out, so your main domain is protected. Mailbox providers watch complaint rates closely. ' + a(GOOGLE, 'Google\'s sender guidelines') + ' ask bulk senders to keep their reported spam rate below 0.3%, and a program that ignores that will see its emails stop reaching the inbox.</p>'
            '<p><b>Account research.</b> A reason to write to each company now: a hiring push, a new location, a funding round, a product launch. This is what makes the first line of an email specific instead of generic.</p>'
            '<p><b>Outreach across channels.</b> Messages written for each channel your buyers use: email first for most B2B programs, with LinkedIn and phone where they fit. Follow ups on a schedule, not when someone remembers.</p>'
            '<p><b>Reply handling.</b> Every reply read and sorted the same day. Out of office, wrong person and unsubscribe are easy. The interested and the "maybe next quarter" replies need a person who can answer well and fast.</p>'
            '<p><b>The handoff.</b> A meeting on your calendar with a short brief: who the person is, why they were contacted, what they said and what to ask. Plus reporting you can actually read, ideally live rather than a monthly PDF.</p>'
            '<p>One thing a good program does not include is a promise of a fixed number of meetings before anyone has tested your offer. Volume promises made before the first send usually turn into loose definitions of what counts as a meeting.</p>'
        )),
        ('how-it-runs', 'How a program runs, week to week', (
            '<p>A program moves from a brief to warmed infrastructure to live outreach, and then runs as a weekly loop of research, sending, replies and adjustments. The first weeks are setup; results come from the loop, not the launch.</p>'
            + fig3 +
            '<p><b>The brief.</b> The provider learns your offer, your best clients, the objections your closers hear and what a qualified meeting means for you. Write that definition down before launch. Most disputes between companies and outbound providers are really disputes about what counted as a meeting.</p>'
            '<p><b>Setup.</b> Domains and mailboxes are created and warmed, the target list is built and the first message angles are drafted for your approval. Nothing should go to a buyer until you have seen what it will say in your name.</p>'
            '<p><b>The weekly loop.</b> Research and drafting run continuously. Approved emails go out at a pace the domains can carry. Replies are sorted and answered. Each week the team looks at which segments and angles are getting positive replies and shifts effort toward them.</p>'
            '<p><b>The handoff.</b> Booked meetings land on your calendar with a brief. Your closer takes the call. Feedback on meeting quality goes back into the targeting, which is how the program gets better instead of just busier.</p>'
            '<p>Your part is small but not zero. Plan for a kickoff, quick approvals on early messaging and honest feedback after the first meetings. Programs where the client never reviews anything tend to drift.</p>'
        )),
        ('vs-in-house', 'SDR as a Service vs hiring an SDR in house', (
            '<p>Hiring in house gives you a person who learns your product deeply and stays inside your culture; SDR as a Service gives you a working system without the hiring, ramp and management. The right choice depends on whether you already have an outbound motion that works.</p>'
            '<p>An in-house hire is slower than it looks. You recruit, then the rep ramps. The Bridge Group\'s 2025 report puts average SDR ramp at 3.0 months and average tenure at 1.9 years, which means a meaningful share of every hire is spent getting up to speed. The same report found only 60% of SDRs reached quota, the lowest share in the study\'s history.</p>'
            + fig1 +
            '<p>The deeper problem is that a new SDR needs a system to work inside: a target list, sending infrastructure, tested messaging, a definition of a qualified meeting and someone to coach them. If none of that exists, you are asking one junior person to build an outbound function and run it at the same time.</p>'
            + fig2 +
            '<p><b>Hire in house when</b> you already know which segments respond, have messaging that books meetings and have a sales leader with time to coach.</p>'
            '<p><b>Use a service when</b> outbound is unproven for your offer, you want results before you commit to headcount, or nobody on your team has time to manage an SDR.</p>'
            '<p>Many companies do both in sequence: a service proves the motion, and once the targeting and messaging work, they hire people to run it. If you go that route, make sure the contract lets you keep the lists, templates and learnings.</p>'
        )),
        ('three-models', 'The three versions you will be pitched in 2026', (
            '<p>In 2026, SDR as a Service comes in three versions: a team of human SDRs, an AI tool sold as a service, and a hybrid where AI agents do the volume work and a person approves what goes out. The hybrid has become the default for good reason.</p>'
            '<p><b>Human SDR teams.</b> The classic model: a provider staffs reps who work your account, usually alongside other clients. Quality depends heavily on the individual rep and how many accounts they juggle. Research is often the first thing to slip when the week gets busy.</p>'
            '<p><b>AI SDR tools sold as a service.</b> Software that finds prospects, writes emails and sends them with little or no human review. These promise volume and speed. The weak point is that nobody checks a confident email written from bad data before a buyer reads it, and high volume strains the sending domains. In June 2025, ' + a(G_AGENTIC, 'Gartner predicted') + ' that over 40% of agentic AI projects will be canceled by the end of 2027, citing costs, unclear value and weak risk controls.</p>'
            '<p><b>Hybrid.</b> AI agents handle research, drafting, sending and reply sorting, and a named person reads and approves every message and handles interested buyers. This matches what buyers say they want. A ' + a(G_REPFREE, 'March 2026 Gartner survey') + ' found 67% of B2B buyers prefer to buy without a rep, yet ' + a(G_VALIDATE, 'Gartner\'s May 2026 follow up') + ' found 69% turn to sales reps to validate AI-generated insights. Buyers want fewer, better conversations, and they still want a person behind them.</p>'
            '<p>At BL Agency we run the hybrid version and call it the Agent Base. Six agents each own one job: <b>Scout</b> finds accounts with a reason to buy, <b>Lens</b> researches them, <b>Quill</b> drafts the emails, <b>Relay</b> sends at a safe pace, <b>Echo</b> sorts replies and <b>Atlas</b> writes the brief for your closer. The dedicated Agent Base manager approves every email before it is sent and is your single point of contact. You can watch the whole base work on a live dashboard.</p>'
        )),
        ('ready', 'Signs you are ready, and signs you are not', (
            '<p>You are ready for SDR as a Service when you know who your best clients are, your closers have time for more meetings and referrals alone no longer fill the pipeline. You are not ready if you cannot yet describe who you sell to or what problem you solve for them.</p>'
            '<p><b>Signs you are ready:</b></p>'
            '<ul><li>You have closed deals and can name the type of company that bought and why.</li>'
            '<li>Someone on your team can take discovery calls and close.</li>'
            '<li>Referrals and inbound are steady but not growing.</li>'
            '<li>You want to close deals, not build and manage an outbound team.</li>'
            '<li>Your deal size justifies a sales conversation, rather than a self-serve signup.</li></ul>'
            '<p><b>Signs you should wait:</b></p>'
            '<ul><li>You are still figuring out what you sell or to whom. Outbound amplifies a clear offer; it cannot find one for you.</li>'
            '<li>Nobody can take the meetings. Booked calls that sit unworked waste the buyer\'s interest and your budget.</li>'
            '<li>You expect results in the first two weeks. Setup and domain warm-up take time before the first email goes out.</li>'
            '<li>Your market is a handful of accounts you already know personally. Account-based selling by your own team may fit better.</li></ul>'
            '<p>If you sit somewhere in between, a short test on one or two segments is usually the right first step. It tells you whether outbound works for your offer before you commit to anything larger.</p>'
        )),
        ('questions', 'How to choose a provider: questions to ask', (
            '<p>Choose a provider on how they protect quality, not on how many emails they promise to send. The questions below expose the difference quickly.</p>'
            '<ol><li><b>Who reads each message before it is sent?</b> A name, not "our AI handles it". Ask to see examples of edits.</li>'
            '<li><b>What counts as a qualified meeting?</b> Agree on title, company fit and intent in writing before launch.</li>'
            '<li><b>How many emails per mailbox per day, and who sets that?</b> Volume should be set to protect the domain, not maximized.</li>'
            '<li><b>Whose domains are used?</b> Outreach should run on separate domains, never your main one.</li>'
            '<li><b>What happens to an interested reply in the first hour?</b> Speed and tone here decide whether a reply becomes a meeting.</li>'
            '<li><b>Where does the contact data come from, and how are stale records caught?</b></li>'
            '<li><b>Can I see the work live?</b> A dashboard you can open any day beats a monthly report.</li>'
            '<li><b>What do I keep if we stop?</b> Lists, messaging, reply data and learnings should be yours.</li></ol>'
            '<p>Also listen for what a provider does not say. Be careful with anyone who guarantees a number of meetings before seeing your offer, will not show you messages before they go out, or cannot explain how they handle a rising spam rate. Those are the patterns behind most bad outsourcing stories.</p>'
        )),
    ],
    'conclusion': (
        '<p>SDR as a Service is a way to get outbound running without hiring, ramping and managing a team first. Done well, it gives you a working system and qualified meetings; done badly, it gives you activity reports and a damaged domain.</p>'
        '<ol><li><b>Know what you are buying:</b> full outbound, not just a list or a dialer.</li>'
        '<li><b>Check the six parts:</b> targeting, infrastructure, research, outreach, replies and handoff.</li>'
        '<li><b>Compare it honestly with hiring:</b> a service fits best when outbound is unproven or nobody can manage an SDR.</li>'
        '<li><b>Prefer the hybrid:</b> AI agents for volume, a named person approving every message.</li>'
        '<li><b>Ask the hard questions</b> about review, meeting definitions, volume and ownership before you sign.</li></ol>'
        '<p>If you would like to see how the hybrid version works for your market, ' + a(CAL, 'book a call') + ' and we will walk you through the Agent Base on a live dashboard.</p>'
    ),
    'faq': [
        ('What does SDR as a Service mean?',
         'It means an outside team builds and runs your outbound prospecting: finding accounts, researching them, reaching out, handling replies and booking qualified meetings with your sales team. You skip hiring, training and managing your own SDRs.'),
        ('How is SDR as a Service different from appointment setting?',
         'Appointment setting usually focuses on booking calls, often by phone and with a looser definition of who qualifies. SDR as a Service owns the full outbound motion, from targeting and messaging to sending infrastructure and the handoff, and is judged on qualified meetings.'),
        ('Is SDR as a Service better than hiring an SDR?',
         'It depends on whether you already have an outbound system that works. A service is usually the better first step when outbound is unproven for your offer or nobody has time to manage a rep. Hiring makes sense once the targeting and messaging are proven and you have someone to coach.'),
        ('How long does it take to see results?',
         'Expect a setup period first, because domains and mailboxes need to be warmed before sending at volume. After launch, the first useful signal is which segments and messages get positive replies, and that shapes everything after.'),
        ('Will an outsourced SDR damage my email domain?',
         'It should not, if outreach runs on separate domains at a controlled volume. Ask any provider whose domains they use, how many emails each mailbox sends per day and what they do when the spam rate starts to rise.'),
        ('Can AI run SDR as a Service on its own?',
         'AI can run most of the volume work, including research, drafting, sending and reply sorting. Fully autonomous setups tend to fail on bad data and unreviewed emails, which is why the hybrid model keeps a person approving every message a buyer reads.'),
        ('What does the dedicated Agent Base manager do?',
         'In the BL Agency Agent Base, the dedicated Agent Base manager reads every email the agents draft, edits or approves it, handles replies that need a person and is your single point of contact.'),
    ],
}
