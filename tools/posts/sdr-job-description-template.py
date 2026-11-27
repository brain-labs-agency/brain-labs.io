# Spec for blog/sdr-job-description-template.html. Build: python3 tools/blogkit.py tools/posts/sdr-job-description-template.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


MONSTER = 'https://hiring.monster.com/resources/blog/job-posting-red-flags-are-turning-candidates-away/'
BUILTIN = 'https://builtin.com/articles/sales-development-representative-job-description'
TOPTAL = 'https://www.toptal.com/sales/sales-development-representatives/job-description'
WORKABLE = 'https://resources.workable.com/sales-development-representative-job-description'
BRIDGE = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'

fig1 = figure(1, bar_chart('Share of job seekers who say each problem discourages them from applying', [
    ('Unclear job description', 51),
    ('Unrealistic requirements', 46),
    ('Long application process', 45),
], unit='%', vmax=60, highlight=('Unclear job description',)),
    'Three of the most common reasons candidates skip a job posting, all of which the job description controls. Source: '
    + a(MONSTER, 'Monster, Job Search Deal-Breakers Report') + '.')

fig2 = figure(2, table(['Vague bullet', 'Specific bullet', 'Why it works better'], [
    ['Generate leads for the sales team', 'Book qualified meetings with operations leaders at US staffing companies for our two account executives', 'Names the buyer, the outcome and who the SDR supports'],
    ['Make outbound calls and send emails', 'Run daily outreach by phone, email and LinkedIn, following sequences you help improve', 'Shows the channels and invites ownership'],
    ['Hit your targets', 'Hold a monthly target of qualified meetings, defined in writing, ramped over your first three months', 'Sets a fair, measurable goal with a ramp'],
    ['Use our CRM', 'Keep every touch and next step in HubSpot the same day', 'Names the tool and the standard'],
    ['Excellent communication skills', 'Hold a natural phone conversation in English with a US buyer who is busy and skeptical', 'Describes the real test, not an adjective'],
]), 'Rewriting common SDR job description bullets. Specific bullets attract candidates who can picture the job and help the wrong ones opt out early.')

fig3 = figure(3, steps('From job description to first day', [
    ('Publish', 'clear JD, short form'),
    ('Screen', '20 min call in English'),
    ('Roleplay', 'live cold call'),
    ('Check', 'references and setup'),
    ('Start', '30 60 90 day plan'),
], accent=('Roleplay',)),
    'The job description is step one of a short process. Each later step tests something the job description promised, so write it with the interview in mind.')

TEMPLATE_BLOCK = (
    '<div class="callout">'
    '<p style="font-size:1.1em"><b>Sales Development Representative (remote, US Eastern hours)</b></p>'
    '<p style="margin-top:18px"><b>About us.</b> [Company] helps [type of customer] [solve which problem]. We sell to [buyer role] at [company type and size] in the United States. Our team is [size], and you will work with [names or roles of the account executives or founder].</p>'
    '<p style="margin-top:18px"><b>The role.</b> You will start conversations with companies that fit our ideal customer and book qualified meetings for our account executives. You will not close deals. Your success is measured by qualified meetings held and the pipeline they create.</p>'
    '<p style="margin-top:18px"><b>What you will do</b></p>'
    '<ul><li>Research target accounts and find the right person to contact at each one.</li>'
    '<li>Run outreach by phone, email and LinkedIn, following and improving our sequences.</li>'
    '<li>Qualify prospects against our written definition of a qualified meeting.</li>'
    '<li>Book meetings and hand each one to the account executive with a short note: who they are, why they agreed and what to ask.</li>'
    '<li>Keep every touch and next step in [CRM] the same day.</li>'
    '<li>Share what you hear from prospects in a weekly review, so we can improve the message.</li></ul>'
    '<p style="margin-top:18px"><b>What success looks like</b></p>'
    '<ul><li>First 30 days: you know our product, buyer and tools, and you have started outreach.</li>'
    '<li>By 90 days: you are booking qualified meetings at your full monthly target.</li></ul>'
    '<p style="margin-top:18px"><b>What you need</b></p>'
    '<ul><li>Advanced spoken and written English. You can hold a natural call with a busy US buyer.</li>'
    '<li>[0 to 2] years in sales development, inside sales, customer service or another role with daily conversations.</li>'
    '<li>Comfort with rejection and the discipline to do the same work well every day.</li>'
    '<li>Availability for [9am to 5pm] US Eastern time, Monday to Friday.</li>'
    '<li>A quiet workspace and a reliable internet connection.</li></ul>'
    '<p style="margin-top:18px"><b>Nice to have</b></p>'
    '<ul><li>Experience selling to US companies.</li>'
    '<li>Experience with [CRM] and a sales engagement tool.</li>'
    '<li>Knowledge of [your industry].</li></ul>'
    '<p style="margin-top:18px"><b>How we work.</b> [Engagement model: contractor, direct hire or through an employer of record]. [Equipment you provide]. [Local holidays policy]. Compensation is [base plus variable], paid in [currency]; we explain the full structure in the first call.</p>'
    '<p style="margin-top:18px"><b>How to apply.</b> Send your CV and a two minute voice note in English telling us why this role. Our process is a 20 minute call, a short cold call roleplay and a final conversation.</p>'
    '</div>'
)

