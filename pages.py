# -*- coding: utf-8 -*-
"""Per-page content blocks for the Afrispan Data Labs site.

All copy is sourced from the Institutional Business Plan (August 2026) and
the founder-provided build brief. No figures are invented; where a claim is
illustrative or unresolved, it is stated as such. No em dashes are used
anywhere in this file, by house rule.
"""

GITHUB_URL = "https://github.com/Afrispan-Data-Labs/ai-governance-suite"

# ---------------------------------------------------------------------------
# Shared inline icons (simple stroke-based SVGs, no external icon library)
# ---------------------------------------------------------------------------

def icon(name):
    icons = {
        "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
        "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="16" y2="17"/></svg>',
        "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3.2 3 14.8 0 18"/><path d="M12 3c-3 3.2-3 14.8 0 18"/></svg>',
        "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>',
        "switch": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 1 0 3-6.2"/><polyline points="4 3 4 7 8 7"/></svg>',
        "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
        "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="8 6 2 12 8 18"/><polyline points="16 6 22 12 16 18"/></svg>',
        "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
        "flag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 22V4"/><path d="M4 4h13l-2 4 2 4H4"/></svg>',
        "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
        "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
    }
    return icons[name]


def status_tag(kind):
    labels = {"proven": "Proven", "building": "Building", "planned": "Planned"}
    return f'<span class="status-tag status-{kind}">{labels[kind]}</span>'


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

HOME_TITLE = "Afrispan Data Labs | Independent AI Deployment Assurance for Nigeria and West Africa"
HOME_DESC = "Afrispan Data Labs independently verifies that AI systems deployed by Nigerian and West African enterprises are safe, compliant, and governed, with evidence, not vendor assertion."

