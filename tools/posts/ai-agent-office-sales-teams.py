# Spec for blog/ai-agent-office-sales-teams.html. Build: python3 tools/blogkit.py tools/posts/ai-agent-office-sales-teams.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


PIXEL = 'https://github.com/pixel-agents-hq/pixel-agents'
HAI = 'https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior'
PAPER = 'https://arxiv.org/abs/2304.03442'
HBR = 'https://fortune.com/2025/12/09/harvard-business-review-survey-only-6-percent-companies-trust-ai-agents/'
MCK = 'https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/state-of-ai-trust-in-2026-shifting-to-the-agentic-era'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027'

fig1 = figure(1, table(['How you see the agents', 'What it tells you', 'What it misses'], [
    ['<b>Monthly or weekly report</b>', 'Totals: emails sent, replies, meetings booked', 'What happened in between, and why a number moved'],
    ['<b>Raw activity log</b>', 'Every action, with a timestamp', 'Context. Hard to read, so in practice nobody reads it'],
    ['<b>Visual office or base</b>', 'Which agent is working, on what, and which one is waiting or stuck', 'Quality. A busy character can still be doing the wrong thing'],
    ['<b>Visual view plus a human approval step</b>', 'Who is doing what, and what a person approved before it reached a buyer', 'Very little. This is the setup to ask for'],
]), 'Four ways to see what sales agents are doing. A visual view is a big step up from a report, but it only becomes real oversight when a person signs off on what goes out.')

fig2 = figure(2, bar_chart('How much companies trust AI agents with their processes', [
    ('Fully trust on core processes', 6),
    ('Only limited, routine tasks', 43),
    ('Supervised or non-core only', 39),
], unit='%', vmax=60, highlight=('Fully trust on core processes',)),
    'Share of 603 business and technology leaders, surveyed in July 2025 by Harvard Business Review Analytic Services. Source: '
    + a(HBR, 'Fortune, December 2025') + '.')

fig3 = figure(3, steps('Who does what in the Agent Base, from signal to meeting', [
    ('Scout', 'finds the account'),
    ('Lens', 'researches it'),
    ('Quill', 'drafts'),
    ('Manager', 'approves'),
    ('Relay', 'sends'),
    ('Echo', 'sorts replies'),
    ('Atlas', 'briefs'),
], accent=('Manager',)),
    'Each agent has one visible job, and the dedicated Agent Base manager (a person) sits in the middle of the line. Nothing reaches a buyer until that step is done.')

