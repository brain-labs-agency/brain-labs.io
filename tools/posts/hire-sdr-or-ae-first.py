# Spec for blog/hire-sdr-or-ae-first.html. Build: python3 tools/blogkit.py tools/posts/hire-sdr-or-ae-first.py
EXT = ' target="_blank" rel="noopener"'


def a(href, text):
    return f'<a href="{href}"{EXT}>{text}</a>'


DOVER = 'https://www.dover.com/blog/your-first-sales-hire'
LEMKIN_FIRST = 'https://www.saastr.com/dear-saastr-when-should-i-hire-our-first-sales-person-and-who-should-i-hire'
LEMKIN_AE = 'https://www.saastr.com/dear-saastr-when-should-i-hire-my-first-ae'
LEMKIN_SDRS = 'https://www.saastr.com/closing-deals-founder-hired-2-sdrs-closed-hire-ae-take-sdrs-close-vp-sales'
BLOND = 'https://www.saastr.com/how-to-build-out-your-sdr-function-in-2024-with-sam-blond-partner-at-founders-fund-and-host-of-saastr-cro-confidential/'
BRIDGE25 = 'https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group'
GARTNER_BUYERS = 'https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights'

fig1 = figure(1, table(['', 'SDR (or BDR)', 'Account Executive (AE)'], [
    ['<b>Main job</b>', 'Starts conversations: research, outreach, qualification and handoff.', 'Turns conversations into revenue: discovery, demo, proposal and close.'],
    ['<b>What they need from you</b>', 'A clear ICP, messaging that works, daily coaching and someone to hand meetings to.', 'Proof the product sells, a known sales process and deals to work on or a way to find them.'],
    ['<b>Who manages them</b>', 'Someone who has run outbound and can set activity and meeting goals.', 'The founder at first, then a sales leader once there are two or more.'],
    ['<b>How you measure them</b>', 'Qualified meetings that the closer accepts.', 'Pipeline, win rate and closed revenue.'],
    ['<b>Typical failure mode</b>', 'Books meetings nobody has time to run, or meetings that do not fit.', 'Waits for inbound that never comes, or cannot sell without the founder.'],
]), 'The two roles side by side. The question "SDR or AE first" is really "what is my bottleneck: starting conversations or closing them?"')

fig2 = figure(2, steps('A sales hiring sequence for founder-led companies', [
    ('Founder sells', 'first customers'),
    ('Two AEs', 'they prospect too'),
    ('Prove outbound', 'repeatable source'),
    ('First SDR', 'when AEs are full'),
    ('Sales leader', 'scale what works'),
], accent=('Two AEs',)),
    f'Most guidance converges on this order. Brex, for example, had six AEs before it hired its first SDR, according to {a(BLOND, "Sam Blond on SaaStr")}.')

fig3 = figure(3, table(['Your situation', 'Hire first', 'Why'], [
    ['You close most deals you get, but you are at capacity and selling is taking over your week.', '<b>AE</b>', 'You need a second closer. Pipeline is not the problem; your time is.'],
    ['You have few customers and no repeatable sales process yet.', '<b>Neither yet</b>', 'Keep selling yourself until the pattern is clear. A hire cannot copy a process that does not exist.'],
    ['You close well and have time to close more, but you have too few first meetings.', '<b>SDR (if you can manage one)</b>', 'Your bottleneck is starting conversations, and you stay the closer.'],
    ['You need more meetings and more closing capacity at the same time.', '<b>AE who prospects</b>', 'A full cycle rep covers both until the volume justifies splitting the roles.'],
    ['You have several AEs whose calendars are full of their own prospecting.', '<b>SDR</b>', 'Now the AEs\' time is the expensive part, and an SDR frees it.'],
]), 'A quick way to decide. Find the row that matches where you are today, not where you expect to be in a year.')

