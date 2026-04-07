/* ============================================================
   KhaiDee Service Worker  —  sw.js
   Strategy:
     • Shell (HTML/CSS/JS/Icons) → Cache-First
     • API / Supabase calls      → Network-First (ไม่ cache)
     • Images                    → Stale-While-Revalidate
   ============================================================ */

const APP_VERSION   = '2.13.0';
const CACHE_SHELL   = `khaidee-shell-v${APP_VERSION}`;
const CACHE_IMAGES  = `khaidee-images-v${APP_VERSION}`;
const CACHE_FONTS   = `khaidee-fonts-v${APP_VERSION}`;

/* ── ไฟล์ที่ต้อง cache ตั้งแต่ install ── */
const SHELL_FILES = [
  '/khaidee1/',
  '/khaidee1/index.html',
  '/khaidee1/manifest.json',
  '/khaidee1/icon.png',
  '/khaidee1/icons/icon-192x192.png',
  '/khaidee1/icons/icon-512x512.png',
  '/khaidee1/offline.html'   /* หน้า fallback เมื่อ offline */
];

/* ── ไม่ cache URL เหล่านี้เลย ── */
const BYPASS_PATTERNS = [
  /supabase\.co/,           /* Supabase API */
  /googleapis\.com\/v/,     /* Google API */
  /chrome-extension:\/\//,
  /\?v=nocache/
];

/* ================================================================
   1. INSTALL — pre-cache shell files
   ================================================================ */
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_SHELL)
      .then(cache => cache.addAll(SHELL_FILES))
      .then(() => self.skipWaiting())
      .catch(err => console.warn('[SW] Install cache error:', err))
  );
});

/* ================================================================
   2. ACTIVATE — ลบ cache เก่าทิ้ง
   ================================================================ */
self.addEventListener('activate', event => {
  const VALID = [CACHE_SHELL, CACHE_IMAGES, CACHE_FONTS];
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys
          .filter(k => !VALID.includes(k))
          .map(k => {
            console.log('[SW] Deleting old cache:', k);
            return caches.delete(k);
          })
      ))
      .then(() => self.clients.claim())
  );
});

/* ================================================================
   3. FETCH — routing logic
   ================================================================ */
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  /* ── ข้าม non-GET และ URL ที่ bypass ── */
  if (request.method !== 'GET') return;
  if (BYPASS_PATTERNS.some(p => p.test(request.url))) return;

  /* ── Google Fonts → Cache-First ── */
  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    event.respondWith(cacheFirst(request, CACHE_FONTS));
    return;
  }

  /* ── Images → Stale-While-Revalidate ── */
  if (/\.(png|jpe?g|gif|webp|svg|ico)$/i.test(url.pathname)) {
    event.respondWith(staleWhileRevalidate(request, CACHE_IMAGES));
    return;
  }

  /* ── Navigation (HTML page requests) → Network-First → Cache → offline.html ── */
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          // อัปเดต cache เสมอเมื่อมีอินเทอร์เน็ต
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_SHELL).then(c => c.put(request, clone));
          }
          return response;
        })
        .catch(async () => {
          // offline → ลอง cache ก่อน
          const cached =
            await caches.match(request) ||
            await caches.match('/khaidee1/') ||
            await caches.match('/khaidee1/index.html');
          // มี cache → เปิด app ได้เลย ไม่ต้องไป offline.html
          if (cached) return cached;
          // ไม่มีเลย → offline.html
          return caches.match('/khaidee1/offline.html');
        })
    );
    return;
  }

  /* ── Shell files (JS / CSS / icons) → Cache-First → fallback offline ── */
  if (
    url.pathname.startsWith('/khaidee1/') &&
    (url.hostname === self.location.hostname || url.hostname === 'tavanh903-byte.github.io')
  ) {
    event.respondWith(
      cacheFirst(request, CACHE_SHELL)
        .catch(() => caches.match('/khaidee1/offline.html'))
    );
    return;
  }

  /* ── อื่นๆ → Network → silent fail ── */
  event.respondWith(fetch(request).catch(() => new Response('', { status: 503 })));
});

/* ================================================================
   Helpers
   ================================================================ */

/** Cache-First: ดึงจาก cache ก่อน ถ้าไม่มีค่อย fetch แล้ว cache */
async function cacheFirst(request, cacheName) {
  const cached = await caches.match(request);
  if (cached) return cached;
  const response = await fetch(request);
  if (response.ok) {
    const cache = await caches.open(cacheName);
    cache.put(request, response.clone());
  }
  return response;
}

/** Stale-While-Revalidate: ส่ง cache ทันที แล้ว update ใน background */
async function staleWhileRevalidate(request, cacheName) {
  const cache  = await caches.open(cacheName);
  const cached = await cache.match(request);

  const fetchPromise = fetch(request).then(response => {
    if (response.ok) cache.put(request, response.clone());
    return response;
  }).catch(() => null);

  return cached || fetchPromise;
}

/* ================================================================
   4. MESSAGE — รับคำสั่งจาก client (เช่น force update)
   ================================================================ */
self.addEventListener('message', event => {
  if (event.data?.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  if (event.data?.type === 'CLEAR_CACHE') {
    caches.keys().then(keys => Promise.all(keys.map(k => caches.delete(k))));
  }
});
