# Spec for blog/cold-calling-b2b-2026.html. Build: python3 tools/blogkit.py tools/posts/cold-calling-b2b-2026.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GONG = 'https://www.gong.io/blog/the-hidden-power-of-cold-calling-insights-from-300m-calls'
GONG_OPENERS = 'https://www.gong.io/resources/labs/the-best-and-worst-cold-call-openers-backed-by-data-from-300m-calls/'
COGNISM = 'https://cognism.com/reports/cold-calling-report-2026'
RAIN = 'https://www.rainsalestraining.com/blog/114-essential-sales-statistics-to-improve-performance'
GARTNER = 'https://www.businesswire.com/news/home/20260520585188/en/Gartner-Survey-Finds-69-of-B2B-Buyers-Turn-to-Sales-Reps-to-Validate-AI-Generated-Insights'
FCC = 'https://wsgr.com/en/insights/fcc-rules-ai-generated-voices-are-artificial-under-the-tcpa.html'
TSR = 'https://hunton.com/insights/legal/telemarketing-sales-rule-changes-remove-exception-for-business-to-business-calls-and-impose-new-recordkeeping-requirements'

fig1 = figure(1, bar_chart('Average vs top-quartile cold callers', [
    ('Connects, average rep', 5.4),
    ('Connects, top quartile', 13.3),
    ('Meetings, average rep', 4.6),
    ('Meetings, top quartile', 16.7),
], unit='%', vmax=20, highlight=('Connects, top quartile', 'Meetings, top quartile')),
    'Connects are the share of dials that reach a prospect; meetings are the share of conversations that end in a booked meeting. The gap between an average and a top cold caller is about two and a half times on connects and more than three times on meetings booked per conversation. Source: '
    + a(GONG, 'Gong Labs, analysis of more than 300 million cold calls') + '.')

fig2 = figure(3, bar_chart('Meeting rate by cold call opener', [
    ('"Heard the name around?"', 11.24),
    ('Permission-based opener', 11.18),
    ('"How\'s your day going?"', 7.6),
    ('"Did I catch you at a bad time?"', 2.15),
], unit='%', vmax=14, highlight=('"Heard the name around?"',)),
    'How often calls that started with each opener (the first one is short for "Have you heard the name tossed around?") ended in a booked meeting. Openers that sound like a script or invite a quick "yes, bad time" do worst. Source: '
    + a(GONG_OPENERS, 'Gong Labs') + '.')

fig3 = figure(2, table(['', 'Cold call', 'Cold email', 'LinkedIn'], [
    ['<b>Best for</b>', 'Fast, two-way conversations and qualifying in real time', 'Reaching many people with a specific, researched reason', 'Warming up a contact and staying visible'],
    ['<b>Main limit</b>', 'Hard to reach people; depends on the caller\'s skill', 'Spam filters and crowded inboxes', 'Slow, and many buyers rarely check messages'],
    ['<b>What it needs</b>', 'Good phone data, a clear reason and a trained rep', 'Clean data, a healthy domain and a review step', 'An active profile and patience'],
    ['<b>Works best with</b>', 'An email that follows the call', 'A call that comes before or after it', 'Email and phone in the same sequence'],
]), 'Cold calling, cold email and LinkedIn do different jobs in a B2B sequence. Most teams that book consistently use all three, and let the buyer\'s response decide which one leads.')

