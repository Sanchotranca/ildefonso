// Service Worker — Residencia San Ildefonso
// Estrategia: HTML network-first (fallback offline.html), estáticos cache-first con revalidación.
// §26 ELIAWEB v4.

const CACHE_NAME = 'rsi-v2';
const STATIC_ASSETS = [
  '/',
  '/css/style.min.css',
  '/js/main.min.js',
  '/offline.html',
  '/img/favicon.ico',
  '/img/favicon-32.png',
  '/img/apple-touch-icon.png',
  '/img/icon-192.png',
  '/img/icon-512.png',
  '/img/logo-san-ildefonso.webp',
  '/img/fachada-rectorado.webp',
  '/manifest.json'
];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(STATIC_ASSETS).catch(function () { /* tolerante a fallos */ });
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE_NAME; })
                            .map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (event) {
  var req = event.request;

  // Solo GET propios — no interceptar POST (formularios), ni cross-origin (fuentes Google, mapas).
  if (req.method !== 'GET') return;
  if (new URL(req.url).origin !== self.location.origin) return;

  // HTML: network-first, fallback a offline.html
  if (req.destination === 'document') {
    event.respondWith(
      fetch(req).catch(function () { return caches.match('/offline.html'); })
    );
    return;
  }

  // Estáticos: cache-first, revalida en background (stale-while-revalidate)
  event.respondWith(
    caches.match(req).then(function (cached) {
      var fetchPromise = fetch(req).then(function (res) {
        if (res && res.status === 200) {
          var copy = res.clone();
          caches.open(CACHE_NAME).then(function (c) { c.put(req, copy); });
        }
        return res;
      }).catch(function () { return cached; });
      return cached || fetchPromise;
    })
  );
});
