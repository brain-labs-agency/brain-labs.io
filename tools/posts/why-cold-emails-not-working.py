# Spec for blog/why-cold-emails-not-working.html. Build: python3 tools/blogkit.py tools/posts/why-cold-emails-not-working.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GOOGLE = 'https://support.google.com/a/answer/14229414'
INSTANTLY = 'https://instantly.ai/cold-email-benchmark-report-2026'
SMARTLEAD = 'https://www.smartlead.ai/benchmarks'
BELKINS = 'https://belkins.io/blog/cold-email-response-rates'
LEMLIST = 'https://lemlist.com/blog/cold-email-response-rate'

fig1 = figure(1, table(['What you see', 'Most likely cause', 'Check this first'], [
    ['<b>Almost no opens, no replies, few bounces</b>', 'Mail is landing in spam or promotions', 'Authentication, spam complaint rate and sending volume per inbox'],
    ['<b>High bounce rate</b>', 'Old or guessed contact data', 'Verify the list before sending and remove bad addresses'],
    ['<b>Replies, but mostly "not me" or "wrong team"</b>', 'Right companies, wrong people', 'Titles and seniority in your list'],
    ['<b>Replies, but mostly "not interested"</b>', 'No reason for this buyer to talk now', 'The signal behind each account'],
    ['<b>Silence from a list you trust</b>', 'The message does not land', 'Length, first line and the ask'],
    ['<b>A few positive replies that never become meetings</b>', 'Slow or clumsy reply handling', 'Time to first response and the booking step'],
]), 'A quick diagnostic. Match what you see in your numbers to the most likely cause before you rewrite anything.')

fig2 = figure(2, bar_chart('Cold email reply rate tiers, Instantly 2026 benchmark', [
    ('Platform average', 3.43),
    ('Top 25% of campaigns', 5.5),
    ('Top 10% of campaigns', 10.7),
], unit='%', vmax=13, highlight=('Platform average',)),
    'Reply rate tiers from campaigns sent on the Instantly platform in 2025. Other datasets measure replies differently and report lower averages, so compare yourself with one source at a time. Source: '
    + a(INSTANTLY, 'Instantly Cold Email Benchmark Report 2026') + '.')

fig3 = figure(3, steps('The order to diagnose a cold email program', [
    ('Delivery', 'is it arriving?'),
    ('List', 'right people?'),
    ('Reason', 'why now?'),
    ('Message', 'does it land?'),
    ('Follow up', 'enough touches?'),
    ('Replies', 'handled fast?'),
], accent=('Delivery',)),
    'Work from left to right. A problem early in the chain hides every fix you make later in it, so there is no point rewriting copy that never reaches an inbox.')

