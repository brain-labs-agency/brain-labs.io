# Spec for blog/ai-agents-for-sales-teams.html. Build: python3 tools/blogkit.py tools/posts/ai-agents-for-sales-teams.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GARTNER_AGENTS = 'https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-predicts-by-2028-ai-agents-will-outnumber-sellers-by-10x-yet-fewer-than-40-percent-of-sellers-will-report-ai-agents-improved-productivity'
GARTNER_BUYERS = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
SF_STATS = 'https://www.salesforce.com/blog/15-sales-statistics/'
SF_NEWS = 'https://cxtoday.com/salesforce-state-of-sales-2026-ai-agents-sales-teams'
GOOGLE = 'https://support.google.com/a/answer/14229414'
FTC = 'https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business'

fig1 = figure(1, table(['Tool type', 'What it does', 'Who decides'], [
    ['<b>Automation</b>', 'Runs a fixed rule: if a lead fills a form, send email 1, wait three days, send email 2.', 'Whoever wrote the rule, once, in advance.'],
    ['<b>Copilot</b>', 'Answers when a rep asks: summarize this call, rewrite this paragraph, suggest a subject line.', 'The rep, every time.'],
    ['<b>AI agent</b>', 'Takes a goal and works through the steps: find accounts, research them, draft emails, sort replies.', 'The agent, inside limits a person sets. A person should approve anything a buyer sees.'],
    ['<b>Autonomous AI SDR</b>', 'An agent chain that finds, writes, sends and replies with no review step.', 'Nobody, until something goes wrong.'],
]), 'Four kinds of sales AI, from the most rigid to the most independent. The useful question is not how smart the tool is, but who decides at each step.')

fig2 = figure(2, bar_chart('Salesforce State of Sales 2026, selected findings', [
    ('AI frees time (reps with agents)', 85),
    ('Time on non-selling tasks', 60),
    ('Security concerns halt AI', 51),
    ('Overwhelmed by too many tools', 42),
], unit='%', vmax=100, highlight=('Time on non-selling tasks',)),
    f'Selected findings from Salesforce\'s State of Sales 2026, a survey of more than 4,000 sales professionals. Most of a rep\'s week still goes to work that is not selling (amber), which is where agents help most. Source: {a(SF_STATS, "Salesforce, February 2026")}.')

fig3 = figure(3, steps('Who does what in an agent-assisted outbound program', [
    ('Find', 'agent'),
    ('Research', 'agent'),
    ('Draft', 'agent'),
    ('Approve', 'human'),
    ('Send', 'agent, paced'),
    ('Reply', 'agent sorts, human answers'),
], accent=('Approve',)),
    'A practical split of work. Agents do the volume steps; a person approves every message before it reaches a buyer (amber) and owns any reply that needs judgment.')

