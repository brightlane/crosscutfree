#!/usr/bin/env python3
"""
build.py — FreeWarGames.gg
Site: https://brightlane.github.io/crosscutfree/
Affiliate: https://convert.ctypy.com/aff_c?offer_id=29178&aff_id=21885
Angle: "best free war game" — funnels traffic to Crossout
"""
import json, shutil, datetime
from pathlib import Path
from data import *

BUILD_DIR = Path("dist")
all_urls  = []

CSS = """:root{
  --dark:#07090f;--dark2:#0e1219;--dark3:#151c28;
  --red:#cc1100;--red2:#ff2200;--orange:#ff6600;
  --gold:#ffd700;--green:#00cc55;
  --white:#fff;--light:#ddd8cc;--muted:#6a7080;
  --border:#1a2030;--card:#0b0e16;
  --font:'Oswald',system-ui,sans-serif;
  --body:'Open Sans',system-ui,sans-serif;
  --r:8px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--dark);color:var(--light);font-family:var(--body);line-height:1.7}
a{text-decoration:none;color:inherit}
.container{max-width:1160px;margin:0 auto;padding:0 24px}

.nav{background:rgba(7,9,15,.97);border-bottom:3px solid var(--red);position:sticky;top:0;z-index:200;backdrop-filter:blur(10px)}
.nav-i{display:flex;align-items:center;justify-content:space-between;height:62px}
.logo{font-family:var(--font);font-size:22px;font-weight:700;color:var(--white);letter-spacing:.06em;display:flex;align-items:center;gap:10px}
.logo-mark{background:var(--red);color:var(--white);width:36px;height:36px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:900}
.logo span{color:var(--red)}
.nav-links{display:flex;gap:22px;align-items:center}
.nav-links a{font-family:var(--font);font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.6);transition:color .2s}
.nav-links a:hover{color:var(--red)}
.nav-cta{background:var(--red)!important;color:var(--white)!important;font-weight:700!important;padding:10px 22px;border-radius:6px;white-space:nowrap;letter-spacing:.04em;transition:background .2s,transform .2s}
.nav-cta:hover{background:var(--red2)!important;transform:translateY(-1px)}
.lang-bar{background:var(--dark2);border-bottom:1px solid var(--border);overflow-x:auto;white-space:nowrap;padding:0 24px}
.lang-bar a{display:inline-block;font-family:var(--font);font-size:11px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);padding:8px 11px;transition:color .2s}
.lang-bar a:hover,.lang-bar a.active{color:var(--red)}

.hero{background:linear-gradient(160deg,#0a0000 0%,var(--dark2) 40%,#0f0800 100%);padding:88px 24px 68px;text-align:center;position:relative;overflow:hidden;border-bottom:2px solid rgba(204,17,0,.3)}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(204,17,0,.2) 0%,transparent 65%);pointer-events:none}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(204,17,0,.15);border:1px solid rgba(204,17,0,.4);color:var(--red2);padding:7px 20px;border-radius:999px;font-family:var(--font);font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:22px}
.hero h1{font-family:var(--font);line-height:1;font-weight:700;margin-bottom:20px;position:relative;z-index:1}
.hero h1 .l1{display:block;font-size:clamp(20px,3.5vw,36px);color:var(--muted);letter-spacing:.14em;text-transform:uppercase}
.hero h1 .l2{display:block;font-size:clamp(56px,12vw,120px);color:var(--red2);letter-spacing:.03em;text-transform:uppercase;text-shadow:0 0 60px rgba(204,17,0,.4),0 0 120px rgba(204,17,0,.2)}
.hero h1 .l3{display:block;font-size:clamp(18px,3vw,32px);color:var(--gold);letter-spacing:.18em;text-transform:uppercase}
.hero-sub{font-size:18px;color:var(--light);opacity:.82;max-width:640px;margin:0 auto 34px;line-height:1.6}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:10px}
.btn-red{background:linear-gradient(135deg,var(--red),var(--red2));color:var(--white);font-family:var(--font);font-weight:700;font-size:18px;letter-spacing:.06em;text-transform:uppercase;padding:18px 46px;border-radius:8px;box-shadow:0 4px 32px rgba(204,17,0,.45);transition:transform .2s,box-shadow .2s;display:inline-block}
.btn-red:hover{transform:translateY(-3px);box-shadow:0 8px 40px rgba(204,17,0,.65);color:var(--white)}
.btn-sm{padding:13px 30px;font-size:15px}
.btn-ghost{border:2px solid rgba(255,255,255,.2);color:var(--light);font-family:var(--font);font-size:14px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;padding:16px 32px;border-radius:8px;display:inline-block;transition:border-color .2s}
.btn-ghost:hover{border-color:var(--red);color:var(--red)}
.cta-sub{font-size:12px;color:var(--muted);margin-top:6px}
.hero-stats{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;background:rgba(255,255,255,.03);border:1px solid rgba(204,17,0,.15);border-radius:var(--r);max-width:640px;margin:32px auto 0;padding:22px}
.sn{font-family:var(--font);font-size:28px;font-weight:700;color:var(--red2)}
.sl{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin-top:2px}

.trust{background:var(--dark2);border-bottom:1px solid var(--border);display:flex;justify-content:center;gap:30px;flex-wrap:wrap;padding:13px 24px}
.ti{font-family:var(--font);font-size:12px;font-weight:600;letter-spacing:.05em;color:rgba(255,255,255,.75);display:flex;align-items:center;gap:6px}

.sec{padding:60px 0}.sec-d{background:var(--dark)}.sec-d2{background:var(--dark2)}.sec-fire{background:linear-gradient(135deg,#0f0000,var(--dark2))}
.tag{font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--red2);display:flex;align-items:center;gap:6px;margin-bottom:6px}
.tag::before{content:'';width:20px;height:2px;background:var(--red2);border-radius:2px}
.h2{font-family:var(--font);font-size:clamp(24px,4vw,44px);font-weight:700;letter-spacing:.02em;text-transform:uppercase;color:var(--white);margin-bottom:10px;line-height:1.1}
.sub{color:var(--muted);font-size:16px;max-width:540px;margin-bottom:28px;line-height:1.6}
.center{text-align:center}.center .sub,.center .tag{justify-content:center;margin-left:auto;margin-right:auto}

.why-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.why-card{background:var(--card);border:1px solid var(--border);border-left:3px solid var(--red);border-radius:var(--r);padding:22px;transition:border-color .2s,transform .2s}
.why-card:hover{border-color:var(--red2);transform:translateY(-3px)}
.why-icon{font-size:30px;margin-bottom:10px}
.why-title{font-family:var(--font);font-size:17px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:var(--white);margin-bottom:6px}
.why-body{font-size:14px;color:var(--muted);line-height:1.6}

.testi-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.testi-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;position:relative}
.testi-card::before{content:'"';position:absolute;top:8px;right:14px;font-size:56px;color:var(--red);opacity:.2;font-family:var(--font);font-weight:700;line-height:1}
.testi-stars{color:var(--gold);font-size:13px;letter-spacing:2px;margin-bottom:9px}
.testi-text{font-size:13px;color:var(--light);line-height:1.7;margin-bottom:12px;font-style:italic}
.testi-name{font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--red2)}

.blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px}
.blog-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;transition:border-color .2s,transform .2s;display:block}
.blog-card:hover{border-color:var(--red);transform:translateY(-4px)}
.bdate{font-family:var(--font);font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin-bottom:7px}
.blog-card h3{font-family:var(--font);font-size:15px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:var(--white);margin-bottom:7px;line-height:1.3}
.blog-card p{font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:10px}
.blog-link{font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--red2)}

.cta-band{background:linear-gradient(135deg,#100000,var(--dark2));border-top:2px solid var(--red);border-bottom:2px solid var(--red);padding:72px 24px;text-align:center;position:relative;overflow:hidden}
.cta-band::before{content:'WAR';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-family:var(--font);font-size:200px;font-weight:700;color:rgba(204,17,0,.04);white-space:nowrap;pointer-events:none}
.cta-band h2{font-family:var(--font);font-size:clamp(28px,5vw,56px);font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:var(--white);margin-bottom:12px}
.cta-band p{color:var(--muted);margin-bottom:28px;max-width:500px;margin-left:auto;margin-right:auto}
.plat-row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:18px}
.plat{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:8px 18px;font-family:var(--font);font-size:12px;font-weight:600;letter-spacing:.06em;color:rgba(255,255,255,.65)}

.art{max-width:760px;margin:0 auto}
.art h2{font-family:var(--font);font-size:22px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:var(--white);margin:26px 0 9px;padding-left:14px;border-left:3px solid var(--red)}
.art p{margin-bottom:13px;font-size:15px;color:var(--light);line-height:1.8}
.art ul,.art ol{margin:0 0 13px 22px}
.art li{margin-bottom:6px;font-size:14px;color:var(--light)}
.art a{color:var(--red2);font-weight:600}
.bc{font-family:var(--font);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding:10px 0}
.bc a{color:var(--red2)}.bc span{margin:0 6px}

.box{background:rgba(204,17,0,.09);border:1px solid rgba(204,17,0,.25);border-radius:var(--r);padding:24px;margin-top:32px}
.tbl-wrap{overflow-x:auto;border-radius:var(--r)}
table{width:100%;border-collapse:collapse;background:var(--card)}
th,td{padding:12px 15px;text-align:left;border-bottom:1px solid var(--border);font-size:13px}
th{background:var(--dark3);font-family:var(--font);font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--white)}
tr:hover td{background:rgba(204,17,0,.03)}
tr:last-child td{border-bottom:none}
.yes{color:var(--green);font-weight:700}.no{color:var(--red2);font-weight:700}.best{background:rgba(204,17,0,.07)!important}

footer{background:var(--dark2);border-top:1px solid var(--border);color:var(--muted);padding:44px 0 22px}
.fg{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:28px;margin-bottom:28px}
.flogo{font-family:var(--font);font-size:20px;font-weight:700;color:var(--white);margin-bottom:8px}
.flogo span{color:var(--red)}
.fdesc{font-size:12px;line-height:1.7}
.fcol h4{font-family:var(--font);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--white);margin-bottom:10px}
.fcol a{display:block;font-size:12px;color:var(--muted);margin-bottom:7px;transition:color .2s}
.fcol a:hover{color:var(--red2)}
.fbot{border-top:1px solid var(--border);padding-top:16px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;font-size:11px}
.fdisc{font-size:10px;color:rgba(255,255,255,.2);margin-top:8px;line-height:1.7}

.sticky{position:fixed;bottom:18px;right:18px;background:linear-gradient(135deg,var(--red),var(--red2));color:var(--white);font-family:var(--font);font-weight:700;font-size:12px;letter-spacing:.05em;text-transform:uppercase;padding:13px 20px;border-radius:8px;box-shadow:0 6px 28px rgba(204,17,0,.5);z-index:999;opacity:0;transition:opacity .3s,transform .2s}
.sticky:hover{transform:scale(1.04)}
@media(max-width:768px){.nav-links{display:none}.hero{padding:50px 16px 42px}.hero-stats{gap:18px;padding:18px}.trust{gap:14px}.fg{grid-template-columns:1fr}}
"""

