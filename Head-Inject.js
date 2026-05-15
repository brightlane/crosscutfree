/**
 * head-inject.js — BrightLane / SaneBox
 * ─────────────────────────────────────
 * Run once: node head-inject.js
 * Patches <head> of EVERY .html file in this folder and all subfolders.
 * Safe to re-run — detects already-patched files and skips them.
 *
 * Usage:
 *   node head-inject.js              ← patch all .html files
 *   node head-inject.js index.html   ← patch one specific file
 */

const fs   = require('fs');
const path = require('path');

// ─── CONFIG ──────────────────────────────────────────────────────────────────
// Page-specific overrides. Key = filename (any depth). Falls back to defaults.
const PAGE_CONFIG = {
  'index.html': {
    title:       'SaneBox Review 2026: AI Email Organizer That Saves Hours Every Week',
    description: 'AI-powered inbox management that reduces email clutter by 30–50%. Full 2026 review, pricing, pros, cons, and free 2-week trial.',
    url:         'https://brightlane.github.io/sanebox/',
  },
  'blog.html': {
    title:       'SaneBox Blog 2026 — Daily Email Productivity Tips | 8 Languages',
    description: 'Daily email productivity tips in English, Spanish, French, German, Portuguese, Japanese, Italian and Dutch. Featuring SaneBox AI email manager.',
    url:         'https://brightlane.github.io/sanebox/blog.html',
  },
  'distribute.html': {
    title:       'SaneBox Social Distribution Dashboard | BrightLane',
    description: 'Auto-distribute SaneBox content across Reddit, Twitter, Pinterest, LinkedIn, and Facebook in 8 languages.',
    url:         'https://brightlane.github.io/sanebox/distribute.html',
  },
  // Add future pages here, or let them fall back to defaults below.
};

const DEFAULTS = {
  title:       'SaneBox Review 2026 | BrightLane',
  description: 'AI email organizer that reduces inbox clutter by up to 50%. Free 2-week trial + $15 credit.',
  url:         'https://brightlane.github.io/sanebox/',
};

// Marker so we never double-inject
const INJECT_MARKER = '<!-- BL-HEAD-INJECTED -->';

// ─── HEAD BLOCK BUILDER ───────────────────────────────────────────────────────
function buildHeadBlock(cfg) {
  const { title, description, url } = cfg;
  return `${INJECT_MARKER}

  <!-- ═══ CORE ═══ -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <!-- ═══ VERIFICATION ═══ -->
  <meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ">
  <meta name="msvalidate.01" content="574044E39556B8B8DAAF1D1F233C87B0">
  <meta name="p:domain_verify" content="PASTE_PINTEREST_TOKEN_HERE">

  <!-- ═══ SEO ═══ -->
  <title>${title}</title>
  <meta name="description" content="${description}">
  <meta name="keywords" content="SaneBox review 2026, AI email organizer, inbox zero, email productivity, SaneLater, email management tool">
  <meta name="author" content="BrightLane Editorial">
  <meta name="publisher" content="BrightLane">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="googlebot" content="index,follow">
  <meta name="bingbot" content="index,follow">
  <meta name="language" content="English">
  <meta name="geo.region" content="US">
  <meta name="geo.placename" content="United States">
  <meta name="ICBM" content="37.0902, -95.7129">

  <!-- ═══ OPEN GRAPH ═══ -->
  <meta property="og:locale" content="en_US">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="BrightLane">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${description}">
  <meta property="og:url" content="${url}">
  <meta property="og:image" content="https://brightlane.github.io/assets/sanebox-cover.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="SaneBox AI Email Organizer — BrightLane Review 2026">
  <meta property="article:author" content="BrightLane Editorial">
  <meta property="article:published_time" content="2026-01-01T00:00:00Z">
  <meta property="article:modified_time" content="2026-05-14T00:00:00Z">
  <meta property="article:section" content="Email Productivity">
  <meta property="article:tag" content="SaneBox">
  <meta property="article:tag" content="inbox zero">
  <meta property="article:tag" content="AI email management">
  <meta property="article:tag" content="productivity 2026">

  <!-- ═══ TWITTER / X ═══ -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@BrightLaneHQ">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${description}">
  <meta name="twitter:image" content="https://brightlane.github.io/assets/sanebox-cover.jpg">

  <!-- ═══ GOOGLE NEWS + DISCOVER ═══ -->
  <meta name="news_keywords" content="SaneBox, email productivity, inbox zero, AI email, email management 2026">
  <meta name="syndication-source" content="https://brightlane.github.io/sanebox/">
  <meta name="original-source" content="https://brightlane.github.io/sanebox/">

  <!-- ═══ APPLE NEWS ═══ -->
  <meta name="apple-news:identifier" content="sanebox-review-2026">
  <meta name="format-detection" content="telephone=no">

  <!-- ═══ MICROSOFT START / MSN ═══ -->
  <meta name="ms.locale" content="en-us">
  <meta name="ms.category" content="productivity">

  <!-- ═══ AI / LLM CRAWLERS ═══ -->
  <meta name="ai-content-declaration" content="human-written, AI-assisted research">
  <meta name="content-type" content="Product Review">
  <meta name="document-classification" content="Productivity Software Review">
  <meta name="coverage" content="Worldwide">
  <meta name="distribution" content="Global">

  <!-- ═══ PWA ═══ -->
  <link rel="manifest" href="/sanebox/manifest.json">
  <meta name="theme-color" content="#1e40af">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="BrightLane">
  <link rel="apple-touch-icon" href="/sanebox/icons/icon-192.png">

  <!-- ═══ CANONICAL + HREFLANG ═══ -->
  <link rel="canonical" href="${url}">
  <link rel="alternate" hreflang="en"       href="https://brightlane.github.io/sanebox/">
  <link rel="alternate" hreflang="es"       href="https://brightlane.github.io/sanebox/blog.html#es">
  <link rel="alternate" hreflang="fr"       href="https://brightlane.github.io/sanebox/blog.html#fr">
  <link rel="alternate" hreflang="de"       href="https://brightlane.github.io/sanebox/blog.html#de">
  <link rel="alternate" hreflang="pt"       href="https://brightlane.github.io/sanebox/blog.html#pt">
  <link rel="alternate" hreflang="ja"       href="https://brightlane.github.io/sanebox/blog.html#ja">
  <link rel="alternate" hreflang="it"       href="https://brightlane.github.io/sanebox/blog.html#it">
  <link rel="alternate" hreflang="nl"       href="https://brightlane.github.io/sanebox/blog.html#nl">
  <link rel="alternate" hreflang="x-default" href="https://brightlane.github.io/sanebox/">

  <!-- ═══ FEEDS + DISCOVERY ═══ -->
  <link rel="alternate" type="application/rss+xml" title="BrightLane RSS" href="/sanebox/feed.xml">
  <link rel="search" type="application/opensearchdescription+xml" title="BrightLane" href="/sanebox/opensearch.xml">
  <link rel="author" href="/sanebox/humans.txt">
  <link rel="preconnect" href="https://try.sanebox.com">
  <link rel="dns-prefetch" href="https://try.sanebox.com">

  <!-- ═══ WEBMENTION ═══ -->
  <link rel="webmention" href="https://webmention.io/brightlane.github.io/webmention">
  <link rel="pingback" href="https://webmention.io/brightlane.github.io/xmlrpc">

  <!-- ═══ NEWSARTICLE SCHEMA ═══ -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "headline": "${title}",
    "description": "${description}",
    "image": {
      "@type": "ImageObject",
      "url": "https://brightlane.github.io/assets/sanebox-cover.jpg",
      "width": 1200,
      "height": 630
    },
    "author": {
      "@type": "Organization",
      "name": "BrightLane",
      "url": "https://brightlane.github.io/"
    },
    "publisher": {
      "@type": "Organization",
      "name": "BrightLane",
      "logo": {
        "@type": "ImageObject",
        "url": "https://brightlane.github.io/assets/logo.png",
        "width": 600,
        "height": 60
      }
    },
    "datePublished": "2026-01-01T00:00:00Z",
    "dateModified": "2026-05-14T00:00:00Z",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "${url}"
    },
    "articleSection": "Email Productivity",
    "keywords": "SaneBox, AI email organizer, inbox zero, email management 2026",
    "inLanguage": "en-US",
    "isAccessibleForFree": true
  }
  </script>`;
}

