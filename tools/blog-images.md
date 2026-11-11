# Blog image registry

Rule: every blog post gets its own image. Never reuse an image another post or page already uses.
Never use page heroes or section images (hero-*.jpg, part-*.jpg) in posts.

## In use
| Image | Used by |
|---|---|
| blog-hiring | blog/hire-bilingual-sdr-latin-america |
| blog-ai | blog/ai-sdr-vs-human-sdr |
| blog-sdr | blog/sdr-as-a-service |
| blog-native-english | blog/native-english-sales-team-latin-america |
| blog-signal | blog/hire-bilingual-cold-callers-latin-america |
| blog-cost | blog/lead-generation-staffing-recruitment-agencies |
| cover-sdr-interview-process | blog/sdr-interview-process (branded cover) |
| cover-outsourced-sdr-vs-in-house-sdr | blog/outsourced-sdr-vs-in-house-sdr (branded cover) |
| cover-sdr-onboarding-plan | blog/sdr-onboarding-plan (branded cover) |
| cover-are-ai-sdrs-worth-it | blog/are-ai-sdrs-worth-it (branded cover) |
| cover-hire-sdr-or-ae-first | blog/hire-sdr-or-ae-first (branded cover) |
| hero-blog | /blog index hero only |

## Available (unused)
| Image | What it shows | Good for |
|---|---|---|
| blog-email | Person typing an email at a sunny desk with a plant | Cold email, deliverability, reply rates |

## Photo stock (Gemini batches)
Vero and Claude generate a batch of 6 to 8 photos about once a week, for the next topics in the backlog. Each photo is reserved for one topic.
When drafting a post: if its topic has a reserved photo here, use it and move it to "In use". If not, use an "Available" image that fits, else build a branded cover.

| Image | Reserved for backlog # | Topic |
|---|---|---|
| blog-email | 18 | Why are my cold emails going to spam? |
| blog-appointment-setting | 14 | B2B appointment setting companies in the USA: how to choose one (US founder smiling at a monitor with a full calendar of booked meetings) |
| blog-sdr-program-fails | 15 | Why outsourced SDR programs fail (and how to spot it in month one) (Sales manager frowning at a pipeline report, crossed-out sticky notes behind her) |
| blog-ai-agents-sales | 16 | AI agents for sales teams: what they do well and where a human still decides (Latin American rep reviewing a draft email on a laptop with a pen) |
| blog-signal-outbound | 19 | Signal-based outbound: start where the buyer can be reached (Over-the-shoulder rep at a laptop with a company news feed, headset on the desk) |
| blog-human-review | 20 | Human in the loop: why every AI-written email needs a reviewer (Two colleagues editing an email together on one laptop) |
| blog-outbound-services | 21 | Outbound lead generation services: what is included and what to ask (Team of three planning a campaign, funnel drawn on a whiteboard) |
| blog-agent-office | 23 | AI agent offices: what the visual agent trend means for sales teams (Woman smiling at her monitor showing an Agent Base style dashboard: 3D hex-tile base on orange sand, evening) |
| blog-agent-dashboard | 24 | Can you see your AI SDR working? Why outbound agents shouldn't be a black box (Sales ops lead with arms crossed in front of an activity dashboard) |

## When nothing fits or the list is empty
Do not reuse. Build a branded cover instead: 1600x900, background gradient #0d4747 to #061f20, the post category in small caps (#efbf6e), a short headline (Fraunces style serif, #f6f1e7), and one simple chart or number motif in amber. Render an HTML page with Playwright (Chromium is pre-installed) to img/cover-<slug>.jpg (quality 85) plus a .webp, then add it to "In use" above.
