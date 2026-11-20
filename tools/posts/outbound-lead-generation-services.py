# Spec for blog/outbound-lead-generation-services.html. Build: python3 tools/blogkit.py tools/posts/outbound-lead-generation-services.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GARTNER_2026 = 'https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience'
GARTNER_2025 = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
GARTNER_VALIDATE = 'https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights'
GOOGLE = 'https://support.google.com/mail/answer/81126?hl=en'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'

fig1 = figure(1, table(['Part of the service', 'What it covers', 'What to ask'], [
    ['<b>Market mapping and ICP</b>', 'Which companies and which people you go after, and why', 'Who writes the ideal customer profile, and do I sign it off?'],
    ['<b>Data and research</b>', 'Building the list, verifying contacts, finding a reason to reach out to each account', 'Where does the data come from, and how is it checked before anyone is contacted?'],
    ['<b>Sending infrastructure</b>', 'Separate domains, mailboxes, authentication and warm up', 'Whose name are the domains in, and what happens to them if we stop?'],
    ['<b>Messaging</b>', 'First emails, follow ups, call openers and LinkedIn notes', 'Who writes them, and does a person read each one before it is sent?'],
    ['<b>Channels</b>', 'Email, phone, LinkedIn, and how they are combined', 'Which channels are included, and how do you choose them per account?'],
    ['<b>Reply handling</b>', 'Reading replies, answering questions, handling objections', 'How fast does an interested reply get a human answer?'],
    ['<b>Meeting booking</b>', 'Scheduling, confirmations and a brief for your team', 'What does my team receive before each meeting?'],
    ['<b>Reporting</b>', 'Activity, replies, meetings booked and meetings held', 'Can I see the work as it happens, or only in a monthly report?'],
]), 'The eight parts of a complete outbound lead generation service, what each covers, and one question that tells you whether it is really included.')

fig2 = figure(2, bar_chart('What B2B buyers say about sellers and outreach', [
    ('Prefer rep-free buying', 67),
    ('Avoid irrelevant suppliers', 73),
    ('Used AI in a recent purchase', 45),
    ('Check AI with a rep', 69),
], unit='%', vmax=100, highlight=('Avoid irrelevant suppliers',)),
    'Buyers want fewer, better conversations with sellers, and they punish irrelevant outreach. Sources: '
    + a(GARTNER_2026, 'Gartner, March 2026') + ' (646 B2B buyers), '
    + a(GARTNER_2025, 'Gartner, June 2025') + ' (632 B2B buyers) and '
    + a(GARTNER_VALIDATE, 'Gartner, May 2026') + ' (645 B2B buyers).')

fig3 = figure(3, timeline('What the first twelve weeks of a new outbound program look like', [
    (0, 3, 'Setup and warm up', 'ICP, data, mailboxes'),
    (3, 6, 'First campaigns', 'low volume, all replies read'),
    (6, 9, 'Tune', 'targeting and copy'),
    (9, 12, 'Steady pipeline', 'regular meetings'),
], 12, unit='wk', accent=('Setup and warm up',)),
    'A typical shape for the first quarter. Setup and mailbox warm up alone take about three weeks, which is why a provider that promises meetings in week one is either skipping steps or sending from domains that are not yours.')

