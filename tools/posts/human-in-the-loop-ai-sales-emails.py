# Spec for blog/human-in-the-loop-ai-sales-emails.html. Build: python3 tools/blogkit.py tools/posts/human-in-the-loop-ai-sales-emails.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


SALESFORCE = 'https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/'
GARTNER_AGENTS = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027'
GARTNER_VALIDATE = 'https://www.businesswire.com/news/home/20260520585188/en/Gartner-Survey-Finds-69-of-B2B-Buyers-Turn-to-Sales-Reps-to-Validate-AI-Generated-Insights'
GOOGLE = 'https://support.google.com/mail/answer/81126?hl=en'
HUNTER = 'https://hunter.io/blog/the-cold-email-confidence-gap-why-senders-fear-ai-more-than-decision-makers'

fig1 = figure(1, bar_chart('Where sellers and buyers stand on AI in sales', [
    ('Sellers who used AI agents', 54),
    ('Buyers who used GenAI', 45),
    ('Buyers wary of GenAI info', 51),
    ('Buyers who check AI with a rep', 69),
], unit='%', vmax=100, highlight=('Buyers who check AI with a rep',)),
    'Sellers are adopting AI agents fast, and buyers use AI too, but most buyers still want a person to check what the AI told them. Sources: '
    + a(SALESFORCE, 'Salesforce State of Sales 2026') + ' (4,050 sales professionals) and '
    + a(GARTNER_VALIDATE, 'Gartner, May 2026') + ' (645 B2B buyers).')

fig2 = figure(2, table(['What can go wrong in an AI draft', 'Example', 'What the reviewer checks'], [
    ['<b>Wrong fact</b>', 'Congratulates a company on a funding round that was a competitor\'s', 'Every claim about the account is traceable to a source'],
    ['<b>Stale fact</b>', 'Mentions a leader who left the company months ago', 'The date of the signal and the person\'s current role'],
    ['<b>Wrong person</b>', 'Pitches a finance tool to the head of marketing', 'The contact owns the problem the email talks about'],
    ['<b>Wrong tone</b>', 'Jokes with a hospital administrator about "crushing" a quarter', 'The voice fits the buyer\'s industry and seniority'],
    ['<b>Overpromise</b>', 'Implies a result or feature the product does not have', 'Claims match what sales can actually deliver'],
    ['<b>Template smell</b>', 'Generic praise, three questions, a calendar link', 'One specific reason, one clear ask, short enough to read on a phone'],
]), 'The six most common problems a human reviewer catches in AI-written sales emails, with a typical example of each and the check that stops it.')

fig3 = figure(3, steps('Where the human sits in the Agent Base', [
    ('Scout', 'finds the account'),
    ('Lens', 'researches it'),
    ('Quill', 'drafts the email'),
    ('Manager', 'approves or edits'),
    ('Relay', 'sends at a safe pace'),
    ('Echo', 'sorts replies'),
], accent=('Manager',)),
    'Agents do the volume work on both sides of the review. The dedicated Agent Base manager (amber) is the only step that can clear an email to go to a buyer, and interested replies come back to the same person.')

