# Spec for blog/why-outsourced-sdr-programs-fail.html. Build: python3 tools/blogkit.py tools/posts/why-outsourced-sdr-programs-fail.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


SAASTR = 'https://www.saastr.com/only-7-of-you-have-really-gotten-outsourced-sdrs-to-work'
GARTNER = 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience'
GOOGLE = 'https://support.google.com/a/answer/14229414'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
FTC = 'https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business'

fig1 = figure(1, bar_chart('SaaStr poll: did outsourced SDRs work for you?', [
    ('Really worked', 7),
    ('Sort of worked', 26),
    ('Everyone else', 67),
], unit='%', vmax=100, highlight=('Really worked',)),
    f'Answers from a SaaStr poll of more than 1,200 people. Only 7% said outsourced SDRs really worked; "Everyone else" is the remainder we calculated from the two published figures. Source: {a(SAASTR, "SaaStr")}.')

fig2 = figure(2, timeline('Month one checkpoints for an outsourced SDR program', [
    (0, 1, 'Definitions', 'meeting and ICP in writing'),
    (1, 2, 'First drafts', 'you approve the sequence'),
    (2, 3, 'First replies', 'you read them, not a summary'),
    (3, 4, 'First review', 'replies, objections, fit'),
], total=4, unit='wk', accent=('First replies',)),
    'What should have happened by the end of each week of month one. The amber week is the most telling: if you cannot read real replies by week three, you will not be able to judge quality later either.')

fig3 = figure(3, table(['Month one signal', 'What it usually means', 'What good looks like'], [
    ['<b>No written meeting definition</b>', 'Every booked call will count, fit or not.', 'A one-page definition you signed off before launch.'],
    ['<b>You never saw the first sequence</b>', 'Generic templates are going out in your name.', 'You approved the emails and the follow ups.'],
    ['<b>Reports are only activity counts</b>', 'Volume is being optimized, not relevance.', 'A weekly review of actual replies and objections.'],
    ['<b>Nobody asked for your call recordings</b>', 'The team is not learning your buyer.', 'Onboarding used your wins, losses and objections.'],
    ['<b>Bounce or spam complaints climbing</b>', 'Lists are weak or sending is too aggressive.', 'Authentication in place and complaint rates watched.'],
    ['<b>Your contact changed already</b>', 'Turnover, or your account is low priority.', 'Named people and a written handover plan.'],
]), 'Six warning signs that show up in the first month, and what they usually mean. One of them is a conversation. Three or more is a pattern.')