POST = {
    'slug': 'outbound-lead-generation-services',
    'title': 'Outbound lead generation services: what is included and what to ask',
    'h1': 'Outbound lead generation services: what is <em>included</em> and what to ask',
    'description': 'What an outbound lead generation service should include, from ICP and data to domains, messaging, replies and booked meetings, how the main service models differ, and the questions to ask before you sign.',
    'category': 'Outbound',
    'date': '2026-11-20',
    'date_label': 'November 20, 2026',
    'hero_img': 'blog-outbound-services',
    'card_img': 'blog-outbound-services',
    'card_title': 'Outbound lead generation services: what is included and what to ask',
    'card_text': 'The eight parts a complete service covers, how the models differ, and how to tell what you are really buying.',
    'takeaways': [
        'An outbound lead generation service finds the companies that fit your offer, contacts the right people by email, phone or LinkedIn, and books qualified meetings on your calendar.',
        'A complete service covers eight parts: ICP, data and research, sending infrastructure, messaging, channels, reply handling, meeting booking and reporting. Many offers leave two or three out.',
        'The biggest differences between providers are who writes and reviews the messages, whose domains and data you keep, and whether you can see the work as it happens.',
        'Judge a provider on qualified meetings held, not activity. Agree what "qualified" means in writing before the first email goes out.',
    ],
    'intro': (
        '<p>"Outbound lead generation services" covers a wide range of offers. One provider sells you a list of contacts. Another runs email sequences from domains it owns. A third runs your whole outbound function, from choosing the market to putting a qualified meeting on your calendar. All three use the same words on their website.</p>'
        '<p>This guide breaks the service into its parts so you can see what a complete one includes, how the main delivery models compare, what results to hold a provider to, and which questions show you what you are actually buying. It is written for founders and sales leaders at US B2B companies who are comparing providers or deciding whether to buy outbound at all.</p>'
    ),
    'cta': {
        'inline_lead': 'Want to see a complete outbound service working?',
        'inline_text': 'Book a 30 minute call. We will walk you through the Agent Base on a live dashboard: the agents that research and draft, and the dedicated Agent Base manager who approves every email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound, done for you, with a person <em>signing off</em>.',
        'band_text': 'Market mapping, domains and warm up, research, writing, replies and booked meetings. Scout, Lens, Quill, Relay, Echo and Atlas do the volume work, and your dedicated Agent Base manager approves every email. You watch it all on a live dashboard.',
    },
    'sections': [
        ('what-it-is', 'What an outbound lead generation service is', (
            '<p>An outbound lead generation service is an outside team that starts conversations with companies that have not contacted you yet, and turns the interested ones into qualified sales meetings. It handles the work before the first call: who to target, how to reach them, what to say and how to follow up.</p>'
            '<p>The key word is outbound. Inbound lead generation waits for buyers to find you through search, ads or content. Outbound goes to them. That makes it the right tool when you know who your best customers are but there are not enough of them finding you on their own, or when you sell into a market where buyers rarely search for a solution until someone gives them a reason.</p>'
            '<p>It is also different from the services it often gets confused with:</p>'
            '<ul><li><b>Data providers</b> sell contact lists and enrichment. You still need someone to research, write, send and follow up.</li>'
            '<li><b>Email tools</b> send sequences. They do not decide who to target or what a good reason to reach out looks like.</li>'
            '<li><b>Appointment setting services</b> often focus on the last step, booking calls, and may work from a list you provide.</li>'
            '<li><b>Outsourced SDR programs</b> put trained reps on your outbound. We compare that model in detail in <a href="/blog/outsourced-sdr-vs-in-house-sdr">outsourced SDR vs in-house SDR</a> and <a href="/blog/sdr-as-a-service">what SDR as a Service means</a>.</li></ul>'
            '<p>A full outbound lead generation service combines all of these. The useful question is not which label a provider uses, but which parts of the work it actually takes off your plate. The next section lists them.</p>'
        )),
        ('whats-included', 'What a complete service includes: the eight parts', (
            '<p>A complete outbound service covers eight parts, from deciding who to target to reporting on meetings held. If a provider leaves one out, that work either falls back on your team or does not get done.</p>'
            + fig1 +
            '<p>Three of these parts are where offers differ most.</p>'
            '<p><b>Data and research.</b> A list is not research. A list tells you a company exists and who works there. Research tells you why that company might care right now: a new hire in the role you sell to, an expansion, a product launch, a change in regulation. Without a reason, the email is a template with a name on it.</p>'
            '<p><b>Messaging and review.</b> Many services now draft emails with AI. That is fine for speed. What matters is whether a person who understands your buyer reads each message before it is sent. We cover why in <a href="/blog/ai-sdr-vs-human-sdr">AI SDR vs human SDR</a>. A service that sends AI drafts without review is fast, and it is your company name on every mistake.</p>'
            '<p><b>Reply handling.</b> Booking a meeting usually takes more than one reply. Someone has to answer questions, handle a "not now", route a referral to the right colleague and confirm the time. Ask who does this and how quickly. A positive reply that sits unanswered for a day is often a lost meeting.</p>'
            '<p>The other parts are less visible but just as important. Sending infrastructure decides whether your emails reach the inbox at all. Reporting decides whether you can tell what is working. Meeting booking decides whether your team walks into each call prepared or starting from zero.</p>'
        )),
        ('models', 'The main service models and how they differ', (
            '<p>Outbound services come in four main models: done for you, tool led, staffing and hybrid. They differ in who does the thinking, who does the work and how much of your own time they need.</p>'
            '<ul><li><b>Done for you.</b> The provider runs the full outbound function: targeting, data, writing, sending, replies and booking. You approve the ICP and the voice, then take the meetings. This needs the least of your team\'s time and puts the most trust in the provider.</li>'
            '<li><b>Tool led.</b> You get software, sometimes with an AI agent that researches and writes, plus setup help. Your team runs it. This works when you already have someone who knows outbound and wants to scale their own work.</li>'
            '<li><b>Staffing.</b> The provider places a rep, often an SDR, who works inside your team and your tools. You manage them. This gives you the most control and needs the most management. We cover hiring in <a href="/blog/hire-bilingual-sdr-latin-america">how to hire a bilingual SDR from Latin America</a>.</li>'
            '<li><b>Hybrid.</b> AI agents do the volume work of research, drafting and sorting replies, and a dedicated person reviews every message and handles the conversations. This is where most of the market has moved in 2026, because it keeps the speed of AI and the judgment of a person.</li></ul>'
            '<p>Commercial models vary too. Some providers charge a monthly fee for a defined scope of work. Others charge per lead or per booked meeting, or mix a base fee with a performance part. Each one rewards something different. A per-meeting model rewards booked meetings, so check how it treats meetings that do not show up or do not fit. A monthly model rewards doing the work well over time, so check what reporting and exit terms protect you.</p>'
            '<p>None of these is right for every company. A useful test is to ask where your bottleneck is. If you have no one who knows outbound, start done for you or hybrid. If you have a strong outbound lead who is out of hours, a tool may be enough. If you want a long-term team member, staffing fits. For founders weighing the first hire, see <a href="/blog/hire-sdr-or-ae-first">should you hire an SDR or an AE first</a>.</p>'
        )),
        ('why-quality', 'Why the quality of outreach matters more than volume', (
            '<p>Quality matters more than volume because buyers now do most of their research without sellers and actively avoid companies that contact them with irrelevant messages. A service that sends more emails to more people often makes your results worse, not better.</p>'
            '<p>Gartner\'s buyer research shows the shift clearly. In a ' + a(GARTNER_2026, 'March 2026 survey of 646 B2B buyers') + ', 67% said they prefer a rep-free buying experience, and 45% had used AI during a recent purchase. In its ' + a(GARTNER_2025, '2025 survey of 632 buyers') + ', 73% said they actively avoid suppliers who send irrelevant outreach.</p>'
            + fig2 +
            '<p>That does not mean buyers never want to talk to a seller. The same 2025 research found buyers still prefer a seller for questions about fit and their own context, and a ' + a(GARTNER_VALIDATE, 'May 2026 Gartner survey') + ' found 69% prefer to check AI-generated insights with a sales rep. Buyers want fewer conversations, and they want each one to be worth their time.</p>'
            '<p>For an outbound service, that changes what good looks like:</p>'
            '<ul><li><b>Fewer accounts, better reasons.</b> Start where there is a signal and a contact who owns the problem, not across an entire list.</li>'
            '<li><b>The right channel for each buyer.</b> Some buyers answer the phone, some live on LinkedIn, some only read email. A good service finds out where each one can be reached before writing anything.</li>'
            '<li><b>Messages a person would send.</b> Short, specific, with one clear ask. If a message would not survive being read aloud to the prospect, it should not be sent.</li></ul>'
            '<p>When you compare providers, ask how many accounts they plan to contact and why those ones. A thoughtful answer about targeting is a better sign than a big number.</p>'
        )),
        ('domains-and-data', 'Your domain, your data and what you keep', (
            '<p>Before you sign, find out whose domains the emails are sent from, who owns the data and the conversations, and what you keep if you stop. These details decide whether the work builds an asset for your company or for the provider.</p>'
            '<p><b>Sending domains.</b> Most outbound teams send from separate domains that look like yours, so that cold outreach never puts your main company domain at risk. That is good practice. The question is who owns those domains and mailboxes. If the provider owns them, the reputation you built leaves with them.</p>'
            '<p><b>Warm up and volume.</b> New mailboxes need a few weeks of gradual, low volume sending before campaigns start. Mailbox providers also watch how recipients react. ' + a(GOOGLE, 'Google\'s sender guidelines') + ' ask senders to keep the spam rate reported in Postmaster Tools below 0.3% and recommend staying under 0.1%. A provider that talks about volume and never mentions spam rates, authentication or warm up is a risk to your deliverability.</p>'
            + fig3 +
            '<p><b>Data and conversation history.</b> The list of accounts researched, the contacts verified, every message sent and every reply received should live in your CRM or be exportable to it. If you change provider or bring outbound in house, that history is what lets the next team start in week four instead of week zero.</p>'
            '<p><b>Exit terms.</b> Ask what notice is required, what is handed over and in what format, and whether there are any restrictions on contacting accounts the provider worked. Clear exit terms are a sign of a provider that expects to keep you because the work is good, not because leaving is hard.</p>'
            '<p>In the Agent Base, mailboxes are set up and warmed before campaigns start, volume stays sensible, and every lead, email, reply and meeting appears on a live dashboard you can open any time.</p>'
        )),
        ('results', 'What results to hold a provider to', (
            '<p>Hold a provider to qualified meetings held with the right people, measured against a definition you agreed before launch. Activity numbers such as emails sent or calls made show effort, not results.</p>'
            '<p>Most disputes between companies and outbound providers come down to definitions. Was the meeting qualified? Did it actually happen? Was the person someone who could buy? Settle these in writing during onboarding:</p>'
            '<ul><li><b>Qualified.</b> Company size, industry, region and the role of the person who attends. Add any must-have, such as a current tool or an active project.</li>'
            '<li><b>Held, not booked.</b> A booked meeting that does not happen should not count. Ask how the provider confirms meetings and what it does about no-shows.</li>'
            '<li><b>Handoff.</b> What your team receives before the call: who the person is, why they were contacted and what they said.</li>'
            '<li><b>Reporting rhythm.</b> Weekly at minimum, with the reply rate, positive replies, meetings booked, meetings held and the reasons people said no.</li></ul>'
            '<p>Give it time, too. A new program needs a few weeks to set up and a few more to learn what lands with your market. Building an in-house SDR team takes time as well: the ' + a(BRIDGE, 'Bridge Group\'s 2025 SDR report') + ', which surveyed 351 B2B companies, puts average SDR ramp time at about three months. An outbound service will not skip learning your market, but it should show you what it is learning every week.</p>'
            '<p>Finally, ask for the reasons behind the numbers. A good provider tells you which segments reply, which messages fall flat and what buyers say when they decline. That feedback is often worth as much as the meetings, because it sharpens your positioning for the whole sales team.</p>'
        )),
        ('questions', 'Questions to ask before you sign', (
            '<p>The best questions make the provider show you its work, not describe it. Ask to see a live account, real messages and real reports, with client details removed.</p>'
            '<ol><li><b>Which of the eight parts do you handle, and which stay with us?</b> Get it in writing.</li>'
            '<li><b>Who decides which accounts we target, and can I approve the list?</b></li>'
            '<li><b>How do you find a reason to contact each account?</b> Ask for three examples from a current campaign.</li>'
            '<li><b>Does a person read every message before it is sent, or a sample?</b> Ask who, and how many clients they cover.</li>'
            '<li><b>Which channels do you use, and how do you choose them per buyer?</b></li>'
            '<li><b>Whose name are the domains and mailboxes in, and what happens to them if we leave?</b></li>'
            '<li><b>How fast does an interested reply get a human answer?</b></li>'
            '<li><b>How do you define a qualified meeting, and do you count meetings booked or held?</b></li>'
            '<li><b>Can I see the work as it happens?</b> A live dashboard is easier to trust than a monthly slide.</li>'
            '<li><b>What do we keep when the engagement ends?</b> Data, conversations, domains, playbooks.</li></ol>'
            '<p>For a longer checklist on vetting providers, including references and contract terms, see <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a>. If a provider is vague on more than two of the questions above, keep looking.</p>'
        )),
    ],
    'conclusion': (
        '<p>Outbound lead generation services share a name but not a scope. The way to compare them is to break the service into its parts and ask who does each one, how well and where you can see it.</p>'
        '<ol><li><b>Know the category:</b> outbound means starting conversations with buyers who have not found you yet and turning the interested ones into qualified meetings.</li>'
        '<li><b>Check all eight parts:</b> ICP, data and research, infrastructure, messaging, channels, replies, booking and reporting.</li>'
        '<li><b>Pick the model for your bottleneck:</b> done for you, tool led, staffing or hybrid.</li>'
        '<li><b>Favor quality over volume:</b> buyers avoid irrelevant outreach, so reasons and review matter more than send counts.</li>'
        '<li><b>Protect your assets:</b> domains, data and conversation history should stay with you.</li>'
        '<li><b>Measure meetings held:</b> against a written definition of qualified, reported every week.</li>'
        '<li><b>Ask to see the work:</b> live accounts, real messages and real reports.</li></ol>'
        '<p>If you want to see what a complete, hybrid service looks like, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will show you the Agent Base on a live dashboard.</p>'
    ),
    'faq': [
        ('What is included in outbound lead generation services?',
         'A complete service covers market mapping and the ideal customer profile, data and account research, sending domains and mailboxes, messaging, the outreach channels, reply handling, meeting booking and reporting. Many offers cover only some of these, so ask which parts stay with your team.'),
        ('What is the difference between inbound and outbound lead generation?',
         'Inbound waits for buyers to find you through search, ads or content. Outbound contacts companies that fit your offer before they reach out, by email, phone or LinkedIn, and turns the interested ones into meetings.'),
        ('Is an outbound lead generation agency the same as an appointment setting company?',
         'Not always. Appointment setting companies often focus on booking calls, sometimes from a list you provide. A full outbound service also decides who to target, researches each account, runs the sending infrastructure and writes the messages.'),
        ('How long does it take for an outbound service to produce meetings?',
         'Setup and mailbox warm up usually take about three weeks. After that, first campaigns run at low volume while targeting and messaging are tuned, and a steady rhythm of meetings typically builds over the following weeks.'),
        ('Should outbound emails be sent from my main domain?',
         'Usually not. Most teams send cold outreach from separate domains that look like the main one, so the main company domain is protected. Make sure those domains and mailboxes are in your name.'),
        ('How should I measure an outbound lead generation provider?',
         'Measure qualified meetings held with the right people, using a definition you agree before launch. Also track reply rate, positive replies and the reasons buyers decline, and ask for a weekly report.'),
        ('How does the Agent Base work?',
         'AI agents find accounts with a reason to buy, research them, draft emails, send at a safe pace, sort replies and prepare meeting briefs. A dedicated Agent Base manager reads and approves every email and handles the replies that need a person, and you can watch it all on a live dashboard.'),
    ],
}
