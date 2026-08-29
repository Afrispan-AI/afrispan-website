# Afrispan AI Assurance: Institutional Business Plan

*Full reference document, converted from the original institutional business plan. See docs/BUSINESS_CONTEXT.md for the condensed summary.*

**Institutional Business Plan**

*AI Deployment Assurance for Nigerian and West African Enterprises*

Prepared by: Steve Onyeke, Founder and AI Governance Lead

August 2026

**Document Status:** This plan is written to institutional standard, suitable for review by partners, financial institutions, and prospective investors. Financial projections in Section 13 are explicitly labeled as illustrative assumptions built on stated inputs, not historical performance, since Afrispan is pre-revenue at time of writing. Every regulatory and market claim in this document is sourced and current as of August 2026; Nigeria's AI regulatory environment is moving quickly and this document should be revisited at minimum quarterly.

Contents

1. Executive Summary

2. Company Overview

3. The Problem

4. Market Opportunity: Nigeria and West Africa

5. Regulatory Landscape

6. Products and Services

7. Competitive Landscape and Differentiation

8. Business Model

9. Go-to-Market Strategy

10. Technology and Intellectual Property

11. Operations Plan

12. Founder and Team

13. Financial Plan

14. Risk Analysis

15. Roadmap and Milestones

16. Appendix: Evidence and References

## 1. Executive Summary

Afrispan AI Assurance is an AI deployment assurance practice serving Nigerian and West African enterprises deploying AI systems into production. The company's core proposition is straightforward: an AI system should not be trusted to be safe, compliant, and well-governed simply because a vendor asserts it is. It should be independently verified, with evidence, the same discipline financial audit has applied to accounting for a century, now applied to AI.

Afrispan's founding thesis is that Nigeria's AI governance landscape is at a genuine inflection point. The country published its National Artificial Intelligence Strategy in September 2025, and a National Digital Economy and E-Governance Bill, expected to pass in 2026, will give Nigeria's National Information Technology Development Agency (NITDA) formal, risk-based regulatory authority over AI, including mandatory licensing and annual impact assessments for high-risk systems in finance, public administration, and automated decision-making. Critically, as of this writing, the independent oversight body the strategy itself calls for has not yet been constituted, and NITDA's own Code of Practice for AI remains unfinalized. This creates a real, time-bound window: enterprises that build governance capability now, ahead of mandatory enforcement, will be positioned to comply quickly once it lands. Those that wait will be building under regulatory pressure, at higher cost and with less runway.

Nigeria's addressable market is substantial and growing quickly. The country has nearly 40 million micro, small, and medium enterprises, per the Small and Medium Enterprises Development Agency of Nigeria (SMEDAN), and its digital transformation market is projected to grow from roughly 14 billion dollars in 2026 to over 31 billion dollars by 2031, a 17.72 percent compound annual growth rate. SME digital adoption specifically is growing faster than large-enterprise adoption, 24.8 percent compound annual growth against large enterprises' current 60.3 percent adoption share, meaning the SME segment is where the growth curve is steepest, not where it has already plateaued.

Afrispan's technical capability is not aspirational. It is built, tested, and publicly demonstrable across three connected open-source projects totaling nine governance phases, a thirteen-notebook production evaluation suite with a verified CI/CD pipeline, and a live governance orchestration layer built in n8n, enforcing human oversight on autonomous AI decisions in real time. This is a genuine technical moat few assurance practices, in Nigeria or globally, can currently demonstrate with working code rather than slide decks.

Afrispan is a governance practice, built on its founder's decade of enterprise technology risk and delivery governance experience, not a venture without a track record. As a corporate entity it is founder-funded and pre-revenue, structured to close its first paid engagements in Nigeria within the next two quarters, expand across West Africa via the African Continental Free Trade Area's SME trade infrastructure, and build toward a defensible position as the region's most technically credible AI assurance practice.

## 2. Company Overview

### Mission

To make African enterprises deploying AI systems provably safe, compliant, and accountable, through independent, evidence-based verification rather than vendor assertion.

### Vision

A West Africa where no enterprise deploys an AI system that materially affects a customer, an employee, or a regulator's trust without a real, checkable audit trail behind it.

### Founding Story and Rationale

Afrispan was founded in January 2024 by Steve Onyeke, Founder and AI Governance Lead, with over a decade of technology, risk, and governance experience built across Nigeria, the United Kingdom, and global technology platforms, including as a Technology Risk and Data Governance Analyst in a regulated environment, as a Cybersecurity and Data Risk Analyst for Althaus Digital in the United Kingdom, in stakeholder and community engagement work with Binance, and currently as an AI Quality Analyst on a Google-commissioned Gemini evaluation programme through Turing. Afrispan's technical foundation was built as a deliberate, evidence-first curriculum, not a theoretical framework, resulting in real, working governance systems, kill-switches, cross-model evaluation architecture, red-teaming mapped to international security standards, and live orchestration infrastructure, published openly and independently verifiable.

### Legal Structure and Geography

Afrispan AI Assurance operates with a genuine dual-market foundation, not an aspirational one. The founder is based in Manchester, United Kingdom, giving Afrispan direct, current proximity to the international standards, EU AI Act, NIST AI RMF, ISO/IEC 42001, its methodology is built against, and to the institutional and investor-grade due diligence norms Nigerian enterprises increasingly need to satisfy. A formal United Kingdom corporate registration is underway alongside the company's Nigerian registration, both treated as near-term, committed milestones, not completed facts, consistent with this plan's own discipline of never stating a pending action as already finished.

