# Spec for blog/signal-based-outbound.html. Build: python3 tools/blogkit.py tools/posts/signal-based-outbound.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


SIXSENSE = 'https://www.businesswire.com/news/home/20251112018032/en/'
GONG = 'https://www.gong.io/resources/labs/the-hidden-power-of-cold-calling-insights-from-300m-calls/'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
USERGEMS = 'https://www.usergems.com/power-up-your-pipeline'
GOOGLE = 'https://support.google.com/mail/answer/81126'

fig1 = figure(1, bar_chart('How much is decided before a buyer talks to sales', [
    ('Ranked vendors before first contact', 94),
    ('Bought from the early favorite', 77),
], unit='%', vmax=100, highlight=('Ranked vendors before first contact',)),
    'Most buying groups already have a favorite before any seller is in the conversation. Source: ' + a(SIXSENSE, '6sense 2025 Buyer Experience Report') + ', a survey of more than 4,000 B2B buyers.')

fig2 = figure(2, table(['Signal', 'What it tells you', 'Best first channel', 'How fast to act'], [
    ['<b>Former customer or champion changes jobs</b>', 'Someone who already trusts you now has a new budget and a new team', 'LinkedIn or a personal email', 'Within the first weeks in the role'],
    ['<b>New leader in the function you sell to</b>', 'New leaders review tools and vendors early', 'Email with a specific reason, then a call', 'Within the first months'],
    ['<b>Job posts for the role your product supports</b>', 'The team is growing or has a gap you can fill', 'Email or phone', 'While the post is open'],
    ['<b>Funding, expansion or a new office</b>', 'There is money and a plan to grow', 'Phone or email to the leader who owns the plan', 'Within a few weeks'],
    ['<b>New tech installed or replaced</b>', 'A related problem is being worked on now', 'Email that names the change', 'While the project is active'],
    ['<b>Visits to your site or pricing page from a known account</b>', 'Active research in your category', 'Phone, quickly', 'Within a day'],
]), 'Common buying signals for B2B outbound, the channel that usually fits each one, and how quickly the signal goes stale. Use the ones your best customers actually showed before they bought.')

fig3 = figure(3, steps('From signal to first message', [
    ('Signal', 'a reason to talk now'),
    ('Research', 'who owns the problem'),
    ('Reachability', 'phone, LinkedIn or email'),
    ('Message', 'written for this account'),
    ('Review', 'a person approves it'),
], accent=('Reachability',)),
    'Signal-based outbound in five steps. The step most teams skip is the third one (amber): checking where the buyer can actually be reached before choosing a channel.')

