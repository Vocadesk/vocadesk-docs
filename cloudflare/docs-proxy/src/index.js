export default {
  async fetch(request) {
    const url = new URL(request.url);
    url.protocol = "https:";
    url.hostname = "docs.vocadesk.com";

    const originRequest = new Request(url, request);
    originRequest.headers.set("Host", "docs.vocadesk.com");

    return fetch(originRequest);
  },
};
