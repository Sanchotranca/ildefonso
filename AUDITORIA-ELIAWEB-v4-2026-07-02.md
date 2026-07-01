# AUDITORÍA COMPLETA — ELIAWEB_STANDARDS_v4 + RESTRICTIONS
**Sitio:** https://www.residenciasanildefonso.es · **Fecha:** 2026-07-02 (noche)
**Método:** descarga FTP completa del servidor (56 archivos) + verificación en vivo. Cada § del estándar revisado.
**Estados:** ✅ CUMPLE · ❌ VIOLA · ⚠️ DESVIACIÓN CONSCIENTE · ➖ NO APLICA · ❓ NO VERIFICABLE desde aquí

---

## §0–§1 Stack y principios
✅ Estático HTML+CSS+JS vanilla + PHP solo para el formulario. Sin frameworks. Ockham aplicado (hero degradado CSS, fuentes de sistema).

## §2 HTML
- ✅ lang, charset 1er hijo, titles únicos, semántico, h1 único, alt+width+height en 30/30 imgs, labels con for/id, skip-link, ids únicos, sin tags obsoletos, sin XHTML, sin onclick/style inline (offline.html corregido hoy), tablas con caption/thead/scope, fieldset donde toca.
- ❌ **index.html: la section aria-label="Resumen" (intro post-hero) no tiene encabezado hijo.** Fix pendiente de decisión.
- ⚠️ 404.html y gracias.html: salto h1→h3 (los h3 del footer, sin h2 en el cuerpo). Patrón común en las 11 páginas; en el resto no hay salto porque el cuerpo tiene h2. Opciones: dejar (impacto casi nulo) o h2 oculto.
- ❓ Validación W3C formal (validator.w3.org): hacer manual.

## §3 CSS
✅ Reset, cascade layers en orden exacto, variables :root para todo, CERO hex fuera de :root (verificado), dark mode completo, escala clamp(), BEM, z-index con variables, svh con fallback, !important solo en reduced-motion, sin #id, sin @import, media queries en em, body font-size 100%, animaciones solo transform/opacity, line-height sin unidades, 2 familias (sistema + Georgia).

## §4 JS
✅ main.js: sin var/eval/==/console.log/document.write, defer, listeners limpios, sin scroll/resize (debounce N/A). Minificado (terser).

## §5 PHP
- ✅ enviar.php: limpieza CR/LF + htmlspecialchars, CSRF verificado, honeypot, PHP 8.2.
- ❓ display_errors=Off: configurado vía cPanel (no verificable por archivo). **Moody: confirmar en cPanel → MultiPHP INI Editor.**

