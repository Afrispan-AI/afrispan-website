#!/usr/bin/env python3
"""Static site builder for the Afrispan Data Labs website.

Renders shared header/nav/footer around per-page content blocks so all six
pages stay visually and structurally consistent. Output is flat, dependency-
free HTML written to the project root, ready to deploy to any static host.
"""
import re

GITHUB_URL = "https://github.com/Afrispan-Data-Labs/ai-governance-suite"
SITE_NAME = "Afrispan Data Labs"
DOMAIN = "afrispan.com"
CONTACT_EMAIL = f"contact@{DOMAIN}"
X_URL = "https://x.com/afrispan"
LINKEDIN_URL = "https://linkedin.com/company/afrispan-data-labs"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("regulatory-case.html", "The Regulatory Case"),
    ("services.html", "Services"),
    ("proof.html", "Proof"),
    ("engagement.html", "Engagement"),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/images/favicon-180.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/images/favicon-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="status-banner">
  <span><strong>Nigeria's AI Digital Economy and E-Governance Bill</strong> is expected to pass in 2026. The independent oversight body it creates has not yet been constituted. <a href="regulatory-case.html" style="color:#fff;text-decoration:underline;">See the regulatory case &rarr;</a></span>
</div>
<header class="site-header">
  <div class="nav-inner">
    <a class="brand" href="index.html" aria-label="{site_name} home">
      <img class="wordmark" src="assets/images/afrispan-wordmark-trimmed.png" alt="{site_name}">
    </a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
    <nav class="primary-nav" aria-label="Primary">
      {nav_links}
      <a class="nav-cta" href="contact.html">Book a discovery call</a>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOTER = """</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="assets/images/afrispan-badge-circle.png" alt="" style="width:38px;height:38px;border-radius:50%;">
          <span>AFRISPAN<br><small>DATA LABS</small></span>
        </div>
        <p style="color:#AAB9D6; max-width: 320px;">Independent AI deployment assurance for Nigerian and West African enterprises. Evidence-based verification, not vendor assertion.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="regulatory-case.html">The Regulatory Case</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="proof.html">Proof</a></li>
        </ul>
      </div>
      <div>
        <h4>Work With Us</h4>
        <ul>
          <li><a href="engagement.html">Engagement</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="{github}" target="_blank" rel="noopener">GitHub Portfolio</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{email}">{email}</a></li>
          <li><a href="{x_url}" target="_blank" rel="noopener">X: @afrispan</a></li>
          <li><a href="{linkedin_url}" target="_blank" rel="noopener">LinkedIn</a></li>
          <li>Lagos, Nigeria (operating base)</li>
          <li>West Africa focus, remote-first</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Afrispan Data Labs. Founder-funded and pre-revenue.</span>
      <span>Engagement terms and professional indemnity cover are being finalized ahead of first paid engagements.</span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def render_nav_links(active_file):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active_file else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n      ".join(links)


def build_page(active_file, title, description, content):
    head = HEAD.format(
        title=title,
        description=description,
        nav_links=render_nav_links(active_file),
        site_name=SITE_NAME,
    )
    footer = FOOTER.format(github=GITHUB_URL, email=CONTACT_EMAIL, site_name=SITE_NAME, x_url=X_URL, linkedin_url=LINKEDIN_URL)
    html = head + content + footer
    return html


def write(filename, title, description, content):
    html = build_page(filename, title, description, content)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {filename} ({len(html)} bytes)")


if __name__ == "__main__":
    import pages
    write("index.html", pages.HOME_TITLE, pages.HOME_DESC, pages.HOME_CONTENT)
    write("regulatory-case.html", pages.REG_TITLE, pages.REG_DESC, pages.REG_CONTENT)
    write("services.html", pages.SERVICES_TITLE, pages.SERVICES_DESC, pages.SERVICES_CONTENT)
    write("proof.html", pages.PROOF_TITLE, pages.PROOF_DESC, pages.PROOF_CONTENT)
    write("engagement.html", pages.ENGAGEMENT_TITLE, pages.ENGAGEMENT_DESC, pages.ENGAGEMENT_CONTENT)
    write("contact.html", pages.CONTACT_TITLE, pages.CONTACT_DESC, pages.CONTACT_CONTENT)
    print("Build complete.")
