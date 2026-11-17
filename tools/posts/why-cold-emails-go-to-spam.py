# Spec for blog/why-cold-emails-go-to-spam.html. Build: python3 tools/blogkit.py tools/posts/why-cold-emails-go-to-spam.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GOOGLE = 'https://support.google.com/mail/answer/81126'
GOOGLE_TOP = 'https://support.google.com/mail/answer/15256272'
GOOGLE_FAQ = 'https://support.google.com/a/answer/14229414'
YAHOO = 'https://senders.yahooinc.com/best-practices'
MICROSOFT = 'https://www.mailgun.com/blog/deliverability/microsoft-sender-requirements/'
GMAIL_2025 = 'https://www.captaindns.com/en/blog/gmail-bulk-sender-2025'
FTC = 'https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'

fig1 = figure(1, table(['Requirement', 'Gmail', 'Yahoo', 'Outlook (Microsoft)'], [
    ['<b>SPF and DKIM</b>', 'One of them for all senders; both above 5,000 messages a day', 'One of them for all senders; both for bulk senders', 'Both, for senders above 5,000 messages a day'],
    ['<b>DMARC</b>', 'Required above 5,000 a day (p=none is enough), with the From domain aligned', 'Required for bulk senders (p=none is enough), with alignment', 'Required above 5,000 a day (p=none is enough), aligned with SPF or DKIM'],
    ['<b>Spam complaint rate</b>', 'Below 0.3%, and Google recommends staying below 0.1%', 'Below 0.3%', 'No published threshold; complaints still hurt reputation'],
    ['<b>Unsubscribe</b>', 'One-click for marketing and subscribed mail above 5,000 a day', 'One-click for bulk, honored within 2 days', 'A visible, working unsubscribe link expected'],
    ['<b>DNS and transport</b>', 'Valid forward and reverse DNS, TLS', 'Valid forward and reverse DNS', 'Not published as a rule; From and Reply-To addresses should accept replies'],
]), 'What the three largest mailbox providers ask of senders. Sources: ' + a(GOOGLE, 'Google email sender guidelines') + ', ' + a(YAHOO, 'Yahoo sender best practices') + ' and a ' + a(MICROSOFT, 'summary of Microsoft\'s May 2025 requirements') + '. Even if you send far fewer than 5,000 a day, treat the bulk column as the standard: it is what filters reward.')

fig2 = figure(2, timeline('A new sending domain, from setup to full volume', [
    (0, 1, 'Set up', 'domains, DNS, inboxes'),
    (1, 3, 'Warm up', 'low volume, real replies'),
    (3, 6, 'Ramp slowly', 'small weekly increases'),
    (6, 8, 'Steady', 'consistent daily pace'),
], 8, unit='wk', accent=('Warm up',)),
    'A cautious shape for a new cold email domain. The warm-up weeks (amber) feel slow, and they are the cheapest insurance you can buy. Google\'s guidance is to start low, increase gradually and avoid sudden spikes.')

fig3 = figure(3, steps('Spam folder diagnostic, in order', [
    ('Authentication', 'SPF, DKIM, DMARC'),
    ('Reputation', 'Postmaster data'),
    ('Volume', 'per inbox, per day'),
    ('List', 'bounces, old data'),
    ('Message', 'links, tracking, copy'),
], accent=('Authentication',)),
    'Check the causes in this order. Each step is quicker to rule out than the next, and a failure early in the chain (amber) makes everything after it irrelevant.')