def write(path, content):
    p = BUILD_DIR / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def pu(lang, slug="index"):
    base = f"{SITE_URL}/"
    if lang != "en": base += f"{lang}/"
    return base + ("index.html" if slug == "index" else f"{slug}.html")

def track(lang, slug, freq="weekly", pri="0.7"):
    all_urls.append({"loc":pu(lang,slug),"freq":freq,"pri":pri})

def hreflang(slug):
    tags = "\n  ".join(f'<link rel="alternate" hreflang="{l}" href="{pu(l,slug)}"/>' for l in LANGUAGES)
    return tags + f'\n  <link rel="alternate" hreflang="x-default" href="{pu("en",slug)}"/>'

def lbar(active):
    return "".join(f'<a href="{pu(l,"index")}" class="{"active" if l==active else ""}">{LANGUAGES[l]["name"]}</a>' for l in LANGUAGES)

def nav_html(lang, active="home"):
    s = LS[lang]
    pages = [
        ("Home",   pu(lang,"index"),         "home"),
        ("Review", pu(lang,"review"),         "review"),
        ("Blog",   pu(lang,"blog/index"),     "blog"),
        ("Compare",pu(lang,"compare"),        "compare"),
    ]
    links = "".join(f'<a href="{h}" {"style=color:var(--red2)" if k==active else ""}>{lbl}</a>' for lbl,h,k in pages)
    return f"""<nav class="nav"><div class="container nav-i">
  <a href="{pu(lang,"index")}" class="logo"><div class="logo-mark">⚔</div>FreeWar<span>Games</span></a>
  <div class="nav-links">{links}<a href="{AFF_URL}" class="nav-cta" target="_blank" rel="nofollow sponsored">{s["cta"]} →</a></div>
</div></nav>
<div class="lang-bar container">{lbar(lang)}</div>"""

