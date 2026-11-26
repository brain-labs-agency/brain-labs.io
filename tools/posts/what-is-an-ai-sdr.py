# Spec for blog/what-is-an-ai-sdr.html. Build: python3 tools/blogkit.py tools/posts/what-is-an-ai-sdr.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


IBM = 'https://www.ibm.com/think/topics/ai-sdr'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
APOLLO = 'https://www.apollo.io/insights/what-are-the-limitations-of-current-ai-sdr-tools'
G_SELLERS = 'https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-predicts-by-2028-ai-agents-will-outnumber-sellers-by-10x-yet-fewer-than-40-percent-of-sellers-will-report-ai-agents-improved-productivity'
G_VALIDATE = 'https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights'
G_AGENTIC = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027'
GOOGLE = 'https://support.google.com/a/answer/81126'

fig1 = figure(1, table(['Part of the SDR job', 'What an AI SDR can do today', 'Where it still needs a person'], [
    ['<b>Finding accounts</b>', 'Filter large databases and watch for signals such as hiring, funding or new locations', 'Deciding which signals actually predict a buyer for your offer'],
    ['<b>Researching each account</b>', 'Read websites, news and profiles in seconds and summarize them', 'Spotting when the research is wrong, stale or about the wrong company'],
    ['<b>Writing the first email</b>', 'Draft a personalized email per contact, in your template and tone', 'Judging whether the message is true, relevant and safe to send under your name'],
    ['<b>Follow ups and sending</b>', 'Keep schedules, pace sends and stop sequences when someone replies', 'Setting volume limits that protect your domains'],
    ['<b>Handling replies</b>', 'Sort replies into interested, not now, wrong person and unsubscribe', 'Answering objections, pricing questions and anything sensitive'],
    ['<b>Qualifying and booking</b>', 'Offer times and prepare a short meeting brief', 'Confirming the meeting is a real opportunity, not just a calendar slot'],
]), 'What an AI SDR handles well and where a human still decides, mapped to the steps of the SDR job. Based in part on the functions described by '
    + a(IBM, 'IBM') + ' and the limitations listed by ' + a(APOLLO, 'Apollo') + '.')

fig2 = figure(2, bar_chart('Median daily activities of a human SDR, by channel', [
    ('Phone', 44),
    ('Email', 41),
    ('LinkedIn', 19),
    ('Text and other', 8),
], vmax=55, highlight=('Email',)),
    'A median of 112 activities a day, for about 4 quality conversations. Most of this volume is what AI SDRs are built to take over. Source: '
    + a(BRIDGE, 'The Bridge Group, 2025 SDR Metrics Report') + ', a survey of 351 B2B companies.')

fig3 = figure(3, steps('How the Agent Base splits the SDR job', [
    ('Scout', 'finds accounts'),
    ('Lens', 'researches'),
    ('Quill', 'drafts'),
    ('Manager', 'approves'),
    ('Relay', 'sends'),
    ('Echo', 'sorts replies'),
    ('Atlas', 'meeting brief'),
], accent=('Manager',)),
    'Six agents do the volume work. The dedicated Agent Base manager sits in the middle and decides what reaches a buyer.')

