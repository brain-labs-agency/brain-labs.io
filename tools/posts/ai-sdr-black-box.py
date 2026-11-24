# Spec for blog/ai-sdr-black-box.html. Build: python3 tools/blogkit.py tools/posts/ai-sdr-black-box.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GARTNER_REPFREE = 'https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience'
GARTNER_VALIDATE = 'https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights'
SF = 'https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/'
GMAIL = 'https://support.google.com/mail/answer/14229414?hl=en'

fig1 = figure(1, table(['Question you should be able to answer', 'Black box AI SDR', 'Glass box AI SDR'], [
    ['<b>Why was this account chosen?</b>', 'A list appeared. The filters are hidden', 'Each account shows the signal that put it on the list, with a source'],
    ['<b>What did the agent learn about it?</b>', 'Nothing visible before the email goes out', 'A short research note you can read and correct'],
    ['<b>What exactly was sent?</b>', 'A template preview, not the real message', 'The final text of every email, per contact'],
    ['<b>Who approved it?</b>', 'Nobody. The agent sends on its own', 'A named person, with the time of approval'],
    ['<b>What came back, and what happened next?</b>', 'A reply count in a weekly report', 'Every reply, how it was sorted, and who answered it'],
    ['<b>Can I stop it right now?</b>', 'Open a support ticket', 'A pause control, and a clear view of what is queued'],
]), 'Six questions that separate a black box AI SDR from one you can see into. If a vendor cannot answer one of them from the dashboard, you will not be able to answer it either when something goes wrong.')

fig2 = figure(2, bar_chart('What B2B buyers say about AI in their buying process', [
    ('Prefer rep-free buying', 67),
    ('Used GenAI in a purchase', 45),
    ('Expect misleading GenAI info', 51),
    ('Validate AI insights with a rep', 69),
], unit='%', vmax=85, highlight=('Validate AI insights with a rep',)),
    'Gartner surveys of about 645 B2B buyers, conducted August to September 2025. Sources: '
    + a(GARTNER_REPFREE, 'Gartner, March 2026') + ' and ' + a(GARTNER_VALIDATE, 'Gartner, May 2026') + '.')

fig3 = figure(3, steps('An outbound line you can audit, step by step', [
    ('Signal', 'why this account'),
    ('Research', 'what we know'),
    ('Draft', 'what we will say'),
    ('Approval', 'who signed off'),
    ('Send', 'what went out'),
    ('Reply', 'what came back'),
], accent=('Approval',)),
    'Every step leaves a record you can open. The approval step is the one that turns a log of what happened into control over what happens.')

