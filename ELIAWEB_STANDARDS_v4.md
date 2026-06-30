# ELIAWEB STANDARDS v4
**Directrices para IA. Leer y aplicar íntegramente antes de crear cualquier web.**
*Revisado junio 2026 — válido para cualquier proyecto web*

---

## ⚠️ NORMA PREVIA — INAMOVIBLE

Antes de violar cualquier directriz de este documento: **PARA y PREGUNTA.**
No improvises. No asumas que "en este caso está bien". Si el cliente pide algo que contradice estas normas, expón el conflicto y espera respuesta antes de continuar.
Dato sin fuente verificable = no existe. "No lo sé" es una respuesta válida.

### Principio rector — Navaja de Ockham

> **Lo más sencillo es lo más efectivo. No añadas complejidad que el proyecto no justifica.**

Esto rige sobre todo lo demás. Ante dos soluciones que cubren el mismo requisito, elige siempre la más simple. Si una tecnología, librería o patrón de diseño necesita una justificación larga para ser elegida: no la uses.

- ¿Puede ser HTML estático? No uses un framework.
- ¿Puede ser CSS puro? No importes una librería.
- ¿Puede ser un archivo JSON? No montes una base de datos.
- ¿Puede hacerse en 10 líneas? No escribas 100.

Este principio se recuerda explícitamente en los puntos de decisión a lo largo del documento.

---

## 0. ELECCIÓN DE STACK — PRIMERA DECISIÓN

Antes de escribir una sola línea de código, determina el stack correcto. **La complejidad mínima que cubra los requisitos es siempre la elección correcta.** Sobreingeniería y subingeniería son igualmente dañinas.

### 0A. Árbol de decisión

1. ¿El cliente necesita editar contenido él mismo (texto, imágenes, blog)?
   - Sí → CMS (WordPress o headless CMS)
   - No → sitio estático (HTML/CSS/JS puro o SSG)

2. ¿Hay usuarios registrados, e-commerce o datos dinámicos por usuario?
   - Sí → framework backend + base de datos
   - No → sin backend

3. ¿La interfaz requiere estado global complejo o interactividad tipo app?
   - Sí → framework frontend (React/Next.js, Vue/Nuxt) — con justificación documentada
   - No → HTML + CSS + JS vanilla (siempre preferir sobre cualquier framework)

### 0B. Stack por tipo de proyecto

| Tipo de proyecto | Stack recomendado | BD |
|---|---|---|
| Landing page / presentación | HTML + CSS + JS vanilla | No |
| Portfolio / brochure | HTML + CSS + JS vanilla | No |
| Blog / contenido estático | SSG (Astro, Eleventy, Hugo) | No — Markdown |
| Web con CMS para el cliente | WordPress (PHP + MySQL) | MySQL |
| E-commerce pequeño | WooCommerce / Shopify | MySQL (WooCommerce) |
| Aplicación web con usuarios | Laravel / Next.js / Django | PostgreSQL o MySQL |

### 0C. Base de datos — cuándo y cuál

- **Sin BD**: sitios estáticos, formularios con Web3Forms, contenido en HTML/JSON/Markdown.
- **SQLite**: apps internas pequeñas, < 100 K registros, sin concurrencia.
- **MySQL / MariaDB**: hosting compartido (cPanel), WordPress, proyectos PHP. Estándar en España.
- **PostgreSQL**: cloud (Supabase, Railway, Render), consultas complejas, proyectos escalables.
- **Redis**: caché de sesiones o datos de alta frecuencia de lectura.

### 0D. Reglas de stack inamovibles

- **Navaja de Ockham**: si puede ser estático, es estático. Si puede ser un archivo, no es una BD. La complejidad debe justificarse, no asumirse.
- Sin framework CSS (Bootstrap, Tailwind) salvo decisión justificada y aprobada (ver apartado 1).
- Sin React/Vue/Angular para un sitio de 5 páginas informativas: es sobreingeniería.
- WordPress solo si el cliente edita contenido o el proyecto necesita ecosistema CMS.
- El stack afecta el hosting: HTML/SSG → cualquier hosting; PHP+MySQL → cPanel; Node.js → VPS/cloud.
- **Repositorio en GitHub desde el primer commit. Sin excepción.** El repo es el backup, el historial y el punto de deploy. Crear el repo antes de escribir una línea de código.

### 0E. Preguntas obligatorias al cliente antes de empezar

- ¿Necesita editar el contenido sin tocar código?
- ¿Hay formularios, reservas, pagos o área privada?
- ¿Presupuesto de hosting mensual? (cPanel compartido: 3–10 €/mes; VPS: 5–20 €/mes)
- ¿Hay un dominio y hosting ya contratados? ¿Cuáles?

Sin estas respuestas: **PREGUNTA. No asumas el stack.**

---

## 1. PRINCIPIOS GENERALES

- **Navaja de Ockham: la solución más simple que funciona es la correcta.** Ante la duda entre dos enfoques, elige el más sencillo.
- HTML para estructura. CSS para presentación. JS para comportamiento. Nunca mezclar.
- Sin frameworks CSS (no Bootstrap, no Tailwind) salvo decisión justificada y aprobada.
- Mobile first. Breakpoints: 600 px → 900 px → 1200 px.
- `!important` prohibido. Excepción única: `prefers-reduced-motion`.
- Un archivo CSS. Un archivo JS mínimo con `defer`. *(Si puedes quitarlo, quítalo.)*
- Repositorio en GitHub desde el primer commit. Sin excepción.
- Nunca publicar sin pasar el checklist del apartado 19.

---

## 2. HTML

### 2A. Atributos y estructura base

- `<html lang="es">` siempre (o el idioma del proyecto). Obligatorio para accesibilidad y SEO.
- `<meta charset="UTF-8">` como primer hijo del `<head>`.
- `<title>` único y descriptivo en cada página.
- Usa HTML5 semántico: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`.
- Un solo `<h1>` por página. Jerarquía sin saltos (h1 → h2 → h3). Nunca saltes de h2 a h4.
- `alt`, `width` y `height` en todos los `<img>`. Imagen decorativa: `alt=""` (vacío, no ausente).
- `<label>` visible asociado a cada campo (`for` + `id` coincidentes).
- Skip link al inicio del `<body>`: `<a href="#main" class="skip-link">Ir al contenido</a>`.
- Los `id` deben ser únicos por página. Duplicar un `id` rompe accesibilidad y JS.
- Valida en [validator.w3.org](https://validator.w3.org) antes de entregar.

### 2B. `<button>` vs `<a>` — distinción crítica

| Elemento | Cuándo usarlo |
|---|---|
| `<a href="...">` | Navega a una URL (interna o externa). Si no tiene `href`, no es un enlace. |
| `<button type="button">` | Dispara una acción en la página: abrir modal, enviar formulario, toggle menú. |

**Nunca:** `<div onclick>`, `<span onclick>`, `<a href="#">` para acciones. Son inaccesibles por teclado y lectores de pantalla. El elemento nativo ya incluye roles ARIA, foco y comportamiento de teclado sin código extra.

`target="_blank"` siempre con `rel="noopener noreferrer"` — sin esto, la pestaña abierta puede acceder al contexto del origen (vulnerabilidad de seguridad).

### 2C. Formularios — estructura semántica

```html
<!-- Campos agrupados: fieldset + legend obligatorios -->
<fieldset>
  <legend>Método de pago</legend>
  <label><input type="radio" name="pago" value="tarjeta"> Tarjeta</label>
  <label><input type="radio" name="pago" value="bizum"> Bizum</label>
</fieldset>
```

Tipos de `input` correctos (nunca `type="text"` para todo):

| Dato | `type` correcto |
|---|---|
| Email | `type="email"` |
| Teléfono | `type="tel"` |
| Número | `type="number"` |
| Fecha | `type="date"` |
| Búsqueda | `type="search"` |
| URL | `type="url"` |
| Contraseña | `type="password"` |

### 2D. Tablas — uso correcto

Las tablas son para **datos tabulares**, nunca para maquetar. Estructura obligatoria:
```html
<table>
  <caption>Descripción de la tabla</caption>
  <thead>
    <tr><th scope="col">Columna A</th><th scope="col">Columna B</th></tr>
  </thead>
  <tbody>
    <tr><td>Dato</td><td>Dato</td></tr>
  </tbody>
