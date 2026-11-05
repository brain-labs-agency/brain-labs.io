# Spec for blog/sdr-interview-process.html. Build: python3 tools/blogkit.py tools/posts/sdr-interview-process.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


SIOP = 'https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance'
NOON = 'https://www.noon.ai/blog/articles/356-structured-interview-validity'
REWORK = 'https://rework.withgoogle.com/intl/en/guides/a-guide-to-structured-interviewing-for-better-hiring-practices'
BRIDGE = 'https://bridgegroupinc.com/research/sdr-tenure-and-ramp-time'
GONG = 'https://www.gong.io/blog/the-best-and-worst-cold-call-openers-backed-by-data-from-300m-calls'

class R(float):
    def __format__(self, spec):
        return f'{float(self):.2f}'


fig1 = figure(1, bar_chart('How well common hiring methods predict job performance, Sackett et al. 2022', [
    ('Structured interview', R(0.42)),
    ('Job knowledge test', R(0.40)),
    ('Work sample test', R(0.33)),
    ('Cognitive ability test', R(0.31)),
    ('Unstructured interview', R(0.19)),
], vmax=0.5, highlight=('Structured interview',)),
    f'Mean operational validity (correlation with later job performance) from the 2022 meta-analysis by Sackett, Zhang, Berry and Lievens. A structured interview predicts about twice as well as an unstructured chat. Sources: {a(SIOP, "SIOP summary of Sackett et al. 2022")} and {a(NOON, "summary of Table 3")}.')

fig2 = figure(2, timeline('The 20-minute SDR screen, minute by minute', [
    (0, 2, 'Open', 'agenda'),
    (2, 7, 'Questions', '3 questions'),
    (7, 12, 'Cold call', 'roleplay'),
    (12, 15, 'Coach', 'one note'),
    (15, 18, 'Research', 'one account'),
    (18, 20, 'Close', 'questions'),
], total=20, accent=('Coach',)),
    'Every candidate gets the same six blocks in the same order. The coaching block (amber) is the one most interviews skip, and it is the best test of how fast someone will ramp.')

fig3 = figure(3, table(['What you score', 'Strong answer (4)', 'Weak answer (1)', 'Where it shows up'], [
    ['<b>Coachability</b>', 'Takes one note and visibly changes the second attempt.', 'Repeats the same call, or argues with the feedback.', 'Coaching block'],
    ['<b>Resilience</b>', 'Describes a bad stretch, what they changed and the result.', 'Blames the list, the product or the manager.', 'Questions'],
    ['<b>Curiosity</b>', 'Asks the buyer questions and listens to the answers.', 'Pitches without asking anything.', 'Cold call roleplay'],
    ['<b>Clarity</b>', 'Short sentences, steady pace, gets to the point in ten seconds.', 'Long preamble, filler, apologetic opener.', 'Cold call roleplay'],
    ['<b>Research instinct</b>', 'Finds a real reason to call a specific account.', 'Lists generic facts about the company.', 'Research block'],
]), 'A five-line scorecard on a 1 to 4 scale. Each interviewer scores alone before anyone discusses the candidate.')

