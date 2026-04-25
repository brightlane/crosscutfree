const fs = require("fs");
const path = require("path");

const graph = require("./seo-graph-engine.json");

const OUTPUT_DIR = "./dist";

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function buildMeta(node) {
  return `
<title>${node.title}</title>
<meta name="description" content="${node.primary_keyword} - complete guide with comparisons, tools, and strategies." />
<meta name="keywords" content="${[
    node.primary_keyword,
    ...(node.secondary_keywords || [])
  ].join(", ")}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="https://yourdomain.com${node.url}" />
`;
}

function buildInternalLinks(node) {
  return (node.internal_links || [])
    .map(id => {
      const target = graph.nodes.find(n => n.id === id);
      if (!target) return "";
      return `<a href="${target.url}">${target.title}</a>`;
    })
    .join("\n");
}

function buildAffiliateBlock(node) {
  if (!node.affiliate_enabled) return "";

  return `
<div class="affiliate-box">
  <a href="https://try.sanebox.com/efdrajzfvk2c?utm_source=seo_graph" rel="sponsored nofollow">
    Try Email Productivity Tool (Official Offer)
  </a>
</div>
`;
}

function renderPage(node) {
  return `
<!DOCTYPE html>
<html lang="en">
<head>
${buildMeta(node)}
<style>
body { font-family: Arial; max-width: 900px; margin: auto; padding: 20px; }
.affiliate-box { background: #f0fff4; padding: 15px; margin: 20px 0; border-left: 4px solid green; }
nav a { display:block; margin:5px 0; }
</style>
</head>

<body>

<h1>${node.title}</h1>

<p>
This page targets <strong>${node.primary_keyword}</strong> and related search intent clusters
to help users understand tools, workflows, and productivity systems.
</p>

${buildAffiliateBlock(node)}

<h2>Internal Resources</h2>
<nav>
${buildInternalLinks(node)}
</nav>

<h2>Key Insights</h2>
<ul>
  ${(node.secondary_keywords || []).map(k => `<li>${k}</li>`).join("\n")}
</ul>

</body>
</html>
`;
}

function build() {
  ensureDir(OUTPUT_DIR);

  graph.nodes.forEach(node => {
    const html = renderPage(node);
    const filePath = path.join(OUTPUT_DIR, node.url);

    ensureDir(path.dirname(filePath));
    fs.writeFileSync(filePath + ".html", html);

    console.log("Generated:", filePath + ".html");
  });
}

build();