## §6 HEAD
✅ Completo en las 11 páginas indexables: OG completo (type/title/desc/url/image+width/height/locale), twitter:card, favicons (ico multi + 32 + 16 + apple-touch 180×180), manifest, theme-color, canonical. offline.html exenta (fallback SW, noindex).
- ⚠️ **favicon-16.png es un cuadrado azul liso** (#003DA5), no el escudo. Menor (los navegadores usan .ico/32px). Fix trivial disponible.

## §7 Schema.org
✅ JSON-LD válido (parseado OK) en todas: LodgingBusiness + BreadcrumbList + FAQPage (contacto) + Article (residencia). Sin datos inventados (numberOfRooms y precios purgados 7-01). ❓ Rich Results Test formal: manual.

## §8 Imágenes
- ✅ WebP en todo, width/height 30/30, lazy en no-LCP, hero móvil sin imagen (degradado), OG 1200×630 exactos en WebP.
- ⚠️ **Sin srcset/sizes (0/30).** Desviación consciente: imágenes ya comprimidas (-90%) y PageSpeed móvil 100/100. Añadirlo = complejidad sin ganancia medible (Ockham). Decisión: no tocar salvo orden contraria.
- ⚠️ 4 imágenes de contenido superan el objetivo 40KB (fachada-rectorado 141KB, arco-patio 106KB, 2 patios ~75KB): solo cargan en desktop (strips del hero) o lazy. PageSpeed no penalizó.
- ⚠️ **og-image.jpg (fallback §17) NO existe en el servidor** — solo el .webp. Algunas redes (FB antiguo) no leen WebP. Fix opcional disponible.
- ➖ Vídeo: no hay.

## §9 Rendimiento
- ✅ PageSpeed móvil 100/100/100/100 (verificado 2026-06-30, sin cambios de peso desde entonces). CSS minificado inline, JS defer minificado, 0 terceros en load (mapa = fachada click-to-load), TTFB correcto, HTTP/2, brotli/gzip activos (verificado en vivo), Cache-Control 1 año en estáticos (verificado), preloads 0 (≤4 ✓).
- ⚠️ §9A pide critical-CSS + carga diferida; el sitio inlinea TODO el CSS por página. Desviación deliberada (mató el CLS 0,386→0). Resultado avala.
- ⚠️ Cache-Control sin "immutable" (pide max-age+immutable). Cosmético.

## §10 Seguridad
✅ En vivo verificado: HSTS, X-Frame SAMEORIGIN, nosniff, Referrer-Policy, Permissions-Policy, CSP estricta (script-src 'self'), .git→404, .env/.bak/.cursorrules→403, Options -Indexes, sin credenciales en el repo, formulario con CSRF+captcha+honeypot, header-injection resuelto.
- ⚠️ CSP lleva style-src 'unsafe-inline': imprescindible con la estrategia de CSS inline que dio el 100. Excepción documentada.
- ⚠️ HSTS sin flag "preload" (el estándar lo incluye). Añadirlo = compromiso hstspreload.org. Opcional.

## §11 Accesibilidad
✅ Skip-link, focus-visible, reduced-motion, labels, h1 único, touch ≥44px, teclado (nav con aria-expanded + Esc). Contraste: 25/25 AA (auditado 7-01; paleta sin cambios desde entonces).

## §12 UX
✅ CTAs verbo+objeto, "Enviar consulta", validación blur + errores específicos + spinner + Cancelar, aria-current, nav ≤7, sin dark patterns, banner cookies con Aceptar/Rechazar misma jerarquía + revocación en footer (11 págs).
❓ Prueba física en móvil/dedo: pendiente de Moody.

## §13 SEO
- ✅ Titles ≤60 únicos, canonicals autoreferentes, robots.txt correcto (no bloquea CSS/JS, permite bots IA), sitemap SOLO indexables (6 URLs con lastmod real), noindex en gracias/404/offline/habitaciones/servicios, NAP idéntico en los 11 footers + JSON-LD, sin keyword stuffing, anclas descriptivas.
- ⚠️ Descriptions cortas en aviso-legal (102ch), politica-cookies (91ch), politica-privacidad (112ch) — indexables; el estándar pide 150-160. Editorial, fix fácil.
- ✅ contacto.html duplica title/desc de contacto.php PERO canonical + 301 lo resuelven (patrón correcto).
- ❓ Search Console: estado desconocido — **Moody: confirmar propiedad verificada y sitemap enviado.**

## §14 GEO
✅ llms.txt en vivo (200, formato agéntico, sin datos falsos), time datetime="2026-06" en footers, FAQPage schema, intro respuesta-directa post-hero en index, robots.txt permite crawlers IA, contenido en HTML estático.

## §15 Formularios
✅ Propio (enviar.php) en vez de Web3Forms: desviación aprobada (mejor: sin clave de terceros). Honeypot, CSRF, RGPD checkbox, autocomplete, captcha matemático, botón descriptivo, 16px, targets 44px.
⚠️ Destino provisional pastorsanchez25@gmail.com — pendiente prueba de Moody y revertir a sanildefonso@crusa.es (repo ya lo tiene).

## §16 Cookies/RGPD
✅ Banner primera visita, Aceptar/Rechazar misma jerarquía, persistencia localStorage, link a política, revocación en footer. GA4 NO instalado → nada dispara. ➖ Consent Mode: aplicar cuando se instale GA4 (pendiente conocido).

## §17 Estructura
✅ Todo presente: index, 404, legales, gracias, robots, sitemap, llms.txt, .htaccess, css/, js/, img/ con favicons y og-image.webp. ⚠️ Falta og-image.jpg (fallback). ➖ fonts/ (no hay webfonts). ⚠️ En el servidor sobran: 3 imgs ex-galería huérfanas + .htaccess.bak + .htaccess.swap.2022 + IMG-20180619-WA0022.jpg (también en repo).

## §18 .htaccess
- ✅ HTTPS forzado (X-Forwarded-Proto, LiteSpeed-safe), www forzado, 404 custom, caché larga, gzip/brotli, cabeceras completas, bloqueo de sensibles, -Indexes.
- ❌ **Los 301 internos emiten http:// (downgrade):** contacto.html→http://…/contacto.php→https (cadena con salto inseguro) y habitaciones.html igual. Causa: destino relativo tras el proxy. **Fix preparado (destinos absolutos https).**
- ❌ **Cadenas en canonicalización:** http://sin-www → https://sin-www → https://www (2 saltos; §29B pide 1). **Fix preparado (regla combinada).**

## §19–§21 Checklists deploy
✅ Cumplidos en lo automatizable (verificado hoy en vivo: puntos 1-13 del post-deploy). ❓ Manuales pendientes: formulario end-to-end (Moody), securityheaders.com/ssllabs formales (previo: A), Search Console.

## §22–§23 Git
- ✅ Repo GitHub, master = producción byte a byte (verificado hoy), .gitignore correcto.
- ⚠️ Sin ramas develop/feature ni PRs: los cambios van directos a master. Para un mantenedor único con deploy por FTP es defendible (Ockham), pero incumple §23A literal. Decisión de Moody si algún día colabora más gente.
- ⚠️ Commits de hoy siguen Conventional Commits aproximado (sin tipo estricto). Menor.

## §24 Testing
❓ Pendientes manuales de Moody: flujo en iPhone/Android físico, teclado completo, JS off, Slow 4G. Automatizado: Lighthouse CI no configurado (opcional).

## §25 Analytics
➖ GA4 y Search Console: NO instalados/desconocido. Pendiente conocido (con Consent Mode v2 cuando toque).

## §26 PWA
✅ manifest completo (name, short_name, icons 192+512+maskable, lang, theme), SW network-first + SWR con offline.html (cache v3 hoy), registro en main.js, assets precacheados todos existentes (verificado).

## §27 Monitorización/Backups
- ✅ Backup código = GitHub sincronizado.
- ❓ **Uptime monitoring: desconocido.** Recomendado UptimeRobot gratuito. **Moody decide.**
- ➖ BD: no hay.

## §28 Legal
✅ Aviso legal con CRUSA CIF A-80991714 + registro + contacto; privacidad RGPD con derechos y AEPD; cookies con categorías y revocación. Web3Forms falso eliminado (7-01). ➖ YMYL: no aplica.

## §29 Redirects
❌ Ver §18: cadenas + downgrade http en 301 internos. Fix preparado. ✅ 301 (no 302) en todo. ✅ habitaciones.html→home con 301.

## §30 Móvil
✅ Viewport sin user-scalable=no, sin anchos fijos, svh, touch-action manipulation, :active feedback, 16px en inputs, safe-area-inset, hamburguesa aria-expanded + Esc + bloqueo scroll body, select nativo, hero móvil = degradado (LCP sin imagen).
⚠️ srcset ausente (ver §8). ❓ Prueba física pendiente.

---

## RESUMEN EJECUTIVO
**Violaciones reales encontradas: 3** → (1) redirects .htaccess con downgrade http + cadenas [fix listo], (2) section "Resumen" sin heading en index [decisión], (3) offline.html onclick+style inline [**YA CORREGIDO hoy**].
**Desviaciones conscientes defendibles: 6** → CSS 100% inline (dio el 100), sin srcset (PageSpeed 100), style-src unsafe-inline (consecuencia del inline), formulario propio vs Web3Forms, sin ramas develop/PR, h3 de footer en 404/gracias.
**Menores/opcionales: 5** → favicon-16 liso, og-image.jpg ausente, descriptions cortas en 3 legales, HSTS sin preload, Cache-Control sin immutable.
**No verificable desde aquí (pendiente Moody): 6** → display_errors en cPanel, prueba formulario, Search Console, uptime monitoring, prueba en dispositivo físico, W3C/Rich Results formales.
