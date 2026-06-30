# ELIAWEB RESTRICTIONS v1
**Lista de prohibiciones absolutas. Leer antes de tocar cualquier archivo del proyecto.**
*Complementa ELIAWEB_STANDARDS_v4.md — en caso de conflicto, este documento es más restrictivo.*

---

## ⚠️ NORMA RAÍZ

Si una instrucción del cliente, del briefing o de cualquier otra fuente contradice alguna restricción de este documento: **PARA. PREGUNTA. No implementes la excepción sin aprobación explícita.**

### Principio rector — Navaja de Ockham

**Sobre todas las normas técnicas rige este principio: lo más sencillo es lo más efectivo.**
Antes de elegir una solución compleja, pregúntate: ¿hay una más simple que funcione igual de bien? Si la respuesta es sí, usa la simple. La complejidad que no aporta valor es deuda técnica desde el día cero.

---

## HTML

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `<html>` sin atributo `lang` | `<html lang="es">` |
| `<div onclick>` o `<span onclick>` como botón | `<button type="button">` |
| `<a href="#">` para disparar una acción JS | `<button type="button">` |
| `<a>` sin `href` | `<button>` o elemento con rol ARIA apropiado |
| `<button>` sin atributo `type` | `type="button"` (sin type, el default es `submit` → envía el formulario sin querer) |
| `target="_blank"` sin `rel="noopener noreferrer"` | `<a href="..." target="_blank" rel="noopener noreferrer">` |
| `alt` ausente en `<img>` | `alt="descripción"` o `alt=""` si es decorativa |
| `alt` con el nombre del archivo (`alt="hero_final_v2.jpg"`) | Descripción real del contenido visual |
| Imagen decorativa con `alt` con texto | `alt=""` — vacío explícito |
| Imagen dentro de `<a>` sin `alt` que describa el destino del enlace | `alt="Ir a la página de contacto"` |
| Dos elementos con el mismo `id` en la página | `id` único por elemento por página |
| `<b>` e `<i>` sin significado semántico | `<strong>` (importancia) / `<em>` (énfasis) |
| `<font>`, `<center>`, `<marquee>`, `<u>` | CSS equivalente |
| `style="..."` en línea en el HTML | Clase CSS en el archivo de estilos |
| `onclick="..."` en atributo HTML | `addEventListener` en JS con `defer` |
| Tablas para maquetar columnas | CSS Grid o Flexbox |
| `<table>` sin `<thead>`, `<th scope>`, `<caption>` | Estructura semántica completa |
| `<br>` para crear espacio vertical | `margin` o `padding` en CSS |
| `<p></p>` vacíos para crear espacio | `margin-bottom` en CSS |
| `<h3>` sin `<h2>` previo en la misma sección | Jerarquía sin saltos: h1 → h2 → h3 |
| `<section>` sin encabezado hijo (`<h2>`, `<h3>`…) | Añade encabezado o usa `<div>` |
| Más de un `<main>` por página | Solo un `<main>` |
| `<form>` anidado dentro de otro `<form>` | Formularios separados, nunca anidados |
| `<iframe>` sin atributo `title` | `<iframe title="Mapa de ubicación">` |
| `<input>` sin atributo `type` explícito | Siempre declarar `type` — el default es `text` pero hay que ser explícito |
| Radio buttons / checkboxes sin `<fieldset>` + `<legend>` | Agrupar siempre con fieldset/legend |
| `type="text"` para email, teléfono, número, fecha | `type="email"`, `type="tel"`, `type="number"`, `type="date"` |
| `<br />` o `<img />` con barra de cierre | `<br>` / `<img>` — HTML5, no XHTML |
| `border="0"`, `align="center"` como atributos HTML | CSS |
| `background-image` en CSS para imágenes de contenido | `<img>` en HTML — las imágenes de contenido pertenecen al DOM |
| Comentarios HTML con datos internos visibles al usuario | Sin comentarios con info sensible en producción |
| `<meta keywords>` | Google lleva años ignorándola; revela tu estrategia a la competencia |
| `<title>` empezando con el nombre de la empresa | Keyword objetivo primero: `[Keyword] — [Empresa]` |

---