POST = {
    'slug': 'ai-agent-office-sales-teams',
    'title': 'AI agent offices: what the visual agent trend means for sales teams',
    'h1': 'AI agent offices: what the <em>visual</em> agent trend means for sales teams',
    'description': 'Why developers started watching their AI agents work in pixel art offices, what a visual view shows that a report does not, and what sales teams should ask for when AI agents run their outbound.',
    'category': 'AI agents',
    'date': '2026-11-23',
    'date_label': 'November 23, 2026',
    'hero_img': 'blog-agent-office',
    'card_img': 'blog-agent-office',
    'card_title': 'AI agent offices: what the visual agent trend means for sales teams',
    'card_text': 'Developers now watch their agents work in tiny offices. Here is why that matters for anyone running AI in outbound.',
    'takeaways': [
        'An "AI agent office" shows each AI agent as a character in a small virtual workspace, so you can see at a glance which agent is working, which is waiting and which is stuck.',
        'The trend took off because agents are hard to trust when you cannot see them. Only 6% of leaders in a 2025 HBR survey fully trust AI agents with core processes.',
        'For sales teams the stakes are higher than for developers: an outbound agent acts in public, in front of your buyers, under your company name.',
        'A visual view is useful, but it is not oversight on its own. Ask for named agent roles, a live activity feed and a person who approves every email before it is sent.',
    ],
    'intro': (
        '<p>In 2026 a strange kind of screenshot started showing up in developer feeds: tiny pixel art offices where little characters walk to their desks, type, read and raise a hand when they need help. Each character is an AI agent doing real work. People who run several agents at once found it easier to watch them this way than to read through terminal logs.</p>'
        '<p>It looks like a toy, and partly it is. But it points at a real problem that every company using AI agents has, including sales teams running AI in their outbound: if you cannot see what your agents are doing, you cannot trust them, and you cannot fix them. This guide explains where the trend came from, what a visual view actually gives you, and what to ask for if AI agents are writing to your buyers.</p>'
    ),
    'cta': {
        'inline_lead': 'Want to see sales agents working in the open?',
        'inline_text': 'Book a 30 minute call. We will show you the Agent Base on a live dashboard: each agent at its station, the activity feed, and the dedicated Agent Base manager who approves every email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'AI agents you can <em>watch</em>, with a person who signs off.',
        'band_text': 'Scout, Lens, Quill, Relay, Echo and Atlas do the volume work of outbound, and your dedicated Agent Base manager approves every email before it reaches a buyer. Every lead, email, reply and meeting shows up on a live dashboard as it happens.',
    },
    'sections': [
        ('what-it-is', 'What an AI agent office is', (
            '<p>An AI agent office is a visual interface that shows each AI agent as a character in a shared virtual space, with its current activity acted out on screen. Instead of reading logs, you look at the room and see who is busy, who is idle and who is waiting for you.</p>'
            '<p>The best known example is ' + a(PIXEL, 'Pixel Agents') + ', an open source project that, in its own words, turns the AI coding agents running in your terminals into animated pixel art characters working in a tiny office. Agents walk to their desks, type when they are editing files, read when they are searching, and show a speech bubble when they are waiting for input or permission. It runs as a VS Code extension or a small command line tool, works with Claude Code today, and lists other coding agents on its roadmap. At the time of writing the repository had close to ten thousand stars on GitHub, which is a lot of attention for something that, strictly speaking, adds no new capability.</p>'
            '<p>The idea is older than the trend. In 2023, Stanford and Google researchers published ' + a(PAPER, 'Generative Agents') + ', in which 25 AI agents with short biographies lived in a small game-like town called Smallville for two simulated days. They planned their days, talked to each other and remembered what happened. ' + a(HAI, 'Stanford HAI') + ' described it as believable humanlike behavior, and the pixel town became the picture most people still have in mind when they hear "AI agents".</p>'
            '<p>What is new in 2026 is that the agents in these offices are not a research simulation. They are doing paid work: writing code, researching, drafting documents and, increasingly, running parts of the sales process. That is why the visual layer stopped being a curiosity and started being a feature people ask for.</p>'
        )),
        ('why-now', 'Why the trend took off: agents are hard to trust when you cannot see them', (
            '<p>The trend took off because companies are deploying agents faster than they are learning to trust them, and a visible agent is easier to trust than an invisible one. Seeing an agent stuck, or working on the wrong thing, is the first step to correcting it.</p>'
            '<p>The trust gap is well documented. In a ' + a(HBR, 'Harvard Business Review Analytic Services survey') + ' of 603 business and technology leaders, reported by Fortune in December 2025, only 6% said they fully trust AI agents to run core business processes on their own. Most limit agents to routine tasks or supervised use, and only 12% said their risk and governance controls were fully in place.</p>'
            + fig2 +
            '<p>McKinsey found a similar picture in its ' + a(MCK, '2026 AI trust research') + ', based on a survey of about 500 organizations: nearly two thirds named security and risk concerns as the top barrier to scaling agentic AI, and 74% rated inaccuracy as a highly relevant risk. Organizations with clear ownership of responsible AI scored much higher on maturity than those without it.</p>'
            '<p>Gartner went further. In June 2025 it ' + a(GARTNER, 'predicted that over 40% of agentic AI projects will be canceled by the end of 2027') + ', citing rising costs, unclear business value and weak risk controls.</p>'
            '<p>Put those together and the appeal of the pixel office is obvious. It answers the most basic question a manager has about any worker, human or not: what are you doing right now? A view that answers that question at a glance lowers the cost of supervision, and supervision is exactly what most companies say they still need.</p>'
        )),
        ('what-it-shows', 'What a visual view shows that a report does not', (
            '<p>A visual view shows the state of the work while it is happening: which agent is active, what it is working on, and where something is waiting on a person. A report shows only the totals, after the fact, when it is too late to step in.</p>'
            '<p>Most AI sales tools still report the way old outbound agencies did: a dashboard of totals, or a weekly summary. Emails sent, open rate, replies, meetings. Those numbers are useful, but they hide the questions that matter most when something goes wrong. Why did replies drop on Tuesday? Which accounts did the agent skip? Is it waiting for an approval nobody has seen?</p>'
            + fig1 +
            '<p>Three states are especially valuable to see:</p>'
            '<ul><li><b>Waiting.</b> An agent that needs input and is not getting it is the most common silent failure. Pixel Agents shows it as a speech bubble for a reason. In sales, a draft waiting for approval or a hot reply waiting for an answer loses value by the hour.</li>'
            '<li><b>Stuck or looping.</b> An agent repeating the same step, or stopping on an error, looks busy in a total and obvious in a visual view.</li>'
            '<li><b>Handoffs.</b> When one agent passes work to another, such as research to drafting, you can see whether the handoff happened and what was passed along.</li></ul>'
            '<p>None of this needs pixel art. A clean activity feed with one line per action does the same job. The characters simply make it easier to keep the view open all day, which is the point: oversight only works if someone actually looks.</p>'
        )),
        ('sales-is-different', 'Why it matters more in sales than in coding', (
            '<p>It matters more in sales because a sales agent acts in public. A coding agent\'s mistake usually stays in a draft until a developer reviews it, while an outbound agent\'s mistake lands in a buyer\'s inbox with your name on it.</p>'
            '<p>Think about what an AI agent does in a typical outbound setup. It picks which companies to contact, decides who at each company to write to, finds a reason to reach out, writes the message, sends it and reads the replies. Each of those steps can go wrong in a way that a buyer sees:</p>'
            '<ul><li><b>Wrong account.</b> A company that is not a fit, or worse, a current customer or a competitor.</li>'
            '<li><b>Wrong reason.</b> A "congratulations on the funding round" about news that is a year old, or about a different company with a similar name.</li>'
            '<li><b>Wrong tone.</b> Copy that sounds automated, overfamiliar or simply off for the buyer\'s industry.</li>'
            '<li><b>Wrong reply.</b> An automatic answer to someone who asked to be removed, or a pushy follow up to a polite "not now".</li></ul>'
            '<p>A developer can afford to let an agent run for an hour and review the result. A sales team usually cannot. By the time a weekly report arrives, a bad sequence may have reached hundreds of buyers and hurt the reputation of your sending domains. We covered how that plays out in <a href="/blog/are-ai-sdrs-worth-it">are AI SDRs worth it</a> and in <a href="/blog/ai-sdr-vs-human-sdr">AI SDR vs human SDR</a>.</p>'
            '<p>That is why the visual agent trend is more than a design fashion for sales teams. It is a reminder that agents working on your revenue should be visible, and that the most important thing to see is the moment before a message leaves the building.</p>'
        )),
        ('what-to-ask-for', 'What to ask for when AI agents run your outbound', (
            '<p>Ask for three things: agents with named, narrow jobs; a live view of what each one is doing; and a person who approves every message before it is sent. The first two make the work visible, and the third makes it safe.</p>'
            '<p><b>Named, narrow jobs.</b> One giant "AI SDR" that does everything is hard to inspect. Smaller agents with one job each are easier to watch and easier to fix, because when something goes wrong you know where to look. In the Agent Base, Scout finds accounts with a reason to buy, Lens researches each one, Quill drafts the email, Relay sends at a safe pace, Echo reads and sorts replies, and Atlas writes a brief for every booked meeting.</p>'
            + fig3 +
            '<p><b>A live view.</b> You should be able to open a dashboard at any time and see which accounts were found, which emails were drafted and approved, what was sent, what came back and which meetings were booked. Our own dashboard shows the agents as a small base of hex tiles, with each agent at its station and an activity feed underneath. The look is a choice. The live feed is the part that matters.</p>'
            '<p><b>A person in the line.</b> Visibility tells you what happened. Approval decides what happens. In the Agent Base, a dedicated Agent Base manager reads every draft, edits or approves it, and handles the replies that need a human. That one step is what turns a view of the work into control over it.</p>'
            '<p>If a vendor offers only one of these three, you are missing either control or confidence. If it offers none, you are buying a black box and hoping.</p>'
        )),
        ('limits', 'Where a visual office stops being useful', (
            '<p>A visual office stops being useful when it replaces judgment instead of supporting it. Watching a character type tells you an agent is working, not that the work is good.</p>'
            '<p>There are three traps to watch for:</p>'
            '<ul><li><b>Busy is not useful.</b> A room full of characters typing can make a slow, poorly targeted campaign look productive. Always connect the view to outcomes: positive replies, meetings held, and the reasons buyers say no.</li>'
            '<li><b>Animation is not approval.</b> Some tools show you the agent "deciding" without letting anyone stop it. If you cannot pause, edit or reject an action before it reaches a buyer, the view is a window, not a control.</li>'
            '<li><b>Nobody is watching.</b> A dashboard only helps if a named person is responsible for looking at it. McKinsey\'s finding that clear ownership goes with higher maturity applies here too: name the owner before you launch.</li></ul>'
            '<p>The healthiest way to think about it is the way you would think about a new team member. You want to see their work early and often, you want a person to check anything that goes to a customer, and over time you want to spend less effort watching because the results have earned it. The view is a tool for building that trust, not a substitute for it.</p>'
        )),
        ('evaluate', 'How to evaluate a vendor\'s agent dashboard', (
            '<p>Evaluate a vendor\'s dashboard by asking it to show you a live account, not a demo video, and by checking whether you can trace one buyer from first signal to booked meeting. If you can follow that thread, the visibility is real.</p>'
            '<ol><li><b>Can I see each agent\'s current task right now?</b> Ask for a live view, with client details hidden if needed.</li>'
            '<li><b>Can I trace one account end to end?</b> Why it was chosen, what was researched, what was drafted, who approved it, what was sent and what came back.</li>'
            '<li><b>Where does a person approve or edit?</b> Ask to see the approval step and who does it.</li>'
            '<li><b>What does "waiting" look like?</b> How do I know when a draft or a reply is waiting on someone?</li>'
            '<li><b>Can I pause the campaign myself?</b> And what happens to messages already queued?</li>'
            '<li><b>How do activity numbers connect to meetings held?</b> Ask for the full funnel, not only the top.</li>'
            '<li><b>Who on your side owns the account?</b> A named person, not a support inbox.</li></ol>'
            '<p>For a wider checklist that also covers contracts, data and domains, see <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a>.</p>'
        )),
    ],
    'conclusion': (
        '<p>The pixel art office is a small trend with a serious idea behind it: AI agents are easier to trust, correct and improve when you can see them work. For sales teams, where agents act in front of buyers, that idea matters even more.</p>'
        '<ol><li><b>Know what it is:</b> a visual view of each agent and its current activity, popularized by tools like Pixel Agents.</li>'
        '<li><b>Know why it spread:</b> trust in agents is low, and visibility is the cheapest way to raise it.</li>'
        '<li><b>See the states that matter:</b> working, waiting, stuck and handed off.</li>'
        '<li><b>Remember that sales is public:</b> outbound mistakes reach buyers before a report reaches you.</li>'
        '<li><b>Ask for three things:</b> named agent roles, a live view and a person who approves every email.</li>'
        '<li><b>Do not confuse busy with good:</b> connect the view to meetings held.</li>'
        '<li><b>Test it live:</b> trace one account from signal to meeting before you sign.</li></ol>'
        '<p>If you want to see what that looks like for outbound, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will walk you through the Agent Base on a live dashboard.</p>'
    ),
    'faq': [
        ('What is an AI agent office?',
         'It is a visual interface that shows each AI agent as a character in a small virtual workspace and acts out what it is doing, such as typing, reading or waiting for input. It lets you see at a glance which agents are busy, idle or stuck.'),
        ('What is Pixel Agents?',
         'Pixel Agents is an open source project that turns AI coding agents running in a terminal into animated pixel art characters in a tiny office. It runs as a VS Code extension or a command line tool and works with Claude Code, with other agents on its roadmap.'),
        ('Where did the idea of AI agents living in a virtual town come from?',
         'A well known early example is the 2023 Generative Agents paper from Stanford and Google researchers, in which 25 AI agents lived in a game-like town called Smallville, planned their days and talked to each other.'),
        ('Do sales teams need a visual dashboard for their AI agents?',
         'They need visibility, whatever it looks like. Because outbound agents write to real buyers, a team should be able to see what each agent is doing and approve messages before they are sent, rather than waiting for a weekly report.'),
        ('Is a visual agent dashboard enough to keep AI outbound safe?',
         'No. A view shows you what is happening, but a person still needs to approve what goes out and own the results. Look for named agent roles, a live activity feed and a human approval step together.'),
        ('Why do so few companies trust AI agents with core processes?',
         'Surveys point to accuracy, security and governance concerns. In one 2025 HBR Analytic Services survey, only 6% of leaders fully trusted agents with core processes, and only 12% said their risk and governance controls were fully in place.'),
        ('How does the Agent Base show what its agents are doing?',
         'A live dashboard shows each agent at its station, from Scout finding accounts to Atlas writing meeting briefs, with an activity feed of every lead, email, reply and meeting. A dedicated Agent Base manager approves every email before it is sent.'),
    ],
}
