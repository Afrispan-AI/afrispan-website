# Afrispan AI Assurance: Website Build Context

This document is the complete handoff for building the Afrispan AI Assurance website. It exists so the new conversation starts with everything already settled, not re-debated. Read this in full before proposing any structure, copy, or design direction.

## Who This Is For

Steve Onyeke, founder of Afrispan AI Assurance, an AI deployment assurance practice. Currently also an AI Quality Analyst at Turing on a Google-commissioned Gemini evaluation programme, and separately in an active, ongoing interview process for a Talabat AI Governance Engineer role in Dubai. Afrispan is the founder's own company and long-term focus; the technical portfolio behind it doubles as both Afrispan's real capability and Steve's own career evidence.

## The Single Most Important Decision Already Made, Do Not Re-litigate This

**This is a practical, credibility-first marketing website. It is explicitly not a client login portal, not a subscription platform, and does not process client data.** This was a deliberate, reasoned decision, not a default:

- Afrispan's actual service lines, conformity assessment, FRIA, cross-border framework, red-teaming, governance orchestration, are consultative engagements requiring deep client-specific access and judgment. They are not standardized, self-serve products yet.
- The realistic near-term market, per the business plan's own TAM/SAM/SOM breakdown, is low hundreds of businesses reached through direct, relationship-led outreach, not a paid acquisition funnel a self-service platform would serve.
- A platform accepting client logins would make Afrispan itself a data processor under Nigeria's NDPA, subject to the exact security rigor it sells, a real, avoidable liability at pre-revenue stage.

**The website's three jobs, in order of importance:**
1. State the business model and regulatory argument plainly, so a visitor understands what Afrispan does and why now, without needing a sales call to find out.
2. Prove technical capability directly, link straight to the real, public GitHub portfolio so a technical stakeholder can verify the work themselves, not take a claim on faith.
3. Convert interest into a conversation, a clear "book a discovery call" or "contact us" path, not a signup form.

**The one thing that should change this plan going forward, not before:** once Afrispan has closed 5 to 10 real paid engagements and understands what a client actually needs to keep watching over time, the ongoing monitoring subscription line becomes a genuine candidate for a lightweight, client-facing dashboard, building directly on Project 3's own dashboard work. That is a deliberate later phase, not something to pull forward into this build.

## Company Facts

- **Name:** Afrispan AI Assurance
- **Founder:** Steve Onyeke, Founder and AI Governance Lead
- **Mission:** To make African enterprises deploying AI systems provably safe, compliant, and accountable, through independent, evidence-based verification rather than vendor assertion.
- **UK connection, stated honestly, not overstated:** the founder is based in Manchester, United Kingdom. A formal UK corporate registration is currently underway alongside the Nigerian registration, treated as in progress, not yet complete, the same honest-status treatment as the domain registration below. This is a real, deliberate credibility factor for Nigerian buyers who value foreign-linked technical assurance, not a UK go-to-market strategy, that remains explicitly out of scope.
- **Social profiles:** X at x.com/afrispan, LinkedIn at linkedin.com/company/afrispan-ai.
- **Primary market:** Nigeria, specifically Lagos first, fintech and digital-first SMEs. This is a deliberate revision from Afrispan's original 2024 Ghana-first plan, reasoned in the business plan on scale and regulatory-timing grounds, not a change of mission. Ghana and wider ECOWAS remain a real phase-two market via AfCFTA.
- **Status:** A governance practice built on the founder's decade of enterprise technology risk and delivery governance experience, not a venture without a track record. As a corporate entity, founder-funded and actively pursuing first paid engagements.
- **GitHub:** github.com/Afrispan-AI/ai-governance-suite, public, migrated with full commit history intact from the original personal repository. The old personal repo (github.com/steveonyeke/python-ai-governance) should carry a note pointing here and be archived, not deleted, since it's still linked from Steve's own career materials.

## The Regulatory Argument, the Website's Real Hook

This is the sharpest, most current argument in the business plan and should anchor the site's core message, not get buried in an appendix.

- Nigeria published its National Artificial Intelligence Strategy in September 2025, a five-year vision to 2029.
- A National Digital Economy and E-Governance Bill, expected to pass in 2026, would give NITDA formal, risk-based regulatory authority: mandatory licensing and annual impact assessments for high-risk AI systems in finance, public administration, and automated decision-making. Penalties reach 10 million naira or 2 percent of annual gross revenue, whichever is higher.
- **The critical, honest finding:** as of March 2026, Nigeria's own independent AI Governance Regulatory Body, the strategy's own capstone institution, has not been constituted, and NITDA's Code of Practice for AI remains unfinalized.
- **The argument this creates:** enterprises know binding obligations are coming, but there is no operational government channel yet to prepare against them. Private-sector assurance, built to the rigor the eventual law will demand, is the practical bridge, not a workaround.
- The mandatory annual impact assessment described in the coming bill is functionally the same deliverable as Afrispan's own Conformity Report and FRIA tooling, already built and demonstrable today.

## Service Lines, What The Site Needs To Describe Clearly

1. **AI Governance Gap Analysis**, the lighter, faster entry point ahead of the full Conformity Report, a structured consultation surfacing where AI is genuinely in use, who's accountable for it, and where the real exposure sits.
2. **Regulatory Conformity Assessment**, scored against EU AI Act, NIST AI RMF, NIST AI 600-1, and ISO/IEC 42001 simultaneously, twenty-two obligations, untested ones marked as such, never omitted.
3. **Fundamental Rights and Impact Assessment**, aligned directly with Nigeria's coming annual impact assessment requirement.
4. **Cross-Border Deployment Framework**, an honest check of whether compliance evidence actually transfers between Nigeria, Ghana, and wider ECOWAS, not an assumption that it does.
5. **Evaluation and Red-Team Engagement**, cross-model judging, adversarial testing mapped to OWASP LLM and Agentic Top 10 and MITRE ATLAS, drift monitoring.
6. **Governance Orchestration and Human Oversight Enforcement**, the differentiator: live infrastructure, not policy documents, automated routing, an immediate independent kill-switch, a resume mechanism requiring a named, substantive human decision.
7. **Complex Workflow Automation, Governed by Design**, building AI-powered business automation with the same assurance discipline built in from day one.