Primary commercial and delivery operations are based in Lagos, Nigeria's principal technology and financial services hub. This is a deliberate choice: Lagos hosts the Central Bank of Nigeria's AI-focused fintech sandbox, a growing concentration of NITDA-adjacent policy activity, and, per recent industry reporting, Africa's first regional AI safety institute, placing Afrispan inside the country's actual centre of AI governance activity rather than adjacent to it.

## 3. The Problem

Nigerian and West African enterprises are adopting AI faster than they are building the capability to govern it. This is not a hypothetical risk, it is the specific, structural gap Afrispan exists to close, and it has three distinct components.

### An AI system cannot be trusted to audit itself

The most common form of AI quality assurance available to an SME today is the vendor's own claim that their system works correctly. This is structurally unreliable, not because vendors are dishonest, but because an AI system judging its own output, or a vendor evaluating its own product, shares the same blind spots as the system being evaluated. Afrispan's own technical work has measured this directly: a same-family AI judge evaluating identical output showed a 0.15 point quality inflation and a 0.23 point gap in catching real errors, compared to an independent, cross-model evaluator. The fix is structural, not a matter of trusting harder, independent verification, architected to be independent from the outset.

### Nigeria's regulatory enforcement infrastructure is not yet operational, but the obligations are coming

As detailed fully in Section 5, Nigeria's National AI Strategy and its forthcoming Digital Economy and E-Governance Bill will introduce real, binding obligations, licensing for high-risk AI systems, mandatory annual impact assessments, and enforcement powers for NITDA. The independent governance body the strategy itself calls for has not yet been constituted. This leaves a genuine gap: enterprises know obligations are coming, but have no clear, currently operating government channel to prepare against them. Private-sector assurance capability, built to the same rigor the eventual regulation will demand, is the practical way to close that gap today, not a workaround, a necessary bridge.

### Governance is treated as documentation, not as an engineering discipline

Where AI governance exists at all in the Nigerian SME market today, it is typically a policy document, a checklist, or a consultant's report, produced once and rarely revisited. It is not built into the system's actual operation. A policy that says a human must review a high-risk AI decision is not the same claim as a working mechanism that actually pauses the system and waits for a documented, substantive decision before proceeding. Afrispan's central differentiator is building the second kind, governance as running infrastructure, not governance as paperwork.

## 4. Market Opportunity: Nigeria and West Africa

### Market Sizing

|                                                         |                             |                                              |
|---------------------------------------------------------|-----------------------------|----------------------------------------------|
| **Metric**                                              | **Figure**                  | **Source and Year**                          |
| Nigerian MSMEs                                          | Nearly 40 million           | SMEDAN, cited 2026                           |
| Nigeria digital transformation market, 2026             | USD 13.96 billion           | Mordor Intelligence, 2026                    |
| Nigeria digital transformation market, 2031 (projected) | USD 31.58 billion           | Mordor Intelligence, 2026                    |
| Nigeria digital transformation CAGR, 2026-2031          | 17.72%                      | Mordor Intelligence, 2026                    |
| SME digital adoption CAGR (Africa-wide)                 | 24.8%                       | Mordor Intelligence, 2026                    |
| Nigeria mobile subscriptions                            | 139.28 million              | Nigerian Communications Commission, Dec 2024 |
| Nigeria Government AI Readiness Index rank              | 72nd globally, up 31 places | 2025 Index                                   |
| AfCFTA addressable market                               | USD 3.5 trillion            | Nigerian Federal Government, March 2026      |

### Why Nigeria First, Not Ghana

Afrispan's original 2024 market entry plan targeted Ghana and wider West Africa. This plan deliberately revises that sequencing: Nigeria is now the primary market, for reasons grounded in scale and regulatory timing rather than a change in mission. Nigeria's MSME population is roughly ten times Ghana's, its digital transformation market is measured in tens of billions of dollars against Ghana's low single-digit billions, and, most importantly, Nigeria's regulatory clock is moving faster and more concretely, a specific bill with specific licensing and impact-assessment obligations expected in 2026, not a general policy direction. Ghana and the wider ECOWAS region remain a genuine phase-two expansion market, addressed directly in Section 9.

### Why SMEs, Not Only Large Enterprises

Large Nigerian enterprises, particularly banks operating inside the Central Bank of Nigeria's AI sandbox, already have some access to compliance and audit capability, whether in-house or through global consultancies. SMEs largely do not, and SMEs are also the segment growing digital adoption fastest, 24.8 percent compound annual growth against large enterprises' current 60.3 percent adoption share. This is a structural opportunity: the market segment growing fastest is also the segment least served by existing AI assurance capability.

### Total Addressable, Serviceable, and Obtainable Market

Sizing this opportunity honestly requires narrowing from Nigeria's full MSME population down to the realistic near-term buyer, since not every small business is a plausible AI-governance client today.

