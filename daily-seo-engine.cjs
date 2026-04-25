const fs = require("fs");
const path = require("path");

// ===============================
// CONFIG
// ===============================
const AFFILIATE_URL = "https://try.sanebox.com/efdrajzfvk2c?utm_source=deploy";
const OUTPUT_DIR = path.join(__dirname, "dist");

// words target (YOU CONTROL THIS)
const WORD_COUNT = 20000; // you asked for extreme scale

// ===============================
// SEO KEYWORDS (EXPANDED CLUSTER)
// ===============================
const keywords = [
  "email productivity system",
  "inbox zero workflow",
  "AI email filtering system",
  "email automation tools",
  "best email management software",
  "productivity for agencies",
  "freelancer inbox optimization",
  "email overload solution",
  "work efficiency tools 2026",
  "AI inbox assistant"
];

// ===============================
// CONTENT GENERATOR
// ===============================
function generateParagraph(keyword) {
  return `
<p>
In modern workflows, ${keyword} has become essential for professionals managing high-volume communication.
Tools like intelligent email sorting systems reduce cognitive load, improve response time, and streamline business operations.
Many agencies now rely on automation layers that categorize messages, prioritize urgency, and eliminate inbox clutter while preserving privacy.
</p>

<p>
A major advantage of advanced email management platforms is their ability to reduce manual filtering by up to 50%,
allowing users to focus on revenue-generating tasks instead of inbox maintenance.
This shift directly impacts productivity metrics across freelance, agency, and enterprise environments.
</p>

<p>
The integration of AI-based sorting systems enables smart categorization such as newsletters, client communication, and low-priority notifications.
This ensures critical messages are never missed while maintaining a clean and actionable inbox structure.
</p>

<p>
<a href="${AFFILIATE_URL}" rel="sponsored">Try the recommended email optimization tool here</a>
</p>
`;
}

// ===============================
// BUILD BLOG CONTENT
// ===============================
function buildBlog() {
  let content = "";

  for (let i = 0; i < 200; i++) {
    const kw = keywords[i % keywords.length];
    content += generateParagraph(kw);
  }

  return content;
}

// ===============================
// HTML WRAPPER
// ===============================
function buildHTML(content) {
  return `
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Email Productivity & Inbox Optimization Guide 2026</title>
<meta name="description" content="Ultimate guide to email productivity, inbox zero systems, and AI-powered email management tools for modern professionals.">
<meta name="keywords" content="${keywords.join(", ")}">

<meta property="og:title" content="Email Productivity Guide 2026">
<meta property="og:description" content="AI inbox systems, productivity workflows, and automation strategies.">

<style>
body { font-family: Arial; max-width: 900px; margin: auto; line-height: 1.7; padding: 20px; }
a { color: #1a73e8; font-weight: bold; }
</style>
</head>

<body>

<h1>Email Productivity Master Guide 2026</h1>

<p>
This guide explores advanced systems for managing digital communication efficiently using AI-assisted tools and automation workflows.
</p>

${content}

<footer>
<p>Affiliate disclosure: links may earn commissions.</p>
</footer>

</body>
</html>
`;
}

// ===============================
// WRITE FILE
// ===============================
function writeBlog() {
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR);
  }

  const content = buildBlog();
  const html = buildHTML(content);

  const filePath = path.join(OUTPUT_DIR, `blog-${Date.now()}.html`);
  fs.writeFileSync(filePath, html);

  console.log("Blog generated:", filePath);
}

// run
writeBlog();
