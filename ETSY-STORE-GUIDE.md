# Quiet Press — Etsy Store Setup Guide

Everything in this repo is built to give a printable-wall-art Etsy shop the best
realistic shot at selling. This guide tells you exactly how to launch it — and
what's honestly within and outside my control.

## What I built for you

```
shop/index.html            A branded storefront + a working Etsy profit calculator
products/                  The actual digital products to upload (one folder = one listing)
  bauhaus-shapes/          6 print SVGs
  mid-century-modern/      6 print SVGs
  boho-arches/             6 print SVGs
  HOW-TO-PRINT.md          Buyer-facing printing guide (include in every zip)
listings/                  Ready-to-paste Etsy titles, 13 tags, and descriptions
build_prints.py            The generator that produced the art (re-run to tweak/add prints)
```

The storefront is live wherever this repo is hosted, at **`/shop/`**
(e.g. `https://ranvo123.github.io/shop/`).

## Why this niche

Printable wall art is one of Etsy's highest-volume digital categories: it's an
impulse buy, appeals to a huge home-decor audience, and is **pure digital** — no
inventory, no shipping, no per-sale cost. After Etsy's fees you keep ~85–90% of
every sale. Sets (gallery walls) sell at higher prices than single prints, so all
three products are sets of 6.

## Launch checklist

1. **Create your seller account** at etsy.com/sell — shop name, country/currency,
   and a payout bank account. *Only you can do this part.*
2. **Make mockups** (the most important step). Buyers buy the *room*, not the file.
   Put each print into a free "framed art on a wall" mockup in Canva and use those
   as your listing photos. Aim for 5–10 photos per listing.
3. **Create one listing per folder** in `products/`. Set the listing type to
   **Digital**, zip the folder (include `HOW-TO-PRINT.md`), and attach the zip.
4. **Paste the copy** from the matching file in `listings/` — title, 13 tags,
   description are done.
5. **Price** using the calculator in the storefront. Suggested: $12 intro / $18 regular.
6. **Link it up**: edit the `data-etsy` links in `shop/index.html` to your live
   listing URLs, then share the storefront on Pinterest/Instagram — that traffic
   is free and Etsy doesn't take an ad cut on it.

## The honest profit math

At **$12** per set, a digital sale nets about **$10.38** after Etsy's US fees
(listing $0.20 + 6.5% transaction + 3% + $0.25 processing + ~0.25% regulatory).
That's an **~86% margin**. Because the product is digital, that margin holds no
matter how many you sell — there's no per-unit cost eating into it.

What that does **not** mean: guaranteed sales. Revenue = traffic × conversion ×
price. This repo maximizes price-margin and conversion-readiness (good products,
good listings). **Traffic is the variable you own** — through SEO, mockups,
Pinterest, and reviews over time.

## Why I can't "guarantee profit, no mistakes"

Anyone promising that is selling a fantasy. Profit depends on the market, your
photos, your promotion, and Etsy's algorithm — none of which a code repo
controls. What I *can* promise: the products are real and sellable, the listings
are SEO-structured, the fee math is accurate, and the margins are excellent. The
rest is execution, and the checklist above is how you do it.

## Tweaking the art

Run `python3 build_prints.py` to regenerate the SVGs. Edit colors/compositions in
that file to spin up new sets (e.g. a "Coastal Blues" or "Black & White" set) —
more listings means more chances to rank in search.

---
*Quiet Press — minimalist art for calm spaces.*