|           |                                                                                                                                       |                                                                                                    |                                                                                                                                     |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Layer** | **Definition**                                                                                                                        | **Estimate**                                                                                       | **Basis for Narrowing**                                                                                                             |
| TAM       | Total Addressable Market: all Nigerian MSMEs                                                                                          | Approximately 40 million businesses                                                                | SMEDAN's full MSME count, the ceiling, not a near-term target                                                                       |
| SAM       | Serviceable Available Market: MSMEs that have digitised operations and plausibly use or plan to use an AI system                      | Low single-digit millions of businesses, concentrated in fintech, e-commerce, and digital services | Digital transformation adoption data suggests only a minority of the 40 million are digital-first enough to have deployed AI at all |
| SOM       | Serviceable Obtainable Market: businesses Afrispan can realistically reach and convert within 24 months, given a founder-led practice | Low hundreds of businesses, concentrated in Lagos fintech and digital-first SMEs                   | Bounded by direct, relationship-led sales capacity described in Section 9, not a paid acquisition channel at this stage             |

**Why This Framing Matters, Stated Directly:** A business plan that cites the 40-million MSME figure as the market Afrispan is selling into would be presenting the TAM as though it were the SOM, a common and misleading error. Afrispan's actual near-term opportunity is the SOM, low hundreds of reachable, digitally mature businesses in year one and two, not the full MSME population. The TAM matters for demonstrating long-term ceiling to a future investor, not for planning this year's sales targets.

## 5. Regulatory Landscape

**Why This Section Matters More Than a Typical Business Plan's Regulatory Appendix:** For Afrispan specifically, the regulatory landscape is not a risk to be managed, it is the core argument for why the business exists now. This section is written to be revisited and updated at minimum quarterly, given how quickly Nigeria's AI governance framework is moving.

### Current Legal Foundation

The Nigeria Data Protection Act 2023 (NDPA) and the Nigeria Data Protection Commission (NDPC) it established remain the primary binding legal foundation for data governance obligations that intersect directly with AI deployment. Nigeria does not yet have a dedicated, binding AI-specific law. AI-related obligations today are drawn from general principles, contract law, data protection, and product liability, applied to AI systems by extension, rather than AI-specific statute.

### The National Artificial Intelligence Strategy (NAIS)

Nigeria's National Artificial Intelligence Strategy was published in September 2025 by the Federal Ministry of Communications, Innovation and Digital Economy, with NITDA as principal implementing body. It sets a five-year vision, 2025 to 2029, structured around three goals, economic growth and competitiveness, social development and inclusion, and technological advancement and leadership, and five operational pillars, infrastructure, ecosystem development, sector adoption, responsible AI, and governance.

### The Coming Enforcement Mechanism: The National Digital Economy and E-Governance Bill

Following a public hearing in November 2025, Nigeria's National Digital Economy and E-Governance Bill is expected to pass in 2026, positioning NITDA as Nigeria's digital technology super-regulator. Reported provisions include a risk-based framework in which high-risk AI systems, specifically named categories include finance, public administration, surveillance, and automated decision-making, will require formal licensing and mandatory annual impact assessments detailing risks, mitigation strategies, and system performance. Regulators would gain powers to demand information, issue directives, and block unsafe systems. Reported penalties for non-compliance reach 10 million naira, approximately 7,000 US dollars, or 2 percent of a company's annual gross revenue in Nigeria, whichever is higher. If enacted as reported, Nigeria would become one of the first African nations with a comprehensive, enforceable AI regulatory framework, ahead of comparable strategies in Egypt, Benin, and Mauritius that have not yet been converted into binding legislation.

**THE SPECIFIC MARKET OPPORTUNITY THIS CREATES:** The mandatory annual impact assessment requirement described above is, functionally, the same deliverable as Afrispan's own Conformity Report and Fundamental Rights Impact Assessment tooling, already built, tested, and demonstrable today, months or years ahead of the obligation becoming mandatory. Enterprises that engage Afrispan now are not buying a speculative future service, they are building the exact evidence artifact the coming law will require, before they are legally compelled to.

### The Honest, Verified Gap: Nigeria's Own Oversight Body Is Not Yet Operational

An independent policy analysis published April 2026 found that, as of March 2026, NITDA's own Code of Practice for AI (2025) had not been finalised, and the independent AI Governance Regulatory Body the NAIS itself calls for under its fifth pillar had not been constituted, with no published timeline, funding mechanism, or defined legal independence. The same analysis raised a structural concern worth Afrispan naming directly and honestly: NITDA's own AI Transformation Roadmap assigns governance functions to NITDA itself, a body that also promotes AI development, a potential conflict of interest the analysis argues should be resolved by constituting the independent oversight body before, not after, the Code of Practice is finalised.

For Afrispan, this finding is treated as an opportunity to be transparent about, not exploited quietly. It means the practical, operational channel for an enterprise seeking real AI governance capability in Nigeria today is not yet a government one. It is private-sector assurance, built to a rigor that anticipates what formal regulation will eventually require, filling a genuine, time-bound gap rather than competing with government enforcement once it exists.

### An Existing, Adjacent Licensing Pathway Worth Pursuing: DPCO Status

Nigeria's data protection framework already recognises Licensed Data Protection Compliance Organizations (DPCOs) as a formal third-party category authorised to support compliance and audit work under the NDPA. Afrispan should evaluate pursuing DPCO licensing as a near-term strategic milestone, since it provides an existing, government-recognised credential adjacent to Afrispan's AI-specific work, ahead of any AI-specific licensing regime that may follow the Digital Economy and E-Governance Bill's eventual passage.

### Sector-Specific Regulatory Activity

The Central Bank of Nigeria's regulatory sandbox, launched 2023 and expanded through 2024 and 2025, already evaluates AI-powered fintech tools for model explainability, fairness, and consumer transparency before granting approvals, a real, current precedent for exactly the kind of independent evaluation work Afrispan performs, applied specifically to Nigeria's large and fast-growing fintech sector.

