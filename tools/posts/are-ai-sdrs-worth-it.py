# Spec for blog/are-ai-sdrs-worth-it.html. Build: python3 tools/blogkit.py tools/posts/are-ai-sdrs-worth-it.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


TC_11X = 'https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have'
GARTNER_AGENTIC = 'https://sdtimes.com/agentic-ai/gartner-more-than-40-of-agentic-ai-projects-will-be-canceled-in-next-few-years/'
GARTNER_BUYERS = 'https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
SAASTR_AGENTS = 'https://developmentcorporate.com/startups/what-really-happened-when-saastr-replaced-its-sales-team-with-ai-agents/'
GMAIL = 'https://support.google.com/a/answer/14229414'

fig1 = figure(1, bar_chart('What B2B buyers told Gartner about AI and sales reps', [
    ('Check AI insights with a rep', 69),
    ('Prefer a rep free experience', 67),
    ('Expect misleading info from GenAI', 51),
    ('Used GenAI in a recent purchase', 45),
], unit='%', vmax=85, highlight=('Check AI insights with a rep',)),
    f'Share of 645 B2B buyers surveyed in August and September 2025. Buyers lean on AI to research, then want a person to confirm what it told them. Source: {a(GARTNER_BUYERS, "Gartner, May 2026")}.')

fig2 = figure(2, table(['', 'Fully autonomous AI SDR', 'AI agents with a human approver', 'Human SDR only'], [
    ['<b>Who decides what a buyer reads</b>', 'The model.', 'A person, on every message.', 'The SDR.'],
    ['<b>Research depth per account</b>', 'Wide but shallow, and sometimes invented.', 'Wide, then checked.', 'Deep, but only for a few accounts a day.'],
    ['<b>Volume</b>', 'High, often too high for the domain.', 'Set by what a person can review well.', 'Limited by hours in the day.'],
    ['<b>Risk to your domain and brand</b>', 'High: one bad batch reaches thousands.', 'Low: errors stop at the approval step.', 'Low to medium.'],
    ['<b>What you can see</b>', 'Usually a send count.', 'Every draft, edit and reply.', 'Whatever the SDR logs in the CRM.'],
    ['<b>Where it breaks</b>', 'Niche markets, missing context, hallucinated facts.', 'If the approver rubber stamps drafts.', 'Ramp time, turnover, inconsistent research.'],
]), 'Three ways to run outbound. The middle column keeps the speed of agents and puts a person at the one step buyers judge you on.')

fig3 = figure(3, steps('How the Agent Base splits the work between agents and a person', [
    ('Find', 'Scout'),
    ('Research', 'Lens'),
    ('Draft', 'Quill'),
    ('Approve', 'the manager'),
    ('Send and reply', 'Relay, Echo, Atlas'),
], accent=('Approve',)),
    'Agents do the volume work on both sides of the amber step. Nothing reaches a buyer until the dedicated Agent Base manager has read it.')