</table>
```
`scope="col"` en `<th>` de cabecera de columna; `scope="row"` en `<th>` de cabecera de fila. Sin `scope`, el lector de pantalla no sabe a qué columna pertenece cada celda.

### 2E. Nunca

| Prohibido | Motivo |
|---|---|
| `<font>`, `<center>`, `<marquee>`, `<b>`, `<i>`, `<u>` | Tags obsoletos HTML5 |
| `style="..."` en línea | Rompe separación CSS/HTML |
| `onclick="..."`, `onload="..."` en HTML | Mezcla responsabilidades, bloquea CSP |
| `<div>` para botones o enlaces | Inaccesible por teclado y lectores de pantalla |
| Tablas para maquetar | Rompe responsive y accesibilidad |
| `<br />`, `<img />` con barra de cierre | Sintaxis XHTML, no HTML5 |
| `border="0"`, `align="center"` como atributos | Corresponde a CSS |
| `<a href="#">` para disparar acciones | Usar `<button type="button">` |
| `target="_blank"` sin `rel="noopener noreferrer"` | Vulnerabilidad de seguridad |
| Mismos `id` en más de un elemento | Rompe JS, ARIA y validación HTML |
| Imagen decorativa con `alt` ausente | Screen reader lee la URL del archivo |
| `<h3>` sin haber puesto antes `<h2>` | Rompe la jerarquía semántica |
| `<section>` sin encabezado hijo | Una section sin h* no tiene significado |

---

## 3. CSS

**Reset obligatorio al inicio:**
```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
```

**Cascade layers — orden fijo, siempre:**
```css
@layer reset, base, layout, components, utilities, motion, print;
```

**Variables en `:root` para todo valor reutilizable:**
```css
:root {
  --space-xs: 0.25rem; --space-sm: 0.5rem;
  --space-md: 1rem;    --space-lg: 2rem;  --space-xl: 4rem;
  --color-primary: ;   --color-bg: ;      --color-text: ;   --color-accent: ;
  --font-body: ;       --font-heading: ;
}
```

**Unidades:** `rem` y `clamp()` para tipografía. `%`, `vw`, `vh`, `clamp()` para layout. Mínimo 16 px en body.
**Naming:** BEM estricto — `.bloque__elemento--modificador`.
**Movimiento accesible** (único `!important` permitido):
```css
@layer motion {
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
  }
}
```

**Dark mode** — implementa siempre que el diseño lo permita:
```css
:root {
  --color-bg:   #ffffff;
  --color-text: #1a1a1a;
  --color-primary: ;
}
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg:   #1a1a1a;
    --color-text: #f0f0f0;
    /* redefine solo las variables que cambian */
  }
}
```
Nunca hardcodees colores fuera de `:root`. Así el dark mode funciona cambiando solo las variables.

**Sistema tipográfico — escala fluida con `clamp()`:**
```css
:root {
  /* Fórmula: clamp(mín, preferido-en-vw, máx) */
  --text-sm:   clamp(0.8rem,  0.75rem + 0.25vw, 0.9rem);
  --text-base: clamp(1rem,    0.95rem + 0.25vw, 1.125rem);
  --text-lg:   clamp(1.125rem,1rem + 0.5vw,     1.35rem);
  --text-xl:   clamp(1.25rem, 1rem + 1vw,       1.75rem);
  --text-2xl:  clamp(1.5rem,  1rem + 2vw,       2.5rem);
  --text-3xl:  clamp(2rem,    1.5rem + 2.5vw,   3.5rem);

  --leading-tight:  1.2;
  --leading-normal: 1.5;
  --leading-loose:  1.8;
}
```
Aplica `line-height: var(--leading-normal)` a párrafos. Usa `--leading-tight` en headings.

### 3A. Flexbox vs Grid — cuándo usar cada uno

| Situación | Herramienta |
|---|---|
| Layout en una dimensión (fila O columna) | **Flexbox** |
| Layout en dos dimensiones (filas Y columnas) | **Grid** |
| Centrar un elemento | Flexbox (`display:flex; place-items:center`) |
| Layout de página completo (header/main/footer) | Grid |
| Alinear iconos con texto | Flexbox |
| Galería de tarjetas que deben alinearse en filas | Grid |
| Componente de navegación horizontal | Flexbox |
| Solapamiento de elementos | Grid (áreas nombradas o `grid-column`) |

Nunca uses `float` para layout. Nunca uses `position:absolute` para maquetar columnas.

### 3B. Animaciones y transiciones — rendimiento

Solo anima propiedades que no disparen layout ni paint:

| ✅ Barato (solo composite) | ❌ Caro (dispara layout/paint) |
|---|---|
| `transform: translate / scale / rotate` | `width`, `height`, `top`, `left`, `margin` |
| `opacity` | `background-color` (caro en algunos contextos) |
| `filter` (con cautela) | `font-size`, `padding`, `border-width` |

```css
/* Correcto: GPU-accelerated, sin reflow */
.card { transition: transform 0.2s ease, opacity 0.2s ease; }
.card:hover { transform: translateY(-4px); opacity: 0.9; }

/* Incorrecto: dispara layout en cada frame */
.card:hover { margin-top: -4px; height: 105%; }
```

Duración máxima recomendada en UI: 300 ms. Más lento se percibe como lento.

### 3C. z-index — estrategia con variables

Nunca valores mágicos (`z-index: 9999`). Define niveles semánticos en `:root`:

```css
:root {
  --z-base:     0;
  --z-raised:   10;   /* cards, dropdowns */
  --z-dropdown: 100;
  --z-sticky:   200;  /* headers sticky */
  --z-modal:    300;
  --z-toast:    400;
  --z-tooltip:  500;
}
```

`z-index` solo funciona en elementos con `position` distinta de `static`. Si no funciona, revisa el contexto de apilamiento (`transform`, `opacity < 1`, `filter` crean un nuevo stacking context).

### 3D. Bug 100vh en iOS — usa svh

`height: 100vh` en iOS incluye la barra del navegador → el contenido queda cortado.

```css
/* Incorrecto en iOS */
.hero { height: 100vh; }

/* Correcto: svh (small viewport height) */
.hero { height: 100svh; }

/* Fallback para navegadores sin svh */
.hero { height: 100vh; height: 100svh; }
```

`svh` = viewport sin barras de navegador. Soporte 2026: Chrome 108+, Safari 15.4+, Firefox 101+.

### 3E. Anti-patrones CSS — errores habituales

| Anti-patrón | Impacto | Solución |
|---|---|---|
| `px` en `font-size` del `body` | Ignora el tamaño de fuente del navegador del usuario | `font-size: 100%` en body, `rem` en el resto |
| Colores hardcoded fuera de `:root` | Inconsistencia, dark mode roto | Siempre `var(--color-*)` |
| `z-index: 9999` sin contexto | Caos visual en proyectos con varios componentes | Variables semánticas (ver 3C) |
| Selectores por ID (`#hero`) | Alta especificidad, difícil de sobrescribir | Clases BEM siempre |
| `margin: auto` sin ancho definido | No centra nada sin `width` o `max-width` | Define el ancho antes de centrar |
| `position: absolute` para todo | Saca el elemento del flujo, rompe responsive | Solo para overlays, tooltips, decoraciones |
| `overflow: hidden` en el contenedor | Recorta `box-shadow`, `outline` y elementos absolutos hijos | Usa `overflow: clip` o revisa el layout |
| `display: none` para accesibilidad | Oculta también de lectores de pantalla | `visibility: hidden` o `aria-hidden="true"` según caso |
| Mezclar `margin` shorthand y longhand | `margin: 1rem` seguido de `margin-top: 0` → el shorthand gana o no | Usa solo uno por regla |
| `calc()` con unidades incompatibles | Error silencioso | `calc(100% - 2rem)` ✅ / `calc(100% - 2px - 1rem)` revisar |

### 3F. Especificidad — regla práctica

Con cascade layers, la especificidad interna a cada layer es la normal, pero un estilo en un layer superior siempre gana a uno en un layer inferior, independientemente de la especificidad. Por eso el orden de layers importa:

```css
@layer reset, base, layout, components, utilities, motion, print;
/* utilities gana siempre sobre components sin !important */
```

Si necesitas sobrescribir algo sin subir la especificidad: mueve la regla a un layer superior, no añadas `!important`.

### 3G. Nunca

| Prohibido | Motivo |
|---|---|
| `!important` (fuera de `prefers-reduced-motion`) | Deuda técnica irresoluble |
| Seleccionar por `#id` | IDs no son reutilizables, especificidad alta |
| `@import` dentro del CSS | Bloquea renderizado, doble request |
| Mezclar shorthand y longhand en la misma regla | Cascada impredecible |
| Colores hexadecimales hardcoded fuera de `:root` | Rompe dark mode y consistencia |
| Selectores > 3 niveles de profundidad | Especificidad explosiva |
| `px` en `font-size` del body | Ignora accesibilidad del navegador |
| `float` para layout de columnas | Float es para texto flotando alrededor de imagen |
| Animaciones en propiedades que disparan layout | Janky scrolling, alto CPU (ver 3B) |
| `height: 100vh` en móvil sin fallback `svh` | Contenido cortado en iOS |
| `z-index` con valores mágicos sin variable | Imposible de mantener |

---

## 4. JAVASCRIPT

**Haz:**
- `const` por defecto. `let` si el valor cambia. Nunca `var`.
- `'use strict';` al inicio (o usar módulos ES).
- Carga con `defer`: `<script src="/js/main.js" defer></script>`.
- `try/catch` en todo bloque asíncrono. Mensajes de error descriptivos y específicos.
- `.catch()` en toda promesa o `try/catch` con `async/await`.
- Limpia event listeners cuando el elemento desaparece del DOM.

**Nunca:**

| Prohibido | Motivo |
|---|---|
| `eval()` | Vector XSS, agujero de seguridad crítico |
| `var` | Scope de función, hoisting impredecible |
| `document.write()` | Bloquea renderizado, puede destruir el DOM |
| Promesas sin `.catch()` | Fallos silenciosos |
| Modificar `Array.prototype` u otros prototipos nativos | Rompe librerías de terceros |
| `console.log` en producción | Expone información interna |
| Datos sensibles en `localStorage` / `sessionStorage` | No cifrado, accesible por XSS |
| Dependencias sin versión fija verificada | Riesgo de supply chain attack |

---

## 5. PHP *(solo si el proyecto usa PHP)*

**Haz:**
- PDO o MySQLi con **prepared statements** para todas las queries.
- `htmlspecialchars()` en todos los outputs hacia HTML.
- Token CSRF en todos los formularios que escriban datos.
- `session.cookie_httponly=1`, `session.cookie_secure=1`. Regenera ID de sesión tras login.
- `password_hash()` / `password_verify()` para contraseñas.
- `display_errors=Off` en producción. Loguea errores en servidor.
- Archivos de configuración fuera del `public_html` o bloqueados.
- Mantén PHP en la versión estable con soporte activo (≥ 8.2).