// ─── FILE WALKER ──────────────────────────────────────────────────────────────
function getAllHtmlFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(getAllHtmlFiles(full));
    } else if (entry.name.endsWith('.html')) {
      results.push(full);
    }
  }
  return results;
}

// ─── PATCHER ─────────────────────────────────────────────────────────────────
function patchFile(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Skip if already injected
  if (html.includes(INJECT_MARKER)) {
    console.log(`⏭  Skipped (already patched): ${filePath}`);
    return;
  }

  // Find <head> open tag
  const headMatch = html.match(/<head[^>]*>/i);
  if (!headMatch) {
    console.log(`⚠️  No <head> found, skipping: ${filePath}`);
    return;
  }

  // Determine config for this file
  const basename = path.basename(filePath);
  const cfg = { ...DEFAULTS, ...(PAGE_CONFIG[basename] || {}) };

  // Remove any existing duplicate charset/viewport/title so we don't double-up
  html = html
    .replace(/<meta\s+charset=["'][^"']*["'][^>]*>/gi, '')
    .replace(/<meta\s+name=["']viewport["'][^>]*>/gi, '')
    .replace(/<meta\s+http-equiv=["']X-UA-Compatible["'][^>]*>/gi, '')
    .replace(/<title>[^<]*<\/title>/i, '');

  // Inject right after <head>
  const insertAfter = headMatch[0];
  const injection   = `\n${buildHeadBlock(cfg)}\n`;
  html = html.replace(insertAfter, insertAfter + injection);

  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`✅ Patched: ${filePath}`);
}

// ─── MAIN ─────────────────────────────────────────────────────────────────────
const targetArg = process.argv[2]; // optional: specific file

if (targetArg) {
  // Single file mode
  const abs = path.resolve(targetArg);
  if (!fs.existsSync(abs)) {
    console.error(`❌ File not found: ${abs}`);
    process.exit(1);
  }
  patchFile(abs);
} else {
  // Batch mode — all .html in current directory tree
  const root  = process.cwd();
  const files = getAllHtmlFiles(root);
  if (files.length === 0) {
    console.log('No .html files found.');
  } else {
    console.log(`Found ${files.length} HTML file(s). Patching...\n`);
    files.forEach(patchFile);
    console.log('\nDone.');
  }
}