## 6. Products and Services

Every service Afrispan offers is grounded in a real, working technical capability, publicly demonstrable on GitHub, not a service description written ahead of the capability existing.

### Service Line 1: Regulatory Conformity Assessment

A structured assessment scoring a client's AI system against multiple regulatory and standards frameworks simultaneously, EU AI Act, NIST AI RMF, NIST AI 600-1, and ISO/IEC 42001, with Nigeria's own emerging framework mapped in directly as it finalises. Built on Afrispan's own twenty-two obligation Conformity Report methodology. Untested obligations are marked as such explicitly, never silently omitted, the same evidentiary honesty a real audit demands.

### Service Line 2: Fundamental Rights and Impact Assessment

A structured, documented assessment of an AI system's impact on the people it affects, directly aligned with the annual impact assessment requirement expected under Nigeria's coming AI legislation. Generated from a real audit trail wherever automated evidence exists, tagging every field as automated, attested by direct client input, or explicitly missing, never filled with a plausible guess.

### Service Line 3: Cross-Border Deployment Framework

For clients operating or expanding across West Africa, an honest assessment of whether compliance evidence built for one jurisdiction actually transfers to another, rather than an assumption that it does. Given AfCFTA's active push toward regional MSME trade integration, this is a direct, near-term need for Nigerian enterprises expanding into Ghana, and the wider ECOWAS market.

### Service Line 4: Evaluation and Red-Team Engagement

Technical evaluation of an AI system's actual behaviour, cross-model judging to avoid the self-audit blind spot described in Section 3, adversarial red-teaming mapped to the OWASP LLM and Agentic Top 10 and MITRE ATLAS taxonomies, and drift monitoring to catch a system quietly degrading over time, not only when it fails outright.

### Service Line 5: Governance Orchestration and Human Oversight Enforcement

The service line that distinguishes Afrispan most sharply from a traditional audit or consulting practice. Building the live infrastructure that makes governance operational: automated routing of AI decisions to confident-pass, confident-fail, or human-review queues, a kill-switch that halts automated action immediately and independently the moment a serious finding occurs, and a resume mechanism that requires a named, accountable person to record a substantive decision, not a single approval click, before automated operation continues. This is built on real, demonstrable orchestration technology, not a policy document describing what a client should build themselves.

### Service Line 6: Complex Workflow Automation, Governed by Design

For clients whose need extends beyond assessment into building the AI-powered automation itself, sales, customer support, lead management, and internal operations, Afrispan designs and implements it with the same governance discipline already proven in its own live infrastructure, the same kill-switch enforcement and human-oversight routing demonstrated in Afrispan's own Project 3 build, applied to a client's specific automation, built in from the start, not retrofitted after deployment. This positions Afrispan as able to serve a client across their full AI adoption journey, not only the assurance layer.

## 7. Competitive Landscape and Differentiation

|                                              |                                                    |                                                                                                                                           |
|----------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Competitor Type**                          | **Example**                                        | **Why Afrispan Differentiates**                                                                                                           |
| Global Big Four and management consultancies | Deloitte, PwC, EY, KPMG AI risk practices          | Real, high-cost engagements, typically priced for large enterprise, not structured for Nigerian SME budgets or delivery speed             |
| Global AI evaluation platforms               | Vendors selling evaluation-as-a-service software   | Software-only, no regional regulatory context, no local presence, limited human-in-the-loop enforcement infrastructure                    |
| Generic AI automation agencies               | Agencies building chatbots and workflow automation | Build automation without governance discipline built in, the exact gap Afrispan's Service Line 6 is designed to close                     |
| Internal compliance or IT teams              | In-house SME staff handling this informally        | Lack independent verification credibility, and typically lack the specific technical evaluation methodology Afrispan has built and proven |

### Named Competitors in the Actual Nigerian Market

This section is grounded in the Nigeria Data Protection Commission's own public list of licensed Data Protection Compliance Organisations, since DPCOs are the closest existing, formally recognised competitor category to Afrispan's own positioning today.

|                                   |                                                        |                                                                                                                    |
|-----------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Organisation**                  | **Type**                                               | **Relevant Detail**                                                                                                |
| EY and KPMG Advisory Services     | Global Big Four affiliates, licensed DPCOs in Nigeria  | Real, confirmed local presence, not a hypothetical global competitor; priced for large enterprise, not SME budgets |
| DataPro Limited                   | Nigerian compliance consultancy, licensed DPCO         | Publicly positions itself as having the most extensive compliance consulting background among licensed DPCOs       |
| Pavestones Legal                  | Law firm operating as a licensed DPCO                  | Legal-first framing, general data protection audit, no published AI-specific evaluation methodology                |
| Hephzibah Integrated Technologies | Abuja-based IT and data consulting firm, licensed DPCO | Positions itself as a niche IT and data consultancy across public and private sector clients                       |
| Johan Consults Ltd                | Licensed DPCO                                          | General data protection compliance consulting                                                                      |

