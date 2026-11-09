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
| cover-lead-generation-saas-companies | blog/lead-generation-saas-companies (branded cover) |
| cover-hire-sales-reps-colombia-argentina-mexico | blog/hire-sales-reps-colombia-argentina-mexico (branded cover) |
| hero-blog | /blog index hero only |

## Available (unused)
| Image | What it shows | Good for |
|---|---|---|
| blog-email | Person typing an email at a sunny desk with a plant | Cold email, deliverability, reply rates |

## When nothing fits or the list is empty
Do not reuse. Build a branded cover instead: 1600x900, background gradient #0d4747 to #061f20, the post category in small caps (#efbf6e), a short headline (Fraunces style serif, #f6f1e7), and one simple chart or number motif in amber. Render an HTML page with Playwright (Chromium is pre-installed) to img/cover-<slug>.jpg (quality 85) plus a .webp, then add it to "In use" above.