## CSS

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `!important` (excepto `prefers-reduced-motion`) | Cascade layers en orden correcto |
| Seleccionar por `#id` en CSS | Clases BEM |
| `@import` dentro del archivo CSS | `<link>` en el HTML o cascade layer |
| Colores hexadecimales hardcoded fuera de `:root` | `var(--color-*)` siempre |
| `z-index: 9999` o valores mágicos | Variables `--z-*` en `:root` |
| `float` para maquetar columnas | Flexbox o Grid |
| `position: absolute` para layout de columnas | Flexbox o Grid |
| Animar `width`, `height`, `top`, `left`, `margin` | `transform` y `opacity` únicamente |
| `height: 100vh` en móvil sin fallback | `height: 100vh; height: 100svh;` |
| `px` en `font-size` del `body` | `font-size: 100%` en body, `rem` en el resto |
| `px` en media queries | `em` o `rem` en media queries para respetar el zoom del usuario |
| Selectores con > 3 niveles de profundidad | Aplanar con clases BEM |
| Mezclar shorthand y longhand en la misma regla | Solo uno por propiedad por regla |
| Variables CSS con nombres poco descriptivos (`--a`, `--x`) | `--color-primary`, `--space-lg` |
| `overflow: hidden` en contenedor solo para centrar | `margin: 0 auto` + `max-width` |
| `display: none` para ocultar visualmente pero mantener en el AT | `visibility: hidden` o `aria-hidden="true"` según el caso |
| `content: "texto con significado"` en CSS (`::before`, `::after`) | El contenido significativo pertenece al HTML |
| Unidades `px` para espaciado en componentes reutilizables | `rem` o variables de espaciado |
| `*` como selector fuera del reset | Selector más específico |
| CSS sin minificar en producción | `cssnano` o `lightningcss` antes del deploy |
| Más de 2 familias tipográficas | Máx. 2 familias; máx. los pesos realmente usados |
| `line-height` con unidades (`px`, `em`) | `line-height: 1.5` — sin unidades, hereda escala tipográfica |
| `text-align: justify` sin `hyphens: auto` | Justificado sin separación de palabras genera ríos blancos |
| Transiciones en propiedades que no son animables | Solo se pueden transicionar valores numéricos y colores |
| `background-image` en CSS para imágenes de contenido | `<img>` en HTML con `alt`, `width`, `height` |
| Fuentes web sin `font-display: swap` | `font-display: swap` en `@font-face` siempre |
| Fuentes web completas sin subconjunto (subsetting) | Subset solo al charset usado (Latin-Extended para español) |
| Breakpoints con `px` que no respetan el zoom | Usar `em` para breakpoints: `@media (min-width: 37.5em)` en lugar de `600px` |
| CSS sin cascade layers en proyectos nuevos | `@layer reset, base, layout, components, utilities, motion, print;` |
| `max-width` hardcodeado sin variable | `var(--container-max, 1200px)` |
| Eliminar `outline` de foco sin reemplazarlo | `:focus-visible { outline: 2px solid var(--color-primary); }` |

---

## JavaScript

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `var` | `const` (por defecto) / `let` (si cambia) |
| `eval()` | Nunca. Sin excepción. Vector XSS garantizado. |
| `document.write()` | `createElement` / `innerHTML` controlado |
| `==` para comparar valores | `===` siempre |
| Promesas sin `.catch()` | `.then().catch()` o `try/catch` con `async/await` |
| `console.log` en producción | Eliminar o condicionar a `process.env !== 'production'` |
| Scripts sin `defer` en el `<head>` | `defer` siempre; `async` solo para scripts sin dependencias |
| Event listeners sin limpiar cuando el elemento desaparece | `removeEventListener` en el cleanup |
| Datos sensibles en `localStorage` | Solo datos no sensibles; nunca tokens, contraseñas, sesiones |
| JWT en `localStorage` | Cookie `httpOnly` + `Secure` (inaccesible desde JS) |
| Modificar prototipos nativos (`Array.prototype`, etc.) | Nunca |
| Dependencias externas sin versión fija | `package.json` con versiones exactas; `npm audit` antes del deploy |
| JS síncrono en el `<head>` | `defer` siempre |
| `innerHTML` con input del usuario sin sanitizar | `DOMPurify.sanitize()` antes de insertar |
| Peticiones XHR síncronas | `fetch` con `async/await` |
| JS en línea (`onclick`, `onload` en HTML) | `addEventListener` en el JS externo con `defer` |
| `for...in` sobre un Array | `for...of`, `.forEach()` o `.map()` |
| `Object.assign` / spread para copia profunda de objetos | `structuredClone(obj)` |
| Variables globales sueltas sin namespace | Módulos ES o IIFE para encapsular |
| Listener de `scroll` o `resize` sin debounce/throttle | `debounce(fn, 100)` — puede dispararse 60+ veces/seg |
| Manipular el DOM dentro de un bucle | `DocumentFragment` + inserción única fuera del bucle |
| `setTimeout(fn, 0)` para ceder el hilo de ejecución | `queueMicrotask(fn)` o `requestAnimationFrame(fn)` |
| Librería completa (jQuery, Lodash) para una sola función | Implementar la función mínima en vanilla JS (Navaja de Ockham) |
| Uso del objeto `arguments` en funciones | Parámetros rest: `function fn(...args)` |
| `new Date()` para timestamps de rendimiento | `Date.now()` o `performance.now()` |