POST = {
    'slug': 'why-cold-emails-not-working',
    'title': 'Why are my cold emails not working? A diagnostic',
    'h1': 'Why are my cold emails <em>not working</em>? A diagnostic',
    'description': 'Cold emails fail for six reasons, in a predictable order: delivery, list, timing, message, follow up and reply handling. Here is how to find which one is yours before you rewrite anything.',
    'category': 'Outbound',
    'date': '2026-11-25',
    'date_label': 'November 25, 2026',
    'hero_img': 'cover-why-cold-emails-not-working',
    'card_img': 'cover-why-cold-emails-not-working',
    'card_title': 'Why are my cold emails not working? A diagnostic',
    'card_text': 'Most teams rewrite the copy first. The problem is usually earlier: delivery, the list or the reason to write at all.',
    'takeaways': [
        'Cold emails usually fail for one of six reasons, in this order: they do not arrive, they go to the wrong people, there is no reason to talk now, the message does not land, there is no follow up, or replies are handled badly.',
        'Diagnose in that order. A delivery problem makes every copy test meaningless, because nobody is reading either version.',
        'Benchmarks are only useful against one source at a time. Published "average reply rates" range from under 1% to above 3% because each dataset counts replies differently.',
        'Most fixes are about fewer, better chosen contacts and a person reading every email before it goes out, not about clever subject lines.',
    ],
    'intro': (
        '<p>You wrote the sequence, loaded the list and pressed send. Two weeks later you have a handful of replies, most of them some version of "please remove me", and no meetings. The natural reaction is to rewrite the email. Usually that is the wrong first move, because the email is only one of six places a cold program can break, and it is rarely the first one.</p>'
        '<p>This guide is a diagnostic. It walks through the six failure points in the order you should check them, shows what each one looks like in your numbers, and explains what to change. It uses published benchmarks and Google\'s own sender rules where they help, and it ends with a short way to decide whether to fix your program or rebuild it.</p>'
    ),
    'cta': {
        'inline_lead': 'Want a second pair of eyes on your outbound?',
        'inline_text': 'Book a 30 minute call. We will walk through where your current program is losing buyers and show you how the Agent Base handles each step, with a dedicated Agent Base manager approving every email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound that is <em>checked</em> at every step.',
        'band_text': 'Scout finds accounts with a reason to talk, Lens researches them, Quill drafts, Relay sends at a safe pace, Echo sorts replies and Atlas briefs you before each meeting. Your dedicated Agent Base manager approves every email before it reaches a buyer.',
    },
    'sections': [
        ('start-with-numbers', 'Start with your numbers, not your copy', (
            '<p>The fastest way to find out why cold emails are not working is to look at where the drop happens: delivery, replies or meetings. Each failure point leaves a different fingerprint in your numbers, so a few minutes with your sending data tells you which part of the program to fix.</p>'
            '<p>Pull four numbers for your last campaign, ideally covering a few hundred contacts or more:</p>'
            '<ul><li><b>Bounce rate.</b> The share of emails that never reached a mailbox at all.</li>'
            '<li><b>Reply rate.</b> All replies, divided by the people you contacted.</li>'
            '<li><b>Positive reply rate.</b> Replies that show interest or ask a question, divided by people contacted.</li>'
            '<li><b>Meetings held.</b> Not booked. Held.</li></ul>'
            '<p>Then match the pattern to a likely cause.</p>'
            + fig1 +
            '<p>Open rates are left out on purpose. Privacy features in modern mail apps load tracking pixels automatically, so open rates are noisy at best. A low open rate can still hint at a spam problem, but replies and bounces are more reliable signals.</p>'
            '<p>Next, decide what "good" looks like, and be careful here. Published benchmarks disagree a lot. The ' + a(INSTANTLY, 'Instantly 2026 benchmark report') + ' puts the average reply rate on its platform at 3.43%, with the top 10% of campaigns above 10%. ' + a(SMARTLEAD, 'Smartlead\'s State of Cold Email 2026') + ', based on more than 850 million emails, puts the typical sender at 0.74%. ' + a(BELKINS, 'Belkins\' study of 7.5 million emails') + ' reports 0.45%, measured as replies divided by all emails sent, including follow ups.</p>'
            + fig2 +
            '<p>Those numbers are not contradictions. They count different things on different platforms. Pick one benchmark that measures replies the way you do and compare yourself with it over time. Your own trend is a better guide than anyone\'s average.</p>'
        )),
        ('check-delivery', 'Check delivery first: are your emails arriving?', (
            '<p>Check delivery first because if your emails land in spam, nothing else you change will show up in the results. The signs are very few replies of any kind, including no angry ones, from a list you believe is accurate.</p>'
            '<p>Google publishes the rules its systems apply. Its ' + a(GOOGLE, 'email sender guidelines') + ' ask every sender to authenticate with SPF or DKIM, and bulk senders (more than 5,000 messages a day to Gmail) to set up SPF, DKIM and a DMARC record, with the From domain aligned. Google says to keep the spam rate reported in Postmaster Tools below 0.1% and never let it reach 0.3%, and that it began ramping up enforcement on non-compliant traffic in November 2025. Most cold programs send far fewer than 5,000 emails a day, but following the bulk rules is still the safest baseline.</p>'
            '<p>A practical delivery checklist:</p>'
            '<ul><li><b>Authentication.</b> SPF, DKIM and DMARC set up on every sending domain, and checked with a header test, not assumed.</li>'
            '<li><b>Separate sending domains.</b> Cold email goes out from secondary domains, so a reputation problem never reaches the domain your customers and invoices use.</li>'
            '<li><b>Warmed inboxes and modest volume.</b> New inboxes that jump straight to full volume look like spam because they behave like spam.</li>'
            '<li><b>Verified data.</b> Bounces hurt your sender reputation. Verify every address before it enters a sequence.</li>'
            '<li><b>An easy way out.</b> A clear line telling people how to opt out, honored right away. Complaints cost more than unsubscribes.</li></ul>'
            '<p>Authentication alone will not make a poor campaign work, but it does help a good one. Smartlead\'s dataset found that ' + a(SMARTLEAD, 'senders with verified SPF, DKIM and DMARC') + ' needed fewer contacts per reply than senders without them. Smartlead is careful to call these patterns, not controlled tests, which is the right way to read every benchmark in this guide.</p>'
            '<p>If delivery is the problem, pause the sequence, fix the setup and lower the volume before you touch the copy. Sending more to make up for low replies is how a small reputation problem becomes a large one.</p>'
        )),
        ('check-list', 'Check the list: are you writing to the right people?', (
            '<p>If your emails arrive but replies say "not my area" or "we are too small for this", the list is the problem. The right message sent to the wrong person is still the wrong email.</p>'
            '<p>List problems come in three forms:</p>'
            '<ul><li><b>Wrong companies.</b> Accounts that match your filters on paper but could never buy, because they are too small, in the wrong market, or already locked into a competitor.</li>'
            '<li><b>Wrong people.</b> The right company, but a contact who neither feels the problem nor makes the decision. This shows up as polite referrals and silence.</li>'
            '<li><b>Too broad.</b> One list of thousands, all receiving the same email. Nothing in it is specific to any of them.</li></ul>'
            '<p>The data points the same way. Woodpecker data cited by ' + a(LEMLIST, 'lemlist') + ' found that campaigns sent to fewer than 50 recipients had a reply rate of 5.8%, against 2.1% for lists of more than 1,000. Belkins found reply rates fall with company size and seniority: in its data, ' + a(BELKINS, 'founders replied more often than VPs') + ', and companies with fewer than 10 employees replied more often than enterprises with 10,000 or more.</p>'
            '<p>That does not mean you should only email founders at tiny companies. It means smaller, sharper segments outperform big generic ones, and that the person you write to has to be someone who would plausibly care. A good test: for every contact in the list, could you say in one sentence why that person, at that company, should read your email? If the answer is "because they match the filter", the list needs work.</p>'
            '<p>If you are a SaaS company, we cover how to build these segments in more detail in <a href="/blog/lead-generation-saas-companies">lead generation for SaaS companies</a>.</p>'
        )),
        ('check-reason', 'Check the reason to write now', (
            '<p>If the right people are reading and replying "not interested", the most common cause is that you gave them no reason to talk now. Most buyers are not in the market on any given day, and an email that could have been sent at any moment is easy to ignore.</p>'
            '<p>A reason to write now is a signal: something that changed at the account and makes your offer more relevant this month than last month. Useful signals are specific and checkable:</p>'
            '<ul><li><b>Hiring.</b> Open roles that point to the problem you solve, such as several sales roles posted at once.</li>'
            '<li><b>Growth events.</b> A new funding round, a new office, a new market or a large new customer.</li>'
            '<li><b>Leadership change.</b> A new VP or head of department, who is often reviewing tools and vendors.</li>'
            '<li><b>Stated priorities.</b> Something the company or the person has said publicly, in a post, a talk or an interview.</li></ul>'
            '<p>The signal should shape the email, not decorate it. "Congrats on the funding round" followed by a generic pitch is not a signal-based email. A good one connects what changed to the specific problem it creates and to the one thing you can help with.</p>'
            '<p>Signals also need a source you can show. Agents and tools that pick up news without checking it are how companies end up congratulating a prospect on a launch from last year. In the Agent Base, Scout records each signal with its source, and the dedicated Agent Base manager can open it before approving the email that uses it.</p>'
            '<p>If you cannot find a reason to write to an account today, the honest answer is often to leave it out of this month\'s campaign and keep it for later. Fewer, better timed emails protect both your reply rate and your domains.</p>'
        )),
        ('check-message', 'Check the message: does it land in ten seconds?', (
            '<p>Only once delivery, list and timing check out should you look at the email itself. A cold email has to make sense in the few seconds a busy person gives it, so the usual problem is that it is too long, too much about you, or asks for too much.</p>'
            '<p>The benchmarks agree that shorter tends to win. ' + a(SMARTLEAD, 'Smartlead') + ' found that first emails under 50 words needed fewer contacts per reply than emails of 100 to 149 words. ' + a(INSTANTLY, 'Instantly') + ' reports that its best performing campaigns keep emails under 80 words. Woodpecker data cited by ' + a(LEMLIST, 'lemlist') + ' found that context-specific copy roughly doubled reply rates compared with generic personalization such as a first name and company name.</p>'
            '<p>Read your email against five questions:</p>'
            '<ul><li><b>Is the first line about them?</b> Not about you, your company or your funding. About something true and specific to the reader.</li>'
            '<li><b>Is there one problem?</b> Not a list of features. One problem this person probably has, given the signal.</li>'
            '<li><b>Is there proof they can check?</b> A specific, verifiable point beats an adjective. "Teams like yours" is not proof.</li>'
            '<li><b>Is the ask small?</b> A question that is easy to answer beats a request for 30 minutes from a stranger.</li>'
            '<li><b>Would you reply?</b> Read it on your phone, as if you had 40 other emails waiting. Be honest.</li></ul>'
            '<p>AI writing tools make long, polished, generic emails very easy to produce, and buyers have learned to spot them. That is why we have a person read every draft. In the Agent Base, Quill writes from the research note Lens prepares, and the dedicated Agent Base manager edits or rejects anything that sounds generic, overclaims or gets a fact wrong.</p>'
        )),
        ('check-follow-up', 'Check follow ups and timing', (
            '<p>If people are reading but you only send one email, you are leaving many of your replies on the table. In the ' + a(INSTANTLY, 'Instantly data') + ', the first email produced 58% of replies and the follow ups produced the other 42%, and the strongest campaigns used four to seven touches.</p>'
            '<p>Smartlead\'s data adds a useful limit: reply rates ' + a(SMARTLEAD, 'fall with each step') + ' of a sequence, so the later emails matter less than the early ones. That suggests a simple pattern:</p>'
            '<ul><li><b>Make every follow up add something.</b> A different angle, a useful resource, a short question. "Just bumping this up" adds nothing.</li>'
            '<li><b>Keep the gap reasonable.</b> A few business days between touches, longer for later steps.</li>'
            '<li><b>Stop on any reply.</b> Including out of office replies that name a return date. Restart after that date, by hand.</li>'
            '<li><b>Stop at the end.</b> When the sequence ends, the account goes back into the pool until there is a new reason to write.</li></ul>'
            '<p>Timing matters less than most people think, but it is not zero. ' + a(BELKINS, 'Belkins') + ' saw slightly higher reply rates for emails sent in the morning, from 8 AM to noon in the recipient\'s time zone. Sending in your prospect\'s working hours, not yours, is the simple version of that rule, and it matters more when your team works from another time zone.</p>'
            '<p>One warning: more follow ups to a list that does not care will raise complaints, not replies. Follow up harder only after the list and the reason to write are right.</p>'
        )),
        ('check-replies', 'Check what happens after someone replies', (
            '<p>The last failure point is the one most teams never measure: what happens after a positive reply. If interested prospects do not turn into held meetings, the problem is response speed, the booking step or the hand off to whoever runs the call.</p>'
            '<p>Common leaks:</p>'
            '<ul><li><b>Slow answers.</b> A reply that waits until tomorrow has often cooled down by then.</li>'
            '<li><b>Too many steps to book.</b> Back and forth on times, or a calendar link with no context, loses people.</li>'
            '<li><b>Lost context.</b> The person who runs the meeting does not know why the prospect replied or what they asked.</li>'
            '<li><b>No-shows.</b> Meetings booked weeks out, with no reminder and no agenda, often do not happen.</li></ul>'
            '<p>Then use the full chain to decide what to do next. If more than one step is broken, start with the earliest one and fix it before you test anything else.</p>'
            + fig3 +
            '<p>This is the order the Agent Base follows. Relay sends at a pace that protects your domains, Echo reads and sorts every reply so interested buyers get a fast answer, and Atlas writes a brief before each meeting so the person on the call knows the account and why the buyer replied. Everything appears on a live dashboard, so you can see where in the chain your buyers are, not just how many emails went out.</p>'
            '<p>If you want to compare this approach with fully autonomous tools, read <a href="/blog/are-ai-sdrs-worth-it">are AI SDRs worth it</a>. If you are weighing an agency, our <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a> covers what to check before you sign.</p>'
        )),
    ],
    'conclusion': (
        '<p>Cold email rarely fails for a mysterious reason. It fails at one of six points, and your numbers usually tell you which one. The mistake is to start at the end of the chain, with the copy, when the problem sits at the start.</p>'
        '<ol><li><b>Delivery.</b> Authenticate, verify the list, keep the volume and complaint rate low.</li>'
        '<li><b>List.</b> Smaller segments, the right people, and a one-sentence reason for each contact.</li>'
        '<li><b>Reason.</b> A real, sourced signal that makes this month the right time.</li>'
        '<li><b>Message.</b> Short, about them, one problem, a small ask.</li>'
        '<li><b>Follow up.</b> Several touches that each add something, sent in their working hours.</li>'
        '<li><b>Replies.</b> Fast answers, easy booking and a brief for the meeting.</li></ol>'
        '<p>If you fix the earliest broken step and measure again, you will learn more in two weeks than in a month of subject line tests. If several steps are broken at once, it may be faster to rebuild the program than to patch it.</p>'
    ),
    'faq': [
        ('What is a good reply rate for cold email?',
         'It depends on how the data counts replies. The ' + a(INSTANTLY, 'Instantly 2026 benchmark') + ' reports a 3.43% platform average, with the top 10% of campaigns above 10%, while ' + a(SMARTLEAD, 'Smartlead') + ' and ' + a(BELKINS, 'Belkins') + ' report averages below 1% using different methods. Pick one source that measures replies the way you do and track your own trend against it.'),
        ('How do I know if my cold emails are going to spam?',
         'The usual signs are very few replies of any kind, including negative ones, from a list you trust, plus a rising spam rate in Google Postmaster Tools. Send test emails to inboxes you control on several providers, and check that SPF, DKIM and DMARC pass in the message headers.'),
        ('Should I rewrite my email or change my list first?',
         'Change the list first if replies say you have the wrong person or the wrong company. Rewrite the email only when delivery is healthy and the right people are reading but not replying.'),
        ('How many follow ups should a cold email sequence have?',
         'Most published data points to several touches rather than one. Instantly found that follow ups produced 42% of replies in its dataset and that four to seven touches worked best, as long as each one adds something new.'),
        ('How long should a cold email be?',
         'Short. Benchmarks from Smartlead and Instantly both found that emails under roughly 50 to 80 words performed better than longer ones. Aim for one specific opening line, one problem, one piece of proof and one small ask.'),
        ('Can AI fix a cold email program that is not working?',
         'AI can speed up research and drafting, but it cannot fix a bad list, a missing reason to write or a delivery problem, and it can make generic emails faster. It works best when a person checks the targeting and approves each email before it goes out.'),
        ('When should I rebuild my outbound instead of fixing it?',
         'Consider a rebuild when more than one of the six steps is broken at once, for example a damaged sending domain plus a list nobody trusts. Fixing one step at a time is slow when every step is affected.'),
    ],
}