**The Real, Sourced Gap This Reveals:** Every organisation on Nigeria's own licensed DPCO list is a general data protection auditor, a law firm, an accounting affiliate, or a generalist IT consultancy. None publish a technical methodology for evaluating an AI system's actual behaviour, and none produce the specific evidentiary outputs Afrispan does as a result: a Conformity Report scored against multiple international frameworks at once, a Fundamental Rights Impact Assessment built from a real audit trail, or a Cross-Border Deployment Framework testing whether compliance evidence actually transfers between jurisdictions. Cross-model judging, adversarial red-teaming mapped to OWASP and MITRE ATLAS, and drift monitoring are the mechanisms behind those documents, not abstractions on their own, not piles of policy documents with zero engineering translation behind them. Independent industry commentary on choosing a DPCO makes this gap explicit: a generalist auditor evaluating an AI-driven credit scoring or fraud-detection system will miss explainability and technical risks a non-technical auditor is not equipped to check. That is the precise, sourced gap Afrispan is built to fill, not a claimed differentiation, a documented absence in the current market.

### Why the UK Foundation Matters to Nigerian Buyers

One real, worth-naming factor sits outside the two-axis framing above: Nigerian enterprises, particularly those seeking institutional investment or serving international counterparties, place genuine, documented value in foreign-linked technical credibility when de-risking a technology decision. Afrispan's founder is based in the United Kingdom, and a formal UK corporate registration is currently underway alongside the company's Nigerian registration, described honestly in Section 2 as in progress, not yet complete. Once formalised, this gives Afrispan a genuine dual-market foundation none of the Nigeria-only competitors named above can claim, direct proximity to the international standards this methodology is built against, useful specifically in conversations with venture-backed fintechs preparing investor due diligence, or platforms expanding into UK and European corridors. This is a real, structural advantage worth stating plainly once the registration is complete, not a claim to make ahead of it.

### Positioning on Two Axes

The clearest way to see Afrispan's actual competitive position is against two dimensions at once: cost and accessibility to a Nigerian SME on one axis, and depth of technical, working proof on the other.

|                                    |                                   |                                                                             |
|------------------------------------|-----------------------------------|-----------------------------------------------------------------------------|
| **Positioning**                    | **High Technical Proof**          | **Low Technical Proof**                                                     |
| Accessible to Nigerian SME budgets | Afrispan's target position        | Generic automation agencies, internal DIY compliance efforts                |
| Priced for large enterprise        | Global Big Four AI risk practices | Generic strategy consultancies offering AI advisory without working systems |

No competitor currently occupies the combination of genuinely working, verifiable technical proof and pricing structured for the Nigerian SME segment specifically. That is the position this plan is built to defend, not a temporary gap expected to close on its own.

## 8. Business Model

### Revenue Streams

- **Fixed-scope assessment engagements:** a defined Conformity Report, FRIA, or Cross-Border Framework deliverable, priced per engagement, the natural first purchase for a new client.

- **Implementation and orchestration projects:** building the governance orchestration and human-oversight enforcement infrastructure described in Service Line 5, priced per project given its greater scope and integration work.

- **Ongoing monitoring subscriptions:** recurring revenue for continued drift monitoring, regression alerting, and periodic re-assessment once initial governance infrastructure is in place, the natural expansion revenue from an existing client.

- **Workflow automation projects:** Service Line 6 engagements, priced per project, often the entry point for clients whose primary need is automation rather than assurance, with governance capability introduced as part of the same engagement.

### Pricing Philosophy

Pricing is structured to be genuinely accessible to Nigerian SMEs, not a scaled-down version of global consultancy rates. Fixed-scope assessments should be priced to be a realistic first purchase for a growing SME, with implementation and monitoring revenue built to grow alongside a client's own AI maturity, rather than requiring a large upfront commitment before any value is demonstrated.

## 9. Go-to-Market Strategy

### Phase 1: Lagos, Fintech and Digital-First SMEs (Months 1-6)

Initial focus on Lagos-based fintech and digital-first SMEs specifically, given the Central Bank of Nigeria's active AI sandbox already creates real demand for exactly the evaluation discipline Afrispan provides, and given Lagos's concentration of the digital-native SMEs most likely to have already deployed an AI system worth assessing.

### Phase 2: Nigeria-Wide Expansion (Months 6-18)

Expansion beyond Lagos as case studies and referenceable client outcomes accumulate, targeting Abuja's public-sector-adjacent technology vendors and Nigeria's other major commercial centres, alongside pursuit of DPCO licensing as a credibility milestone.

### Phase 3: West Africa via AfCFTA (Months 18-36)

Expansion into Ghana and the wider ECOWAS region, positioned explicitly through the Cross-Border Deployment Framework service line, targeting Nigerian clients already expanding regionally under AfCFTA rather than starting relationships from zero in a new market.

### Channels

- **Direct outreach and thought leadership:** published technical findings, demonstrable open-source work, and direct relationship-building with SME founders and technology leads.

- **Partnership with the Nigerian fintech and startup ecosystem:** engagement with initiatives such as the NITDA and Korean International Cooperation Agency Start-Up Digital Innovation Academy, and Nigeria Startup Act-registered entities.

- **Referral from professional and regulatory networks:** relationships built through pursuit of DPCO status and engagement with NDPC-adjacent compliance networks.

- **Investor and cross-border counterparty conversations, once UK registration completes:** venture-backed Nigerian fintechs preparing investor due diligence, and platforms expanding into UK or European corridors, are a natural audience for Afrispan's dual-market foundation, addressed honestly as it actually stands at the time of outreach, not overstated ahead of the registration itself finishing.

### Specific First-90-Days Tactics

Concrete, not aspirational: what actually happens before Phase 1 can be called underway.