POST = {
    'slug': 'signal-based-outbound',
    'title': 'Signal-based outbound: start where the buyer can be reached',
    'h1': 'Signal-based outbound: start where the buyer can be <em>reached</em>',
    'description': 'What signal-based outbound is, which buying signals are worth acting on, why reachability matters as much as the signal, and how to run it without turning it into another volume machine.',
    'category': 'Outbound',
    'date': '2026-11-18',
    'date_label': 'November 18, 2026',
    'hero_img': 'blog-signal-outbound',
    'card_img': 'blog-signal-outbound',
    'card_title': 'Signal-based outbound: start where the buyer can be reached',
    'card_text': 'Pick accounts with a reason to talk now, then reach them on the channel they actually answer.',
    'takeaways': [
        'Signal-based outbound means contacting accounts that show a reason to buy right now, such as a new leader, a hiring push or a job change, instead of working evenly through a static list.',
        'Timing matters because buyers decide early: 94% of buying groups rank their preferred vendors before they first talk to a seller, according to 6sense.',
        'A signal only helps if you can reach the person behind it, so check whether each buyer answers the phone, LinkedIn or email before you choose the channel.',
        'Signals are a reason to write, not a message. Each one still needs research, a specific first line and a person who approves it before it goes out.',
    ],
    'intro': (
        '<p>Most outbound still starts with a list: a few thousand companies that match a filter, loaded into a sequence and worked from top to bottom. Every account gets the same number of touches, whether or not anything is happening there. Signal-based outbound turns that around. You start with accounts where something just changed, and you spend your effort where there is a reason to talk now.</p>'
        '<p>This guide explains what signal-based outbound is, which signals are worth acting on, and the part most guides leave out: a signal is useless if you cannot reach the person behind it. We run outbound for US B2B companies with a base of AI agents and a dedicated Agent Base manager, and "signal first, not volume first" is how we work, so we also show what that looks like day to day.</p>'
    ),
    'cta': {
        'inline_lead': 'Want outbound that starts with a signal?',
        'inline_text': 'Book a 30 minute call. We will show you how the Agent Base finds accounts with a reason to buy, checks where each buyer can be reached, and has a person approve every email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound that starts with a <em>reason</em> to talk.',
        'band_text': 'Scout finds accounts with a buying signal, Lens researches each one, Quill drafts the email and your dedicated Agent Base manager approves it before it goes out. You watch it all on a live dashboard.',
    },
    'sections': [
        ('what-it-is', 'What signal-based outbound is', (
            '<p>Signal-based outbound is outreach that starts from an event at the account, not from a list. You contact a company because something just happened there that makes your offer relevant now, such as a new sales leader, a funding round, a hiring push or a former customer joining the team.</p>'
            '<p>The difference from list-based outbound is where the effort goes:</p>'
            '<ul><li><b>List-based outbound</b> spreads effort evenly. Every account that matches the filter gets the same sequence, and the hope is that a small share happens to be in the market.</li>'
            '<li><b>Signal-based outbound</b> concentrates effort. Accounts with a fresh signal get research and a written reason to talk. Accounts without one wait, or get a lighter touch.</li></ul>'
            '<p>A signal is not the same as a fit. Fit tells you a company <i>could</i> buy: right industry, right size, right tech. A signal tells you it might buy <i>soon</i>. Good outbound needs both. A perfect-fit account with no signal is a long shot this quarter, and a strong signal at a company that will never buy is noise.</p>'
            '<p>The idea is not new: good sellers have always called the new VP in their first month. What changed is that job posts, leadership changes, tech changes and website visits can now be tracked across thousands of accounts. That makes the approach possible at scale, and also makes it easy to drown in signals that mean very little.</p>'
        )),
        ('why-now', 'Why timing matters more than volume', (
            '<p>Timing matters because buyers decide before they talk to you. In the ' + a(SIXSENSE, '6sense 2025 Buyer Experience Report') + ', 94% of buying groups had ranked their preferred vendors before first contact with a seller, and they bought from that early favorite 77% of the time.</p>'
            + fig1 +
            '<p>Buyers are also trying to avoid sellers altogether. A ' + a(GARTNER, 'Gartner survey') + ' found that 61% of B2B buyers prefer a rep-free buying experience. Put those two findings together and the cost of bad timing is clear: if you reach a buyer after the shortlist is made, you are asking them to reopen a decision. If you reach them while the problem is new, you can help shape it.</p>'
            '<p>Volume does not fix timing. Sending more emails to more accounts raises the chance of hitting someone at the right moment, but it also:</p>'
            '<ul><li><b>Hurts deliverability.</b> ' + a(GOOGLE, 'Google\'s sender guidelines') + ' tie inbox placement to spam complaint rates and authentication, so mass sends to people who never wanted them put your whole domain at risk.</li>'
            '<li><b>Burns your market.</b> In a niche with a few hundred buyers, a generic sequence today makes the well-timed email next quarter less likely to be read.</li>'
            '<li><b>Trains buyers to ignore you.</b> A message with no reason to exist reads like every other one in the inbox.</li></ul>'
            '<p>A signal gives the message a reason to exist. "You just opened an office in Austin" or "You posted three SDR roles this month" is a better first line than any clever subject line, because it is about the buyer\'s situation, not yours.</p>'
        )),
        ('which-signals', 'Which buying signals are worth acting on', (
            '<p>The signals worth acting on are the ones that came before a purchase in your own past deals. Start with your last ten or twenty customers and ask what was happening at each company in the months before they bought, then watch for the same events at accounts like them.</p>'
            + fig2 +
            '<p>Some patterns show up across many markets:</p>'
            '<ul><li><b>People moves are strong.</b> A person who used your product before, or championed it, already trusts you. UserGems, a vendor that tracks job changes, reports in its ' + a(USERGEMS, 'pipeline research') + ' that past champions converted to opportunities more often than any other contact type in its data. Treat vendor numbers with care, but the logic holds: trust travels with people.</li>'
            '<li><b>New leaders review vendors.</b> Someone new in a role is expected to make changes, and early in the role they have the mandate to do it.</li>'
            '<li><b>Hiring is a plan made public.</b> A company posting several roles in the function you serve is telling you where it is investing.</li>'
            '<li><b>Website visits are fast and fragile.</b> A known account on your pricing page is a strong signal, but it fades within days.</li></ul>'
            '<p>Weaker signals still have a use. A content download, a social like or a broad "intent topic" spike rarely justifies a call on its own. Use them to rank accounts that already have a stronger signal, not as the reason to write.</p>'
            '<p><b>Keep the list short.</b> Three to five signals that you have seen before real deals beat twenty that a tool can track. Every signal you add needs a different first line, a different reason and a different person to contact, so more signals mean more work per account. Add a new one only after the first ones are producing replies.</p>'
        )),
        ('reachability', 'Reachability: the signal is useless if you can\'t reach the buyer', (
            '<p>A signal tells you when to reach out, but not how. Before choosing a channel, check where each buyer can actually be reached: some answer their phone, some live on LinkedIn, and some only read email. Starting on the channel they use is worth more than adding channels they ignore.</p>'
            '<p>Most outbound playbooks answer the channel question with "all of them": email, LinkedIn and phone in a fixed sequence for every prospect. That looks thorough, but it treats every buyer the same, which is the habit signal-based outbound is meant to break. A better approach is to check reachability per person:</p>'
            '<ul><li><b>Phone.</b> Is there a verified direct dial, and does this person pick up? Field sales leaders and operators often do. Many executives in large companies never will.</li>'
            '<li><b>LinkedIn.</b> Do they post, comment or update their profile? An active profile is a channel; an empty one is not.</li>'
            '<li><b>Email.</b> Is the address verified, and is the domain one that filters cold email hard? A bounce damages your sender reputation for every other prospect.</li></ul>'
            '<p>The phone deserves a fresh look. Gong analyzed more than ' + a(GONG, '300 million cold calls') + ' and found that average reps reached a live person on about 5.4% of dials, while top reps reached about 13.3%. The same study found that calling a prospect nearly doubled email reply rates, from 1.81% to 3.44%, even when nobody answered. Calls and emails work together when the person is reachable by both.</p>'
            + fig3 +
            '<p>Reachability also tells you when to stop. If a buyer has a strong signal but no working channel, find a second person at the account who shares the problem rather than sending more messages into silence.</p>'
        )),
        ('message', 'Turning a signal into a message worth replying to', (
            '<p>A signal is a reason to write, not the message itself. The first line names what changed, the next line connects it to a problem the buyer probably has now, and the ask is small. Without that connection, "Congrats on the funding" is just another template.</p>'
            '<p>Compare two openings for the same signal, a company hiring four SDRs:</p>'
            '<ul><li><b>Weak:</b> "I saw you are hiring! We help companies like yours grow pipeline."</li>'
            '<li><b>Better:</b> "Four SDR roles open at once usually means the team is being asked for more pipeline this quarter. The hard part is often the first 90 days, before new reps book meetings. Worth comparing notes on how other teams handle that gap?"</li></ul>'
            '<p>The second version does three things the first does not. It shows the sender understood what the signal means, it names a likely problem in the buyer\'s words, and it asks for a conversation rather than a demo.</p>'
            '<p>Rules that keep signal-based messages honest:</p>'
            '<ul><li><b>Do the research.</b> Read the job post, the press release or the new leader\'s profile before writing. Guessing wrong about what a signal means is worse than not mentioning it.</li>'
            '<li><b>Don\'t be creepy.</b> Mentioning a public job post is fine. Telling someone you saw them on your pricing page at 11 pm is not.</li>'
            '<li><b>One reason per email.</b> Stacking three signals in one message reads like surveillance and blurs the point.</li>'
            '<li><b>Follow up with something new.</b> A second email that adds a useful idea earns more than "just bumping this up."</li></ul>'
            '<p>This is where AI helps and where it needs a person. An agent can read the job post and draft a first line quickly. A person who knows the market should still decide whether the line is true, relevant and worth sending.</p>'
        )),
        ('mistakes', 'Where signal-based outbound goes wrong', (
            '<p>Signal-based outbound fails when teams treat signals as a new way to generate volume. If every tracked event triggers an automatic sequence, you are back to list-based outbound with a fancier filter, and buyers can tell.</p>'
            '<p>The most common mistakes:</p>'
            '<ul><li><b>Too many signals, too little meaning.</b> Tracking dozens of intent topics creates a long list of "hot" accounts that are not hot. Start with the few signals tied to your past deals.</li>'
            '<li><b>Acting too late.</b> A job change is worth more in the first weeks than after six months. Website visits are worth most within a day. Build the process so signals reach a person while they are fresh.</li>'
            '<li><b>Ignoring fit.</b> A big funding round at a company that will never buy your product is still not a lead.</li>'
            '<li><b>Automating the message.</b> Merge fields that drop the signal into a template ("Congrats on {event}!") are easy to spot and easy to ignore.</li>'
            '<li><b>Skipping reachability.</b> A perfect signal sent to an unverified email address bounces, and the bounce hurts every other send.</li>'
            '<li><b>Measuring opens and sends.</b> Judge the program on replies from the right people and on meetings held, not on activity.</li></ul>'
            '<p>The pattern behind all of these is the same: the tool finds the signal, but nobody owns the judgment about whether it is real and whether the message is good enough to send under your name.</p>'
        )),
        ('how-we-run-it', 'How the Agent Base runs signal-first outbound', (
            '<p>In the Agent Base, AI agents do the watching and the research, and a dedicated Agent Base manager makes the decisions. Every account starts with a signal and a reachability check, and every email is approved by a person before it reaches a buyer.</p>'
            '<p>Here is who does what:</p>'
            '<ul><li><b>Scout</b> finds companies in your market that show a reason to buy right now, and the person who decides.</li>'
            '<li><b>Lens</b> researches each account so the first email carries something specific to that company.</li>'
            '<li><b>Quill</b> writes the first email and the follow ups in your voice, one prospect at a time.</li>'
            '<li><b>Your dedicated Agent Base manager</b> reads every draft and edits or approves it. Nothing goes out without this step.</li>'
            '<li><b>Relay</b> sends approved emails at a safe pace and keeps the follow up schedule.</li>'
            '<li><b>Echo</b> reads and sorts replies, and sends the interested ones straight to the Agent Base manager.</li>'
            '<li><b>Atlas</b> writes a short brief for every booked meeting: who they are, why we wrote and what to ask.</li></ul>'
            '<p>Before any of that, we qualify where each buyer can be reached, by phone, LinkedIn or email, and start there. Calls go to verified direct dials. Mailboxes are set up and warmed for about three weeks before email campaigns start, so the domain stays healthy. Calling can start before email does.</p>'
            '<p>You do not have to take our word for the work. Every lead found, every email sent, every reply and every booked meeting shows up on a live dashboard you can open any time. If you are comparing this model with hiring your own rep, our guide to <a href="/blog/outsourced-sdr-vs-in-house-sdr">outsourced vs in-house SDRs</a> covers the trade-offs, and <a href="/blog/ai-sdr-vs-human-sdr">AI SDR vs human SDR</a> explains why we keep a person in the loop.</p>'
        )),
    ],
    'conclusion': (
        '<p>Signal-based outbound is a simple idea that is easy to get wrong. Contact accounts with a reason to talk now, reach each buyer where they actually answer, and keep a person in charge of what gets sent.</p>'
        '<ol><li><b>Start from your own deals:</b> find the three to five events that came before past purchases.</li>'
        '<li><b>Combine fit and signal:</b> an account needs both to deserve research.</li>'
        '<li><b>Act while it is fresh:</b> days for website visits, weeks for job changes and new leaders.</li>'
        '<li><b>Check reachability first:</b> phone, LinkedIn or email, based on the person, not a fixed sequence.</li>'
        '<li><b>Write from the signal:</b> name what changed, connect it to a problem, ask for something small.</li>'
        '<li><b>Keep a reviewer:</b> someone who owns the judgment on every message, and measures replies and meetings, not sends.</li></ol>'
        '<p>If you would rather have this run for you, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will walk you through the Agent Base on a live dashboard.</p>'
    ),
    'faq': [
        ('What is signal-based outbound?',
         'Signal-based outbound is outreach that starts from an event at the account, such as a new leader, a funding round, a hiring push or a former customer changing jobs. Instead of working evenly through a list, you focus effort on accounts with a reason to talk now.'),
        ('What is the difference between signal-based selling and intent data?',
         'Intent data is one type of signal, usually showing that people at a company are researching a topic online. Signal-based selling is the wider approach of acting on any meaningful event, including job changes, hiring, funding and leadership moves, many of which are public and easy to verify.'),
        ('Which buying signals are the strongest for B2B outbound?',
         'Usually the ones tied to people: a former customer or champion joining a new company, or a new leader in the function you sell to. Website visits from known accounts are also strong but fade within days. The best signals for you are the events that came before your own past deals.'),
        ('How fast should you act on a buying signal?',
         'As fast as the signal fades. Act within a day on a pricing page visit, within the first weeks on a job change or new leader, and while the role is still open on a job post. A late message on a stale signal reads like any other cold email.'),
        ('Does signal-based outbound replace cold calling?',
         'No. It tells you who to call and why. Gong\'s analysis of more than 300 million cold calls found that calling a prospect nearly doubled email reply rates, so phone and email work best together when the buyer can be reached on both.'),
        ('Can AI run signal-based outbound on its own?',
         'AI is good at watching for signals and researching accounts at scale. It is weaker at judging whether a signal really matters and whether a message is worth sending under your name. That is why the Agent Base keeps a dedicated Agent Base manager who approves every email.'),
        ('How many signals should we track?',
         'Start with three to five that you have seen before real deals. Each new signal needs its own reason, message and contact, so adding more creates work before it creates pipeline. Add signals only after the first ones are producing replies.'),
    ],
}
