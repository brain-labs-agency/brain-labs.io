# brain-labs.io blog backlog (researched Nov 2, 2026)

How this list was built:
- **GSC**: Google Search Console queries brain-labs.io already gets impressions for (Aug 1 to Oct 31, 2026).
- **Bing**: Bing Webmaster keyword research, global impressions Aug 2 to Oct 30, 2026. Bing is a small slice of search, so niche B2B terms often show 0; read these numbers as a relative signal, not total demand.
- **AC**: phrases Google autocomplete suggests (US, English). Autocomplete only shows phrases people actually type, so it confirms that the question exists.
- **Community**: threads on Reddit, Bravado and SaaStr where buyers ask this.
- **AI-cited**: the kind of page ChatGPT and Perplexity cite for the query, which is mostly buyer guides, "questions to ask" lists and comparisons. Write to answer the question in the first 2 sentences of each section.

Rules: no prices, no rates, no salaries (see the blog plan). No em dashes. Never reuse an image (see tools/blog-images.md). Long form per tools/blogkit.py.

Service tags:
- **AB**: Agent Base (outbound done for you).
- **T**: Hire sales talent.

Priority:
- **A**: write first.
- **B**: next.
- **C**: fill.

Status values:
- `todo`
- `draft` (on a preview branch)
- `live`

Order: work top to bottom. Each weekday, pick the 2 highest `todo` rows, preferably one AB and one T when both are available.

Update Nov 2 (evening):
- Market check: Google autocomplete is US/English. Bing numbers are global, and the US is the largest country for every term (examples: "what is an sdr" US 339 of 436; "cold calling" US 1,347 of 2,834; "appointment setter" US 545 of 1,280; "ai sdr" US 64 of 219).
- Added 16 topics: ICP verticals (staffing, SaaS, consulting, coaching), problem searches (book more meetings, pipeline generation), category terms (appointment setting companies, outbound lead generation services, fractional SDR, GTM agency, AI agents for sales) and the visual-agent trend.