**Nunca:**

| Prohibido | Motivo |
|---|---|
| `eval()`, `exec()`, `system()` con input de usuario | Remote Code Execution |
| `mysql_query()` sin prepared statements | SQL injection trivial |
| `include`/`require` con rutas controladas por usuario | LFI/RFI |
| Confiar en `$_FILES['type']` para validar uploads | El MIME lo controla el cliente |
| PHP < 8.1 en producción | Sin soporte de seguridad |
| `display_errors=On` en producción | Expone rutas y lógica interna |

---

## 6. HEAD — OBLIGATORIO EN CADA PÁGINA

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Robots: solo añadir cuando quieres noindex. Si no está, Google asume index,follow -->
<!-- <meta name="robots" content="noindex, follow"> solo en /gracias.html y similares -->

<!-- SEO -->
<title>[Keyword] — [Negocio] | [Ciudad si aplica]</title>   <!-- máx. 60 chars, única -->
<meta name="description" content="...">                      <!-- 150–160 chars, única -->
<link rel="canonical" href="https://www.dominio.es/pagina.html">

<!-- Open Graph -->
<meta property="og:type"         content="website">
<meta property="og:title"        content="...">
<meta property="og:description"  content="...">
<meta property="og:url"          content="https://www.dominio.es/pagina.html">
<meta property="og:image"        content="https://www.dominio.es/img/og-image.webp">
<meta property="og:image:width"  content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale"       content="es_ES">
<meta name="twitter:card"        content="summary_large_image">

<!-- Favicons — conjunto completo -->
<link rel="icon"             href="/favicon.ico" sizes="any">
<link rel="icon"             href="/img/favicon-32.png" type="image/png" sizes="32x32">
<link rel="icon"             href="/img/favicon-16.png" type="image/png" sizes="16x16">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">  <!-- 180×180 px -->
<link rel="manifest"         href="/manifest.json">
<meta name="theme-color"     content="#[color-primary-del-proyecto]">

<!-- Rendimiento: preload del hero y preconnect a orígenes críticos -->
<link rel="preload" href="/img/hero.avif" as="image" type="image/avif">
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="dns-prefetch" href="https://fonts.gstatic.com">

<!-- Fuentes autohospedadas: preload -->
<!-- <link rel="preload" href="/fonts/fuente.woff2" as="font" type="font/woff2" crossorigin> -->

<!-- Critical CSS inline (< 14 KB, solo estilos above-the-fold) -->
<style>/* critical CSS aquí */</style>

<!-- CSS completo diferido — no bloquea render -->
<link rel="stylesheet" href="/css/style.css" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="/css/style.css"></noscript>

<!-- Schema.org JSON-LD — un bloque por tipo -->
<script type="application/ld+json">{ ... }</script>
```

---

## 7. SCHEMA.ORG JSON-LD

- Usa **JSON-LD** siempre. No Microdata, no RDFa.
- Un `<script type="application/ld+json">` por tipo de schema. Una página puede tener varios bloques.
- El contenido marcado en JSON-LD **debe ser visible** en la página para el usuario.
- Valida siempre en [Rich Results Test](https://search.google.com/test/rich-results) antes de publicar.

**Mínimo para cualquier sitio:**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "",
  "url": "https://www.dominio.es/",
  "logo": "https://www.dominio.es/img/logo.webp"
}
```

**Solo si es negocio local** (ver apartado 13B para NAP completo):
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "", "telephone": "", "email": "",
  "url": "https://www.dominio.es/",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "", "addressLocality": "", "postalCode": "", "addressCountry": "ES"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 0.0, "longitude": 0.0 }
}
```

**Para páginas FAQ** — añade un bloque adicional:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "¿Cuál es la pregunta?",
    "acceptedAnswer": { "@type": "Answer", "text": "La respuesta directa y completa." }
  }]
}
```

---

## 8. IMÁGENES