HOME_CONTENT = f"""
<section class="hero">
  <div class="container">
    <span class="eyebrow">Nigeria's AI Governance Window Is Open</span>
    <h1>Prove your AI systems are governed, before the law requires it.</h1>
    <p class="lede">Afrispan Data Labs is an independent AI deployment assurance practice for Nigerian and West African enterprises. We verify what your AI systems actually do, with evidence, not vendor assertion, the same discipline financial audit has applied to accounting for a century, now applied to AI.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="contact.html">Book a discovery call</a>
      <a class="btn btn-secondary" href="{GITHUB_URL}" target="_blank" rel="noopener">View the technical portfolio on GitHub</a>
    </div>
    <div class="stat-strip">
      <div class="stat"><span class="num">22</span><span class="label">obligations scored per Conformity Assessment</span></div>
      <div class="stat"><span class="num">4</span><span class="label">frameworks assessed simultaneously: EU AI Act, NIST AI RMF, NIST AI 600-1, ISO/IEC 42001</span></div>
      <div class="stat"><span class="num">5</span><span class="label">governance principles proven across 9 executed phases</span></div>
      <div class="stat"><span class="num">100%</span><span class="label">open source and publicly verifiable on GitHub</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="kicker">The Regulatory Argument</span>
      <h2>Nigeria's AI obligations are coming. The enforcement body isn't ready yet.</h2>
      <p>Nigeria published its National Artificial Intelligence Strategy in September 2025, a five-year vision to 2029. A National Digital Economy and E-Governance Bill, expected to pass in 2026, would give NITDA formal, risk-based regulatory authority over AI, including mandatory licensing and annual impact assessments for high-risk systems in finance, public administration, and automated decision-making. Penalties reach 10 million naira or 2 percent of annual gross revenue, whichever is higher.</p>
    </div>
    <div class="callout callout-orange">
      <span class="callout-label">The honest, verified gap</span>
      <p>As of March 2026, Nigeria's own independent AI Governance Regulatory Body, the strategy's own capstone institution, has not been constituted, and NITDA's Code of Practice for AI remains unfinalized. Enterprises know binding obligations are coming, but there is no operational government channel yet to prepare against them.</p>
    </div>
    <p>Private-sector assurance, built to the rigor the eventual law will demand, is the practical bridge, not a workaround. The mandatory annual impact assessment described in the coming bill is functionally the same deliverable as Afrispan's own Conformity Report and FRIA tooling, already built and demonstrable today.</p>
    <a class="btn btn-outline-navy" href="regulatory-case.html">Read the full regulatory case &rarr;</a>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">What We Do</span>
      <h2>Six ways we help you prove your AI systems are governed</h2>
      <p>Every service line is grounded in a real, working technical capability, not a description written ahead of the capability existing.</p>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <div class="icon-badge">{icon('shield')}</div>
        <h3>Regulatory Conformity Assessment</h3>
        <p>Scored against EU AI Act, NIST AI RMF, NIST AI 600-1, and ISO/IEC 42001 simultaneously. Untested obligations marked, never omitted.</p>
        {status_tag('proven')}
      </div>
      <div class="card">
        <div class="icon-badge">{icon('doc')}</div>
        <h3>Fundamental Rights and Impact Assessment</h3>
        <p>Aligned directly with Nigeria's coming annual impact assessment requirement, with every finding tagged by its evidentiary basis.</p>
        {status_tag('proven')}
      </div>
      <div class="card">
        <div class="icon-badge">{icon('globe')}</div>
        <h3>Cross-Border Deployment Framework</h3>
        <p>An honest check of whether your compliance evidence actually transfers between Nigeria, Ghana, and wider ECOWAS.</p>
        {status_tag('proven')}
      </div>
      <div class="card">
        <div class="icon-badge">{icon('eye')}</div>
        <h3>Evaluation and Red-Team Engagement</h3>
        <p>Cross-model judging, adversarial testing mapped to OWASP LLM and Agentic Top 10 and MITRE ATLAS, and drift monitoring.</p>
        {status_tag('building')}
      </div>
      <div class="card">
        <div class="icon-badge">{icon('switch')}</div>
        <h3>Governance Orchestration and Human Oversight</h3>
        <p>Live infrastructure, not policy documents: automated routing, an independent kill-switch, and a named-person resume mechanism.</p>
        {status_tag('proven')}
      </div>
      <div class="card">
        <div class="icon-badge">{icon('bolt')}</div>
        <h3>Complex Workflow Automation, Governed by Design</h3>
        <p>AI-powered business automation with the same assurance discipline built in from day one, not retrofitted after deployment.</p>
        {status_tag('building')}
      </div>
    </div>
    <p style="margin-top:28px;"><a class="btn btn-outline-navy" href="services.html">See the full detail on each service line &rarr;</a></p>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="kicker">Technical Proof</span>
      <h2>Built and demonstrated, not just proposed</h2>
      <p>Afrispan's technical capability is not aspirational. It spans three connected open-source projects, publicly demonstrable on GitHub, so a technical stakeholder can verify the work directly rather than take a claim on faith.</p>
    </div>
    <div class="grid grid-3">
      <div class="card-flat">
        <span class="service-number">Project 1</span>
        <h4>Nine governance phases</h4>
        <p>Real Gemini API execution throughout. A working kill-switch with immutable, hash-chained audit logging. The FRIA, Conformity Report, and Cross-Border Framework generators.</p>
        {status_tag('proven')}
      </div>
      <div class="card-flat">
        <span class="service-number">Project 2</span>
        <h4>Production evaluation architecture</h4>
        <p>Thirteen notebooks, cross-model judging, red-teaming mapped to OWASP and MITRE ATLAS, a verified CI/CD pipeline on GitHub Actions.</p>
        {status_tag('building')}
      </div>
      <div class="card-flat">
        <span class="service-number">Project 3</span>
        <h4>Live governance orchestration</h4>
        <p>Three-queue routing, a shared kill-switch gate, pre-committed evaluation verdicts, and a real-time dashboard, built and verified on real hardware.</p>
        {status_tag('proven')}
      </div>
    </div>
    <p style="margin-top:28px;"><a class="btn btn-outline-navy" href="proof.html">See the full technical portfolio &rarr;</a></p>
  </div>
</section>

<section class="section-paper">
  <div class="container">
    <div class="section-head">
      <span class="kicker">About the Founder</span>
      <h2>Built by someone who has done both sides of this work</h2>
    </div>
    <div class="founder-card">
      <div class="founder-content">
        <span class="founder-role">Steve Onyeke, Founder and AI Product Lead</span>
        <p>Steve brings over eight years of enterprise technology risk and data governance experience, including as a Technology Risk and Data Governance Analyst in a regulated healthtech environment, where he authored data governance policy that achieved full regulatory audit readiness and delivered bi-monthly C-suite risk reporting across a two-hundred-person organisation.</p>
        <p>He is currently an AI Quality Analyst on a Google-commissioned Gemini evaluation programme delivered through Turing, performing large-scale side-by-side model evaluation. He holds an MBA from Nexford University and a BSc in Computer Science from the University of Jos, and is based in Manchester, United Kingdom, with West Africa as Afrispan's primary market and regular in-market presence planned.</p>
        <p>Few AI assurance practices, in Nigeria or globally, can pair hands-on technical evaluation work with enterprise governance experience in one person. That combination is why Afrispan's assessments look at how a system actually behaves, not only at what its policy documents claim.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band">
      <h2>Ready to see where your AI systems actually stand?</h2>
      <p>Start with a direct conversation about your system and context, not a signup form.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Book a discovery call</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# THE REGULATORY CASE
# ---------------------------------------------------------------------------

REG_TITLE = "The Regulatory Case | Afrispan Data Labs"
REG_DESC = "Why Nigeria's coming AI regulation creates a real, time-bound window for private-sector assurance, sourced from Nigeria's National AI Strategy and the National Digital Economy and E-Governance Bill."

REG_CONTENT = f"""
<section class="hero-page section-navy">
  <div class="container">
    <span class="eyebrow">The Regulatory Case</span>
    <h1>The law is coming. The enforcement channel isn't built yet.</h1>
    <p class="lede">This is the sharpest, most current argument behind Afrispan's existence, and it is fully sourced. Every claim below traces to Nigeria's own published strategy documents, an independent policy analysis, or official government reporting.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="kicker">Timeline</span>
      <h2>How Nigeria's AI regulatory landscape has moved</h2>
    </div>
    <div class="timeline">
      <div class="timeline-item">
        <span class="timeline-date">September 2025</span>
        <h3>National Artificial Intelligence Strategy published</h3>
        <p>Published by the Federal Ministry of Communications, Innovation and Digital Economy, with NITDA as principal implementing body. It sets a five-year vision, 2025 to 2029, structured around three goals and five operational pillars, including sector adoption, responsible AI, and governance.</p>
      </div>
      <div class="timeline-item">
        <span class="timeline-date">November 2025</span>
        <h3>Public hearing on the Digital Economy and E-Governance Bill</h3>
        <p>Nigeria's National Digital Economy and E-Governance Bill, expected to pass in 2026, would position NITDA as Nigeria's digital technology super-regulator.</p>
      </div>
      <div class="timeline-item">
        <span class="timeline-date">Expected 2026</span>
        <h3>Bill expected to pass, with real, binding obligations</h3>
        <p>Reported provisions include a risk-based framework naming finance, public administration, surveillance, and automated decision-making as high-risk categories, requiring formal licensing and mandatory annual impact assessments detailing risks, mitigation strategies, and system performance. Regulators would gain powers to demand information, issue directives, and block unsafe systems. Reported penalties reach 10 million naira, approximately 7,000 US dollars, or 2 percent of a company's annual gross revenue, whichever is higher.</p>
      </div>
      <div class="timeline-item is-gap">
        <span class="timeline-date">As of March 2026</span>
        <h3>The honest, verified gap: the oversight body isn't constituted</h3>
        <p>An independent policy analysis published in April 2026 found that, as of March 2026, NITDA's own Code of Practice for AI (2025) had not been finalised, and the independent AI Governance Regulatory Body the strategy itself calls for under its fifth pillar had not been constituted, with no published timeline, funding mechanism, or defined legal independence.</p>
      </div>
    </div>

    <div class="callout callout-orange">
      <span class="callout-label">The structural concern this raises</span>
      <p>The same analysis raised a concern worth naming directly and honestly: NITDA's own AI Transformation Roadmap assigns governance functions to NITDA itself, a body that also promotes AI development, a potential conflict of interest the analysis argues should be resolved by constituting the independent oversight body before, not after, the Code of Practice is finalised.</p>
    </div>

    <div class="callout callout-green">
      <span class="callout-label">The argument this creates</span>
      <p>Enterprises know binding obligations are coming, but there is no clear, currently operating government channel to prepare against them. Private-sector assurance, built to the same rigor the eventual regulation will demand, is the practical way to close that gap today, not a workaround, a necessary bridge. For Afrispan, this finding is treated as an opportunity to be transparent about, not exploited quietly. It means the practical, operational channel for an enterprise seeking real AI governance capability in Nigeria today is not yet a government one.</p>
    </div>

    <h2>Why this matters for your business, concretely</h2>
    <p>The mandatory annual impact assessment described in the coming bill is functionally the same deliverable as Afrispan's own Conformity Report and Fundamental Rights and Impact Assessment tooling, already built and demonstrable today, months or years ahead of the obligation becoming mandatory. Enterprises that engage Afrispan now are not buying a speculative future service. They are building the exact evidence artifact the coming law will require, before they are legally compelled to.</p>

    <hr class="divider">

    <h2>The existing legal foundation, and an adjacent licensing path worth pursuing</h2>
    <p>The Nigeria Data Protection Act 2023 (NDPA) and the Nigeria Data Protection Commission (NDPC) it established remain the primary binding legal foundation for data governance obligations that intersect directly with AI deployment today. Nigeria does not yet have a dedicated, binding AI-specific law. AI-related obligations today are drawn from general principles, contract law, data protection, and product liability, applied to AI systems by extension.</p>
    <p>Nigeria's data protection framework already recognises Licensed Data Protection Compliance Organisations (DPCOs) as a formal third-party category authorised to support compliance and audit work under the NDPA. Afrispan is evaluating DPCO licensing as a near-term strategic milestone, since it provides an existing, government-recognised credential adjacent to Afrispan's AI-specific work, ahead of any AI-specific licensing regime that may follow the Digital Economy and E-Governance Bill's eventual passage.</p>

    <h2>A live, sector-specific precedent</h2>
    <p>The Central Bank of Nigeria's regulatory sandbox, launched in 2023 and expanded through 2024 and 2025, already evaluates AI-powered fintech tools for model explainability, fairness, and consumer transparency before granting approvals, a real, current precedent for exactly the kind of independent evaluation work Afrispan performs, applied specifically to Nigeria's large and fast-growing fintech sector.</p>

    <div class="cta-band" style="margin-top:48px;">
      <h2>See how our service lines map to these obligations</h2>
      <p>Every service line below exists because of a specific, sourced gap in what Nigeria's coming regulation will require and what is operationally available today.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="services.html">Explore service lines</a>
        <a class="btn btn-secondary" href="contact.html">Talk to us</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# SERVICES