POST = {
    'slug': 'why-cold-emails-go-to-spam',
    'title': 'Why are my cold emails going to spam? A practical diagnosis',
    'h1': 'Why are my cold emails going to <em>spam?</em>',
    'description': 'The real reasons cold emails land in spam: missing SPF, DKIM and DMARC, new or overloaded domains, spam complaints, old lists and risky message habits. A step by step diagnosis and how to fix each one.',
    'category': 'Outbound',
    'date': '2026-11-17',
    'date_label': 'November 17, 2026',
    'hero_img': 'blog-email',
    'card_img': 'blog-email',
    'card_title': 'Why are my cold emails going to spam?',
    'card_text': 'Authentication, domain reputation, complaints, lists and copy: how to find which one is sinking your outbound.',
    'takeaways': [
        'Cold emails usually land in spam for one of five reasons: broken authentication, a new or overloaded domain, too many spam complaints, a stale list or risky message habits.',
        'Gmail, Yahoo and Outlook now require SPF, DKIM and DMARC for high-volume senders, and Gmail wants your complaint rate below 0.3%, ideally below 0.1%.',
        'Copy tweaks rarely fix a spam problem on their own. Check authentication and reputation first, then volume, then the list, then the message.',
        'The lasting fix is fewer, better targeted emails: buyers who find a message relevant do not press the spam button, and that signal is what filters weigh most.',
    ],
    'intro': (
        '<p>You wrote a careful email, loaded a list and pressed send. Replies never came, and when you sent a test to your own Gmail it landed in spam, or never arrived at all. It is one of the most common questions founders and sales leaders type into Google, and the honest answer is that there is rarely a single cause.</p>'
        '<p>Mailbox providers decide where your email goes from a mix of signals: whether your domain proves who you are, how your domain has behaved before, how recipients react, how clean your list is and what the message itself looks like. This guide walks through each one, in the order you should check them, with what Gmail, Yahoo and Microsoft say in their own documentation. We run outbound for US B2B companies, so we also show how we set this up before a single campaign goes live.</p>'
    ),
    'cta': {
        'inline_lead': 'Rather not fight the spam folder yourself?',
        'inline_text': 'Book a 30 minute call. We will show you the Agent Base: warmed inboxes, a safe sending pace and a dedicated Agent Base manager who approves every email before it goes out.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound that reaches the <em>inbox</em>, approved by a person.',
        'band_text': 'Mailboxes are set up and warmed before campaigns start. Quill drafts each email, your dedicated Agent Base manager approves it, and Relay sends at a safe pace. You watch it all on a live dashboard.',
    },
    'sections': [
        ('short-answer', 'The short answer: five reasons cold emails land in spam', (
            '<p>Cold emails go to spam because the receiving mailbox provider does not trust the sender enough. That lack of trust almost always comes from one of five places: authentication, domain reputation, recipient complaints, list quality or the message itself.</p>'
            '<p>Spam filters at Gmail, Yahoo and Outlook do not read your email the way a person does and decide it is "salesy". They combine technical checks with behavior over time. A perfectly written email from a domain registered last week, sending 300 messages on day one to an old list, will land in spam. A plain, slightly clumsy email from a well-authenticated domain with a history of replies will often reach the inbox.</p>'
            '<p>Here are the five causes, in the order you should check them:</p>'
            '<ol><li><b>Authentication is missing or broken.</b> SPF, DKIM or DMARC are not set, are set on the wrong domain or do not align with the From address.</li>'
            '<li><b>The domain has no reputation yet, or a bad one.</b> New domains that send at full volume straight away, or domains that sent too much too fast in the past.</li>'
            '<li><b>Too many people mark you as spam.</b> Complaints are the strongest negative signal a sender can get, and cold outreach to the wrong people produces them quickly.</li>'
            '<li><b>The list is stale or unverified.</b> High bounce rates and old addresses tell providers you are not careful about who you write to.</li>'
            '<li><b>The message looks risky.</b> Link-heavy templates, tracking domains shared with thousands of other senders, misleading subject lines and identical copy sent to everyone.</li></ol>'
            '<p>The rest of this guide takes each cause in turn and ends with a diagnostic you can run this week.</p>'
        )),
        ('authentication', 'Authentication: what Gmail, Yahoo and Outlook now require', (
            '<p>Authentication is the first thing to check, because without it nothing else matters. Gmail, Yahoo and Microsoft all require SPF, DKIM and DMARC for senders above roughly 5,000 messages a day, and they all reward smaller senders who set them up the same way.</p>'
            '<p>The three records do different jobs. <b>SPF</b> lists the servers allowed to send for your domain. <b>DKIM</b> adds a signature that proves the message was not changed on the way. <b>DMARC</b> tells the receiver what to do when SPF or DKIM fail, and requires that the domain in your From address matches the domain that passed the check. That last point, called alignment, is where many cold email setups quietly fail: the sending tool signs with its own domain, so DKIM passes but does not align with yours.</p>'
            + fig1 +
            '<p>The rules have tightened year by year. ' + a(GOOGLE, 'Google\'s sender guidelines') + ' have required authentication since February 2024, and from November 2025 Gmail began ' + a(GMAIL_2025, 'rejecting non-compliant mail more often') + ' instead of only filtering it. Microsoft started routing non-compliant mail from high-volume senders to the Junk folder from May 5, 2025, with outright rejections to follow.</p>'
            '<p>What to do:</p>'
            '<ul><li><b>Check each sending domain.</b> Use any free DNS lookup or your provider\'s admin console to confirm SPF, DKIM and DMARC records exist and pass. Send a test to a Gmail address, open it, choose "Show original" and look for PASS on all three.</li>'
            '<li><b>Confirm alignment.</b> The domain in the From line should be the domain that signs DKIM. If your sending tool uses its own domain, set up custom DKIM for yours.</li>'
            '<li><b>Start DMARC at p=none with reporting.</b> It meets the requirement and the reports show you every service sending as your domain, including ones you forgot.</li>'
            '<li><b>Use DKIM keys of 2048 bits</b> if your provider supports them, which Google recommends.</li></ul>'
        )),
        ('reputation', 'Domain reputation: new domains, sudden volume and shared infrastructure', (
            '<p>If authentication passes and you still land in spam, the most likely cause is reputation. Mailbox providers judge a domain by its history, and a new domain, or one that suddenly sends much more than usual, has no history worth trusting.</p>'
            '<p>Google is direct about this. Its ' + a(GOOGLE_TOP, 'list of the top Gmail sender issues') + ' tells senders to keep volumes consistent rather than sending in bursts, especially from new domains, and its main guidelines warn that suddenly doubling your volume can trigger rate limits or a drop in reputation. The safe pattern is to start with low volume to people likely to engage and increase gradually.</p>'
            + fig2 +
            '<p>Three habits damage reputation most often in cold outbound:</p>'
            '<ul><li><b>Sending cold email from your main domain.</b> If that domain gets a bad reputation, your invoices, proposals and support replies start landing in spam too. Use separate, clearly related sending domains, and keep your primary domain for day to day mail.</li>'
            '<li><b>Skipping the warm-up.</b> Buying a domain on Monday and sending a full campaign on Tuesday is the single fastest route to the spam folder. New inboxes need a few weeks of low, steady volume first.</li>'
            '<li><b>Too much volume per inbox.</b> Spreading a campaign across several warmed inboxes at a modest daily pace is safer than pushing hundreds of messages through one.</li></ul>'
            '<p>Shared infrastructure matters too. Google\'s top-issues list warns that sharing IP addresses and domains with other senders can lower reputation for everyone using them. Many cold email tools route open and click tracking through one shared domain. If other senders on that domain are spamming, your links inherit their reputation. A custom tracking domain, or no tracking at all, removes that risk.</p>'
            '<p>To see how Gmail views you, set up ' + a(GOOGLE_FAQ, 'Google Postmaster Tools') + ' for each sending domain. It shows spam rate, authentication results and delivery errors, although low-volume senders may see little data at first.</p>'
        )),
        ('complaints', 'Spam complaints: the signal that outweighs everything else', (
            '<p>Spam complaints are the strongest reason a healthy domain slides into the spam folder. Gmail requires senders to keep their complaint rate below 0.3% and recommends staying below 0.1%, which means one complaint per thousand delivered emails is already the comfortable ceiling.</p>'
            '<p>Cold email lives closer to that line than any other kind of mail, because the recipient did not ask to hear from you. Google\'s own guidance says not to send to people who did not sign up, and ' + a(YAHOO, 'Yahoo') + ' uses the same 0.3% threshold, calculated on mail delivered to the inbox. B2B outreach to a carefully chosen buyer is legal in the US under the ' + a(FTC, 'CAN-SPAM Act') + ' when you identify yourself, use honest headers and subject lines, include a physical address and honor opt-outs within 10 business days. But being legal does not stop the spam button. Relevance does.</p>'
            '<p>Buyers are not shy about it. A ' + a(GARTNER, 'Gartner survey of 632 B2B buyers') + ' found that 73% actively avoid suppliers who send irrelevant outreach. Every irrelevant email you send is a small bet that the reader will complain instead of ignoring you.</p>'
            '<p>How to keep complaints low:</p>'
            '<ul><li><b>Narrow the list.</b> Write only to people whose role and company match a problem you solve. A smaller list with a clear reason to write beats a large one every time.</li>'
            '<li><b>Give each email a specific reason.</b> A reference to something real about the company, a hiring push, a new market or a product launch, tells the reader this is not a blast.</li>'
            '<li><b>Make opting out easy.</b> A plain line such as "Not relevant? Reply and I will not write again" turns a potential complaint into a polite reply. Honor it the same day.</li>'
            '<li><b>Stop sooner.</b> Long follow-up sequences to people who never opened anything mostly produce complaints. Three or four touches are usually enough.</li>'
            '<li><b>Watch the trend weekly.</b> If Postmaster Tools shows the spam rate rising, pause the segment that is causing it before the domain pays the price.</li></ul>'
        )),
        ('list-quality', 'List quality: bounces, old data and addresses nobody reads', (
            '<p>A poor list sends you to spam in two ways: high bounce rates tell providers you do not know who you are writing to, and old or abandoned addresses can be recycled into spam traps. Verify every address before you send and remove anything that bounces at once.</p>'
            '<p>B2B data decays quickly. People change jobs, companies rebrand and domains expire. A list bought or exported six months ago will contain addresses that no longer exist, and a hard bounce is one of the clearest signs of careless sending. Google\'s guidelines also tell senders not to buy email addresses from other companies.</p>'
            '<p>What good list hygiene looks like in practice:</p>'
            '<ul><li><b>Verify before every campaign,</b> not once a year. Remove invalid addresses and treat "catch-all" domains, which accept anything, with caution.</li>'
            '<li><b>Remove hard bounces immediately</b> and do not retry them from another inbox.</li>'
            '<li><b>Avoid role addresses</b> such as info@ or sales@ for cold outreach. They are often shared, filtered more aggressively and more likely to produce complaints.</li>'
            '<li><b>Build lists from current signals.</b> A company that posted a relevant job this month, raised funding or opened a new office is both easier to verify and more likely to care.</li>'
            '<li><b>Keep a suppression list</b> of everyone who opted out or complained, shared across every tool and inbox you use.</li></ul>'
            '<p>The common thread with complaints is that list quality and relevance are the same decision. The work you do to find the right people is also the work that keeps you out of spam.</p>'
        )),
        ('message', 'The message: links, tracking, images and misleading habits', (
            '<p>The content of the email matters less than most people think, but some habits do raise the risk. The main ones are too many links, shared tracking domains, image-heavy templates, misleading subject lines and sending the identical text to hundreds of people.</p>'
            '<p>Filters care less about individual "spam words" than about patterns that look like bulk or deceptive mail. Google\'s top-issues list names a few directly: do not use emojis or images to imply the message is verified, and do not put "Re:" or "Fwd:" on a message that is not a reply or a forward. The FTC says the same thing from the legal side: subject lines must not mislead.</p>'
            '<p>Practical rules for cold email copy:</p>'
            '<ul><li><b>Write in plain text.</b> A short message that looks like a person wrote it to one other person. No banners, no heavy formatting, no attachments on the first touch.</li>'
            '<li><b>Use one link at most,</b> and none in the first email if you can avoid it. Links to unfamiliar or shortened URLs are a common filtering trigger.</li>'
            '<li><b>Turn off open tracking</b> or use a custom tracking domain. Tracking pixels and redirect links add risk and are less reliable than they used to be.</li>'
            '<li><b>Vary the message.</b> If every email in a campaign is identical except the first name, filters see a blast. Real, account-specific lines make each message different.</li>'
            '<li><b>Use a real sender.</b> A named person, a From address that accepts replies and a signature with your company and physical address.</li></ul>'
            '<p>If you fix the copy but the problem stays, go back to authentication and reputation. Message changes cannot rescue a domain that providers already distrust.</p>'
        )),
        ('diagnose-and-fix', 'How to diagnose your spam problem this week, and how we prevent it', (
            '<p>To find the cause, check in a fixed order: authentication first, then domain reputation, then sending volume, then the list and finally the message. Each step is faster to rule out than the next, and an early failure makes later fixes pointless.</p>'
            + fig3 +
            '<ol><li><b>Authentication.</b> Send a test to Gmail and Outlook addresses, open the headers and confirm SPF, DKIM and DMARC all pass and align with your From domain.</li>'
            '<li><b>Reputation.</b> Open Postmaster Tools for each sending domain. Look at spam rate and any delivery errors. If the domain is new, assume it has not earned trust yet.</li>'
            '<li><b>Volume.</b> Count how many emails each inbox sends per day and how that changed recently. A recent jump is a strong suspect.</li>'
            '<li><b>List.</b> Check the bounce rate of the last campaign and when the data was last verified.</li>'
            '<li><b>Message.</b> Count links, check tracking, and read the subject line as a stranger would.</li></ol>'
            '<p>If a domain is badly damaged, the fastest path is often to pause it, fix the cause and warm up a fresh one slowly rather than trying to push through.</p>'
            '<p><b>How the Agent Base handles this.</b> We start every program with about three weeks of setup and email warm-up before any campaign goes live. Mailboxes are set up and warmed, and volume stays sensible. Scout finds companies with a current reason to buy and Lens researches each one, so every email carries something specific to that account, which keeps complaints low. Quill drafts the email, and your dedicated Agent Base manager reads and approves every draft before it is sent. Relay then sends approved emails at a safe pace and keeps the follow-up schedule, and Echo reads and sorts every reply. You can see each email and reply on a live dashboard, so a deliverability problem is visible the day it starts.</p>'
        )),
    ],
    'conclusion': (
        '<p>Cold emails land in spam when mailbox providers do not trust the sender. The fix is rarely a clever subject line. It is a set of basic, unglamorous habits kept every day.</p>'
        '<ol><li><b>Authenticate every sending domain</b> with SPF, DKIM and DMARC, and make sure they align with your From address.</li>'
        '<li><b>Protect reputation:</b> separate sending domains, a real warm-up and small, steady daily volumes per inbox.</li>'
        '<li><b>Keep complaints under 0.1%</b> by writing only to people with a clear reason to hear from you and making opt-out easy.</li>'
        '<li><b>Verify the list</b> before each campaign and remove bounces at once.</li>'
        '<li><b>Write plain, specific emails</b> with few links, honest subject lines and a real sender.</li>'
        '<li><b>Diagnose in order:</b> authentication, reputation, volume, list, message.</li></ol>'
        '<p>If you would rather have this run for you, <a href="' + CAL + '"' + EXT + '>book a call</a> and we will walk you through the Agent Base, from warm-up to the approved emails on your dashboard.</p>'
    ),
    'faq': [
        ('Why are my cold emails going to spam even though my copy is good?',
         'Because filters judge the sender before the copy. Missing or misaligned SPF, DKIM and DMARC, a new domain sending too much too soon, a history of spam complaints or a list with many bounces will send even a well written email to spam.'),
        ('Do I need SPF, DKIM and DMARC for cold email?',
         'Yes. Gmail, Yahoo and Microsoft require all three for senders above about 5,000 messages a day, and smaller senders who set them up are treated better. DMARC can start at p=none, but the From domain should align with the domain that passes SPF or DKIM.'),
        ('What spam complaint rate is too high?',
         'Gmail requires a spam rate below 0.3% and recommends staying below 0.1%. Yahoo uses the same 0.3% limit. For cold email, treat 0.1% as the real ceiling and pause any segment that pushes you toward it.'),
        ('How long should I warm up a new domain before sending cold email?',
         'Plan for a few weeks of low, steady volume before a full campaign, then increase gradually. Google advises avoiding sudden spikes and sending at a consistent rate. We use about three weeks of setup and warm-up before campaigns go live.'),
        ('Should I send cold email from my main company domain?',
         'It is safer not to. If a cold campaign damages that domain\'s reputation, your everyday business email suffers too. Use separate, clearly related sending domains, fully authenticated, and keep your primary domain for normal mail.'),
        ('Does open tracking hurt deliverability?',
         'It can. Tracking pixels and redirect links add risk, and many tools route them through a shared domain whose reputation you do not control. Turn tracking off or use a custom tracking domain, and judge campaigns by replies.'),
        ('How do I check whether my emails are landing in spam?',
         'Send tests to Gmail and Outlook addresses you control, check the headers for SPF, DKIM and DMARC passes, and set up Google Postmaster Tools for each sending domain to see your spam rate and delivery errors over time.'),
    ],
}