POST = {
    'slug': 'ai-agents-for-sales-teams',
    'title': 'AI agents for sales teams: what they do well and where a human still decides',
    'h1': 'AI agents for sales teams: what they do well and where a human still <em>decides</em>',
    'description': 'What AI agents for sales teams actually do well (research, list building, first drafts, reply sorting, admin) and the decisions a person should still own: targeting, approval, judgment replies and the relationship.',
    'category': 'AI in sales',
    'date': '2026-11-16',
    'date_label': 'November 16, 2026',
    'hero_img': 'blog-ai-agents-sales',
    'card_img': 'blog-ai-agents-sales',
    'card_title': 'AI agents for sales teams: what they do well and where a human still decides',
    'card_text': 'Where agents save real time, where they go wrong, and the decisions a person should keep.',
    'takeaways': [
        'AI agents are good at the volume work around selling: account research, list building, first drafts, reply sorting, CRM updates and meeting briefs.',
        'More agents does not mean more productivity. Gartner predicts agents will outnumber sellers ten to one by 2028, yet fewer than 40% of sellers will say agents made them more productive.',
        'A person should still decide who to target, approve every message a buyer will read, and own any reply that needs judgment, because buyers punish irrelevant outreach.',
        'The setups that work split the job: agents do the steps, a named human approves the output, and the team can see every action the agents take.',
    ],
    'intro': (
        '<p>AI agents for sales teams have moved from demo to default in about two years. Salesforce\'s ' + a(SF_NEWS, 'State of Sales 2026') + ' found that most sales organizations already use AI across the sales cycle, and many sales leaders say agents are now part of how they plan to grow. The pitch is simple: hand the repetitive work to software and let people sell.</p>'
        '<p>The results are less simple. Some teams get real time back. Others end up with more tools, more noise and buyers who stop answering. This guide explains what an AI agent for sales actually is, the jobs it does well, the decisions a person should still own, the most common ways agent programs go wrong, and how to set up the split so it holds up. We run an outbound service built on agents and a human reviewer, so we close with how we do it and where that model does not fit.</p>'
    ),
    'cta': {
        'inline_lead': 'Want agents without the black box?',
        'inline_text': 'Book a 30 minute call and see the Agent Base: AI agents research and draft, and a dedicated Agent Base manager approves every email before it goes out.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Agents do the work. A person <em>decides</em>.',
        'band_text': 'Scout finds the accounts, Lens researches them and Quill drafts the email. Your dedicated Agent Base manager approves every message, Relay sends at a safe pace, Echo sorts the replies and Atlas briefs you before each meeting.',
    },
    'sections': [
        ('what-is-an-ai-agent', 'What an AI agent for sales actually is', (
            '<p>An AI agent for sales is software that takes a goal, such as "find companies like our best customers and draft a first email to each", and works through the steps on its own, using data sources and tools along the way. That is different from a copilot, which waits for a rep to ask, and from automation, which runs a fixed rule someone wrote in advance.</p>'
            '<p>Vendors use the word loosely, so it helps to separate four kinds of tools that often share the label:</p>'
            + fig1 +
            '<p>Most of the confusion in the market comes from the last row. A fully autonomous AI SDR promises to find buyers, write to them, send, follow up and handle replies without anyone checking. An agent that hands its output to a person before a buyer sees it is a different product, even if both are called "AI SDRs".</p>'
            '<p>Two features make something a real agent rather than a smarter template:</p>'
            '<ul><li><b>It plans steps.</b> Given a target profile, it decides which sources to search, what to read about each account and what to write, instead of filling blanks in a fixed sequence.</li>'
            '<li><b>It uses tools.</b> It can query a data provider, read a company website or news item, write to your CRM and update a dashboard, not just generate text in a chat window.</li></ul>'
        )),
        ('what-agents-do-well', 'What AI agents do well in a sales team', (
            '<p>AI agents do well on work that is repetitive, research heavy and easy to check: building account lists, researching each account, drafting first versions of emails, sorting replies, logging activity in the CRM and preparing meeting briefs.</p>'
            '<p>The time is real. In the ' + a(SF_STATS, 'State of Sales 2026') + ' data, reps spend about 60% of their time on tasks that are not selling, and 85% of reps who use agents say AI frees them for higher-value work. Here is what an agent can take on:</p>'
            '<ul><li><b>Account and list building.</b> An agent can filter companies by industry, size, region and technology, then look for a reason to reach out now: a new funding round, a leadership hire, a job posting, a product launch.</li>'
            '<li><b>Account research.</b> Before a first email, someone should read the company\'s site, recent news and the contact\'s role. Agents summarize this quickly and consistently.</li>'
            '<li><b>First drafts.</b> With good research and a clear brief, an agent can write a relevant first version of an email in your voice. The keyword is first: a draft is a starting point for a person, not a finished message.</li>'
            '<li><b>Reply sorting.</b> Out-of-office notes, "not the right person", unsubscribes and real interest arrive in the same inbox. An agent can label them, route them and draft an answer for review.</li>'
            '<li><b>CRM and admin.</b> Logging emails and updating stages are the tasks reps skip first. Agents do them every time.</li>'
            '<li><b>Meeting briefs.</b> An agent can summarize who the person is, what they replied and what to ask.</li></ul>'
            + fig2 +
            '<p>What these jobs share: the work is slow to do but fast to review. That is the sweet spot for agents.</p>'
        )),
        ('the-productivity-gap', 'Why more agents does not mean more productivity', (
            '<p>More agents do not automatically make a sales team more productive, and the data says so. Gartner ' + a(GARTNER_AGENTS, 'predicts') + ' that by 2028 AI agents will outnumber human sellers by about ten to one, yet fewer than 40% of sellers will report that agents improved their productivity.</p>'
            '<p>Gartner calls this a value ceiling, and the reasons are familiar to anyone who has rolled out sales tools:</p>'
            '<ul><li><b>Tool overload.</b> Salesforce found 42% of reps feel overwhelmed by too many tools. Adding an agent that needs its own prompts, settings and checks can add to that load instead of removing it.</li>'
            '<li><b>Bad inputs.</b> An agent that reads a stale CRM or a poor data source produces confident, wrong work. In the same Salesforce data, 74% of sales teams using AI say they are prioritizing data hygiene, which tells you where the problems showed up.</li>'
            '<li><b>Unclear ownership.</b> When an agent sends an email and a buyer complains, who is responsible? If nobody owns the agent\'s output, nobody fixes it.</li>'
            '<li><b>Security and silos.</b> About half of sales professionals in the Salesforce survey say data security concerns halt AI projects, and about half of leaders say technology silos delay them.</li></ul>'
            '<p>Gartner\'s advice for sales leaders is practical: pilot with clear objectives, fix data quality and process before scaling, train sellers to work with the tools, and use AI to take routine tasks away so people can spend time with buyers. The productivity comes from redesigning the work, not from adding agents to the old process.</p>'
        )),
        ('where-humans-decide', 'Where a human still decides', (
            '<p>A person should still decide four things: who to target, whether a message is good enough to send, how to answer any reply that needs judgment, and how the relationship moves once a buyer engages. These are the points where a wrong call costs you a buyer\'s trust, and an agent cannot feel that cost.</p>'
            '<p><b>1. Who to target.</b> An agent can find thousands of companies that match a filter. It cannot know that your best customers share a trait no database tracks, that one segment always stalls in procurement, or that a competitor\'s customers are locked into long contracts this year. The target profile is a strategy decision for the people who know your wins and losses.</p>'
            '<p><b>2. Whether a message is good enough to send.</b> This is the most important approval in outbound. A ' + a(GARTNER_BUYERS, 'Gartner survey of 632 B2B buyers') + ' found that 73% actively avoid suppliers who send irrelevant outreach. One agent mistake repeated across a list (a wrong fact about the company, a misread job title, a tone that does not fit) reaches every buyer on it. A person reading each draft catches what the agent cannot see: that the "recent news" is two years old, that the contact left the company, or that the email simply does not sound like you.</p>'
            '<p><b>3. Replies that need judgment.</b> An agent can sort a reply. It should not decide alone how to answer "we tried something like this and it failed", a question about a sensitive topic, or a referral to a colleague. These replies decide meetings.</p>'
            '<p><b>4. The relationship.</b> Discovery, negotiation and the decision to buy remain human conversations. The same Gartner survey found 61% of buyers prefer a rep-free buying experience overall. Read that as a warning against being chased by reps, not as trust in software to run a major purchase. When a buyer does engage, they expect a person who understands their situation.</p>'
            '<p>A useful rule: let agents do anything a person can check in less time than it would take to do. Keep with people anything that is hard to undo once a buyer has seen it.</p>'
        )),
        ('failure-modes', 'The most common ways agent programs go wrong', (
            '<p>Agent programs usually go wrong in one of four ways: invented personalization, the wrong person, too much volume, and no one watching. Each one is preventable with a review step and visibility into what the agents are doing.</p>'
            '<ul><li><b>Invented personalization.</b> Language models fill gaps with plausible text. An agent that cannot find a real reason to contact someone may write one anyway, such as a "congratulations on the expansion" that never happened. Buyers notice, and it is worse than no personalization at all.</li>'
            '<li><b>The wrong person.</b> Data providers go stale. Contacts change jobs, titles get misread, and an email meant for a head of operations lands with an intern. Research agents help, but a person scanning the list before launch catches the obvious misses.</li>'
            '<li><b>Too much volume.</b> Agents make it cheap to send more email, and more email is the fastest way to damage your sender reputation. Google\'s ' + a(GOOGLE, 'sender guidelines') + ' ask bulk senders to keep the user-reported spam rate below 0.1% and never reach 0.3%, along with proper authentication.</li>'
            '<li><b>No one watching.</b> When an agent runs in the background with only a weekly meeting count as output, problems compound for weeks before anyone looks.</li></ul>'
            '<p>There is also a legal point that does not change with automation. The FTC\'s ' + a(FTC, 'CAN-SPAM compliance guide') + ' applies to business-to-business email, requires a working opt out and a valid postal address, and says you cannot contract away responsibility for email sent on your behalf. An agent sending in your name does not move that responsibility anywhere. This is not legal advice; ask your own counsel if in doubt.</p>'
        )),
        ('how-to-set-it-up', 'How to set up the split between agents and people', (
            '<p>Set it up so agents own the steps and a named person owns the output. In practice that means one agent per job, a human approval before anything reaches a buyer, a person on every reply that needs judgment, and a shared view where anyone on the team can see what the agents did today.</p>'
            + fig3 +
            '<p>A setup that works for most small and mid-size teams looks like this:</p>'
            '<ol><li><b>Write the brief first.</b> Define the target profile, the problem you solve, the proof you can share, the words you never use and what counts as a qualified meeting. Agents follow briefs closely, so a vague brief produces vague work.</li>'
            '<li><b>Give each agent one job.</b> One agent finds accounts, one researches, one drafts. Narrow jobs are easier to check and easier to fix than one agent that does everything.</li>'
            '<li><b>Name the approver.</b> One person reads and approves every draft before it is sent. That person can edit, reject or send back for rework, and their decisions improve the next round of drafts.</li>'
            '<li><b>Pace the sending.</b> Keep volume at a level your domains can carry, warm new inboxes, and watch spam complaints and bounces every week.</li>'
            '<li><b>Route replies by type.</b> Let an agent label and draft. Let a person answer anything that is not a simple out-of-office or unsubscribe.</li>'
            '<li><b>Make it visible.</b> Use a dashboard or shared inbox where the team can see accounts, drafts, sends, replies and meetings. If you cannot see the work, you cannot judge it.</li>'
            '<li><b>Review weekly.</b> Look at the replies, not just the counts: which messages got answers, which objections repeat, which segments are quiet. Feed that back into the brief.</li></ol>'
        )),
        ('how-the-agent-base-works', 'How we split the work in the Agent Base', (
            '<p>The Agent Base is our version of this split: six AI agents, each with one job, and a dedicated Agent Base manager who reads and approves every email before it reaches a buyer. You approve the target profile and the meeting definition before launch, and you can watch all of it on a live dashboard.</p>'
            '<ul><li><b>Scout</b> finds accounts that match your profile and show a reason to buy now.</li>'
            '<li><b>Lens</b> researches each account and contact, so the email starts from facts, not guesses.</li>'
            '<li><b>Quill</b> drafts the email in your voice from that research. Your dedicated Agent Base manager edits or approves every draft. Nothing goes out on autopilot.</li>'
            '<li><b>Relay</b> sends approved emails at a safe pace for your domains.</li>'
            '<li><b>Echo</b> sorts replies and drafts answers, which the manager reviews before they are sent.</li>'
            '<li><b>Atlas</b> writes a brief for each booked meeting so you walk in prepared.</li></ul>'
            '<p>We built it this way because the evidence above points the same direction: agents are fast at the steps, and a person is needed at the moments a buyer will judge you. The dashboard exists because outbound should not be a black box. You should be able to open it and see what was researched, what was written, what was approved and what buyers said.</p>'
            '<p>Where it is not the right fit: if your sale depends on live phone conversations from the first touch, or you already have an experienced SDR team with a proven playbook, agents may add less than a strong human hire. In that case our ' + '<a href="/talent">talent team</a>' + ' can help you hire bilingual SDRs from Latin America who work US hours.</p>'
        )),
    ],
    'conclusion': (
        '<p>AI agents can take a large share of the repetitive work off a sales team, but they do not decide what is worth saying to a buyer. The teams that get real value keep that decision with a person.</p>'
        '<ol><li><b>Use agents for volume work</b> that is slow to do and fast to check: lists, research, drafts, reply sorting, CRM updates and meeting briefs.</li>'
        '<li><b>Do not expect more agents to mean more productivity.</b> Fix data and process first, pilot one job at a time and measure the result.</li>'
        '<li><b>Keep four decisions human:</b> who to target, what gets sent, how to answer judgment replies and how the relationship moves.</li>'
        '<li><b>Watch for the four failure modes:</b> invented personalization, the wrong person, too much volume and no one watching.</li>'
        '<li><b>Make the work visible</b> so you can see every account, draft, send and reply.</li></ol>'
        '<p>If you want to see this split working on your market, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will walk you through the Agent Base.</p>'
    ),
    'faq': [
        ('What are AI agents for sales teams?',
         'They are software that take a sales goal, such as building a target list or drafting first emails, and work through the steps on their own using data sources and tools. A person should approve their output before a buyer sees it.'),
        ('What can AI agents do for a sales team?',
         'They do well on repetitive, research-heavy work: building account lists, researching companies and contacts, drafting first emails, sorting replies, logging activity in the CRM and preparing meeting briefs.'),
        ('Can AI agents replace SDRs?',
         'Not fully. Agents can replace much of the research and drafting an SDR does, but someone still needs to decide who to target, approve what gets sent and handle replies that need judgment.'),
        ('Why do AI agents not always make sellers more productive?',
         'Because adding tools to an old process can add work instead of removing it. Gartner predicts fewer than 40% of sellers will say agents improved their productivity by 2028, and points to data quality, process design and seller training as the things to fix first.'),
        ('Should a human review every AI-written sales email?',
         'For outbound to new buyers, yes. One mistake in an agent draft repeats across the whole list, and Gartner found 73% of B2B buyers avoid suppliers who send irrelevant outreach.'),
        ('How do I start using AI agents in sales?',
         'Start with one job that has a clear output, such as account research or first drafts. Write a clear brief, name the person who checks the output, measure time saved and quality, and only then add the next job.'),
        ('How does the Agent Base use AI agents?',
         'Six agents each do one job: Scout finds accounts, Lens researches them, Quill drafts emails, Relay sends at a safe pace, Echo sorts replies and Atlas writes meeting briefs. A dedicated Agent Base manager approves every email before it goes out, and you see the work on a live dashboard.'),
    ],
}