| # | Working title | Real question people ask | Demand signal | Service | Pri | Status |
|---|---|---|---|---|---|---|
| 1 | How to hire a bilingual SDR from Latin America | "hire sales talent in latin america" | GSC 17 impr | T | A | live |
| 2 | AI SDR vs human SDR: which one books meetings that close? | "ai sdr vs human sdr" | AC; Bing "ai sdr" 219 | AB | A | live |
| 3 | Building a native-level English sales team from Latin America | "native speaking sales team" | GSC 29 impr (top query) | T | A | live |
| 4 | What is SDR as a Service? (upgrade the short post to long form) | "sdr as a service meaning / model / companies" | AC | AB | A | live |
| 5 | Where to hire bilingual LatAm cold callers for US B2B outbound | "where can i hire bilingual latam cold callers experienced in us b2b outbound" | GSC 22 impr | T | A | live |
| 6 | Lead generation for staffing and recruitment agencies: what works in 2026 | "lead generation for staffing companies", "how to get clients for recruitment agency" | AC; core ICP (staffing) | AB | A | live |
| 7 | Outsourced SDR vs in-house SDR: what actually works | "outsourced sdr vs hiring in-house what actually works better" | Reddit thread; AC "outsourced sdr reddit" | AB | A | live |
| 8 | How to interview an SDR: the 20-minute screen | "sdr interview process" | AC | T | A | live |
| 9 | Lead generation for SaaS companies: outbound that books demos | "lead generation for saas companies" | AC; core ICP (SaaS) | AB | A | todo |
| 10 | Are AI SDRs worth it? What happened to fully autonomous AI SDRs | "are ai sdrs worth it", "ai sdr review", "ai sdr reddit" | AC; Reddit churn threads | AB | A | live |
| 11 | SDR onboarding plan: the first 30, 60 and 90 days | "sdr onboarding plan" | AC | T | A | live |
| 12 | 12 questions to ask an outsourced SDR agency before you sign | "questions to ask outsourced sdr agency" | AI-cited format (Belkins, Danish Lead Co rank) | AB | A | draft |
| 13 | Hiring sales reps in Colombia, Argentina or Mexico: how to choose | "hire sales reps latin america" by country | Near data: Colombia now top LatAm hiring market; EF EPI | T | A | todo |
| 14 | B2B appointment setting companies in the USA: how to choose one | "b2b appointment setting companies in usa", "appointment setting for b2b" | AC; AI-cited format | AB | A | todo |
| 15 | Why outsourced SDR programs fail (and how to spot it in month one) | "outsourced sdrs don't work" | SaaStr "only 7%" piece; Reddit | AB | A | todo |
| 16 | AI agents for sales teams: what they do well and where a human still decides | "ai agents for sales teams", "ai agent for lead generation" | AC; Bing "ai sales agent" 126 | AB | A | todo |
| 17 | Should a founder hire an SDR or an AE first? | "should i hire an sdr or ae first" | Many 2026 posts; founder threads | AB + T | A | live |
| 18 | Why are my cold emails going to spam? | "why are my cold emails going to spam" | AC | AB | A | todo |
| 19 | Signal-based outbound: start where the buyer can be reached | "signal based selling", "signal based outbound" | AC | AB | A | todo |
| 20 | Human in the loop: why every AI-written email needs a reviewer | "ai sdr" plus "human review" angle | Hybrid model is the 2026 consensus | AB | A | todo |
| 21 | Outbound lead generation services: what is included and what to ask | "outbound lead generation services / agency / tools" | AC | AB | A | todo |
| 22 | Nearshore vs offshore sales teams: what changes for US buyers | "what is considered nearshore", "inshore vs nearshore" | AC | T | B | draft |
| 23 | AI agent offices: what the visual agent trend means for sales teams | "ai agent office", "pixel agents" | Social trend; dev tools like Pixel Agents and AI Office | AB | B | todo |
| 24 | Can you see your AI SDR working? Why outbound agents shouldn't be a black box | "ai agents visualized" trend; AI SDR churn complaints | Social trend (pixel agent offices); pairs with the LinkedIn video | AB | B | todo |
| 25 | Why are my cold emails not working? A diagnostic | "why are my cold emails not working" | AC | AB | B | todo |
| 26 | What is an AI SDR, and what it can't do yet | "ai sdr meaning", "what is ai sdr agent" | AC; Bing "ai sdr" 219 | AB | B | todo |
| 27 | How to test a sales candidate's English (beyond the CV) | "english test for sales reps" | Supports GSC native-speaker query | T | B | todo |
| 28 | When to stop founder-led sales and bring in outbound help | "when to hire first sdr" | Founder threads; SignalFire, SaaStr | AB | B | todo |
| 29 | What counts as a qualified meeting? Define it before launch | "what is a qualified meeting" | Buyer guides say most agency disputes are definition disputes | AB | B | todo |
| 30 | Lead generation for consulting firms and high-ticket services | "lead generation for consulting companies / business consultants" | AC; ICP | AB | B | todo |
| 31 | SDR ramp time: how long until a new rep books meetings | "sdr ramp time" | AC | T | B | todo |
| 32 | Fractional SDR: what it is and when it makes sense | "fractional sdr meaning", "fractional sdr reddit" | AC | T | B | todo |
| 33 | Cold email reply rate benchmarks (and what moves them) | "cold email reply rate average / benchmark" | AC (rates only, no money) | AB | B | todo |
| 34 | Outsourced SDR vs appointment setting vs lead gen agency | "lead generation agency meaning", "appointment setting companies" | AC; Bing "lead generation agency" 165 | AB | B | todo |
| 35 | How many meetings should an SDR book per month? | "how many meetings should an sdr book" | AC | T | B | todo |
| 36 | How to book more sales meetings without adding headcount | "how to book more sales meetings", "how to get more sales meetings" | AC | AB | B | todo |
| 37 | SDR vs BDR: the difference and which one you need | "sdr vs bdr" | AC; Bing "bdr" 10K (noisy) | T | B | todo |
| 38 | Cold calling in 2026: does it still work for B2B? | "what is cold calling", "cold calling meaning" | Bing "cold calling" 2,834, "what is cold calling" 1,021 | T | B | todo |
| 39 | Hiring appointment setters: what to look for and what to avoid | "hire appointment setters", "hire appointment setters reddit" | AC; Bing "appointment setter" US 545 | T | B | todo |
| 40 | AI cold calling agents: what they can and can't do | "ai cold calling agent / software" | AC | AB | B | todo |
| 41 | Hiring a remote SDR: what to change in your process | "hire remote sdr" | AC | T | B | todo |
| 42 | Pipeline generation strategy for small sales teams | "pipeline generation strategy", "pipeline generation ai" | AC | AB | B | todo |
| 43 | Bilingual sales reps for Spanish-speaking US markets | "bilingual sdr", "bilingual sales jobs" | AC | T | B | todo |
| 44 | Sales staff augmentation: adding reps without a long hiring cycle | "staff augmentation companies" (sales) | AC | T | B | todo |
| 45 | Account research before the first email: what to look for | "how to research accounts for outbound" | Supports Agent Base (Scout and Lens) | AB | B | todo |
| 46 | Why AI SDRs struggle with niche ICPs and small markets | "ai sdr niche b2b" | Review sites: tools shine only with large TAMs | AB | B | todo |
| 47 | What is an SDR? The role explained for founders | "what is an sdr", "sdr meaning sales" | Bing 436 + 440 | T | C | todo |
| 48 | Outbound sales in 2026: how it works now | "outbound sales" | Bing 284 | AB | C | todo |
| 49 | Lead generation for coaching and high-ticket programs | "lead generation for coaching business" | AC; ICP (high-ticket coaching) | AB | C | todo |
| 50 | What is a GTM agency, and do you need one? | "gtm agency meaning", "gtm agency reddit" | AC | AB | C | todo |
| 51 | Appointment setting services: what you get and what to check | "appointment setting services / companies" | AC; Bing "appointment setter" 1,280 (mostly job seekers) | AB | C | todo |
| 52 | SDR job description template for US companies hiring in LatAm | "sdr job description", "appointment setter job description" | Bing 113 | T | C | todo |
| 53 | LinkedIn outreach that gets replies | "linkedin outreach" | Bing 63 | AB | C | todo |
| 54 | Clay agency vs outbound agency: what each one delivers | "clay agency reddit" | AC | AB | C | todo |
| 55 | Building a sales pipeline from zero | "sales pipeline" | Bing 1,107 (broad) | AB | C | todo |
| 56 | Hiring through an agency, directly, or through an EOR | "how to hire sales reps in latin america" | Near and South guides | T | C | todo |

## High-demand topics left out by the no-prices rule
These have strong intent, but answering them means quoting figures:
- "how much does an sdr cost" / "outsourced sdr cost" (AC)
- "sdr salary" (AC)
- "cost to hire sales reps in latin america"

Revisit only if Vero changes the rule.

## Images: one per post, never reused
Follow tools/blog-images.md. Each post gets an image no other post or page uses.
Never use page heroes or section images (hero-*, part-*).
Take an image from "Available" in tools/blog-images.md if it fits the topic; otherwise build a branded cover as described there.
Move the image to "In use" with the post slug, in the same commit as the post.
