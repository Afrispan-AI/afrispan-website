# CLAUDE.md

This file is read automatically at the start of every Claude Code session in this repository. Read it in full before making any change.

## What This Repository Is

The Afrispan AI Assurance marketing website. A dependency-light static site, plain HTML, CSS, and JavaScript, no framework, no backend, no client login or subscription system. That last point is a deliberate decision, not a limitation, see `docs/BUSINESS_CONTEXT.md` for the full reasoning if it's ever questioned.

`build.py` and `pages.py` are the source build tooling, they render a shared header and footer around each page's own content so all pages stay visually consistent. The `.html` files in the root are the actual generated output, flat, portable, deployable as-is with no build step required at deploy time. When adding or editing a page, extend `pages.py` and re-run `build.py` rather than hand-editing the generated HTML files directly, since a hand-edit will be silently overwritten the next time the build script runs.

## Structure

```
index.html              Home
regulatory-case.html    The regulatory argument (Nigeria's AI governance landscape)
services.html           The six service lines
proof.html              Technical portfolio, links to github.com/Afrispan-AI/ai-governance-suite
engagement.html         Engagement tiers, no pricing numbers (see Non-Negotiable Rules)
contact.html            Contact and discovery-call conversion path, with a real Netlify-hosted form (AJAX-submitted, inline success message, no separate thank-you page)
css/style.css
js/main.js
assets/images/          Real, final brand assets: afrispan-wordmark-new-dark.png, afrispan-wordmark-new-light.png (originals, heavy padding, not used directly), afrispan-wordmark-new-light-trimmed.png (cropped, opaque background, unused), afrispan-wordmark-new-light-transparent.png (used in the header), afrispan-wordmark-new-dark-trimmed.png (cropped, currently unused), afrispan-badge-circle.png, favicons
build.py, pages.py      Source templates, regenerate the HTML pages, do not hand-edit generated HTML directly
docs/BUSINESS_CONTEXT.md  Full business plan, regulatory, and technical portfolio detail, read this for anything not covered here
```

## Non-Negotiable Rules

**No em dashes, anywhere.** In copy, in code comments, in commit messages. Use commas, colons, or restructured sentences instead.

**No pricing numbers anywhere on the site.** Per the business plan, pricing is illustrative and not yet validated against a real client engagement. `engagement.html` describes tiers and scope, never a number. If asked to add pricing, check `docs/BUSINESS_CONTEXT.md` first, this is a deliberate, stated decision, not an oversight to quietly fix.

**Every capability claim stays honest.** Where the technical portfolio's own status is simulated, illustrative, or planned rather than proven, the website's language must reflect that, never upgrade a claim to sound more finished than the underlying work actually is. Cross-check against `docs/BUSINESS_CONTEXT.md` or the portfolio repo's own `CLAUDE.md` before stating a capability as complete.

**This is not a client login platform.** Do not add authentication, account creation, or any form that collects and stores client system data. The site's job is exactly three things: state the business model and regulatory argument, prove technical capability via the public GitHub link, and convert interest into a conversation. See `docs/BUSINESS_CONTEXT.md` for the full reasoning if this is ever reconsidered, it should be a deliberate decision, not a drift.

**Real brand assets only.** The logo files in `assets/images/` are final, real Afrispan brand assets. Never regenerate, reinterpret, or approximate the logo, use the existing files exactly as they are.

## Working Style

State assumptions explicitly rather than guessing silently when a request is ambiguous. Verify a claim against `docs/BUSINESS_CONTEXT.md` before adding it to the site rather than writing plausible-sounding marketing copy from scratch. Prefer small, checkable edits to `pages.py` over large rewrites, and re-run `build.py` to confirm the generated HTML actually reflects the change before considering it done.
