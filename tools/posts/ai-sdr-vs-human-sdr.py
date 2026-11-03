# Spec for blog/ai-sdr-vs-human-sdr.html. Build: python3 tools/blogkit.py tools/posts/ai-sdr-vs-human-sdr.py
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


G_REPFREE = 'https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience'
G_VALIDATE = 'https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights'
G_AGENTIC = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027'
GOOGLE = 'https://support.google.com/a/answer/81126'
TC_11X = 'https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have'
BRIDGE = 'https://bridgegroupinc.com/research/sdr-tenure-and-ramp-time'

fig1 = figure(1, bar_chart('What B2B buyers told Gartner about reps and AI (share of buyers)', [
    ('Prefer fully digital buying', 70),
    ('Validate AI insights with a rep', 69),
    ('Prefer buying without a rep', 67),
    ('Expect misleading info from GenAI', 51),
    ('Expect misleading info from a rep', 49),
    ('Used GenAI in a recent purchase', 45),
], unit='%', vmax=100, highlight=('Validate AI insights with a rep',)),
    f'Buyers want less of the rep, yet still check AI answers with one. Survey of 645 B2B buyers, fielded August to September 2025. Source: {a(G_VALIDATE, "Gartner, May 2026")}.')

fig2 = figure(2, table(['Task', 'Who should own it', 'Why'], [
    ['<b>Building the account list</b>', 'AI agent', 'Scanning thousands of companies for a trigger is pattern work, and agents do it fast and without fatigue.'],
    ['<b>Researching each account</b>', 'AI agent, checked by a person', 'Agents pull the facts. A person catches the stale title or the wrong company with the same name.'],
    ['<b>Writing the first email</b>', 'AI drafts, a person approves', 'Drafting is fast with AI. Deciding whether the angle is right for this buyer is judgment.'],
    ['<b>Sending and pacing</b>', 'AI agent, inside human-set limits', 'Software keeps the schedule. A person sets the volume that protects the domain.'],
    ['<b>Sorting replies</b>', 'AI agent', 'Out of office, wrong person and unsubscribe are easy to classify.'],
    ['<b>Answering an interested buyer</b>', 'Person', 'This is the moment a meeting is won or lost. Tone, timing and context matter most here.'],
    ['<b>Live calls and objections</b>', 'Person', 'Buyers test whether someone understands their business. That test is still human.'],
    ['<b>Meeting brief for the closer</b>', 'AI drafts, a person reviews', 'A short, accurate brief saves the closer time on every call.'],
]), 'A task-by-task split. The pattern: AI owns volume and pattern work, a person owns judgment and anything a buyer reads or hears.')

fig3 = figure(3, steps('How an Agent Base splits the work between AI agents and one person', [
    ('Scout', 'finds accounts'),
    ('Lens', 'researches'),
    ('Quill', 'drafts'),
    ('Manager', 'approves'),
    ('Relay', 'sends'),
    ('Echo', 'sorts replies'),
    ('Atlas', 'briefs closer'),
], accent=('Manager',)),
    'Six agents handle research, drafting, sending, reply sorting and meeting briefs. The dedicated Agent Base manager (amber) reads and approves every email before it reaches a buyer.')

