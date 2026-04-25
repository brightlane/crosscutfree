const fs = require("fs");
const path = require("path");

/**
 * =========================
 * CONFIG
 * =========================
 */
const CONFIG = {
  domain: "https://brightlane.github.io/sanebox/",
  outputDir: path.join(__dirname, "sanebox"),
  keywordsFile: path.join(__dirname, "keywords.json"),
  sitemapPath: path.join(__dirname, "sitemap.xml"),

  affiliateLinks: [
    "https://try.sanebox.com/efdrajzfvk2c?utm_source=hub",
    "https://try.sanebox.com/efdrajzfvk2c?utm_source=pricing",
    "https://try.sanebox.com/efdrajzfvk2c?utm_source=review",
    "https://try.sanebox.com/efdrajzfvk2c?utm_source=compare"
  ]
};

/**
 * =========================
 * LOAD KEYWORDS
 * =========================
 */
function loadKeywords() {
  const raw = fs.readFileSync(CONFIG.keywordsFile, "utf-8");
  return JSON.parse(raw);
}

/**
 * =========================
 * INTENT CLASSIFIER
 * =========================
 */
function getIntent(keyword) {
  if (keyword.includes("vs")) return "comparison";
  if (keyword.includes("pricing") || keyword.includes("price")) return "transactional";
  if (keyword.includes("how") || keyword.includes("what")) return "informational";
  if (keyword.includes("for")) return "use-case";
  return "commercial";
}

/**
 * =========================
 * SLUG GENERATOR
 * =========================
 */
function slugify(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

/**
 * =========================
 * AFFILIATE ROTATOR (DETERMINISTIC)
 * =========================
 */
function getAffiliateLink(keyword) {
  const index = Math.abs(hashCode(keyword)) % CONFIG.affiliateLinks.length;
  return CONFIG.affiliateLinks[index];
}

function hashCode(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = (hash << 5) - hash + str.charCodeAt(i);
    hash |= 0;
  }
  return hash;
}

/**
 * =========================
 * PAGE TEMPLATE
 * =========================
 */
function generatePage({ keyword, intent, links }) {
  const slug = slugify(keyword);
  const affiliate = getAffiliateLink(keyword);

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>${keyword} | SaneBox AI Email Guide</title>
<meta name="description" content="Learn about ${keyword}. AI email automation, productivity insights, and SaneBox optimization guide.">

<meta name="keywords" content="${keyword}, sanebox, email automation, inbox management">

<style>
body { font-family: Arial; max-width: 900px; margin: auto; padding: 20px; }
a.cta { background:#10b981;color:#fff;padding:12px 18px;display:inline-block;margin:10px 0;text-decoration:none;border-radius:6px; }
.box { background:#f5f5f5;padding:15px;margin:15px 0; }
</style>
</head>

<body>

<h1>${keyword}</h1>

<div class="box">
<strong>Intent:</strong> ${intent}
<br>
<strong>Category:</strong> SaneBox AI Email Optimization
</div>

<p>
This page explains <strong>${keyword}</strong> in the context of AI email productivity and automation.
SaneBox helps reduce inbox overload and improves workflow efficiency.
</p>

<a class="cta" href="${affiliate}" rel="sponsored">Try SaneBox Free</a>

<h2>Related Pages</h2>
<ul>
${links.map(l => `<li><a href="${l.url}">${l.keyword}</a></li>`).join("\n")}
</ul>

<footer>
<p>Affiliate disclosure: This page contains affiliate links.</p>
</footer>

</body>
</html>`;
}

/**
 * =========================
 * BUILD GRAPH
 * =========================
 */
function buildGraph(keywords) {
  const nodes = keywords.map(k => ({
    keyword: k,
    intent: getIntent(k),
    url: `${CONFIG.domain}${slugify(k)}.html`
  }));

  return nodes.map(node => {
    const links = nodes
      .filter(n => n.keyword !== node.keyword)
      .slice(0, 3)
      .map(n => ({ keyword: n.keyword, url: n.url }));

    return { ...node, links };
  });
}

/**
 * =========================
 * WRITE PAGES
 * =========================
 */
function writePages(graph) {
  if (!fs.existsSync(CONFIG.outputDir)) {
    fs.mkdirSync(CONFIG.outputDir, { recursive: true });
  }

  graph.forEach(node => {
    const html = generatePage(node);
    const filePath = path.join(CONFIG.outputDir, `${slugify(node.keyword)}.html`);
    fs.writeFileSync(filePath, html);
  });
}

/**
 * =========================
 * SITEMAP GENERATOR
 * =========================
 */
function generateSitemap(graph) {
  const urls = graph.map(n => `
  <url>
    <loc>${n.url}</loc>
  </url>`).join("");

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls}
</urlset>`;

  fs.writeFileSync(CONFIG.sitemapPath, xml);
}

/**
 * =========================
 * RUNNER
 * =========================
 */
function run() {
  const keywords = loadKeywords();
  const graph = buildGraph(keywords);

  writePages(graph);
  generateSitemap(graph);

  console.log("SEO GRAPH BUILD COMPLETE ✔");
  console.log(`Pages generated: ${graph.length}`);
}

run();
