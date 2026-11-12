# Spec for blog/b2b-appointment-setting-companies-usa.html. Build: python3 tools/blogkit.py tools/posts/b2b-appointment-setting-companies-usa.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
SAASTR = 'https://www.saastr.com/only-7-of-you-have-really-gotten-outsourced-sdrs-to-work'
NOSHOW = 'https://focus-digital.co/average-no-show-rate-for-booked-sales-meetings-by-booking-channel/'
FTC_DNC = 'https://ftc.gov/business-guidance/resources/qa-telemarketers-sellers-about-dnc-provisions-tsr-0'
FCC_AI = 'https://wsgr.com/en/insights/fcc-rules-ai-generated-voices-are-artificial-under-the-tcpa.html'
FTC_SPAM = 'https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business'
GOOGLE = 'https://support.google.com/a/answer/14229414'

fig1 = figure(1, table(['Model', 'How it works', 'What it rewards', 'What to watch'], [
    ['<b>Dedicated SDR team</b>', 'One or more SDRs work your account on a monthly engagement, usually by phone and email.', 'Steady effort and learning over months.', 'How many other clients each rep works, and whether you see the replies.'],
    ['<b>Pay per appointment</b>', 'You are billed for each meeting that meets an agreed definition.', 'Volume of meetings that pass the definition.', 'A loose definition, weak follow up on no-shows, and messaging you never approved.'],
    ['<b>Campaign or project</b>', 'A fixed scope: one list, one offer, one period.', 'Fast tests of a segment or message.', 'Little product depth, and no time to learn from replies.'],
    ['<b>AI plus human review</b>', 'Software researches and drafts; a person approves before anything is sent.', 'Relevance and consistency at a steady pace.', 'Who approves, how often, and whether you can see each step.'],
]), 'The four models you will be pitched. None is right for every company. The last column is where most disappointments start, so ask about it first.')

fig2 = figure(2, bar_chart('No-show rate by booking channel (2026 compilation)', [
    ('Referral or partner intro', 12),
    ('Inbound, self-scheduled', 15),
    ('Cold email, SDR-booked', 36),
    ('Cold call, SDR-booked', 39),
    ('Outsourced appointment setter', 42),
], unit='%', vmax=50, highlight=('Outsourced appointment setter',)),
    f'Share of booked B2B meetings where the prospect neither attended nor cancelled, by how the meeting was booked. Treat these as directional: they come from a compilation of published datasets, not a single study. Source: {a(NOSHOW, "Focus Digital, 2026")}.')

fig3 = figure(3, steps('How to choose an appointment setting company in two weeks', [
    ('Shortlist', 'three providers'),
    ('Define', 'qualified meeting'),
    ('Sample work', 'calls and emails'),
    ('Pilot', 'one segment'),
    ('Judge', 'held meetings'),
], accent=('Judge',)),
    'A short selection path. The last step (amber) is the one that matters: judge each provider on meetings held with the right people, not on meetings booked.')

