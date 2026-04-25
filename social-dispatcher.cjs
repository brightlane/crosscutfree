// =====================================
// social-dispatcher.cjs
// Lightweight social posting layer
// =====================================

require("dotenv").config();

// ===============================
// CORE SOCIAL FUNCTION
// ===============================
function postToSocial(title, url) {
  console.log("\n📣 SOCIAL DISPATCH START");
  console.log("Title:", title);
  console.log("URL:", url);

  // route to all platforms safely
  postToTwitter(title, url);
  postToReddit(title, url);
  postToFacebook(title, url);

  console.log("📣 SOCIAL DISPATCH COMPLETE\n");
}

// ===============================
// TWITTER / X (placeholder-safe)
// ===============================
function postToTwitter(title, url) {
  if (!process.env.TWITTER_API_KEY) {
    console.log("[Twitter] Skipped (no API key)");
    return;
  }

  console.log("[Twitter] Would post:");
  console.log(`${title} - ${url}`);

  // Future real API call:
  // fetch("https://api.twitter.com/2/tweets", ...)
}

// ===============================
// REDDIT (placeholder-safe)
// ===============================
function postToReddit(title, url) {
  if (!process.env.REDDIT_TOKEN) {
    console.log("[Reddit] Skipped (no API key)");
    return;
  }

  console.log("[Reddit] Would submit post:");
  console.log({ title, url });

  // Future real API call:
  // POST to Reddit API /submit
}

// ===============================
// FACEBOOK GRAPH API
// ===============================
function postToFacebook(title, url) {
  if (!process.env.FB_ACCESS_TOKEN) {
    console.log("[Facebook] Skipped (no API key)");
    return;
  }

  console.log("[Facebook] Would publish:");
  console.log(`${title} - ${url}`);

  // Future real API call:
  // https://graph.facebook.com/me/feed
}

// ===============================
// EXPORT
// ===============================
module.exports = {
  postToSocial
};
