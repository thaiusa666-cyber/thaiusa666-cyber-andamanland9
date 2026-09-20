#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Andaman Land — static site generator.

รันด้วย:  python3 build.py
ผลลัพธ์:  dist/  (อัปโหลด/deploy โฟลเดอร์นี้ได้เลย)

ทุกหน้าเป็น HTML จริงที่ Google อ่านได้โดยไม่ต้องรัน JavaScript
"""
import html
import json
import os
import re
import shutil
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))

from data import (BASE_URL, SITE, LANGS, LANG_LABEL, LANG_HTML, HREFLANG, TAGLINE,
                  t, LOCATION_NAMES, LOCATION_PAGES, LOCATION_ORDER, TYPE_ORDER,
                  TYPE_NAMES, PRICE_BANDS, SIZE_BANDS)
from content_pages import (LOCATION_COPY, SERVICES, INVEST_INTRO, INVEST_CATEGORIES,
                           INVEST_RISK, ABOUT, CONTACT_COPY, LEGAL_PAGES)
from content_articles import ARTICLES

DIST = os.path.join(ROOT, "dist")
TODAY = date.today().isoformat()
PAGES = []          # (route, lang, changefreq, group)
PREVIEW = []        # (route, lang, title, body_html)

e = html.escape


# --------------------------------------------------------------------- utils
def route(key, lang, slug=None):
    base = "/%s/" % lang
    if key == "home":
        return base
    if key == "property":
        return "%sproperty/%s/" % (base, slug)
    if key == "location":
        return "%slocations/%s/" % (base, slug)
    if key == "article":
        return "%sbuying-guide/%s/" % (base, slug)
    mapping = {"properties": "properties", "land": "land-for-sale", "locations": "locations",
               "investment": "investment", "guide": "buying-guide", "about": "about",
               "contact": "contact", "disclaimer": "legal-disclaimer", "privacy": "privacy",
               "terms": "terms", "cookies": "cookies"}
    return base + mapping[key] + "/"


def write(route_path, content, changefreq="monthly", group="pages", lang="en"):
    out = os.path.join(DIST, route_path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)
    PAGES.append((route_path, lang, changefreq, group))


def loc_name(slug, lang):
    return LOCATION_NAMES.get(slug, {}).get(lang, slug)


def type_name(slug, lang):
    return TYPE_NAMES.get(slug, {}).get(lang, slug)


def fmt_price(p, lang, currency="THB"):
    if not p:
        return {"en": "Price on application", "th": "สอบถามราคา", "zh": "价格面议"}[lang]
    return "฿%s" % format(int(p), ",d") if currency == "THB" else "%s %s" % (currency, format(int(p), ",d"))


def fmt_size(p, lang):
    bits = []
    if p.get("rai"):
        bits.append("%g %s" % (p["rai"], t("p_rai", lang)))
    if p.get("ngan"):
        bits.append("%g %s" % (p["ngan"], t("p_ngan", lang)))
    if p.get("square_wah"):
        bits.append("%g %s" % (p["square_wah"], t("p_wah", lang)))
    if not bits:
        return {"en": "Size on application", "th": "สอบถามขนาด", "zh": "面积面议"}[lang]
    return "  ".join(bits)


# --------------------------------------------------------------- generated art
def land_svg(slug, label, tone=0):
    """Deterministic limestone/sea illustration used as an image placeholder.
    Replace with real photographs (WebP) — see README."""
    seed = sum(ord(c) for c in slug)
    skies = [("#0A2A31", "#16505B"), ("#0C333B", "#1B6C79"), ("#123E49", "#2A7F86")]
    a, b = skies[(seed + tone) % len(skies)]
    h1 = 120 + (seed % 40)
    h2 = 160 + ((seed // 3) % 50)
    x1 = 90 + (seed % 120)
    x2 = 420 + ((seed // 5) % 160)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img" aria-label="%s" preserveAspectRatio="xMidYMid slice">'
        '<defs><linearGradient id="s%d" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
        '<title>%s</title>'
        '<rect width="800" height="600" fill="url(#s%d)"/>'
        '<circle cx="640" cy="120" r="42" fill="#C89B3E" opacity=".28"/>'
        '<path d="M0 %d q %d -%d %d 0 t %d 0 V600 H0 Z" fill="#0A2A31" opacity=".45"/>'
        '<path d="M%d 330 l 46 -%d l 52 %d Z" fill="#0A2A31" opacity=".65"/>'
        '<path d="M%d 350 l 60 -%d l 68 %d Z" fill="#0A2A31" opacity=".8"/>'
        '<rect y="470" width="800" height="130" fill="#08222A"/>'
        '<g stroke="#C89B3E" stroke-width="1.2" opacity=".55">'
        '<path d="M60 520 H740"/><path d="M60 512 V528"/><path d="M400 512 V528"/><path d="M740 512 V528"/></g>'
        '<text x="60" y="560" fill="#9FB6B5" font-family="Karla,system-ui,sans-serif" font-size="19">%s</text>'
        '</svg>'
    ) % (e(label), seed % 97, a, b, e(label), seed % 97,
         300 + (seed % 30), x1, h1, x1 * 2, x2,
         x1, h2, h2, x2, h1, h1, e(label))


def hero_svg():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 620" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
        '<defs><linearGradient id="hsky" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#071E24"/><stop offset=".55" stop-color="#0E3D47"/><stop offset="1" stop-color="#155B66"/></linearGradient>'
        '<linearGradient id="hfade" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#071E24" stop-opacity=".95"/><stop offset=".72" stop-color="#071E24" stop-opacity=".1"/></linearGradient></defs>'
        '<rect width="1440" height="620" fill="url(#hsky)"/>'
        '<circle cx="1180" cy="150" r="70" fill="#C89B3E" opacity=".22"/>'
        '<path d="M880 430 l 70 -150 l 78 150 Z" fill="#06181D" opacity=".75"/>'
        '<path d="M1010 440 l 95 -205 l 104 205 Z" fill="#06181D" opacity=".85"/>'
        '<path d="M1210 445 l 58 -120 l 64 120 Z" fill="#06181D" opacity=".7"/>'
        '<rect y="440" width="1440" height="180" fill="#051519"/>'
        '<g stroke="#C89B3E" stroke-width="1" opacity=".35">'
        '<path d="M0 500 H1440"/><path d="M180 492 V512"/><path d="M540 492 V512"/><path d="M900 492 V512"/><path d="M1260 492 V512"/></g>'
        '<rect width="1440" height="620" fill="url(#hfade)"/>'
        '</svg>')


# ------------------------------------------------------------------- partials
def nav_links(lang, active):
    items = [("home", t("nav_home", lang)), ("properties", t("nav_properties", lang)),
             ("locations", t("nav_locations", lang)), ("investment", t("nav_investment", lang)),
             ("guide", t("nav_guide", lang)), ("about", t("nav_about", lang)),
             ("contact", t("nav_contact", lang))]
    out = []
    for key, label in items:
        cur = ' aria-current="page"' if key == active else ""
        out.append('<a href="%s"%s>%s</a>' % (route(key, lang), cur, e(label)))
    return "".join(out)


def lang_switcher(lang, key, slug=None):
    links = []
    for code in LANGS:
        cur = ' aria-current="true"' if code == lang else ""
        links.append('<a href="%s" hreflang="%s"%s>%s</a>' % (route(key, code, slug), HREFLANG[code], cur, LANG_LABEL[code]))
    return '<div class="lang" aria-label="%s">%s</div>' % (e(t("nav_language", lang)), '<span aria-hidden="true">|</span>'.join(links))


def header(lang, key, slug=None):
    return (
        '<a class="skip" href="#main">Skip to content</a>'
        '<header class="site-header"><div class="wrap header-row">'
        '<a class="logo" href="%s"><b>%s</b><span>%s</span></a>'
        '<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">%s</button>'
        '<nav class="nav" id="site-nav" aria-label="Main">%s%s'
        '<a class="btn btn--small btn--brass" href="%s">%s</a></nav>'
        '</div></header>'
    ) % (route("home", lang), e(SITE["brand"]), e(SITE["brand_small"]), e(t("menu", lang)),
         nav_links(lang, key), lang_switcher(lang, key, slug),
         route("contact", lang), e(t("cta_contact", lang)))


def footer(lang):
    q = "".join('<li><a href="%s">%s</a></li>' % (route(k, lang), e(t(lbl, lang))) for k, lbl in
                [("properties", "nav_properties"), ("land", "nav_land"), ("locations", "nav_locations"),
                 ("investment", "nav_investment"), ("guide", "nav_guide"), ("about", "nav_about"),
                 ("contact", "nav_contact")])
    legal = "".join('<li><a href="%s">%s</a></li>' % (route(k, lang), e(t(lbl, lang))) for k, lbl in
                    [("disclaimer", "legal_disclaimer"), ("privacy", "privacy"),
                     ("terms", "terms"), ("cookies", "cookies")])
    contact = (
        '<li><span>%s</span><a href="tel:%s">%s</a></li>'
        '<li><span>WhatsApp</span><a href="%s">%s</a></li>'
        '<li><span>LINE</span><a href="%s">%s</a></li>'
        '<li><span>%s</span><a href="mailto:%s">%s</a></li>'
    ) % (e(t("btn_call", lang)), e(SITE["phone_href"]), e(SITE["phone"]),
         e(whatsapp_url("")), e(SITE["whatsapp"]), e(SITE["line_url"]), e(SITE["line"]),
         e(t("fm_email", lang)), e(SITE["email"]), e(SITE["email"]))
    social = "".join('<li><a href="%s" rel="noopener">%s</a></li>' % (e(SITE[k]), lbl) for k, lbl in
                     [("facebook", "Facebook"), ("instagram", "Instagram"),
                      ("youtube", "YouTube"), ("tiktok", "TikTok")])
    return (
        '<footer class="site-footer"><div class="wrap">'
        '<div class="foot-grid">'
        '<div><h4>%s</h4><p>%s</p><p>%s<br>%s</p></div>'
        '<div><h4>%s</h4><ul>%s</ul></div>'
        '<div><h4>%s</h4><ul class="channels">%s</ul><h4 style="margin-top:18px">%s</h4><ul>%s</ul></div>'
        '<div><h4>%s</h4><ul>%s</ul></div>'
        '</div>'
        '<div class="foot-legal"><p><strong>%s</strong> %s</p>'
        '<p>© %s %s. %s</p></div>'
        '</div></footer>'
    ) % (e(SITE["legal_name"]), e(TAGLINE[lang]), e(SITE["address"]), e(SITE["hours"]),
         e(t("quick_links", lang)), q,
         e(t("contact_us", lang)), contact, e(t("follow", lang)), social,
         e(t("legal", lang)), legal,
         e(t("legal_disclaimer", lang)), e(t("disclaimer_short", lang)),
         date.today().year, e(SITE["legal_name"]), e(t("rights", lang)))


def whatsapp_url(text):
    num = re.sub(r"\D", "", SITE["whatsapp"])
    if not num:
        return "#whatsapp-not-configured"
    return "https://wa.me/%s?text=%s" % (num, re.sub(r"\s+", "%20", text))


def org_schema(lang):
    data = {
        "@context": "https://schema.org", "@type": "RealEstateAgent",
        "name": SITE["legal_name"], "url": BASE_URL + route("home", lang),
        "description": TAGLINE[lang], "areaServed": ["Phuket", "Thailand"],
        "email": SITE["email"], "telephone": SITE["phone"],
        "address": {"@type": "PostalAddress", "streetAddress": SITE["address"],
                    "addressLocality": SITE["city"], "addressRegion": SITE["region"],
                    "postalCode": SITE["postal"], "addressCountry": SITE["country"]},
        "openingHours": SITE["hours"],
        "founder": {"@type": "Person", "name": SITE["agent"]},
        "sameAs": [SITE[k] for k in ("facebook", "instagram", "youtube", "tiktok") if not SITE[k].startswith("[")],
    }
    if not SITE["gbp_url"].startswith("["):
        data["hasMap"] = SITE["gbp_url"]
    return data


def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                 "item": BASE_URL + u} for i, (n, u) in enumerate(items)]}


def crumbs_html(lang, items):
    li = []
    for name, url in items:
        li.append('<li><a href="%s">%s</a></li>' % (url, e(name)) if url else '<li>%s</li>' % e(name))
    return '<nav class="crumbs" aria-label="%s"><div class="wrap"><ol>%s</ol></div></nav>' % (e(t("breadcrumb", lang)), "".join(li))


def page(lang, key, title, description, body, slug=None, schemas=None, og_type="website"):
    r = route(key, lang, slug)
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s"/>' % (HREFLANG[c], BASE_URL + route(key, c, slug)) for c in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s"/>' % (BASE_URL + route(key, "en", slug))
    jsonld = "".join('<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False)
                     for s in (schemas or []))
    ga = ""
    if SITE["ga4_id"]:
        ga = ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>'
              '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
              'gtag("js",new Date());gtag("config","%s");</script>') % (SITE["ga4_id"], SITE["ga4_id"])
    gsc = '<meta name="google-site-verification" content="%s"/>' % SITE["gsc_token"] if SITE["gsc_token"] else ""
    doc = (
        '<!DOCTYPE html><html lang="%s" data-lang="%s"><head>'
        '<meta charset="utf-8"/>'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"/>'
        '<title>%s</title>'
        '<meta name="description" content="%s"/>'
        '<link rel="canonical" href="%s"/>%s%s'
        '<meta property="og:site_name" content="%s"/>'
        '<meta property="og:type" content="%s"/>'
        '<meta property="og:locale" content="%s"/>'
        '<meta property="og:title" content="%s"/>'
        '<meta property="og:description" content="%s"/>'
        '<meta property="og:url" content="%s"/>'
        '<meta property="og:image" content="%s"/>'
        '<meta name="twitter:card" content="summary_large_image"/>'
        '<meta name="twitter:title" content="%s"/>'
        '<meta name="twitter:description" content="%s"/>'
        '<meta name="twitter:image" content="%s"/>'
        '<meta name="theme-color" content="#0A2A31"/>'
        '<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"/>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"/>'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Karla:wght@400;600&family=IBM+Plex+Sans+Thai:wght@400;600&family=Noto+Sans+SC:wght@400;600&display=swap"/>'
        '<link rel="stylesheet" href="/assets/css/style.css"/>%s%s'
        '</head><body>%s<main id="main">%s</main>%s'
        '<script src="/assets/js/site.js" defer></script></body></html>'
    ) % (LANG_HTML[lang], lang, e(title), e(description), BASE_URL + r, alts, gsc,
         e(SITE["legal_name"]), og_type, {"en": "en_US", "th": "th_TH", "zh": "zh_CN"}[lang],
         e(title), e(description), BASE_URL + r, BASE_URL + "/assets/img/andaman-land-phuket-og.svg",
         e(title), e(description), BASE_URL + "/assets/img/andaman-land-phuket-og.svg",
         jsonld, ga, header(lang, key, slug), body, footer(lang))
    PREVIEW.append((r, lang, title, body))
    return doc


# ------------------------------------------------------------------ components
def img_tag(slug, alt, lazy=True):
    return '<img src="/assets/img/%s.svg" alt="%s" width="800" height="600"%s decoding="async"/>' % (
        e(slug), e(alt), ' loading="lazy"' if lazy else "")


def status_badge(p, lang):
    st = p["status"]
    cls = {"sold": " badge--sold", "reserved": " badge--reserved"}.get(st, "")
    return '<span class="badge%s">%s</span>' % (cls, e(t("st_" + st, lang)))


def property_card(p, lang):
    loc = p[lang]
    url = route("property", lang, p["slug"])
    size_attr = p.get("rai") if p.get("rai") else ""
    price_attr = p.get("price") if p.get("price") else ""
    sample = ' <span class="badge badge--sample">SAMPLE</span>' if p.get("sample") else ""
    return (
        '<article class="card" data-card data-loc="%s" data-type="%s" data-price="%s" data-size="%s" data-created="%s">'
        '<div class="thumb">%s</div>'
        '<div class="card-body">'
        '<p class="meta">%s · %s%s</p>'
        '<h3><a href="%s">%s</a></h3>'
        '<p class="price">%s</p>'
        '<ul class="spec"><li>%s</li><li>%s: %s</li></ul>'
        '<div class="card-foot"><a class="btn btn--ghost btn--small" href="%s">%s</a></div>'
        '</div></article>'
    ) % (e(p["location"]), e(p["property_type"]), price_attr, size_attr, e(p["created_at"]),
         img_tag(p["slug"], loc["title"]),
         status_badge(p, lang), e(loc_name(p["location"], lang)), sample,
         url, e(loc["title"]), e(fmt_price(p.get("price"), lang, p.get("currency", "THB"))),
         e(fmt_size(p, lang)), e(t("p_id", lang)), e(p["id"]),
         url, e(t("btn_view", lang)))


def select(name, label, options, lang):
    opts = '<option value="">%s</option>' % e(t("f_any", lang))
    opts += "".join('<option value="%s">%s</option>' % (e(v), e(l)) for v, l in options)
    return ('<div class="field"><label for="f-%s">%s</label>'
            '<select id="f-%s" name="%s">%s</select></div>') % (name, e(label), name, name, opts)


def search_form(lang, action=None, submit_label=None):
    locs = [(s, loc_name(s, lang)) for s in LOCATION_ORDER]
    types = [(s, type_name(s, lang)) for s in TYPE_ORDER]
    prices = [(code, lbl[lang]) for code, lbl, _, _ in PRICE_BANDS]
    sizes = [(code, lbl[lang]) for code, lbl, _, _ in SIZE_BANDS]
    attrs = 'id="filter-form" data-filter-form' if action is None else 'action="%s" method="get"' % action
    reset = ('<button class="btn btn--ghost" type="button" id="filter-reset">%s</button>' % e(t("btn_reset", lang))) if action is None else ""
    return (
        '<form class="searchbar" %s role="search" aria-label="%s">'
        '<div class="search-grid">%s%s%s%s</div>'
        '<div class="search-actions"><button class="btn btn--brass" type="submit">%s</button>%s</div>'
        '</form>'
    ) % (attrs, e(t("search_title", lang)),
         select("location", t("f_location", lang), locs, lang),
         select("type", t("f_type", lang), types, lang),
         select("price", t("f_price", lang), prices, lang),
         select("size", t("f_size", lang), sizes, lang),
         e(submit_label or t("btn_search", lang)), reset)


def enquiry_form(lang, property_id="", title=None, sub=None, name="enquiry"):
    msgs = json.dumps({
        "name": t("fm_err_name", lang), "email": t("fm_err_email", lang),
        "contact": t("fm_err_contact", lang), "message": t("fm_err_message", lang),
        "ok": t("fm_ok", lang), "fail": t("fm_fail", lang),
        "sending": t("fm_sending", lang), "wait": t("fm_wait", lang),
    }, ensure_ascii=False)
    opt = e(t("fm_optional", lang))
    endpoint = ' data-endpoint="%s"' % SITE["form_endpoint"] if SITE["form_endpoint"] else ""

    def f(fid, label, typ="text", extra="", hint=""):
        return ('<div class="field"><label for="%s-%s">%s%s</label>'
                '<input id="%s-%s" type="%s" name="%s"%s/>'
                '<span class="err" data-err="%s"></span></div>') % (
            name, fid, e(label), hint, name, fid, typ, fid, extra, fid)

    pref = ('<div class="field"><label for="%s-preferred">%s</label>'
            '<select id="%s-preferred" name="preferred">'
            '<option>WhatsApp</option><option>LINE</option><option>%s</option><option>%s</option>'
            '</select></div>') % (name, e(t("fm_pref", lang)), name, e(t("fm_email", lang)), e(t("fm_phone", lang)))

    return (
        '<form class="form" name="%s" data-enquiry data-messages=\'%s\'%s netlify data-netlify="true" netlify-honeypot="company-website">'
        '<input type="hidden" name="form-name" value="%s"/>'
        '<input type="hidden" name="page_language" value="%s"/>'
        '<p class="hp"><label>Do not fill this in <input name="company-website" tabindex="-1" autocomplete="off"/></label></p>'
        '%s%s'
        '<div class="form-grid">%s%s</div>'
        '<div class="form-grid">%s%s</div>'
        '<div class="form-grid">%s%s</div>'
        '<div class="form-grid">%s%s</div>'
        '<div class="field"><label for="%s-message">%s</label>'
        '<textarea id="%s-message" name="message"></textarea><span class="err" data-err="message"></span></div>'
        '<span class="err" data-err="contact"></span>'
        '<div class="form-status" role="status" aria-live="polite"></div>'
        '<button class="btn btn--brass" type="submit">%s</button>'
        '</form>'
    ) % (name, msgs.replace("'", "&#39;"), endpoint, name, lang,
         ('<h2>%s</h2>' % e(title)) if title else "",
         ('<p>%s</p>' % e(sub)) if sub else "",
         f("name", t("fm_name", lang)), f("nationality", t("fm_nationality", lang), hint=" (%s)" % opt),
         f("email", t("fm_email", lang), "email"), f("phone", t("fm_phone", lang), "tel", hint=" (%s)" % opt),
         f("whatsapp", t("fm_whatsapp", lang), "tel", hint=" (%s)" % opt), f("line", t("fm_line", lang), hint=" (%s)" % opt),
         pref, f("property_id", t("fm_property", lang), "text",
                 ' value="%s"' % e(property_id) if property_id else "", hint=" (%s)" % opt),
         name, e(t("fm_message", lang)), name,
         e(t("btn_send", lang)))


def contact_buttons(lang, ptitle=""):
    msg = "Hello Benz, I am interested in %s" % ptitle if ptitle else "Hello Benz, I am interested in land in Phuket"
    return (
        '<div class="btn-row">'
        '<a class="btn btn--brass" href="%s" rel="noopener">%s</a>'
        '<a class="btn btn--ghost" href="%s" rel="noopener">%s</a>'
        '<a class="btn btn--ghost" href="mailto:%s?subject=%s">%s</a>'
        '<a class="btn btn--ghost" href="tel:%s">%s</a>'
        '</div>'
    ) % (e(whatsapp_url(msg)), e(t("btn_whatsapp", lang)),
         e(SITE["line_url"]), e(t("btn_line", lang)),
         e(SITE["email"]), e(re.sub(r"\s+", "%20", ptitle or "Land enquiry")), e(t("btn_email", lang)),
         e(SITE["phone_href"]), e(t("btn_call", lang)))


def faq_block(lang, items):
    if not items:
        return ""
    body = "".join('<details><summary>%s</summary><p>%s</p></details>' % (e(q), e(a)) for q, a in items)
    return '<section class="section"><div class="wrap narrow"><h2>%s</h2><div class="faq">%s</div></div></section>' % (
        e(t("sec_faq", lang)), body)


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def cta_band(lang):
    return (
        '<section class="section section--ink"><div class="wrap narrow">'
        '<h2>%s</h2><p>%s</p>%s'
        '<p><a class="btn btn--brass" href="%s">%s</a></p>'
        '</div></section>'
    ) % (e(CONTACT_COPY[lang][0]), e(CONTACT_COPY[lang][1]), contact_buttons(lang),
         route("contact", lang), e(t("btn_viewing", lang)))


# ------------------------------------------------------------------ page builds
def build_home(lang, props):
    featured = [p for p in props if p.get("featured") and p["status"] != "sold"][:3] or props[:3]
    cards = "".join(property_card(p, lang) for p in featured)
    areas = "".join('<li><a href="%s">%s<span>%s</span></a></li>' % (
        route("location", lang, s), e(loc_name(s, lang)),
        e("%d %s" % (len([p for p in props if p["location"] == s]), t("nav_properties", lang).lower()))
    ) for s in LOCATION_PAGES)
    services = "".join('<div class="tile"><h3>%s</h3><p>%s</p></div>' % (e(s[lang][0]), e(s[lang][1])) for s in SERVICES)
    invest = "".join('<div class="tile"><h3>%s</h3><p>%s</p></div>' % (e(c[lang][0]), e(c[lang][1])) for c in INVEST_CATEGORIES[:3])
    guides = "".join('<div class="tile"><h3><a href="%s">%s</a></h3><p>%s</p></div>' % (
        route("article", lang, a["slug"]), e(a[lang]["title"]), e(a[lang]["meta"])) for a in ARTICLES[:3])

    body = (
        '<section class="hero"><div class="hero-art">%s</div>'
        '<div class="wrap hero-inner">'
        '<p class="hero-mark">%s</p>'
        '<h1>%s</h1><p>%s</p>'
        '<div class="btn-row"><a class="btn btn--brass" href="%s">%s</a>'
        '<a class="btn btn--ghost" href="%s">%s</a></div>'
        '%s</div></section>'
        '<section class="section"><div class="wrap">'
        '<h2>%s</h2><div class="grid">%s</div>'
        '<p style="margin-top:22px"><a class="btn btn--ghost" href="%s">%s</a></p>'
        '</div></section>'
        '<section class="section section--mist"><div class="wrap">'
        '<h2>%s</h2><ul class="arealist">%s</ul></div></section>'
        '<section class="section"><div class="wrap"><h2>%s</h2><div class="tiles">%s</div></div></section>'
        '<section class="section section--mist"><div class="wrap"><h2>%s</h2><div class="tiles">%s</div>'
        '<p style="margin-top:22px"><a class="btn btn--ghost" href="%s">%s</a></p></div></section>'
        '<section class="section"><div class="wrap"><h2>%s</h2><div class="tiles">%s</div>'
        '<p style="margin-top:22px"><a class="btn btn--ghost" href="%s">%s</a></p></div></section>'
        '%s'
    ) % (hero_svg(), e(TAGLINE[lang]), e(t("home_h1", lang)), e(t("home_sub", lang)),
         route("land", lang), e(t("btn_view_land", lang)),
         route("contact", lang), e(t("cta_contact", lang)),
         search_form(lang, action=route("properties", lang)),
         e(t("sec_featured", lang)), cards, route("properties", lang), e(t("btn_all_land", lang)),
         e(t("sec_locations", lang)), areas,
         e(t("sec_services", lang)), services,
         e(t("sec_invest", lang)), invest, route("investment", lang), e(t("nav_investment", lang)),
         e(t("sec_guide", lang)), guides, route("guide", lang), e(t("btn_read", lang)),
         cta_band(lang))

    title = "%s | %s" % (t("home_h1", lang), SITE["brand"])
    schemas = [org_schema(lang),
               {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["legal_name"],
                "url": BASE_URL + route("home", lang), "inLanguage": LANG_HTML[lang]}]
    return page(lang, "home", title, t("home_sub", lang), body, schemas=schemas)


def listing_page(lang, props, key, heading, intro, description, only=None):
    subset = [p for p in props if (only is None or only(p))]
    cards = "".join(property_card(p, lang) for p in subset)
    sorts = [("newest", t("sort_newest", lang)), ("price-asc", t("sort_price_asc", lang)),
             ("price-desc", t("sort_price_desc", lang)), ("size", t("sort_size", lang))]
    sort_html = ('<div class="field"><label for="sort-select">%s</label>'
                 '<select id="sort-select" data-sort name="sort">%s</select></div>') % (
        e(t("sort_by", lang)), "".join('<option value="%s">%s</option>' % (v, e(l)) for v, l in sorts))
    body = (
        '%s'
        '<section class="section"><div class="wrap">'
        '<h1>%s</h1><p class="lead">%s</p>'
        '%s'
        '<div class="result-bar" style="margin-top:28px">'
        '<p class="count"><span id="result-count" data-count>%d</span> %s</p>%s</div>'
        '<div class="grid" id="listing-grid" data-listing-grid>%s</div>'
        '<div class="empty" id="result-empty" data-empty hidden>%s</div>'
        '</div></section>%s'
    ) % (crumbs_html(lang, [(t("nav_home", lang), route("home", lang)), (heading, None)]),
         e(heading), e(intro), search_form(lang),
         len(subset), e(t("results", lang)), sort_html, cards,
         e(t("no_results", lang)), cta_band(lang))
    schemas = [breadcrumb_schema([(t("nav_home", lang), route("home", lang)), (heading, route(key, lang))]),
               {"@context": "https://schema.org", "@type": "ItemList",
                "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                     "url": BASE_URL + route("property", lang, p["slug"]),
                                     "name": p[lang]["title"]} for i, p in enumerate(subset)]}]
    return page(lang, key, "%s | %s" % (heading, SITE["brand"]), description, body, schemas=schemas)


def build_property(lang, p, props):
    loc = p[lang]
    title = loc["title"]
    heading = "%s – %s" % (title, fmt_size(p, lang)) if p.get("rai") else title
    crumbs = [(t("nav_home", lang), route("home", lang)),
              (t("nav_properties", lang), route("properties", lang)),
              (loc_name(p["location"], lang), route("location", lang, p["location"])
               if p["location"] in LOCATION_PAGES else None),
              (title, None)]
    facts = [
        (t("p_id", lang), p["id"]),
        (t("p_price", lang), fmt_price(p.get("price"), lang, p.get("currency", "THB"))),
        (t("p_size", lang), fmt_size(p, lang)),
        (t("p_sqm", lang), ("%g" % p["square_meter"]) if p.get("square_meter") else "[ADD SQM]"),
        (t("p_type", lang), type_name(p["property_type"], lang)),
        (t("p_location", lang), "%s, %s" % (loc_name(p["location"], lang), p["province"])),
        (t("p_district", lang), p["district"]),
        (t("p_title_deed", lang), p["title_deed"]),
        (t("p_road", lang), p["road_access"]),
        (t("p_electricity", lang), p["electricity"]),
        (t("p_water", lang), p["water"]),
        (t("p_zoning", lang), p["zoning"]),
        (t("p_gps", lang), ("%s, %s" % (p["latitude"], p["longitude"])) if p.get("latitude") else "[ADD GPS COORDINATES]"),
        (t("p_dist_airport", lang), p["distance_airport"]),
        (t("p_dist_beach", lang), p["distance_beach"]),
        (t("p_dist_attr", lang), p["distance_attractions"]),
    ]
    facts_html = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(k), e(str(v))) for k, v in facts)
    features = "".join("<li>%s</li>" % e(f) for f in loc.get("features", []))
    nearby = "".join("<li>%s</li>" % e(f) for f in loc.get("nearby", []))

    images = [{"src": i, "alt": ""} if isinstance(i, str) else i for i in (p.get("images") or [])]
    if images:
        gallery = "".join('<img src="%s" alt="%s" loading="lazy" width="800" height="600"/>' % (e(i.get("src", "")), e(i.get("alt", title))) for i in images)
    else:
        gallery = "".join(img_tag(p["slug"], "%s — %s" % (title, n + 1)) for n in range(3))

    if p.get("map_url"):
        mapbox = '<p><a class="btn btn--ghost btn--small" href="%s" rel="noopener">%s</a></p>' % (e(p["map_url"]), e(t("p_open_maps", lang)))
    elif p.get("latitude"):
        u = "https://www.google.com/maps/search/?api=1&query=%s,%s" % (p["latitude"], p["longitude"])
        mapbox = '<p><a class="btn btn--ghost btn--small" href="%s" rel="noopener">%s</a></p>' % (e(u), e(t("p_open_maps", lang)))
    else:
        mapbox = '<div class="mapbox">[ADD GOOGLE MAP URL / GPS COORDINATES]</div>'

    video = ('<h2>%s</h2><p><a href="%s" rel="noopener">%s</a></p>' % (e(t("p_video", lang)), e(p["video_url"]), e(p["video_url"]))) if p.get("video_url") else ""

    notices = ""
    if p.get("sample"):
        notices += '<div class="notice notice--sample">%s</div>' % e(t("placeholder_note", lang))
    if p["status"] == "sold":
        notices += '<div class="notice notice--sold"><strong>%s.</strong> %s</div>' % (e(t("st_sold", lang)), e(t("sold_notice", lang)))

    similar = [q for q in props if q["slug"] != p["slug"] and q["location"] == p["location"]][:3]
    if len(similar) < 3:
        similar += [q for q in props if q["slug"] != p["slug"] and q not in similar][:3 - len(similar)]
    similar_html = "".join(property_card(q, lang) for q in similar)

    aside = (
        '<aside class="aside">'
        '<p class="meta">%s · %s</p>'
        '<h2 style="font-size:1.25rem">%s</h2>'
        '<p class="price" style="font-size:1.2rem">%s</p>'
        '<p class="meta">%s</p>'
        '%s'
        '<p><a class="btn btn--brass btn--block" href="#enquiry">%s</a></p>'
        '<p class="meta">%s: %s<br>%s<br>%s</p>'
        '</aside>'
    ) % (status_badge(p, lang), e(p["id"]), e(t("p_agent", lang)),
         e(fmt_price(p.get("price"), lang, p.get("currency", "THB"))), e(fmt_size(p, lang)),
         contact_buttons(lang, title), e(t("btn_details", lang)),
         e(SITE["agent"]), e(p["contact_phone"]), e(p["contact_email"]),
         e(loc_name(p["location"], lang)))

    body = (
        '%s'
        '<section class="section"><div class="wrap">'
        '<div class="detail"><div>'
        '<h1>%s</h1>%s'
        '<p class="lead">%s</p>'
        '<h2>%s</h2><dl class="factgrid">%s</dl>'
        '%s%s'
        '<h2>%s</h2><p>%s</p>'
        '<h2>%s</h2><div class="gallery">%s</div>'
        '%s'
        '<h2>%s</h2>%s'
        '</div>%s</div>'
        '</div></section>'
        '<section class="section section--mist" id="enquiry"><div class="wrap narrow">%s</div></section>'
        '<section class="section"><div class="wrap"><h2>%s</h2><div class="grid">%s</div></div></section>'
    ) % (crumbs_html(lang, crumbs), e(heading), notices, e(loc["description"]),
         e(t("p_key_facts", lang)), facts_html,
         ('<h2>%s</h2><ul>%s</ul>' % (e(t("p_utilities", lang)), features)) if features else "",
         ('<h2>%s</h2><ul>%s</ul>' % (e(t("p_nearby", lang)), nearby)) if nearby else "",
         e(t("p_potential", lang)), e(loc.get("potential", "")),
         e(t("p_gallery", lang)), gallery, video,
         e(t("p_map", lang)), mapbox, aside,
         enquiry_form(lang, property_id=p["id"], title=t("lead_title", lang), sub=t("lead_sub", lang),
                      name="enquiry-%s" % p["id"]),
         e(t("p_similar", lang)), similar_html)

    listing = {
        "@context": "https://schema.org", "@type": "RealEstateListing",
        "name": title, "url": BASE_URL + route("property", lang, p["slug"]),
        "description": re.sub(r"\[ADD[^\]]*\]", "", loc["description"]).strip() or title,
        "datePosted": p["created_at"], "inLanguage": LANG_HTML[lang],
        "provider": {"@type": "RealEstateAgent", "name": SITE["legal_name"]},
        "about": {"@type": "Place", "name": "%s, %s" % (loc_name(p["location"], lang), p["province"]),
                  "address": {"@type": "PostalAddress", "addressLocality": p["district"],
                              "addressRegion": p["province"], "addressCountry": "TH"}},
    }
    if p.get("latitude"):
        listing["about"]["geo"] = {"@type": "GeoCoordinates", "latitude": p["latitude"], "longitude": p["longitude"]}
    if p.get("price"):
        listing["offers"] = {"@type": "Offer", "price": p["price"], "priceCurrency": p.get("currency", "THB"),
                             "availability": "https://schema.org/InStock" if p["status"] == "for-sale" else "https://schema.org/SoldOut"}
    schemas = [listing, breadcrumb_schema([(n, u) for n, u in crumbs if u] + [(title, route("property", lang, p["slug"]))])]
    desc = "%s. %s, %s. %s" % (title, fmt_size(p, lang), loc_name(p["location"], lang),
                               t("btn_details", lang))
    return page(lang, "property", "%s | %s" % (heading, SITE["brand"]), desc[:300], body,
                slug=p["slug"], schemas=schemas, og_type="article")


def build_locations_index(lang, props):
    items = "".join(
        '<div class="tile"><h3><a href="%s">%s</a></h3><p>%s</p></div>' % (
            route("location", lang, s), e(loc_name(s, lang)), e(LOCATION_COPY[s][lang]["intro"][0]))
        for s in LOCATION_PAGES)
    heading = {"en": "Land for sale by area in Phuket", "th": "ที่ดินขายแยกตามทำเลในภูเก็ต", "zh": "按区域浏览普吉在售土地"}[lang]
    body = (
        '%s<section class="section"><div class="wrap"><h1>%s</h1>'
        '<p class="lead">%s</p><div class="tiles">%s</div></div></section>%s'
    ) % (crumbs_html(lang, [(t("nav_home", lang), route("home", lang)), (t("nav_locations", lang), None)]),
         e(heading), e(LOCATION_COPY["phuket"][lang]["typical"]), items, cta_band(lang))
    return page(lang, "locations", "%s | %s" % (heading, SITE["brand"]),
                LOCATION_COPY["phuket"][lang]["intro"][0][:300], body,
                schemas=[breadcrumb_schema([(t("nav_home", lang), route("home", lang)),
                                            (t("nav_locations", lang), route("locations", lang))])])


def build_location(lang, slug, props):
    copy = LOCATION_COPY[slug][lang]
    name = loc_name(slug, lang)
    h1 = {"en": "Land for sale in %s" % name, "th": "ที่ดินขายใน%s" % name, "zh": "%s土地出售" % name}[lang]
    here = [p for p in props if p["location"] == slug]
    cards = "".join(property_card(p, lang) for p in here) or '<div class="empty">%s</div>' % e(t("no_results", lang))
    nearby = "".join("<li>%s</li>" % e(x) for x in copy["nearby"])
    related = "".join('<div class="tile"><h3><a href="%s">%s</a></h3><p>%s</p></div>' % (
        route("article", lang, a["slug"]), e(a[lang]["title"]), e(a[lang]["meta"])) for a in ARTICLES[:3])
    crumbs = [(t("nav_home", lang), route("home", lang)),
              (t("nav_locations", lang), route("locations", lang)), (name, None)]
    body = (
        '%s<section class="section"><div class="wrap">'
        '<div class="detail"><div>'
        '<h1>%s</h1>%s'
        '<h2>%s</h2><p>%s</p>'
        '<h2>%s</h2><ul>%s</ul>'
        '<h2>%s</h2><div class="mapbox">[ADD MAP EMBED OR GOOGLE MAPS LINK FOR %s]</div>'
        '</div>'
        '<aside class="aside"><h2 style="font-size:1.2rem">%s</h2><p class="meta">%s</p>%s'
        '<p><a class="btn btn--brass btn--block" href="%s">%s</a></p></aside>'
        '</div></div></section>'
        '<section class="section section--mist"><div class="wrap"><h2>%s</h2><div class="grid">%s</div></div></section>'
        '%s'
        '<section class="section"><div class="wrap"><h2>%s</h2><div class="tiles">%s</div></div></section>%s'
    ) % (crumbs_html(lang, crumbs), e(h1),
         "".join("<p>%s</p>" % e(x) for x in copy["intro"]),
         e(t("sec_typical", lang)), e(copy["typical"]),
         e(t("sec_nearby_attr", lang)), nearby,
         e(t("p_map", lang)), e(name.upper()),
         e(t("cta_contact", lang)), e(CONTACT_COPY[lang][1]), contact_buttons(lang, h1),
         route("contact", lang), e(t("btn_viewing", lang)),
         e(t("sec_available", lang)), cards,
         faq_block(lang, copy["faq"]),
         e(t("sec_related", lang)), related, cta_band(lang))
    schemas = [breadcrumb_schema([(n, u) for n, u in crumbs if u] + [(name, route("location", lang, slug))]),
               faq_schema(copy["faq"]),
               {"@context": "https://schema.org", "@type": "Place", "name": "%s, Phuket, Thailand" % name,
                "description": copy["intro"][0]}]
    return page(lang, "location", "%s | %s" % (h1, SITE["brand"]), copy["intro"][0][:300], body,
                slug=slug, schemas=schemas)


def build_investment(lang):
    cats = "".join(
        '<div class="tile" id="%s"><h3>%s</h3><p>%s</p><ul style="font-size:.92rem;color:var(--muted)">%s</ul></div>' % (
            c["slug"], e(c[lang][0]), e(c[lang][1]), "".join("<li>%s</li>" % e(x) for x in c[lang][2]))
        for c in INVEST_CATEGORIES)
    h1 = {"en": "Investment opportunities in Phuket", "th": "โอกาสการลงทุนในภูเก็ต", "zh": "普吉投资机会"}[lang]
    body = (
        '%s<section class="section"><div class="wrap"><h1>%s</h1>%s</div></section>'
        '<section class="section section--mist"><div class="wrap"><div class="tiles">%s</div></div></section>'
        '<section class="section"><div class="wrap narrow"><h2>%s</h2><p>%s</p></div></section>%s'
    ) % (crumbs_html(lang, [(t("nav_home", lang), route("home", lang)), (t("nav_investment", lang), None)]),
         e(h1), "".join('<p class="lead">%s</p>' % e(x) if i == 0 else "<p>%s</p>" % e(x)
                        for i, x in enumerate(INVEST_INTRO[lang])),
         cats, e(INVEST_RISK[lang][0]), e(INVEST_RISK[lang][1]), cta_band(lang))
    return page(lang, "investment", "%s | %s" % (h1, SITE["brand"]), INVEST_INTRO[lang][0][:300], body,
                schemas=[breadcrumb_schema([(t("nav_home", lang), route("home", lang)),
                                            (t("nav_investment", lang), route("investment", lang))])])


def build_guide_index(lang):
    items = "".join('<div class="tile"><h3><a href="%s">%s</a></h3><p>%s</p></div>' % (
        route("article", lang, a["slug"]), e(a[lang]["title"]), e(a[lang]["meta"])) for a in ARTICLES)
    h1 = {"en": "Buying guide for Phuket property", "th": "คู่มือผู้ซื้ออสังหาริมทรัพย์ภูเก็ต", "zh": "普吉房产购买指南"}[lang]
    lead = {"en": "Ten guides covering ownership rules, process, costs, due diligence and development, written for buyers from outside Thailand.",
            "th": "คู่มือ 10 เรื่อง ครอบคลุมกฎการถือครอง ขั้นตอน ค่าใช้จ่าย การตรวจสอบ และการพัฒนาโครงการ เขียนสำหรับผู้ซื้อจากต่างประเทศ",
            "zh": "十篇指南，涵盖持有规则、流程、费用、尽职调查与开发，专为海外买家撰写。"}[lang]
    body = (
        '%s<section class="section"><div class="wrap"><h1>%s</h1><p class="lead">%s</p>'
        '<div class="notice">%s</div><div class="tiles">%s</div></div></section>%s'
    ) % (crumbs_html(lang, [(t("nav_home", lang), route("home", lang)), (t("nav_guide", lang), None)]),
         e(h1), e(lead), e(t("disclaimer_short", lang)), items, cta_band(lang))
    return page(lang, "guide", "%s | %s" % (h1, SITE["brand"]), lead[:300], body,
                schemas=[breadcrumb_schema([(t("nav_home", lang), route("home", lang)),
                                            (t("nav_guide", lang), route("guide", lang))])])


def build_article(lang, a):
    c = a[lang]
    sections = "".join("<h2>%s</h2>%s" % (e(h), "".join("<p>%s</p>" % e(p) for p in ps)) for h, ps in c["sections"])
    others = "".join('<div class="tile"><h3><a href="%s">%s</a></h3></div>' % (
        route("article", lang, o["slug"]), e(o[lang]["title"]))
        for o in ARTICLES if o["slug"] != a["slug"])
    crumbs = [(t("nav_home", lang), route("home", lang)),
              (t("nav_guide", lang), route("guide", lang)), (c["title"], None)]
    body = (
        '%s<article class="section"><div class="wrap narrow prose">'
        '<h1>%s</h1><p class="meta">%s %s</p><p class="lead">%s</p>%s'
        '<div class="notice"><strong>%s.</strong> %s</div>'
        '<p><a class="btn btn--ghost btn--small" href="%s">%s</a></p>'
        '</div></article>%s'
        '<section class="section section--mist"><div class="wrap"><h2>%s</h2><div class="tiles">%s</div></div></section>%s'
    ) % (crumbs_html(lang, crumbs), e(c["title"]), e(t("updated", lang)), e(a["updated"]),
         e(c["lead"]), sections,
         e(t("legal_disclaimer", lang)), e(t("disclaimer_short", lang)),
         route("guide", lang), e(t("back_to_guides", lang)),
         faq_block(lang, c.get("faq", [])),
         e(t("sec_related", lang)), others, cta_band(lang))
    schemas = [
        {"@context": "https://schema.org", "@type": "Article", "headline": c["title"],
         "description": c["meta"], "inLanguage": LANG_HTML[lang],
         "datePublished": a["updated"], "dateModified": a["updated"],
         "author": {"@type": "Organization", "name": SITE["legal_name"]},
         "publisher": {"@type": "Organization", "name": SITE["legal_name"]},
         "mainEntityOfPage": BASE_URL + route("article", lang, a["slug"])},
        breadcrumb_schema([(n, u) for n, u in crumbs if u] + [(c["title"], route("article", lang, a["slug"]))]),
    ]
    if c.get("faq"):
        schemas.append(faq_schema(c["faq"]))
    return page(lang, "article", "%s | %s" % (c["title"], SITE["brand"]), c["meta"], body,
                slug=a["slug"], schemas=schemas, og_type="article")


def build_about(lang):
    ab = ABOUT[lang]
    secs = "".join("<h2>%s</h2>%s" % (e(h), "".join("<p>%s</p>" % e(p) for p in ps)) for h, ps in ab["sections"])
    fields = [("Business name", SITE["legal_name"]), ("Agent", SITE["agent"]),
              ("Phone", SITE["phone"]), ("WhatsApp", SITE["whatsapp"]), ("LINE", SITE["line"]),
              ("Email", SITE["email"]), ("Address", SITE["address"]),
              ("Opening hours", SITE["hours"]), ("Google Business Profile", SITE["gbp_url"]),
              ("Established", SITE["founded"])]
    facts = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(k), e(v)) for k, v in fields)
    h1 = {"en": "About Andaman Land by Benz Supawat",
          "th": "เกี่ยวกับ Andaman Land by Benz Supawat",
          "zh": "关于 Andaman Land by Benz Supawat"}[lang]
    body = (
        '%s<section class="section"><div class="wrap narrow prose">'
        '<h1>%s</h1><p class="lead">%s</p>%s'
        '<h2>%s</h2><p class="meta">%s</p><dl class="factgrid">%s</dl>'
        '</div></section>%s'
    ) % (crumbs_html(lang, [(t("nav_home", lang), route("home", lang)), (t("nav_about", lang), None)]),
         e(h1), e(ab["lead"]), secs, e(ab["facts_title"]), e(ab["facts_note"]), facts, cta_band(lang))
    return page(lang, "about", "%s | %s" % (h1, SITE["brand"]), ab["lead"][:300], body,
                schemas=[org_schema(lang),
                         breadcrumb_schema([(t("nav_home", lang), route("home", lang)),
                                            (t("nav_about", lang), route("about", lang))])])


def build_contact(lang):
    h1, lead = CONTACT_COPY[lang]
    channels = (
        '<ul class="channels">'
        '<li><span>%s</span><a href="tel:%s">%s</a></li>'
        '<li><span>WhatsApp</span><a href="%s" rel="noopener">%s</a></li>'
        '<li><span>LINE</span><a href="%s" rel="noopener">%s</a></li>'
        '<li><span>%s</span><a href="mailto:%s">%s</a></li>'
        '<li><span>%s</span>%s</li>'
        '<li><span>%s</span>%s</li>'
        '</ul>'
    ) % (e(t("fm_phone", lang)), e(SITE["phone_href"]), e(SITE["phone"]),
         e(whatsapp_url("Hello Benz")), e(SITE["whatsapp"]), e(SITE["line_url"]), e(SITE["line"]),
         e(t("fm_email", lang)), e(SITE["email"]), e(SITE["email"]),
         e(t("p_location", lang)), e(SITE["address"]),
         e({"en": "Hours", "th": "เวลาทำการ", "zh": "营业时间"}[lang]), e(SITE["hours"]))
    body = (
        '%s<section class="section"><div class="wrap">'
        '<div class="detail"><div><h1>%s</h1><p class="lead">%s</p>%s'
        '<h2>%s</h2><div class="mapbox">[ADD GOOGLE MAPS EMBED OR OFFICE LOCATION]</div></div>'
        '<aside class="aside">%s%s</aside></div>'
        '</div></section>'
    ) % (crumbs_html(lang, [(t("nav_home", lang), route("home", lang)), (t("nav_contact", lang), None)]),
         e(h1), e(lead),
         enquiry_form(lang, title=None, sub=None, name="contact-%s" % lang),
         e(t("p_map", lang)), channels, contact_buttons(lang))
    return page(lang, "contact", "%s | %s" % (h1, SITE["brand"]), lead[:300], body,
                schemas=[org_schema(lang),
                         breadcrumb_schema([(t("nav_home", lang), route("home", lang)),
                                            (t("nav_contact", lang), route("contact", lang))])])


def build_legal(lang, key):
    title, blocks = LEGAL_PAGES[key][lang]
    secs = "".join("<h2>%s</h2>%s" % (e(h), "".join("<p>%s</p>" % e(p) for p in ps)) for h, ps in blocks)
    body = (
        '%s<section class="section"><div class="wrap narrow prose"><h1>%s</h1>%s'
        '<p class="meta">%s %s</p></div></section>'
    ) % (crumbs_html(lang, [(t("nav_home", lang), route("home", lang)), (title, None)]),
         e(title), secs, e(t("updated", lang)), TODAY)
    return page(lang, key, "%s | %s" % (title, SITE["brand"]), title, body,
                schemas=[breadcrumb_schema([(t("nav_home", lang), route("home", lang)),
                                            (title, route(key, lang))])])


def build_404(lang):
    txt = {"en": ("Page not found",
                  "The page you asked for has moved or never existed. The links below will get you back on track.",
                  "Browse land for sale", "Contact Benz"),
           "th": ("ไม่พบหน้านี้",
                  "หน้าที่คุณเปิดอาจถูกย้ายหรือไม่เคยมีอยู่ ลองใช้ลิงก์ด้านล่างเพื่อกลับเข้าสู่เว็บไซต์",
                  "ดูที่ดินที่ประกาศขาย", "ติดต่อ Benz"),
           "zh": ("页面未找到",
                  "您访问的页面可能已移动或从未存在。请使用下方链接继续浏览。",
                  "浏览在售土地", "联系 Benz")}[lang]
    body = ('<section class="section"><div class="wrap narrow prose"><h1>%s</h1><p>%s</p>'
            '<p class="btn-row"><a class="btn btn--brass" href="%s">%s</a>'
            '<a class="btn btn--ghost" href="%s">%s</a></p></div></section>') % (
        e(txt[0]), e(txt[1]), route("land", lang), e(txt[2]), route("contact", lang), e(txt[3]))
    doc = page(lang, "home", "%s | %s" % (txt[0], SITE["brand"]), txt[1], body)
    doc = doc.replace("</head>", '<meta name="robots" content="noindex,follow"/></head>', 1)
    out = os.path.join(DIST, lang, "404.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    if lang == "en":
        with open(os.path.join(DIST, "404.html"), "w", encoding="utf-8") as f:
            f.write(doc)


# ------------------------------------------------------------------- site files
def sitemaps():
    groups = {}
    for r, lang, freq, group in PAGES:
        groups.setdefault(group, []).append((r, freq))

    def urlset(entries):
        out = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
        for r, freq in entries:
            out.append("<url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq></url>" % (BASE_URL, r, TODAY, freq))
        out.append("</urlset>")
        return "\n".join(out)

    names = []
    for group, entries in groups.items():
        name = "sitemap-%s.xml" % group
        names.append(name)
        with open(os.path.join(DIST, name), "w", encoding="utf-8") as f:
            f.write(urlset(entries))

    index = ['<?xml version="1.0" encoding="UTF-8"?>', '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for n in sorted(names):
        index.append("<sitemap><loc>%s/%s</loc><lastmod>%s</lastmod></sitemap>" % (BASE_URL, n, TODAY))
    index.append("</sitemapindex>")
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(index))


def robots():
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: %s/sitemap.xml\n" % BASE_URL)


def root_redirect():
    doc = (
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>'
        '<title>%s</title><link rel="canonical" href="%s/en/"/>'
        '<meta http-equiv="refresh" content="0; url=/en/"/>'
        '<meta name="robots" content="noindex,follow"/></head>'
        '<body><p>Redirecting to <a href="/en/">English site</a>. '
        '<a href="/th/">ภาษาไทย</a> · <a href="/zh/">中文</a></p>'
        '<script>(function(){try{var l=localStorage.getItem("al_lang");'
        'if(l&&["en","th","zh"].indexOf(l)>-1){location.replace("/"+l+"/");return;}}catch(e){}'
        'location.replace("/en/");})();</script></body></html>'
    ) % (e(SITE["legal_name"]), BASE_URL)
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)


def build_preview():
    """Single-file clickable preview (dist/preview.html). Not used in production."""
    with open(os.path.join(ROOT, "assets", "css", "style.css"), encoding="utf-8") as f:
        css = f.read()
    sections = []
    for r, lang, title, body in PREVIEW:
        clean = re.sub(r'\sid="(listing-grid|filter-form|sort-select|result-count|result-empty|filter-reset|site-nav|main)"', "", body)
        sections.append('<div class="pv-page" data-route="%s" data-title="%s" data-lang="%s" hidden>%s</div>'
                        % (r, e(title), lang, clean))
    header_by_lang = {lang: header(lang, "home") for lang in LANGS}
    footer_by_lang = {lang: footer(lang) for lang in LANGS}
    chrome = "".join('<div class="pv-chrome" data-lang="%s" hidden>%s</div>' % (l, header_by_lang[l]) for l in LANGS)
    chrome_foot = "".join('<div class="pv-foot" data-lang="%s" hidden>%s</div>' % (l, footer_by_lang[l]) for l in LANGS)
    doc = PREVIEW_TEMPLATE % {"css": css, "chrome": chrome, "pages": "".join(sections), "foot": chrome_foot,
                              "title": e(SITE["legal_name"])}
    with open(os.path.join(DIST, "preview.html"), "w", encoding="utf-8") as f:
        f.write(doc)


PREVIEW_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"/>
<title>%(title)s — preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Karla:wght@400;600&family=IBM+Plex+Sans+Thai:wght@400;600&family=Noto+Sans+SC:wght@400;600&display=swap"/>
<style>
%(css)s
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box;}
.pv-note{background:#0A2A31;color:#C89B3E;font-size:.82rem;padding:7px 16px;text-align:center;}
.site-header{top:env(safe-area-inset-top,0px);}
</style>
</head>
<body>
<div class="pv-note">Preview build — images are generated placeholders. Deploy the dist/ folder for the real multi-page site.</div>
<div id="pv-chrome">%(chrome)s</div>
<main id="pv-main">%(pages)s</main>
<div id="pv-foot">%(foot)s</div>
<script>
(function(){
  var pages=[].slice.call(document.querySelectorAll('.pv-page'));
  function langOf(r){var m=r.match(/^\\/(en|th|zh)\\//);return m?m[1]:'en';}
  function show(route,query){
    var target=pages.filter(function(p){return p.dataset.route===route;})[0]||pages[0];
    pages.forEach(function(p){p.hidden=p!==target;});
    var lang=target.dataset.lang;
    document.documentElement.setAttribute('lang',lang==='zh'?'zh-Hans':lang);
    [].forEach.call(document.querySelectorAll('.pv-chrome,.pv-foot'),function(c){c.hidden=c.dataset.lang!==lang;});
    document.title=target.dataset.title;
    init(target,query);
    window.scrollTo(0,0);
  }
  /* ---- per-page listing filter + sort ---- */
  function init(page,query){
    var grid=page.querySelector('[data-listing-grid]');
    if(grid&&!grid.dataset.ready){
      grid.dataset.ready='1';
      var cards=[].slice.call(grid.querySelectorAll('[data-card]'));
      var form=page.querySelector('[data-filter-form]');
      var sort=page.querySelector('[data-sort]');
      var count=page.querySelector('[data-count]');
      var empty=page.querySelector('[data-empty]');
      var bands={price:{"0-10":[0,1e7],"10-30":[1e7,3e7],"30-60":[3e7,6e7],"60-100":[6e7,1e8],"100+":[1e8,1e12]},
                 size:{"0-1":[0,1],"1-3":[1,3],"3-10":[3,10],"10-50":[10,50],"50+":[50,1e6]}};
      function v(n){var el=form&&form.querySelector('[name="'+n+'"]');return el?el.value:'';}
      function band(raw,b,tbl){if(!b)return true;var n=parseFloat(raw);if(isNaN(n))return false;var r=tbl[b];return !r||(n>=r[0]&&n<r[1]);}
      function num(x,f){var n=parseFloat(x);return isNaN(n)?f:n;}
      function apply(){
        var shown=0;
        cards.forEach(function(c){
          var ok=(!v('location')||c.dataset.loc===v('location'))&&(!v('type')||c.dataset.type===v('type'))&&
                 band(c.dataset.price,v('price'),bands.price)&&band(c.dataset.size,v('size'),bands.size);
          c.hidden=!ok; if(ok)shown++;
        });
        if(count)count.textContent=shown;
        if(empty)empty.hidden=shown!==0;
        if(sort){
          var vis=cards.filter(function(c){return !c.hidden;});
          vis.sort(function(a,b){
            if(sort.value==='price-asc')return num(a.dataset.price,Infinity)-num(b.dataset.price,Infinity);
            if(sort.value==='price-desc')return num(b.dataset.price,-Infinity)-num(a.dataset.price,-Infinity);
            if(sort.value==='size')return num(b.dataset.size,-Infinity)-num(a.dataset.size,-Infinity);
            return (b.dataset.created||'').localeCompare(a.dataset.created||'');
          });
          vis.forEach(function(c){grid.appendChild(c);});
        }
      }
      if(form){
        form.addEventListener('submit',function(ev){ev.preventDefault();apply();});
        form.addEventListener('change',apply);
        var rs=page.querySelector('#filter-reset,[data-filter-reset]');
      }
      if(sort)sort.addEventListener('change',apply);
      page._apply=apply;
      apply();
    }
    if(query&&page._apply){
      var qs=new URLSearchParams(query);
      ['location','type','price','size'].forEach(function(k){
        var el=page.querySelector('[data-filter-form] [name="'+k+'"]');
        if(el&&qs.get(k))el.value=qs.get(k);
      });
      page._apply();
    }
    /* forms: validate then explain that preview cannot send */
    [].forEach.call(page.querySelectorAll('form[data-enquiry]'),function(f){
      if(f.dataset.ready)return; f.dataset.ready='1';
      var msgs=JSON.parse(f.getAttribute('data-messages')||'{}');
      var status=f.querySelector('.form-status');
      f.addEventListener('submit',function(ev){
        ev.preventDefault();
        var get=function(n){var el=f.querySelector('[name="'+n+'"]');return el?el.value.trim():'';};
        var set=function(n,msg){var s=f.querySelector('[data-err="'+n+'"]');if(s)s.textContent=msg||'';};
        var ok=true;
        ['name','email','message','contact'].forEach(function(n){set(n,'');});
        if(!get('name')){set('name',msgs.name);ok=false;}
        if(!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(get('email'))){set('email',msgs.email);ok=false;}
        if(!get('phone')&&!get('whatsapp')&&!get('line')){set('contact',msgs.contact);ok=false;}
        if(get('message').length<5){set('message',msgs.message);ok=false;}
        if(!status)return;
        if(ok){status.className='form-status show ok';status.textContent=msgs.ok+' (preview: nothing was actually sent)';f.reset();}
        else{status.className='form-status show bad';status.textContent=msgs.fail;}
      });
    });
  }
  document.addEventListener('click',function(ev){
    var a=ev.target.closest&&ev.target.closest('a[href^="/"]');
    if(!a)return;
    ev.preventDefault();
    location.hash='#'+a.getAttribute('href');
  });
  document.addEventListener('click',function(ev){
    var b=ev.target.closest&&ev.target.closest('.nav-toggle');
    if(!b)return;
    var nav=b.parentNode.querySelector('.nav');
    if(nav)nav.classList.toggle('open');
  });
  function fromHash(){
    var h=location.hash.slice(1)||'/en/';
    var q='';var i=h.indexOf('?');
    if(i>-1){q=h.slice(i+1);h=h.slice(0,i);}
    if(h.charAt(0)!=='/')h='/'+h;
    show(h,q);
  }
  window.addEventListener('hashchange',fromHash);
  fromHash();
})();
</script>
</body>
</html>
"""