## Competitive Positioning, Real and Sourced

Every organisation on Nigeria's own official licensed DPCO registry, EY and KPMG's Nigerian affiliates, DataPro, Pavestones Legal, Hephzibah, Johan Consults, is a generalist data-protection auditor. None publish a technical methodology for evaluating an AI system's actual behaviour, and none produce the specific evidentiary outputs Afrispan does as a result: a Conformity Report scored against multiple international frameworks at once, a Fundamental Rights Impact Assessment built from a real audit trail, or a Cross-Border Deployment Framework testing whether compliance evidence actually transfers between jurisdictions. That is Afrispan's real, documented market gap, not piles of policy documents with zero engineering translation behind them, not an assumed differentiation. The website should lean on this specific, checkable fact rather than generic "we're different" language.

## The Technical Portfolio, What The Site Links To As Proof

Full detail lives in the repository's own `CLAUDE.md` and `docs/PROJECT_HISTORY.md`. Summary for website-copy purposes:

- **Project 1**, nine phases, real Gemini API execution throughout, discovered five recurring governance principles: an AI system cannot audit itself, surface pattern-matching fails at the edges, monitoring is not governing, authority is not judgment, and judge/human disagreement is diagnostic, not noise. Includes a real kill-switch with immutable SHA-256 hash-chained audit logging, and the FRIA, Conformity Report, and Cross-Border Framework generators.
- **Project 2**, thirteen notebooks, a production evaluation architecture, cross-model judging (measured 0.15 point quality inflation from same-family judging), red-teaming mapped to OWASP and MITRE ATLAS, a verified CI/CD pipeline on GitHub Actions. Architecture is pytest-verified; most notebooks run in simulated mode pending funded API billing, stated honestly wherever relevant, never implied otherwise.
- **Project 3**, live governance orchestration in n8n: three-queue PR routing with non-blocking human review, a kill-switch converging drift alarms and red-team findings into one shared gate, pre-committed verdicts (closing a real gap named by an external reviewer, Federico Blanco Sanchez-Llanos), and a real-time dashboard. Built, tested, and verified on real local hardware, not simulated, the first phase of this portfolio to reach that status.

**Website copy rule inherited from this whole project's discipline: never claim something is proven, live, or complete unless it genuinely is. Where something is illustrative, planned, or simulated, say so plainly, in the copy itself, not hidden in a footnote.**

## Brand System, Locked

- **Colors:** Deep Navy #0D2B5B (primary, must dominate), Emerald Green #00A651 (accent, sparing), Sunrise Orange #FF7A00 (accent, sparing).
- **Typography:** Headlines in Manrope SemiBold/Bold. Body and UI text in Inter Regular/Medium. Long-form documents may use Source Serif 4.
- **Real logo assets exist**: a horizontal wordmark, provided in both a dark-background variant (navy background, white "AFRISPAN AI ASSURANCE" text) and a light-background variant (light background, navy "AFRISPAN AI ASSURANCE" text), each with green and orange underline accents either side of "AI ASSURANCE", and a standalone circular navy badge with a white stylised arch-and-peak "A" mark. These are real, final assets, not placeholders, upload them fresh to this new chat since files do not carry across conversations. Do not reconstruct or reinterpret the logo from memory or description.

## Non-Negotiable Rules, Carried Over From The Entire Project

- No em dashes, anywhere, in any generated copy, code, or documentation.
- Verify before asserting. If a website claim needs a statistic or regulatory fact, it should trace back to something already sourced in the business plan, not be invented fresh for marketing effect.
- Every capability claim tagged honestly by its real status, proven, building, or planned, never blurred for a better-sounding pitch.

## Open Items Not Yet Resolved, Worth Surfacing Early In The New Chat

- **Domain name, live:** afrispanai.com is confirmed live and serving the real site. afrispanai.co.uk is confirmed live and correctly redirects to afrispanai.com.
- **Dedicated Afrispan email, configured but not yet verified:** contact@afrispanai.com. Email hosting is configured at LCN, but actual deliverability, whether a message sent from that address reaches an external inbox correctly, has not yet been tested and confirmed. Treat this as configured, not yet verified working, not as fully operational.
- **Pricing:** the business plan's figures are explicitly illustrative, anchored against real Nigerian professional-services rates and an international SME compliance-audit benchmark, but not yet validated against a real client quote. The website should avoid stating specific prices until this is resolved, a "contact for pricing" or engagement-tiers-without-numbers approach fits the current stage better.
- **Liability and professional indemnity:** the business plan flags that a qualified Nigerian lawyer should review the engagement contract template and confirm indemnity cover before the first paid client, this has not yet happened. The website's own terms and any contact-form disclaimers should not overstate guarantees Afrispan cannot yet legally back.

## Full Source Documents

The complete Institutional Business Plan and the technical portfolio's `CLAUDE.md` and `docs/PROJECT_HISTORY.md` contain the full depth behind everything summarised above. If a specific figure, quote, or technical claim is needed for website copy and isn't in this briefing, it should be pulled from those source documents directly, or verified fresh, not approximated from memory.

## Suggested First Step For The New Chat

Confirm the domain name decision, then propose a simple, practical site structure covering: home and positioning, the regulatory argument, service lines, the technical proof and GitHub link, about and founder, and contact, before writing any actual page copy or code.
