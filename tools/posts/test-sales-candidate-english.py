# Spec for blog/test-sales-candidate-english.html. Build: python3 tools/blogkit.py tools/posts/test-sales-candidate-english.py
EXT = ' target="_blank" rel="noopener"'
CAL = 'https://cal.com/vero-grados-bl-agency/bl-meetings'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


KICK = 'https://kickresume.com/en/press/ai-job-search-data'
GARTNER_FAKE = 'https://www.personneltoday.com/hr/by-2028-one-in-four-candidate-profiles-will-be-fake'
SELF = 'https://www.cambridge.org/core/product/786D4E0E0D500DCDD43CCE24ED610592/core-reader'
CEFR = 'https://www.coe.int/en/web/common-european-framework-reference-languages/table-1-cefr-3.3-common-reference-levels-global-scale'
TOEIC = 'https://www.ets.org/toeic/about/speaking-writing.html'
EF25 = 'https://www.ef.edu/about-us/press/articles/2025/ef-english-proficiency-index-2025-launched/'
MUNRO = 'https://www.benjamins.com/catalog/bct.121.02mun'

fig1 = figure(1, table(['Skill', 'What it looks like on the job', 'How to test it', 'Red flag'], [
    ['<b>Being understood</b>', 'A busy buyer follows every sentence the first time, on a phone line.', 'Live call with no warm up; note every time you had to ask "sorry?"', 'You stop listening to the pitch and start decoding the words.'],
    ['<b>Listening</b>', 'Catches what the buyer meant, including the soft no and the hidden worry.', 'Play a short real call; ask what the buyer wanted and feared.', 'Summarizes the words but misses the meaning.'],
    ['<b>Fluency under pressure</b>', 'Keeps pace and stays natural when interrupted or challenged.', 'Roleplay with interruptions and a firm objection.', 'Fluent until the script breaks, then long pauses or a switch to set phrases.'],
    ['<b>Tone and register</b>', 'Sounds like a peer to a US director: direct, warm, not stiff.', 'Listen to how they open, push back and close.', 'Over-formal, apologetic or translated phrasing.'],
    ['<b>Writing</b>', 'Short, clear emails and follow ups with natural phrasing.', 'A timed written reply to a real buyer email, done live.', 'Polished in the CV, clumsy when written in front of you.'],
]), 'The five parts of sales English. A CV or certificate speaks to none of them directly, which is why each one needs its own short test.')

fig2 = figure(2, timeline('A 30 minute English test for sales roles', [
    (0, 5, 'Warm start', 'surprise switch'),
    (5, 10, 'Listening', 'call summary'),
    (10, 20, 'Roleplay', 'cold call, objections'),
    (20, 26, 'Written reply', 'timed, live'),
    (26, 30, 'Debrief', 'self review'),
], 30, unit='min', accent=('Roleplay',)),
    'One way to run the test in 30 minutes. The roleplay (amber) carries the most weight because it shows English, sales skill and composure at the same time.')

fig3 = figure(3, table(['Seat', 'Being understood', 'Listening', 'Fluency under pressure', 'Tone', 'Writing'], [
    ['<b>Cold caller</b>', '4', '4', '4', '3', '2'],
    ['<b>SDR, phone and email</b>', '4', '3', '3', '3', '3'],
    ['<b>SDR, email first</b>', '3', '3', '2', '3', '4'],
    ['<b>Account executive</b>', '4', '4', '4', '4', '3'],
    ['<b>Customer success</b>', '3', '4', '3', '4', '3'],
]), 'An example of minimum scores per seat on a 1 to 4 scale (4 is strong). Set your own bars before you interview, so every candidate for the same seat is held to the same standard.')

