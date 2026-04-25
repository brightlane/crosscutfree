const graph = require("./seo-graph-engine.json");
const fs = require("fs");

let urls = graph.nodes.map(n => `
<url>
  <loc>https://yourdomain.com${n.url}.html</loc>
  <changefreq>weekly</changefreq>
</url>
`).join("\n");

const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls}
</urlset>`;

fs.writeFileSync("./dist/sitemap.xml", sitemap);
console.log("Sitemap generated");
