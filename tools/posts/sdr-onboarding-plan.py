# Spec for blog/sdr-onboarding-plan.html. Build: python3 tools/blogkit.py tools/posts/sdr-onboarding-plan.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


BRIDGE = 'https://bridgegroupinc.com/research/sdr-tenure-and-ramp-time'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
RAIN = 'https://www.rainsalestraining.com/blog/sales-rep-onboarding-how-long-does-it-really-take'
SHRM = 'https://www.shrm.org/mena/topics-tools/news/talent-acquisition/dont-underestimate-importance-good-onboarding'

fig1 = figure(1, timeline('An SDR onboarding plan in three blocks', [
    (0, 30, 'Learn and shadow', 'foundations, then supervised touches'),
    (30, 60, 'Own a segment', 'coached daily'),
    (60, 90, 'Full rhythm', 'independent, weekly coaching'),
], total=90, unit='days', accent=('Own a segment',)),
    'The 90 days split into three blocks: week one for foundations, then supervised outreach, then a segment of their own. Days 31 to 60 (amber) are where most plans go quiet, and where daily coaching makes the biggest difference.')

fig2 = figure(2, bar_chart('Average months for a new seller to reach each stage, RAIN Group', [
    ('Ready for buyers', 3),
    ('Competent', 9),
    ('Top performer', 15),
], unit=' months', vmax=18, highlight=('Ready for buyers',)),
    f'Averages reported by 423 sales leaders, for sellers in general, assuming the company has onboarding systems in place. The first 90 days get a rep in front of buyers; competence takes longer, which is why coaching cannot stop at day 90. Source: {a(RAIN, "RAIN Group, Sales Rep Onboarding: How Long Does It Really Take?")}.')

fig3 = figure(3, table(['Checkpoint', 'What the rep can do', 'What the manager checks', 'Red flag'], [
    ['<b>Day 7</b>', 'Explain the ICP, the problem you solve and three customer stories in their own words.', 'A five minute pitch back to the manager.', 'Reads from notes, cannot say who the buyer is.'],
    ['<b>Day 30</b>', 'Research an account, write a first email and run a cold call that the manager approves.', 'Three researched accounts and two recorded calls.', 'Same generic opener on every touch.'],
    ['<b>Day 60</b>', 'Work one segment end to end with a daily activity rhythm and book first meetings.', 'Reply quality, meeting notes and CRM hygiene.', 'Activity is up but no one replies, or notes are empty.'],
    ['<b>Day 90</b>', 'Hit the agreed meeting goal for the segment and coach a newer rep on one skill.', 'Qualified meetings against the written definition.', 'Meetings that the AE rejects as not qualified.'],
]), 'Four checkpoints with something you can see, not a feeling. Agree them with the rep on day one so nobody is surprised at day 90.')