- Formato: **AVIF** primero. Fallback WebP. Fallback final JPG. La OG image va en WebP/JPG (las redes sociales no soportan AVIF).
- Siempre `width` y `height` explícitos (evita CLS).
- Hero: `loading="eager" fetchpriority="high"` + preload en el head.
- Todo lo demás: `loading="lazy"`.
- OG image: exactamente **1200 × 630 px**.
- Comprimir en [squoosh.app](https://squoosh.app) antes de subir. Calidad 75–80.

```html
<!-- Hero: AVIF > WebP > JPG, eager, con srcset por resoluciones -->
<picture>
  <source type="image/avif"
          srcset="/img/hero-400.avif 400w, /img/hero-800.avif 800w, /img/hero-1200.avif 1200w"
          sizes="(max-width: 600px) 100vw, (max-width: 900px) 80vw, 1200px">
  <source type="image/webp"
          srcset="/img/hero-400.webp 400w, /img/hero-800.webp 800w, /img/hero-1200.webp 1200w"
          sizes="(max-width: 600px) 100vw, (max-width: 900px) 80vw, 1200px">
  <img src="/img/hero-1200.jpg"
       srcset="/img/hero-400.jpg 400w, /img/hero-800.jpg 800w, /img/hero-1200.jpg 1200w"
       sizes="(max-width: 600px) 100vw, (max-width: 900px) 80vw, 1200px"
       alt="Descripción real" width="1200" height="630"
       loading="eager" fetchpriority="high">
</picture>

<!-- Imagen de contenido: lazy, con srcset -->
<picture>
  <source type="image/avif" srcset="/img/foto-400.avif 400w, /img/foto-800.avif 800w" sizes="(max-width: 600px) 100vw, 800px">
  <img src="/img/foto-800.jpg" alt="..." width="800" height="600" loading="lazy">
</picture>
```

**Regla `srcset`:** genera al menos 3 tamaños por imagen (400 w, 800 w, 1200 w). El navegador elige el óptimo según la pantalla y la densidad de píxeles del dispositivo.

**Vídeo:**
- Aloja los vídeos propios en el servidor o en CDN. No embeber vídeos propios en YouTube solo para reproducirlos en el sitio.
- Usa `<video>` con `preload="none"` salvo que el vídeo sea el elemento principal de la página.
- Incluye siempre subtítulos (`<track kind="subtitles" src="...vtt">`). Obligatorio WCAG.
- Para vídeos de YouTube/Vimeo embebidos: usa fachada (thumbnail clickable que carga el iframe solo al pulsar).
```html
<!-- Fachada de YouTube: evita cargar 500 KB de JS en el load inicial -->
<lite-youtube videoid="ID_DEL_VIDEO"></lite-youtube>
<!-- https://github.com/paulirish/lite-youtube-embed -->
```
- `autoplay` solo con `muted` y `playsinline`. Nunca autoplay con sonido.
- Incluye `controls` siempre que el usuario deba controlar la reproducción.

---

## 9. RENDIMIENTO — PAGESPEED

**Objetivos mínimos antes de entregar:**

| Métrica | Objetivo | Herramienta |
|---|---|---|
| PageSpeed móvil | ≥ 90 | pagespeed.web.dev |
| LCP | < 2,5 s | PageSpeed / DebugBear |
| INP | < 200 ms | PageSpeed |
| CLS | < 0,1 | PageSpeed |

Solo el 12% de webs supera 90 en móvil. Es alcanzable siguiendo estas directrices.

### 9A. Renderizado y CSS

- **Critical CSS inline** en el `<head>` (< 14 KB). Contiene solo los estilos visibles above-the-fold: tipografía base, reset, layout del hero, nav.
- CSS completo cargado de forma no bloqueante (patrón `media="print"` + onload del apartado 6).
- Elimina CSS no utilizado antes de producción. Herramienta: [PurgeCSS](https://purgecss.com).
- Minifica el CSS en producción.

### 9B. JavaScript

- Todo JS con `defer`. Nunca JS síncrono en `<head>` ni bloqueando el body.
- Divide el JS en módulos: carga solo lo necesario para la página actual.
- Evita tareas largas en el main thread (> 50 ms). Fragmenta con `setTimeout` o Web Workers si es necesario.
- Minifica en producción. Elimina código no utilizado (tree shaking).
- Herramienta de auditoría: Lighthouse en DevTools → apartado "Avoid long main-thread tasks".

### 9C. Resource hints — en el `<head>`, en este orden

```html
<!-- Preload: solo 2–4 recursos críticos de la página actual -->
<link rel="preload" href="/img/hero.avif" as="image" type="image/avif">
<link rel="preload" href="/fonts/mi-fuente.woff2" as="font" type="font/woff2" crossorigin>

<!-- Preconnect: orígenes de terceros críticos (máx. 2–3) -->
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>

<!-- DNS-prefetch: orígenes de terceros secundarios -->
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
```

No pongas más de 4 `preload`. Compiten por el ancho de banda y contraproducen.

### 9D. LCP — elemento más grande visible

- El elemento LCP (casi siempre el hero) nunca lleva `loading="lazy"`.
- Preload explícito del hero en el `<head>` (ver 9C).
- El hero debe estar en el HTML inicial, no inyectado con JS.
- Usa `fetchpriority="high"` en el `<img>` del hero.
- El servidor debe responder en < 200 ms (TTFB). Si no, revisar hosting o implementar CDN.

### 9E. CLS — estabilidad visual

- Dimensiones (`width` y `height`) en **todos** los `<img>` y `<video>`. Sin excepción.
- No inyectar contenido dinámico sobre contenido existente (banners, ads, embeds) sin reservar su espacio con `min-height`.
- Fuentes: usa `font-display: swap` para evitar saltos de texto al cargar.
- Evita `position: fixed` que empuje el layout al aparecer.

### 9F. INP — respuesta a interacciones

- Evita event listeners pesados que bloqueen el main thread.
- Operaciones costosas (filtros, cálculos, renders) fuera del evento de clic: usa `requestAnimationFrame` o `setTimeout(fn, 0)`.
- No adjuntes demasiados event listeners al `document` o `window`. Usa event delegation.

### 9G. Fuentes

- Autohospeda las fuentes siempre que sea posible (Google Fonts añade latencia de origen externo).
- Formatos: `woff2` primero, `woff` como fallback.
- `font-display: swap` en el `@font-face`.
- Preload de las fuentes críticas (la del cuerpo de texto y la del heading principal).
- No cargues más de 2 familias tipográficas. No cargues pesos que no uses.

### 9H. Terceros y embeds pesados

- Mapas (Google Maps, Mapbox): carga bajo demanda. No en el load inicial.
- Vídeos (YouTube, Vimeo): usa fachada (thumbnail + botón play) que carga el iframe solo al clic.
- Chat widgets, pixels de seguimiento: diferir hasta que el usuario interactúe.
- Cada script de tercero añade latencia. Audita con PageSpeed → "Reduce the impact of third-party code".

### 9I. Infraestructura

- HTTPS en producción (obligatorio, ver apartado 18).
- HTTP/2 o HTTP/3 en el servidor (los hostings modernos lo tienen por defecto).
- Gzip o Brotli activado (ver `.htaccess`, apartado 18).
- Cache-Control en activos estáticos (ver `.htaccess`, apartado 18).
- CDN si el tráfico es internacional o el servidor de origen está lejos del usuario.

### 9J. Minificación

Minifica en el pipeline de build antes de cada deploy. Nunca en producción en tiempo de ejecución.

| Recurso | Herramienta recomendada | Alternativa online |
|---|---|---|
| CSS | `cssnano` (postcss) / `lightningcss` | [cssminifier.com](https://cssminifier.com) |
| JS | `terser` | [toptal.com/developers/javascript-minifier](https://www.toptal.com/developers/javascript-minifier) |
| HTML | `html-minifier-terser` | [kangax.github.io/html-minifier-terser](https://kangax.github.io/html-minifier-terser/) |
| Imágenes | Squoosh (manual) / `sharp` (automático) | [squoosh.app](https://squoosh.app) |
| SVG | `svgo` | [svgomg](https://jakearchibald.github.io/svgomg/) |

En proyectos sin build system: minifica los archivos finales manualmente con las herramientas online antes del deploy. Incluye el paso en el checklist pre-deploy.

### 9K. Lo que NUNCA debes hacer para el rendimiento

| Prohibido | Impacto |
|---|---|
| JS síncrono en `<head>` sin `defer`/`async` | Bloquea render completamente |
| `loading="lazy"` en el hero o imagen LCP | Retrasa el LCP hasta 1–2 s extra |
| Más de 4 recursos en `<link rel="preload">` | Compiten entre sí, contraproducen |
| `@import` de CSS dentro del CSS | Bloquea CSSOM, doble request |
| Fuentes de Google Fonts cargadas en `<head>` sin preconnect | Latencia DNS extra por conexión |
| Imágenes sin `width` y `height` | CLS garantizado |
| Embeds de YouTube/Maps en el load inicial | Añaden 500 KB–2 MB de JS de tercero |
| CSS/JS sin minificar en producción | Bytes extra = LCP más lento |

---

## 10. SEGURIDAD

**Principios:**
- Nunca confíes en el input del usuario. Valida en servidor, no solo en cliente.
- Nunca expongas información interna en errores, headers o comentarios HTML.
- Nunca dejes credenciales, API keys o tokens en el código fuente.

**XSS:** Codifica el output (no solo filtra el input). `htmlspecialchars()` en PHP. CSP vía header (ver apartado 18).

**Inyección SQL:** Solo prepared statements. Nunca concatenes input de usuario en queries.

**CSRF:** Token único por sesión en formularios que modifiquen datos. Verificar en servidor.

**Archivos sensibles** (`.env`, `config.php`, `.git/`): fuera del webroot o bloqueados en `.htaccess`.

**Uploads:** Valida MIME en servidor. Limita tamaño. Guarda fuera de `public_html`. Renombra el archivo.

**Contraseñas:** `password_hash()` / `password_verify()`. Nunca en texto plano.

**Log de errores — producción:**

- `display_errors=Off` en producción. Los errores no se muestran al usuario.
- Los errores se **registran en un archivo de log** en el servidor, nunca en pantalla.
- PHP: `log_errors=On` + `error_log=/ruta/fuera/del/webroot/error.log` en `php.ini` o `.htaccess`.
- JS: captura errores no controlados con `window.onerror` y envíalos a un endpoint de log o a un servicio como Sentry (solo si el proyecto lo justifica — Navaja de Ockham).
- Los mensajes de error visibles al usuario son genéricos: "Ha ocurrido un error. Por favor, inténtalo de nuevo." Sin rutas, versiones ni stack trace.
- Revisa el log de errores tras cada deploy. Un deploy sin comprobación del log es un deploy ciego.

---

## 11. ACCESIBILIDAD — mínimo WCAG 2.1 AA

| Regla | Mínimo |
|---|---|
| Contraste texto/fondo | 4,5:1 (texto normal) · 3:1 (texto grande) |
| Skip link | Visible al recibir foco, al inicio del body |
| Iconos sin texto | `aria-label` obligatorio |
| Formularios | `<label>` por campo, errores descriptivos |
| Movimiento | `prefers-reduced-motion` respetado |
| `<h1>` | Uno solo por página |
| Navegación por teclado | Todos los interactivos alcanzables con Tab |
| Foco visible | No eliminar outline sin reemplazarlo |

---

## 12. UX Y USABILIDAD

### 12A. Heurísticos de Nielsen — aplica los 10

1. **Estado del sistema visible**: el usuario siempre sabe qué está pasando (spinners, confirmaciones, paso activo).
2. **Lenguaje del usuario**: sin jerga técnica. Iconos con significado universal.
3. **Control y salida clara**: siempre hay "Cancelar", "Volver" o deshacer.
4. **Consistencia**: mismo elemento = mismo comportamiento en todo el sitio.
5. **Prevención de errores**: validación en tiempo real antes del envío.
6. **Reconocimiento sobre recuerdo**: opciones visibles, no hay que memorizar rutas.
7. **Flexibilidad**: atajos para usuarios avanzados sin perjudicar a los nuevos.
8. **Diseño minimalista**: cada elemento que no ayuda, molesta. Elimina lo decorativo.
9. **Errores en lenguaje humano**: qué pasó + cómo solucionarlo.
10. **Ayuda accionable**: si necesita explicación, algo falla en el diseño.

### 12B. Jerarquía visual y diseño

- Una acción principal (CTA) por página. Las secundarias, visualmente subordinadas.
- Contraste funcional: el elemento más importante destaca sobre el resto.
- Espacio en blanco no es vacío: es respiración y estructura.
- Tipografía: máx. 2 familias. Cuerpo ≥ 16 px. Interlineado ≥ 1.5 en párrafos.
- Color: nunca como único indicador de estado. Acompaña siempre con forma, texto o icono.
- Animaciones: solo si aportan comprensión. Duración < 300 ms en transiciones de UI.

### 12C. Navegación

- Máximo 5–7 elementos en la nav principal.
- Logo siempre al inicio (convención universal).
- Indica la página activa: `aria-current="page"` + estilo visual.
- Hamburger menu: aceptable en móvil para sitios de contenido; pon lo crítico accesible sin abrirlo.
- Breadcrumbs en sitios con > 2 niveles.
- Nunca abrir enlaces en nueva pestaña sin advertirlo.

### 12D. Formularios — UX

- Solo los campos estrictamente necesarios. Cada campo extra reduce conversión.
- Etiquetas siempre visibles. Nunca solo placeholder como etiqueta.
- Validación en línea: errores campo a campo al salir del foco, no solo al enviar.
- Mensajes de error específicos: no "Campo inválido" → "El email debe incluir @".
- Botón de envío descriptivo: "Enviar consulta", "Reservar cita". Nunca "Submit" ni "Enviar" seco.
- Feedback tras envío: spinner → éxito o redirigir a `/gracias.html`.

### 12E. Microcopy

- CTAs: **verbo + objeto**. "Descargar guía", "Reservar cita". Nunca "Click aquí".
- Consistencia: el mismo CTA tiene el mismo texto en todo el sitio.
- Estados vacíos: cuando no hay contenido, explica por qué y qué puede hacer el usuario.
- Placeholders: solo como ejemplo de formato, nunca como sustituto de la etiqueta.

### 12F. UX en móvil

- Touch targets: mínimo **44 × 44 px**. Espacio entre elementos táctiles: ≥ 8 px.
- Activa el teclado correcto: `type="email"`, `type="tel"`, `type="number"`.
- Sin pop-ups en la carga inicial (Google penaliza intersticiales en el primer acceso).
- Contenido importante en zona de pulgar (parte central e inferior).
- Sin hover como único feedback — en táctil no hay hover.

### 12G. Rendimiento como UX

- 47% de usuarios esperan carga en ≤ 2 s. 40% abandona si supera 3 s.
- Cada segundo de más = −7% en conversiones.
- Ver objetivos y técnicas en el apartado 9.

### 12H. Dark patterns — NUNCA

| Patrón | Por qué está prohibido |
|---|---|
| Confirmshaming | Manipulación emocional |
| Casillas pre-marcadas | El usuario debe consentir activamente |
| Costes ocultos | Aparecen solo al final del proceso |
| Falsa urgencia / escasez | Contadores que se reinician |
| Bait and switch | Se muestra A, se entrega B |
| Roach motel | Suscribirse fácil, cancelar imposible |
| Publicidad camuflada como contenido | Engaño al usuario |
| Pop-up de suscripción inmediato | Bloquea el contenido antes de verlo |
| Botón de cierre microscópico | El X debe ser fácil de encontrar y pulsar |

Desde 2024: el Digital Services Act (DSA) prohíbe la mayoría de dark patterns con multas de hasta el 6% de la facturación global.

### 12I. Checklist UX antes de entregar

- [ ] ¿CTA principal claro en cada página?
- [ ] ¿El usuario sabe dónde está en todo momento?
- [ ] ¿Formularios con validación en línea y errores descriptivos?
- [ ] ¿Touch targets ≥ 44 px?
- [ ] ¿Navegación ≤ 7 elementos?
- [ ] ¿Feedback para todas las acciones?
- [ ] ¿Probado el flujo completo en móvil con el dedo?
- [ ] ¿Hay algún dark pattern? Si la respuesta no es "no, ninguno": PREGUNTAR.
- [ ] ¿Carga en < 3 s en 4G lenta? (throttle en DevTools)

---

## 13. SEO TÉCNICO

### 13A. On-page — siempre

- Title: `[Keyword] — [Negocio] | [Ciudad si aplica]`, máx. 60 chars, único por página.
- Meta description: 150–160 chars, única por página, con llamada a la acción.
- Canonical en todas las páginas apuntando a la URL definitiva (`https://www.`).
- Schema.org JSON-LD con tipo adecuado (ver apartado 7).
- `robots.txt` y `sitemap.xml` en la raíz.
- OG completo: og:title, og:description, og:image 1200×630, og:url.

### 13B. SEO local — SOLO si el negocio tiene ubicación física

- `@type` en JSON-LD: subtipo de `LocalBusiness` (`LodgingBusiness`, `Restaurant`, `MedicalBusiness`, etc.).
- JSON-LD incluye: dirección, teléfono, email, horario, coordenadas GPS verificadas en Google Maps.
- **NAP** (nombre + dirección + teléfono): **idéntico** en JSON-LD, footer de todas las páginas y Google Business Profile. Cualquier discrepancia penaliza.
- Registra y mantén actualizado el Google Business Profile.

### 13C. Rastreabilidad e indexación

- `robots.txt`: bloquea solo lo que NO debe rastrearse (admin, parámetros de búsqueda interna). No bloquees CSS ni JS.
- Diferencia crítica: `robots.txt` impide el **rastreo**, no la indexación. Para no indexar: `<meta name="robots" content="noindex, follow">` en el head.
- **No indexar**: `/gracias.html`, páginas de login, resultados de búsqueda interna con parámetros duplicados.
- Canonical: cada página apunta a sí misma. Sin cadenas canónicas (A→B→C). Siempre apunta a la URL final.
- Sitemap: solo páginas indexables. `<lastmod>` con fecha real. Envía a Search Console tras cada publicación importante.
- Hreflang *(solo si hay versiones en múltiples idiomas)*: incluir siempre la variante `x-default`.

### 13D. E-E-A-T y Helpful Content

Google evalúa cuatro pilares:

| Pilar | Cómo demostrarlo |
|---|---|
| **Experience** | Experiencia propia visible: casos reales, fotos originales, fecha de la experiencia |
| **Expertise** | Bio del autor con credenciales, contenido profundo, fuentes citadas |
| **Authoritativeness** | Menciones externas, consistencia de marca, backlinks de calidad |
| **Trustworthiness** | HTTPS, política de privacidad, aviso legal, NAP verificable, sin dark patterns |

**Trust es el pilar más importante.** Un sitio con alta pericia pero sin confianza es penalizado.

Google premia: contenido creado para personas (no para bots), punto de vista único, autor identificable, fecha de actualización visible, fuentes citadas con enlace.

Google penaliza: contenido generado masivamente sin valor diferencial, IA sin revisión humana, páginas que no responden lo que promete el título, sitios que abarcan demasiados temas sin autoridad demostrada.

**YMYL** (Your Money or Your Life): estándar E-E-A-T máximo en salud, finanzas, legal, seguridad y gobierno. En proyectos YMYL: credenciales del autor visibles + aviso de que el contenido no sustituye asesoramiento profesional. Sin excepciones.

### 13E. Enlazado interno

- Ninguna página huérfana: toda página tiene al menos un enlace entrante.
- Las páginas más importantes reciben más enlaces (header, footer, CTAs).
- Texto ancla descriptivo: "Ver precios de habitaciones", nunca "haz clic aquí".
- Máximo 3 clics desde el inicio para cualquier página importante.
- Enlaza siempre a la URL final. Sin cadenas de redirección internas.

### 13F. Canibalización de keywords

**Definición:** dos o más páginas del mismo sitio compiten por la misma keyword principal → Google no sabe cuál mostrar → las dos pierden posicionamiento.

**Cómo evitarlo:**
- Una keyword objetivo por página. Sin solapamientos entre páginas.
- Si dos páginas tienen la misma intención de búsqueda, unificarlas en una o usar canonical para señalar la principal.
- Si hay versiones similares inevitables (p. ej., `/habitacion-doble` y `/habitacion-doble-vista-mar`): diferencia clara de intención + enlazado interno de la secundaria a la principal.

**Cómo detectarlo:** Google Search Console → Consultas → filtrar por keyword → si aparecen varias URLs para la misma búsqueda, hay canibalización.

---

## 14. GEO — POSICIONAMIENTO EN IAs

GEO (Generative Engine Optimization): optimizar para que ChatGPT, Perplexity, Google AI Overviews y similares encuentren, citen y sinteticen el contenido. Complementa al SEO, no lo reemplaza.

### 14A. Principios

- Las IAs extraen texto plano, no renderizan CSS/JS. El contenido debe ser comprensible en el HTML sin estilos.
- Las IAs favorecen páginas que responden directamente desde el primer párrafo.
- Contenido desactualizado pierde relevancia frente a versiones más recientes.

### 14B. Estructura de contenido para ser citado

| Regla | Cómo aplicarla |
|---|---|
| Respuesta directa al inicio | El primer párrafo de cada sección da la respuesta; luego se amplía |
| Jerarquía H2/H3 clara | Cada sección tiene encabezado descriptivo |
| Párrafos cortos | Máximo ~120 palabras por párrafo |
| Listas y tablas | Para comparaciones, procesos, datos |
| Datos con fuente | Estadísticas con enlace a fuente; aumenta la autoridad |
| Fecha de actualización visible | `<time datetime="2026-06">junio 2026</time>` en el contenido |

### 14C. Implementación técnica

**`llms.txt`** en la raíz (como `robots.txt`, pero para LLMs):
```
# llms.txt — [Nombre del sitio]
## Sobre este sitio
[Descripción de 2–3 frases: qué es y a quién sirve]
## Páginas principales
- [Inicio](https://www.dominio.es/): [qué contiene]
## Contacto
[Email, teléfono si es negocio]
```

`<time datetime="...">` para fechas: permite a las IAs conocer la fecha sin ambigüedad.
Schema `FAQPage` en páginas con preguntas frecuentes (ver apartado 7).
`sitemap.xml` actualizado con `<lastmod>` real.

### 14D. E-E-A-T para IAs

Los datos de 2025 muestran: páginas con señales fuertes de E-E-A-T son 2,3× más citadas en Google AI Overviews. Páginas con encabezados claros, datos con fuentes y atribución de autor tienen 73% más tasa de selección por sistemas RAG. Ver E-E-A-T completo en apartado 13D.

### 14E. Lo que NO funciona con las IAs

- Keyword stuffing.
- `llms.txt` sin contenido de calidad detrás.
- Contenido masivo sin datos reales.
- Contenido relevante oculto en JS que el crawler no lee.

### 14F. Cómo cita cada plataforma

| Plataforma | Cómo cita | Qué prioriza |
|---|---|---|
| Google AI Overviews | Enlace directo | Contenido que ya rankea orgánicamente |
| Perplexity | Inline con enlace → tráfico directo | Datos estructurados, fuentes |
| ChatGPT | Mención de marca sin enlace | Presencia en múltiples fuentes externas |
| Claude / Gemini | Variable | Claridad, estructura, E-E-A-T |

---

## 15. FORMULARIOS

Para sitios estáticos sin backend: **Web3Forms** (hasta 250 envíos/mes gratis).

```html
<form action="https://api.web3forms.com/submit" method="POST">
  <input type="hidden" name="access_key" value="CLAVE_DEL_PROYECTO">
  <input type="hidden" name="redirect"    value="https://www.dominio.es/gracias.html">
  <!-- Honeypot anti-spam -->
  <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" aria-hidden="true">

  <label for="name">Nombre</label>
  <input id="name" type="text" name="name" autocomplete="name" required>

  <label for="email">Email</label>
  <input id="email" type="email" name="email" autocomplete="email" required>

  <label for="message">Mensaje</label>
  <textarea id="message" name="message" required></textarea>

  <!-- RGPD obligatorio -->
  <label>
    <input type="checkbox" required>
    He leído y acepto la <a href="/politica-privacidad.html">política de privacidad</a>
  </label>

  <button type="submit">Enviar consulta</button>
</form>
```

Reglas adicionales: `font-size: 16px` en inputs (evita zoom iOS). Touch targets ≥ 44 × 44 px. La clave de Web3Forms se registra con el email del cliente, no con el tuyo.

---

## 16. BANNER DE COOKIES Y RGPD

### 16A. Categorías de cookies — España (LOPD/RGPD + AEPD)

| Categoría | Requiere consentimiento | Ejemplos |
|---|---|---|
| **Técnicas / necesarias** | No | Sesión, token CSRF, preferencias de accesibilidad, recordar el consentimiento |
| **De preferencias / funcionales** | Sí (salvo excepción) | Idioma elegido por el usuario, personalización no esencial |
| **Analíticas / estadísticas** | Depende (ver nota) | GA4 con IP anonimizada + sin perfilado + 13 meses → exención AEPD |
| **De marketing / publicidad** | Sí, siempre | Retargeting, píxeles sociales (Meta, TikTok), Google Ads |
| **De terceros** | Sí, siempre | Embeds de YouTube, Google Maps con cookies propias |

**Nota exención analítica AEPD:** GA4 puede usarse sin consentimiento previo SOLO si cumple TODAS estas condiciones: first-party (sin compartir con Google para publicidad), IP anonimizada (anonymize_ip + Consent Mode v2 con denied por defecto), sin cross-device tracking, sin remarketing, datos limitados a estadística agregada, retención máxima 13 meses, informado en política de cookies.

### 16B. Reglas del banner

- Aceptar y Rechazar con la **misma jerarquía visual** (mismo tamaño, mismo color). Sin dark patterns.
- El botón "Rechazar" o "Solo necesarias" debe ser igual de prominente que "Aceptar todo".
- Persistencia en `localStorage` (clave: `[siglas-proyecto]-cookies-v1`).
- Solo aparece en la primera visita o si el usuario borra localStorage.
- Enlace a la política de cookies accesible desde el banner.
- Permitir retirar el consentimiento igual de fácil que darlo (icono flotante o link en footer).

### 16C. Implementación con GA4 + Consent Mode v2

GA4 **NUNCA** dispara antes de que el usuario consienta (salvo exención analítica confirmada). Carga el snippet antes de cualquier otra etiqueta de Google:

```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'analytics_storage': 'denied',
    'ad_storage':        'denied',
    'ad_user_data':      'denied',
    'ad_personalization':'denied',
    'wait_for_update':   500
  });
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
```

Cuando el usuario acepta (desde el banner):
```js
gtag('consent', 'update', {
  'analytics_storage': 'granted',
  'ad_storage':        'granted'  // solo si el proyecto usa publicidad
});
```

Verifica en DevTools → Network: sin consentimiento, ninguna petición a `google-analytics.com`.

---

## 17. ESTRUCTURA DE ARCHIVOS

```
/
├── index.html
├── 404.html
├── aviso-legal.html
├── politica-privacidad.html
├── politica-cookies.html
├── gracias.html               ← destino del formulario
├── robots.txt
├── sitemap.xml
├── llms.txt                   ← para crawlers de IAs (ver apartado 14C)
├── .htaccess
├── css/
│   └── style.css              ← único CSS con cascade layers
├── js/
│   └── main.js                ← JS mínimo con defer
├── img/
│   ├── favicon.ico
│   ├── favicon-32.png
│   ├── apple-touch-icon.png
│   ├── og-image.webp          ← 1200 × 630 px (redes sociales no soportan AVIF)
│   ├── og-image.jpg           ← fallback OG
│   ├── hero.avif              ← formato preferido PageSpeed
│   ├── hero.webp              ← fallback
│   └── hero.jpg               ← fallback final
└── fonts/                     ← si se autohospedan fuentes
```

---

## 18. .HTACCESS

```apache
# HTTPS forzado
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# www forzado (ajustar si el proyecto va sin www)
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# 404 personalizada
ErrorDocument 404 /404.html

# Caché larga en activos estáticos
<FilesMatch "\.(avif|webp|jpg|png|svg|ico|css|js|woff2)$">
  Header set Cache-Control "max-age=31536000, public, immutable"
</FilesMatch>

# Compresión Gzip
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json
</IfModule>

# Cabeceras de seguridad
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "geolocation=(), camera=(), microphone=()"
Header always set Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:;"

# Bloquear archivos sensibles
<FilesMatch "\.(env|git|cursorrules|yml|yaml|sql|log|bak|swp)$">
  Require all denied
</FilesMatch>
<FilesMatch "^\.">
  Require all denied
</FilesMatch>

# Sin listado de directorios
Options -Indexes
```

*Ajusta el CSP según los recursos externos del proyecto. No uses `'unsafe-inline'`.*

---

## 19. PRE-DEPLOY — CHECKLIST

| # | Acción |
|---|---|
| 1 | Clave del servicio de formulario registrada y sustituida en HTML |
| 2 | *(Solo negocio local)* Coordenadas GPS verificadas en Google Maps, en JSON-LD |
| 3 | Imágenes reales subidas, comprimidas (squoosh.app), sin placeholders |
| 4 | *(Solo negocio local)* NAP idéntico en footer, JSON-LD y Google Business Profile |
| 5 | Archivos sensibles bloqueados o fuera del webroot |
| 6 | `display_errors=Off` en producción (si hay PHP) |
| 7 | Validación HTML sin errores: [validator.w3.org](https://validator.w3.org) |
| 8 | `llms.txt` creado y accesible en `/llms.txt` |
| 9 | E-E-A-T revisado: autoría identificada, fuentes citadas, fechas visibles |
| 10 | *(Solo YMYL)* Credenciales del autor visibles + aviso de que no sustituye asesoramiento profesional |
| 11 | Ninguna página huérfana: todas tienen al menos un enlace entrante |
| 12 | Canonical correcto en todas las páginas, sin cadenas canónicas |
| 13 | Critical CSS extraído e inlineado en el head |
| 14 | CSS y JS minificados |
| 15 | PageSpeed móvil ≥ 90 en [pagespeed.web.dev](https://pagespeed.web.dev) |
| 16 | Merge a `main` y push al repositorio |

---

## 20. DEPLOY — OPCIONES

**Opción A — cPanel Git Version Control** (recomendada para hosting compartido)
1. cPanel → Git™ Version Control → nuevo repositorio apuntando al repo.
2. Crea `.cpanel.yml` en raíz con las rutas de copia a `public_html`.
3. Pull or Deploy → Deploy HEAD Commit.
4. Activa webhook GitHub → cPanel para auto-deploy en cada push.

**Opción B — GitHub Actions con FTP/SFTP**
Si el hosting no tiene Git Version Control: configura el workflow en `.github/workflows/deploy.yml` con los secrets del servidor.

**Opción C — Vercel / Netlify / Cloudflare Pages**
Para estáticos sin cPanel. `.htaccess` no funciona aquí: traduce las reglas a `vercel.json`, `_headers`+`_redirects` (Netlify) o `_headers` (Cloudflare).

---

## 21. POST-DEPLOY — CHECKLIST

| # | Verificación | Herramienta |
|---|---|---|
| 1 | HTTPS forzado | `http://dominio.es` → 301 a `https://www.` |
| 2 | www forzado | `https://dominio.es` → 301 a `https://www.` |
| 3 | 404 personalizada | Visitar `/ruta-que-no-existe` |
| 4 | robots.txt accesible | `/robots.txt` |
| 5 | sitemap.xml accesible | `/sitemap.xml` |
| 6 | llms.txt accesible | `/llms.txt` |
| 7 | Cabeceras de seguridad | [securityheaders.com](https://securityheaders.com) → A |
| 8 | Mozilla Observatory | [observatory.mozilla.org](https://observatory.mozilla.org) → B mínimo |
| 9 | SSL Labs | [ssllabs.com/ssltest](https://www.ssllabs.com/ssltest) → A |
| 10 | PageSpeed móvil | [pagespeed.web.dev](https://pagespeed.web.dev) → LCP < 2,5 s · INP < 200 ms · CLS < 0,1 · Score ≥ 90 |
| 11 | Rich Results | [search.google.com/test/rich-results](https://search.google.com/test/rich-results) |
| 12 | Mobile-Friendly | [search.google.com/test/mobile-friendly](https://search.google.com/test/mobile-friendly) |
| 13 | Validación HTML | [validator.w3.org](https://validator.w3.org) → sin errores |
| 14 | Formulario | Envío de prueba → email recibido |
| 15 | Banner cookies | Borrar localStorage, recargar → aparece; Aceptar/Rechazar funcionan |
| 16 | Embeds pesados | DevTools Network: cero peticiones a Google Maps / YouTube hasta interacción |
| 17 | Search Console | Añadir propiedad, verificar, enviar `sitemap.xml` |
| 18 | *(Solo negocio local)* Google Business Profile | Actualizar URL, verificar NAP idéntico |

---

## 22. WORKFLOW DE MANTENIMIENTO

```
Editar local → git commit → git push main → auto-deploy → web actualizada
```

- Antes de cada cambio significativo: rama de desarrollo → PR → revisión → merge a `main`.
- Actualiza páginas clave cada 3–6 meses. Las IAs y Google penalizan contenido sin actualización reciente.

---

## 23. GIT WORKFLOW

### 23A. Estructura de ramas

```
main          ← producción; siempre desplegable; nunca commits directos
develop       ← integración; se testea aquí antes de fusionar a main
feature/*     ← una rama por funcionalidad (feature/navbar-mobile)
fix/*         ← correcciones de bug (fix/cls-hero)
hotfix/*      ← urgencias directas sobre main (hotfix/form-broken)
```

Todo cambio a `main` pasa por PR. Nunca comitas directamente a `main`.

### 23B. Conventional Commits

Formato: `tipo(ámbito): descripción breve`

| Tipo | Cuándo |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de bug |
| `perf` | Mejora de rendimiento |
| `style` | Formato sin impacto funcional |
| `refactor` | Reorganización sin cambio de comportamiento |
| `docs` | Solo documentación |
| `chore` | Mantenimiento, dependencias, CI |

Ejemplos:
```
feat(formulario): añadir honeypot anti-spam
fix(hero): corregir CLS por imagen sin width/height
perf(css): extraer critical CSS al head
```

### 23C. .gitignore esencial

```gitignore
.DS_Store
Thumbs.db
*.swp
.env
.env.*
config.local.php
node_modules/
vendor/
dist/
/build
.vscode/
.idea/
*.log
```

### 23D. Flujo por tarea

1. `git checkout develop && git pull`
2. `git checkout -b feature/nombre-descriptivo`
3. Commits convencionales durante el desarrollo
4. `git push -u origin feature/nombre-descriptivo`
5. PR a `develop` → revisar → merge
6. Cuando `develop` está listo: PR `develop` → `main` → deploy

---

## 24. TESTING Y COMPATIBILIDAD

### 24A. Navegadores objetivo (2026)

Soporte: dos últimos lanzamientos estables de Chrome/Edge, Safari (macOS + iOS), Firefox, Samsung Internet. No dar soporte a IE11 ni versiones anteriores a 2023.

### 24B. Checklist de testing manual

- [ ] Flujo completo en Chrome / Edge / Safari / Firefox
- [ ] Flujo completo en iOS Safari (dispositivo físico o BrowserStack)
- [ ] Flujo completo en Android Chrome
- [ ] Formulario: envío → confirmación en pantalla → email recibido
- [ ] Banner de cookies: primera visita aparece; acepta/rechaza persisten tras recarga
- [ ] URL inexistente → 404 personalizada
- [ ] Navegación completa por teclado (Tab, Shift+Tab, Enter, Esc)
- [ ] Sin scroll horizontal en ninguna resolución
- [ ] Imágenes: `alt` presente y descriptivo en todas
- [ ] Throttle "Slow 4G" en DevTools → carga tolerable
- [ ] JS desactivado: contenido principal accesible sin JS

### 24C. Herramientas automatizadas

| Herramienta | Qué mide |
|---|---|
| Lighthouse (DevTools) | PageSpeed, accesibilidad, SEO, PWA |
| axe DevTools (extensión) | Accesibilidad WCAG automática |
| [wave.webaim.org](https://wave.webaim.org) | Accesibilidad visual |
| [validator.w3.org](https://validator.w3.org) | HTML válido |
| [securityheaders.com](https://securityheaders.com) | Cabeceras de seguridad |

### 24D. Lighthouse CI (GitHub Actions)

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on: [push]
jobs:
  lhci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @lhci/cli
      - run: lhci autorun
```

Configura `lighthouserc.js` para bloquear el merge si el score de rendimiento baja de 90.

---

## 25. ANALYTICS — GA4 + GOOGLE SEARCH CONSOLE

### 25A. Principio rector

GA4 **nunca** dispara antes del consentimiento del usuario. Ver implementación completa en apartado 16C (Consent Mode v2).

### 25B. Configuración mínima en GA4

- IP anonimizada: activa por defecto en GA4; no envíes IPs completas vía GTM.
- Desactiva **señales de Google** si no haces remarketing: Admin → Recopilación de datos → Señales de Google.
- Retención de datos: máx. 14 meses (RGPD).
- Si usas Google Tag Manager: configura el contenedor en Consent Mode v2. Ningún tag de marketing activo hasta tener consentimiento.

### 25C. Eventos clave

| Evento | Cuándo disparar |
|---|---|
| `form_submit` | Formulario enviado con éxito |
| `phone_call` | Clic en `tel:` del teléfono |
| `file_download` | Descarga de PDF o recurso |
| `view_promotion` | Visualización de oferta/banner importante |

```js
gtag('event', 'form_submit', {
  'event_category': 'contacto',
  'event_label': 'formulario-home'
});
```

### 25D. Google Search Console

- Añadir propiedad el día del deploy. Verificar con archivo HTML o DNS TXT.
- Enviar `sitemap.xml` inmediatamente tras la verificación.
- *(Solo negocio local)* Vincular Search Console con el perfil de Google Business → mejora los datos de búsqueda local.
- Activa notificaciones por email: Configuración → Notificaciones → todas activas.
- Revisión mensual: Cobertura de índice, Core Web Vitals, Sitemaps, Acciones manuales.
- Alert crítica: caída de cobertura o acción manual → actuar en 24 h.

### 25E. Negocio local — enlace con Google Business Profile

- *(Solo negocio local)* Vincular el sitio web al perfil de Google Business Profile.
- Verificar que la URL en el perfil apunta a `https://www.dominio.es/` (con www, sin slash final).
- NAP idéntico en el perfil, en el JSON-LD y en el footer de la web. Cualquier discrepancia penaliza.
- Publicar actualizaciones en el perfil (novedades, fotos, horarios) → señal positiva para SEO local.

---

## 26. PWA BÁSICO

Implementa PWA si el proyecto requiere uso offline, instalación en pantalla de inicio o notificaciones push. En sitios estáticos simples, manifest.json + service worker básico mejoran el score de Lighthouse sin coste significativo.

### 26A. manifest.json completo

```json
{
  "name": "Nombre completo del negocio",
  "short_name": "Nombre corto",
  "description": "Descripción de 1 frase",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#[color-primary]",
  "lang": "es",
  "icons": [
    { "src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
```

### 26B. Service Worker — estrategia de caché

```js
// /sw.js
const CACHE_NAME = 'v1';
const STATIC_ASSETS = ['/', '/css/style.css', '/js/main.js', '/offline.html'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(STATIC_ASSETS)));
});

self.addEventListener('fetch', e => {
  // HTML: network first, fallback a offline.html
  if (e.request.destination === 'document') {
    e.respondWith(fetch(e.request).catch(() => caches.match('/offline.html')));
    return;
  }
  // Estáticos: cache first, revalida en background
  e.respondWith(
    caches.match(e.request).then(cached => {
      const networkFetch = fetch(e.request).then(res => {
        caches.open(CACHE_NAME).then(c => c.put(e.request, res.clone()));
        return res;
      });
      return cached || networkFetch;
    })
  );
});
```

### 26C. Registro del Service Worker

```js
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => navigator.serviceWorker.register('/sw.js'));
}
```

Crea `/offline.html` con mensaje claro: "Sin conexión. Comprueba tu red e inténtalo de nuevo."

---

## 27. MONITORIZACIÓN Y BACKUPS

### 27A. Core Web Vitals en producción (RUM)

| Herramienta | Qué mide | Frecuencia recomendada |
|---|---|---|
| Google Search Console → Experiencia de página | LCP, INP, CLS de usuarios reales | Mensual |
| [pagespeed.web.dev](https://pagespeed.web.dev) (CrUX) | Percentil 75 de CWV | Tras cada deploy |
| Lighthouse CI (GitHub Actions) | CWV por deploy | Automático en cada push |

Si aparece degradación de CWV: identificar el recurso con Lighthouse → corregir → nuevo deploy.

### 27B. Uptime monitoring

Configura monitorización de disponibilidad desde el primer día:
- **UptimeRobot** (gratuito hasta 50 monitores, check cada 5 min)
- **Freshping** (gratuito, check cada 1 min)

Alerta por email al responsable del proyecto si el sitio cae.

### 27C. Backups

- El repositorio git es el backup del código. Cada cambio: `git commit` + `git push` antes de tocar producción.
- **Base de datos** (si existe): backup automático diario en el hosting. Verifica que está activo. Descarga copia mensual a almacenamiento externo.
- Comprueba que el plan de hosting incluye backups automáticos y durante cuántos días los conserva.
- Mínimo aceptable: repositorio git + backup de BD fuera del servidor.

---

## 28. LEGAL — CONTENIDO MÍNIMO OBLIGATORIO (España)

*Directrices de contenido mínimo. La revisión final por un abogado es responsabilidad del cliente.*

### 28A. Aviso Legal (LSSI art. 10)

- Nombre y apellidos o razón social del titular
- NIF / CIF
- Domicilio
- Email de contacto y teléfono
- Si es empresa: datos de inscripción en el registro mercantil
- Si es profesional colegiado: colegio y número de colegiado

### 28B. Política de Privacidad (RGPD art. 13)

- **Responsable del tratamiento**: nombre, NIF, domicilio, email
- **Finalidades** de cada tratamiento (formulario, newsletter, GA4, etc.)
- **Base jurídica** de cada tratamiento (consentimiento, interés legítimo, contrato)
- **Destinatarios** (p. ej., Google LLC para GA4)
- **Transferencias internacionales** (Google LLC → EE.UU. — indicar base legal: cláusulas contractuales tipo)
- **Plazo de conservación** de los datos
- **Derechos**: acceso, rectificación, supresión, portabilidad, oposición, limitación
- **Derecho a reclamar ante la AEPD** (obligatorio mencionarlo)

### 28C. Política de Cookies (LSSI + RGPD)

- Lista de cookies: nombre, proveedor, finalidad, duración
- Categorías (técnicas, analíticas, marketing)
- Cómo aceptar, rechazar y revocar el consentimiento
- Enlace a las políticas de terceros (Google, Meta, etc.)

### 28D. Aviso YMYL

En salud, finanzas, legal o seguridad, incluir de forma visible en la página:
> "Este contenido tiene carácter informativo y no sustituye el asesoramiento profesional de [médico / asesor financiero / abogado]."

---

## 29. REDIRECTS Y MIGRACIONES

### 29A. 301 vs 302

| Código | Cuándo |
|---|---|
| **301** | Redirección permanente. Transfiere link equity (~99%). Usar en migraciones, URLs canónicas y cambios definitivos. |
| **302** | Redirección temporal. No transfiere link equity. Usar para tests A/B, mantenimiento o páginas estacionales. |

Nunca usar 302 cuando la redirección es permanente. Es el error más habitual en migraciones.

### 29B. Reglas anti-pérdida de posicionamiento

- **Sin cadenas de redirección**: A → B → C pierde rendimiento y link equity. Apunta siempre directo al destino final.
- **Sin bucles**: A → B → A. Detecta con [httpstatus.io](https://httpstatus.io).
- Redirige todas las variantes al canonical: `http://`, `http://www.`, `https://`, `https://www.` → todos a `https://www.dominio.es/`.
- Una URL migrada sin redirección = 404 = pérdida de tráfico y posicionamiento acumulado.

### 29C. Proceso de migración

1. Extrae todas las URLs actuales (Screaming Frog o sitemap).
2. Crea mapa: URL antigua → URL nueva.
3. Implementa en `.htaccess`:
```apache
RewriteRule ^servicios-old/?$ /servicios/ [R=301,L]
RewriteRule ^blog/post-antiguo/?$ /blog/post-nuevo/ [R=301,L]
```
4. Verifica con [httpstatus.io](https://httpstatus.io) que todas devuelven 301 (no cadenas).
5. Envía el nuevo `sitemap.xml` a Search Console el día del lanzamiento.
6. Monitoriza Search Console 30 días: errores 404 no mapeados → añadir redirección.

No elimines los redirects antes de 6 meses: los backlinks externos siguen llegando a las URLs antiguas.

---

## 30. WEB MÓVIL — DIRECTRICES ESPECÍFICAS

> Google indexa mobile-first desde 2019. El rendimiento y la usabilidad en móvil determinan el posicionamiento para TODOS los usuarios. Trata el móvil como el contexto principal, no como un ajuste posterior.

### 30A. Viewport — configuración obligatoria

```html
<!-- Nunca omitir. Nunca añadir user-scalable=no. -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Nunca `user-scalable=no` ni `maximum-scale=1`.** El usuario tiene derecho a hacer zoom. Es una violación de WCAG 1.4.4 y Google la penaliza en la evaluación de Mobile Friendliness.

### 30B. Layout móvil — reglas base

```css
/* Reset móvil obligatorio */
img, video, iframe, svg { max-width: 100%; height: auto; }
* { box-sizing: border-box; }

/* Contenedor centrado: nunca ancho fijo sin fallback */
.container {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding-inline: var(--space-md);
}

/* Viewport height en iOS: la toolbar de Safari reduce el 100vh */
.full-height {
  min-height: 100vh;
  min-height: 100svh; /* svh = sin barra del navegador */
}

/* Evita scroll horizontal involuntario */
body { overflow-x: hidden; }  /* solo si hay una causa verificada */
/* Mejor solución: encontrar el elemento que desborda y corregirlo */
```

**Detectar el elemento que causa scroll horizontal:** abre DevTools → Console → `document.querySelectorAll('*').forEach(el => { if (el.offsetWidth > document.documentElement.offsetWidth) console.log(el); })`

### 30C. Touch — targets y feedback

```css
/* Mínimo táctil: 44×44 px (Apple) / 48×48 px (Material Design) */
.btn, a, button, [role="button"] {
  min-height: 44px;
  min-width: 44px;
  padding: var(--space-sm) var(--space-md);
}

/* Elimina el delay de 300 ms por detección de double-tap */
button, a { touch-action: manipulation; }

/* Feedback táctil visible */
button:active, a:active { opacity: 0.75; }

/* Espaciado entre targets adyacentes */
.nav-list li + li { margin-top: 8px; }
```

Nunca uses `:hover` como único feedback. En táctil no hay hover. Toda interacción que depende de hover debe tener alternativa con click/tap o `:focus`.

### 30D. iOS Safari — correcciones específicas

```css
/* 1. Inputs: evita zoom automático de iOS (ocurre si font-size < 16px) */
input, select, textarea { font-size: 16px; } /* mínimo absoluto */

/* 2. Notch y Dynamic Island: safe area */
body {
  padding-top: env(safe-area-inset-top);
  padding-right: env(safe-area-inset-right);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
}
/* O solo en el footer/header si el body no necesita padding */
.header { padding-top: max(1rem, env(safe-area-inset-top)); }
.footer { padding-bottom: max(1rem, env(safe-area-inset-bottom)); }

/* 3. Scroll bounce en modales/overlays */
.modal-body { overscroll-behavior: contain; }

/* 4. position: sticky en iOS — el offset es obligatorio */
.header-sticky { position: sticky; top: 0; } /* sin top: 0 no funciona */

/* 5. Formularios en iOS — reestilizar si quitas la apariencia nativa */
select { -webkit-appearance: none; background-image: url("arrow.svg"); }
```

```html
<!-- Vídeo en iOS: autoplay requiere muted + playsinline -->
<video autoplay muted playsinline loop>
  <source src="/video/hero.mp4" type="video/mp4">
</video>
```

### 30E. Formularios en móvil

```html
<!-- Teclado correcto por tipo de dato -->
<input type="email" autocomplete="email">       <!-- teclado con @ -->
<input type="tel"   autocomplete="tel">         <!-- teclado numérico -->
<input type="number" inputmode="numeric">       <!-- sin flechas de incremento -->
<input type="text"  inputmode="numeric" pattern="[0-9]{5}"> <!-- código postal -->
<input type="date">                             <!-- picker nativo del SO -->
<input type="search" inputmode="search">        <!-- tecla "Buscar" en lugar de "Intro" -->
```

El `<select>` nativo tiene mejor UX táctil en iOS/Android que cualquier componente JS personalizado. No lo sustituyas salvo que haya un requisito funcional que el nativo no cubre.

### 30F. Imágenes responsivas — tamaños por breakpoint

```html
<picture>
  <!-- AVIF > WebP > JPG, con srcset por breakpoint -->
  <source type="image/avif"
    srcset="/img/hero-400.avif 400w, /img/hero-800.avif 800w, /img/hero-1200.avif 1200w"
    sizes="(max-width: 600px) 100vw, (max-width: 900px) 80vw, 1200px">
  <source type="image/webp"
    srcset="/img/hero-400.webp 400w, /img/hero-800.webp 800w, /img/hero-1200.webp 1200w"
    sizes="(max-width: 600px) 100vw, (max-width: 900px) 80vw, 1200px">
  <img src="/img/hero-1200.jpg"
    srcset="/img/hero-400.jpg 400w, /img/hero-800.jpg 800w, /img/hero-1200.jpg 1200w"
    sizes="(max-width: 600px) 100vw, (max-width: 900px) 80vw, 1200px"
    alt="..." width="1200" height="630" loading="eager" fetchpriority="high">
</picture>
```

Objetivo de peso por imagen en móvil: hero < 80 KB (AVIF), imágenes de contenido < 40 KB.

### 30G. Rendimiento móvil — objetivos y pruebas

| Métrica | Objetivo móvil | Herramienta |
|---|---|---|
| LCP | < 2,5 s en 4G | Lighthouse modo móvil |
| INP | < 200 ms | DevTools → Performance |
| CLS | < 0,1 | Lighthouse |
| JS total parseado | < 200 KB | DevTools → Coverage |
| Peticiones HTTP iniciales | < 30 | DevTools → Network |
| Peso total de la página | < 1 MB | PageSpeed Insights |

**Cómo simular móvil en DevTools:**
1. Network → Throttling → "Slow 4G"
2. Performance → CPU → "4x slowdown"
3. Lighthouse → Device → Mobile

### 30H. Navegación en móvil

```html
<!-- Hamburgesa accesible: aria-expanded refleja el estado -->
<button class="menu-toggle" aria-label="Abrir menú" aria-expanded="false"
        aria-controls="nav-main" type="button">
  <span class="hamburger-icon" aria-hidden="true"></span>
</button>
<nav id="nav-main" hidden>
  <!-- items de navegación -->
</nav>
```

```js
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#nav-main');
toggle.addEventListener('click', () => {
  const isOpen = toggle.getAttribute('aria-expanded') === 'true';
  toggle.setAttribute('aria-expanded', String(!isOpen));
  nav.hidden = isOpen;
  document.body.style.overflow = isOpen ? '' : 'hidden'; // bloquea scroll del body
});
// Cerrar con Esc
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && !nav.hidden) toggle.click();
});
```

### 30I. Checklist móvil antes del deploy

- [ ] `<meta name="viewport">` presente, sin `user-scalable=no`
- [ ] Sin scroll horizontal en ningún breakpoint (probar con DevTools a 320 px, 360 px, 390 px)
- [ ] Todos los touch targets ≥ 44 × 44 px
- [ ] `font-size ≥ 16px` en todos los campos de formulario
- [ ] Vídeos con `muted` + `playsinline` si tienen `autoplay`
- [ ] Safe areas configuradas (`env(safe-area-inset-*)`)
- [ ] LCP < 2,5 s en Lighthouse modo móvil (Slow 4G)
- [ ] Flujo completo probado en iPhone físico (Safari) y Android Chrome
- [ ] Navegación completa accesible con el dedo sin zoom
- [ ] Menú hamburguesa con `aria-expanded` y cierre con Esc
- [ ] Imágenes con `srcset` y `sizes` para tamaños móvil

---

*Este documento es ley en el proyecto. Si algo de lo que te piden contradice estas directrices: PARA y PREGUNTA.*