# ---------------------------------------------------------------------------

SERVICES_TITLE = "Service Lines | Afrispan Data Labs"
SERVICES_DESC = "Six service lines, from Regulatory Conformity Assessment to Governance Orchestration, each grounded in a real, working technical capability and tagged honestly by its status."

def _service_block(number, anchor, title, status_kind, icon_name, body_paragraphs, extra=""):
    paras = "".join(f"<p>{p}</p>" for p in body_paragraphs)
    return f"""
    <div class="service-block" id="{anchor}">
      <div class="service-head">
        <div>
          <span class="service-number">Service Line {number}</span>
          <h2 class="mt-0">{title}</h2>
        </div>
        <div class="icon-badge" style="margin-bottom:0;">{icon(icon_name)}</div>
      </div>
      {status_tag(status_kind)}
      <div style="margin-top:16px;">
        {paras}
      </div>
      {extra}
    </div>
    """

SERVICES_CONTENT = f"""
<section class="hero-page section-navy">
  <div class="container">
    <span class="eyebrow">Service Lines</span>
    <h1>Six ways we help you prove your AI systems are governed</h1>
    <p class="lede">Every service Afrispan offers is grounded in a real, working technical capability, publicly demonstrable on GitHub, not a service description written ahead of the capability existing. Each line below is tagged honestly by its actual status.</p>
    <div class="jump-nav">
      <a href="#conformity">1. Conformity Assessment</a>
      <a href="#fria">2. Impact Assessment</a>
      <a href="#cross-border">3. Cross-Border Framework</a>
      <a href="#evaluation">4. Evaluation and Red-Team</a>
      <a href="#orchestration">5. Governance Orchestration</a>
      <a href="#automation">6. Workflow Automation</a>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    {_service_block(1, "conformity", "Regulatory Conformity Assessment", "proven", "shield", [
        "A structured assessment scoring your AI system against multiple regulatory and standards frameworks simultaneously: EU AI Act, NIST AI RMF, NIST AI 600-1, and ISO/IEC 42001, with Nigeria's own emerging framework mapped in directly as it finalises.",
        "Built on Afrispan's own twenty-two-obligation Conformity Report methodology. Untested obligations are marked as such explicitly, never silently omitted, the same evidentiary honesty a real audit demands.",
    ])}

    {_service_block(2, "fria", "Fundamental Rights and Impact Assessment", "proven", "doc", [
        "A structured, documented assessment of your AI system's impact on the people it affects, directly aligned with the annual impact assessment expected under Nigeria's coming AI legislation.",
        "Generated from a real audit trail wherever automated evidence exists, with every field tagged as automated, attested by direct client input, or explicitly missing, never filled with a plausible guess.",
    ])}

    {_service_block(3, "cross-border", "Cross-Border Deployment Framework", "proven", "globe", [
        "For clients operating or expanding across West Africa, an honest assessment of whether compliance evidence actually transfers between Nigeria, Ghana, and the wider ECOWAS market, rather than an assumption that it does.",
        "Given the African Continental Free Trade Area's active push toward regional MSME trade integration, this is a direct, near-term need for Nigerian enterprises expanding into Ghana and the wider ECOWAS market.",
    ])}

    {_service_block(4, "evaluation", "Evaluation and Red-Team Engagement", "building", "eye", [
        "Technical evaluation of an AI system's actual behaviour. Cross-model judging avoids the self-audit blind spot our own testing has measured directly: a same-family AI judge evaluating identical output showed a 0.15 point quality inflation and a 0.23 point gap in catching real errors, compared to an independent, cross-model evaluator.",
        "Adversarial red-teaming is mapped to the OWASP LLM and Agentic Top 10 and MITRE ATLAS taxonomies, with drift monitoring to catch a system quietly degrading over time, not only when it fails outright.",
        "Stated honestly: the evaluation architecture is complete and pytest-verified, but most notebooks run in simulated mode pending funded API billing. This is stated plainly wherever relevant, never implied otherwise.",
    ])}

    {_service_block(5, "orchestration", "Governance Orchestration and Human Oversight Enforcement", "proven", "switch", [
        "The service line that distinguishes Afrispan most sharply from a traditional audit or consulting practice: live infrastructure that makes governance operational, not a policy document describing what a client should build themselves.",
        "Automated routing sends AI decisions to confident-pass, confident-fail, or human-review queues. A kill-switch halts automated action immediately and independently the moment a serious finding occurs. A resume mechanism requires a named, accountable person to record a substantive decision, not a single approval click, before automated operation continues.",
        "This is the first phase of Afrispan's technical portfolio to reach a real milestone: built, tested, and verified on real local hardware, not simulated.",
    ])}

    {_service_block(6, "automation", "Complex Workflow Automation, Governed by Design", "building", "bolt", [
        "For clients whose need extends beyond assessment into building the AI-powered automation itself, sales, customer support, lead management, and internal operations, Afrispan designs and implements the automation with the same assurance discipline built in from the start, not retrofitted after deployment.",
        "This builds directly on the orchestration technology proven in Service Line 5, and positions Afrispan to serve a client across their full AI adoption journey, not only at the assurance layer.",
    ])}
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Why This Is A Real Gap</span>
      <h2>No competitor on Nigeria's own licensed auditor registry does this</h2>
    </div>
    <div class="table-wrap">
      <table class="data-table">
        <thead>
          <tr><th>Organisation</th><th>Type</th><th>Relevant detail</th></tr>
        </thead>
        <tbody>
          <tr><td>EY and KPMG Advisory Services</td><td>Global Big Four affiliates, licensed DPCOs in Nigeria</td><td>Real, confirmed local presence, priced for large enterprise, not SME budgets</td></tr>
          <tr><td>DataPro Limited</td><td>Nigerian compliance consultancy, licensed DPCO</td><td>Publicly positions itself as having the most extensive compliance consulting background among licensed DPCOs</td></tr>
          <tr><td>Pavestones Legal</td><td>Law firm operating as a licensed DPCO</td><td>Legal-first framing, general data protection audit, no published AI-specific evaluation methodology</td></tr>
          <tr><td>Hephzibah Integrated Technologies</td><td>Abuja-based IT and data consulting firm, licensed DPCO</td><td>Positions itself as a niche IT and data consultancy across public and private sector clients</td></tr>
          <tr><td>Johan Consults Ltd</td><td>Licensed DPCO</td><td>General data protection compliance consulting</td></tr>
        </tbody>
      </table>
    </div>
    <div class="callout">
      <span class="callout-label">The real, sourced gap this reveals</span>
      <p>Every organisation on Nigeria's own licensed DPCO list is a general data protection auditor, a law firm, an accounting affiliate, or a generalist IT consultancy. None publish a technical methodology for evaluating an AI system's actual behaviour: cross-model judging to catch a same-family evaluator's blind spots, adversarial red-teaming mapped to OWASP or MITRE ATLAS, or drift monitoring to catch a system degrading over time. That is the precise, sourced gap Afrispan is built to fill, not a claimed differentiation, a documented absence in the current market.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band">
      <h2>See how engagements are structured</h2>
      <p>No published rate card yet, engagement pricing is still being validated against real client conversations. Here is how the engagement types work.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="engagement.html">View engagement types</a>
        <a class="btn btn-secondary" href="contact.html">Book a discovery call</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# PROOF (technical portfolio)
# ---------------------------------------------------------------------------

PROOF_TITLE = "Technical Proof | Afrispan Data Labs"
PROOF_DESC = "The full, verifiable technical portfolio behind Afrispan's service lines: three GitHub projects, nine governance phases, a production evaluation architecture, and live governance orchestration."

PROOF_CONTENT = f"""
<section class="hero-page section-navy">
  <div class="container">
    <span class="eyebrow">Technical Proof</span>
    <h1>Verify the work yourself. Don't take our word for it.</h1>
    <p class="lede">Every service Afrispan offers is grounded in a real, working technical capability, publicly demonstrable on GitHub, not a service description written ahead of the capability existing.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="{GITHUB_URL}" target="_blank" rel="noopener">View the full portfolio on GitHub</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="kicker">Governance Principles</span>
      <h2>Five principles this work has proven, not assumed</h2>
      <p>Discovered across nine executed phases of real, working evaluation and orchestration, not derived from theory.</p>
    </div>
    <div class="grid grid-3">
      <div class="card-flat">
        <div class="icon-badge">{icon('eye')}</div>
        <h4>An AI system cannot audit itself</h4>
        <p>The most common form of AI quality assurance available today is the vendor's own claim that its system works correctly. This is structurally unreliable, because an AI system judging its own output shares the same blind spots as the system being evaluated.</p>
      </div>
      <div class="card-flat">
        <div class="icon-badge">{icon('compass')}</div>
        <h4>Surface pattern-matching fails at the edges</h4>
        <p>Systems that appear to work reliably on typical cases can fail precisely where the judgment matters most, at the edge cases a governance process is meant to catch.</p>
      </div>
      <div class="card-flat">
        <div class="icon-badge">{icon('layers')}</div>
        <h4>Monitoring is not governing</h4>
        <p>Watching a system and having the authority and mechanism to stop or correct it are two different capabilities. A dashboard that only observes is not a governance control.</p>
      </div>
      <div class="card-flat">
        <div class="icon-badge">{icon('shield')}</div>
        <h4>Authority is not judgment</h4>
        <p>A mechanism that can halt a system is not the same as one that can decide correctly what to do next. Real oversight requires a named, accountable person exercising judgment, not just a switch.</p>
      </div>
      <div class="card-flat">
        <div class="icon-badge">{icon('check')}</div>
        <h4>Judge and human disagreement is diagnostic, not noise</h4>
        <p>When a cross-model judge and a human reviewer disagree, that disagreement is signal worth investigating, not error to be averaged away. Afrispan's own testing measured a 0.15 point quality inflation and a 0.23 point gap in error detection between a same-family judge and an independent, cross-model evaluator.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">The Portfolio</span>
      <h2>Three connected projects, full commit history intact</h2>
      <p>Published openly at <a href="{GITHUB_URL}" target="_blank" rel="noopener">github.com/Afrispan-Data-Labs/ai-governance-suite</a>, migrated with full commit history from the founder's original personal repository.</p>
    </div>
    <div class="table-wrap">
      <table class="data-table">
        <thead>
          <tr><th>Project</th><th>Scope</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr>
            <td>Project 1</td>
            <td>Nine phases proving core governance principles, including a real, working kill-switch with immutable, hash-chained audit logging, and the FRIA, Conformity Report, and Cross-Border Framework generators</td>
            <td>{status_tag('proven')}<div class="small-note" style="margin-top:6px;">Complete, executed against real API calls</div></td>
          </tr>
          <tr>
            <td>Project 2</td>
            <td>Thirteen-notebook production evaluation suite, cross-model judging, red-teaming mapped to OWASP and MITRE ATLAS, a verified CI/CD pipeline on GitHub Actions</td>
            <td>{status_tag('building')}<div class="small-note" style="margin-top:6px;">Architecture complete and pytest-verified; most notebooks run in simulated mode pending funded API billing</div></td>
          </tr>
          <tr>
            <td>Project 3</td>
            <td>Live governance orchestration in n8n: three-queue PR routing with non-blocking human review, a kill-switch converging drift alarms and red-team findings into one shared gate, pre-committed evaluation verdicts, and a real-time dashboard</td>
            <td>{status_tag('proven')}<div class="small-note" style="margin-top:6px;">Built, tested, and verified on real local hardware, the first phase of this portfolio to reach that status</div></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="callout callout-green">
      <span class="callout-label">A gap closed on external review</span>
      <p>Project 3's pre-committed verdict design closes a real gap named by an external reviewer, Federico Blanco Sanchez-Llanos, before that gap could reach a client engagement.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="kicker">Tooling</span>
      <h2>What this is actually built on</h2>
    </div>
    <div class="grid grid-3">
      <div class="card-flat"><h4>Evaluation and observability</h4><p>RAGAS, DeepEval, and Langfuse.</p></div>
      <div class="card-flat"><h4>Red-teaming</h4><p>Promptfoo, mapped to OWASP LLM and Agentic Top 10, and MITRE ATLAS.</p></div>
      <div class="card-flat"><h4>Governance orchestration</h4><p>n8n, for automated routing and human-oversight enforcement.</p></div>
      <div class="card-flat"><h4>CI/CD verification</h4><p>GitHub Actions, for a verified, repeatable pipeline.</p></div>
      <div class="card-flat"><h4>Engineering delivery</h4><p>Claude Code, with the same discipline of small, verified increments and honest status tagging used throughout this portfolio.</p></div>
      <div class="card-flat"><h4>Original repository</h4><p>The founder's original personal repository at github.com/steveonyeke/python-ai-governance carries a note pointing to the current organisation repository and remains archived, not deleted.</p></div>
    </div>
  </div>