POST = {
    'slug': 'ai-sdr-vs-human-sdr',
    'title': 'AI SDR vs human SDR: which one books meetings that close?',
    'h1': 'AI SDR vs human SDR: which one books meetings that <em>close</em>?',
    'description': 'AI SDRs win on volume and speed, human SDRs win on judgment and trust. What each does well, why fully autonomous AI SDRs stalled, and how a hybrid model books meetings that close.',
    'category': 'Outbound',
    'date': '2026-11-03',
    'date_label': 'November 3, 2026',
    'hero_img': 'blog-ai',
    'card_img': 'blog-ai',
    'card_title': 'AI SDR vs human SDR: which one books meetings that close?',
    'card_text': 'What AI agents do well, where a person still decides, and why the hybrid model is winning.',
    'takeaways': [
        'Neither wins alone. AI SDRs are faster to scale and never skip the research; human SDRs are better at the moments that decide whether a meeting turns into a deal.',
        'Fully autonomous AI SDRs stalled on three things: bad data, damaged sending domains and emails that said things that were not true.',
        'Buyers still check with people. In a 2026 Gartner survey, 69% of B2B buyers said they validate AI-generated insights with a sales rep.',
        'The model that works splits the job by task: agents research, draft, send and sort, and one accountable person approves everything a buyer reads.',
    ],
    'intro': (
        '<p>If you run sales at a B2B company, you have probably been pitched an AI SDR this year. The promise is simple: software that finds prospects, writes emails and books meetings around the clock, without hiring, ramping or managing a rep. The question underneath it is just as simple. Does it book meetings that actually close?</p>'
        '<p>The honest answer is that the question is framed wrong. "AI or human" made sense when AI SDRs were sold as full replacements. In 2026, the teams getting results split the work task by task. This guide covers what AI does better than people, what people still do better, why the fully autonomous version stalled, and how to set up a model that uses both.</p>'
    ),
    'cta': {
        'inline_lead': 'Weighing an AI SDR?',
        'inline_text': 'Book a 30 minute call and we will walk you through how the Agent Base splits the work between AI agents and a dedicated Agent Base manager.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'AI agents do the work. A person <em>signs off</em>.',
        'band_text': 'Six AI agents research, draft, send and sort. Your dedicated Agent Base manager approves every email before it reaches a buyer, and you watch it all on a live dashboard.',
    },
    'sections': [
        ('short-answer', 'The short answer: compare tasks, not job titles', (
            '<p>An AI SDR books more first touches; a human SDR books more meetings that hold up. The better question is which tasks inside the SDR job each one should own, because the job is really six or seven jobs bundled together.</p>'
            '<p>Look at what an SDR does in a week. They build a list, research accounts, write messages, send and follow up, read replies, answer the interested ones, get on calls and hand a meeting to a closer. Some of those tasks are pattern work: the same steps, repeated hundreds of times, where speed and consistency win. Others are judgment work: deciding whether an angle fits this buyer, reading a hesitant reply correctly, handling an objection on a live call.</p>'
            '<p><b>AI is very good at pattern work.</b> An agent can scan thousands of companies for a hiring signal, summarize a 10-K or draft a follow up in seconds, and it does the hundredth one as carefully as the first.</p>'
            '<p><b>People are still better at judgment work.</b> A good rep notices that a prospect just changed roles, that the company is in a quiet period, or that the polite reply actually means no. Those calls decide whether a meeting is worth your closer\'s hour.</p>'
        )),
        ('ai-strengths', 'What AI SDRs do better than people', (
            '<p>AI SDRs win on volume, speed and consistency in the research and drafting stages. They do not get tired, they do not skip the research step on a Friday afternoon, and they can work every account in a list instead of the twenty a rep has time for.</p>'
            '<p><b>Research at scale.</b> The single biggest improvement AI brings to outbound is research. A human SDR doing proper account research might manage a handful of accounts an hour. An agent can read a company\'s site, recent news, job posts and the prospect\'s public profile in seconds, and pull out the one detail that makes an email relevant.</p>'
            '<p><b>Speed to follow up.</b> Agents never forget the third touch. Follow ups go out on schedule, and replies are read and sorted the moment they arrive, which matters when an interested buyer is comparing two vendors that week.</p>'
            '<p><b>Consistency.</b> A rep\'s best email and worst email can be very far apart depending on the day. An agent working from a good brief produces drafts within a narrow range. That makes quality easier to manage, because you fix the brief once instead of coaching every rep on every message.</p>'
            '<p><b>Ramp.</b> A new human SDR takes time to become productive. The Bridge Group\'s 2025 research puts average SDR ramp at ' + a(BRIDGE, 'about three months') + '. An agent can be set up on your offer and ideal customer in days, although it still needs a person to define who that customer is.</p>'
            '<p>Notice that every strength above sits before or after the moment a buyer reads something you sent.</p>'
        )),
        ('human-strengths', 'Where a human SDR still wins', (
            '<p>Human SDRs win wherever a buyer is deciding whether to trust you. That includes the email they read, the reply they get and the call they take, and it is exactly where meetings turn into pipeline or quietly die.</p>'
            '<p>The buyer data is clear on this. A ' + a(G_REPFREE, 'March 2026 Gartner survey') + ' found that 67% of B2B buyers would rather buy without talking to a rep. That sounds like a case for full automation, until you read the follow up. In ' + a(G_VALIDATE, 'Gartner\'s May 2026 release') + ' from the same survey, 69% of buyers said they turn to sales reps to validate AI-generated insights, and 51% said they are more likely to run into misleading information from generative AI.</p>'
            + fig1 +
            '<p>Put those numbers together and the picture is a buyer who wants fewer, better conversations. They do not want to be chased by a rep, and they do not fully trust what AI tells them either. When they do engage, they want a person who knows what they are talking about.</p>'
            '<p><b>Judgment on the message.</b> A person reading a draft can tell when a true fact is the wrong thing to lead with: a layoff, a bad quarter, a founder who just left.</p>'
            '<p><b>Reading the reply.</b> "Not right now, maybe next quarter" can be a brush off or a real timing signal. "Send me more info" can mean interest or a polite exit. The answer you send decides which one it becomes.</p>'
            '<p><b>Live conversations.</b> On the phone, buyers test whether the person understands their business. Objection handling, follow up questions and knowing when to stop pushing are still human skills.</p>'
        )),
        ('why-stalled', 'Why fully autonomous AI SDRs stalled', (
            '<p>Fully autonomous AI SDRs stalled because they removed the person at exactly the step where mistakes become public. The three problems that show up most often are bad data, damaged sending domains and emails that claim things that are not true.</p>'
            '<p><b>Bad data in, confident nonsense out.</b> An agent that writes from a stale title, the wrong company or a misread news item will still write a fluent, confident email. Without a reviewer, that email goes out.</p>'
            '<p><b>Sending at a volume the domain cannot carry.</b> The pitch for many AI SDR tools was volume: thousands of emails a day. Mailbox providers push back on that. ' + a(GOOGLE, 'Google\'s sender guidelines') + ' ask bulk senders to keep their reported spam rate below 0.3%. When a program sends more than the market wants to read, complaints rise, inbox placement drops and every later email, including the good ones, lands in spam.</p>'
            '<p><b>Claims nobody checked.</b> The category also had a trust problem at the vendor level. In March 2025, ' + a(TC_11X, 'TechCrunch reported') + ' that 11x, one of the best known AI SDR startups, had listed customers who said they were not customers. Buyers who had been told AI would replace their SDR team started asking harder questions.</p>'
            '<p>This is not unique to sales. In June 2025, ' + a(G_AGENTIC, 'Gartner predicted') + ' that over 40% of agentic AI projects will be canceled by the end of 2027, citing rising costs, unclear business value and weak risk controls. Outbound is one of the clearest examples, because the risk is visible: every mistake lands in a stranger\'s inbox with your name on it.</p>'
            '<p>The lesson is not that AI SDRs do not work. It is that the autonomous version put the agent in charge of deciding what is safe to send.</p>'
        )),
        ('split', 'How to split the work: a task-by-task view', (
            '<p>The practical answer is to give AI the volume and pattern work and give a person every decision a buyer will see. Here is how that looks across the full SDR job.</p>'
            + fig2 +
            '<p>Three rules fall out of this table.</p>'
            '<ol><li><b>Nothing reaches a buyer without a person approving it.</b> That one step catches most of the hallucination and bad data problems before they cost you anything.</li>'
            '<li><b>A person sets the volume.</b> The agent should send at the pace that keeps your domain healthy, not at the pace the software allows.</li>'
            '<li><b>Interested replies go to a person fast.</b> Agents can sort and draft, but the reply to a buyer who said yes is the most valuable email in the whole program.</li></ol>'
            '<p>The one thing to avoid is the middle ground where nobody owns quality. An AI tool sending on its own, with a busy founder checking the dashboard once a week, gets you the volume of automation and the accountability of nobody. That is the setup behind most of the horror stories on Reddit.</p>'
        )),
        ('agent-base', 'What a hybrid team looks like in practice', (
            '<p>A hybrid team pairs a set of specialized AI agents with one accountable person who approves their work. At BL Agency we call this an Agent Base, and the person in the middle is the dedicated Agent Base manager.</p>'
            + fig3 +
            '<p>Each agent has one narrow job, which makes its work easier to check.</p>'
            '<ul><li><b>Scout</b> finds companies in your market that show a reason to buy right now, and the person who decides.</li>'
            '<li><b>Lens</b> researches each account so the first email carries something specific to them, not a template.</li>'
            '<li><b>Quill</b> writes the first email and the follow ups in your voice, one prospect at a time.</li>'
            '<li><b>The dedicated Agent Base manager</b> reads every draft, edits it or approves it. Nothing reaches a buyer without this step.</li>'
            '<li><b>Relay</b> sends the approved emails at a safe pace and keeps the follow up schedule.</li>'
            '<li><b>Echo</b> reads every reply, sorts it and drafts the answer. Interested replies go straight to the Agent Base manager.</li>'
            '<li><b>Atlas</b> spots each booked meeting and writes a short brief for the closer: who they are, why we wrote, and what to ask.</li></ul>'
            '<p>The design choice that matters is where the person sits. Not at the end, reviewing a weekly report, but in the middle of the flow, between the draft and the send. That is the step the autonomous tools removed, and it is the step that protects your brand and your domain.</p>'
            '<p>The second design choice is visibility. Every client sees the base working on a live dashboard: which accounts Scout found, what Quill drafted, what the manager approved and which replies came in. An AI SDR you cannot see is hard to trust, and harder to fix when something drifts.</p>'
        )),
        ('decide', 'How to decide what your team needs', (
            '<p>Choose based on how many buyers you can reach, how much judgment each conversation needs and who on your side will own quality. Those three answers usually point clearly to one setup.</p>'
            '<p><b>You have a small, specific market.</b> If your ideal customer list is a few hundred accounts, every email is precious. Volume is not your constraint; relevance is. Use AI for research and drafting, and keep a person approving every message.</p>'
            '<p><b>Your deals depend on live conversations.</b> If buyers need a call before they will take a demo, you need people on the phone. AI can prepare those calls and handle the follow ups, but it should not be the voice on the line.</p>'
            '<p><b>Nobody on your team has time to own outbound.</b> This is the most common situation, and it is where autonomous tools do the most damage. If nobody can review drafts daily, you need that person to come with the service, not to be assumed.</p>'
            '<p><b>Questions to ask any AI SDR vendor:</b></p>'
            '<ol><li>Who reads each email before it is sent, and can I see their edits?</li>'
            '<li>How many emails per mailbox per day will you send, and who decided that number?</li>'
            '<li>What happens to an interested reply in the first hour?</li>'
            '<li>Where does your contact data come from, and how do you catch stale titles?</li>'
            '<li>Can I see the work live, or only a weekly report?</li>'
            '<li>What do you do when a domain\'s spam rate starts to climb?</li></ol>'
            '<p>A vendor who answers most of these with "the AI handles it" is selling the version that stalled.</p>'
        )),
    ],
    'conclusion': (
        '<p>AI SDR vs human SDR is a choice between two halves of the same job. The teams booking meetings that close in 2026 stopped choosing and started splitting the work.</p>'
        '<ol><li><b>Give AI the pattern work:</b> list building, research, drafting, sending on schedule and sorting replies.</li>'
        '<li><b>Give a person the judgment work:</b> approving what goes out, answering interested buyers and taking live calls.</li>'
        '<li><b>Put the person in the middle of the flow,</b> between the draft and the send, not at the end reading a report.</li>'
        '<li><b>Protect the domain:</b> a person decides the volume, inside the limits mailbox providers set.</li>'
        '<li><b>Make the work visible,</b> so you can see what the agents did and what the person changed.</li></ol>'
        '<p>If you would like to see how that looks for your market, ' + a(CAL, 'book a call') + ' and we will walk you through the Agent Base on a live dashboard.</p>'
    ),
    'faq': [
        ('Can an AI SDR replace a human SDR completely?',
         'Not for most B2B teams. AI can take over list building, research, drafting, sending and reply sorting, but the decisions a buyer sees, like what to send and how to answer an interested reply, still need a person. The fully autonomous tools that tried to remove that step ran into bad data, spam problems and emails with false claims.'),
        ('Are AI SDRs worth it in 2026?',
         'They are worth it as part of a hybrid setup. Used to research and draft, with a person approving every email and setting the sending volume, AI agents let a small team cover far more accounts. Used unsupervised, they tend to damage the domain faster than they build pipeline.'),
        ('Do buyers mind getting emails written by AI?',
         'Buyers mind emails that are wrong, generic or pushy, whoever wrote them. A May 2026 Gartner survey found 51% of B2B buyers expect to run into misleading information from generative AI, which is why a human review step matters.'),
        ('Why do AI SDR emails end up in spam?',
         'Usually because of volume and complaints. Google asks bulk senders to keep their reported spam rate below 0.3%, and programs that send thousands of loosely targeted emails a day cross that line quickly. Once the domain\'s reputation drops, even good emails stop reaching the inbox.'),
        ('What is a hybrid AI SDR model?',
         'It is a setup where AI agents handle the volume and pattern work of outbound and a person approves everything a buyer reads or hears. At BL Agency this is the Agent Base: six agents for research, drafting, sending, reply sorting and meeting briefs, and a dedicated Agent Base manager who signs off on every email.'),
        ('Should I hire a human SDR or use an AI SDR first?',
         'Start with who will own quality. If you have someone with time to review drafts and handle replies every day, AI tools can make that person far more productive. If you do not, hire that person first, or use a service where the reviewer comes included, before adding any AI that sends on its own.'),
        ('What does the dedicated Agent Base manager do?',
         'The dedicated Agent Base manager reads every draft the agents write, edits or approves it, and handles the replies that need a person. They are also your single point of contact.'),
    ],
}