POST = {
    'slug': 'test-sales-candidate-english',
    'title': 'How to test a sales candidate\'s English (beyond the CV)',
    'h1': 'How to test a sales candidate\'s English <em>beyond</em> the CV',
    'description': 'How to test a sales candidate\'s English when the CV, the self-rating and the certificate tell you little: the five skills to measure, a 30 minute test, a scoring rubric and remote checks.',
    'category': 'Hiring',
    'date': '2026-11-12',
    'date_label': 'November 12, 2026',
    'hero_img': 'cover-test-sales-candidate-english',
    'card_img': 'cover-test-sales-candidate-english',
    'card_title': 'How to test a sales candidate\'s English (beyond the CV)',
    'card_text': 'The five skills to measure, a 30 minute test, a scoring rubric and the checks that matter for remote hires.',
    'takeaways': [
        'A CV, a self-rating or a certificate does not tell you how a candidate sounds to a busy US buyer. Many CVs are now written with AI, and self-ratings only moderately match tested ability.',
        'Test five things separately: being understood, listening, fluency under pressure, tone and writing. Each one breaks in a different way on a sales call.',
        'A 30 minute live test built around the job (switch, listen, roleplay, write) tells you more than any score. Keep the roleplay if you only have ten minutes.',
        'Score on a shared rubric with a minimum per seat, set before you interview. A cold caller and an email-first SDR need different bars.',
    ],
    'intro': (
        '<p>Every CV for a US-facing sales role says "fluent English" or "C1". Some candidates add a certificate, and almost all rate themselves as advanced. Then the first live call reveals someone who reads well but freezes when a buyer interrupts, or someone with a strong accent who is perfectly easy to follow. The paper did not predict either.</p>'
        '<p>This guide is about testing English the way a sales job uses it. We cover why the CV tells you so little, the five skills that actually matter, what certificates can and cannot show, a 30 minute test you can run in one interview, a rubric that lets two interviewers agree, and the extra checks you need when you hire remotely. It builds on our guide to ' + '<a href="/blog/native-english-sales-team-latin-america">building a native-level English sales team</a>' + ', with a sharper focus on the test itself.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring bilingual sales reps?',
        'inline_text': 'We interview every candidate in English and roleplay them on a live cold call before you meet them. Tell us the seat and the hours, and we come back with three profiles in 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'English tested on a <em>live</em> call, not on paper.',
        'band_text': 'Vetted SDRs, cold callers and AEs from Latin America, interviewed in English and roleplayed on a sales call before you meet them, with honest notes on where each one is strong.',
    },
    'sections': [
        ('why-cv-fails', 'Why the CV and the self-rating tell you so little', (
            '<p>The CV tells you little about spoken English because it is a written document that can be polished, translated or generated, and the self-rating is the candidate\'s own guess. Neither shows how the person sounds on a phone line with a stranger who is in a hurry.</p>'
            '<p>The written part has become even less reliable. Kickresume reported that ' + a(KICK, 'about half of its 1.22 million users in 2025') + ' used AI to write or improve their resumes. A Gartner survey of more than 3,000 job candidates, reported by ' + a(GARTNER_FAKE, 'Personnel Today') + ', found that 39% used AI during the application process, mainly to write CV and cover letter text and to answer assessment questions. Gartner also predicts that by 2028, one in four candidate profiles worldwide will be fake. A perfectly written CV is no longer evidence of anything about the person\'s English.</p>'
            '<p>Self-ratings are a weak signal too. A ' + a(SELF, 'study of 807 language learners') + ' that compared self-assessed speaking levels with a standardized oral proficiency interview found only a moderate match. Self-assessment could separate stronger speakers from weaker ones in broad strokes, but not as precisely as a real test.</p>'
            '<p>None of this means candidates are dishonest. Most people rate their English by how comfortable they feel in their usual settings: reading documents, writing on chat, talking with patient colleagues. A cold call is a different setting entirely. The fix is not to distrust every CV but to stop treating it as the test.</p>'
            '<p>Use the CV to decide who to test, and the test to decide who to hire.</p>'
        )),
        ('five-skills', 'What to measure: the five parts of sales English', (
            '<p>Measure five separate skills: being understood, listening, fluency under pressure, tone and writing. A candidate can be strong in one and weak in another, and each weakness shows up in a different moment of a sales conversation.</p>'
            + fig1 +
            '<p><b>Being understood is not the same as having no accent.</b> Research by Munro and Derwing, revisited in their ' + a(MUNRO, 'later work on accent and intelligibility') + ', found that accent, comprehensibility and intelligibility are related but partly independent: speech can be heavily accented and still highly intelligible. For a sales role, what you need is a buyer who understands every sentence the first time. Count how often you have to ask the candidate to repeat; ignore how "native" they sound.</p>'
            '<p><b>Listening is the skill most interviews skip.</b> Candidates spend the interview talking, so you rarely see whether they catch a buyer\'s soft no ("send me something and I\'ll take a look") or the worry behind a question. Test it directly.</p>'
            '<p><b>Fluency under pressure</b> is where prepared candidates break. Many people speak smoothly about themselves because they have practiced; the same person may pause for long seconds when a buyer cuts in. A sales call is mostly interruptions.</p>'
            '<p><b>Tone</b> decides whether a US director hears a peer or a script. Watch for over-formal openings, too many apologies and phrases translated word for word.</p>'
            '<p><b>Writing</b> matters more for email-first SDRs and less for cold callers. Test it live, because a written sample sent from home tells you nothing in the age of AI.</p>'
        )),
        ('certificates', 'What certificates and standardized tests can and cannot show', (
            '<p>A certificate or a CEFR level tells you the candidate passed a general English test, which makes it a reasonable floor but a poor predictor of sales performance. Use it to filter, never to decide.</p>'
            '<p>The levels themselves are broad. The Council of Europe\'s ' + a(CEFR, 'CEFR global scale') + ' describes a B2 speaker as able to interact with a degree of fluency and spontaneity that makes regular interaction with native speakers quite possible without strain for either party, and a C1 speaker as able to express ideas fluently and spontaneously without much obvious searching for expressions. Both descriptions fit someone who could do well on a sales call, and both fit someone who could struggle with a fast, skeptical buyer. The scale was not built to answer your question.</p>'
            '<p>Workplace tests are closer but still not the job. The ' + a(TOEIC, 'TOEIC Speaking test') + ', for example, has 11 questions in about 20 minutes: reading aloud, describing a picture, answering questions and giving an opinion. Most responses get 15 to 30 seconds and the longest gets 60, with preparation time for several tasks. Nobody interrupts, pushes back or says no. That is a sensible design for a standardized test and exactly why it cannot tell you how someone handles a live objection.</p>'
            '<p>Speaking is also the skill most likely to lag. The ' + a(EF25, 'EF English Proficiency Index 2025') + ', based on 2.2 million test takers in 123 countries and regions, found that speaking was the weakest English skill in more than half of the countries measured. A strong reading or overall score can hide a weaker spoken level.</p>'
            '<p>When a candidate has a recent, recognized certificate, take it as a good sign and move on to the live test. When they do not, do not penalize them for it. Many strong sales professionals learned English at work and never took an exam.</p>'
        )),
        ('the-test', 'A 30 minute English test built around the job', (
            '<p>The best English test for a sales candidate is a short version of the job, done live: an unplanned switch into English, a listening task, a roleplay with objections and a timed written reply. It fits in 30 minutes and you can run it inside your first interview.</p>'
            + fig2 +
            '<p><b>Minutes 0 to 5: the warm start.</b> If you share another language with the candidate, open in it, then switch to English without warning. Ask about something real, such as the hardest deal in their last role. Rehearsed answers sound fluent; this shows you how they think in English when they have not prepared.</p>'
            '<p><b>Minutes 5 to 10: listening.</b> Play two minutes of a real or realistic sales call where the buyer is vague or indirect. Ask the candidate what the buyer wanted, what worried them and what the rep should do next. You are testing meaning, not word recall.</p>'
            '<p><b>Minutes 10 to 20: the roleplay.</b> You are the buyer: a busy director at a company they could realistically call. Interrupt in the first 20 seconds, ask a sharp question such as "why would I change what we use today?", then give a firm no. Run it once, give one piece of coaching, and run it again. The second round shows how fast they adapt, which predicts ramp better than the first.</p>'
            '<p><b>Minutes 20 to 26: the written reply.</b> Paste a short buyer email into a shared document, such as "Not a priority this quarter. Maybe reach out next year." Give them five minutes to reply while you stay on the call. Look for short sentences, a natural tone and a sensible next step.</p>'
            '<p><b>Minutes 26 to 30: the debrief.</b> Ask what they would change about their call. Self-awareness in English is a good sign for coaching later.</p>'
            '<p>If you only have ten minutes, keep the roleplay. Our ' + '<a href="/blog/sdr-interview-process">20-minute SDR screen</a>' + ' shows how to fit it into a full first interview.</p>'
        )),
        ('scoring', 'How to score it so two interviewers agree', (
            '<p>Score each of the five skills on a simple 1 to 4 scale with written anchors, and set a minimum per seat before you start interviewing. Without a shared rubric, "good English" means something different to each interviewer, and the loudest opinion wins.</p>'
            '<p>A rubric that works in practice:</p>'
            '<ul><li><b>4, strong.</b> You never had to work to understand them, and a US buyer would not notice anything but the content.</li>'
            '<li><b>3, solid.</b> Occasional slips that never block meaning; pace holds under pressure.</li>'
            '<li><b>2, workable with coaching.</b> Meaning gets through, but you asked for repeats or noticed stiff, translated phrasing.</li>'
            '<li><b>1, not yet.</b> A buyer would lose the thread or end the call.</li></ul>'
            + fig3 +
            '<p>The table is an example, not a standard. The point is that different seats lean on different skills. A cold caller lives on being understood and on fluency under pressure; an email-first SDR leans on writing; an account executive needs strength almost everywhere because they run long, complex conversations.</p>'
            '<p>Three habits keep the scores honest:</p>'
            '<ul><li><b>Score right after the call</b>, each interviewer alone, before you compare notes.</li>'
            '<li><b>Write one line of evidence</b> per score, such as "asked for a repeat twice in the roleplay".</li>'
            '<li><b>Record the roleplay</b> (with consent) so a second person can score it, and so you can compare candidates side by side.</li></ul>'
        )),
        ('remote', 'Extra checks for remote hires', (
            '<p>When you hire remotely, add checks that confirm the English you heard is the candidate\'s own, live and unaided. With AI writing tools, real-time prompts and even interview fraud on the rise, a remote test needs a little more structure than an in-person one.</p>'
            '<p>The Gartner survey reported by ' + a(GARTNER_FAKE, 'Personnel Today') + ' found that 6% of candidates admitted to interview fraud, either posing as someone else or having someone pose as them. That is a small share, but in a remote process it is enough to justify a few simple habits:</p>'
            '<ul><li><b>Camera on, for the whole test.</b> Explain why at the start. Honest candidates do not mind.</li>'
            '<li><b>Unpredictable follow ups.</b> Ask "why?" and "what happened next?" about their own stories. Prompted answers fall apart on the second follow up.</li>'
            '<li><b>Live writing only.</b> Do the written reply in a shared document while you watch it appear, not as homework.</li>'
            '<li><b>Same person, every round.</b> Check that the voice and face in the final interview match the first screen.</li>'
            '<li><b>A reference from a manager who heard them sell</b>, ideally one who worked with US buyers. Ask whether any buyer ever asked to speak with someone else.</li></ul>'
            '<p>Also check the setup. A good headset, a quiet room and a stable connection change how a candidate sounds more than most people expect. If the audio is poor, ask whether that is the setup they would work with; a buyer will not make allowances for it.</p>'
        )),
        ('first-30-days', 'Confirm the level in the first 30 days', (
            '<p>The test reduces risk, but the first month of real calls confirms the hire. Listen to recorded calls in the first two weeks and score them on the same rubric you used in the interview, so you can see whether the interview level holds on the job.</p>'
            '<p>Most new hires sound a little stiffer on their first real calls than in the roleplay, then improve fast as they learn the product and the common objections. What you are looking for is direction. A rep whose scores rise each week is on track. A rep whose being-understood or listening scores stay low after a few weeks of coaching may be in the wrong seat; an email-first role, for example, can be a better fit than the phone.</p>'
            '<p>A few things speed up the climb:</p>'
            '<ul><li><b>Call reviews twice a week</b>, with one specific thing to change each time.</li>'
            '<li><b>A shared phrase bank</b> of natural openers, objection answers and follow up lines that work for your buyer.</li>'
            '<li><b>Shadowing a strong rep</b> for a few days before going solo.</li></ul>'
            '<p>Our ' + '<a href="/blog/sdr-onboarding-plan">SDR onboarding plan</a>' + ' sets out the full first 30, 60 and 90 days. If you would rather start from candidates who have already been tested this way, our ' + '<a href="/talent">talent team</a>' + ' interviews every bilingual candidate in English and roleplays them on a live call before you meet them.</p>'
        )),
    ],
    'conclusion': (
        '<p>Testing a sales candidate\'s English is not about finding the most native-sounding speaker. It is about finding someone a busy US buyer understands the first time, who listens well, keeps their pace under pressure and writes like a person.</p>'
        '<ol><li><b>Use the CV to decide who to test</b>, not who to hire. AI-written CVs and self-ratings are weak evidence.</li>'
        '<li><b>Measure five skills</b>: being understood, listening, fluency under pressure, tone and writing.</li>'
        '<li><b>Treat certificates as a floor</b>, not a decision. They do not test interruptions or objections.</li>'
        '<li><b>Run a 30 minute live test</b> built around the job, with the roleplay at the center.</li>'
        '<li><b>Score on a shared rubric</b> with minimums per seat, add remote checks, and confirm the level in the first 30 days.</li></ol>'
        '<p>If you want profiles that have already passed a live English roleplay, <a href="/talent">request profiles</a> and tell us the seat and the hours you need covered.</p>'
    ),
    'faq': [
        ('How do I test a sales candidate\'s English?',
         'Run a short live test built around the job: switch into English without warning, ask them to summarize a real sales call, roleplay a cold call with interruptions and a firm no, and have them write a short reply to a buyer email while you watch. Score each skill on a shared rubric.'),
        ('Is a CEFR level or English certificate enough to hire a sales rep?',
         'No. A certificate is a useful floor, but tests like TOEIC Speaking use short, prepared answers with no interruptions or objections. Use it to filter candidates, then decide on a live roleplay.'),
        ('What English level does an SDR need?',
         'It depends on the seat. A cold caller needs to be understood the first time and keep pace under pressure; an email-first SDR needs strong writing. Set a minimum score per skill for each seat before you interview.'),
        ('Does a strong accent mean a candidate will struggle on calls?',
         'Not necessarily. Research by Munro and Derwing shows that accent and intelligibility are partly independent, so speech can be heavily accented and still easy to understand. Judge whether a buyer would follow every sentence, not how native the person sounds.'),
        ('How can I tell if a candidate used AI in a written English test?',
         'Do the written part live. Paste a buyer email into a shared document during the call and watch the reply appear in a few minutes. A polished sample sent from home tells you little now that many CVs are written with AI.'),
        ('How long should an English test for a sales role take?',
         'About 30 minutes covers a warm start, a listening task, a roleplay with coaching and a timed written reply. If you only have ten minutes, keep the roleplay, because it shows English, sales skill and composure together.'),
        ('Does BL Agency test candidates\' English before I meet them?',
         'Yes. Every candidate is interviewed in English by our sales team and roleplayed on a live cold call before they enter our pool, and you get honest notes on where each one is strong. You still interview them yourself before deciding.'),
    ],
}