POST = {
    'slug': 'cold-calling-b2b-2026',
    'title': 'Cold calling in 2026: does it still work for B2B?',
    'h1': 'Cold calling in 2026: does it still <em>work</em> for B2B?',
    'description': 'Whether cold calling still works for B2B in 2026, what the latest data from Gong and Cognism shows, why it works with email instead of against it, what changed in the rules, and what to look for in a rep who can do it well.',
    'category': 'Hiring',
    'date': '2026-11-19',
    'date_label': 'November 19, 2026',
    'hero_img': 'cover-cold-calling-b2b-2026',
    'card_img': 'cover-cold-calling-b2b-2026',
    'card_title': 'Cold calling in 2026: does it still work for B2B?',
    'card_text': 'Yes, for teams with good data and good callers. The gap between an average rep and a great one is the real story.',
    'takeaways': [
        'Cold calling still works for B2B in 2026, but the results depend heavily on the caller. Top-quartile reps connect about two and a half times as often as average reps and book more than three times as many meetings per conversation.',
        'Calling makes email work better. In Gong\'s data, email reply rates nearly doubled when a call came first, even when nobody picked up.',
        'Cold calling means a person dialing another person for a specific reason. It is not a robocall, and AI-generated voices now fall under federal robocall rules.',
        'The rep matters more than the script. Hire for clear spoken English, resilience, curiosity and the ability to say why they are calling in one sentence.',
    ],
    'intro': (
        '<p>Cold calling means phoning a potential buyer who has not asked to hear from you, with a reason to talk. Every year someone declares it dead, and every year the data says otherwise. Buyers screen unknown numbers, prefer to research on their own and use AI to compare vendors. Yet the phone is still one of the few channels where a seller can have a real conversation with a stranger in under a minute.</p>'
        '<p>This guide answers the question directly: does cold calling still work for B2B in 2026, and for whom? It covers what the latest numbers show, how calling and email support each other, what changed in the rules, how a good cold call is built, and what to look for when you hire someone to make the calls. We place bilingual sales professionals from Latin America with US companies, many of them in cold calling roles, so the last part is where we spend most of our time.</p>'
    ),
    'cta': {
        'inline_lead': 'Need someone who can cold call well?',
        'inline_text': 'Tell us your market and the US hours you need covered. We send three bilingual reps from Latin America, interviewed in English and roleplayed on a live cold call, within 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Cold callers who sound like they <em>belong</em> on the call.',
        'band_text': 'Vetted bilingual sales professionals from Latin America, interviewed in English and roleplayed on a cold call before you meet them. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('short-answer', 'The short answer: yes, if the caller is good', (
            '<p>Cold calling still works for B2B in 2026, but it works very unevenly. Teams with accurate phone data, a clear reason to call and well-trained reps book meetings every week; teams that treat it as a numbers game with a script mostly reach voicemail and annoy the people they do reach.</p>'
            '<p>The best evidence comes from very large call datasets. ' + a(GONG, 'Gong Labs analyzed more than 300 million cold calls') + ' and found that the average rep connects with a prospect on 5.4% of dials and books a meeting in 4.6% of those conversations. Top-quartile reps connect on 13.3% of dials and book a meeting in 16.7% of conversations.</p>'
            + fig1 +
            '<p>Gong translated that into a simple comparison: at about 200 dials a week, an average rep books roughly two meetings a month while a top rep books around eighteen. Same channel, same buyers, very different outcomes.</p>'
            '<p>' + a(COGNISM, 'Cognism\'s 2026 cold calling report') + ', based on more than 200,000 calls, points the same way. It puts the average cold call success rate at 2.7%, and reports that it took an average of 1.55 calls to reach a prospect, down from 2.9 the year before. Its data also shows calls getting shorter and buyers getting more selective, with fewer flat rejections and more "not now" and "we already have something".</p>'
            '<p>So the honest answer to "does cold calling still work?" is "it works for people who are good at it." That makes it as much a hiring question as a channel question.</p>'
        )),
        ('why-it-works', 'Why the phone still works when buyers prefer self-service', (
            '<p>The phone still works because buyers who research on their own still want a person to confirm what they found. A short, relevant call can do in two minutes what a sequence of five emails often cannot: start a real conversation and find out if there is a fit.</p>'
            '<p>The trend toward self-service is real. A ' + a(GARTNER, 'Gartner survey of 645 B2B buyers') + ' published in May 2026 found that 67% prefer a buying experience without a sales rep. But the same survey found that 69% prefer to validate AI-generated insights with a sales rep. Buyers want to do the research themselves and then talk to someone who can tell them what is true.</p>'
            '<p>Buyers also say yes to outreach more often than sellers think. ' + a(RAIN, 'RAIN Group\'s research') + ' found that 82% of buyers accept meetings with sellers who reach out to them, and that it takes an average of eight touches to generate a meeting. The phone is rarely the only touch, but it is often the one that turns interest into a calendar invite.</p>'
            '<p>There are three things a call does that email cannot:</p>'
            '<ul><li><b>It is two-way.</b> The buyer can ask a question, push back or say "call me next quarter", and the rep can respond right away.</li>'
            '<li><b>It carries tone.</b> Confidence, warmth and clarity come through in a voice in a way that is hard to fake in text.</li>'
            '<li><b>It qualifies fast.</b> In two minutes a good rep can learn whether the timing, the problem and the person are right. That saves the account executive from meetings that were never going anywhere.</li></ul>'
            '<p>None of this works without a good reason to call. A call that opens with a specific, researched reason sounds like a person with something useful to say. A call that opens with a pitch sounds like every other interruption in the buyer\'s day.</p>'
        )),
        ('calls-and-email', 'Cold calling and email work better together', (
            '<p>Cold calling and cold email work better as a pair than either one alone. In Gong\'s data, a call before an email nearly doubled the email reply rate, even when the prospect did not pick up.</p>'
            '<p>The ' + a(GONG, 'same Gong analysis') + ' found an email reply rate of 1.81% without a call and 3.44% when a call came first. A missed call with a short voicemail still puts a name and a voice in the buyer\'s head, so the email that follows is no longer from a stranger.</p>'
            + fig3 +
            '<p>In practice, most teams that book meetings consistently build sequences like this:</p>'
            '<ul><li><b>Day one:</b> a call with a specific reason, a short voicemail if nobody answers, and an email the same day that repeats the reason in writing.</li>'
            '<li><b>The next week:</b> a second call at a different time, a LinkedIn connection or comment, and a short follow-up email.</li>'
            '<li><b>After that:</b> a few more spaced touches, letting the buyer\'s behavior (opens, replies, a pickup) decide which channel leads.</li></ul>'
            '<p>This is also why "phone vs email" is the wrong debate. The useful question is which channel this buyer actually answers. Some buyers pick up the phone readily; others live in email. A good rep learns quickly which is which in their market and adjusts.</p>'
        )),
        ('rules', 'What changed in the rules for cold calling', (
            '<p>The main changes are about automated and AI-generated calls, not about a person dialing a business contact. A human rep calling a business with a relevant reason is still a normal, legal part of B2B sales in the US, but AI voice calls and misleading claims now face clearer federal rules.</p>'
            '<p>Two changes are worth knowing:</p>'
            '<ul><li><b>AI voices count as artificial voices.</b> In February 2024 the FCC issued a ' + a(FCC, 'declaratory ruling') + ' that AI-generated voices, including voice cloning, fall under the TCPA\'s rules for "artificial or prerecorded voice" calls. In general that means calls using an AI voice need the recipient\'s prior express consent. An "AI cold caller" that dials strangers is not a legal shortcut.</li>'
            '<li><b>B2B calls can no longer mislead.</b> The FTC\'s 2024 update to the Telemarketing Sales Rule ' + a(TSR, 'extended its rules against misrepresentation to business-to-business calls') + ' and added new recordkeeping requirements for telemarketers. In plain terms: what your rep says on the call has to be true.</li></ul>'
            '<p>Other rules still apply depending on who you call and where, including state laws and rules for calling mobile numbers. This is not legal advice, and if calling is a big part of your plan it is worth a short review with counsel. For most B2B teams the practical rules are simple: a real person makes the call, the reason is genuine, the claims are true, and anyone who asks not to be called again is removed right away.</p>'
            '<p>These rules are one reason the human cold caller is not going away. AI can help a rep research the account and prepare the call, but the call itself is still best made by a person.</p>'
        )),
        ('good-call', 'What a good B2B cold call sounds like in 2026', (
            '<p>A good cold call in 2026 is short, honest about being a cold call, and built around one specific reason the buyer should care right now. It aims to earn a next step, not to close anything.</p>'
            '<p>The opener matters more than most reps think. Gong\'s analysis of ' + a(GONG_OPENERS, 'cold call openers') + ' found that openers that sound natural and give the buyer some control do much better than ones that invite a quick exit. "Did I catch you at a bad time?" led to a meeting in only 2.15% of calls, while a permission-based opener reached 11.18%.</p>'
            + fig2 +
            '<p>A simple structure works for most B2B calls:</p>'
            '<ol><li><b>Open honestly.</b> Say who you are and that this is a cold call. Ask for a few seconds to explain why you called.</li>'
            '<li><b>Give one reason.</b> Name something specific: a new role, a hiring push, a problem common in their industry. One sentence.</li>'
            '<li><b>Ask one question.</b> Check whether the problem is real for them. Then listen.</li>'
            '<li><b>Handle the first objection calmly.</b> "Not interested" often means "not sure why you are calling". Clarify once, without arguing.</li>'
            '<li><b>Ask for a small next step.</b> A short meeting, or permission to send one useful thing by email.</li></ol>'
            '<p>Timing helps too. Cognism\'s 2026 data found Thursday was the strongest day, with the longest conversations between 10 and 11 in the morning and solid results between 2 and 3 in the afternoon. That is one reason reps who work full US business hours have an advantage over teams that only overlap for part of the day.</p>'
        )),
        ('hiring', 'What to look for when you hire a cold caller', (
            '<p>Hire a cold caller for clear spoken English, resilience, curiosity and the ability to explain a reason for calling in one sentence. Product knowledge can be taught in a few weeks; the ability to stay calm and natural on the twentieth hard "no" of the day is much harder to train.</p>'
            '<p>Since the gap between average and top-quartile reps is so large, the hire is the biggest lever you have. These are the traits we test for:</p>'
            '<ul><li><b>Clear, natural spoken English.</b> Not a perfect accent, but easy to understand at normal speed on a phone line, with the confidence to keep a conversation moving.</li>'
            '<li><b>Composure under rejection.</b> Good callers hear "no" as information, not as a verdict. They stay polite, ask one clarifying question and move on.</li>'
            '<li><b>Listening.</b> The best reps talk less than they think they will. They ask one good question and follow the answer.</li>'
            '<li><b>Preparation.</b> They research before they dial and can say why this person, at this company, now.</li>'
            '<li><b>Activity with judgment.</b> Cold calling still needs volume, but good reps know when to switch channel, when to stop calling an account and when to escalate a hot lead.</li></ul>'
            '<p>The only reliable way to test these is a live roleplay. A CV that says "cold calling experience" tells you little; ten minutes on a mock call with a realistic, slightly difficult buyer tells you a lot. Our <a href="/blog/sdr-interview-process">20-minute SDR screen</a> shows how we structure it, and our <a href="/blog/sdr-onboarding-plan">30, 60 and 90 day onboarding plan</a> covers how to get a new caller to full pace.</p>'
            '<p>Every candidate we place is interviewed in English by our sales team and put through a live cold call roleplay before they enter our pool, and you interview them yourself before deciding.</p>'
        )),
        ('latam', 'Building a cold calling team from Latin America', (
            '<p>Latin America is a strong place to hire B2B cold callers for US companies because of time zone overlap and a deep pool of bilingual reps with US sales experience. Reps in countries like Colombia, Mexico and Argentina can work full US business hours, which matters for a channel where timing affects who picks up.</p>'
            '<p>A few points make the difference between a LatAm calling team that works and one that does not:</p>'
            '<ul><li><b>Test the call, not the CV.</b> Spoken English on a phone line, with background noise and interruptions, is different from a video interview. Run the roleplay on the phone.</li>'
            '<li><b>Cover the right hours.</b> Match the rep\'s schedule to your buyers\' best calling windows in their time zone, not just to your office hours.</li>'
            '<li><b>Give them context.</b> A rep calling US buyers needs to understand the industry vocabulary and the common objections. Recorded calls from your best rep are the fastest teacher.</li>'
            '<li><b>Use their second language.</b> Bilingual reps can also cover Spanish-speaking buyers in the US and Latin America, which opens segments many teams ignore.</li></ul>'
            '<p>We cover the hiring process in more detail in <a href="/blog/hire-bilingual-cold-callers-latin-america">where to hire bilingual LatAm cold callers</a> and the country differences in <a href="/blog/hire-sales-reps-colombia-argentina-mexico">hiring in Colombia, Argentina or Mexico</a>.</p>'
        )),
    ],
    'conclusion': (
        '<p>Cold calling is not dead in 2026. It is less forgiving. Buyers screen more, research more on their own and decide faster whether a call is worth their time, which rewards good callers and punishes everyone else.</p>'
        '<ol><li><b>It still works:</b> the data from hundreds of millions of calls shows steady meetings for skilled reps.</li>'
        '<li><b>The rep is the variable:</b> top-quartile callers book more than three times as many meetings per conversation.</li>'
        '<li><b>Pair it with email:</b> a call before an email nearly doubles reply rates, even without a pickup.</li>'
        '<li><b>Keep it human and honest:</b> AI voices fall under robocall rules, and B2B calls can no longer mislead.</li>'
        '<li><b>Build the call around one reason:</b> an honest opener, one specific reason, one question and a small next step.</li>'
        '<li><b>Hire with a live roleplay:</b> clear English, composure, listening and preparation matter more than any script.</li></ol>'
        '<p>If you want a cold caller who already passed a live roleplay in English, <a href="/talent">request profiles</a> and we will send three within 72 hours.</p>'
    ),
    'faq': [
        ('Does cold calling still work for B2B in 2026?',
         'Yes, for teams with accurate phone data, a clear reason to call and skilled reps. Gong\'s analysis of more than 300 million calls shows top-quartile reps connecting on 13.3% of dials and booking a meeting in 16.7% of conversations.'),
        ('What is a good cold call success rate?',
         'It depends on how you measure it and on your market. Cognism\'s 2026 report puts the average success rate at 2.7%, while Gong\'s data shows average reps booking a meeting in 4.6% of conversations and top reps in 16.7%. Track your own trend over time rather than chasing a single benchmark.'),
        ('Is cold calling better than cold email?',
         'Neither is better on its own; they do different jobs. Gong found email reply rates nearly doubled when a call came first, so most teams that book consistently use both, plus LinkedIn.'),
        ('Is B2B cold calling legal in the US?',
         'A person calling a business contact with a genuine reason is a normal part of B2B sales. Calls using AI-generated voices generally need prior consent under an FCC ruling from 2024, and B2B telemarketing cannot use misleading claims under the FTC\'s updated Telemarketing Sales Rule. Check state rules and talk to counsel if calling is central to your plan.'),
        ('Can AI make cold calls instead of a rep?',
         'AI can research accounts, prepare call notes and summarize calls. Calls that use an AI-generated voice fall under federal rules for artificial voices, which generally require the recipient\'s prior consent, so live cold calls are still best made by a person.'),
        ('What is the best time to cold call B2B buyers?',
         'Cognism\'s 2026 data found Thursday the strongest day, with the best conversations between 10 and 11 in the morning and good results between 2 and 3 in the afternoon. Test your own market, since industries differ.'),
        ('What should I look for when hiring a cold caller?',
         'Clear, natural spoken English, composure under rejection, good listening, preparation before each call and judgment about when to switch channel. Test them with a live cold call roleplay rather than relying on the CV.'),
    ],
}