POST = {
    'slug': 'hire-sdr-or-ae-first',
    'title': 'Should a founder hire an SDR or an AE first?',
    'h1': 'Should a founder hire an SDR or an <em>AE</em> first?',
    'description': 'Most founders should hire a full cycle AE before an SDR. Here is why, the cases where an SDR comes first, the mistakes that sink early sales hires and a hiring sequence that works.',
    'category': 'Hiring',
    'date': '2026-11-10',
    'date_label': 'November 10, 2026',
    'hero_img': 'cover-hire-sdr-or-ae-first',
    'card_img': 'cover-hire-sdr-or-ae-first',
    'card_title': 'Should a founder hire an SDR or an AE first?',
    'card_text': 'Why most founders should start with a full cycle AE, when an SDR comes first and the hiring order that works.',
    'takeaways': [
        'Most founders should hire a full cycle AE first: someone who finds and closes their own deals. An SDR needs a working sales process and a closer to hand meetings to.',
        'Hire an SDR first only when you close well, have time to close more and your real bottleneck is first meetings, and when someone can coach the SDR every day.',
        'Close the first customers yourself before you hire anyone, and consider hiring two reps instead of one so you can tell whether the person or the process is the problem.',
        'Do not ask an AE to manage SDRs. Closers rarely know how to set SDR goals, and the SDR ends up as an assistant.',
    ],
    'intro': (
        '<p>Every founder who has carried sales alone hits the same point: the calendar is full, the pipeline is thin or both, and it is time to hire. The first question is usually which role. An SDR sounds cheaper and easier to hire, and it promises more meetings. An AE sounds like the "real" sales hire, but it feels like a bigger bet.</p>'
        '<p>This guide answers the question directly, then walks through what each role needs to succeed, the cases where an SDR should come first, the mistakes that sink early sales hires and a hiring sequence you can follow. It ends with what changes when your first rep is hired from Latin America.</p>'
    ),
    'cta': {
        'inline_lead': 'Hiring your first AE or SDR?',
        'inline_text': 'We place vetted bilingual sales professionals from Latin America with US companies. Tell us the role and get three interviewed profiles in 72 hours.',
        'href': '/talent',
        'button': 'Request profiles',
        'band_label': 'Hire sales talent',
        'band_h2': 'Your first sales hire, <em>screened by operators</em>.',
        'band_text': 'Bilingual AEs and SDRs from Latin America who work your US business hours. Every candidate is assessed by people who run revenue operations every day, and you get a short list with an honest note on each person.',
    },
    'sections': [
        ('short-answer', 'The short answer: hire an AE first, in most cases', (
            '<p>Most founders should hire a full cycle Account Executive first: a rep who can prospect for their own deals and close them. An SDR only creates value when there is a proven sales process and someone with time to turn the meetings into revenue, and at most early companies that someone is the overloaded founder.</p>'
            '<p>This is the common advice from people who have built many sales teams. ' + a(DOVER, 'Dover\'s guide to the first sales hire') + ' puts it simply: hire an AE first, because an AE can run the whole cycle while an SDR feeds a motion that already exists. ' + a(BLOND, 'Sam Blond') + ', former CRO of Brex, warns founders against hiring SDRs before outbound works and before someone can manage them, and recommends full cycle AEs who source and close their own deals until then.</p>'
            '<p>The logic is about bottlenecks. An SDR solves "we do not have enough first meetings." An AE solves "we do not have enough people who can turn meetings into customers." In a founder-led company, the second problem almost always comes first, because the founder is doing every demo, every proposal and every follow up.</p>'
                    )),
        ('roles', 'What an SDR and an AE do, and what each one needs', (
            '<p>An SDR starts conversations and an AE turns them into revenue. Each role only works when the company gives it the right inputs, and the inputs an SDR needs are usually the ones an early company has not built yet.</p>'
            + fig1 +
            '<p><b>An SDR needs a lot of structure.</b> They work from a defined ICP, tested messaging and a clear rule for what counts as a qualified meeting. They need daily coaching, especially in the first months, and a closer who accepts the meetings and gives feedback. The ' + a(BRIDGE25, 'Bridge Group 2025 SDR report') + ', based on 351 B2B companies, puts average SDR ramp at 3.0 months and found that only 60% of SDRs hit quota, the lowest share in the study\'s history.</p>'
            '<p><b>An AE needs proof and a process.</b> A good AE can run discovery, handle objections and negotiate, but they cannot invent product market fit. They need evidence that customers buy, a sales process the founder has already walked many times and either deals to work on or the willingness to find their own.</p>'
            '<p><b>The ratio tells you something too.</b> The same Bridge Group report found companies run about one SDR for every 2.4 AEs, a ratio that has held steady since 2018. SDRs are built to feed several closers. With no AE at all, the founder becomes the only closer, and the SDR can quickly produce more meetings than the founder can run.</p>'
        )),
        ('case-for-ae', 'The case for hiring an AE first', (
            '<p>An AE first takes the most expensive work off the founder\'s plate and tests whether someone other than the founder can sell the product. Both matter more early on than adding first meetings.</p>'
            '<p><b>It frees the founder.</b> In most founder-led companies, the founder runs every sales call and also has to build the product, raise money and hire. A full cycle AE takes over whole deals, not just the top of the funnel. Lemkin\'s view is blunt: ' + a(LEMKIN_AE, '"If you\'re doing all the selling and you\'re at capacity, you\'re already behind."') + '</p>'
            '<p><b>It proves the sale is repeatable.</b> A company is only ready to scale sales when someone other than the founder can close, and the first AE is the real test of that.</p>'
            '<p><b>It keeps the person who closes close to the buyer.</b> Buyers do much of their research alone now, but they still want a person at the key moments. ' + a(GARTNER_BUYERS, 'Gartner\'s 2026 buyer survey') + ' found reps remain the most important source when buyers choose a preferred supplier and finalize a purchase. That is AE work.</p>'
            '<p><b>A full cycle AE can still prospect.</b> Hiring an AE first does not mean giving up on outbound. The best early AEs book a good share of their own meetings. Sam Blond\'s advice is that AEs should keep doing outbound "whether it\'s day one or year ten." You get some new pipeline and the closing capacity in the same hire.</p>'
                    )),
        ('case-for-sdr', 'When an SDR first does make sense', (
            '<p>An SDR first makes sense when the founder closes well, has time to close more and the only thing missing is first meetings, and when someone can coach the SDR every day. If all three are true, an SDR can be the right first hire.</p>'
                        '<ul><li><b>The founder is a strong closer with spare capacity.</b> Some founders, often in services or high ticket B2B, have a short cycle and a high win rate but only a few qualified conversations a month. More meetings is the whole problem.</li>'
            
            '<li><b>The ICP and the message are already proven.</b> The founder has booked meetings with outbound before and knows which accounts and messages work. The SDR follows a playbook instead of inventing one.</li>'
            '<li><b>Someone can manage the SDR.</b> Lemkin notes that managing SDRs well ' + a(LEMKIN_SDRS, 'is a skill') + ', and some founders have it. If you do not, a marketing or demand generation lead who has run a small SDR team can fill the gap.</li></ul>'
            '<p>The test is honest arithmetic about time. Count the hours you spend each week on demos, follow ups and proposals. If one more qualified meeting a day would break your week, you need a closer. If you could take it gladly, an SDR may be the faster win.</p>'
            '<p>One more option is worth knowing about. If your bottleneck is first meetings but you are not ready to manage an SDR, an outbound program run for you, such as our Agent Base, can fill the calendar while you keep closing. That lets you hire an AE later with a pipeline already in place.</p>'
        )),
        ('mistakes', 'The mistakes that sink early sales hires', (
            '<p>Most failed first sales hires fail for the same handful of reasons, and almost none of them are about choosing SDR or AE. They are about timing, structure and who manages the new rep.</p>'
            '<p><b>1. Hiring before the founder has sold enough.</b> Lemkin\'s rule of thumb is to ' + a(LEMKIN_FIRST, 'close about 10 customers yourself') + ' before your first sales hire, and in a later post he suggests ' + a(LEMKIN_AE, '10 to 20') + '. You need to know the objections, the buyers and the steps before you can teach them.</p>'
            '<p><b>2. Hiring only one rep.</b> If you hire one rep and it fails, you do not know whether the person or the process was the problem. Lemkin recommends ' + a(LEMKIN_FIRST, 'hiring two') + ' so you can compare.</p>'
            '<p><b>3. Hiring an SDR with no one to manage them.</b> SDRs need daily coaching, call reviews and a steady flow of feedback. An SDR left alone with a sequencing tool and a list usually sends a lot and books little.</p>'
            '<p><b>4. Asking the AE to run the SDRs.</b> It sounds efficient, but Lemkin calls it ' + a(LEMKIN_SDRS, '"the big potential mistake"') + ': most AEs are closers who do not know how to set SDR goals and end up treating SDRs like assistants.</p>'
            '<p><b>5. Hiring a VP of Sales too early.</b> ' + a(DOVER, 'Dover\'s guide') + ' warns that a VP scales an existing process rather than building one from scratch. Your first hire should be someone who sells.</p>'
                    )),
        ('sequence', 'A hiring sequence that works', (
            '<p>A sequence that works for most founder-led B2B companies is: founder sells, then two full cycle AEs, then proof that outbound works, then the first SDR, then a sales leader. Each step creates what the next one needs.</p>'
            + fig2 +
            '<ul><li><b>Founder sells.</b> Close the first customers yourself. Write down the questions buyers ask, the objections and the steps from first call to signature.</li>'
            '<li><b>Two AEs.</b> Hire full cycle reps who prospect and close, and stay close to their calls.</li>'
            '<li><b>Prove outbound.</b> Find out which outbound sources work: which accounts reply, which messages earn meetings and which meetings close. Your AEs, or an outside program, generate this evidence.</li>'
            '<li><b>First SDR.</b> Hire when AEs are spending a large share of their week on prospecting that someone else could do, and when someone is ready to manage the SDR. Sam Blond\'s rule fits here: ' + a(BLOND, '"Only scale when you are encouraged by the numbers."') + '</li>'
            '<li><b>Sales leader.</b> Once several reps are hitting their numbers, hire a leader to scale and manage the team.</li></ul>'
            '<p>To decide where you are today, find your row:</p>'
            + fig3
        )),
        ('latam', 'Hiring your first AE or SDR from Latin America', (
            '<p>Hiring your first AE or SDR from Latin America works well when the rep covers your business hours, sells confidently in English to US buyers and is screened by someone who can judge sales skill, not just a CV. Those are the three things to check, whichever role you hire first.</p>'
            '<p><b>Hours.</b> Latin America sits inside the US business day, so a rep there can cover your Eastern, Central, Mountain or Pacific hours without a night shift. For an AE, that means live discovery calls and demos when your buyers are at their desks. For an SDR, it means calling when prospects pick up.</p>'
            '<p><b>English and selling, tested together.</b> A first sales hire talks to buyers from day one. The screen should include a live roleplay in English, not just a language test, so you hear how they handle an objection or a skeptical buyer in real time.</p>'
            '<p><b>The right profile for the role.</b> A first AE should have run full cycles before, ideally selling something similar to what you sell, and be comfortable prospecting for their own deals. A first SDR should show research habits, resilience on the phone and the discipline to follow a plan, since they will work from your playbook.</p>'
            '<p><b>A short list, not a pile of CVs.</b> At BL Agency we place SDRs, BDRs, AEs, sales operations and customer success professionals with US companies. Every candidate is assessed by people who run revenue operations every day. You get three interviewed profiles in 72 hours, with an honest note on where each person is strong and where they are not, and a 30 day replacement if the fit is wrong.</p>'
                    )),
    ],
    'conclusion': (
        '<p>For most founders, the first sales hire should be a full cycle AE: someone who takes whole deals off your plate and proves that someone other than you can sell. An SDR comes first only when you close well, have time to close more and can coach the SDR every day.</p>'
        '<ol><li><b>Name your bottleneck.</b> Closing capacity points to an AE. First meetings, with spare closing time, point to an SDR.</li>'
        '<li><b>Sell first.</b> Close the first customers yourself and write down how you did it.</li>'
        '<li><b>Hire two if you can.</b> It is the fastest way to learn whether the process or the person is the problem.</li>'
        '<li><b>Give every hire a manager.</b> Do not leave an SDR alone, and do not make an AE run SDRs.</li>'
        '<li><b>Scale on evidence.</b> Add SDRs when AEs are full and outbound is proven.</li></ol>'
        '<p>If you are ready to hire, request profiles and we will send three interviewed candidates for the role you need.</p>'
    ),
    'faq': [
        ('Should my first sales hire be an SDR or an AE?', 'In most cases an AE, ideally one who prospects for their own deals. An SDR needs a proven sales process, daily management and a closer with time for the meetings, which most early companies do not have yet.'),
        ('When should a founder hire the first salesperson?', 'Most guidance says after you have closed the first customers yourself. Jason Lemkin suggests ' + a(LEMKIN_FIRST, 'about 10') + ', and the clearest sign is that selling is now the bottleneck on your time.'),
        ('Can an SDR work without an AE?', 'Yes, if the founder closes the deals and has the time and skill to manage the SDR. Without both, the SDR tends to book meetings nobody can run well.'),
        ('Should I hire one sales rep or two?', 'Two if you can. With two reps you can compare results and tell whether a problem comes from the person or from the process.'),
        ('Can my AE manage the SDRs?', 'It is usually a mistake. Most AEs are closers who do not know how to set SDR goals, so it is better for the founder or a demand generation lead to manage them until you hire a sales leader.'),
        ('What is the difference between an SDR and a BDR?', 'Both start conversations and hand qualified meetings to a closer. Companies often use SDR for inbound follow up and BDR for outbound prospecting, but many use the titles interchangeably.'),
        ('Can I hire my first AE or SDR from Latin America?', 'Yes. Reps in Latin America work inside the US business day, and many have sold to US buyers in English. <a href="/talent">Request profiles</a> and we will send three interviewed candidates in 72 hours.'),
    ],
}