POST = {
    'slug': 'ai-sdr-black-box',
    'title': 'Can you see your AI SDR working? Why outbound agents shouldn\'t be a black box',
    'h1': 'Can you <em>see</em> your AI SDR working? Why outbound agents shouldn\'t be a black box',
    'description': 'What makes an AI SDR a black box, what it costs you in reputation and learning, and the six things you should be able to see before any AI agent writes to your buyers.',
    'category': 'AI agents',
    'date': '2026-11-24',
    'date_label': 'November 24, 2026',
    'hero_img': 'blog-agent-dashboard',
    'card_img': 'blog-agent-dashboard',
    'card_title': 'Can you see your AI SDR working? Why outbound agents shouldn\'t be a black box',
    'card_text': 'If you cannot see why an account was chosen, what was sent and who approved it, you are not running outbound. You are hoping.',
    'takeaways': [
        'A black box AI SDR shows you totals (emails sent, replies, meetings) but not the decisions behind them: which accounts, why, what was said and who approved it.',
        'That matters because outbound happens in public. A bad decision reaches buyers and your sending domains long before a weekly report reaches you.',
        'A glass box setup lets you trace any single buyer from signal to meeting: the reason, the research, the final email, the approver and the reply.',
        'Before you sign with any AI SDR vendor, ask to trace one live account end to end, and ask who on their side approves messages before they are sent.',
    ],
    'intro': (
        '<p>Most companies that try an AI SDR get the same experience in the first month. The dashboard looks busy. Thousands of contacts were "engaged". A few meetings appeared on the calendar. But when someone asks a simple question, such as why the agent wrote to a competitor, or why replies dropped last week, nobody can answer it. The tool knows. You do not.</p>'
        '<p>That is what people mean when they call an AI SDR a black box. This guide explains what is hidden inside it, why that is a bigger problem in sales than in most other places AI is used, and what a transparent setup looks like in practice. It ends with the checks to run before you let any agent write to your buyers.</p>'
    ),
    'cta': {
        'inline_lead': 'Want to see every step your outbound agents take?',
        'inline_text': 'Book a 30 minute call. We will open the Agent Base dashboard and trace one account from the signal that found it to the meeting it booked, including the dedicated Agent Base manager who approved the email.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound agents you can <em>see</em>, with a person who signs off.',
        'band_text': 'Scout, Lens, Quill, Relay, Echo and Atlas do the volume work of outbound. Your dedicated Agent Base manager approves every email before it reaches a buyer, and every lead, email, reply and meeting shows up on a live dashboard.',
    },
    'sections': [
        ('what-black-box-means', 'What "black box" means for an AI SDR', (
            '<p>An AI SDR is a black box when you can see what went in (your ideal customer profile, maybe some example emails) and what came out (activity totals and a few meetings), but not the decisions in between. You cannot see why it picked an account, what it read, what it actually wrote or how it handled a reply.</p>'
            '<p>An outbound campaign is a long chain of small decisions. For every single contact, someone or something decides:</p>'
            '<ul><li><b>Who.</b> Which company is a fit, and which person at that company should hear from you.</li>'
            '<li><b>Why now.</b> What reason exists to write today, such as a new hire, a funding round, an expansion or a product launch.</li>'
            '<li><b>What to say.</b> The angle, the claim, the tone and the ask.</li>'
            '<li><b>When and how often.</b> The sending pace, the follow ups and when to stop.</li>'
            '<li><b>How to respond.</b> What to do with "interested", "not now", "wrong person" and "remove me".</li></ul>'
            '<p>A human SDR makes those decisions too, but a manager can listen to calls, read emails and ask "why this one?". With a fully autonomous AI SDR, those same decisions are made thousands of times a week, inside a system that usually reports only the outcome. The more autonomous the tool, the more decisions are hidden, and the more you depend on the vendor\'s word that they were good ones.</p>'
            '<p>Black box does not mean bad. Some autonomous tools do decent work. It means unknowable: when results are good you cannot repeat them on purpose, and when results are bad you cannot find out why.</p>'
        )),
        ('why-sales-is-different', 'Why a black box is riskier in outbound than elsewhere', (
            '<p>It is riskier because outbound happens in public. Most AI mistakes inside a company stay inside the company until someone reviews them, while an outbound agent\'s mistake lands in a buyer\'s inbox, under your name, the moment it is made.</p>'
            '<p>Three kinds of damage build up quietly when nobody can see the decisions:</p>'
            '<ul><li><b>Reputation with buyers.</b> A wrong fact about their company, an email to the wrong person or a pushy reply to a polite "not now" is remembered. You rarely get a second first impression with a target account.</li>'
            '<li><b>Reputation with inbox providers.</b> ' + a(GMAIL, 'Gmail\'s sender guidelines') + ' ask senders to keep their spam rate below 0.1% and to never reach 0.3%, and Google says it began ramping up enforcement on non-compliant traffic in November 2025. An agent sending poorly targeted email at volume can push your domains past those lines before anyone looks.</li>'
            '<li><b>Lost learning.</b> Outbound is how many companies learn what their market cares about. If the replies, objections and patterns live inside a tool you cannot inspect, that knowledge never reaches your sales team or your product team.</li></ul>'
            '<p>We looked at how these problems led many teams to cancel fully autonomous tools in <a href="/blog/are-ai-sdrs-worth-it">are AI SDRs worth it</a>. The common thread in those stories is not that the AI was weak. It is that nobody could see the problem until the damage was done.</p>'
        )),
        ('what-buyers-think', 'Buyers use AI too, and they still want a human to check it', (
            '<p>Buyers are not against AI. They use it heavily, but they also say they trust it less than a person when the stakes are real, which is a strong hint about how they will read an email that looks machine-made.</p>'
            '<p>In a ' + a(GARTNER_REPFREE, 'Gartner survey of 646 B2B buyers') + ' published in March 2026, 67% said they prefer a rep-free buying experience and 45% had used AI during a recent purchase. A second ' + a(GARTNER_VALIDATE, 'Gartner release in May 2026') + ' added the other half of the picture: 69% of buyers prefer to validate AI-generated insights with a sales rep, and 51% said they are more likely to encounter misleading information from generative AI.</p>'
            + fig2 +
            '<p>Read together, those numbers describe a buyer who is busy, skeptical and good at spotting generic content. They do not want more contact. They want contact that is accurate, relevant and clearly checked by someone who knows the subject. A black box agent, sending at volume with no person reading the output, is close to the opposite of that.</p>'
            '<p>Sellers feel the same tension. The ' + a(SF, 'Salesforce State of Sales 2026 report') + ', based on a survey of 4,050 sales professionals, found that 54% of sellers had already used AI agents and that sellers expect agents to cut prospect research time by 34% and email drafting time by 36%. In the same announcement, a Salesforce sales leader put the limit plainly: stand-alone agents without full customer context tend to fail. Context, in outbound, is exactly what a reviewer brings.</p>'
        )),
        ('what-to-see', 'The six things you should be able to see', (
            '<p>You should be able to see six things for any contact your AI SDR touches: why the account was chosen, what the agent learned, the exact message, who approved it, what came back and whether you can stop it. If all six are visible, the system is a glass box. If any are missing, that is where your blind spot is.</p>'
            + fig1 +
            '<p>A few notes on what "visible" should mean in practice:</p>'
            '<ul><li><b>The reason, with a source.</b> "Hiring for three SDR roles" is useful only if you can click through to the job posts. Signals without sources are how agents end up congratulating a company on news that is a year old.</li>'
            '<li><b>The real email, not the template.</b> Personalization is where AI goes wrong most often, so the preview of a template tells you very little. You need the final text that went to each person.</li>'
            '<li><b>A named approver.</b> "Approved by system" is not approval. You want to know which person read the message and when.</li>'
            '<li><b>Replies in full.</b> The reply rate is a number. The replies themselves are your market talking. Read them, or make sure someone on your side does.</li></ul>'
            '<p>None of this needs to be fancy. A plain activity feed with one line per action, and a way to click into any account, covers most of it. The point is that the trail exists and that you can open it without asking the vendor to pull a report.</p>'
        )),
        ('how-agent-base-works', 'What a glass box looks like in practice', (
            '<p>In practice, a glass box splits the work into named steps that each leave a record, and puts a person at the point where a message is about to leave. That way you can follow any buyer from the first signal to the booked meeting and see who decided what along the way.</p>'
            '<p>This is how we built the Agent Base. Instead of one large "AI SDR", six agents each do one job:</p>'
            '<ul><li><b>Scout</b> finds accounts that match your profile and have a current reason to talk, and records the signal with its source.</li>'
            '<li><b>Lens</b> researches each account and the right contact, and writes a short note anyone can read.</li>'
            '<li><b>Quill</b> drafts the email from that note.</li>'
            '<li><b>Relay</b> sends approved emails at a pace that protects your domains.</li>'
            '<li><b>Echo</b> reads and sorts the replies.</li>'
            '<li><b>Atlas</b> writes a brief for every meeting that gets booked.</li></ul>'
            + fig3 +
            '<p>Between Quill and Relay sits the dedicated Agent Base manager, a person who reads every draft, edits or approves it, and handles the replies that need a human answer. Nothing reaches a buyer without that step. All of it, from the signal to the meeting brief, shows up on a live dashboard you can open at any time.</p>'
            '<p>The split matters as much as the dashboard. When something goes wrong in a single all-in-one agent, you do not know where to look. When the work is split into named steps, a bad email is either a research problem, a drafting problem or an approval problem, and each one has an obvious fix.</p>'
        )),
        ('black-box-signs', 'Signs your current AI SDR is a black box', (
            '<p>The clearest sign is that you learn about problems from buyers or from your inbox provider instead of from your own dashboard. If the first you hear of a bad email is an angry reply, a screenshot on LinkedIn or a deliverability warning, the tool is hiding its decisions from you.</p>'
            '<p>Other signs to watch for:</p>'
            '<ul><li><b>Your reports only show totals.</b> Emails sent, open rate, replies and meetings, with no way to click into a single account.</li>'
            '<li><b>You cannot read the real emails.</b> You can see the sequence template, but not the personalized message each buyer received.</li>'
            '<li><b>Nobody on your side reads replies.</b> The tool marks them "positive" or "negative" and books what it can. The rest disappears.</li>'
            '<li><b>The vendor explains drops with words, not records.</b> "The market is slow right now" instead of "these three signals stopped producing replies, here are the accounts".</li>'
            '<li><b>Pausing is a support request.</b> You cannot stop a campaign yourself, or you cannot see what is still queued.</li>'
            '<li><b>The meetings do not hold up.</b> Booked meetings that no-show or turn out to be poor fits are a sign that qualification decisions are happening where nobody can review them.</li></ul>'
            '<p>If three or more of these sound familiar, the fix is rarely a better prompt. It is more visibility and a person in the line before messages go out.</p>'
        )),
        ('questions-to-ask', 'Questions to ask before you sign with an AI SDR vendor', (
            '<p>Ask the vendor to show you, on a live account, how to trace one buyer from the first signal to the meeting, and ask who approves messages before they are sent. Those two requests reveal more than any demo deck.</p>'
            '<ol><li><b>Can you open one live account and walk me through every step?</b> Client names can be hidden. The trail should not be.</li>'
            '<li><b>Where does the signal for each account come from?</b> Ask to click through to the source.</li>'
            '<li><b>Can I read the exact email each contact received?</b> Not the template, the final message.</li>'
            '<li><b>Who approves emails before they are sent, and how?</b> A named role, not "the system checks it".</li>'
            '<li><b>What happens to replies?</b> Who reads them, who answers the ones that need a person, and how fast.</li>'
            '<li><b>How do you protect my sending domains?</b> Ask about sending pace, authentication and what happens when complaints rise.</li>'
            '<li><b>Can I pause everything myself, today?</b> And can I see what is queued when I do?</li></ol>'
            '<p>For a wider list that also covers contracts, data ownership and reporting, see <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a>. For a side by side view of where automation helps and where people still matter, see <a href="/blog/ai-sdr-vs-human-sdr">AI SDR vs human SDR</a>.</p>'
        )),
    ],
    'conclusion': (
        '<p>AI agents are very good at the volume work of outbound: finding accounts, researching them and drafting first versions. What they should not be is invisible. Outbound happens in front of your buyers, so every decision an agent makes is a decision made in public under your name.</p>'
        '<ol><li><b>Know what is hidden:</b> a black box shows totals, not the decisions behind them.</li>'
        '<li><b>Know why it matters more in sales:</b> mistakes reach buyers and inbox providers before a report reaches you.</li>'
        '<li><b>Remember the buyer:</b> buyers use AI too, and most still want a person to validate what AI tells them.</li>'
        '<li><b>Ask for six things:</b> the reason, the research, the real email, the approver, the reply and a pause control.</li>'
        '<li><b>Split the work:</b> named agents with one job each are easier to see and easier to fix.</li>'
        '<li><b>Put a person in the line:</b> approval before sending is what turns visibility into control.</li>'
        '<li><b>Test it live:</b> trace one account end to end before you sign.</li></ol>'
        '<p>If you want to see that trail on real outbound, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will walk you through the Agent Base dashboard.</p>'
    ),
    'faq': [
        ('What does it mean that an AI SDR is a black box?',
         'It means you can see the inputs and the totals, but not the decisions in between: why an account was chosen, what the agent learned about it, what it actually wrote, who approved it and how it handled the reply.'),
        ('Why is a black box AI SDR risky?',
         'Because outbound happens in public. A wrong fact, a message to the wrong person or a pushy reply reaches the buyer under your name, and poorly targeted volume can raise spam complaints and hurt your sending domains before anyone notices.'),
        ('How can I tell if my AI SDR is a black box?',
         'If you only get totals, cannot read the exact email each contact received, cannot see who approved it, and learn about problems from buyers or deliverability warnings instead of from your dashboard, the tool is a black box.'),
        ('What should an AI SDR dashboard show?',
         'For any contact: the signal that put the account on the list with its source, the research note, the final email, the person who approved it, the reply and what happened next, plus a way to pause sending yourself.'),
        ('Do B2B buyers trust AI-generated sales content?',
         'Many use AI themselves, but trust is limited. In Gartner research published in 2026, 69% of B2B buyers said they prefer to validate AI-generated insights with a sales rep, and 51% said they are more likely to encounter misleading information from generative AI.'),
        ('Is a human approval step really necessary for AI outbound?',
         'For most B2B teams, yes. A person who reads every message before it is sent catches wrong facts, poor fits and tone problems that the agent cannot see, and is accountable for what goes out under your name.'),
        ('How does the Agent Base keep outbound visible?',
         'Six agents each do one job, from Scout finding accounts to Atlas writing meeting briefs. A dedicated Agent Base manager approves every email before it is sent, and every lead, email, reply and meeting appears on a live dashboard.'),
    ],
}