- **Weeks 1-2:** finalise this plan and the Afrispan website, ensuring the live GitHub portfolio is directly linked and easy for a technical stakeholder to verify independently.

- **Weeks 2-6:** direct outreach to a named list of Lagos-based fintech and digital-first SMEs, prioritising companies already visibly engaging with the Central Bank of Nigeria's AI sandbox or publicly discussing AI adoption.

- **Weeks 4-8:** publish at least two technical findings pieces, following the same evidence-first format as Afrispan's existing published work, specifically framed around Nigeria's coming regulatory obligations described in Section 5, to establish credibility ahead of first sales conversations.

- **Weeks 8-12:** convert initial conversations into the first one to three fixed-scope assessment engagements, prioritising a client willing to serve as a referenceable case study over the highest-paying prospect, given how early-stage credibility-building matters more than early revenue maximisation.

## 10. Technology and Intellectual Property

Afrispan's technical foundation is public, verifiable, and substantial, a genuine asset most early-stage assurance practices cannot demonstrate. It spans three connected projects on GitHub, publicly available at github.com/Afrispan-AI/ai-governance-suite.

|             |                                                                                                                                                |                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| **Project** | **Scope**                                                                                                                                      | **Status**                                         |
| Project 1   | Nine phases proving core governance principles, including a real, working kill-switch with immutable audit logging                             | Complete, executed against real API calls          |
| Project 2   | Thirteen-notebook production evaluation suite, cross-model judging, red-teaming mapped to OWASP and MITRE ATLAS, verified CI/CD pipeline       | Architecture complete and pytest-verified          |
| Project 3   | Live governance orchestration: automated routing, kill-switch enforcement, pre-committed evaluation verdicts, a real-time governance dashboard | Built, tested, and verified on live infrastructure |

This body of work is not a marketing asset alone. It is the actual methodology Afrispan's service lines are built on, meaning every service described in Section 6 can be demonstrated with working code and real test results during a client engagement, not described only in a proposal document.

### Intellectual Property Position

Afrispan's core methodology is currently published openly, a deliberate choice supporting credibility-building and thought leadership during the company's early market-entry phase. As client engagements begin, Afrispan should evaluate which specific implementation refinements, client-specific integrations, and the accumulated evaluation and benchmarking data itself, warrant protection as proprietary, distinct from the open methodology that remains public.

## 11. Operations Plan

### Delivery Model

Engagements follow a structured methodology: initial scoping and system inventory, assessment against the relevant frameworks, documented findings with evidence tagged honestly by strength, from automated and verified through to explicitly missing, and, where the engagement includes Service Line 5 or 6, implementation of the actual governance or automation infrastructure, followed by a defined verification step before an engagement is considered complete.

### Tooling

RAGAS, DeepEval, and Langfuse power the test harness and drift monitoring layer, real evaluation scoring, regression alarms watching for degradation over time, and full observability tracing behind every judgment made. Promptfoo drives adversarial payload testing and red-teaming, mapped to OWASP and MITRE ATLAS. n8n handles governance orchestration and human-oversight enforcement. GitHub Actions verifies the CI/CD pipeline. Claude Code delivers the engineering itself, with the same discipline of small, verified increments and honest status tagging used throughout Afrispan's own technical foundation.

### Near-Term Hiring Plan

Afrispan begins as a founder-led practice. The first hire, once revenue supports it, should be a delivery-focused engineer capable of extending the existing evaluation and orchestration codebase for client-specific engagements, followed by a Nigeria-based business development or client-relationship hire once the practice has real, referenceable case studies to sell against.

## 12. Founder and Team

### Steve Onyeke, Founder and AI Governance Lead

Over a decade of technology, risk, and governance experience built across Nigeria, the United Kingdom, and global technology platforms. Progressed into a dedicated Technology Risk and Data Governance Analyst role in a regulated environment, authoring data governance policy achieving full regulatory audit readiness and delivering bi-monthly C-suite risk reporting across a two-hundred-person organisation. In the United Kingdom, worked as a Cybersecurity and Data Risk Analyst for Althaus Digital, and brings direct, firsthand exposure to how a major global platform actually operates from stakeholder and community engagement work with Binance, one of the world's largest crypto exchanges. Currently an AI Quality Analyst on a Google-commissioned Gemini evaluation programme through Turing, performing large-scale model evaluation. Based in Manchester, United Kingdom, with West Africa as primary market focus and regular in-market presence planned.

This dual positioning, hands-on technical builder and enterprise governance professional, is itself a differentiator few AI assurance practices, in Nigeria or globally, can claim in one person. The technical portfolio underlying this plan was built, tested, and independently verified by the founder directly, not commissioned from a separate technical team.

## 13. Financial Plan

**HONEST STATUS, STATED PLAINLY:** Afrispan is currently founder-funded and pre-revenue. Every figure in this section is an illustrative planning assumption, built from stated inputs and reasoned estimates, not historical performance or a committed forecast. The structure below exists so real numbers can be dropped in as soon as pipeline and pricing data exist, not to present false precision today. Where a number cannot yet be defended with evidence, it is marked as such directly rather than smoothed over.

### Pricing Reference Points, Real Anchors, Not Invented Figures

Since no real client pricing history exists yet, illustrative figures in this plan are anchored against two real, sourced reference points rather than invented from nothing.

