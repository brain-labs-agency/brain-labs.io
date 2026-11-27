# Spec for blog/when-to-stop-founder-led-sales.html. Build: python3 tools/blogkit.py tools/posts/when-to-stop-founder-led-sales.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


SF_SDR = 'https://signalfire.com/blog/when-to-hire-sales-development-representatives'
SF_FLS = 'https://www.signalfire.com/blog/moving-past-founder-led-sales'
SAASTR = 'https://www.saastr.com/why-founder-led-sales-breaks-earlier-than-you-think'
BCV = 'https://www.baincapitalventures.com/insight/founders-dont-hire-aes-until-youve-figured-out-how-to-sell-yourselves'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'

fig1 = figure(1, table(['Signal', 'What it looks like', 'What it usually means'], [
    ['<b>New bookings stop growing</b>', 'Revenue still rises, but each month adds about the same number of new deals', 'The founder\'s calendar is full. Pipeline is capped by one person\'s hours'],
    ['<b>Replies go unanswered</b>', 'Interested prospects wait days for an answer, or never get one', 'Selling is competing with product, hiring and fundraising, and losing'],
    ['<b>Outbound happens at night</b>', 'Prospecting only gets done after the real work, in bursts', 'The top of the funnel has no owner and no rhythm'],
    ['<b>Pipeline is lumpy</b>', 'A strong month after a conference, then a quiet one', 'Deals come from events and referrals, not from a steady motion'],
    ['<b>You can explain the win</b>', 'You know who buys, why they buy and what they say on the first call', 'The story is repeatable enough for someone else to tell it'],
]), 'Five signals that founder-led sales is reaching its limit. The first four say you need help; the last one says the help has something to work with. Built from the warning signs described by '
    + a(SAASTR, 'SaaStr') + ' and ' + a(BCV, 'Bain Capital Ventures') + '.')

fig2 = figure(2, table(['', 'First SDR in house', 'SDR hired from Latin America', 'Outsourced SDR agency', 'Agent Base (AI agents plus a manager)'], [
    ['<b>Who runs the day to day</b>', 'You', 'You', 'The agency', 'A dedicated Agent Base manager'],
    ['<b>Who you manage</b>', 'An early career rep, weekly', 'An early career rep, weekly, on your hours', 'An account manager', 'One point of contact'],
    ['<b>Who owns the playbook</b>', 'You', 'You', 'Shared', 'Shared, built on your story'],
    ['<b>Time before outreach starts</b>', 'Hiring cycle plus ramp', 'Faster sourcing, then ramp', 'Setup and warm up', 'About three weeks of setup and warm up'],
    ['<b>What you can see</b>', 'Your CRM', 'Your CRM', 'Usually a weekly report', 'A live dashboard'],
    ['<b>Best when</b>', 'You want the skill inside the company and have time to coach', 'Same, with US hours covered and a wider talent pool', 'You want meetings without managing a rep', 'You want research at scale with a person approving every email'],
]), 'Four ways to bring in outbound help after founder-led sales. None is right for every company; the deciding questions are who manages the work and who owns the playbook.')

fig3 = figure(3, steps('A 90 day handoff from founder-led sales', [
    ('Write it down', 'ICP, story, objections'),
    ('Define the meeting', 'what counts as qualified'),
    ('Shadow', 'they watch you sell'),
    ('Co-sell', 'you join their calls'),
    ('Hand off', 'weekly review only'),
], accent=('Define the meeting',)),
    'The handoff works best in stages. The step most teams skip is agreeing what a qualified meeting is before anyone books one. Co-selling for longer than feels necessary is normal; '
    + a(BCV, 'Bain Capital Ventures') + ' notes first hires often co-sell with the founder "for quite some time."')