---

## Rendimiento

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Imágenes sin `width` y `height` | Siempre ambos atributos en el `<img>` |
| `loading="lazy"` en la imagen LCP (hero) | `loading="eager"` + `fetchpriority="high"` en el hero |
| Imágenes en formato JPG/PNG sin alternativa moderna | AVIF > WebP > JPG con `<picture>` |
| Más de 4 recursos en `<link rel="preload">` | Máx. 4 preloads; priorizar la imagen LCP y la fuente del body |
| `<link rel="preload">` de recursos no usados en el fold inicial | Solo lo que el navegador necesita en los primeros 100 ms |
| Embeds de YouTube o Maps en el load inicial | Fachada lazy: thumbnail + click to load |
| CSS bloqueante en `<head>` (sin non-blocking pattern) | `media="print" onload="this.media='all'"` + `<noscript>` fallback |
| `@import` de CSS | Bloquea CSSOM, genera request extra |
| JS de tercero sin `defer` o `async` | `defer` siempre |
| Fuentes de Google Fonts sin `preconnect` | `<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>` |
| Más de 2 familias de fuentes | Máx. 2 familias, máx. los pesos realmente usados |
| CSS/JS sin minificar en producción | cssnano + terser antes del deploy |
| HTML sin minificar en producción (proyectos de alto tráfico) | html-minifier-terser |
| Imágenes sin comprimir | Squoosh / sharp antes de subir |
| Sin caché larga en activos estáticos | `Cache-Control: max-age=31536000, immutable` |
| Sin compresión Gzip/Brotli en el servidor | Activar en `.htaccess` o configuración del servidor |
| Chat widgets, píxeles o scripts de tracking en el load inicial | Diferir hasta interacción del usuario |
| Fonts sin `font-display: swap` | `font-display: swap` en `@font-face` |
| Fuentes web sin subsetting (charset completo) | Solo subconjunto Latin-Extended para español |
| PageSpeed móvil < 90 al deploy | Nunca hacer deploy con score < 90 sin aprobación |
| HTTP/1.1 cuando el hosting soporta HTTP/2 | Verificar que el hosting tiene HTTP/2 activo |
| `document.querySelector` dentro de un bucle | Cachear la referencia antes del bucle |
| Imágenes bajo el fold sin `loading="lazy"` | `loading="lazy"` en todo `<img>` que no sea LCP |
| Render-blocking CSS sin non-blocking pattern | `media="print" onload="this.media='all'"` + noscript fallback |
| Importar una librería entera para usar una función | Vanilla JS o import selectivo (Navaja de Ockham) |
| SVGs decorativos inlineados con paths complejos | `<img src="icon.svg">` o CSS `background-image` |
| Fonts de Google cargadas en `<link>` sin `display=swap` en la URL | `&display=swap` en la URL de Google Fonts |

---

## ⚡ WEB MÓVIL — ESPECIAL IMPORTANCIA

> **Desde 2019 Google indexa mobile-first.** El rendimiento y la usabilidad en móvil determinan el posicionamiento de TODOS los usuarios, incluidos los de escritorio. Un fallo en móvil no es un fallo secundario: es el fallo principal.