POST = {
    'slug': 'why-outsourced-sdr-programs-fail',
    'title': 'Why outsourced SDR programs fail (and how to spot it in month one)',
    'h1': 'Why outsourced SDR programs fail, and how to spot it in <em>month one</em>',
    'description': 'Why most outsourced SDR programs fail: loose meeting definitions, teams that never learn the buyer, volume over relevance and no visibility. Plus the warning signs to check in month one.',
    'category': 'Outbound',
    'date': '2026-11-13',
    'date_label': 'November 13, 2026',
    'hero_img': 'blog-sdr-program-fails',
    'card_img': 'blog-sdr-program-fails',
    'card_title': 'Why outsourced SDR programs fail (and how to spot it in month one)',
    'card_text': 'The four reasons most programs disappoint, and the warning signs you can see in the first four weeks.',
    'takeaways': [
        'In a SaaStr poll of more than 1,200 people, only 7% said outsourced SDRs really worked for them. The failures follow a small number of repeat patterns.',
        'The four big ones: nobody defined the meeting, the team never learned the buyer, volume replaced relevance, and the client could not see the work.',
        'Each of them is visible in month one if you know where to look. You do not need to wait for a disappointing quarter.',
        'Fixing a program usually means less volume and more review: a written meeting definition, approved messaging, and a weekly read of real replies.',
    ],
    'intro': (
        '<p>Most founders who hire an outsourced SDR team do not decide it failed on a specific day. It fades. The first weeks are busy and promising, the reports show plenty of activity, a few meetings appear, and then sometime around month three the sales team admits that the meetings are not turning into pipeline. By then a quarter is gone, and so is some goodwill with the accounts that were emailed.</p>'
        '<p>The good news is that the reasons are not mysterious. The same few patterns explain most failures, and nearly all of them leave traces in the first four weeks. This guide walks through why outsourced SDR programs fail, what each failure looks like early, and what to do about it. We run an outbound service ourselves, so we also explain how we designed ours around these problems, and where we are not the right fit.</p>'
    ),
    'cta': {
        'inline_lead': 'Worried your outbound program is drifting?',
        'inline_text': 'Book a 30 minute call. We will walk you through the Agent Base, where AI agents research and draft and a dedicated Agent Base manager approves every email before it is sent.',
        'href': CAL,
        'target': EXT,
        'button': 'Book a call',
        'band_label': 'The Agent Base',
        'band_h2': 'Outbound you can <em>see</em> from week one.',
        'band_text': 'Scout finds the accounts, Lens researches them and Quill drafts the email. Your dedicated Agent Base manager approves every message, and you watch the work on a live dashboard.',
    },
    'sections': [
        ('short-answer', 'The short answer: most programs fail for the same few reasons', (
            '<p>Outsourced SDR programs mostly fail because the agency is asked to sell something it does not understand, to a buyer nobody defined, and is measured on numbers that do not reflect quality. When SaaStr asked its audience, only 7% of more than 1,200 respondents said outsourced SDRs had really worked, and another 26% said they had sort of worked, according to ' + a(SAASTR, 'Jason Lemkin\'s write-up of the poll') + '.</p>'
            '<p>Lemkin\'s own explanation is simple: it is hard to outsource something you do not already know well yourself. He writes that he has only had success outsourcing a function when he had already done it well in house, and when he treated the outside team as part of the core team. Commenters in the same thread add the usual details: complex products need deep product knowledge, and companies often outsource sales development before they have made it work internally.</p>'
            + fig1 +
            '<p>That poll is not a scientific study, and it mixes very different kinds of companies and agencies. But it matches what buyers describe in forums and what agencies admit in their own guides. When we read the complaints side by side, four patterns cover almost all of them:</p>'
            '<ol><li><b>Nobody defined the meeting</b>, so anything with a calendar invite counted.</li>'
            '<li><b>The team never learned the buyer</b>, so the messages were generic.</li>'
            '<li><b>Volume replaced relevance</b>, which hurt both replies and deliverability.</li>'
            '<li><b>The client could not see the work</b>, so problems surfaced months late.</li></ol>'
            '<p>The rest of this guide takes them one at a time, then shows how to check for all four in your first month.</p>'
        )),
        ('the-meeting', 'Failure 1: nobody defined what a meeting is', (
            '<p>The most common failure is a missing definition. If you and the agency never agreed in writing on who counts as a qualified meeting, every booked call becomes a win on their report and a waste of time on yours. This is where most disputes between clients and agencies begin.</p>'
            '<p>It happens because "book meetings with decision makers" sounds specific on a sales call and is not. Does a manager count, or only a director? Does a company with twenty employees count if your product needs two hundred? Does the person need to have the problem you solve, or just agree to talk? If nobody wrote it down, the agency will answer those questions in the direction that makes its numbers look best, often without meaning to.</p>'
            '<p>The damage goes beyond wasted calls. When account executives notice that a share of booked meetings are poor fits, they start preparing less for all of them. Show rates fall, the good meetings get a weaker first call, and the program looks worse than it is. A loose definition does not only let bad meetings in; it lowers the value of the good ones.</p>'
            '<p><b>How to spot it in month one:</b> ask to see the meeting definition in writing before launch. It should name the titles or roles, the company profile (industry, size, region), the problem the person must have, and what the SDR must confirm before booking. It should also say what happens with no-shows and with meetings you flag as not a fit. If, at the end of week one, there is no such document, you have found the first warning sign.</p>'
            '<p>We cover the full list of contract questions in our guide to <a href="/blog/questions-to-ask-outsourced-sdr-agency">12 questions to ask an outsourced SDR agency</a>. If you only ask one, ask this one.</p>'
        )),
        ('the-buyer', 'Failure 2: the team never learned your buyer', (
            '<p>The second failure is shallow knowledge. An outside team that never studied your product, your customers and the objections your sales team hears will write emails that could be sent by any company in your category, and buyers can tell. This is Lemkin\'s core point: it is hard to hand off something you do not know well yourself, and harder still for someone who has never met your customers.</p>'
            '<p>Even inside a company, learning the job takes time. The Bridge Group\'s ' + a(BRIDGE25, '2025 SDR Metrics Report') + ' puts average SDR ramp at 3.0 months for in-house reps who sit next to the product team. An outside rep who works several clients at once, and who received a questionnaire instead of a real onboarding, will not get there faster.</p>'
            '<p><b>How to spot it in month one:</b> watch what the agency asks you for. A team that intends to learn your buyer will ask for recorded sales calls, recent wins and losses, the objections that repeat, and time with someone who sells today. A team that does not ask is planning to work from templates. Then read the first sequence before it goes out and ask yourself one question: would my best customer have replied to this when they were still a prospect?</p>'
            '<p>This failure is also why outsourcing before you have any sales motion of your own is risky. If you cannot yet explain why your customers buy, nobody else can explain it for you. Our guide to <a href="/blog/outsourced-sdr-vs-in-house-sdr">outsourced vs in-house SDRs</a> covers when each model makes sense.</p>'
        )),
        ('volume', 'Failure 3: volume replaced relevance', (
            '<p>The third failure is a volume habit. When a program is measured on emails sent and meetings booked, the easiest way to hit the number is to send more, and sending more to weakly researched lists lowers reply rates, annoys buyers and damages the domains you send from. More activity becomes the problem, not the solution.</p>'
            '<p>Buyers notice. In a ' + a(GARTNER, 'Gartner survey of 632 B2B buyers') + ', 73% said they actively avoid suppliers who send irrelevant outreach. That means a careless campaign does not just fail to book meetings this quarter; it can make the exact companies you want as customers less likely to talk to you later.</p>'
            '<p>Inbox providers notice too. Google\'s ' + a(GOOGLE, 'email sender guidelines') + ' ask senders to authenticate their mail and to keep the user-reported spam rate below 0.1%, never reaching 0.3%. A program that pushes volume to cold lists can cross those lines quickly, and once a sending domain is flagged, even your good emails stop arriving. The FTC\'s ' + a(FTC, 'CAN-SPAM guide') + ' adds that you cannot contract away your legal responsibility for email sent on your behalf, so the risk stays with you even when someone else presses send.</p>'
            '<p><b>How to spot it in month one:</b> look at what the weekly report leads with. If the first numbers are emails sent, open rates and dials, the program is being run on volume. Ask instead for reply rates by segment, the text of real replies, bounce rates and spam complaints. A healthy program can tell you which segment replied best and why. An unhealthy one can tell you how many emails it sent.</p>'
            '<p>For most B2B companies selling to a defined set of accounts, fewer, better researched messages beat more messages. Many teams learned the same lesson from <a href="/blog/are-ai-sdrs-worth-it">fully autonomous AI SDR tools</a>.</p>'
        )),
        ('visibility', 'Failure 4: you could not see the work', (
            '<p>The fourth failure is a black box. If you only receive a monthly number, you cannot tell whether a slow month is bad targeting, weak messaging, a deliverability problem or simply timing, and you lose the most valuable thing outbound produces: what buyers actually said. Programs without visibility tend to fail late and expensively, because nobody sees the problem until the quarter is over.</p>'
            '<p>Visibility also covers people. Sales development has high turnover everywhere. The Bridge Group\'s ' + a(BRIDGE25, '2025 report') + ' found median annual SDR attrition of 40% in 2024, counting departures and promotions. When the rep on your account changes, everything they learned about your buyer leaves with them unless it was written down. Agencies are not immune to this; they often feel it more, because their reps move between clients as well as between jobs.</p>'
            '<p><b>How to spot it in month one:</b> ask for access, not reports. You should be able to open a shared inbox, a dashboard or your own CRM and read every email sent and every reply received. Ask who exactly works on your account, how many other clients they handle, and what happens when one of them leaves. If the answer to "can I read the replies?" is a summary deck, you have found the fourth warning sign.</p>'
        )),
        ('month-one', 'The month one checklist: what to look for, week by week', (
            '<p>You can check for all four failures in the first four weeks. By the end of month one, a healthy program has a written meeting definition, a sequence you approved, real replies you have read and a first review of what buyers said. If any of those is missing, raise it before month two, not at the end of the quarter.</p>'
            + fig2 +
            '<p><b>Week one: definitions.</b> The meeting definition and the ideal customer profile are written down and signed off. The agency has asked for your call recordings, win and loss notes and objection list. Sending domains are set up with authentication and are warming.</p>'
            '<p><b>Week two: first drafts.</b> You have seen and approved the first sequence, including follow ups. You know which accounts it goes to first, and you have looked at a sample of the list to check that the companies and titles match the definition.</p>'
            '<p><b>Week three: first replies.</b> You can read real replies, positive and negative, in a place you control. You may not have many meetings yet, and that is fine. What matters is that the replies come from the right people and say something you can learn from.</p>'
            '<p><b>Week four: first review.</b> A working session, not a report. Which segments replied, which objections repeated, which meetings fit the definition and which did not, and what changes for month two.</p>'
            + fig3
        )),
        ('fix-or-stop', 'How to fix a failing program, or decide to stop', (
            '<p>Most struggling programs can be fixed if the problem is caught in the first month: write the meeting definition, cut volume, approve the messaging and start reading replies every week. If the agency will not agree to those four changes, the program is unlikely to improve, and it is usually better to stop and keep what you have learned.</p>'
            '<p>Change one thing at a time so you can see what worked: start with the definition, then narrow to the segment where replies were best, then rewrite the sequence from the real objections. Judge each change on meeting quality, not on the number of meetings.</p>'
            '<p>When you decide to stop, make sure you leave with your assets: the account lists, the messaging that worked, the full reply history, meeting notes and the sending domains. That is a contract point to settle before you start, which is why it is on our list of questions.</p>'
            '<p>Since we are asking you to hold providers to this standard, here is how we built the Agent Base around the four failures:</p>'
            '<ul><li><b>The meeting:</b> you approve the target profile and the meeting definition before launch.</li>'
            '<li><b>The buyer:</b> <b>Scout</b> finds accounts that match your profile and show a reason to buy now, and <b>Lens</b> researches each one before anything is written.</li>'
            '<li><b>Relevance over volume:</b> <b>Quill</b> drafts each email from that research, and your dedicated Agent Base manager edits or approves every draft. <b>Relay</b> sends at a safe pace. Nothing goes out on autopilot.</li>'
            '<li><b>Visibility:</b> <b>Echo</b> sorts replies, <b>Atlas</b> writes a brief for every booked meeting, and you see accounts, drafts, sends, replies and meetings on a live dashboard.</li></ul>'
            '<p>Where we are not the right fit: if your sale depends on live phone calls from day one, or you already have a strong SDR manager and a working playbook, an in-house team may serve you better. Our <a href="/talent">talent team</a> can help you hire bilingual SDRs from Latin America instead.</p>'
        )),
    ],
    'conclusion': (
        '<p>Outsourced SDR programs fail more often than they succeed, but rarely for mysterious reasons. The same four patterns explain most of it, and each one shows itself in the first month.</p>'
        '<ol><li><b>Define the meeting in writing</b> before launch, including no-shows and poor fits.</li>'
        '<li><b>Make sure the team learns your buyer</b> from your calls, wins, losses and objections, and approve the first sequence.</li>'
        '<li><b>Choose relevance over volume</b>, and watch reply rates, bounces and spam complaints, not sends.</li>'
        '<li><b>Insist on seeing the work</b>: every email, every reply and the names of the people on your account.</li>'
        '<li><b>Run the month one checklist</b> and raise problems before month two, while they are still cheap to fix.</li></ol>'
        '<p>If you want to see how the Agent Base handles each of these on your market, <a href="' + CAL + '"' + EXT + '>book a call</a> and bring the checklist.</p>'
    ),
    'faq': [
        ('Why do outsourced SDR programs fail?',
         'Mostly for four reasons: no written definition of a qualified meeting, a team that never learned the buyer, a focus on volume over relevance, and no visibility into the actual emails and replies. In a SaaStr poll of more than 1,200 people, only 7% said outsourced SDRs really worked for them.'),
        ('How soon can I tell if an outsourced SDR program is failing?',
         'Usually within the first month. By week four you should have a written meeting definition, a sequence you approved, real replies you can read and a first review of what buyers said. If any of those is missing, raise it before month two.'),
        ('Do outsourced SDRs ever work?',
         'Yes, under conditions. Jason Lemkin of SaaStr says he only had success when he had already done the work well in house and treated the outside team as part of the core team. Clear definitions, approved messaging and weekly reply reviews make success much more likely.'),
        ('What should an outsourced SDR agency report every week?',
         'Replies with the actual text, objections that repeat, meetings booked against the written definition, results by segment, and deliverability health such as bounces and spam complaints. Activity counts alone are not enough.'),
        ('Can a bad outbound program hurt my brand?',
         'It can. A Gartner survey found 73% of B2B buyers actively avoid suppliers who send irrelevant outreach, and aggressive sending can damage your domains with inbox providers. The emails go out in your name, so the reputation risk stays with you.'),
        ('Should I fix a failing SDR program or start over?',
         'Try to fix it first if the agency agrees to a written meeting definition, lower volume, approved messaging and weekly reply reviews. If it will not, stop, and make sure you keep your lists, messaging, reply history and domains.'),
        ('How does the Agent Base avoid these failures?',
         'You approve the meeting definition and target profile before launch, AI agents research every account before drafting, a dedicated Agent Base manager approves every email, and you can see all accounts, sends, replies and meetings on a live dashboard.'),
    ],
}