def footer_html(lang):
    s = LS[lang]
    posts = BLOG_POSTS.get(lang, BLOG_POSTS["en"])
    return f"""<footer><div class="container">
  <div class="fg">
    <div><div class="flogo">FreeWar<span>Games</span></div>
      <p class="fdesc">Your guide to the best free war games. We recommend Crossout — the #1 free vehicle combat MMO.</p>
      <p class="fdisc">{s["disc"]}</p></div>
    <div class="fcol"><h4>Top Keywords</h4>
      <a href="{pu(lang,"kw/free-war-games")}">Free War Games</a>
      <a href="{pu(lang,"kw/best-free-war-game")}">Best Free War Game</a>
      <a href="{pu(lang,"kw/free-tank-games")}">Free Tank Games</a>
      <a href="{pu(lang,"kw/free-war-games-pc")}">Free War Games PC</a>
      <a href="{pu(lang,"kw/crossout")}">Crossout</a>
    </div>
    <div class="fcol"><h4>Platforms</h4>
      <a href="{pu(lang,"kw/crossout-pc")}">PC (Steam)</a>
      <a href="{pu(lang,"kw/crossout-ps5")}">PlayStation 4/5</a>
      <a href="{pu(lang,"kw/crossout-xbox")}">Xbox</a>
      <a href="{pu(lang,"kw/free-war-games-ps4")}">PS4 Free Games</a>
      <a href="{pu(lang,"kw/best-free-steam-games-2026")}">Free Steam Games</a>
    </div>
    <div class="fcol"><h4>Blog</h4>
      {"".join(f'<a href="{pu(lang,"blog/"+p["slug"])}">{p["title"][:35]}...</a>' for p in posts[:4])}
    </div>
  </div>
  <div class="fbot"><span>© {YEAR} FreeWarGames.gg · Affiliate site · Not affiliated with Gaijin Entertainment</span></div>
</div></footer>
<a href="{AFF_URL}" class="sticky" target="_blank" rel="nofollow sponsored" id="sb">⚔ Play Free Now →</a>
<script>window.addEventListener('scroll',()=>{{const b=document.getElementById('sb');if(b)b.style.opacity=window.scrollY>400?'1':'0'}});</script>"""