### Viewport y layout

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `<meta name="viewport">` ausente | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` — nunca omitir |
| `user-scalable=no` o `maximum-scale=1` en el viewport | Violación WCAG 1.4.4 — el usuario tiene derecho a hacer zoom |
| Elementos con ancho fijo > 360 px sin `max-width` | `max-width: 100%` en todos los elementos de ancho fijo |
| `width: 100vw` sin compensar el scrollbar | Causa scroll horizontal — usar `width: 100%` en su lugar |
| `overflow-x: hidden` en body para tapar desbordamiento | Oculta el síntoma, no el problema; además rompe `position: sticky` |
| Contenedor centrado con `width: 800px; margin: auto` sin fallback | `max-width: 800px; width: 100%; margin: 0 auto` |
| `height: 100vh` sin `100svh` como segunda declaración | `height: 100vh; height: 100svh;` — Safari iOS corta el viewport |
| `position: fixed` dentro de un ancestro con `transform`, `filter` o `will-change` | El fixed deja de ser relativo al viewport — reestructura el DOM |
| Header/navbar que ocupa > 15% de la altura visible en móvil | Compactar en móvil; contenido por encima de navegación |
| Elementos decorativos de escritorio que no se ocultan en móvil | `display: none` en el breakpoint móvil para lo no esencial |
| Grid de escritorio que no colapsa a columna única en móvil | `grid-template-columns: 1fr` por defecto, expandir con `min-width` |
| Texto que desborda su contenedor en pantallas < 360 px | `overflow-wrap: break-word; word-break: break-word` |
| Imágenes sin `max-width: 100%` | `img { max-width: 100%; height: auto; }` en el reset |

### Touch e interacción

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Touch targets < 44 × 44 px | Mínimo 44 × 44 px (Apple HIG) / 48 × 48 px (Material Design) |
| Separación < 8 px entre targets táctiles adyacentes | Al menos 8 px de margen entre botones/links |
| Interacciones que solo funcionan con `:hover` | Duplicar siempre la lógica en `:focus`, `:active` o clic |
| Menús dropdown que se abren con `hover` puro | Toggle con click/tap; hover como acelerador opcional en desktop |
| Sin `touch-action: manipulation` en botones e links | Elimina el delay de 300 ms por detección de double-tap |
| Swipe como única forma de acceder a una acción | Añadir siempre alternativa visible (botón, link) |
| Gestos complejos (3 dedos, doble swipe) para acciones principales | UI estándar con botones visibles |
| `pointer-events: none` en zonas que el usuario necesita pulsar | Revisar el z-index y la estructura; no deshabilitar la interacción |
| Zona de clic que no incluye el label del elemento | El área táctil debe incluir texto e icono |
| Elementos interactivos demasiado juntos en una lista | `padding` generoso; al menos `min-height: 44px` por fila |

### iOS Safari — errores específicos

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `height: 100vh` sin `svh` | `height: 100vh; height: 100svh;` — la toolbar de Safari reduce el viewport |
| `position: sticky` sin declarar `top`, `bottom`, `left` o `right` | `position: sticky; top: 0;` — el valor de offset es obligatorio |
| Autoplay de audio o vídeo con sonido | `autoplay muted playsinline` — iOS bloquea audio sin gesto del usuario |
| `font-size < 16px` en `<input>`, `<select>`, `<textarea>` | iOS Safari hace zoom automático aunque esté configurado `user-scalable=no` |
| Sin soporte para `env(safe-area-inset-*)` | `padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left)` en el body para notch/Dynamic Island |
| `position: fixed` sin probar en Safari iOS | `position: fixed` + `transform` en el ancestro → el fixed deja de anclarse al viewport |
| `-webkit-appearance: none` sin reestilizar el elemento | Deja el input sin estilos visuales; siempre añadir estilos propios después |
| `<input type="date">` sin estilos de reset | iOS muestra su propio picker pero con estilo inconsistente — resetear con `-webkit-appearance: none` |
| `overscroll-behavior` no definido en overlays/modals | `overscroll-behavior: contain` evita que el scroll del modal propague al body |
| Menú hamburgesa que bloquea el scroll del body sin `overflow: hidden` en body | `body { overflow: hidden }` mientras el menú está abierto; restaurar al cerrar |

### Formularios en móvil

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `type="text"` para email, teléfono o número | `type="email"` → teclado con @; `type="tel"` → teclado numérico; `type="number"` → teclado numérico con decimales |
| `font-size < 16px` en cualquier campo de formulario | 16 px mínimo en `input`, `select`, `textarea` — iOS hace zoom si es menor |
| Campos de formulario con `height` fija pequeña (< 44px) | `min-height: 44px` en todos los campos |
| `<select>` nativo reemplazado por dropdown JS en móvil | El `<select>` nativo en iOS/Android tiene mejor UX táctil que cualquier custom select |
| Teclado numérico para fechas en lugar de `type="date"` | `type="date"` activa el picker nativo del sistema operativo |
| Modal con formulario sin gestión del desplazamiento | El teclado virtual puede cubrir campos — scroll automático al campo con foco |
| Labels dentro del campo (floating labels) en móvil sin prueba | Verificar que el label no queda oculto bajo el teclado al escribir |
| Campos demasiado estrechos para escribir en táctil | `width: 100%` en todos los campos; nunca anchos fijos en formularios |
| Sin `inputmode` cuando el `type` no activa el teclado correcto | `inputmode="numeric"` para códigos postales, PIN, etc. |
| Autocomplete desactivado en campos estándar | `autocomplete="name"`, `"email"`, `"tel"`, `"current-password"`, etc. |

### Rendimiento móvil

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| JS > 200 KB (parseado + ejecutado) sin code splitting | Dividir en chunks; cargar solo lo necesario para el fold inicial |
| Imágenes sin `srcset` y `sizes` | Móvil debe recibir la imagen del tamaño de su pantalla, no la de escritorio |
| Hero image > 200 KB en móvil | Comprimir con Squoosh; AVIF < 80 KB para un hero 800 px |
| Sin throttle de red en pruebas de rendimiento | Probar siempre en "Slow 4G" (DevTools → Network → Throttling) |
| Más de 50 peticiones HTTP en el load inicial | Cada request en móvil tiene mayor latencia — consolidar y diferir |
| CSS no crítico bloqueando render | Non-blocking CSS obligatorio; en móvil el render es más lento |
| Scripts de tercero (analytics, chat, píxeles) sin diferir | `defer`, `async` o carga al interactuar — roban CPU al hilo principal |
| Sin comprobación del LCP en móvil específicamente | Lighthouse en modo móvil (simulado); LCP < 2,5 s en 4G |
| Fuentes web sin subsetting Latin | Una fuente completa puede pesar 200+ KB — subconjunto reduce a < 30 KB |
| Animaciones CSS en propiedades que disparan layout | Solo `transform` y `opacity` — en CPU de móvil el impacto se multiplica |

### Tipografía y contenido en móvil

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Texto < 16 px en el cuerpo en móvil | Mínimo 16 px; recomendado 18 px — pantallas pequeñas y luz solar |
| Longitud de línea > 70 caracteres en móvil | `max-width: 65ch` en contenedores de texto |
| `text-align: justify` sin `hyphens: auto` | Los ríos blancos en columna estrecha dificultan la lectura |
| Texto en ALL CAPS en párrafos | Más difícil de leer; reservar para headings cortos |
| Interlineado < 1.5 en párrafos en móvil | `line-height: 1.6` o superior en cuerpo de texto móvil |
| Contraste < 4,5:1 (o < 7:1 en contenido crítico) | Las pantallas OLED en exterior pierden contraste — ser conservador |
| Imágenes de texto (texto embebido en imagen) | Texto real en HTML — las imágenes de texto no escalan ni se traducen |
| Párrafos sin separación visual entre ellos | `margin-bottom: 1em` mínimo entre párrafos |

### Navegación en móvil

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Menú de escritorio (horizontal, con dropdowns) en móvil sin adaptar | Diseño de navegación móvil independiente |
| Hamburgesa sin texto "Menú" o aria-label descriptivo | `<button aria-label="Abrir menú" aria-expanded="false">` |
| Menú que se abre sin animación de entrada visible | Transición de 200–300 ms para que el usuario sepa qué ocurrió |
| Breadcrumbs con > 3 niveles en móvil sin truncar | Mostrar solo el nivel actual y el padre inmediato |
| Links del footer en columnas de escritorio en móvil | Columna única en móvil; o acordeón si hay muchos grupos |
| Logo tan grande que ocupa > 40% de la barra superior | Limitar a 32–40 px de alto; priorizar espacio para el contenido |
| Sin botón de "scroll to top" en páginas largas | Botón flotante visible tras scrollear > 100vh |
| CTA principal que no es visible sin hacer scroll en móvil | El CTA más importante debe estar en el primer pantallado |
| Menú abierto que no tiene opción visible de cierre | Botón X visible; tecla Esc también debe cerrar |

---

## SEO

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `<title>` duplicado en varias páginas | Único y descriptivo por página (máx. 60 chars) |
| Meta description ausente o duplicada | Única por página, 150–160 chars |
| Página sin canonical | `<link rel="canonical" href="URL-final">` en todas |
| Cadenas de canonical (A→B→C) | Siempre apunta a la URL final directamente |
| `robots.txt` bloqueando CSS o JS | Solo bloquear lo que no debe rastrearse |
| Confundir `robots.txt` con `noindex` | `robots.txt` bloquea rastreo; `noindex` bloquea indexación |
| Dos páginas con la misma keyword objetivo | Una keyword por página; unificar o usar canonical |
| Texto ancla "clic aquí" o "más información" | Texto descriptivo del destino |
| Página huérfana (sin enlace entrante) | Toda página tiene al menos un enlace interno |
| `noindex` en páginas que deben indexarse | Revisar antes del deploy |
| `noindex` en páginas en producción heredado del entorno de staging | Verificar que el meta robots es correcto en producción |
| Imágenes sin `alt` descriptivo | `alt` describe el contenido visual, nunca el nombre del archivo |
| NAP inconsistente entre footer, JSON-LD y Google Business *(negocio local)* | NAP idéntico en las tres fuentes |
| Schema.org con datos falsos o inventados | Solo datos verificables |
| Schema.org implementado con Microdata o RDFa | JSON-LD siempre (más limpio, más fácil de mantener) |
| Sitemap con URLs no indexables o con parámetros | Solo páginas limpias con `index, follow` |
| `<h1>` ausente o duplicado | Un solo `<h1>` por página |
| OG image en AVIF | OG image en WebP o JPG — redes sociales no soportan AVIF |
| OG image con tamaño distinto de 1200×630 px | Exactamente 1200×630 px |
| Keyword stuffing (repetir keyword artificialmente) | Keyword natural en title, h1, primer párrafo y URL |
| `<meta name="keywords">` | Google la ignora desde 2009; solo revela tu estrategia |
| URLs con parámetros como URL canónica | URLs limpias y descriptivas |
| Contenido relevante renderizado solo con JS | HTML estático para contenido que debe indexarse |
| Links rotos internos (404) | Verificar antes del deploy y mensualmente con Search Console |
| Redirigir con 302 cuando el cambio es permanente | 301 para redirecciones definitivas |
| `display: none` en contenido que debe indexarse | Google puede ignorar contenido oculto con CSS |
| Fecha de actualización ausente en contenido de blog/artículos | `<time datetime="AAAA-MM-DD">` visible en la página |

---

## Seguridad

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| API keys, tokens o contraseñas en el código fuente | Variables de entorno, fuera del repo |
| API keys en el repositorio aunque sea privado | Variables de entorno; rotar la key si se expuso |
| `display_errors=On` en producción (PHP) | `display_errors=Off`; `log_errors=On` en servidor |
| Concatenar input del usuario en queries SQL | Prepared statements siempre, sin excepción |
| Confiar en validación solo del cliente (JS) | Validar siempre en el servidor |
| Archivos `.env`, `.git`, `config.php` accesibles desde web | Bloquear en `.htaccess` o fuera del webroot |
| `innerHTML` con datos del usuario sin sanitizar | `DOMPurify.sanitize()` antes de insertar |
| Sin cabeceras de seguridad (CSP, HSTS, X-Frame-Options…) | Configurar en `.htaccess` (ver sección 18 del doc principal) |
| CSP con `'unsafe-inline'` o `'unsafe-eval'` | Nonces o hashes para scripts inline necesarios |
| HTTPS no forzado | Redirigir 301 todo `http://` a `https://` en `.htaccess` |
| `target="_blank"` sin `rel="noopener noreferrer"` | Siempre añadir el `rel` |
| Listado de directorios activado | `Options -Indexes` en `.htaccess` |
| Mensajes de error con rutas, versiones o stack interno | Mensajes genéricos; log en servidor |
| Archivos de upload en `public_html` sin restricciones | Guardar fuera del webroot; sin permisos de ejecución |
| Sin validación de MIME en uploads | Validar MIME en servidor + renombrar archivo |
| Formularios sin token CSRF (proyectos con backend) | Token único por sesión, verificado en servidor |
| Contraseñas en texto plano o con MD5/SHA1 | `password_hash()` + `password_verify()` en PHP |
| Cookies de sesión sin flags `Secure` y `HttpOnly` | `session.cookie_secure=1; session.cookie_httponly=1` en PHP |
| JWT en `localStorage` | Cookie `httpOnly` + `Secure` |
| `Access-Control-Allow-Origin: *` en APIs con datos privados | Listar orígenes explícitamente |
| Peticiones GET para operaciones que modifican estado | GET solo para lecturas; POST/PUT/DELETE para mutaciones |
| Subida de archivos ejecutables (.php, .js server-side) | Whitelist de extensiones permitidas (jpg, png, pdf, etc.) |
| Versión de PHP/WordPress/plugins visible en headers o meta tags | Ocultar en `php.ini`: `expose_php=Off` |
| Input del usuario en rutas de archivo sin saneamiento | Nunca usar input del usuario directamente en `include()` o `require()` |