# --------------------------------------------------------------------- runner
def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    with open(os.path.join(ROOT, "data", "properties.json"), encoding="utf-8") as f:
        props = json.load(f)["properties"]
    props.sort(key=lambda p: p["created_at"], reverse=True)

    # static assets
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))
    img_dir = os.path.join(DIST, "assets", "img")
    os.makedirs(img_dir, exist_ok=True)
    for p in props:
        with open(os.path.join(img_dir, p["slug"] + ".svg"), "w", encoding="utf-8") as f:
            f.write(land_svg(p["slug"], p["en"]["title"]))
    for s in LOCATION_PAGES:
        name = "land-for-sale-%s-phuket" % s
        with open(os.path.join(img_dir, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(land_svg(name, "Land for sale in %s, Phuket" % LOCATION_NAMES[s]["en"]))
    with open(os.path.join(img_dir, "andaman-land-phuket-og.svg"), "w", encoding="utf-8") as f:
        f.write(land_svg("andaman-land-phuket-og", "Andaman Land by Benz Supawat — land for sale in Phuket"))
    with open(os.path.join(img_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
                '<rect width="64" height="64" fill="#0A2A31"/>'
                '<path d="M14 44 L32 16 L50 44 Z" fill="none" stroke="#C89B3E" stroke-width="4"/></svg>')

    # admin dashboard (excluded from sitemap and robots)
    admin_src = os.path.join(ROOT, "admin", "index.html")
    if os.path.exists(admin_src):
        os.makedirs(os.path.join(DIST, "admin"), exist_ok=True)
        shutil.copy(admin_src, os.path.join(DIST, "admin", "index.html"))
        shutil.copy(os.path.join(ROOT, "data", "properties.json"),
                    os.path.join(DIST, "admin", "properties.json"))
    admin_login_src = os.path.join(ROOT, "admin-login.html")
    if os.path.exists(admin_login_src):
        shutil.copy(admin_login_src, os.path.join(DIST, "admin-login.html"))

    for lang in LANGS:
        write(route("home", lang), build_home(lang, props), "weekly", "pages", lang)

        h = {"en": "Land and property for sale in Phuket", "th": "ที่ดินและอสังหาริมทรัพย์ขายในภูเก็ต", "zh": "普吉在售土地与房产"}[lang]
        intro = {"en": "Every plot listed by Andaman Land, filterable by area, type, price and size.",
                 "th": "ทุกแปลงที่ Andaman Land ลงประกาศ กรองได้ตามทำเล ประเภท ราคา และขนาด",
                 "zh": "Andaman Land 的全部在售地块，可按区域、类型、价格与面积筛选。"}[lang]
        write(route("properties", lang), listing_page(lang, props, "properties", h, intro, intro), "daily", "properties", lang)

        h2 = {"en": "Land for sale in Phuket", "th": "ที่ดินขายในภูเก็ต", "zh": "普吉土地出售"}[lang]
        intro2 = {"en": "Land only: development land, beachfront land, investment land and commercial plots across Phuket.",
                  "th": "เฉพาะที่ดิน ทั้งที่ดินเพื่อพัฒนาโครงการ ที่ดินติดหาด ที่ดินเพื่อการลงทุน และที่ดินเชิงพาณิชย์ทั่วภูเก็ต",
                  "zh": "仅土地：普吉各区的开发用地、海滨土地、投资用地与商业地块。"}[lang]
        write(route("land", lang), listing_page(lang, props, "land", h2, intro2, intro2,
                                                only=lambda p: p["property_type"] in TYPE_ORDER),
              "daily", "properties", lang)

        for p in props:
            write(route("property", lang, p["slug"]), build_property(lang, p, props), "weekly", "properties", lang)

        write(route("locations", lang), build_locations_index(lang, props), "monthly", "locations", lang)
        for s in LOCATION_PAGES:
            write(route("location", lang, s), build_location(lang, s, props), "weekly", "locations", lang)

        write(route("investment", lang), build_investment(lang), "monthly", "pages", lang)
        write(route("guide", lang), build_guide_index(lang), "monthly", "articles", lang)
        for a in ARTICLES:
            write(route("article", lang, a["slug"]), build_article(lang, a), "monthly", "articles", lang)

        write(route("about", lang), build_about(lang), "monthly", "pages", lang)
        write(route("contact", lang), build_contact(lang), "monthly", "pages", lang)
        for key in ("disclaimer", "privacy", "terms", "cookies"):
            write(route(key, lang), build_legal(lang, key), "yearly", "pages", lang)

        build_404(lang)

    root_redirect()
    sitemaps()
    robots()
    build_preview()

    for extra in ("netlify.toml", "vercel.json", "_headers"):
        src = os.path.join(ROOT, extra)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(DIST, extra))

    print("Built %d pages into %s" % (len(PAGES), DIST))
    print("Languages: %s | properties: %d | locations: %d | articles: %d"
          % (", ".join(LANGS), len(props), len(LOCATION_PAGES), len(ARTICLES)))


if __name__ == "__main__":
    main()