POST = {
    'slug': 'sdr-job-description-template',
    'title': 'SDR job description template for US companies hiring in Latin America',
    'h1': 'SDR job description <em>template</em> for US companies hiring in Latin America',
    'description': 'A copy and paste SDR job description template for US B2B companies hiring in Latin America, with how to write responsibilities, requirements and the details remote candidates look for.',
    'category': 'Hiring',
    'date': '2026-11-27',
    'date_label': 'November 27, 2026',
    'hero_img': 'cover-sdr-job-description-template',
    'card_img': 'cover-sdr-job-description-template',
    'card_title': 'SDR job description template for US companies hiring in Latin America',
    'card_text': 'A ready to use template, plus how to write responsibilities and requirements that attract strong bilingual SDRs and filter out the rest.',
    'takeaways': [
        'A good SDR job description names the buyer, the outcome and how success is measured. Vague postings attract many applicants and few good ones.',
        'Unclear descriptions and unrealistic requirements are two of the top reasons candidates do not apply, according to Monster\'s survey of job seekers.',
        'When hiring in Latin America, state the working hours in US Eastern time, the English level, the engagement model and how you will test the candidate.',
        'Keep must-haves short. Separate them from nice-to-haves, and replace adjectives like "excellent communicator" with the real test the candidate will face.',
    ],
    'intro': (
        '<p>The job description is the first sales pitch your new SDR will ever hear from you. Strong candidates read it the way a buyer reads a cold email: is this specific, is it real, and is it for me? A generic posting copied from a template site gets generic applicants. A clear one attracts people who can picture the job and quietly turns away the ones who would not last.</p>'
        '<p>This guide gives you a complete SDR job description template you can copy, written for US B2B companies hiring bilingual SDRs in Latin America. It then walks through how to write each part, what changes when the role is remote and cross-border, and the mistakes that cost you good candidates.</p>'
    ),
    'cta': {
        'inline_lead': 'Rather skip the job post?',
        'inline_text': 'Tell us who you sell to and the hours you need covered. We come back with three bilingual SDR profiles from Latin America within 72 hours, already interviewed in English and tested on a live cold call roleplay.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Skip the posting. Meet <em>three</em> SDRs this week.',
        'band_text': 'Vetted bilingual SDRs, account executives, sales ops and customer success professionals from Latin America, screened by people who run outbound every day. Profiles in 72 hours, replacement in the first 30 days.',
    },
    'sections': [
        ('what-it-should-do', 'What an SDR job description needs to do', (
            '<p>An SDR job description has two jobs: attract candidates who can do the work, and help the wrong candidates decide not to apply. It does both by being specific about the buyer, the outcome, the measure of success and the working conditions.</p>'
            '<p>Most SDR postings fail the second job. They list every skill a salesperson could have, describe the role in adjectives and leave out the details a candidate actually needs to decide. The result is a large pile of applications and a long screening process.</p>'
            '<p>Candidates notice. In ' + a(MONSTER, 'Monster\'s Job Search Deal-Breakers Report') + ', 51% of job seekers said unclear job descriptions discourage them from applying, and 46% said the same about unrealistic requirements, such as "entry-level" roles that ask for years of experience.</p>'
            + fig1 +
            '<p>Every bar in that chart is something you control. A clear description, realistic requirements and a short application process cost nothing and widen the pool of good candidates.</p>'
            '<p>Before you write, answer four questions for yourself:</p>'
            '<ul><li><b>Who will the SDR contact?</b> The buyer role, company type and market.</li>'
            '<li><b>What is the outcome?</b> Usually qualified meetings for account executives or the founder.</li>'
            '<li><b>How will you measure it?</b> What counts as a qualified meeting, and over what ramp.</li>'
            '<li><b>Who will manage them?</b> Name the role. Candidates care a great deal about who will coach them.</li></ul>'
            '<p>If you cannot answer these yet, the job description is not the problem. Our guide on <a href="/blog/hire-sdr-or-ae-first">whether to hire an SDR or an AE first</a> can help you decide whether this is the right hire.</p>'
        )),
        ('template', 'The SDR job description template', (
            '<p>Below is a complete SDR job description template for a remote, bilingual role working US hours. Copy it, replace everything in square brackets and cut anything that does not apply to your team.</p>'
            + TEMPLATE_BLOCK +
            '<p>A few notes on the choices in this template:</p>'
            '<ul><li><b>"You will not close deals."</b> Saying this up front prevents the most common mismatch: candidates who want to be account executives and leave when they find out.</li>'
            '<li><b>A 30 and 90 day picture.</b> It tells candidates there is a ramp and a plan, which strong candidates look for.</li>'
            '<li><b>A voice note instead of a cover letter.</b> For a role that lives on the phone, two minutes of spoken English tells you more than a page of writing, and it takes the candidate less time.</li>'
            '<li><b>The process in the posting.</b> Telling candidates there is a 20 minute call and a roleplay sets expectations and filters out people who are not ready to sell live.</li></ul>'
            '<p>The rest of this guide explains how to adapt each part.</p>'
        )),
        ('responsibilities', 'How to write the responsibilities', (
            '<p>Write responsibilities as outcomes and specific actions, not as general duties. "Book qualified meetings with operations leaders at US staffing companies" tells a candidate far more than "generate leads."</p>'
            '<p>Most templates online, such as ' + a(WORKABLE, 'Workable\'s') + ' and ' + a(TOPTAL, 'Toptal\'s') + ', list ten or more responsibilities. That is fine as a starting point, but the best postings cut the list to five or six bullets that describe a real day. Each bullet should answer one of these: who the SDR contacts, through which channels, toward what outcome, with which tools, and how they hand off.</p>'
            + fig2 +
            '<p>Three details matter more than the rest:</p>'
            '<ul><li><b>The buyer.</b> Naming the buyer role and industry helps candidates with relevant experience recognize themselves, and it signals that you know your market.</li>'
            '<li><b>The channels.</b> Phone, email, LinkedIn or all three. A candidate who hates the phone should know before applying if calling is half the job.</li>'
            '<li><b>The target.</b> Say that there is a monthly target of qualified meetings and a ramp, even if you do not publish the number. The ' + a(BRIDGE, 'Bridge Group\'s 2025 report') + ' puts average SDR ramp at about three months, so a target that starts on day one is a red flag to experienced candidates.</li></ul>'
            '<p>Avoid publishing activity quotas such as a set number of calls per day in the posting. They describe inputs, not results, and they make the role sound like a call center rather than a sales job. Discuss activity expectations in the interview, where you can explain the reasoning.</p>'
        )),
        ('requirements', 'How to write the requirements', (
            '<p>Keep must-have requirements to four or five, and move everything else to a separate "nice to have" list. Long requirement lists discourage good candidates who meet most but not all of them, and they rarely filter out weak ones.</p>'
            '<p>For an SDR, the must-haves are usually:</p>'
            '<ul><li><b>Language.</b> For US buyers, advanced spoken English. Describe it as a situation ("hold a natural call with a busy US buyer") rather than a test score.</li>'
            '<li><b>Experience.</b> Many SDR roles are entry level. ' + a(TOPTAL, 'Toptal\'s template') + ' notes that a junior SDR may have zero to two years of experience, and ' + a(BUILTIN, 'Built In') + ' describes the role as typically entry level. Customer service, hospitality and recruiting experience often transfer well.</li>'
            '<li><b>Resilience.</b> Most outreach gets no reply or a no. Say so honestly.</li>'
            '<li><b>Availability.</b> The hours, stated in the time zone your buyers are in.</li></ul>'
            '<p>On education, be careful. Both ' + a(TOPTAL, 'Toptal') + ' and ' + a(BUILTIN, 'Built In') + ' treat a bachelor\'s degree as preferred rather than required for SDRs. Unless a degree really matters for your buyers, leave it out or list it as a nice to have. It narrows your pool without telling you much about how someone performs on the phone.</p>'
            '<p>Replace adjectives with observable behavior wherever you can:</p>'
            '<ul><li>Instead of "excellent communication skills," write "can explain our product in two sentences to someone who did not ask."</li>'
            '<li>Instead of "self-starter," write "plans their own day and follows up without being reminded."</li>'
            '<li>Instead of "coachable," write "takes feedback from call reviews and applies it the next day."</li></ul>'
            '<p>These rewrites also give you your interview questions. If the posting promises a candidate will hold a natural call in English, the interview should include one.</p>'
        )),
        ('latin-america', 'What to add when hiring in Latin America', (
            '<p>When the role is remote and based in Latin America, add five details a domestic posting often leaves out: the working hours in US time, the English level and how you will test it, the engagement model, the equipment and connectivity you expect, and how local holidays work.</p>'
            '<ul><li><b>Hours in US time.</b> Write "9am to 5pm US Eastern" rather than "US business hours." Reps in Bogotá and Lima work on Eastern time for most of the year, while Mexico City is an hour behind, so a precise window avoids confusion. ' + a(TOPTAL, 'Toptal') + ' also recommends mentioning office hours and remote work options in the posting.</li>'
            '<li><b>English, tested live.</b> Say that part of the interview will be in English and include a short roleplay. It attracts confident speakers and saves everyone time. Our guide on <a href="/blog/native-english-sales-team-latin-america">building a native-level English sales team</a> explains what to listen for.</li>'
            '<li><b>Engagement model.</b> Contractor, direct hire through a local entity or an employer of record. Candidates in the region compare offers partly on this, so be clear.</li>'
            '<li><b>Equipment and connectivity.</b> Say whether you provide a laptop and headset and what internet connection you expect. Call quality is part of the job.</li>'
            '<li><b>Holidays and schedule.</b> Say whether the rep follows local holidays, US holidays or a mix. Both are common; the problem is not saying.</li></ul>'
            '<p>On compensation, explain the structure, such as base plus variable, the currency and how commission is calculated, and check with your advisors whether the location of the role triggers any pay transparency rules. Candidates want to understand how they will be paid before they invest time in your process.</p>'
            '<p>If you are still choosing a country, our guide on <a href="/blog/hire-sales-reps-colombia-argentina-mexico">hiring sales reps in Colombia, Argentina or Mexico</a> compares the main options.</p>'
        )),
        ('mistakes', 'Mistakes that cost you good candidates', (
            '<p>The mistakes that cost the most good SDR candidates are vague responsibilities, inflated requirements, hidden working hours, unclear targets and a slow or complicated application. Each one is easy to fix in the posting itself.</p>'
            '<ul><li><b>Copying a generic template unchanged.</b> Candidates see dozens of identical postings a week. Specific details about your buyer and team are what make yours stand out.</li>'
            '<li><b>Entry-level title, senior requirements.</b> Asking for years of experience for a junior role is one of the deal-breakers in Monster\'s survey. Decide which you are hiring and write for that.</li>'
            '<li><b>Hiding the hours.</b> For a cross-border role, the schedule is often the first thing candidates check.</li>'
            '<li><b>No mention of a manager.</b> SDRs who are coached stay and improve. Naming who they will work with tells candidates the role has support.</li>'
            '<li><b>A long application.</b> ' + a(MONSTER, 'Monster found') + ' 45% of job seekers say long or complicated application processes reduce their likelihood of applying. A CV and a short voice note is enough for a first filter.</li>'
            '<li><b>Promising what the role is not.</b> If the job is mostly cold calling, say so. Candidates who discover it in week two leave in week four.</li></ul>'
            '<p>One more check before you publish: read the posting out loud as if you were a strong SDR with two other offers. Would you know exactly what the job is, who you would work with and how you would be measured? If not, keep editing.</p>'
        )),
        ('after-posting', 'From job description to hire', (
            '<p>The job description is the first step of a short process: publish, screen in a 20 minute call, run a live roleplay, check references and set up, then start with a 30, 60 and 90 day plan. Each step should test something the posting promised.</p>'
            + fig3 +
            '<p><b>Screen.</b> A short call, partly in English, tells you most of what the CV cannot: how the candidate sounds, how they handle a surprise question and whether they understood the role. Our <a href="/blog/sdr-interview-process">20 minute SDR interview</a> shows a structure you can run in one call.</p>'
            '<p><b>Roleplay.</b> Give the candidate a short brief on your buyer and run a five minute cold call where you play a skeptical prospect. You will learn more from how they handle a "not interested" than from any question about past results.</p>'
            '<p><b>Check and set up.</b> Speak to a recent manager if you can, and make sure equipment, accounts and tools are ready before day one.</p>'
            '<p><b>Start with a plan.</b> The first weeks decide whether the hire works. Our <a href="/blog/sdr-onboarding-plan">SDR onboarding plan</a> gives a structure for the first 30, 60 and 90 days, and the template above already sets those expectations.</p>'
            '<p>If you would rather not run this process yourself, our <a href="/talent">talent team</a> does the sourcing, the English interview and the roleplay, and sends three profiles within 72 hours.</p>'
        )),
    ],
    'conclusion': (
        '<p>A good SDR job description is short, specific and honest. It tells strong candidates exactly what the job is, and it helps the wrong ones decide not to apply before you spend time screening them.</p>'
        '<p>To recap:</p>'
        '<ol><li><b>Answer four questions first.</b> The buyer, the outcome, the measure and the manager.</li>'
        '<li><b>Start from the template.</b> Replace every bracket and cut what does not apply.</li>'
        '<li><b>Write outcomes, not duties.</b> Name the buyer, the channels, the target and the tools.</li>'
        '<li><b>Keep must-haves short.</b> Language, experience, resilience and availability. Move the rest to nice to have.</li>'
        '<li><b>Add the cross-border details.</b> Hours in US Eastern time, how English is tested, the engagement model, equipment and holidays.</li>'
        '<li><b>Test what you promised.</b> A short screen, a live roleplay and a structured onboarding.</li></ol>'
        '<p>If you want to skip the posting and start interviewing, <a href="/talent">tell us about the role</a>. We will send three bilingual SDR profiles from Latin America within 72 hours.</p>'
    ),
    'faq': [
        ('What should an SDR job description include?',
         'The buyer the SDR will contact, the outcome expected (usually qualified meetings), how success is measured, the main responsibilities, a short list of must-have requirements, the working hours, the engagement model and the hiring process.'),
        ('How long should an SDR job description be?',
         'Long enough to answer what the job is, who it is for and how it is measured, and no longer. Five or six responsibilities and four or five must-have requirements are usually enough.'),
        ('Does an SDR need a degree?',
         'Usually not. Templates from Toptal and Built In treat a bachelor\'s degree as preferred rather than required. Spoken English, resilience and the ability to hold a real conversation predict success better.'),
        ('Should I include the meeting quota in the posting?',
         'Say that there is a monthly target of qualified meetings and a ramp period. The exact number is better discussed in the interview, together with your definition of a qualified meeting.'),
        ('How do I describe the English level for a Latin American SDR?',
         'Describe the situation the rep will face, such as holding a natural phone call with a busy US buyer, and say that part of the interview will be in English with a short roleplay.'),
        ('What is the difference between an SDR and a BDR job description?',
         'Often very little. Many companies use the titles interchangeably. Where they differ, SDR roles lean toward inbound leads and BDR roles toward outbound prospecting. Describe the actual work rather than relying on the title.'),
        ('How quickly can I hire an SDR in Latin America?',
         'Running your own posting and interviews usually takes several weeks. Through BL Agency\'s <a href="/talent">talent service</a>, you receive three interviewed profiles within 72 hours.'),
    ],
}