POST = {
    'slug': 'b2b-appointment-setting-companies-usa',
    'title': 'B2B appointment setting companies in the USA: how to choose one',
    'h1': 'B2B appointment setting companies in the USA: how to <em>choose</em> one',
    'description': 'How to choose a B2B appointment setting company in the USA: the four models, the qualified meeting definition, show rates, US calling and email rules, and a two-week way to compare providers.',
    'category': 'Outbound',
    'date': '2026-11-12',
    'date_label': 'November 12, 2026',
    'hero_img': 'blog-appointment-setting',
    'card_img': 'blog-appointment-setting',
    'card_title': 'B2B appointment setting companies in the USA: how to choose one',
    'card_text': 'The four models, show rates, US calling and email rules, and a two-week way to compare providers.',
    'takeaways': [
        'A B2B appointment setting company books first meetings between your sales team and qualified prospects. The model it uses (dedicated SDRs, pay per appointment, campaigns, or AI with human review) shapes what it is rewarded for.',
        'The meeting that matters is the one that happens with the right person. Compare providers on held meetings against a written definition, not on meetings booked.',
        'US rules still apply when someone else dials or sends: AI voices fall under the TCPA, and the FTC is clear you cannot contract away CAN-SPAM responsibility.',
        'Choose in two weeks: shortlist three, write the definition, ask for sample work on your buyer, pilot one segment and judge on what held.',
    ],
    'intro': (
        '<p>Search for B2B appointment setting companies in the USA and you get pages of providers that look the same: booked meetings, experienced callers, a calendar full of demos. The differences are in the details you cannot see on a landing page: how they define a meeting, who they call, what happens when a prospect does not show up, and whether their outreach makes your brand look good or careless.</p>'
        '<p>This guide explains what these companies actually do, the four business models you will be pitched, the rules every US provider should follow on phone and email, and a simple two-week process to compare three providers on real work. We run an outbound service ourselves, so we also say plainly where our model fits and where a classic appointment setter is the better choice.</p>'
    ),
    'cta': {
        'inline_lead': 'Comparing appointment setting providers?',
        'inline_text': 'Book a 30 minute call and see the Agent Base: AI agents research and draft, and a dedicated Agent Base manager approves every email before it reaches a buyer.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Meetings with the <em>right</em> people, approved by a person.',
        'band_text': 'Scout finds the accounts, Lens researches them, Quill drafts and Relay sends at a safe pace. Your dedicated Agent Base manager approves every message, and you watch it all on a live dashboard.',
    },
    'sections': [
        ('what-they-do', 'What a B2B appointment setting company does', (
            '<p>A B2B appointment setting company finds prospects that match your ideal customer, contacts them by phone, email or LinkedIn, and books a first meeting with your sales team. It owns the top of the funnel up to the meeting; your team runs the meeting and closes the deal.</p>'
            '<p>In practice the work breaks into five parts, and every provider does them with a different mix of people and software:</p>'
            '<ul><li><b>List building.</b> Choosing target accounts and the people inside them, ideally with a reason to talk now.</li>'
            '<li><b>Messaging.</b> Call openers, email sequences and LinkedIn notes written for your buyer.</li>'
            '<li><b>Outreach.</b> Dials, emails and follow ups, at a pace that does not burn your domains or your reputation.</li>'
            '<li><b>Qualification.</b> Confirming on the call or by reply that the person fits your definition before a meeting is booked.</li>'
            '<li><b>Handover.</b> A calendar invite, a short brief on the account and a reminder so the meeting actually happens.</li></ul>'
            + fig1 +
            '<p>The model matters because it decides what the provider is rewarded for. A pay per appointment provider earns on meetings that pass the definition, so the definition becomes the whole contract. A dedicated SDR team earns on time, so the question is how much of that time goes to your account. Neither is wrong. Each one needs a different set of questions, which we cover below.</p>'
            '<p>One more thing to know before the first call: appointment setting is a narrower service than a full outbound program. Some providers only book meetings and hand you a calendar; others also give you the replies, the objections and what each segment said. If you want to learn from the market as well as fill calendars, ask for the second kind.</p>'
        )),
        ('qualified-meeting', 'Start with a written definition of a qualified meeting', (
            '<p>The single most useful thing you can do before choosing a provider is write down what a qualified meeting means for you. Without it, you cannot compare providers, you cannot judge a pilot, and most disputes later will be arguments about what should have counted.</p>'
            '<p>A good definition fits on half a page and covers four things:</p>'
            '<ul><li><b>Who.</b> The titles or roles that count, and the ones that do not. "VP of Operations or Director of Logistics" is a definition; "a decision maker" is not.</li>'
            '<li><b>Which companies.</b> Industry, size, region and any exclusions, such as current customers or competitors.</li>'
            '<li><b>Why now.</b> The problem or trigger the person must confirm, for example a new site opening, a system being replaced, or a team that is hiring.</li>'
            '<li><b>What happens on no-show.</b> Whether the provider rebooks, how many attempts, and whether a meeting that did not happen counts.</li></ul>'
            '<p>Share the same definition with every provider you talk to and watch how they react. A provider confident in its quality will improve the definition with you, ask about your best customers and push back where the target is too narrow to fill. A provider that wants to keep it loose is telling you what month three will look like.</p>'
            '<p>There is a good reason to be strict. In a ' + a(SAASTR, 'SaaStr poll of more than 1,200 people') + ', only 7% said outsourced SDRs had really worked for them. The causes raised in that discussion (vague targets, messaging the client never saw, reps spread across too many accounts) all begin with an unclear definition of what success is.</p>'
            '<p>Our guide to the ' + '<a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a>' + ' goes deeper on how to write this into the contract.</p>'
        )),
        ('show-rate', 'Why show rate matters more than meetings booked', (
            '<p>A booked meeting is a promise; a held meeting is the result. Compare appointment setting companies on how many meetings actually happen with the right person, because the gap between booked and held is where the value of a provider shows.</p>'
            + fig2 +
            '<p>The pattern in the chart is intuitive. Meetings the buyer asked for, through a referral or an inbound request, show up most often. Meetings booked after a cold call or a cold email show up less, and in this compilation, meetings booked by outsourced appointment setters had the highest no-show rate of all. The exact figures will vary by market, but the direction is a useful warning: a provider that books many meetings but lets a large share go unattended is not filling your pipeline, it is filling your calendar.</p>'
            '<p>What drives a strong show rate is mostly within the provider\'s control:</p>'
            '<ul><li><b>Real qualification on the call.</b> The prospect confirmed the problem, not just agreed to "a quick chat" to end the call.</li>'
            '<li><b>A clear reason in the invite.</b> One or two lines on why the meeting is worth their time, in their words.</li>'
            '<li><b>Short booking windows.</b> Meetings set within a few business days hold better than ones set weeks out.</li>'
            '<li><b>A reminder from a person.</b> A short, human confirmation the day before, not only an automated calendar ping.</li>'
            '<li><b>A brief for your rep.</b> Your seller walks in knowing who the person is and why they agreed, so the meeting is worth having.</li></ul>'
            '<p>Ask every provider for its show rate on held meetings, how it defines a no-show, and what it does about one. Then ask for the same numbers from your pilot rather than from their best client.</p>'
        )),
        ('us-or-not', 'US-based, nearshore or offshore callers: what changes', (
            '<p>Where the callers sit matters less than whether they work your buyer\'s hours and sound natural to them. A US-based team, a nearshore team in Latin America and an offshore team can all book good meetings; what differs is time zone overlap, how the calls sound and how much context the callers have about US business.</p>'
            '<p>For phone-heavy appointment setting, hours are the first filter. Decision makers in the US answer during their business day, so a team that works those hours as its normal day will call at the right time without burning out on night shifts. Latin American teams sit inside or close to US business hours, which is one reason US companies increasingly hire there. Our guide to ' + '<a href="/blog/nearshore-vs-offshore-sales-teams">nearshore vs offshore sales teams</a>' + ' compares the options in detail.</p>'
            '<p>The second filter is how the callers sound to your buyer. Accent is not the issue; being easy to understand, keeping pace and handling a firm "no" calmly are. Ask any provider to let you listen to real recorded calls in your segment, not a demo reel, and judge them as your buyer would.</p>'
            '<p>The third is context. A caller who has worked with US companies knows how a procurement team works, what a busy director will tolerate in the first 20 seconds and when to send a short email instead. Ask who the callers are, how long they have worked US accounts, and how many other clients they call for at the same time.</p>'
            '<p>If what you want is your own caller rather than a provider, that is a different decision: you hire and manage the person. Our ' + '<a href="/talent">talent team</a>' + ' places bilingual SDRs and cold callers from Latin America who work US hours.</p>'
        )),
        ('rules', 'Phone, email and AI voice: the US rules every provider should know', (
            '<p>A good US appointment setting company should explain, without being asked twice, how it follows the rules for calls, AI voices and email. The responsibility does not leave your company when someone else dials or sends, so these answers protect you as much as them.</p>'
            '<p><b>Calls to businesses.</b> The FTC\'s ' + a(FTC_DNC, 'Do Not Call guidance for telemarketers') + ' says most calls to a business made to sell to that business are exempt from the National Do Not Call provisions. That exemption is narrower than many assume: it covers calls to the business, not to a person\'s personal phone, and state rules can add their own requirements. Ask the provider how it handles mobile numbers and internal do-not-call requests.</p>'
            '<p><b>AI voices.</b> In February 2024 the FCC issued a ruling that AI-generated voices, including cloned voices, count as an "artificial or prerecorded voice" under the TCPA. As this ' + a(FCC_AI, 'Wilson Sonsini summary of the ruling') + ' explains, such calls generally need the recipient\'s prior express consent, and callers must identify themselves and offer a way to opt out. If a provider pitches AI voice agents that cold call your prospects, ask exactly how it gets consent.</p>'
            '<p><b>Email.</b> The FTC\'s ' + a(FTC_SPAM, 'CAN-SPAM guide') + ' says the law makes no exception for business-to-business email, requires a working opt out and a valid postal address, and that you cannot contract away your responsibility. Google\'s ' + a(GOOGLE, 'sender guidelines') + ' add technical rules: authenticate mail with SPF and DKIM, publish DMARC, and keep the user-reported spam rate below 0.1%.</p>'
            '<p>There is also a reputation rule that no regulator writes down. A ' + a(GARTNER, 'Gartner survey of 632 B2B buyers') + ' found that 73% actively avoid suppliers who send irrelevant outreach. Every careless call or email booked in your name makes your next approach to that account harder. This section is not legal advice; for your situation, ask your own counsel.</p>'
        )),
        ('compare', 'How to compare three providers in two weeks', (
            '<p>Shortlist three providers, give each the same written definition, ask for sample work on your real buyer and run a short pilot on one segment. Two weeks is enough to choose well, because the sample work and the first replies show more than any sales deck.</p>'
            + fig3 +
            '<p><b>Days 1 to 3: shortlist and define.</b> Pick three providers that already work with companies like yours. Send each the same qualified meeting definition, your best two customer stories and a short list of target accounts.</p>'
            '<p><b>Days 4 to 7: ask for sample work.</b> Ask each provider for a call opener, a three-step email sequence and a short list of ten accounts with the reason each is a fit now. You will see quickly who understood your buyer and who sent a template with your name in it.</p>'
            '<p><b>Days 8 to 10: listen.</b> Ask for recordings of real calls in a similar segment and a few anonymized reply threads. Listen for pace, tone and how objections are handled.</p>'
            '<p><b>Days 11 to 14: decide on a pilot.</b> Choose one provider for a pilot on one segment, with the definition in the contract, a weekly review of replies and meetings, and a clear exit if quality is not met. Score the pilot on:</p>'
            '<ul><li><b>Held meetings</b> that match the definition, with notes from your reps on each one.</li>'
            '<li><b>What you learned</b>: which problems buyers recognized and which objections repeated.</li>'
            '<li><b>Brand safety</b>: no complaints, no spam flags, no angry replies forwarded to your CEO.</li></ul>'
        )),
        ('agent-base', 'Where the Agent Base fits, and where it does not', (
            '<p>The Agent Base is not a classic appointment setter. It is an email-first outbound program where AI agents do the research, drafting and sorting, and a dedicated Agent Base manager approves every message before it reaches a buyer. It fits companies that want meetings with well-researched accounts and want to see every step; it is not built for high-volume phone campaigns.</p>'
            '<p>Here is how the work is split:</p>'
            '<ul><li><b>Scout</b> finds accounts that match your profile and show a reason to talk now, and <b>Lens</b> researches each one.</li>'
            '<li><b>Quill</b> drafts the emails in your voice, and your dedicated Agent Base manager edits or approves every draft. Nothing is sent on autopilot.</li>'
            '<li><b>Relay</b> sends approved emails at a safe pace from domains set up for outbound.</li>'
            '<li><b>Echo</b> sorts replies and drafts answers for review, and <b>Atlas</b> writes a short brief for each booked meeting so your rep walks in prepared.</li>'
            '<li>You see accounts, drafts, sends, replies and meetings on a live dashboard.</li></ul>'
            '<p>When a classic appointment setting company is the better choice: if your buyers mostly answer the phone and rarely read email, if you need many calls per day from day one, or if your offer is simple enough that volume matters more than research. In those cases, a phone-first provider, or your own bilingual callers through our ' + '<a href="/talent">talent team</a>' + ', will serve you better.</p>'
            '<p>Whichever way you go, hold every provider, including us, to the same definition and the same two-week test.</p>'
        )),
    ],
    'conclusion': (
        '<p>Choosing a B2B appointment setting company in the USA is less about finding the provider with the biggest promise and more about making them all play by the same rules. When every provider gets the same definition and the same test, the right one becomes easy to see.</p>'
        '<ol><li><b>Know the model</b> you are buying, and what it rewards.</li>'
        '<li><b>Write the qualified meeting definition</b> before the first call, including no-shows.</li>'
        '<li><b>Judge on held meetings</b> with the right people, not on meetings booked.</li>'
        '<li><b>Check the rules</b> on calls, AI voices and email, because the responsibility stays with you.</li>'
        '<li><b>Compare on real work</b>: sample messaging, recorded calls and a short pilot on one segment.</li></ol>'
        '<p>If you want to see how the Agent Base would research and write to your market, <a href="' + CAL + '"' + EXT + '>book a call</a> and bring your definition.</p>'
    ),
    'faq': [
        ('What does a B2B appointment setting company do?',
         'It finds prospects that match your ideal customer, contacts them by phone, email or LinkedIn, qualifies them and books a first meeting with your sales team. Your team runs the meeting and closes the deal.'),
        ('How do I choose an appointment setting company in the USA?',
         'Write a qualified meeting definition, shortlist three providers, ask each for sample messaging and recorded calls on your real buyer, then run a short pilot on one segment. Choose on held meetings with the right people, not on meetings booked.'),
        ('Is pay per appointment better than a monthly SDR team?',
         'Neither is better for everyone. Pay per appointment rewards meetings that pass the definition, so the definition must be strict. A dedicated team rewards steady effort and learning, so ask how much of the team\'s time goes to your account and whether you see the replies.'),
        ('What is a good show rate for booked B2B meetings?',
         'It varies by channel and market. Meetings from referrals and inbound requests show up far more often than meetings booked by cold call or cold email, so ask each provider for its held meeting numbers, how it defines a no-show and what it does about one.'),
        ('Can an appointment setting company use AI voices to cold call?',
         'The FCC ruled in February 2024 that AI-generated voices count as artificial voices under the TCPA, so these calls generally need the recipient\'s prior express consent. Ask any provider using AI voice agents exactly how it gets consent. This is not legal advice.'),
        ('Do Do Not Call rules apply to B2B cold calling?',
         'The FTC says most calls to a business made to sell to that business are exempt from the National Do Not Call provisions, but the exemption covers calls to the business, state rules can add requirements and other laws still apply. Ask your provider how it handles mobile numbers and opt outs.'),
        ('Is the Agent Base an appointment setting service?',
         'It books meetings, but it works differently from a classic appointment setter. AI agents research accounts, draft emails and sort replies, and a dedicated Agent Base manager approves every email before it is sent. It is email first, so phone-heavy campaigns are better served by a phone-first provider or your own callers.'),
    ],
}