</section>

<section class="section-navy">
  <div class="container">
    <div class="cta-band" style="background:transparent; padding:0;">
      <h2>Go look at the actual code</h2>
      <p>A technical stakeholder should be able to verify this work directly, not take a claim on faith.</p>
      <div class="hero-ctas">
        <a class="btn btn-light" href="{GITHUB_URL}" target="_blank" rel="noopener">View the repository on GitHub</a>
        <a class="btn btn-secondary" href="contact.html">Discuss an engagement</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# ENGAGEMENT
# ---------------------------------------------------------------------------

ENGAGEMENT_TITLE = "Engagement | Afrispan Data Labs"
ENGAGEMENT_DESC = "How Afrispan engagements are structured: fixed-scope assessments, implementation and orchestration projects, ongoing monitoring, and workflow automation. Scoped and quoted directly, no published rate card yet."

ENGAGEMENT_CONTENT = f"""
<section class="hero-page section-navy">
  <div class="container">
    <span class="eyebrow">Engagement</span>
    <h1>How engagements are structured</h1>
    <p class="lede">Afrispan is currently founder-funded and pre-revenue, and has not yet validated pricing against a real client engagement. Rather than publish a rate card ahead of that validation, here is the shape of how each engagement type works. Every engagement is scoped and quoted directly, after a discovery conversation about your specific system.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-2">
      <div class="tier-card">
        <span class="tier-name">Fixed-Scope Assessment Engagement</span>
        <span class="tier-for">Best for: a first, defined-scope engagement to establish your baseline</span>
        <div class="tier-price">Scoped and quoted per engagement</div>
        <ul class="tier-list">
          <li>A defined Conformity Report, FRIA, or Cross-Border Framework deliverable</li>
          <li>Scored against relevant frameworks simultaneously</li>
          <li>Untested obligations marked explicitly, never silently omitted</li>
          <li>A concrete, reviewable deliverable, not an open-ended retainer</li>
        </ul>
      </div>
      <div class="tier-card">
        <span class="tier-name">Implementation and Orchestration Project</span>
        <span class="tier-for">Best for: building live governance infrastructure, Service Line 5</span>
        <div class="tier-price">Priced per project, reflecting integration scope</div>
        <ul class="tier-list">
          <li>Automated decision routing to pass, fail, or human-review queues</li>
          <li>An independent kill-switch and named-person resume mechanism</li>
          <li>Built on real, demonstrated orchestration infrastructure</li>
          <li>A defined verification step before the engagement is considered complete</li>
        </ul>
      </div>
      <div class="tier-card">
        <span class="tier-name">Ongoing Monitoring Subscription</span>
        <span class="tier-for">Best for: continued assurance once initial governance infrastructure is in place</span>
        <div class="tier-price">Recurring, scoped after an initial engagement</div>
        <ul class="tier-list">
          <li>Continued drift monitoring and regression alerting</li>
          <li>Periodic re-assessment as your AI system evolves</li>
          <li>The natural next step after an initial engagement, not a required starting point</li>
        </ul>
      </div>
      <div class="tier-card">
        <span class="tier-name">Workflow Automation Project</span>
        <span class="tier-for">Best for: clients whose primary need is automation, with governance built in</span>
        <div class="tier-price">Priced per project</div>
        <ul class="tier-list">
          <li>AI-powered automation for sales, support, lead management, or internal operations</li>
          <li>The same assurance discipline built in from day one</li>
          <li>Often the entry point for a client, with governance capability introduced in the same engagement</li>
        </ul>
      </div>
    </div>

    <div class="callout" style="margin-top:8px;">
      <span class="callout-label">How pricing is being approached</span>
      <p>Afrispan's pricing is being developed to be genuinely accessible to Nigerian SMEs, not a scaled-down version of global consultancy rates, anchored against real Nigerian professional-services benchmarks and international SME compliance-audit reference points, not invented figures. A published rate card will follow once pricing has been validated against real client engagements. Until then, every quote reflects your specific system, scope, and evidence needs, discussed directly.</p>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="cta-band" style="background:var(--white); border:1px solid var(--line);">
      <h2 style="color:var(--navy);">Get a scoped quote for your system</h2>
      <p style="color:var(--ink-soft);">Start with a discovery conversation. No commitment, no login required.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="contact.html">Book a discovery call</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------

CONTACT_TITLE = "Contact | Afrispan Data Labs"
CONTACT_DESC = "Start a conversation about your AI system with Afrispan Data Labs. No client portal, no signup form, just a direct discovery conversation."

CONTACT_CONTENT = f"""
<section class="hero-page section-navy">
  <div class="container">
    <span class="eyebrow">Contact</span>
    <h1>Start with a conversation, not a login.</h1>
    <p class="lede">Afrispan does not run a self-service platform or a client portal today, deliberately. Every engagement starts with a direct conversation about your specific system and context.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-2">
      <div>
        <h2>Reach us directly</h2>
        <p><a class="btn btn-primary" href="mailto:contact@afrispan.com">Email contact@afrispan.com</a></p>
        <p class="small-note">Afrispan's domain registration is in progress, so this address may not be receiving mail yet. Until it is confirmed live, the GitHub organisation page below is the current, working point of contact.</p>
        <ul class="tier-list" style="margin-top:20px;">
          <li>Operating base: Lagos, Nigeria</li>
          <li>Remote-first, with regular in-market presence planned</li>
          <li>Primary market: Nigeria, Lagos fintech and digital-first SMEs first</li>
        </ul>
        <p style="margin-top:20px;"><a href="{GITHUB_URL}" target="_blank" rel="noopener">View the technical portfolio on GitHub &rarr;</a></p>
      </div>
      <div>
        <h2>What to expect</h2>
        <div class="timeline">
          <div class="timeline-item">
            <span class="timeline-date">Step 1</span>
            <h4>Tell us about your system</h4>
            <p>A short conversation about what your AI system does, who it affects, and what evidence already exists.</p>
          </div>
          <div class="timeline-item">
            <span class="timeline-date">Step 2</span>
            <h4>We scope the right engagement</h4>
            <p>Conformity Assessment, FRIA, Evaluation, Orchestration, or a combination, matched to your actual need and stage.</p>
          </div>
          <div class="timeline-item">
            <span class="timeline-date">Step 3</span>
            <h4>We agree deliverables before work begins</h4>
            <p>A clear, reviewable deliverable and evidence standard, agreed upfront, not an open-ended retainer.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="callout" style="margin-top:44px;">
      <span class="callout-label">An honest note on where Afrispan is today</span>
      <p>Afrispan is a founder-funded, pre-revenue practice, actively finalising its engagement contract terms and confirming professional indemnity cover ahead of its first paid engagements. Nothing on this site constitutes a guarantee of regulatory outcome, a certification, or legal advice. Every assessment's findings are stated honestly by their evidentiary basis, and every engagement contract will define its scope and liability explicitly before work begins.</p>
    </div>
  </div>
</section>
"""
