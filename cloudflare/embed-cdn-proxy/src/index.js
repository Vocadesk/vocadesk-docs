export default {
  async fetch(request) {
    const url = new URL(request.url);
    url.protocol = "https:";
    url.hostname = "cdn.vocadesk.com";

    const originRequest = new Request(url, request);
    originRequest.headers.set("Host", "cdn.vocadesk.com");

    // cacheTtl: 0 - never let Cloudflare's edge cache a response from here.
    // GitHub Pages has its own propagation delay after a release publishes;
    // without this, a 404 hit during that window gets cached for hours,
    // blocking every customer loading a brand-new versioned bundle.
    return fetch(originRequest, { cf: { cacheTtl: 0, cacheEverything: false } });
  },
};