POST = {
    'slug': 'sdr-onboarding-plan',
    'title': 'SDR onboarding plan: the first 30, 60 and 90 days',
    'h1': 'SDR onboarding plan: the first <em>30, 60 and 90</em> days',
    'description': 'A week by week SDR onboarding plan for the first 90 days: what to cover in week one, milestones at days 30, 60 and 90, how to coach and how to onboard a remote SDR.',
    'category': 'Hiring',
    'date': '2026-11-06',
    'date_label': 'November 6, 2026',
    'hero_img': 'cover-sdr-onboarding-plan',
    'card_img': 'cover-sdr-onboarding-plan',
    'card_title': 'SDR onboarding plan: the first 30, 60 and 90 days',
    'card_text': 'What to cover in week one, what a rep should do by days 30, 60 and 90, and how to coach along the way.',
    'takeaways': [
        'Average SDR ramp is about three months, so a 90 day plan matches the real ramp. Plan it week by week before the rep starts.',
        'Week one is for the buyer, the problem and the customer stories, not tools. A rep who can explain the buyer learns tools fast.',
        'Give the rep real touches early, with approval, and one segment of their own by day 31. Most plans go quiet in the middle month.',
        'Agree visible checkpoints for days 7, 30, 60 and 90 on day one, and keep coaching after day 90.',
    ],
    'intro': (
        '<p>Most SDRs are hired with a clear job description and onboarded with a calendar of product demos and tool logins. Three weeks later they are sending emails nobody approved, to a list nobody checked, and the manager finds out at the end of the month.</p>'
        '<p>This guide sets out a 30, 60 and 90 day SDR onboarding plan you can copy. It covers what to do before day one, what week one should teach, what a rep should be doing at each checkpoint, how to coach and how to change the plan for a remote SDR, including bilingual reps working from Latin America.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring an SDR to onboard?',
        'inline_text': 'Start with someone who has already passed an English interview and a live cold call roleplay. Tell us the role and get three interviewed profiles in 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'SDRs who arrive <em>ready to learn</em> your market.',
        'band_text': 'Vetted SDRs, cold callers and AEs from Latin America, interviewed in English and roleplayed on a live cold call by people who sell.',
    },
    'sections': [
        ('short-answer', 'The short answer: plan the 90 days before day one', (
            '<p>A good SDR onboarding plan covers the first 90 days week by week: the buyer and the product in week one, supervised outreach for the rest of the first month, one segment of their own in the second month and a full working rhythm by the third. It works because it matches how long the job actually takes to learn.</p>'
            '<p>The Bridge Group\'s ' + a(BRIDGE25, '2025 SDR Metrics Report') + ' puts average SDR ramp at 3.0 months. Ninety days is not an arbitrary number; it is roughly how long a typical rep takes to reach full productivity. The plan is there to make that time count.</p>'
            '<p>It also matters for retention. A widely shared ' + a(SHRM, 'SHRM article on onboarding') + ' cites Click Boarding data that employees who went through a structured onboarding program were 58% more likely to still be with the company after three years. For SDRs, whose average tenure is about 1.9 years according to ' + a(BRIDGE, 'the Bridge Group') + ', a better start buys more productive months.</p>'
            '<p>The plan has three parts that work together:</p>'
            '<ul><li><b>A schedule.</b> What the rep learns and does each week, written down before they start.</li>'
            '<li><b>Checkpoints.</b> Something the rep shows at days 7, 30, 60 and 90, agreed on day one.</li>'
            '<li><b>A coaching rhythm.</b> Daily at first, then weekly, with one specific note at a time.</li></ul>'
        )),
        ('before-day-one', 'Before day one: what to have ready', (
            '<p>Before the rep starts, have their accounts, tools, first segment and coaching calendar ready, so the first week is spent learning the buyer instead of waiting for logins. A rep who spends three days chasing access learns that the job is waiting.</p>'
            '<p>The checklist:</p>'
            '<ul><li><b>Access.</b> Email, CRM, sequencer, dialer, data tool, calendar and recording tool, all working and tested.</li>'
            '<li><b>Domains and sending limits.</b> If the rep will send email, the domain and mailbox should be set up and warmed, with clear daily limits. Someone other than the new rep owns deliverability.</li>'
            '<li><b>A starter segment.</b> A short list of accounts in one segment the rep will own from day 31. Pick a segment where you already have customers, so there are stories to tell.</li>'
            '<li><b>The playbook.</b> Your ideal customer profile, the problems you solve, three customer stories, common objections with answers and examples of emails and calls that worked.</li>'
            '<li><b>A written definition of a qualified meeting.</b> What must be true before a meeting counts. The rep should learn this in week one, not discover it when an AE rejects a meeting.</li>'
            '<li><b>A coaching calendar.</b> A daily 15 minute check in for the first month, call reviews twice a week and a weekly one to one.</li>'
            '<li><b>A buddy.</b> A peer the rep can ask small questions without waiting for the manager.</li></ul>'
            '<p>If you are building the team for the first time, the interview is part of this preparation. A rep hired through a structured screen with a live roleplay starts with skills you have already seen. Our guide to the <a href="/blog/sdr-interview-process">20-minute SDR interview</a> shows how.</p>'
        )),
        ('days-1-30', 'Days 1 to 30: learn the buyer, then practice with a net', (
            '<p>The first 30 days should teach the rep who buys and why, then let them practice real outreach with every message approved. By day 30, the rep should be able to research an account, write a first email and run a cold call that the manager signs off on.</p>'
            + fig1 +
            '<p><b>Week 1: foundations.</b></p>'
            '<ul><li>The ideal customer profile and the signals that make an account worth contacting now.</li>'
            '<li>The problem you solve, told through three customer stories the rep can repeat in their own words.</li>'
            '<li>Listening to ten recorded calls, good and bad, and reading your best email threads.</li>'
            '<li>The definition of a qualified meeting and how the handoff to the AE works.</li>'
            '<li>Tools, but last. They are easy once the rep understands the buyer.</li></ul>'
            '<p>End the week with a five minute pitch back to the manager: who we sell to, what problem we solve and one story.</p>'
            '<p><b>Weeks 2 to 4: supervised outreach.</b> The rep starts real work, with a net.</p>'
            '<ul><li>Research a few accounts a day and write the reason for contacting each one.</li>'
            '<li>Draft first emails that the manager approves before sending.</li>'
            '<li>Roleplay cold calls daily, then make live calls with the manager or buddy listening.</li>'
            '<li>Shadow an AE on discovery calls to hear what happens after the handoff.</li></ul>'
            '<p>Keep volume low on purpose. The goal of the first month is good habits, not activity numbers.</p>'
        )),
        ('days-31-60', 'Days 31 to 60: own one segment', (
            '<p>In the second month the rep should own one segment end to end, with a daily activity rhythm and daily coaching, and book their first meetings. This is the month most onboarding plans skip: the training sessions end, the rep is on their own and quality slips without anyone noticing.</p>'
            '<p>What changes:</p>'
            '<ul><li><b>Ownership.</b> The starter segment is now theirs: research, sequences, calls, replies and CRM notes.</li>'
            '<li><b>Rhythm.</b> A daily block for research, a block for calls at the times your buyers pick up and a block for replies. Protect the call block from meetings.</li>'
            '<li><b>Approval loosens.</b> The manager moves from approving every email to reviewing a sample each day and every reply that needs judgment.</li>'
            '<li><b>Coaching gets specific.</b> Two recorded calls reviewed each week, with one note per review. One note the rep can apply beats ten they cannot.</li></ul>'
            '<p>Watch for the middle month red flags: activity rising while replies stay flat, the same opener on every touch or CRM notes that say nothing. Each one is a coaching conversation, not a performance problem yet.</p>'
            '<p>The rep should also start writing down what they hear. Which objections come up, which titles reply, which stories land. That record is useful for the whole team, and it trains the habit of learning from the market.</p>'
        )),
        ('days-61-90', 'Days 61 to 90: full rhythm and clear goals', (
            '<p>By days 61 to 90 the rep should work at a full rhythm, hit the meeting goal you agreed for their segment and need coaching weekly rather than daily. Day 90 is a checkpoint, not a finish line; the rep is ready for buyers, not yet a top performer.</p>'
            + fig2 +
            '<p>RAIN Group\'s survey of 423 sales leaders, summarized in ' + a(RAIN, 'their onboarding research') + ', found that new sellers take about three months on average to be ready for buyers, nine months to be competent and 15 months to become top performers. Those figures cover sellers in general, not only SDRs, but the lesson holds: onboarding gets the rep to the starting line.</p>'
            '<p>What to do in the third month:</p>'
            '<ul><li><b>Set the goal on qualified meetings,</b> measured against your written definition. Activity goals can support it, but they should not replace it.</li>'
            '<li><b>Add a second segment or channel</b> if the first is running well.</li>'
            '<li><b>Move to weekly coaching</b> with a call review and a look at reply quality.</li>'
            '<li><b>Ask the rep to teach.</b> Explaining one skill to a newer rep shows whether they really own it.</li></ul>'
            '<p>The Bridge Group found that ' + a(BRIDGE25, 'only 60% of SDRs reached quota in 2025') + ', the lowest share in its history. Clear goals, set early and measured on quality, are one of the few things a manager fully controls.</p>'
        )),
        ('checkpoints', 'Checkpoints and coaching: what to measure', (
            '<p>Measure onboarding with four checkpoints, each tied to something the rep shows you: a pitch at day 7, approved outreach at day 30, a working segment at day 60 and qualified meetings at day 90. Agree them on day one, so the rep knows exactly what good looks like.</p>'
            + fig3 +
            '<p>How to coach between checkpoints:</p>'
            '<ul><li><b>One note at a time.</b> Pick the change that matters most and ask the rep to try it on the next call.</li>'
            '<li><b>Review recordings, not summaries.</b> What the rep says happened and what happened are often different.</li>'
            '<li><b>Ask before telling.</b> "What would you change about that call?" builds the habit of self review.</li>'
            '<li><b>Separate skill from effort.</b> Low activity is an effort conversation; low replies on good activity is a skill conversation.</li></ul>'
            '<p>If a rep misses a checkpoint, slow down rather than speed up. Go back to the step that is not working, practice it and set a new date. Most missed checkpoints in the first 60 days are a sign the plan moved too fast, not that the hire was wrong.</p>'
        )),
        ('remote', 'Onboarding a remote or LatAm-based SDR', (
            '<p>A remote SDR needs the same plan with more structure: fixed overlap hours, recorded calls for review, written answers to common questions and a buddy they can message without waiting. Distance does not change what the rep has to learn; it changes how easily they can ask.</p>'
            '<p>Adjustments that help:</p>'
            '<ul><li><b>Overlap hours.</b> Agree the hours the rep works and make sure they cover your buyers\' day. Many reps in Latin America work on US Eastern or Central time with little or no time difference.</li>'
            '<li><b>Daily check in on video</b> for the first month, even if it is short.</li>'
            '<li><b>A written playbook</b> the rep can search, so small questions do not wait for a meeting.</li>'
            '<li><b>Shared call recordings</b> that the manager reviews on a fixed schedule.</li>'
            '<li><b>Local market context.</b> A bilingual rep may know a buyer\'s culture better than you do. Ask what they hear and use it.</li></ul>'
            '<p>English matters most on the phone. Test it on a live call before hiring, not on a written test. At BL Agency, every candidate in our talent pool has passed an English interview and a live cold call roleplay before a client meets them, so onboarding can start with your buyer instead of the basics. Our guide on <a href="/blog/hire-bilingual-sdr-latin-america">hiring a bilingual SDR from Latin America</a> covers the rest of the process.</p>'
        )),
    ],
    'conclusion': (
        '<p>An SDR onboarding plan works when it is written before day one, matched to a real ramp of about three months and measured with checkpoints you can see.</p>'
        '<ol><li><b>Prepare before day one:</b> access, a starter segment, the playbook, a qualified meeting definition and a coaching calendar.</li>'
        '<li><b>Days 1 to 30:</b> learn the buyer, then practice real outreach with every message approved.</li>'
        '<li><b>Days 31 to 60:</b> own one segment, with daily coaching and a protected call block.</li>'
        '<li><b>Days 61 to 90:</b> full rhythm, goals on qualified meetings and weekly coaching.</li>'
        '<li><b>Keep coaching after day 90.</b> Ready for buyers is the start, not the end.</li></ol>'
        '<p>If you are about to hire the SDR you will onboard, <a href="/talent">tell us the role</a> and we will send three interviewed profiles in 72 hours.</p>'
    ),
    'faq': [
        ('How long should SDR onboarding take?',
         'Plan for about 90 days. The Bridge Group 2025 SDR Metrics Report puts average SDR ramp at 3.0 months, so a 30, 60 and 90 day plan matches how long the job takes to learn. Coaching continues after that.'),
        ('What should an SDR learn in the first week?',
         'The ideal customer profile, the problem you solve, three customer stories, the definition of a qualified meeting and how the handoff to the AE works. Tools come last, because they are easy once the rep understands the buyer.'),
        ('When should a new SDR start outreach?',
         'In the second week, with every email and call approved by the manager. Real touches with a safety net teach faster than more training sessions.'),
        ('What goals should an SDR have at 30, 60 and 90 days?',
         'At day 30, approved research, emails and calls. At day 60, one segment worked end to end with first meetings booked. At day 90, the agreed goal of qualified meetings for that segment.'),
        ('How often should I coach a new SDR?',
         'Daily for the first month, with short check ins and two call reviews a week. Move to weekly coaching once the rep works a full rhythm, usually in the third month.'),
        ('How is onboarding a remote SDR different?',
         'The content is the same, but it needs more structure: fixed overlap hours, a daily video check in, a written playbook, shared call recordings and a buddy the rep can message.'),
        ('What are signs an SDR onboarding is not working?',
         'Activity that rises while replies stay flat, the same opener on every touch, empty CRM notes and meetings the AE rejects. Each is a reason to slow down and coach the step that is failing.'),
    ],
}