POST = {
    'slug': 'are-ai-sdrs-worth-it',
    'title': 'Are AI SDRs worth it? What happened to fully autonomous AI SDRs',
    'h1': 'Are AI SDRs worth it? What happened to <em>fully autonomous</em> AI SDRs',
    'description': 'A clear look at AI SDRs in 2026: why many fully autonomous AI SDR rollouts were dropped, what buyers think of AI written outreach, where AI agents do help and how to judge one before you sign.',
    'category': 'AI and outbound',
    'date': '2026-11-10',
    'date_label': 'November 10, 2026',
    'hero_img': 'cover-are-ai-sdrs-worth-it',
    'card_img': 'cover-are-ai-sdrs-worth-it',
    'card_title': 'Are AI SDRs worth it? What happened to fully autonomous AI SDRs',
    'card_text': 'Why many autonomous AI SDR rollouts were dropped, where agents do help, and how to judge one before you sign.',
    'takeaways': [
        'AI SDRs are worth it when they do the research and drafting and a person decides what reaches the buyer. Fully autonomous ones have a poor track record so far.',
        'The common failure points are a vague ICP, invented facts in emails, too much volume for the domain and nobody reading the output.',
        'Buyers use AI to research but still want a person to confirm what it says. In a 2026 Gartner survey, 69% check AI insights with a sales rep.',
        'Judge any AI SDR on qualified meetings, reply quality and domain health over 90 days, and ask who reads each email before it goes out.',
    ],
    'intro': (
        '<p>Two years ago the pitch was simple: replace your SDR team with an AI that never sleeps, writes thousands of personal emails a day and books meetings while you focus on closing. Many companies signed up. A lot of them left within months, and the threads asking "are AI SDRs worth it" and "AI SDR reddit" are full of founders explaining why.</p>'
        '<p>The answer is not that AI has no place in outbound. It is that the fully autonomous version, where no person reads what goes out, keeps running into the same problems. This guide covers what happened to autonomous AI SDRs, why they break, what buyers think of AI written outreach, where agents do earn their place and how to judge one before you commit.</p>'
    ),
    'cta': {
        'inline_lead': 'Want AI agents with a person in charge?',
        'inline_text': 'Book a 30 minute call and we will walk through the Agent Base: AI agents find, research and draft, and a dedicated Agent Base manager approves every email before it reaches a buyer.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'AI agents do the work. A person <em>signs off</em>.',
        'band_text': 'Scout finds the accounts, Lens researches them and Quill drafts the email. Your dedicated Agent Base manager approves every message, Relay sends at a safe pace, Echo sorts the replies and Atlas briefs you on each meeting. You see all of it on a live dashboard.',
    },
    'sections': [
        ('short-answer', 'The short answer: are AI SDRs worth it?', (
            '<p>AI SDRs are worth it when they take over the slow parts of outbound, like finding accounts, researching them and drafting first emails, and a person still decides what reaches each buyer. Fully autonomous AI SDRs, sold as a replacement for the whole function, have mostly not delivered, and the reasons are well documented.</p>'
            '<p>The question people type is really two questions:</p>'
            '<ul><li><b>Can AI do SDR work?</b> Parts of it, yes, and faster than a person: list building, account research, first drafts, sorting replies and writing meeting briefs.</li>'
            '<li><b>Can AI run outbound with nobody watching?</b> So far, not reliably. The failures show up in the places a buyer notices first: a wrong fact in the first line, a message that misreads the company, or a domain that lands in spam.</li></ul>'
            '<p>Even the strongest public success story comes with a lot of human work. SaaStr replaced most of its sales team with about 20 AI agents, and by ' + a(SAASTR_AGENTS, 'its own account of the experiment') + ' the agents needed daily training and review for more than 30 days, plus a person spending one to two hours a day correcting their behavior. That is not a criticism. It is the cost of doing it well, and most buyers of AI SDR tools did not plan for it.</p>'
                    )),
        ('what-happened', 'What happened to fully autonomous AI SDRs', (
            '<p>Many fully autonomous AI SDR rollouts were dropped within months because the results did not match the demos, and the contracts were often built to hide that. The category grew fast in 2024, then ran into public questions about customer claims, churn and how much supervision the tools really needed.</p>'
            '<p>The best known case is 11x. In March 2025, ' + a(TC_11X, 'TechCrunch reported') + ' that the company had listed customers that were not using its product, including ZoomInfo, which said it had run a one month pilot and decided not to proceed. Former employees described high churn and said customers often signed one year contracts with a break clause around month three, then used it to leave. 11x disputed parts of the reporting and said its current retention was 79%. Whatever the exact numbers, the pattern was clear: many buyers tried an autonomous AI SDR and stopped.</p>'
            '<p>The wider market tells a similar story:</p>'
            '<ul><li><b>Agent projects get cancelled.</b> Gartner predicted in June 2025 that ' + a(GARTNER_AGENTIC, 'more than 40% of agentic AI projects will be cancelled by the end of 2027') + ', citing rising costs, unclear business value and weak risk controls.</li>'
            '<li><b>Many "agents" are not agents.</b> The same Gartner note warned about "agent washing" and estimated that only about 130 of the thousands of vendors claiming agentic AI are the real thing.</li>'
            '<li><b>Adoption is still small.</b> In the ' + a(BRIDGE25, 'Bridge Group 2025 SDR report') + ', based on 351 B2B companies, "AI SDRs" showed up as their own category for the first time, at 1% of respondents.</li></ul>'
                    )),
        ('why-it-breaks', 'Why autonomous outbound breaks', (
            '<p>Autonomous outbound breaks because the model is only as good as the context it gets, and with no person reading the output, small errors get repeated thousands of times. Four failure points come up again and again in reviews and in the threads where buyers explain why they cancelled.</p>'
            '<p><b>1. A vague ICP.</b> An AI SDR given "B2B SaaS companies with 50 to 500 employees" will find thousands of them and write to all of them. Without a clear buyer, a reason to reach out now and a list of who not to contact, more volume just means more irrelevant emails.</p>'
            '<p><b>2. Invented facts.</b> Language models fill gaps with plausible text. In an email that can mean congratulating someone on a funding round that never happened or praising a product the company retired. One wrong fact in the first line ends the conversation, and the buyer remembers the sender.</p>'
            '<p><b>3. Volume the domain cannot carry.</b> Mailbox providers now watch complaint rates closely. Google tells bulk senders to keep the spam rate reported in Postmaster Tools ' + a(GMAIL, 'below 0.3%') + ', and an autonomous tool that sends too much, too fast, can push a domain past that line in days.</p>'
            '<p><b>4. Nobody watching.</b> When the tool runs on its own, problems surface late: as a drop in replies, a complaint from a prospect or a note from your own sales team.</p>'
            '<p>There is also a market size problem. Tools that send at volume work best when the total market is large enough to absorb mistakes. If you sell to a few thousand companies in one niche, every wasted first impression is expensive, and you cannot simply buy a new list next quarter.</p>'
                    )),
        ('buyers', 'What buyers actually do with AI written outreach', (
            '<p>Buyers now use AI to research vendors, but they still want a person to confirm what it tells them, and they are quick to ignore outreach that reads like it came from a machine. That combination is the strongest argument for keeping a human in the loop.</p>'
            '<p>' + a(GARTNER_BUYERS, 'Gartner\'s survey of 645 B2B buyers') + ', published in May 2026, shows both sides at once:</p>'
            + fig1 +
            '<p>Three things stand out for outbound:</p>'
            '<ul><li><b>Buyers research on their own first.</b> Most prefer a rep free experience, and 45% used GenAI in a recent purchase.</li>'
            '<li><b>Trust is split.</b> About half of buyers expect misleading information from GenAI, and about half expect it from sales reps. An AI written email with a wrong fact confirms both fears at once.</li>'
            '<li><b>People still matter at the key moments.</b> Gartner found reps remain the most important source when buyers define the problem, choose a preferred supplier and finalize the purchase.</li></ul>'
            '<p>For an outbound program, that means the first email has one job: earn a reply from a person who already does a lot of research alone. A message with a real, checked reason to write, signed by someone who will be there for the conversation, does that job far better than a high volume sequence.</p>'
        )),
        ('where-ai-helps', 'Where AI agents do earn their place', (
            '<p>AI agents earn their place on the tasks that are slow, repetitive and easy to check: finding accounts, researching them, drafting, sorting replies and preparing meeting briefs. These are the hours a human SDR spends before and after the part that matters, and agents can do them faster and more consistently.</p>'
                        '<ul><li><b>Finding accounts.</b> An agent can scan job posts, leadership changes, funding news and tech changes across a whole market every day and flag the companies with a reason to buy now.</li>'
            '<li><b>Account research.</b> An agent can read a company\'s site, recent news and the buyer\'s public profile and pull out the one detail worth mentioning. The person checks that the detail is true and relevant.</li>'
            '<li><b>First drafts.</b> An agent can write a first email and follow ups in your voice, one prospect at a time. Editing a good draft is much faster than writing from scratch.</li>'
            '<li><b>Reply handling.</b> An agent can sort replies into interested, not now, wrong person and unsubscribe, and draft an answer. Interested replies go straight to a person.</li>'
            '<li><b>Meeting briefs.</b> When a meeting is booked, an agent can write a short note: who they are, why you wrote and what to ask.</li></ul>'
                        '<p>The tasks that should stay with a person are the ones where a mistake is expensive and hard to undo: deciding who is worth contacting, approving what a buyer reads, answering an interested reply and running the meeting. Keep those four with people and you get most of the benefit of AI with very little of the risk.</p>'
        )),
        ('hybrid', 'The hybrid model: agents do the work, a person approves', (
            '<p>The model that works in 2026 is a hybrid: AI agents handle the volume work and a named person approves every message before it reaches a buyer. It keeps the speed of automation and puts human judgment at the one step buyers use to decide whether to reply.</p>'
                        + fig2 +
            '<p>This is how we built the Agent Base at BL Agency. Each agent has one job, and one person is accountable for what goes out:</p>'
            + fig3 +
            '<ul><li><b>Scout</b> finds companies in your market that show a reason to buy now, and the person who decides.</li>'
            '<li><b>Lens</b> researches each account so the first email carries something specific, not a template.</li>'
            '<li><b>Quill</b> writes the first email and the follow ups in your voice, one prospect at a time.</li>'
            '<li><b>Your dedicated Agent Base manager</b> reads every draft, edits it or approves it. Nothing reaches a buyer without this step.</li>'
            '<li><b>Relay</b> sends approved emails at a safe pace and keeps the follow up schedule.</li>'
            '<li><b>Echo</b> reads every reply, sorts it and drafts the answer. Interested replies go straight to the Agent Base manager.</li>'
            '<li><b>Atlas</b> spots each booked meeting and writes a short brief.</li></ul>'
            '<p>The approval step only works if it is real. If the approver clicks "send" on every draft without reading it, you are back to an autonomous tool with an extra login. That is why the volume should be set by what one person can review carefully, not by what the software can send.</p>'
                    )),
        ('how-to-judge', 'How to judge an AI SDR before and after you sign', (
            '<p>Judge an AI SDR on qualified meetings, reply quality and domain health over a full 90 days, and ask before you sign who reads each email before it goes out. If the answer is "nobody" or "you can if you want to," expect the problems described above.</p>'
            '<p><b>Questions to ask before you sign:</b></p>'
            '<ul><li>Who reads each email before a buyer sees it, and what happens when they reject a draft?</li>'
            '<li>Can I see every draft, every edit and every reply, or only a summary?</li>'
            '<li>How do you decide daily send volume, and what happens if my spam rate rises?</li>'
            '<li>How is the ICP defined, and who updates it when the first replies come in?</li>'
            '<li>What counts as a qualified meeting, and is that written into the agreement?</li>'
            '</ul>'
            '<p><b>What to measure in the first 90 days:</b></p>'
            '<ul><li><b>Qualified meetings,</b> using a definition you agreed before launch. A meeting with the wrong person is not a result.</li>'
            '<li><b>Positive reply rate,</b> not total replies. "Remove me" and "wrong person" are signals too, and you want them falling.</li>'
            '<li><b>Domain health,</b> including the spam rate in Postmaster Tools and inbox placement. A program that books meetings while damaging your domain is borrowing from next quarter.</li>'
            '<li><b>Your own time.</b> Track the hours your team spends fixing or supervising the tool. If it is more than an SDR would need, the math has changed.</li>'
            '</ul>'
            '<p>Give it the full 90 days. Month one is mostly setup and learning the market, month two shows whether replies are improving, and month three tells you whether meetings turn into pipeline. Deciding after two weeks rewards tools that send the most, not the ones that work.</p>'
        )),
    ],
    'conclusion': (
        '<p>AI SDRs are worth it, but not in the form they were first sold. The autonomous version, where nobody reads what goes out, has a track record of cancelled contracts and burned domains. The version that works uses agents for the volume and keeps a person on the decisions buyers notice.</p>'
        '<ol><li><b>Split the work.</b> Agents find, research, draft, sort replies and brief. People choose the targets, approve the messages and run the conversations.</li>'
        '<li><b>Make the approval step real.</b> Set volume by what a person can review well.</li>'
        '<li><b>Protect the domain.</b> Watch the spam rate from day one and send at a safe pace.</li>'
        '<li><b>Insist on visibility.</b> You should see every draft, edit and reply.</li>'
        '<li><b>Measure for 90 days.</b> Qualified meetings, positive replies, domain health and your own time.</li></ol>'
        '<p>If you want to see how that looks in practice, book a call and we will show you the Agent Base and the dashboard your team would use.</p>'
    ),
    'faq': [
        ('Are AI SDRs worth it in 2026?', 'They are worth it when they handle research, drafting and reply sorting and a person approves what reaches each buyer. Fully autonomous AI SDRs have a weak track record so far, with many companies dropping them within months.'),
        ('Why do companies cancel AI SDR tools?', 'The usual reasons are a vague ICP, invented facts in emails, sending more than the domain can carry and no one reviewing the output. The tool also often needs far more supervision than buyers expected.'),
        ('Can an AI SDR fully replace a human SDR?', 'Not reliably today. Agents can replace much of the research and drafting time, but deciding who to contact, approving messages and handling interested replies still work best with a person.'),
        ('Do buyers know when an email was written by AI?', 'Often, yes, especially when it is generic or gets a fact wrong. Buyers also use AI themselves, and ' + a(GARTNER_BUYERS, 'Gartner found') + ' 69% check AI generated insights with a sales rep, so a human checked message builds more trust.'),
        ('What is a human in the loop AI SDR?', 'It is a setup where AI agents find accounts, research them and draft emails, and a named person reads and approves every message before it is sent. At BL Agency that person is the dedicated Agent Base manager.'),
        ('How long should I test an AI SDR before deciding?', 'Plan for 90 days. The first month is setup and learning, the second shows whether replies improve and the third shows whether meetings turn into real pipeline.'),
        ('Will an AI SDR hurt my email deliverability?', 'It can, if it sends too much too fast or writes to people who mark it as spam. Google asks bulk senders to keep the reported spam rate ' + a(GMAIL, 'below 0.3%') + ', so volume should follow what a person can review, not what the tool can send.'),
    ],
}