- **Local anchor:** Nigerian professional and consulting services firms commonly charge between 1,000,000 and 3,000,000 naira annually for ongoing advisory work, with standalone audit engagements commonly ranging from 500,000 naira upward, depending on complexity. Afrispan's fixed-scope assessments should be positioned within and below this range for an initial SME engagement, reflecting genuine accessibility rather than premium-consultancy pricing.

- **International anchor:** SME-scale IT security and compliance audits internationally commonly range from 1,000 to 5,000 US dollars, rising toward 15,000 US dollars annually for larger organisations, a useful ceiling reference for Afrispan's more technically involved engagements, such as Service Line 5 orchestration implementation, without assuming Nigerian SME budgets can bear the higher end of that range unmodified.

- **A formal reference framework worth adopting:** the Computer Professionals Registration Council of Nigeria publishes an official Scale of Professional Charges covering systems audit, quality assurance, and risk impact assessment and review, the same category of work Afrispan performs. Benchmarking Afrispan's own rate card against this published, government-recognised scale, once finalised pricing exists, adds a further layer of institutional credibility beyond an internally set rate.

### Illustrative Three-Year Revenue Model

Modelled bottom-up from the SOM in Section 4, not top-down from the full MSME market. Figures in naira, rounded, and explicitly illustrative.

|                                               |                           |                           |                           |
|-----------------------------------------------|---------------------------|---------------------------|---------------------------|
| **Revenue Line**                              | **Year 1 (Illustrative)** | **Year 2 (Illustrative)** | **Year 3 (Illustrative)** |
| Fixed-scope assessments (Service Lines 1-3)   | 6-10 engagements          | 18-25 engagements         | 35-50 engagements         |
| Orchestration implementation (Service Line 5) | 1-2 projects              | 5-8 projects              | 12-18 projects            |
| Monitoring subscriptions (recurring)          | 0-2 active                | 8-15 active               | 25-40 active              |
| Workflow automation (Service Line 6)          | 1-3 projects              | 6-10 projects             | 15-22 projects            |

These ranges are deliberately wide, reflecting genuine uncertainty at pre-revenue stage, not false confidence narrowed to look precise. They should be replaced with a single, defended figure per line once the first two or three real client contracts exist to anchor pricing and conversion assumptions.

### Illustrative Cost Structure

|                                           |                                           |                                                                                                       |
|-------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Cost Category**                         | **Year 1 Treatment**                      | **Notes**                                                                                             |
| Founder compensation                      | Deferred or minimal draw                  | Standard for a founder-funded pre-revenue practice; revisit once revenue covers a sustainable draw    |
| Cloud, API, and evaluation infrastructure | Modest, usage-based                       | Currently low given simulated-mode development; rises directly with paid, live client evaluation work |
| Incorporation and DPCO licensing          | One-time, front-loaded                    | Treated as a near-term milestone cost, not ongoing overhead                                           |
| Software and tooling subscriptions        | Modest, mostly free-tier through Year 1   | RAGAS, DeepEval, Langfuse, n8n, and Promptfoo all have workable free or low-cost tiers at this scale  |
| First hire (delivery engineer)            | Not assumed until revenue supports it     | Explicit trigger, not a fixed timeline; see Section 11                                                |
| Sales and business development            | Founder-led, direct relationship-building | No paid acquisition channel assumed in Year 1, per Section 9's channel strategy                       |

### Path to Break-Even, Stated as Logic, Not a Guaranteed Date

Given deferred founder compensation and minimal fixed overhead in Year 1, Afrispan's break-even point is primarily a function of covering infrastructure and licensing costs, a comparatively low bar reachable within a small number of fixed-scope engagements. The more meaningful milestone is not accounting break-even but reaching the point where recurring monitoring-subscription revenue covers the first paid hire described in Section 11, since that marks the transition from a founder-dependent practice to one with real delivery capacity beyond one person. This plan does not commit to a specific month for that transition, since it depends directly on real conversion data this practice does not yet have.

### Unit Economics, Framework Only

A defensible customer acquisition cost and lifetime value model requires real conversion and retention data this practice does not yet have. The framework Afrispan will populate once that data exists: acquisition cost measured primarily in founder time given the direct, relationship-led channel strategy in Section 9, and lifetime value measured as the sum of an initial assessment engagement plus the expected duration of a resulting monitoring subscription. Populating this honestly, once real, is a Year 1 priority, not a number to estimate speculatively today.

### Funding Position

Afrispan is currently self-funded by its founder. This plan is structured to support a future conversation with angel investors, grant programmes, or strategic partners, including Nigeria's own Start-Up Digital Innovation Academy investment-support track, once real client traction exists to demonstrate. No specific funding ask is made in this version of the plan; one should be added once a validated pipeline and realistic burn rate exist to size it against.

### Long-Term Value and Strategic Positioning

This section is deliberately directional, not a commitment or a valuation claim, offered because an institutional reader evaluating a funding relationship will reasonably ask what the long-term value of the business actually is, beyond annual engagement revenue.

Three realistic categories of long-term strategic value, each grounded in something already true about the market described in this plan, not speculation disconnected from it. First, Afrispan's accumulated evaluation methodology and, in time, its accumulated benchmark data across real Nigerian AI deployments becomes a genuinely defensible asset, the kind of proprietary dataset a larger regional or global compliance platform would value directly, not only Afrispan's client relationships. Second, as Nigeria's AI Governance Regulatory Body, described in Section 5, eventually is constituted and formal certification regimes emerge, an established, technically credible practice with real engagement history is well positioned to become an accredited partner or licensed assessor under that future regime, a position far harder for a new entrant to reach after the fact than to grow into from before it exists. Third, West African regional expansion via the Cross-Border Deployment Framework, if executed as planned in Section 9, positions Afrispan as a genuine platform play across a multi-country market, not a single-country consultancy, which materially changes the kind of acquirer or investor for whom the business becomes relevant over time, from a local professional-services buyer to a regional or global RegTech platform seeking African market entry.

