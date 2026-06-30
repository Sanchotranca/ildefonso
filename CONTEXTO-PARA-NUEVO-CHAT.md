# CONTEXTO PARA NUEVO CHAT — Residencia San Ildefonso UAH
**Última actualización:** 2026-06-30
**Estado:** listo para deploy en cuanto se ejecuten 5 acciones del usuario

---

## PROYECTO

- **Web estática** institucional para Residencia Universitaria San Ildefonso (UAH).
- **Gestor:** CRUSA (Ciudad Residencial Universitaria de Alcalá), CIF A-80991714.
- **Dominio previsto:** https://www.residenciasanildefonso.es
- **Hosting:** Webempresa (Apache shared, PHP activo).
- **Estándar aplicado:** ELIAWEB_STANDARDS_v4 (§11 a §25).

### Carpeta local (Windows)
```
C:\Users\David\OneDrive\Escritorio\ildefonso-claude-create-residencia-website-pP3AP\
```

---

## ESTRUCTURA DE ARCHIVOS

```
/
├── index.html                  ← Inicio (con intro informativa + CTA "Reservar habitación")
├── residencia.html             ← Historia, ubicación, instalaciones (CTA reservar)
├── contacto.html               ← redirect estático a contacto.php
├── contacto.php                ← Formulario real (CSRF + captcha + honeypot + RGPD)
├── enviar.php                  ← Procesa form (header-injection-proof, From noreply@)
├── habitaciones.html           ← OCULTA: noindex, fuera de sitemap, fuera de nav
├── servicios.html              ← OCULTA: noindex, fuera de sitemap, fuera de nav
├── aviso-legal.html
├── politica-privacidad.html    ← Web3Forms eliminado, refleja enviar.php propio
├── politica-cookies.html       ← Lista cookie técnica rsi-cookies-v1
├── gracias.html                ← noindex, follow
├── 404.html
├── robots.txt                  ← Permite explícitamente bots IA (GPT, Claude, Perplexity, etc.)
├── sitemap.xml                 ← 6 URLs indexables (sin gracias/404/habitaciones/servicios)
├── llms.txt                    ← Limpio: sin "41 habitaciones", sin precios mensuales
├── .htaccess                   ← HTTPS+www forzados, CSP estricta, bloqueo archivos sensibles
├── .gitignore                  ← Cubre §23C ELIAWEB + extras (.min generados no se versionan)
├── manifest.json
├── BUILD-PROD.ps1              ← Script para minificar + apuntar HTML a .min antes del deploy
├── BORRAR-IMG-HUERFANAS.ps1    ← Borra 34 imgs huérfanas (43 MB) sin tocar og-image.jpg
├── DEPLOY.md, README.md, ELIAWEB_*.md  ← documentación
├── css/style.css               ← Cascade layers, ~1150 líneas, sin minificar
├── js/main.js                  ← Validación blur ES, spinner submit, revocar cookies, ~140 líneas
└── img/                        ← 61 imágenes (43 MB huérfanas pendientes borrar)
```

---

## ESTADO ACTUAL — HECHO Y VERIFICADO

### Seguridad (§11 + §16 + §18)
- ✅ Header injection arreglado en `enviar.php` (`limpiar()` elimina CR/LF)
- ✅ From SMTP = `noreply@residenciasanildefonso.es` (SPF/DKIM-conforme)
- ✅ CSRF + captcha matemático + honeypot + RGPD opt-in
- ✅ `.htaccess`: HTTPS, www, HSTS, CSP, X-Frame, X-Content-Type, Referrer-Policy, Permissions-Policy, COOP. Bloqueo de `.git`, `.cursorrules`, `.swp`, `.env`, archivos ocultos `^\.`, `/scripts/`, `/contenido-backup/`
- ✅ `display_errors=Off`, `log_errors=On`
- ✅ Cookies AEPD: misma jerarquía Aceptar/Rechazar, sin pre-marcadas, política lista `rsi-cookies-v1`, link "Configurar cookies" en footer para revocar

### Accesibilidad WCAG 2.1 AA (§11)
- ✅ Contrastes verificados: 25/25 combinaciones pasan AA, mayoría AAA
  - `btn--accent` reforzado con `--color-accent-strong #0058AD` (7.00:1 AAA)
  - breadcrumb activo en `#fff + font-weight 600` (9.50:1 AAA)
  - error form: 9.66:1 AAA
- ✅ Skip link, focus-visible, prefers-reduced-motion, h1 único, labels asociados
- ✅ Touch targets ≥44px, font-size 16px inputs (no zoom iOS)

### SEO + GEO (§13 + §14)
- ✅ Titles únicos ≤60 chars, descriptions únicas, canonicales correctos
- ✅ OG 1200×630 en todas, NAP idéntico en 6 footers
- ✅ Schema LodgingBusiness + BreadcrumbList + FAQPage + Article + TouristAttraction
- ✅ `<time datetime="2026-06">junio 2026</time>` en 8 footers activos
- ✅ Intro informativa post-hero en index (respuesta directa para IAs)
- ✅ llms.txt sin datos inventados (sin "41 habitaciones", sin precios mensuales)
- ✅ robots.txt permite explícitamente GPTBot, ClaudeBot, PerplexityBot, etc.