POST = {
    'slug': 'human-in-the-loop-ai-sales-emails',
    'title': 'Human in the loop: why every AI-written sales email needs a reviewer',
    'h1': 'Human in the loop: why every AI-written email needs a <em>reviewer</em>',
    'description': 'What human in the loop means for AI-written sales emails, what a reviewer catches that the model misses, how to review at scale without slowing down, and how to tell if a vendor really has a person approving every email.',
    'category': 'AI and outbound',
    'date': '2026-11-19',
    'date_label': 'November 19, 2026',
    'hero_img': 'blog-human-review',
    'card_img': 'blog-human-review',
    'card_title': 'Human in the loop: why every AI-written email needs a reviewer',
    'card_text': 'AI can research and draft at scale. A person still has to decide what goes out under your name.',
    'takeaways': [
        'Human in the loop means a person reads and approves every AI-written email before it reaches a buyer. The AI researches and drafts; the human decides.',
        'Reviewers catch what models miss: wrong or stale facts, the wrong contact, a tone that does not fit, and claims your team cannot back up.',
        'Review protects more than one deal. Spam complaints and careless messages hurt your sending domain and your name with every account in your market.',
        'Review does not have to be slow. Agents prepare the research and the draft, so the reviewer spends a minute or two per email on judgment, not typing.',
    ],
    'intro': (
        '<p>AI can now research an account, find the right contact and write a first email in less time than it takes a person to open a CRM record. That speed is why so many sales teams tried fully autonomous AI SDRs. It is also why many of them pulled back: when nobody reads the emails, small mistakes go out at scale, under your company\'s name.</p>'
        '<p>The approach most teams are settling on in 2026 is simple to describe. Let AI do the research and the drafting, and keep a person in the loop who approves every email before it is sent. This guide explains what that means in practice, what a reviewer actually catches, how to keep review fast, and what to ask a vendor that says it has "human oversight".</p>'
    ),
    'cta': {
        'inline_lead': 'Want AI outbound with a person approving every email?',
        'inline_text': 'Book a 30 minute call. We will show you how the Agent Base drafts each email with AI and how your dedicated Agent Base manager reviews it before anything is sent.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'AI does the work. A person <em>decides</em> what goes out.',
        'band_text': 'Scout finds the account, Lens researches it, Quill drafts the email and your dedicated Agent Base manager reads, edits or approves it before Relay sends it. You watch every step on a live dashboard.',
    },
    'sections': [
        ('what-it-means', 'What human in the loop means for sales emails', (
            '<p>Human in the loop means a person reviews and approves each AI-written email before it is sent to a prospect. The AI does the research and writes the draft, and a human makes the final call on whether it goes out, gets edited or gets thrown away.</p>'
            '<p>The term comes from machine learning, where it describes any system in which a person checks or corrects the model\'s output. In outbound sales it has a narrower and more practical meaning. It is not a manager glancing at a weekly report or a sample of ten emails. It is one person who sees every message before a buyer does.</p>'
            '<p>It helps to separate three setups that vendors often blur together:</p>'
            '<ul><li><b>Fully autonomous:</b> the AI finds contacts, writes and sends. People only see results. Fast, but nobody catches a bad email until a prospect complains.</li>'
            '<li><b>Human on the loop:</b> the AI sends on its own while a person monitors dashboards and spot checks a sample. Better, but most emails still go out unread.</li>'
            '<li><b>Human in the loop:</b> nothing reaches a buyer until a person approves it. The AI does the volume work; the human owns the judgment.</li></ul>'
            '<p>Only the last one gives you a real answer to the question "who decided to send this?" That answer matters when a prospect replies angry, when a customer forwards an email to your CEO, or when an email makes a claim your product cannot back up.</p>'
            '<p>Human in the loop is not a step back from AI. It is how teams get the speed of AI research and drafting without handing their reputation to a model. We covered the wider comparison in ' + '<a href="/blog/ai-sdr-vs-human-sdr">AI SDR vs human SDR</a>' + '; this post is about the review step itself.</p>'
        )),
        ('why-now', 'Why the review step matters more in 2026', (
            '<p>The review step matters more now because almost everyone is using AI to write outreach, so buyers see more of it and trust it less. When every inbox is full of fluent, slightly generic emails, the one that is accurate and specific is the one that gets a reply.</p>'
            '<p>Adoption has moved fast. ' + a(SALESFORCE, 'Salesforce\'s State of Sales 2026') + ', a survey of 4,050 sales professionals, found that 54% of sellers have already used AI agents and nearly 9 in 10 plan to by 2027. Sellers expect agents to cut the time they spend on prospect research and email drafting by about a third.</p>'
            '<p>Buyers use AI too, and they are cautious about it. A ' + a(GARTNER_VALIDATE, 'Gartner survey of 645 B2B buyers') + ' published in May 2026 found that 45% used generative AI in a recent purchase, 51% said they are more likely to run into misleading information from it, and 69% prefer to validate AI-generated insights with a sales rep.</p>'
            + fig1 +
            '<p>Put those together and the picture is clear. Buyers expect AI-made content to be wrong some of the time, and they look for a person to confirm what is true. An email that reads as unchecked AI output starts the conversation on the wrong side of that doubt.</p>'
            '<p>The tools themselves are also still settling. ' + a(GARTNER_AGENTS, 'Gartner predicts') + ' that more than 40% of agentic AI projects will be canceled by the end of 2027, citing cost, unclear value and weak risk controls. A review step is one of the simplest risk controls you can add, and it is much easier than rebuilding a burned domain or a damaged account relationship.</p>'
        )),
        ('what-reviewers-catch', 'What a human reviewer catches that AI misses', (
            '<p>A reviewer catches mistakes of fact, fit and judgment that a model cannot see from inside the draft. The model writes what is likely; the reviewer checks what is true and what is wise to say.</p>'
            '<p>Most AI drafts read well. That is the problem. A fluent email with one wrong detail is more damaging than a clumsy one, because it looks careful and still gets the buyer\'s company wrong. These are the issues reviewers fix most often:</p>'
            + fig2 +
            '<p>Three of these deserve a closer look.</p>'
            '<ul><li><b>Stale and wrong facts.</b> Models and data providers both lag behind reality. A leader changes jobs, a product is renamed, a funding round belongs to a company with a similar name. A reviewer who opens the source behind each claim catches these in seconds.</li>'
            '<li><b>The wrong person.</b> AI is good at finding a name with the right title. It is less good at knowing whether that person owns the problem. A reviewer who knows your best customers can tell when a "VP of Operations" at one company does a completely different job from the one at another.</li>'
            '<li><b>Claims you cannot back up.</b> When a model fills a gap, it tends to promise. "We can cut your onboarding time in half" may sound good, but if nobody on your team would say it on a call, it should not be in an email.</li></ul>'
            '<p>There is also a quieter category: emails that are accurate but should not be sent. The account is in a sensitive moment, such as layoffs or a public incident, or a sales rep is already talking to someone there. A person who reads the account notes will stop those; a sequence will not.</p>'
        )),
        ('reputation', 'What one bad email costs: domain, brand and market', (
            '<p>One bad email rarely costs one deal. It can cost you sending reputation with email providers, credibility with a buyer you will want to reach again, and goodwill in a market where people talk to each other.</p>'
            '<p><b>Your sending domain.</b> Mailbox providers watch how people react to your mail. ' + a(GOOGLE, 'Google\'s email sender guidelines') + ' ask all senders to keep their spam rate reported in Postmaster Tools below 0.3%, and recommend staying under 0.1%. In cold outreach, the fastest way to raise spam reports is to send emails that feel careless or irrelevant. A reviewer who stops off-target sends is protecting the domain every future email depends on.</p>'
            '<p><b>Your name with the buyer.</b> Most B2B markets are smaller than they look. If you sell to heads of operations at mid-size logistics companies, there may be only a few thousand people who can buy from you. Each one you annoy is someone who will remember your company name the wrong way, and they will not get a second first impression.</p>'
            '<p><b>Your name in the market.</b> Bad AI outreach is now a genre people screenshot and post. One email that calls a prospect by the wrong name, references the wrong company or makes an odd claim can travel well beyond the inbox it landed in.</p>'
            '<p>None of this means AI-written email is unwelcome. ' + a(HUNTER, 'Hunter reports') + ' that 67% of decision-makers in its survey do not mind receiving AI-generated emails. What they mind is a bad email. The review step is how you make sure the emails people receive are the good kind, whoever drafted them.</p>'
        )),
        ('review-at-scale', 'How to review AI emails at scale without slowing down', (
            '<p>You review at scale by letting AI do everything except the decision. When research, sources and the draft arrive together, a trained reviewer can approve, edit or reject an email in a minute or two, so the human step adds judgment without adding a bottleneck.</p>'
            '<p>The teams that find review slow are usually asking the reviewer to redo the research. The fix is to prepare each email so it can be judged at a glance:</p>'
            '<ul><li><b>Show the sources next to the draft.</b> Every claim about the account should link to where it came from: a news story, a job post, a LinkedIn update. The reviewer checks the link, not the whole internet.</li>'
            '<li><b>Show why this account and this person.</b> One line on the signal and one line on why the contact owns the problem. If the reason is weak, the email gets rejected before anyone polishes it.</li>'
            '<li><b>Use a short checklist.</b> Facts true and current, right person, one clear reason, one small ask, nothing we cannot back up, tone fits the buyer. Six checks, every time.</li>'
            '<li><b>Edit the prompt, not just the email.</b> When the reviewer fixes the same issue three times, it becomes a rule for the drafting agent. Review quality goes up and review time goes down week by week.</li>'
            '<li><b>Track rejections.</b> The share of drafts that need major edits or get rejected is the best early signal of whether targeting and data are working.</li></ul>'
            '<p>Speed also comes from separating the steps. Agents can research and draft overnight so drafts are waiting when the reviewer starts. Approved emails then go out at a safe, steady pace instead of in bursts.</p>'
            + fig3 +
            '<p>In the Agent Base, that is the exact order: Scout finds accounts with a reason to buy, Lens researches each one, Quill drafts, the dedicated Agent Base manager approves or edits, Relay sends, and Echo sorts the replies and passes the interested ones back to the manager. Atlas then writes a short brief for each booked meeting.</p>'
        )),
        ('who-reviews', 'Who should be the reviewer', (
            '<p>The reviewer should be someone who understands your buyer and your offer well enough to say no, not just someone who can fix grammar. In practice that means an experienced SDR, a sales manager or a dedicated outbound specialist who knows the market and owns the results.</p>'
            '<p>Look for four things in the person who holds this job:</p>'
            '<ul><li><b>Buyer knowledge.</b> They can tell a real reason to reach out from a weak one, and they know which titles actually buy.</li>'
            '<li><b>Strong written English.</b> They can hear when an email sounds like a template or like a person, and fix it in a few words.</li>'
            '<li><b>Willingness to reject.</b> A reviewer who approves almost everything is not reviewing. A good one throws away drafts that are fine but not worth sending.</li>'
            '<li><b>Ownership of replies.</b> The same person should handle the interested replies. Nothing teaches better judgment about what to send than reading what comes back.</li></ul>'
            '<p>It also matters that the reviewer has authority. If the person reading drafts can only flag issues to someone else, review turns into a queue. They should be able to edit, approve and reject on their own, and change the targeting when the same problem keeps coming back.</p>'
            '<p>This is why the Agent Base gives every client one dedicated Agent Base manager rather than a pool of anonymous checkers. One person learns your market, your voice and your no-go list, reads every draft and is your single point of contact. If you would rather build the role in house, our <a href="/blog/sdr-interview-process">20-minute SDR screen</a> works well for testing judgment and written English in candidates for this job.</p>'
        )),
        ('vendor-questions', 'How to tell if a vendor really has a human in the loop', (
            '<p>Ask to see the review step, not hear about it. A vendor with a real human in the loop can show you, on a live account, the draft, the person who approved it, what they changed and when it was sent.</p>'
            '<p>"Human oversight" can mean anything from one person reading every email to a weekly look at a dashboard. These questions separate the two quickly:</p>'
            '<ol><li><b>Does a person read every email before it is sent, or a sample?</b> Ask for the share in writing.</li>'
            '<li><b>Who is that person, and how many clients do they cover?</b> A reviewer spread across dozens of accounts cannot know any of them well.</li>'
            '<li><b>Can I see the edit history?</b> If drafts are never edited or rejected, the review is not real.</li>'
            '<li><b>What happens to replies?</b> Interested replies should reach a person fast, not another automated sequence.</li>'
            '<li><b>Can I set a no-go list and approve the voice?</b> You should control which accounts and claims are off limits.</li>'
            '<li><b>Can I watch it happen?</b> A live dashboard of research, drafts, approvals and replies is the easiest proof that the loop exists.</li></ol>'
            '<p>We go deeper on vetting outbound providers in <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a>. For the review step, the short version is this: if nobody can show you the person, assume there is not one.</p>'
        )),
    ],
    'conclusion': (
        '<p>AI has made research and drafting fast to scale. It has not made judgment automatic. The teams getting good results from AI outbound in 2026 keep a person between the draft and the buyer.</p>'
        '<ol><li><b>Define the loop:</b> a person approves every email before it is sent, not a sample.</li>'
        '<li><b>Know what to check:</b> facts, freshness, the right person, tone, and claims you can back up.</li>'
        '<li><b>Protect the domain:</b> careless sends raise spam complaints that hurt every future email.</li>'
        '<li><b>Make review fast:</b> sources and reasons next to each draft, a short checklist, and prompt fixes for repeat issues.</li>'
        '<li><b>Pick the right reviewer:</b> someone who knows the buyer, writes well, rejects freely and owns the replies.</li>'
        '<li><b>Verify vendors:</b> ask to see the person, the edits and the approvals on a live account.</li></ol>'
        '<p>If you want AI outbound with a person approving every email, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will walk you through the Agent Base on a live dashboard.</p>'
    ),
    'faq': [
        ('What does human in the loop mean in AI sales outreach?',
         'It means a person reviews and approves every AI-written email before it reaches a prospect. The AI researches the account and drafts the message, and the human decides whether it is sent, edited or discarded.'),
        ('Is human in the loop the same as human oversight?',
         'Not always. Human oversight can mean someone watching a dashboard or spot checking a sample while the AI sends on its own. Human in the loop means nothing is sent without a person approving it.'),
        ('Does reviewing every AI email slow down outbound?',
         'Less than most teams expect. When the research, sources and draft arrive together, a trained reviewer can approve or fix an email in a minute or two. The agents still do the slow work of finding accounts and writing drafts.'),
        ('Do buyers mind receiving AI-written emails?',
         'Many do not. Hunter reports that 67% of decision-makers in its survey do not mind AI-generated emails. What buyers react to is a careless or inaccurate email, which is exactly what a reviewer stops.'),
        ('What should a reviewer check in an AI-written sales email?',
         'That every fact is true and current, the contact owns the problem, there is one clear reason for reaching out, the ask is small, the tone fits the buyer, and nothing promises more than your team can deliver.'),
        ('Can AI review its own emails instead of a person?',
         'AI checks can catch spelling, length and some factual mismatches, and they are a useful first pass. They cannot judge whether a message is wise to send under your name, which is the part that protects your reputation.'),
        ('How does the Agent Base handle review?',
         'Every client has a dedicated Agent Base manager. Quill drafts each email, the manager reads it and edits or approves it, and only then does Relay send it. Interested replies come back to the same person, and you can watch the whole flow on a live dashboard.'),
    ],
}