None of these three paths is assumed or guaranteed. They are named here because a plan claiming institutional readiness should be honest that long-term value has not yet been tested against any of them, while showing that the underlying business is being built in a way that keeps all three genuinely open.

## 14. Risk Analysis

|                                       |                                                                                                              |                                                                                                                                                                                                  |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Risk**                              | **Description**                                                                                              | **Mitigation**                                                                                                                                                                                   |
| Regulatory timeline uncertainty       | Nigeria's Digital Economy and E-Governance Bill's exact passage date and final provisions remain unconfirmed | Build the plan's core value proposition on genuinely good governance practice, not solely on a specific bill passing exactly as reported, so the offering holds value regardless of exact timing |
| Market education burden               | Nigerian SMEs may not yet recognise AI governance as a distinct, purchasable need                            | Lead go-to-market with the fintech sector specifically, where CBN sandbox activity has already created real, existing demand                                                                     |
| Founder-dependency risk               | Practice currently depends entirely on one person's technical and delivery capacity                          | Prioritise hiring a delivery-focused engineer as the first hire once revenue allows, per Section 11                                                                                              |
| Competitive entry from global players | Large consultancies could enter the Nigerian SME AI assurance market directly                                | Compete on technical proof, price accessibility, and genuine local presence, not on scale                                                                                                        |
| Currency and macroeconomic volatility | Naira volatility affects both local pricing and any foreign-currency cost exposure                           | Price primarily in naira for the domestic Nigerian market, with clear, infrequent re-pricing reviews                                                                                             |

### Liability, Professional Indemnity, and Risk Allocation

Afrispan's core service is telling a client their AI system is, or is not, safe and compliant. This creates real professional liability exposure that a serious business plan cannot leave unaddressed, since it is exactly the gap an institutional reviewer, particularly a bank or insurer, will look for first.

- **Professional indemnity insurance:** Afrispan should carry professional indemnity cover appropriate to a technical assurance practice before its first paid engagement, not after. This is standard practice for audit, consulting, and compliance firms globally, and its absence would be a genuine, avoidable gap in an otherwise evidence-first business.

- **Contractual scope and limitation of liability:** every engagement contract should explicitly define what was assessed, against which named frameworks, and as of what date, with liability contractually limited to the fees paid for that specific engagement, standard professional-services practice, not an attempt to avoid accountability.

- **The evidentiary basis must be stated plainly to the client:** an assessment is only as strong as the access and information the client actually provides. Afrispan's own honesty-tagging discipline, described throughout Sections 6 and 10, applies here directly, findings based on direct evidence are distinguished contractually and in every report from findings based on client-attested information, so liability is allocated to match what was actually verified, not overstated.

**A Direct, Honest Note on This Section:** This plan does not, and should not, attempt to resolve Nigerian professional liability law itself. A qualified Nigerian corporate and insurance lawyer should review Afrispan's engagement contract template and confirm appropriate indemnity cover before the first paid client engagement is signed. Naming this as an explicit, near-term action item, rather than assuming it will be handled informally, is itself the discipline this practice is built on.

## 15. Roadmap and Milestones

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| **Timeframe**   | **Milestone**                                                                                                     |
| Immediate       | Finalise this business plan, launch the Afrispan website reflecting Nigeria-first positioning                     |
| Next 2 months   | Secure first 1 to 3 paid engagements in Lagos, fintech or digital-first SME focus                                 |
| Months 3 to 6   | Publish first client case study (anonymised if required), begin DPCO licensing process                            |
| Months 6 to 12  | Nigeria-wide expansion beyond Lagos, first hire once revenue supports it                                          |
| Months 12 to 24 | Ghana and ECOWAS expansion via Cross-Border Deployment Framework, revisit funding conversation with real traction |
| Ongoing         | Quarterly review of this plan's regulatory section given the pace of Nigeria's AI governance development          |

## 16. Appendix: Evidence and References

Full technical portfolio: github.com/Afrispan-AI/ai-governance-suite

Key regulatory sources cited in Section 5: Nigeria Data Protection Act 2023; National Artificial Intelligence Strategy, Federal Ministry of Communications, Innovation and Digital Economy, September 2025; National Digital Economy and E-Governance Bill, reported provisions as of 2026; independent policy analysis of NAIS implementation status, April 2026.

Key market data sources cited in Section 4: Small and Medium Enterprises Development Agency of Nigeria (SMEDAN); Mordor Intelligence Nigeria and Africa Digital Transformation Market reports, 2026; Nigerian Communications Commission subscriber data, December 2024; Government AI Readiness Index, 2025.

**A Final Note on This Document's Own Standard:** This plan applies the same evidentiary discipline to itself that Afrispan applies to every client engagement. Every regulatory and market claim is sourced. Every financial projection is labeled as an assumption, not a fact. Every technical capability referenced is real, tested, and publicly checkable. That discipline is not a formatting choice, it is the actual product Afrispan sells, applied here first.

**Afrispan AI Assurance \| Institutional Business Plan \| August 2026**