POST = {
    'slug': 'sdr-interview-process',
    'title': 'How to interview an SDR: the 20-minute screen',
    'h1': 'How to interview an SDR: the <em>20-minute</em> screen',
    'description': 'A structured 20-minute SDR interview: what to score, the questions to ask, a live cold call roleplay with a coaching round, a scorecard and what to do after the screen.',
    'category': 'Hiring',
    'date': '2026-11-05',
    'date_label': 'November 5, 2026',
    'hero_img': 'cover-sdr-interview-process',
    'card_img': 'cover-sdr-interview-process',
    'card_title': 'How to interview an SDR: the 20-minute screen',
    'card_text': 'Three fixed questions, a live cold call, one round of coaching and a five-line scorecard.',
    'takeaways': [
        'A structured interview predicts job performance about twice as well as an unstructured conversation. Ask every candidate the same questions and score them the same way.',
        'Twenty minutes is enough for a first SDR screen if you spend most of it watching the candidate do the job: a cold call roleplay and a quick account research exercise.',
        'Coach once and run the roleplay again. How much a candidate improves in three minutes is the best early signal of how fast they will ramp.',
        'Score alone on a short rubric before discussing, then move strong candidates to the next step within days.',
    ],
    'intro': (
        '<p>Most SDR interviews are conversations about a CV. The candidate describes their last job, the interviewer asks about goals and motivation, and both leave with a feeling. Feelings are a poor predictor of who will book meetings in month three.</p>'
        '<p>This guide lays out a 20-minute SDR screen that tests the job instead of the story about the job. It covers what to score, the questions to ask, how to run a live cold call roleplay with a coaching round, how to score fairly and what to do after the screen. It works for in-house hires and for remote SDRs, including bilingual reps from Latin America.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring an SDR now?',
        'inline_text': 'We screen every candidate in English with a live cold call roleplay before you meet them. Tell us the role and get three interviewed profiles in 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'SDRs who passed the screen <em>before</em> you meet them.',
        'band_text': 'Vetted SDRs, cold callers and AEs from Latin America, interviewed in English and roleplayed on a live cold call by people who sell.',
    },
    'sections': [
        ('short-answer', 'The short answer: structure beats conversation', (
            '<p>The best SDR interview is a short, structured screen: the same questions for every candidate, a live cold call roleplay, one round of coaching and a scorecard filled in before anyone discusses the result. Twenty minutes is enough for a first screen if most of it is spent watching the candidate work.</p>'
            '<p>The research behind this is strong. A 2022 meta-analysis by Sackett, Zhang, Berry and Lievens, published in the <i>Journal of Applied Psychology</i>, found that ' + a(SIOP, 'structured interviews had the highest mean validity') + ' of the common hiring methods it reviewed, at .42. Unstructured interviews came in at ' + a(NOON, '.19') + '. In plain terms, the same hour of interviewing tells you about twice as much when the questions and scoring are fixed in advance.</p>'
            + fig1 +
            '<p>Google reached a similar conclusion in its own hiring. Its ' + a(REWORK, 're:Work guide to structured interviewing') + ' reports that pre-made questions and rubrics saved interviewers about 40 minutes per interview, and that rejected candidates who had a structured interview were 35% happier with the process than those who did not.</p>'
            '<p>For SDRs, structure matters even more, because the job is learnable and repetitive. You are not looking for the most impressive person in the room. You are looking for the person who will make a hundred good attempts a week, take feedback and get better every month.</p>'
        )),
        ('what-to-score', 'Decide what you are scoring before you interview', (
            '<p>Score five things: coachability, resilience, curiosity, clarity and research instinct. Write down what a strong and a weak answer look like for each before the first interview, so every candidate is judged against the same bar.</p>'
            '<p>These five come from the work itself. An SDR spends the day finding accounts with a reason to talk, writing or calling to start a conversation, handling rejection and learning from a manager who reviews their calls. Each trait maps to one of those tasks.</p>'
            '<ul><li><b>Coachability.</b> New SDRs improve through feedback on real calls and emails. Someone who absorbs one note quickly will be productive sooner than someone with more experience who does not.</li>'
            '<li><b>Resilience.</b> Most attempts do not turn into conversations. Look for people who can describe a bad stretch, what they changed and what happened next.</li>'
            '<li><b>Curiosity.</b> Meetings come from relevance. A curious SDR asks questions, listens and connects what they hear to the reason for the call.</li>'
            '<li><b>Clarity.</b> In the first ten seconds of a call, clarity beats polish. Short sentences and a steady pace matter more than vocabulary or accent.</li>'
            '<li><b>Research instinct.</b> The best emails and calls have a specific reason behind them. Some candidates find that reason naturally; others recite the company\'s About page.</li></ul>'
            '<p><b>What to leave out of the screen.</b> Years of experience, industry background and tool familiarity are easy to check from a CV and easy to teach. They are worth a quick question, not the interview. Culture fit as a vague feeling is worse than useless, because it rewards people who resemble the interviewer. If there are values you care about, write them as behaviors and score them like everything else.</p>'
        )),
        ('the-20-minutes', 'The 20-minute screen, minute by minute', (
            '<p>Split the 20 minutes into six fixed blocks: a two-minute opening, five minutes of questions, a five-minute cold call roleplay, three minutes of coaching and a second attempt, three minutes of account research and two minutes for the candidate\'s questions. Keep the order the same for every candidate.</p>'
            + fig2 +
            '<p><b>Open (0 to 2).</b> Tell the candidate exactly what will happen, including the roleplay. Surprising people does not test resilience; it tests whether they have seen your format before. Telling them up front gives everyone the same starting point.</p>'
            '<p><b>Questions (2 to 7).</b> Ask three fixed questions from the next section. Use the same wording each time and the same follow-up prompts. Take notes on what they say, not on how you feel about it.</p>'
            '<p><b>Cold call (7 to 12).</b> Give a short brief: who you sell to, one line on the offer and the persona they are calling. Allow one minute to prepare, then play a busy buyer. Interrupt early, say you are in a meeting, then say you already have a vendor.</p>'
            '<p><b>Coach (12 to 15).</b> Give one specific piece of feedback, such as "lead with the reason you are calling, not your name and company", and run the call again. This is the most important block in the screen.</p>'
            '<p><b>Research (15 to 18).</b> Name a real company in your market and give the candidate two minutes with a browser to find one reason to contact them this month. Ask them to explain what they found and how they would open with it.</p>'
            '<p><b>Close (18 to 20).</b> Let them ask questions. Good candidates ask about the market, the list, how meetings are defined and how they will be coached. Note what they ask; it is part of the signal.</p>'
        )),
        ('questions', 'The questions to ask, and what good answers sound like', (
            '<p>Ask three fixed questions: one about rejection, one about learning and one about why sales development. Behavioral questions about real past situations predict more than hypothetical ones about what someone would do, so ask for specific examples and follow up until you get one.</p>'
            '<p>Choose three from this list and use them with every candidate for the role:</p>'
            '<ol><li><b>"Tell me about a week where nothing worked. What did you change?"</b> A strong answer names a specific week, a specific change and a result. A weak answer talks about staying positive.</li>'
            '<li><b>"What is the best piece of feedback a manager has given you, and what did you do with it?"</b> Listen for a concrete change in behavior, not a compliment they received.</li>'
            '<li><b>"Walk me through how you would prepare for a call with a new account."</b> Strong candidates describe a short, practical routine. Weak ones describe reading everything, which never fits an SDR\'s day.</li>'
            '<li><b>"Why sales development, and why now?"</b> There is no single right answer, but strong candidates connect the role to a plan, such as moving into an account executive seat, and know what the job involves day to day.</li>'
            '<li><b>"Tell me about a time you got a hard no. What happened next?"</b> Listen for curiosity about the reason, not just persistence.</li>'
            '<li><b>"How do you keep track of your own numbers?"</b> SDRs who measure their own activity and conversion improve faster than those who wait for a manager\'s report.</li></ol>'
            '<p><b>Follow-up prompts.</b> Prepare two follow-ups for each question, such as "What did you try first?" and "How did you know it worked?". Use them whenever an answer stays general. A candidate who cannot get specific after two prompts has told you something useful.</p>'
            '<p><b>Questions to avoid.</b> Skip brainteasers, "sell me this pen" and questions about personal life. They add noise, favor people who have practiced them and, in the case of personal questions, can create legal risk. Keep everything tied to the work.</p>'
        )),
        ('roleplay', 'Run the cold call roleplay with a coaching round', (
            '<p>Run a five-minute cold call where you play a busy, skeptical buyer, then give one piece of feedback and run it again. The first attempt shows where the candidate starts; the second shows how fast they learn, which is what you are really hiring for.</p>'
            '<p><b>Make the brief realistic and short.</b> Three lines are enough: the buyer\'s title and company type, what you sell in one sentence and the reason for the call. Use the same brief for every candidate so attempts are comparable.</p>'
            '<p><b>Play the buyer consistently.</b> Use the same three moments every time: an interruption in the first ten seconds, a "send me an email", and a "we already have someone for that". Do not get harder for candidates you like less. Consistency is what makes the roleplay fair.</p>'
            '<p><b>Listen for the opener.</b> The first ten seconds decide whether the buyer stays on the line. Gong\'s analysis of ' + a(GONG, 'more than 300 million cold calls') + ' found that "Did I catch you at a bad time?" worked about a fifth as often as the strongest openers. Many candidates default to apologetic openers from support roles. That is fine on the first attempt; it is what coaching is for.</p>'
            '<p><b>Give one note, not five.</b> Pick the single change that would most improve the call and say it plainly. "Ask a question after you say why you are calling" is better than a list of everything that went wrong.</p>'
            '<p><b>Score the change, not the polish.</b> A candidate who goes from a weak first call to a clearly better second call is often a better hire than one who was smooth both times and did not change anything. You will be coaching this person every week; the roleplay is a preview of those sessions.</p>'
            '<p><b>For bilingual roles,</b> run the roleplay in the language of the buyers they will call. If they will call US buyers, switch to English without warning partway through the interview. You learn how they think in English, not how well they rehearsed.</p>'
        )),
        ('scoring', 'Score fairly and decide fast', (
            '<p>Score each of the five traits from 1 to 4 straight after the screen, alone, before you talk to anyone else who met the candidate. Then compare scores, discuss the gaps and decide within a day or two.</p>'
            + fig3 +
            '<p><b>Why score alone first.</b> When interviewers discuss before scoring, the most confident voice in the room sets the result. Independent scores, written down, keep each person\'s observation intact and make disagreements visible.</p>'
            '<p><b>Use a four-point scale.</b> Without a middle option, interviewers have to decide whether a candidate leans strong or weak on each trait. Write the anchors down, as in the table above, so a 3 means the same thing to everyone.</p>'
            '<p><b>Set a bar, not a ranking.</b> Decide in advance what total score moves a candidate forward, and require a minimum on coachability. Comparing candidates only against each other means the best of a weak week gets hired.</p>'
            '<p><b>Watch for red flags.</b> Blaming every past result on someone else, refusing the coaching note, and never asking the buyer a question are each worth a closer look, even when the total score is high.</p>'
            '<p><b>Move fast.</b> Strong SDR candidates often have several processes running. A clear decision and next step within a day or two is part of a good candidate experience, and it is often what wins the hire.</p>'
        )),
        ('after-the-screen', 'What to do after the screen', (
            '<p>Move candidates who pass the screen to a short written exercise, a conversation with the hiring manager and reference calls with former managers. Keep the whole process to about a week, and plan the first 90 days before the offer goes out.</p>'
            '<p><b>Written exercise.</b> Ask for a first email and one follow-up to a real account in your market, with a short note on why they chose that angle. Limit it to thirty minutes. You are checking whether the research instinct from the screen holds up in writing.</p>'
            '<p><b>Hiring manager conversation.</b> The manager who will coach the SDR should meet them, ideally with a second short roleplay. This is also where you talk about the territory, the targets and how meetings are defined.</p>'
            '<p><b>Reference calls.</b> Ask former managers how the candidate responded to coaching on recorded calls and how they handled a bad month. Those two questions map directly to your scorecard.</p>'
            '<p><b>Why it is worth the effort.</b> A wrong SDR hire is expensive in time even before it shows in results. The Bridge Group\'s ' + a(BRIDGE, 'research on SDR tenure and ramp') + ' puts average ramp at 3.0 months and average tenure at 1.9 years. A hire that does not work out uses a large share of that window before anyone is sure.</p>'
            '<p><b>Hiring remotely or from Latin America.</b> The same screen works over video. Add a check of their working hours against your buyers\' day, test their English on a live call rather than a written test and confirm their setup: a quiet space, a reliable connection and a headset. At BL Agency, every candidate in our talent pool has been through an English interview and a live cold call roleplay with our sales team before a client meets them. You still run your own screen; this one just starts you closer to the finish.</p>'
        )),
    ],
    'conclusion': (
        '<p>A good SDR interview is short, structured and spent watching the candidate do the work.</p>'
        '<ol><li><b>Decide what you are scoring</b> before the first interview: coachability, resilience, curiosity, clarity and research instinct.</li>'
        '<li><b>Run the same 20 minutes</b> for every candidate: questions, a cold call, a coaching round, research and their questions.</li>'
        '<li><b>Ask behavioral questions</b> and follow up until the answer is specific.</li>'
        '<li><b>Coach once and run the call again,</b> and score the change.</li>'
        '<li><b>Score alone on a four-point rubric,</b> then compare and decide within a day or two.</li>'
        '<li><b>Finish with a written exercise, a manager conversation and references,</b> all within about a week.</li></ol>'
        '<p>If you would rather start from SDRs who have already passed a screen like this, <a href="/talent">request profiles</a> and we will send three interviewed candidates within 72 hours.</p>'
    ),
    'faq': [
        ('How long should an SDR interview be?',
         'A first screen of about 20 minutes is enough if it is structured: fixed questions, a live cold call roleplay, one round of coaching and a short research exercise. Follow it with a written exercise, a hiring manager conversation and references.'),
        ('What questions should I ask in an SDR interview?',
         'Ask behavioral questions about real situations: a week where nothing worked and what they changed, the best feedback they received and what they did with it, and how they prepare for a call with a new account. Follow up until the answer is specific.'),
        ('What should I look for in an SDR candidate?',
         'Coachability, resilience, curiosity, clarity on the phone and an instinct for finding a real reason to contact an account. Experience and tool knowledge matter less, because they are easier to teach.'),
        ('How do I run a cold call roleplay in an interview?',
         'Give a three-line brief, allow a minute to prepare and play a busy buyer who interrupts, asks for an email and says they already have a vendor. Then give one piece of feedback and run the call again to see how fast the candidate improves.'),
        ('Is "sell me this pen" a good SDR interview question?',
         'No. It favors people who have practiced it and tells you little about prospecting. A short roleplay based on your real buyer and offer is a better test of the job.'),
        ('How do I make SDR interviews fair?',
         'Use the same questions, brief and roleplay for every candidate, score each trait on a written rubric and have each interviewer score alone before discussing. Structured interviews are both more predictive and perceived as fairer by candidates.'),
        ('How do I interview a remote or nearshore SDR?',
         'Run the same structured screen over video, test English on a live call rather than in writing, confirm their working hours overlap with your buyers and check their setup: a quiet space, a reliable connection and a headset.'),
    ],
}