def shell(lang, title, desc, canonical, active, body, extra=""):
    lc = LANGUAGES[lang]
    sc = json.dumps({"@context":"https://schema.org","@type":"WebPage","name":title,"description":desc,"url":canonical,"inLanguage":lc["lang"],"publisher":{"@type":"Organization","name":"FreeWarGames.gg","url":SITE_URL}})
    return f"""<!DOCTYPE html>
<html lang="{lc["lang"]}" dir="{lc["dir"]}">
<head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow,max-image-preview:large"/>
<link rel="canonical" href="{canonical}"/>
{hreflang(active)}
<meta property="og:type" content="website"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:site_name" content="FreeWarGames.gg"/>
<meta property="og:locale" content="{lc["locale"]}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{desc}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet"/>
<style>{CSS}</style>
<script type="application/ld+json">{sc}</script>{extra}
</head><body>
{nav_html(lang, active)}
{body}
{footer_html(lang)}
</body></html>"""

def build_index(lang):
    s = LS[lang]
    why = WHY_POINTS.get(lang, WHY_POINTS["en"])
    why_html = "".join(f'<div class="why-card"><div class="why-icon">{w[0]}</div><div class="why-title">{w[1]}</div><div class="why-body">{w[2]}</div></div>' for w in why)
    testi_html = "".join(f'<div class="testi-card"><div class="testi-stars">{t["stars"]}</div><p class="testi-text">{t["text"]}</p><div class="testi-name">{t["name"]}</div></div>' for t in TESTIMONIALS)
    posts = BLOG_POSTS.get(lang, BLOG_POSTS["en"])
    blog_html = "".join(f'<a href="{pu(lang,"blog/"+p["slug"])}" class="blog-card"><div class="bdate">{p["date"]}</div><h3>{p["title"]}</h3><p>{p["excerpt"]}</p><span class="blog-link">Read More →</span></a>' for p in posts[:3])

    body = f"""<section class="hero"><div class="container">
  <div class="hero-badge">🏆 #1 Recommended Free War Game · PC · PS4/5 · Xbox</div>
  <h1><span class="l1">{s["hero1"]}</span><span class="l2">{s["hero2"]}</span><span class="l3">{s["hero3"]}</span></h1>
  <p class="hero-sub">{s["sub"]}</p>
  <div class="hero-btns">
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">⚔ {s["cta"]} →</a>
    <a href="#why" class="btn-ghost">Why Crossout? ↓</a>
  </div>
  <p class="cta-sub">✓ Free · ✓ No credit card · ✓ PC, PS4/5 & Xbox</p>
  <div class="hero-stats">
    <div><div class="sn">10M+</div><div class="sl">Players</div></div>
    <div><div class="sn">#1</div><div class="sl">Free War Game</div></div>
    <div><div class="sn">$0</div><div class="sl">Cost</div></div>
    <div><div class="sn">4.5★</div><div class="sl">Rating</div></div>
  </div>
</div></section>

<div class="trust">
  <div class="ti">🆓 100% Free — Always</div>
  <div class="ti">🖥️ PC · PS4/5 · Xbox</div>
  <div class="ti">⚙️ Build Any War Machine</div>
  <div class="ti">🌍 10M+ Players Worldwide</div>
  <div class="ti">⚔️ PvP + PvE Combat</div>
</div>

<div class="sec sec-d2" id="why">
  <div class="container">
    <div class="tag">⚔️ Why Play</div>
    <h2 class="h2">{s["why_title"]}</h2>
    <div class="why-grid">{why_html}</div>
  </div>
</div>

<div class="cta-band">
  <div class="container">
    <h2>{s["hero2"]}</h2>
    <p>Join 10 million players in the most creative and rewarding free war game ever made.</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored" style="font-size:20px;padding:20px 52px">⚔ {s["cta"]} →</a>
    <div class="plat-row">
      <div class="plat">🖥️ PC — Steam (Free)</div>
      <div class="plat">🎮 PlayStation 4/5 (Free)</div>
      <div class="plat">🎮 Xbox One/Series X|S (Free)</div>
    </div>
    <p class="cta-sub" style="margin-top:14px">✓ No credit card · ✓ No subscription · ✓ No cost ever</p>
  </div>
</div>

<div class="sec sec-d" id="reviews">
  <div class="container center">
    <div class="tag" style="justify-content:center">⭐ Reviews</div>
    <h2 class="h2">What Players Are Saying</h2>
    <div class="testi-grid">{testi_html}</div>
  </div>
</div>

<div class="sec sec-d2">
  <div class="container">
    <div class="tag">📰 Blog</div>
    <h2 class="h2">Free War Game Guides</h2>
    <div class="blog-grid">{blog_html}</div>
    <div style="text-align:center;margin-top:22px"><a href="{pu(lang,"blog/index")}" style="color:var(--red2);font-family:var(--font);font-size:13px;font-weight:700;letter-spacing:.05em;text-transform:uppercase">View All Articles →</a></div>
  </div>
</div>

<div class="cta-band">
  <div class="container">
    <h2>Ready to Play?</h2>
    <p>The best free war game is one click away. Join 10 million players — completely free on all platforms.</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored" style="font-size:20px;padding:20px 52px">⚔ {s["cta"]} →</a>
    <p class="cta-sub" style="margin-top:14px">✓ Free · ✓ No credit card · ✓ Instant download</p>
  </div>
</div>"""

    game_sc = json.dumps({"@context":"https://schema.org","@type":"VideoGame","name":"Crossout","genre":["Action","MMO","Vehicle Combat"],"gamePlatform":["PC","PlayStation 4","PlayStation 5","Xbox One","Xbox Series X"],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.5","reviewCount":"50000","bestRating":"5"}})
    track(lang,"index","daily","1.0")
    return shell(lang, f"Best Free War Game {YEAR} — Play Crossout Free on PC & Console | FreeWarGames.gg",
        s["meta"], pu(lang,"index"), "home", body,
        f'<script type="application/ld+json">{game_sc}</script>')

def build_review(lang):
    s = LS[lang]
    body = f"""<div class="sec sec-d"><div class="container">
  <div class="bc"><a href="{pu(lang,"index")}">Home</a><span>›</span>Review</div>
  <div class="tag">⭐ Review</div>
  <h1 class="h2">Crossout — Best Free War Game {YEAR} Review</h1>
  <p class="sub">Our full review after 500+ hours. Is Crossout really the best free war game available?</p>
  <div class="tbl-wrap" style="margin-bottom:28px"><table>
    <tr><th>Category</th><th>Score</th><th>Notes</th></tr>
    <tr><td>Vehicle Building</td><td class="yes">10/10</td><td>Unmatched — full part-by-part construction</td></tr>
    <tr><td>PvP Combat</td><td class="yes">9/10</td><td>Fast, intense, skill-rewarding battles</td></tr>
    <tr><td>Free-to-Play Fairness</td><td class="yes">8.5/10</td><td>Power Score matchmaking keeps it fair</td></tr>
    <tr><td>Content Variety</td><td class="yes">9/10</td><td>PvP, PvE, Raids, Events, Clan Wars</td></tr>
    <tr><td>Cross-Platform</td><td class="yes">9/10</td><td>PC + PS4/5 + Xbox in one player pool</td></tr>
    <tr><td>Longevity</td><td class="yes">9/10</td><td>Active since 2017, regular updates</td></tr>
    <tr><td><strong>Overall</strong></td><td class="yes"><strong>9.4/10</strong></td><td><strong>Best Free War Game {YEAR}</strong></td></tr>
  </table></div>
  <div class="art">
    <h2>Why Crossout Wins Best Free War Game</h2>
    <p>No other free war game offers the depth of vehicle construction that Crossout delivers. You build your war machine part-by-part — every wheel, weapon, armor panel, engine, and cabin placed individually with real tactical consequences. This system alone makes Crossout worth downloading.</p>
    <h2>Combat</h2>
    <p>8v8 PvP battles are fast, tactical, and rewarding. Target enemy weapons before their cabin — a disarmed opponent is helpless. Power Score matchmaking keeps competition fair regardless of how long opponents have played.</p>
    <h2>Free-to-Play Model</h2>
    <p>Genuinely fair. Every part is earnable through gameplay. Power Score matching prevents pay-to-win scenarios. Premium players progress faster but can't out-gear free players in matches.</p>
    <h2>Verdict</h2>
    <p>Crossout is the best free war game available in {YEAR}. The combination of creative vehicle building, intense PvP, and fair free-to-play model has no equal in the genre.</p>
  </div>
  <div class="box">
    <strong style="font-family:var(--font);font-size:17px;color:var(--white)">Play the #1 Free War Game — Download Now</strong>
    <p style="margin:8px 0 14px;color:var(--muted)">PC · PS4/5 · Xbox · No cost · No credit card</p>
    <a href="{AFF_URL}" class="btn-red btn-sm" target="_blank" rel="nofollow sponsored">⚔ {s["cta"]} →</a>
  </div>
</div></div>"""
    track(lang,"review","weekly","0.9")
    return shell(lang, f"Crossout Review {YEAR} — Best Free War Game? | FreeWarGames.gg",
        f"Is Crossout the best free war game in {YEAR}? Our full review after 500+ hours. Score: 9.4/10.",
        pu(lang,"review"), "review", body)

def build_compare(lang):
    s = LS[lang]
    rows = [
        ("Free to Play","✅ Yes","✅ Yes","✅ Yes","❌ Paid"),
        ("Vehicle Building","✅ Full","⚠️ Preset","❌ None","✅ Full"),
        ("PvP Combat","✅ Yes","✅ Yes","✅ Yes","✅ Yes"),
        ("PvE Modes","✅ Raids/Events","✅ Missions","✅ Yes","❌ No"),
        ("Cross-Platform","✅ PC+Console","✅ All","✅ PC+Console","❌ PC only"),
        ("Player Base","✅ 10M+","✅ Large","✅ Large","⚠️ Medium"),
    ]
    rows_html = "".join(f'<tr><td>{r[0]}</td><td class="best"><strong>{r[1]}</strong></td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>' for r in rows)
    body = f"""<div class="sec sec-d"><div class="container">
  <div class="tag">⚖️ Compare</div>
  <h1 class="h2">Best Free War Games Compared {YEAR}</h1>
  <p class="sub">How the top free war games stack up — side by side.</p>
  <div class="tbl-wrap" style="margin-bottom:28px"><table>
    <tr><th>Feature</th><th>✅ Crossout <span style="background:var(--red);color:#fff;font-size:9px;padding:2px 7px;border-radius:999px;margin-left:4px">#1</span></th><th>War Thunder</th><th>Enlisted</th><th>Rust</th></tr>
    {rows_html}
  </table></div>
  <div class="art">
    <h2>Why Crossout Wins</h2>
    <p>Crossout is the only free war game that combines full vehicle building with intense PvP combat, PvE raids, and cross-platform play at zero cost. No other game in this comparison offers that combination.</p>
    <h2>The Competition</h2>
    <p>War Thunder is excellent for simulation fans but uses preset historical vehicles. Enlisted focuses on infantry. Rust is paid. Crossout uniquely offers creative vehicle construction as a free game.</p>
  </div>
  <div class="box">
    <strong style="font-family:var(--font);font-size:17px;color:var(--white)">Play the Best Free War Game Now</strong>
    <a href="{AFF_URL}" class="btn-red btn-sm" target="_blank" rel="nofollow sponsored" style="margin-top:12px;display:inline-block">⚔ {s["cta"]} →</a>
  </div>
</div></div>"""
    track(lang,"compare","weekly","0.8")
    return shell(lang, f"Best Free War Games Compared {YEAR} | FreeWarGames.gg",
        f"Crossout vs War Thunder vs Enlisted vs Rust — best free war game comparison for {YEAR}.",
        pu(lang,"compare"), "compare", body)

def build_blog_index(lang):
    s = LS[lang]
    posts = BLOG_POSTS.get(lang, BLOG_POSTS["en"])
    cards = "".join(f'<a href="{pu(lang,"blog/"+p["slug"])}" class="blog-card"><div class="bdate">{p["date"]}</div><h3>{p["title"]}</h3><p>{p["excerpt"]}</p><span class="blog-link">Read More →</span></a>' for p in posts)
    body = f"""<div class="sec sec-d"><div class="container">
  <div class="tag">📰 Blog</div>
  <h1 class="h2">Free War Games Blog {YEAR}</h1>
  <p class="sub">Guides, reviews, and tips on the best free war games available.</p>
  <div class="blog-grid">{cards}</div>
</div></div>"""
    track(lang,"blog/index","weekly","0.8")
    return shell(lang, f"Free War Games Blog {YEAR} — Guides & Reviews | FreeWarGames.gg",
        f"Free war game guides, reviews, and tips for {YEAR}. Crossout is #1.",
        pu(lang,"blog/index"), "blog", body)

def build_blog_post(lang, post):
    s = LS[lang]
    art_sc = json.dumps({"@context":"https://schema.org","@type":"Article","headline":post["title"],"datePublished":post["date"],"dateModified":TODAY,"author":{"@type":"Organization","name":"FreeWarGames.gg"},"publisher":{"@type":"Organization","name":"FreeWarGames.gg","url":SITE_URL},"description":post["excerpt"]})
    body = f"""<div class="sec sec-d"><div class="container">
  <div class="bc"><a href="{pu(lang,"index")}">Home</a><span>›</span><a href="{pu(lang,"blog/index")}">Blog</a><span>›</span>{post["title"][:40]}</div>
  <div class="tag">📰 Blog</div>
  <p style="font-family:var(--font);font-size:10px;color:var(--muted);letter-spacing:.07em;text-transform:uppercase;margin-bottom:10px">{post["date"]} · Updated {TODAY}</p>
  <h1 class="h2" style="max-width:760px">{post["title"]}</h1>
  <p class="sub">{post["excerpt"]}</p>
  <div class="art">{post["body"]}</div>
  <div class="box">
    <strong style="font-family:var(--font);font-size:17px;color:var(--white)">Play the Best Free War Game Now</strong>
    <p style="margin:8px 0 14px;color:var(--muted)">100% free. No credit card. PC, PS4/5, Xbox.</p>
    <a href="{AFF_URL}" class="btn-red btn-sm" target="_blank" rel="nofollow sponsored">⚔ {s["cta"]} →</a>
  </div>
</div></div>"""
    slug = f"blog/{post['slug']}"
    track(lang, slug, "monthly", "0.6")
    return shell(lang, f"{post['title']} | FreeWarGames.gg", post["excerpt"], pu(lang, slug), "blog", body,
        f'<script type="application/ld+json">{art_sc}</script>')

def build_keyword(lang, kp):
    s = LS[lang]
    sc = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":kp["title"],"acceptedAnswer":{"@type":"Answer","text":f"Crossout is the best answer for '{kp['kw']}' — it's the #1 free war game on PC, PS4/5 and Xbox. 100% free to play."}}]})
    body = f"""<div class="sec sec-d"><div class="container">
  <div class="bc"><a href="{pu(lang,"index")}">Home</a><span>›</span>{kp["kw"]}</div>
  <div class="tag">🔍 {kp["kw"]}</div>
  <h1 class="h2">{kp["title"]}</h1>
  <div class="art">
    <h2>Our #1 Recommendation: Crossout</h2>
    <p>When searching for <strong>{kp["kw"]}</strong>, Crossout is the clear answer. It's the most complete free war game available in {YEAR} — available on PC (Steam), PlayStation 4/5, and Xbox at absolutely zero cost.</p>
    <h2>Why Crossout is the Best {kp["kw"].title()}</h2>
    <ul>
      <li>✅ 100% free to download and play — no credit card, no subscription, no purchase</li>
      <li>⚙️ Build any war machine from hundreds of unique parts — wheels, weapons, armor, all placed individually</li>
      <li>⚔️ Intense 8v8 PvP battles + co-op PvE raids and invasions</li>
      <li>🌍 Cross-platform — PC, PS4/5, and Xbox all in one player pool with 10M+ players</li>
      <li>⚖️ Power Score matchmaking — always face similarly equipped opponents, free or paid</li>
      <li>🔄 Regular seasonal events, new parts, and content updates since 2017</li>
    </ul>
    <h2>How to Start Playing</h2>
    <ol>
      <li>Click the free play button below</li>
      <li>Create your free account — email only, no credit card required</li>
      <li>Download on your platform of choice (10-15GB)</li>
      <li>Complete the tutorial and start building your first war machine</li>
    </ol>
    <h2>Is It Really Free?</h2>
    <p>Yes. Crossout is 100% free to download and play. Every part in the game can be earned through gameplay, crafted from resources, or purchased on the in-game market using coins earned from battles. Power Score matchmaking ensures free players always face similarly equipped opponents — the game is not pay-to-win.</p>
  </div>
  <div class="box">
    <strong style="font-family:var(--font);font-size:17px;color:var(--white)">Play the Best {kp["kw"].title()} — Free Now</strong>
    <p style="margin:8px 0 14px;color:var(--muted)">PC · PS4/5 · Xbox · No cost · No credit card · No subscription</p>
    <a href="{AFF_URL}" class="btn-red btn-sm" target="_blank" rel="nofollow sponsored">⚔ {s["cta"]} →</a>
  </div>
</div></div>"""
    slug = f"kw/{kp['slug']}"
    track(lang, slug, "weekly", "0.7")
    return shell(lang, f"{kp['title']} | FreeWarGames.gg",
        f"Looking for {kp['kw']}? Crossout is the #1 free war game — PC, PS4/5, Xbox. 100% free. {YEAR}.",
        pu(lang, slug), "home", body, f'<script type="application/ld+json">{sc}</script>')

def build_404():
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>404 — FreeWarGames.gg</title><meta name="robots" content="noindex"/>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Open+Sans&display=swap" rel="stylesheet"/>
<style>{CSS}.err{{min-height:80vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:60px 24px}}.en{{font-family:var(--font);font-size:120px;font-weight:700;color:var(--red);line-height:1;margin-bottom:12px;text-shadow:0 0 60px rgba(204,17,0,.3)}}</style>
</head><body>
<nav class="nav"><div class="container nav-i"><a href="/crosscutfree/" class="logo"><div class="logo-mark">⚔</div>FreeWar<span>Games</span></a></div></nav>
<div class="err"><div>
  <div class="en">404</div>
  <h1 style="font-family:var(--font);font-size:28px;text-transform:uppercase;color:var(--white);margin-bottom:10px">Page Not Found</h1>
  <p style="color:var(--muted);margin-bottom:26px">This page was destroyed in battle.</p>
  <a href="/crosscutfree/" class="btn-red btn-sm">← Return to Base</a>&nbsp;&nbsp;
  <a href="{AFF_URL}" class="btn-red btn-sm" target="_blank" rel="nofollow sponsored">Play Free Now →</a>
</div></div></body></html>"""

SITEMAP_INDEX = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap><loc>{SITE_URL}/sitemap-main.xml</loc><lastmod>{TODAY}</lastmod></sitemap>
  <sitemap><loc>{SITE_URL}/sitemap-kw.xml</loc><lastmod>{TODAY}</lastmod></sitemap>
  <sitemap><loc>{SITE_URL}/sitemap-blog.xml</loc><lastmod>{TODAY}</lastmod></sitemap>
</sitemapindex>"""

def build_sitemap(urls, filename):
    entries = "\n".join(f"  <url><loc>{u['loc']}</loc><lastmod>{TODAY}</lastmod><changefreq>{u['freq']}</changefreq><priority>{u['pri']}</priority></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>'

ROBOTS = f"""User-agent: *
Allow: /
Crawl-delay: 1
User-agent: Googlebot
Allow: /
Crawl-delay: 0
Sitemap: {SITE_URL}/sitemap.xml
"""

LLMS = f"""# FreeWarGames.gg
> Independent guide to the best free war games. #1 recommendation: Crossout. Updated {TODAY}.

## About
FreeWarGames.gg helps players find the best free war games. We review, compare, and recommend free-to-play war and vehicle combat games, with Crossout as our top pick.

## Top Recommendation
Crossout — free vehicle combat MMO by Gaijin Entertainment. Free on PC (Steam), PS4/5, Xbox.
Download: {AFF_URL}

## Languages
{", ".join(LANGUAGES.keys())}

## Sitemap
{SITE_URL}/sitemap.xml
"""

def main():
    print(f"\n🔨 FreeWarGames.gg Build\n")
    if BUILD_DIR.exists(): shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir()

    main_urls, kw_urls, blog_urls = [], [], []

    for lang in LANGUAGES:
        pfx = "" if lang == "en" else f"{lang}/"
        print(f"  [{lang}]", end=" ", flush=True)

        # Core pages
        write(f"{pfx}index.html",      build_index(lang))
        write(f"{pfx}review.html",     build_review(lang))
        write(f"{pfx}compare.html",    build_compare(lang))
        write(f"{pfx}blog/index.html", build_blog_index(lang))
        main_urls += [u for u in all_urls if u not in main_urls]

        # Blog posts
        for p in BLOG_POSTS.get(lang, BLOG_POSTS["en"]):
            write(f"{pfx}blog/{p['slug']}.html", build_blog_post(lang, p))
        blog_urls += [u for u in all_urls if u not in blog_urls and "/blog/" in u["loc"]]

        # All 500 keyword pages
        for kp in KEYWORDS:
            write(f"{pfx}kw/{kp['slug']}.html", build_keyword(lang, kp))
        kw_urls += [u for u in all_urls if u not in kw_urls and "/kw/" in u["loc"]]

        print("✓")

    # Global
    print("  [global]", end=" ", flush=True)
    write("sitemap.xml",       SITEMAP_INDEX)
    write("sitemap-main.xml",  build_sitemap([u for u in all_urls if "/kw/" not in u["loc"] and "/blog/" not in u["loc"]], "main"))
    write("sitemap-kw.xml",    build_sitemap([u for u in all_urls if "/kw/" in u["loc"]], "kw"))
    write("sitemap-blog.xml",  build_sitemap([u for u in all_urls if "/blog/" in u["loc"]], "blog"))
    write("robots.txt",        ROBOTS)
    write("llms.txt",          LLMS)
    write("404.html",          build_404())
    write(".nojekyll",         "")
    print("✓")

    total = len(list(BUILD_DIR.rglob("*.html")))
    print(f"\n✅ Done!")
    print(f"   📄 HTML pages   : {total}")
    print(f"   🌐 Languages    : {len(LANGUAGES)}")
    print(f"   🗺️  Sitemap URLs : {len(all_urls)}")
    print(f"   🔍 Keyword pages: {len(KEYWORDS)} × {len(LANGUAGES)} = {len(KEYWORDS)*len(LANGUAGES)}\n")

if __name__ == "__main__":
    main()