POST = {
    'slug': 'what-is-an-ai-sdr',
    'title': 'What is an AI SDR, and what it can\'t do yet',
    'h1': 'What is an AI SDR, and what it <em>can\'t</em> do yet',
    'description': 'A plain definition of an AI SDR: what it does, how it works, where it falls short in 2026, and how to set one up so a person still decides what reaches your buyers.',
    'category': 'AI agents',
    'date': '2026-11-26',
    'date_label': 'November 26, 2026',
    'hero_img': 'cover-what-is-an-ai-sdr',
    'card_img': 'cover-what-is-an-ai-sdr',
    'card_title': 'What is an AI SDR, and what it can\'t do yet',
    'card_text': 'Software that prospects, researches, writes and books like an SDR. Here is what it does well, where it breaks, and who should still decide.',
    'takeaways': [
        'An AI SDR is software that does the early stages of sales development: it finds prospects, researches them, writes and sends outreach, sorts replies and books meetings.',
        'It is strong at volume and speed: research, first drafts, follow up schedules and reply sorting. Those are the tasks that fill most of a human SDR\'s day.',
        'It is still weak at judgment: choosing the right signals, catching wrong facts, handling objections and protecting your domain and brand.',
        'The setups that work in 2026 keep a person in the loop who approves what goes out. Ask any vendor who reads the emails before buyers do.',
    ],
    'intro': (
        '<p>"AI SDR" has become one of the most searched terms in B2B sales, and one of the most loosely used. Some vendors mean a writing assistant inside your sequencing tool. Others mean an agent that finds, emails and books buyers with nobody watching. Founders reading the pitches often cannot tell which one they are being sold.</p>'
        '<p>This guide gives a plain definition, explains how an AI SDR works step by step, and is honest about what it cannot do yet. It ends with the questions to ask before you let one write to your buyers, and how we use AI agents with a person in charge at BL Agency.</p>'
    ),
    'cta': {
        'inline_lead': 'Want to see AI agents and a person working on the same pipeline?',
        'inline_text': 'Book a 30 minute call about the Agent Base. We will show you what each agent does, where the dedicated Agent Base manager steps in, and what you would see on your live dashboard.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'AI agents for the volume. A <em>person</em> for the judgment.',
        'band_text': 'Scout, Lens, Quill, Relay, Echo and Atlas do the research, drafting, sending and sorting. Your dedicated Agent Base manager approves every email before it reaches a buyer, and you watch it all on a live dashboard.',
    },
    'sections': [
        ('definition', 'What an AI SDR is', (
            '<p>An AI SDR is software that performs the work of a sales development representative at the top of the funnel: it identifies prospects, reaches out to them, qualifies interest and hands promising leads to a human seller. ' + a(IBM, 'IBM defines it') + ' as "a software system that uses AI to perform the early (top of funnel) stages of the sales process."</p>'
            '<p>To understand the term, start with the human role. An SDR does not close deals. They find companies that fit, contact the right person, start a conversation and book a meeting for an account executive. If you need a refresher on how the role fits a sales team, our guide on <a href="/blog/hire-sdr-or-ae-first">whether to hire an SDR or an AE first</a> covers it.</p>'
            '<p>An AI SDR tries to do the same job with software. In practice the label covers three quite different products:</p>'
            '<ul><li><b>Assistants.</b> AI features inside a tool your reps already use, such as drafting an email or summarizing an account. A person still does the job; the AI makes them faster.</li>'
            '<li><b>Autonomous agents.</b> Systems that choose accounts, write and send emails, and respond to replies on their own. This is what most vendors mean when they say "AI SDR."</li>'
            '<li><b>Managed hybrids.</b> A set of agents that do the volume work, run by a person who approves what goes out and handles the conversations that need judgment.</li></ul>'
            '<p>The difference between these matters more than any feature list. The same research and writing ability can be safe in one setup and risky in another, depending on who reads the email before a buyer does.</p>'
            '<p>The category is also young. The Bridge Group\'s ' + a(BRIDGE, '2025 SDR Metrics Report') + ', which surveyed 351 B2B companies, listed "AI SDRs" as a category for the first time that year, and only about 1% of respondents chose it. Most sales teams are still deciding what role, if any, an AI SDR should play.</p>'
        )),
        ('how-it-works', 'How an AI SDR works, step by step', (
            '<p>An AI SDR works by chaining the steps of outbound together: it builds a list, researches each account, drafts a message, sends it on a schedule, reads the replies and books the meetings. Each step uses a mix of data providers, language models and rules set by whoever configures it.</p>'
            '<p>A typical flow looks like this:</p>'
            '<ul><li><b>Targeting.</b> You describe your ideal customer profile. The system filters a contact database and, in better tools, watches for signals such as a new hire, a funding round or a new office.</li>'
            '<li><b>Research.</b> For each account it reads the website, recent news and public profiles, and summarizes what might be relevant.</li>'
            '<li><b>Writing.</b> A language model drafts a first email and follow ups, using the research and your instructions.</li>'
            '<li><b>Sending.</b> Emails go out from connected mailboxes at a set pace, and sequences stop when someone replies.</li>'
            '<li><b>Reply handling.</b> Replies are sorted into categories such as interested, not now, wrong person or unsubscribe, and some tools draft or send an answer.</li>'
            '<li><b>Booking and handoff.</b> Interested prospects get times to meet, and the human seller receives a summary. ' + a(IBM, 'IBM describes') + ' this as handing high-intent leads to account executives with context.</li></ul>'
            + fig1 +
            '<p>Notice that every step depends on the one before it. A wrong signal leads to the wrong account, which leads to research about the wrong problem and an email that does not land. That chain is why the quality of an AI SDR depends so much on its setup and supervision, not just on the model writing the emails.</p>'
        )),
        ('what-it-does-well', 'What an AI SDR does well', (
            '<p>An AI SDR is good at the high-volume, repeatable parts of sales development: research, first drafts, schedules and sorting. Those tasks take most of a human SDR\'s day and are where software saves the most time.</p>'
            '<p>The numbers show how much repetitive work the human role involves. The ' + a(BRIDGE, 'Bridge Group report') + ' puts the median SDR at 112 activities a day across phone, email, LinkedIn and text, which produce about 4.1 quality conversations. Most of the day goes into work that comes before a real conversation.</p>'
            + fig2 +
            '<p>That is where AI helps:</p>'
            '<ul><li><b>Research at scale.</b> An agent can read an account\'s website, news and hiring pages in seconds, so every email can carry a specific reason to write.</li>'
            '<li><b>Consistent follow up.</b> Software does not forget the third touch or send it a week late.</li>'
            '<li><b>First drafts.</b> Personalized drafts per contact, in your structure and tone, ready for review.</li>'
            '<li><b>Reply sorting.</b> Out of office notes, unsubscribes and referrals to a colleague are handled quickly, so interested replies are not buried.</li>'
            '<li><b>Signal watching.</b> Agents can monitor many accounts at once for events that create a reason to reach out now.</li>'
            '<li><b>Meeting preparation.</b> A short brief on who the person is, why you wrote and what to ask saves the seller time before the call.</li></ul>'
            '<p>None of this is trivial. Teams that move this work to agents free their people to spend time on the conversations that actually create pipeline. The question is not whether AI can do these tasks. It is whether anyone checks the output before it reaches a buyer.</p>'
        )),
        ('what-it-cant-do', 'What an AI SDR can\'t do yet', (
            '<p>An AI SDR still cannot reliably make the judgment calls that decide whether outbound works: which signals matter, whether a fact is true, how to handle a real objection and when to stop. Those gaps are why fully autonomous setups often disappoint.</p>'
            '<p>Even vendors in the space list the limits openly. ' + a(APOLLO, 'Apollo\'s 2026 overview') + ' names data decay, generic personalization, deliverability failures, qualification gaps and weak governance as the main problems with current AI SDR tools. In our experience running outbound, these are the gaps that show up first:</p>'
            '<ul><li><b>Wrong or stale facts.</b> Contact data ages quickly. An agent that writes confidently about a job someone left or a product a company dropped damages trust in one sentence.</li>'
            '<li><b>Personalization that is not relevant.</b> Mentioning a recent post is not the same as connecting it to a problem the buyer has. Models are good at the first and inconsistent at the second.</li>'
            '<li><b>Objections and nuance.</b> A reply such as "we tried something like this last year" needs a person who understands the offer and the buyer, not a template.</li>'
            '<li><b>Qualification.</b> Booking a meeting is easy. Knowing whether it is a real opportunity for your account executive is harder.</li>'
            '<li><b>Domain protection.</b> High volume without care can hurt your sender reputation. Mailbox providers such as ' + a(GOOGLE, 'Google set requirements for bulk senders') + ', and once a domain is damaged, every email suffers, including your team\'s.</li>'
            '<li><b>Brand judgment.</b> An agent does not know which customer is in a delicate renewal or which competitor you never want to email.</li></ul>'
            '<p>Expectations are also running ahead of results. ' + a(G_SELLERS, 'Gartner predicts') + ' that by 2028 AI agents will outnumber sellers by ten to one, yet fewer than 40% of sellers will say agents improved their productivity. Gartner has also predicted that ' + a(G_AGENTIC, 'over 40% of agentic AI projects will be canceled by the end of 2027') + '. We look at what happened to teams that went fully autonomous in <a href="/blog/are-ai-sdrs-worth-it">are AI SDRs worth it</a>.</p>'
        )),
        ('buyers', 'What buyers think when an AI writes to them', (
            '<p>Buyers do not object to AI as such. They object to messages that are wrong, generic or obviously sent at scale, and they still want a person to check what AI tells them. That is the standard any AI SDR has to meet.</p>'
            '<p>Gartner\'s research on B2B buyers points the same way. In a ' + a(G_VALIDATE, 'May 2026 survey release') + ', Gartner reported that 69% of B2B buyers turn to sales reps to validate insights generated by AI. Buyers use AI in their own research, but they rely on people to confirm what matters.</p>'
            '<p>For outbound, that has three practical consequences:</p>'
            '<ul><li><b>Accuracy beats volume.</b> One wrong claim about a buyer\'s company costs more than ten emails gained. A reviewer who catches errors is worth more than higher send limits.</li>'
            '<li><b>The reason to write must be real.</b> A signal that genuinely relates to your offer earns a reply. A compliment about a podcast appearance does not.</li>'
            '<li><b>A person must be reachable.</b> When a buyer replies with a real question, the answer should come from someone who knows the offer, quickly.</li></ul>'
            '<p>This is why the debate has shifted from "AI or human" to "how do AI and people split the work." We compare the two directly in <a href="/blog/ai-sdr-vs-human-sdr">AI SDR vs human SDR</a>. The short version: AI wins on research and speed, people win on judgment and conversations, and buyers notice the difference.</p>'
        )),
        ('human-in-the-loop', 'The setup that works: AI agents with a person in charge', (
            '<p>The AI SDR setup that works best in 2026 is a hybrid: agents do the volume work, and a named person reviews and approves every message before it is sent, then handles the replies that need judgment. You keep the speed of software without giving up control of what reaches your buyers.</p>'
            '<p>That is how we built the Agent Base at BL Agency. Instead of one agent that tries to do everything, each agent has one job, and the dedicated Agent Base manager sits in the middle:</p>'
            + fig3 +
            '<ul><li><b>Scout</b> finds companies in your market that show a reason to buy right now, and the person who decides.</li>'
            '<li><b>Lens</b> researches each account so the first email carries something specific.</li>'
            '<li><b>Quill</b> writes the first email and the follow ups, one prospect at a time.</li>'
            '<li><b>The dedicated Agent Base manager</b> reads every draft and edits or approves it. Nothing reaches a buyer without this step.</li>'
            '<li><b>Relay</b> sends approved emails at a safe pace and keeps the follow up schedule.</li>'
            '<li><b>Echo</b> reads and sorts every reply, and sends interested replies straight to the manager.</li>'
            '<li><b>Atlas</b> writes a short brief for each booked meeting.</li></ul>'
            '<p>Two more pieces make it work. Mailboxes are set up and warmed before campaigns start, and volume stays sensible to protect your domain. And every lead, email, reply and meeting appears on a live dashboard you can open any time, so you are never waiting for a weekly report to know what happened.</p>'
            '<p>Whether you use our setup or build your own, the principle is the same: let the agents do the work that scales, and keep the decisions that carry risk with a person you can name.</p>'
        )),
        ('questions', 'Questions to ask before you buy an AI SDR', (
            '<p>Before you buy, ask questions that reveal who makes the decisions, not just what the tool can do. A demo will always show good emails. What you need to know is what happens with the bad ones.</p>'
            '<ul><li><b>Who reads the emails before they are sent?</b> If the answer is "nobody, it is fully autonomous," decide whether you are comfortable with that under your name.</li>'
            '<li><b>Can I see why each account was chosen?</b> Ask for the signal or reason behind any single prospect.</li>'
            '<li><b>Can I see the exact email each person received?</b> Not a template preview, the real message.</li>'
            '<li><b>How do you protect my domain?</b> Ask about separate sending domains, warm up, daily limits and authentication.</li>'
            '<li><b>What happens with replies that need judgment?</b> Who answers objections, pricing questions and complaints?</li>'
            '<li><b>How do you define a qualified meeting?</b> Agree the definition before launch, in writing.</li>'
            '<li><b>What does the first month look like?</b> Setup and warm up take time. Be wary of anyone promising meetings in week one.</li>'
            '<li><b>Can I pause everything right now?</b> You should be able to stop sending without a support ticket.</li></ul>'
            '<p>Many of these questions apply to any outsourced outbound partner, AI or not. For a longer list, see our <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency before you sign</a>.</p>'
        )),
    ],
    'conclusion': (
        '<p>An AI SDR is a useful tool with a misleading name. It can do much of the volume work of sales development faster than a person, but it cannot yet carry the judgment that makes outbound work. The teams getting results treat it as a set of capable assistants, not as a replacement for the people who decide.</p>'
        '<ol><li><b>Know the definition.</b> Software that prospects, researches, writes, sends, sorts and books at the top of the funnel.</li>'
        '<li><b>Know the three kinds.</b> Assistants, autonomous agents and managed hybrids carry very different risks.</li>'
        '<li><b>Use it for volume.</b> Research, drafts, schedules and reply sorting are where it shines.</li>'
        '<li><b>Keep judgment human.</b> Signals, facts, objections, qualification and domain safety need a person.</li>'
        '<li><b>Meet the buyer\'s standard.</b> Accurate, relevant and with a real person reachable.</li>'
        '<li><b>Ask who approves.</b> The answer tells you more than any demo.</li></ol>'
        '<p>If you want the speed of AI agents with a person signing off on every email, that is exactly what the Agent Base is built to do.</p>'
    ),
    'faq': [
        ('What does AI SDR stand for?',
         'AI SDR stands for artificial intelligence sales development representative. It is software that does the early stages of sales development: finding prospects, reaching out, qualifying interest and booking meetings for a human seller.'),
        ('What is the difference between an AI SDR and a sales engagement tool?',
         'A sales engagement tool sends sequences that a person builds and manages. An AI SDR also chooses accounts, researches them, writes the messages and handles replies, with more or less human oversight depending on the setup.'),
        ('Can an AI SDR replace a human SDR?',
         'Not fully, as of 2026. It can take over much of the volume work, but judgment on signals, facts, objections and qualification still needs a person. Most teams that get results use a hybrid model.'),
        ('Do AI SDRs hurt email deliverability?',
         'They can, if they send high volume from your main domain without authentication, warm up or sensible limits. Mailbox providers such as Google set requirements for bulk senders, and a damaged domain affects all your email.'),
        ('Do buyers mind getting emails written by AI?',
         'Buyers mostly mind emails that are wrong, generic or obviously mass produced. Gartner reports that 69% of B2B buyers turn to sales reps to validate AI-generated insights, so having a person behind the message matters.'),
        ('What is a human in the loop AI SDR?',
         'It is a setup where AI agents research and draft, but a person reviews and approves each message before it is sent and handles replies that need judgment. In the Agent Base, that person is the dedicated Agent Base manager.'),
        ('How long does it take to launch an AI SDR?',
         'Plan for a few weeks before the first campaigns. Domains and mailboxes need to be set up and warmed, and the targeting and messaging need testing. At BL Agency, setup and warm up alone take about three weeks.'),
    ],
}
