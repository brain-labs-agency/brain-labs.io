# Spec for blog/hire-remote-sdr.html. Build: python3 tools/blogkit.py tools/posts/hire-remote-sdr.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


GALLUP_HYBRID = 'https://www.gallup.com/401384/indicator-hybrid-work.aspx'
GALLUP_ONBOARD = 'https://www.gallup.com/workplace/353096/practical-tips-leaders-better-onboarding-process.aspx'
MS_ONBOARD = 'https://www.microsoft.com/en-us/worklab/strategies-for-onboarding-in-a-hybrid-world'
HBR_BUDDY = 'https://hbr.org/2019/06/every-new-employee-needs-an-onboarding-buddy'
MS_PARANOIA = 'https://www.weforum.org/stories/2022/10/work-productivity-hybrid-remote-microsoft/'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'

fig1 = figure(1, table(['Part of the process', 'Office habit', 'What to change for a remote SDR'], [
    ['<b>Job description</b>', 'Location and a list of duties', 'Core hours in your time zone, the tools, and the weekly output you expect'],
    ['<b>Screening</b>', 'CV review and a chat about experience', 'A short written task and a live roleplay call, because writing and calls are the job'],
    ['<b>Interview</b>', 'In person, judged on presence', 'On video and on the phone, judged on how they sound to a buyer'],
    ['<b>Setup check</b>', 'Not needed, the office provides it', 'Quiet space, reliable internet, a good headset and a backup plan'],
    ['<b>Onboarding</b>', 'Learn by sitting next to the team', 'A written plan, recorded calls to study, a buddy and daily check ins'],
    ['<b>Management</b>', 'Walk the floor', 'Agreed activity and outcome numbers, call reviews and a weekly one to one'],
]), 'Where a remote SDR hire differs from an office hire. Most of the changes move evidence from impressions to work you can see.')

fig2 = figure(2, bar_chart('New hires who said their onboarding buddy helped them get productive quickly', [
    ('Met buddy once', 56),
    ('Met 2 to 3 times', 73),
    ('Met 4 to 8 times', 86),
    ('Met more than 8 times', 97),
], unit='%', vmax=110, highlight=('Met more than 8 times',)),
    'Microsoft research on new hires in their first 90 days, as reported in ' + a(MS_ONBOARD, 'Microsoft WorkLab') + ' and ' + a(HBR_BUDDY, 'Harvard Business Review') + '. The more often a new hire met their buddy, the more likely they were to say it helped.')

fig3 = figure(3, timeline('A remote SDR\'s first four weeks', [
    (0, 1, 'Learn', 'product, ICP, calls'),
    (1, 2, 'Shadow', 'live calls, review'),
    (2, 3, 'Supervised', 'own small list'),
    (3, 4, 'Own a segment', 'daily targets'),
], 4, unit='wk', accent=('Supervised',)),
    'A practical shape for the first month. The supervised week is the one remote teams most often skip, and it is where a manager catches habits before they reach hundreds of buyers.')