### UX (§12 + §15)
- ✅ Topbar tel/email visible SIEMPRE (sin abrir hamburger móvil)
- ✅ Nav unificado a `href="/"` en 9 archivos
- ✅ CTA "Reservar habitación" en index y residencia
- ✅ Form: validación blur con `setCustomValidity` ES, spinner "Enviando…", botón "Cancelar" (`type="reset"`), mensajes de error específicos al volver de `enviar.php?error=`
- ✅ Microcopy CTAs verbo+objeto, sin dark patterns

---

## PENDIENTES — REQUIEREN ACCIÓN DE DAVID

| # | Acción | Por qué |
|---|---|---|
| 1 | Ejecutar `BUILD-PROD.ps1` en PowerShell | Minifica CSS/JS + apunta HTML a .min. §19 #14 pre-deploy. |
| 2 | Ejecutar `BORRAR-IMG-HUERFANAS.ps1` | Libera 43 MB. Lista validada (excluye og-image.jpg). |
| 3 | Crear cuenta `noreply@residenciasanildefonso.es` en Webempresa cPanel | Sin ella, `enviar.php` falla en producción. |
| 4 | Confirmar precios reales POR NOCHE (individual y doble) | Para reponer Schema `makesOffer`. Quitados por anti-invención. |
| 5 | Credenciales FTP/SFTP Webempresa + subir | Deploy. |
| 6 | (Más adelante) ID GA4 `G-XXXXXXXXXX` | Añadir snippet con Consent Mode v2. NO se ha tocado. |

---

## DECISIONES CLAVE TOMADAS (no reabrir)

- **Precios:** son **POR NOCHE**, no por mes. Los números exactos los confirmará David más tarde. Mientras tanto: Schema `makesOffer` y `priceRange` quitados; llms.txt dice "consultar". FAQ visible mantiene 35/45 €/noche provisional.
- **Habitaciones:** "Pocas habitaciones" (anti-invención). El número 41 fue quitado de todo el código activo. Aún aparece en habitaciones.html y servicios.html (ocultas) — se revisará si se activan.
- **`habitaciones.html` y `servicios.html`:** OCULTAS. Mantienen archivo + noindex/nofollow + fuera de sitemap + sin enlace entrante. David lo llama "producto mínimo para publicar".
- **og-image.jpg:** se MANTIENE (fallback OG exigido por §17). NO incluido en .ps1 de borrado.
- **Nav unificado a `href="/"`** (no `index.html`).
- **CTA principal:** "Reservar habitación" en index y residencia, ambos → contacto.php.
- **CSP `'unsafe-inline'`** en style-src: aceptado por critical CSS inline, documentado en .htaccess líneas 87-93.

---

## QUIRKS TÉCNICOS DESCUBIERTOS (importantes para el siguiente chat)

- **OneDrive lag con bash sandbox:** los comandos bash leen versiones STALE de archivos editados con Edit tool. Solución: usar Read tool (filesystem real) para verificar contenido real.
- **bash NO tiene permisos de borrado** sobre la carpeta OneDrive (Operation not permitted). Por eso se generó `BORRAR-IMG-HUERFANAS.ps1` para ejecución manual.
- **Minificación NO se puede hacer en sandbox** por mismo motivo. Por eso `BUILD-PROD.ps1` corre en Windows con node/npm reales.

---

## IDs DRIVE RELEVANTES

```
Sistema-MOODY:                   1UizQXJcm735W99urFSaPOBV7Tm5dwo-7
EXONEOCÓRTEX:                    1ueVooS49hFbHIawT4LSPhUmrLUUo-gtN
/Trabajo (subcarpeta proyectos): 10ogdbRyMb_nNwe93WulhtLshDDjvJyQ5
ESTADO & MEMORIA actual:         1FIH8zQb9OrK9SVC6lw362x95m71-39YdXM2vF-iMlpo
NORMAS DEL BRAZO v1:             1TQf1ME5VoE7FwlDMYQn3HfNhgtdwNT4g-H9JwAnosfM
ELIAWEB STANDARDS v4:            1lGwJuhPjbOiffZJWssx66Q1hLVit78rSnTDXVGcH3YU
ELIAWEB RESTRICTIONS:            1GMbo5wPbSD5K_9e3BDK9Ewb2M1GY5CAeYy8gK1Ah2bY
```

---

## CÓMO RETOMAR EN EL NUEVO CHAT

1. **Pegar este documento** al inicio del chat nuevo.
2. **Pedir a Claude que lea** ESTADO & MEMORIA en Drive (Sistema-MOODY) según norma operativa.
3. **Conectar la carpeta del proyecto:**
   ```
   C:\Users\David\OneDrive\Escritorio\ildefonso-claude-create-residencia-website-pP3AP
   ```
4. **Decir qué quieres hacer:**
   - Confirmar precios y reponer Schema makesOffer (acción 4)
   - Ayudar con FTP/deploy (acción 5)
   - Configurar GA4 (acción 6, cuando tengas el ID)
   - Reactivar habitaciones.html / servicios.html (cuando estén listas)
   - Cualquier ajuste de copy o estructura

---

## NORMAS DE TRABAJO (David — TDAH, micro-pasos)

- Español siempre.
- Dato sin fuente verificable = no existe. "No lo sé" es obligatorio cuando no se sabe.
- Nunca borrar/mover/renombrar/publicar sin lista exacta + OK explícito.
- Si algo falla: PARAR. Describir. Esperar instrucción. No improvisar.
- bash sandbox lee versiones stale de archivos editados — verificar con Read tool.
- Al terminar: reportar qué se hizo, dónde está, qué no se hizo.
- Objetivo de fondo: ingresos para proceso legal de custodia de su hija Lía.