POST = {
    'slug': 'when-to-stop-founder-led-sales',
    'title': 'When to stop founder-led sales and bring in outbound help',
    'h1': 'When to stop founder-led sales and bring in <em>outbound</em> help',
    'description': 'The signals that founder-led sales has hit its limit, what must be true before you hand off, the four ways to add outbound help, and a 90 day handoff plan.',
    'category': 'Outbound',
    'date': '2026-11-27',
    'date_label': 'November 27, 2026',
    'hero_img': 'cover-when-to-stop-founder-led-sales',
    'card_img': 'cover-when-to-stop-founder-led-sales',
    'card_title': 'When to stop founder-led sales and bring in outbound help',
    'card_text': 'The signals that you have become the bottleneck, what to have in place before you hand off, and how to do it without losing what made the first deals close.',
    'takeaways': [
        'Bring in outbound help when your sales are repeatable but capped by your own hours. The clearest sign is new bookings that stop growing while demand is still there.',
        'Do not hand off sales to fix them. If you cannot yet explain who buys and why, any hire or agency will run faster in the wrong direction.',
        'Before anyone else prospects for you, write down your ideal customer, your story, the common objections and what counts as a qualified meeting.',
        'There are four main ways to add help: a first SDR, an SDR hired from Latin America, an outsourced agency, or an Agent Base. Choose by who manages the work and who owns the playbook.',
    ],
    'intro': (
        '<p>Founder-led sales is how almost every B2B company gets its first customers, and for good reason. Nobody knows the product, the problem or the buyer better than the person who built the company. But there comes a point when the founder\'s calendar becomes the limit on growth. Prospecting happens late at night, replies sit unanswered, and the pipeline rises and falls with how busy the rest of the job is.</p>'
        '<p>This guide is about that point. It covers the signals that you have reached it, what must be in place before you hand anything off, the main ways to bring in outbound help, what you should keep doing yourself and a simple 90 day plan for the handoff. It is written for founders of US B2B companies who are still doing most of the selling themselves.</p>'
    ),
    'cta': {
        'inline_lead': 'Still doing outbound at night?',
        'inline_text': 'Book a 30 minute call about the Agent Base. We will look at your market and your story, and show you how the agents and a dedicated Agent Base manager would take prospecting off your plate while you stay on the calls that matter.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Keep closing. Let a <em>base</em> fill your calendar.',
        'band_text': 'Scout, Lens, Quill, Relay, Echo and Atlas find accounts with a reason to buy, research them, draft the emails and sort the replies. Your dedicated Agent Base manager approves every email before it reaches a buyer, and you watch it all on a live dashboard.',
    },
    'sections': [
        ('short-answer', 'The short answer: when to hand off', (
            '<p>Stop doing all of the selling yourself when two things are true at once: your sales are repeatable, and your own time has become the bottleneck. Repeatable without a bottleneck means you can keep going; a bottleneck without repeatability means you still have selling to figure out.</p>'
            '<p>Investors who work with early companies say the same thing in different words. ' + a(BCV, 'Bain Capital Ventures') + ' admits there is "no clean metric that says \'hire salespeople now\'" and quotes Decagon\'s CEO: "You should only hire if founder sales are going well and you feel like it\'s getting repeatable." Their summary is blunt: hire to scale what is working, not to figure out what might work.</p>'
            '<p>The second condition, the bottleneck, is easier to miss because it builds slowly. Jason Lemkin at ' + a(SAASTR, 'SaaStr') + ' argues founder-led sales usually stops scaling earlier than founders expect. His test is a simple question: are your new bookings still growing? He notes that founders often "push through flattening bookings for 6+ months" before they act, because the growth rate still looks fine on paper while the number of new deals each month has stopped rising.</p>'
            '<p>Put together, the decision looks like this:</p>'
            '<ul><li><b>Repeatable and capped by your time.</b> Bring in outbound help now. Every month you wait is pipeline you will not get back.</li>'
            '<li><b>Repeatable but you still have room.</b> Start preparing: document the story and the ideal customer so the handoff is fast when you need it.</li>'
            '<li><b>Not yet repeatable.</b> Keep selling yourself. Adding people or an agency will amplify the confusion, not fix it.</li></ul>'
        )),
        ('signals', 'Five signs founder-led sales has hit its limit', (
            '<p>The clearest sign is that new bookings flatten while demand is still there: people would buy, but nobody has time to find and talk to them. Four other signals usually show up at the same time, and one more tells you that you are ready to hand off.</p>'
            + fig1 +
            '<p>When product, hiring or fundraising get urgent, prospecting is the first thing to slip. Mintlify\'s co-founder told ' + a(BCV, 'Bain Capital Ventures') + ' that before their first sales hire they were "often dropping the ball, missing replies." That is what a capacity limit looks like from the inside.</p>'
            '<p>The fifth signal is different. It is not a problem but a precondition. If you can explain who buys, why they buy, what they say on the first call and which objections come up, you have something another person can carry. If you cannot, sell a little longer and take notes before you hand anything off.</p>'
        )),
        ('before-handoff', 'What must be true before you hand off', (
            '<p>Before anyone prospects on your behalf, you need a written ideal customer profile, a story that has closed deals, a list of common objections, a definition of a qualified meeting and the time to manage whoever takes over. Without these, any hire or partner is guessing.</p>'
            '<p>' + a(SF_SDR, 'SignalFire\'s guide on hiring a first SDR') + ' puts the risk well: without a defined customer and a repeatable process, an SDR will "let you run faster, but in the wrong direction." It suggests four questions before hiring: do you have a repeatable sales process, can you handle more sales meetings, do you have the bandwidth to manage a more junior employee, and does your go-to-market motion benefit from an SDR at all?</p>'
            '<p>Here is the minimum to have written down, in plain language, before the handoff:</p>'
            '<ul><li><b>Ideal customer profile.</b> Company type, size, region and the trigger that makes them likely to buy now. Include who signs and who uses the product.</li>'
            '<li><b>The story.</b> The problem in the buyer\'s words, why the old way fails and what changes with you. Two or three customer examples you are allowed to mention.</li>'
            '<li><b>Objections.</b> The five things prospects say most often, and how you answer them.</li>'
            '<li><b>A qualified meeting.</b> The role, fit and interest a prospect must show before a meeting counts, and who confirms it.</li>'
            '<li><b>Your funnel math.</b> Even rough numbers: how many first meetings become opportunities, and how many of those close.</li></ul>'
            '<p>The last item comes from Stripe\'s Jeanne DeWitt Grosser, who told ' + a(SF_FLS, 'SignalFire') + ' that founders should set up an operating model, "your funnel math in a large spreadsheet," before building a sales team. You do not need precision. You need enough to know whether a new source of meetings is working.</p>'
        )),
        ('options', 'Four ways to bring in outbound help', (
            '<p>There are four common ways to add outbound help: hire a first SDR in house, hire an SDR from Latin America, use an outsourced SDR agency, or use a managed system like the Agent Base. The right choice depends mostly on who will manage the work day to day and who will own the playbook.</p>'
            + fig2 +
            '<p><b>A first SDR in house</b> builds the skill inside your company, which matters if outbound will be a core channel for years. The cost is your time. SignalFire is direct about it: "If you can\'t make the time to manage an early career employee, don\'t hire an SDR." Plan for ramp too. The ' + a(BRIDGE, 'Bridge Group\'s 2025 SDR report') + ' puts average ramp at about three months.</p>'
            '<p><b>An SDR hired from Latin America</b> works the same way, with two differences: reps in cities like Bogotá and Lima work US Eastern hours on a normal schedule, and the pool of bilingual candidates is wide. You still manage and coach them. Our guide on <a href="/blog/hire-bilingual-sdr-latin-america">how to hire a bilingual SDR from Latin America</a> covers that path.</p>'
            '<p><b>An outsourced SDR agency</b> takes the management off your plate and can start faster. The trade-off is control: quality varies widely, and you depend on the agency to learn your story. We compare the two models in <a href="/blog/outsourced-sdr-vs-in-house-sdr">outsourced SDR vs in-house SDR</a>, and list what to ask in <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a>.</p>'
            '<p><b>The Agent Base</b> is how we run outbound at BL Agency. Agents find accounts with a reason to buy (Scout), research them (Lens), draft each email (Quill), send at a safe pace (Relay), sort replies (Echo) and brief each booked meeting (Atlas). A dedicated Agent Base manager reads and approves every email before it goes out, and you see all of it on a live dashboard. Setup and email warm up take about three weeks before campaigns start.</p>'
        )),
        ('keep-doing', 'What a founder should keep doing', (
            '<p>Handing off prospecting does not mean leaving sales. Keep running the first calls with your best-fit accounts, stay close to your largest customers and review the message every week. Founders who disappear from sales entirely lose the feedback that made the first deals close.</p>'
            '<p>Jeanne DeWitt Grosser puts it plainly in ' + a(SF_FLS, 'SignalFire\'s interview') + ': "founders should never fully remove themselves from sales."</p>'
            '<p>What to hand off first:</p>'
            '<ul><li><b>List building and research.</b> Finding companies that fit and the right person at each one. This is the most time-consuming part and the easiest to delegate.</li>'
            '<li><b>First touches and follow ups.</b> The emails, calls and LinkedIn messages that start conversations.</li>'
            '<li><b>Reply sorting and booking.</b> Separating real interest from out-of-office notes and not-now replies, and getting meetings on the calendar.</li></ul>'
            '<p>What to keep, at least for now:</p>'
            '<ul><li><b>The first call with high-fit accounts.</b> Your credibility as a founder is an asset in early deals.</li>'
            '<li><b>Message ownership.</b> Read a sample of outgoing emails every week and listen to a few calls. If the story drifts, you will hear it first.</li>'
            '<li><b>The qualified meeting definition.</b> Review it with whoever books meetings, monthly at first. Most disputes with outbound help are really disputes about this definition.</li></ul>'
            '<p>This is also why we built the Agent Base around a person and a live dashboard. A founder should be able to see what is being sent in their name and why, without asking for a report.</p>'
        )),
        ('handoff-plan', 'A 90 day handoff plan', (
            '<p>A good handoff runs in five stages over roughly 90 days: write down how you sell, define a qualified meeting, let the new person or partner watch you sell, co-sell, and then step back to a weekly review. Skipping stages is the most common reason handoffs fail.</p>'
            + fig3 +
            '<p><b>Days 1 to 15: write it down.</b> Turn what is in your head into a short document: the ideal customer, the story, the objections and the funnel math from the previous sections.</p>'
            '<p><b>Days 15 to 30: define the meeting and set up.</b> Agree in writing what counts as a qualified meeting and who confirms it. If email is part of the plan, this is also when domains and mailboxes are set up and warmed, which takes weeks, not days. Calling and LinkedIn can start earlier.</p>'
            '<p><b>Days 30 to 60: shadow, then co-sell.</b> Whoever books meetings should hear how those meetings go. Invite them to your calls, then join theirs. ' + a(BCV, 'Bain Capital Ventures') + ' describes one founder who joined calls "3-4 hours a day for the first three months" after the first hires.</p>'
            '<p><b>Days 60 to 90: hand off and review.</b> Step out of the daily work and into a weekly review: meetings booked and held, what prospects are saying, which messages get replies and which objections are new. Adjust the story and the targeting from what you hear.</p>'
            '<p>For an in-house hire, pair this with a structured onboarding. Our <a href="/blog/sdr-onboarding-plan">SDR onboarding plan for the first 30, 60 and 90 days</a> goes into the detail.</p>'
        )),
        ('mistakes', 'Mistakes founders make in the transition', (
            '<p>The most common mistakes are handing off sales before they are repeatable, hiring a junior rep with nobody to manage them, judging results in the first few weeks, and stepping away from sales completely. Each one is avoidable with a little planning.</p>'
            '<ul><li><b>Hiring to fix broken sales.</b> If deals do not close when you run them, they will not close when someone else does. Bain Capital Ventures\' advice is short: "Don\'t hire to fix broken sales."</li>'
            '<li><b>No manager for the first SDR.</b> An early career rep needs weekly coaching, call reviews and a clear plan. Without them, the role fails and the founder concludes that outbound does not work.</li>'
            '<li><b>Expecting results in week one.</b> New reps take months to ramp, and email needs weeks of warm up before campaigns start. SignalFire notes that a strong outbound capability can take a minimum of two years to build. Judge the first quarter on learning and early meetings, not on closed revenue.</li>'
            '<li><b>Leaving entirely.</b> The founder\'s voice is part of what made early deals close. Stay in the review, stay on key calls and stay close to customers.</li></ul>'
            '<p>The ' + a(BRIDGE, 'Bridge Group\'s 2025 data') + ' is a useful reality check here: only about 60% of SDRs hit quota, and the median quota is around ten held meetings a month. Set expectations with that in mind, and adjust them as soon as you have your own numbers.</p>'
        )),
    ],
    'conclusion': (
        '<p>Founder-led sales is not a phase to escape as early as possible. It is where your story, your ideal customer and your first proof come from. The time to bring in outbound help is when that story is repeatable and your own hours have become the limit on growth.</p>'
        '<p>To recap:</p>'
        '<ol><li><b>Check both conditions.</b> Repeatable sales and a capacity bottleneck, at the same time.</li>'
        '<li><b>Watch the signals.</b> Flat new bookings, missed replies, outbound at night and a lumpy pipeline.</li>'
        '<li><b>Write it down first.</b> Ideal customer, story, objections, qualified meeting and funnel math.</li>'
        '<li><b>Pick the model by who manages it.</b> In-house SDR, an SDR from Latin America, an agency or an Agent Base.</li>'
        '<li><b>Hand off in stages.</b> Shadow, co-sell, then step back to a weekly review.</li>'
        '<li><b>Stay in sales.</b> Keep the key calls, the message and the customers.</li></ol>'
        '<p>If you recognize the signals and want to see what the Agent Base would look like for your market, <a href="' + CAL + '"' + EXT + '>book a call</a>. We will walk through your story and show you where the agents and your dedicated Agent Base manager would take over.</p>'
    ),
    'faq': [
        ('When should a founder stop doing sales?',
         'A founder should stop doing all of the selling when sales are repeatable and their own time has become the bottleneck. They should not stop selling entirely; most advisors recommend staying on key calls and close to the largest customers.'),
        ('What is the clearest sign founder-led sales has hit its limit?',
         'New bookings that stop growing while demand is still there. SaaStr\'s Jason Lemkin suggests asking whether new bookings are still growing, not only whether revenue is.'),
        ('Should my first sales hire be an SDR or an account executive?',
         'It depends on where the bottleneck is. If you close well but lack conversations, an SDR or outbound help fills the calendar. If you have more conversations than you can handle, an account executive helps. Our guide <a href="/blog/hire-sdr-or-ae-first">should a founder hire an SDR or an AE first</a> goes deeper.'),
        ('Can I hand off outbound before I have product-market fit?',
         'It is risky. Without a repeatable story, outbound help tends to test messages at scale instead of booking qualified meetings. Most advisors recommend founders sell until they can explain who buys and why.'),
        ('How long does the handoff take?',
         'Plan for about 90 days from documenting how you sell to stepping back to a weekly review. A new in-house SDR takes about three months to ramp on average, and email outreach needs a few weeks of setup and warm up first.'),
        ('Is an outsourced team or an AI system better than hiring an SDR?',
         'Neither is better for everyone. An in-house SDR builds the skill inside the company but needs your management time. An agency or a managed system like the Agent Base removes that management load. Choose by who will run the work and who owns the playbook.'),
        ('What should a founder keep doing after handing off outbound?',
         'Keep the first call with high-fit accounts, review outgoing messages and calls every week, stay in contact with your largest customers and own the definition of a qualified meeting.'),
    ],
}