POST = {
    'slug': 'hire-remote-sdr',
    'title': 'Hiring a remote SDR: what to change in your process',
    'h1': 'Hiring a remote SDR: what to <em>change</em> in your process',
    'description': 'How to hire a remote SDR: what to put in the job description, how to screen with a written task and a live roleplay, how to check the setup, and how to onboard and manage a rep you do not see every day.',
    'category': 'Hiring',
    'date': '2026-11-23',
    'date_label': 'November 23, 2026',
    'hero_img': 'cover-hire-remote-sdr',
    'card_img': 'cover-hire-remote-sdr',
    'card_title': 'Hiring a remote SDR: what to change in your process',
    'card_text': 'The job description, screen, setup check, onboarding and management habits that make a remote SDR work.',
    'takeaways': [
        'Hiring a remote SDR works when you judge candidates on the work itself, writing and live calls, instead of on how they come across in an office interview.',
        'Put core hours in your time zone, the tools and the weekly output you expect in the job description. Those three lines filter out most bad fits.',
        'Check the setup as part of the hire: a quiet space, reliable internet and a good headset matter as much as experience for a rep who lives on calls.',
        'Remote onboarding needs more structure, not less: a written plan, recorded calls, a buddy and a supervised week before the rep owns a segment.',
    ],
    'intro': (
        '<p>Most US companies now hire SDRs who will never sit in their office. Sales development is a phone, email and LinkedIn job, so it moves to remote work easily. What does not move easily is the hiring process. Many teams still hire a remote rep the way they would hire someone for the desk next to them, then wonder why the hire looked great on video and struggled on the phones.</p>'
        '<p>This guide covers what to change at each step, from the job description to the first month of management, so that the evidence you hire on is the same work the rep will do every day. It is written for founders and sales leaders hiring their first or next remote SDR, whether in the US or from Latin America.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring a remote SDR who works your hours?',
        'inline_text': 'Tell us your market and the US time zone you need covered. We send three bilingual sales professionals from Latin America, each interviewed in English and put through a live cold call roleplay, within 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Remote SDRs who sound right on a <em>US call</em>.',
        'band_text': 'Vetted bilingual sales professionals from Latin America, working your US business hours. Every candidate is interviewed in English and roleplayed on a live call before you meet them. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('what-changes', 'What actually changes when the SDR is remote', (
            '<p>When the SDR is remote, you lose the informal signals an office gives you, so the process has to test the work directly. You cannot overhear their calls, see their energy or notice when they are stuck, which means you need to see writing, calls and results instead.</p>'
            '<p>Remote is now the normal setup for this kind of role. As of August 2026, ' + a(GALLUP_HYBRID, 'Gallup reports') + ' that among US employees whose jobs can be done remotely, 54% work hybrid, 25% work fully remote and only 21% work fully on site. SDR work sits firmly in that remote-capable group: a headset, a CRM, a dialer and an inbox are the whole office.</p>'
            '<p>What changes is not the job. An SDR still researches accounts, starts conversations and books qualified meetings. What changes is how you find out whether someone can do it, and how you help them get good at it. Three things move:</p>'
            '<ul><li><b>Evidence.</b> In an office, managers learn a lot from being in the room. Remotely, you only know what you test, record or measure.</li>'
            '<li><b>Communication.</b> More of the job runs in writing: messages to the team, notes in the CRM, handoffs to account executives. Written clarity becomes a core skill, not a bonus.</li>'
            '<li><b>Structure.</b> A remote rep cannot learn by osmosis. Whatever an office teaches without trying, a remote process has to teach on purpose.</li></ul>'
            '<p>The rest of this guide walks through each step of the hire with those three shifts in mind.</p>'
        )),
        ('job-description', 'Write the job description for a remote rep', (
            '<p>A remote SDR job description should state the core hours in your time zone, the tools the rep will use and the weekly output you expect. Those three lines do more filtering than any list of soft skills.</p>'
            + fig1 +
            '<p><b>Core hours.</b> Your buyers decide when calls can happen, so name the hours that matter, for example "available 9 to 5 Eastern". A candidate in a far time zone who agrees to work nights may burn out within months. Reps in the Americas avoid that problem: most of Latin America sits within a few hours of US time zones, which is one reason US teams hire there. We compare the countries in <a href="/blog/hire-sales-reps-colombia-argentina-mexico">hiring sales reps in Colombia, Argentina or Mexico</a>.</p>'
            '<p><b>Tools.</b> List the CRM, dialer, sequencing tool and communication apps. Experience with your exact stack is not essential, but comfort learning new software on their own is, because nobody will be at the next desk to show them.</p>'
            '<p><b>Output.</b> Describe what a good week looks like in plain terms: the number of accounts researched, conversations started and qualified meetings booked once the rep is fully ramped. This tells strong candidates you manage by results, and it gives you a fair standard later. For how those numbers should build during the first months, see our <a href="/blog/sdr-onboarding-plan">SDR onboarding plan</a>.</p>'
            '<p>Finally, say what kind of remote it is: fully remote, remote with occasional travel, or remote within certain regions. Vague wording here attracts candidates who will turn down the offer late in the process.</p>'
        )),
        ('screening', 'Screen on the work: a written task and a live call', (
            '<p>Screen a remote SDR with a short written task and a live roleplay call, because writing and calling are the job. A CV tells you where someone has worked, while a roleplay tells you how they will sound to your buyers next month.</p>'
            '<p>The written task should take no more than 20 to 30 minutes. Give the candidate a real company in your market and ask for a short first email and one follow up. You are looking for three things: did they find a real reason to write, is the message short and clear, and does it sound like a person. The task also shows whether they meet a deadline without a reminder, which is a useful remote signal on its own.</p>'
            '<p>The live call matters even more. Play a busy buyer and give the candidate a few minutes to open, handle one or two objections and ask for a meeting. Pay attention to:</p>'
            '<ul><li><b>The first ten seconds.</b> Do they get to the reason for the call quickly, or read a script?</li>'
            '<li><b>Listening.</b> Do they respond to what you actually said?</li>'
            '<li><b>Recovery.</b> When you push back, do they stay calm and curious?</li>'
            '<li><b>The ask.</b> Do they ask for a specific next step?</li></ul>'
            '<p>Run the call on the phone or with video off for part of it. A remote rep will spend most of the day on audio only, and some candidates who shine on camera sound flat without it. Our <a href="/blog/sdr-interview-process">20 minute SDR interview</a> lays out a full screen you can reuse, including the roleplay and how to score it.</p>'
            '<p>If the rep will speak with US buyers in English as a second language, test that on the same call rather than relying on a certificate. Listen for whether a buyer would stay on the line, not for a perfect accent.</p>'
        )),
        ('setup', 'Check the setup, not only the person', (
            '<p>Check the candidate\'s working setup before you make an offer: a quiet space, reliable internet, a good headset and a backup plan for outages. For a rep who lives on calls, a noisy room or a dropped connection costs meetings every day.</p>'
            '<p>This step feels awkward to many hiring managers, but candidates who have worked remotely before expect it. Keep it simple and respectful:</p>'
            '<ul><li><b>Space.</b> Ask where they will work and whether it is quiet during your core hours. Background noise on a call is one of the fastest ways to lose a buyer\'s attention.</li>'
            '<li><b>Connection.</b> Ask what happens when their internet drops. A mobile hotspot or a nearby coworking space is a reasonable answer. "It never drops" is not.</li>'
            '<li><b>Equipment.</b> A noise-cancelling headset and a reliable computer are the minimum. Decide in advance whether you supply them or the rep does, and say so in the offer.</li>'
            '<li><b>Hours.</b> Confirm they can be available for your full core hours, including the early or late slots when your buyers are most reachable.</li></ul>'
            '<p>The live roleplay from the previous step doubles as a setup check. You will hear the audio quality, the background and how the connection holds up for ten minutes. Microsoft, which onboarded thousands of remote employees during the pandemic, made a point of ' + a(MS_ONBOARD, 'sending new remote hires their hardware well before day one') + '. The same principle applies at any size: a rep should start their first morning ready to learn, not waiting for tools.</p>'
        )),
        ('onboarding', 'Onboard with more structure, not less', (
            '<p>Remote onboarding needs a written plan, an active manager and a buddy, because a remote rep cannot pick up the job by sitting near the team. The first month decides whether a good hire ramps or drifts.</p>'
            '<p>The bar is low. ' + a(GALLUP_ONBOARD, 'Gallup found') + ' that only 12% of US employees say their company does a good job of onboarding, and only 29% of new hires feel fully prepared and supported after it. Remote hires feel any gap sooner, because there is no hallway to fill it.</p>'
            '<p>Two things make the biggest difference:</p>'
            '<ul><li><b>An active manager.</b> In Microsoft\'s research across more than 150,000 employees, new hires whose managers played an active role in onboarding were ' + a(MS_ONBOARD, '3.5 times more likely to be satisfied with it') + '. For an SDR, that means daily check ins in the first weeks and a manager who listens to calls.</li>'
            '<li><b>A buddy.</b> A peer the rep can message with small questions, without feeling they are bothering the manager. The effect grows with contact.</li></ul>'
            + fig2 +
            '<p>Build the first weeks around real work. Give the rep recorded calls and real emails to study, have them shadow live calls, then let them work a small list with review before they own a segment. The supervised week is the one remote teams skip most often, and it is where a manager catches habits before they reach hundreds of buyers.</p>'
            + fig3 +
            '<p>Our <a href="/blog/sdr-onboarding-plan">30, 60 and 90 day SDR onboarding plan</a> goes deeper on what to cover in each phase.</p>'
        )),
        ('managing', 'Manage by output and call reviews, not by presence', (
            '<p>Manage a remote SDR by agreed activity and outcome numbers, regular call reviews and a weekly one to one. Watching for online status or mouse movement measures presence, not selling.</p>'
            '<p>Trust is the hardest part for many managers. In Microsoft\'s ' + a(MS_PARANOIA, 'Work Trend Index research') + ' covering 20,000 people in 11 countries, more than eight in ten employees said they were at least as productive working from home, while more than half of managers said productivity had dropped. Microsoft called the gap "productivity paranoia". The cure is not more monitoring. It is clearer evidence.</p>'
            '<p>For an SDR, that evidence is easy to get, because almost all of the work leaves a trace:</p>'
            '<ul><li><b>Leading numbers.</b> Accounts researched, conversations, positive replies. Review them weekly, not hourly.</li>'
            '<li><b>Outcomes.</b> Qualified meetings booked and held. Use the same definition of "qualified" that your account executives use.</li>'
            '<li><b>Call reviews.</b> Listen to two or three recorded calls together each week. This is the remote version of walking the floor, and it is where most coaching happens.</li>'
            '<li><b>Written updates.</b> A short end of day note on what happened and where they are stuck takes five minutes and saves a lot of guessing.</li></ul>'
            '<p>Be patient with ramp time. The ' + a(BRIDGE, 'Bridge Group\'s 2025 SDR report') + ' puts average ramp at about three months, and remote does not shorten it. What remote changes is how early you can spot a problem, if you are looking at the right evidence.</p>'
        )),
        ('where-to-hire', 'Where to find remote SDRs who work your hours', (
            '<p>Look for remote SDRs where your core hours are their normal working day: within the US, or in Latin America, where most countries are close to US time zones. A rep who works your hours without working nights stays sharper and stays longer.</p>'
            '<p>You have three main routes:</p>'
            '<ul><li><b>Hire directly.</b> Post the role, run the process above and employ the rep yourself. This gives you full control and takes the most time, especially if you hire across borders.</li>'
            '<li><b>Use a talent partner.</b> A specialist sends you pre-screened candidates, you interview and decide, and the partner handles contracts. This is faster, and the quality depends on how well the partner tests calls and English.</li>'
            '<li><b>Outsource the function.</b> If you need outbound results more than a team member, an outsourced service may fit better. We compare the options in <a href="/blog/outsourced-sdr-vs-in-house-sdr">outsourced SDR vs in-house SDR</a>.</li></ul>'
            '<p>If you are considering Latin America, our guide on <a href="/blog/hire-bilingual-sdr-latin-america">how to hire a bilingual SDR from Latin America</a> covers sourcing, English and contracts, and <a href="/blog/nearshore-vs-offshore-sales-teams">nearshore vs offshore sales teams</a> explains why time zone overlap matters so much for calling roles.</p>'
            '<p>At BL Agency, we send three profiles within 72 hours. Each candidate has been interviewed in English and put through a live cold call roleplay, with honest notes on each. You interview them yourself and decide, and reps cover any US time zone.</p>'
        )),
    ],
    'conclusion': (
        '<p>Hiring a remote SDR is not harder than hiring one for the office. It just asks you to replace impressions with evidence at every step.</p>'
        '<ol><li><b>Name what changes:</b> evidence, written communication and structure.</li>'
        '<li><b>Write a remote job description:</b> core hours, tools and weekly output.</li>'
        '<li><b>Screen on the work:</b> a short written task and a live roleplay call.</li>'
        '<li><b>Check the setup:</b> space, connection, headset and hours.</li>'
        '<li><b>Onboard on purpose:</b> a written plan, an active manager, a buddy and a supervised week.</li>'
        '<li><b>Manage by evidence:</b> numbers, call reviews and short written updates.</li>'
        '<li><b>Hire where your hours are their day:</b> the US or nearby Latin America.</li></ol>'
        '<p>If you want remote SDRs who have already been tested on a live call, <a href="/talent">request profiles</a> and we will send three within 72 hours.</p>'
    ),
    'faq': [
        ('Can an SDR work fully remote?',
         'Yes. SDR work runs on phone, email, LinkedIn and a CRM, so it fits remote work well. What matters is a quiet setup, overlap with your buyers\' hours and a manager who reviews calls and results regularly.'),
        ('What should I include in a remote SDR job description?',
         'Include the core hours in your time zone, the tools the rep will use, the weekly output you expect once they are ramped, and what kind of remote the role is. These lines filter candidates better than a list of soft skills.'),
        ('How do I interview a remote SDR?',
         'Use a short written task, such as a first email to a real company in your market, and a live roleplay call where you play the buyer. Run part of the call on audio only, since that is how the rep will work.'),
        ('How long does it take a remote SDR to ramp?',
         'Industry research puts average SDR ramp at about three months, and remote does not change that much. A structured first month with shadowing and a supervised week helps a remote rep reach full output on time.'),
        ('How do I manage a remote SDR without micromanaging?',
         'Agree on activity and outcome numbers, review them weekly, listen to a few recorded calls together each week and ask for a short daily written update. That gives you clear evidence without tracking online status.'),
        ('Should a remote SDR work in my time zone?',
         'They should be available during the hours your buyers can be reached. Reps in Latin America usually overlap with US business hours without working nights, which helps with focus and retention.'),
        ('How does BL Agency help with remote SDR hiring?',
         'We send three bilingual sales professionals from Latin America within 72 hours, each interviewed in English and put through a live cold call roleplay. You interview them and decide, and replacement is included in the first 30 days.'),
    ],
}