---

## Accesibilidad

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Eliminar el `outline` de foco sin reemplazarlo | `:focus-visible { outline: 2px solid var(--color-primary); }` |
| Color como único indicador de estado | Acompañar siempre con forma, texto o icono |
| Contraste < 4,5:1 en texto normal | Verificar en [contrast.tools](https://contrast.tools) |
| Contraste < 3:1 en texto grande (> 18 px bold o > 24 px) | Ídem |
| Contraste que pasa en modo claro pero no en modo oscuro | Verificar ambos modos |
| Iconos sin texto alternativo | `aria-label="..."` o `<span class="sr-only">` |
| ARIA cuando el elemento HTML nativo hace el trabajo | `<button>` ya tiene rol, foco y teclado — no añadir `role="button"` a un div |
| `aria-hidden="true"` en un elemento con foco | El usuario del teclado quedaría atrapado |
| Movimiento sin respetar `prefers-reduced-motion` | `@media (prefers-reduced-motion: reduce)` desactiva animaciones |
| GIFs animados sin mecanismo para detenerlos | Botón de pausa o usar vídeo con `controls` |
| Vídeo sin subtítulos | `<track kind="subtitles" src="...vtt">` |
| Interactivos no alcanzables con Tab | Todo elemento interactivo debe estar en el flujo de teclado |
| Orden de tabulación roto (Tab salta de forma inesperada) | Evitar `tabindex` > 0; el orden visual = orden del DOM |
| `tabindex="-1"` en elementos que deben ser tabulables | Solo para elementos que se enfocan programáticamente |
| Más de un `<h1>` por página | Uno solo |
| `placeholder` como sustituto del `<label>` | `<label>` visible siempre; `placeholder` solo como ejemplo |
| Autoplay con sonido | `autoplay` solo con `muted` + `playsinline` |
| Touch targets < 44 × 44 px | Mínimo 44 × 44 px con al menos 8 px de separación |
| Sin skip link | `<a href="#main" class="skip-link">` al inicio del body |
| Autofocus en un campo al cargar la página | Desorientador para lectores de pantalla |
| `title` como única fuente de información de tooltip | No es accesible en móvil/touch; usar texto visible o `aria-describedby` |
| Contenido solo en CSS `content: ""` que sea significativo | El contenido semántico pertenece al HTML |
| Enlace que abre en nueva pestaña sin advertencia visual | Indicar `(abre en nueva pestaña)` en el `aria-label` o texto visible |
| Texto justificado (`text-align: justify`) sin `hyphens: auto` | Los ríos blancos dificultan la lectura con dislexia |
| Tamaño de fuente < 16 px en el cuerpo de texto | Mínimo 16 px; recomendado 18 px para lectura cómoda |

---

## UX y dark patterns

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Confirmshaming ("No, prefiero pagar más") | Texto neutro para rechazar: "No, gracias" |
| Casillas pre-marcadas para suscripciones o cookies | El usuario debe marcar activamente |
| Falsa urgencia o escasez (contador que se reinicia) | Urgencia real y verificable o sin contador |
| Bait and switch (se muestra A, se entrega B) | Lo que se muestra es lo que se entrega |
| Pop-up de suscripción inmediato al entrar | Esperar al menos 30 s o scroll del 50% |
| Botón de cierre microscópico o difícil de encontrar | El X debe ser fácil de encontrar y pulsar |
| Roach motel (fácil suscribirse, imposible cancelar) | Cancelar igual de fácil que suscribirse |
| Publicidad camuflada como contenido editorial | Etiquetar siempre como "Publicidad" o "Patrocinado" |
| Costes ocultos que aparecen al final del proceso | Mostrar el precio total desde el principio |
| Carrusel / slider con avance automático sin controles | Pausar por defecto; botones prev/next visibles |
| Scroll infinito sin forma de llegar al footer | Botón "Cargar más" o paginación clásica |
| Solicitar el email dos veces (confirmación de email) | Un solo campo de email; el error se detecta al enviar |
| Campo de contraseña sin opción "mostrar/ocultar" | Botón toggle para mostrar la contraseña |
| Modal de cookies que solo tiene "Aceptar todo" visible | Opción "Rechazar" con misma jerarquía visual (RGPD) |
| Overlay de cookies que bloquea todo el contenido | El contenido debe ser accesible; el banner no bloquea |
| Interstitial en la carga inicial en móvil | Google penaliza los intersticiales en el primer acceso |

## Formularios

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| `font-size < 16 px` en inputs en iOS | `font-size: 16px` mínimo — iOS hace zoom si es menor |
| Botón de envío con texto "Enviar" o "Submit" | Texto descriptivo: "Enviar consulta", "Reservar cita" |
| Sin feedback tras el envío | Spinner → mensaje de éxito o redirección a `/gracias.html` |
| Sin checkbox de consentimiento RGPD | Checkbox explícito con enlace a política de privacidad |
| Sin honeypot anti-spam | `<input type="checkbox" name="botcheck" style="display:none">` |
| Clave de Web3Forms en el repositorio público | Registrar con el email del cliente; variables de entorno si es público |
| Validación solo en el cliente | Validar también en el servidor |
| Mensajes de error genéricos ("Campo inválido") | Específicos: "El email debe incluir @" |
| Mensaje de error mostrado antes de que el usuario toque el campo | Mostrar al salir del campo (blur) o al enviar |
| Sin `autocomplete` en campos de datos del usuario | `autocomplete="name"`, `autocomplete="email"`, etc. |
| Más campos de los estrictamente necesarios | Cada campo extra reduce conversiones |
| `required` en campos que no son realmente obligatorios | Solo `required` en lo mínimo indispensable |

---

## Cookies y RGPD

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| GA4 disparando antes del consentimiento | Consent Mode v2 con `analytics_storage: denied` por defecto |
| Botón "Rechazar" más pequeño o menos visible que "Aceptar" | Misma jerarquía visual para ambos botones |
| Casillas pre-marcadas en el banner de cookies | El usuario debe marcar activamente |
| Cookies de marketing sin consentimiento previo | Siempre consentimiento previo; nunca asumir |
| Banner de cookies sin enlace a política de cookies | Enlace obligatorio en el banner |
| Sin opción de revocar el consentimiento | Icono flotante o link en footer para gestionar preferencias |
| Guardar el consentimiento más de 13 meses (analítica exenta) | Retención máxima 13 meses para exención AEPD |

---

## Stack y arquitectura

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Framework CSS (Bootstrap, Tailwind) sin justificación aprobada | HTML + CSS vanilla por defecto |
| React / Vue / Angular para un sitio de < 5 páginas informativas | HTML + CSS + JS vanilla |
| WordPress si el cliente no va a editar el contenido | Sitio estático |
| Base de datos para contenido que puede ser un archivo estático | JSON / Markdown / HTML estático |
| Decidir el stack sin respuesta a las preguntas del apartado 0E del doc principal | Preguntar primero, siempre |
| Dependencias de npm sin evaluar su mantenimiento y seguridad | Revisar `npm audit`; preferir dependencias con < 5 dependencias transitivas |
| Arquitectura que requiere VPS/cloud si el cliente tiene hosting compartido | Elegir el stack que encaje con el hosting ya contratado |

---

## Deploy y producción

| ❌ PROHIBIDO | ✅ CORRECTO |
|---|---|
| Empezar a codificar sin repositorio en GitHub | Crear el repo en GitHub **antes** del primer commit |
| Commit directamente a `main` sin PR | Rama `feature/*` o `fix/*` → PR → revisión → merge |
| Deploy sin pasar el checklist del apartado 19 del doc principal | Checklist completo antes de cada deploy |
| `display_errors=On` en producción | `display_errors=Off`; `log_errors=On` en servidor |
| Errores del servidor visibles al usuario | Mensaje genérico; detalles solo en el log del servidor |
| Log de errores sin revisar tras el deploy | Revisar el log de errores tras cada deploy |
| Errores JS no capturados en producción | `window.onerror` o Sentry si el proyecto lo justifica |
| PageSpeed móvil < 90 en producción | Resolver antes del deploy o aprobación explícita |
| Archivos sensibles accesibles (`.env`, `.git`, `config.php`) | Bloquear en `.htaccess` o fuera del webroot |
| Deploy sin backup previo (si hay BD) | Backup de BD antes de cada deploy con cambios de esquema |
| Sin monitoring de uptime tras el deploy | UptimeRobot o Freshping desde el primer día |
| Solución compleja cuando existe una simple equivalente | Navaja de Ockham: elige siempre la solución más simple |

---

*Este documento es complementario a ELIAWEB_STANDARDS_v4.md. Si algo aquí contradice el doc principal, aplica el criterio más restrictivo y PREGUNTA.*
