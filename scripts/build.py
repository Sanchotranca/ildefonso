#!/usr/bin/env python3
"""Generador estático de páginas para residenciasanildefonso.es"""
import os
import json as _json
from textwrap import dedent

ROOT = "/home/user/ildefonso"
SITE_URL = "https://www.residenciasanildefonso.es"
SITE_NAME = "Residencia Universitaria San Ildefonso"
PHONE_RAW = "+34918788146"
PHONE_FMT = "+34 91 878 81 46"
EMAIL = "sanildefonso@crusa.es"
ADDR_STREET = "Plaza San Diego, s/n"
ADDR_LOCALITY = "Alcalá de Henares"
ADDR_REGION = "Madrid"
ADDR_POSTAL = "28801"
ADDR_COUNTRY = "ES"
GEO_LAT = "40.482236"
GEO_LON = "-3.363976"

# Páginas: slug -> (title, description, nav-key)
PAGES = {
    "index":               ("Residencia universitaria San Ildefonso · Alcalá de Henares",
                            "Residencia universitaria San Ildefonso en Alcalá de Henares: alojamiento, manutención y vida en el Colegio de San Ildefonso, Patrimonio de la Humanidad.",
                            "inicio"),
    "residencia":          ("La Residencia — Residencia San Ildefonso | Alcalá de Henares",
                            "Historia, ubicación e instalaciones de la Residencia Universitaria San Ildefonso, en el Patio de los Filósofos del histórico Colegio de San Ildefonso (UAH).",
                            "residencia"),
    "habitaciones":        ("Habitaciones y tarifas — Residencia San Ildefonso | Alcalá de Henares",
                            "Habitaciones individuales y dobles con baño privado, calefacción y wifi. Tarifas con pensión completa o media en la Residencia San Ildefonso de Alcalá.",
                            "habitaciones"),
    "servicios":           ("Servicios — Residencia San Ildefonso | Alcalá de Henares",
                            "Servicios de la Residencia San Ildefonso: comedor, biblioteca, salas de estudio, wifi, lavandería, conserjería 24 h y vida cultural y deportiva.",
                            "servicios"),
    "contacto":            ("Contacto y solicitud — Residencia San Ildefonso | Alcalá",
                            "Contacta con la Residencia San Ildefonso de Alcalá de Henares: dirección, teléfono, email y formulario para solicitar plaza o reservar visita.",
                            "contacto"),
    "gracias":             ("Mensaje recibido — Residencia San Ildefonso",
                            "Hemos recibido tu mensaje. Te responderemos en un plazo máximo de 48 horas laborables.",
                            ""),
    "404":                 ("Página no encontrada — Residencia San Ildefonso",
                            "La página que buscas no existe o se ha movido. Vuelve al inicio para seguir explorando la Residencia San Ildefonso.",
                            ""),
    "aviso-legal":         ("Aviso legal — Residencia San Ildefonso",
                            "Aviso legal del sitio web de la Residencia Universitaria San Ildefonso, gestionada por CRUSA, Universidad de Alcalá.",
                            ""),
    "politica-privacidad": ("Política de privacidad — Residencia San Ildefonso",
                            "Información sobre el tratamiento de datos personales conforme al RGPD y la LOPDGDD en residenciasanildefonso.es.",
                            ""),
    "politica-cookies":    ("Política de cookies — Residencia San Ildefonso",
                            "Información sobre las cookies utilizadas en residenciasanildefonso.es y cómo configurarlas.",
                            ""),
}

NAV = [
    ("inicio",        "/",                  "Inicio"),
    ("residencia",    "/residencia.html",   "La Residencia"),
    ("habitaciones",  "/habitaciones.html", "Habitaciones"),
    ("servicios",     "/servicios.html",    "Servicios"),
    ("contacto",      "/contacto.html",     "Contacto"),
]

def head(slug, title, description, extra_jsonld=""):
    canonical = SITE_URL + ("/" if slug == "index" else f"/{slug}.html")
    og_image = f"{SITE_URL}/img/og-image.webp"
    # Páginas que no deben indexarse en buscadores
    is_noindex = slug in ("404", "gracias")
    robots = "noindex, follow" if is_noindex else "index, follow"
    # Preload del hero solo donde se usa (index — fondo CSS del .hero)
    hero_preload = (
        '<link rel="preload" as="image" href="/img/hero.webp" fetchpriority="high" type="image/webp">'
        if slug == "index" else ""
    )
    # En páginas noindex (404, gracias) NO emitir JSON-LD: no aporta SEO
    # y solo añade ~700 bytes por página. Las páginas indexables sí lo llevan.
    if is_noindex:
        jsonld_block = ""
    else:
        base_jsonld = """{
  "@context": "https://schema.org",
  "@type": "LodgingBusiness",
  "@id": "%(site)s#residencia",
  "name": "%(name)s",
  "url": "%(site)s",
  "telephone": "%(phone)s",
  "email": "%(email)s",
  "taxID": "A-80991714",
  "image": "%(img)s",
  "priceRange": "270–995 €/mes",
  "currenciesAccepted": "EUR",
  "paymentAccepted": "Transferencia bancaria, Tarjeta",
  "numberOfRooms": 41,
  "petsAllowed": false,
  "smokingAllowed": false,
  "amenityFeature": [
    {"@type": "LocationFeatureSpecification", "name": "Wifi gratuito", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Comedor / pensión completa", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Biblioteca y salas de estudio", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Conserjería 24 horas", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Limpieza y lavandería", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Calefacción", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Baño privado en habitación", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Televisión y aire acondicionado", "value": true}
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "%(street)s",
    "addressLocality": "%(loc)s",
    "addressRegion": "%(reg)s",
    "postalCode": "%(pc)s",
    "addressCountry": "%(cc)s"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "%(lat)s", "longitude": "%(lon)s" },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00", "closes": "19:00"
  }],
  "makesOffer": [
    {"@type": "Offer", "name": "Habitación individual", "price": "365", "priceCurrency": "EUR", "priceSpecification": {"@type": "UnitPriceSpecification", "price": "365", "priceCurrency": "EUR", "unitText": "MES"}, "availability": "https://schema.org/InStock"},
    {"@type": "Offer", "name": "Habitación doble (por persona)", "price": "270", "priceCurrency": "EUR", "priceSpecification": {"@type": "UnitPriceSpecification", "price": "270", "priceCurrency": "EUR", "unitText": "MES"}, "availability": "https://schema.org/InStock"}
  ],
  "sameAs": ["https://crusa.es/", "https://www.uah.es/"]
}""" % {
            "site": SITE_URL, "name": SITE_NAME, "phone": PHONE_FMT, "email": EMAIL,
            "img": og_image, "street": ADDR_STREET, "loc": ADDR_LOCALITY, "reg": ADDR_REGION,
            "pc": ADDR_POSTAL, "cc": ADDR_COUNTRY, "lat": GEO_LAT, "lon": GEO_LON,
        }
        jsonld_block = f'<script type="application/ld+json">{base_jsonld}</script>'
        if extra_jsonld:
            jsonld_block += f'\n  <script type="application/ld+json">{extra_jsonld}</script>'

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="#9b1c1c">
  <link rel="canonical" href="{canonical}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Meta geo (Bing, Yandex y bots no-Google) -->
  <meta name="geo.region" content="ES-MD">
  <meta name="geo.placename" content="Alcalá de Henares, Madrid">
  <meta name="geo.position" content="{GEO_LAT};{GEO_LON}">
  <meta name="ICBM" content="{GEO_LAT}, {GEO_LON}">

  <link rel="icon" href="/img/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="/img/crest.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&amp;family=Source+Sans+3:wght@400;600;700&amp;display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&amp;family=Source+Sans+3:wght@400;600;700&amp;display=swap">

  <link rel="stylesheet" href="/css/style.css">

  {hero_preload}

  {jsonld_block}
</head>
<body>
  <a class="skip-link" href="#main">Saltar al contenido principal</a>
"""

def topbar():
    return f"""
  <div class="topbar" role="complementary" aria-label="Información de contacto">
    <div class="container topbar__inner">
      <ul class="topbar__links">
        <li><a href="/residencia.html">La Residencia</a></li>
        <li><a href="/contacto.html">Solicitud de plaza</a></li>
        <li><a href="https://crusa.es/" rel="noopener noreferrer external">CRUSA</a></li>
      </ul>
      <div class="topbar__contact">
        <span><a href="tel:{PHONE_RAW}" aria-label="Llamar al teléfono">📞 {PHONE_FMT}</a></span>
        <span><a href="mailto:{EMAIL}">✉ {EMAIL}</a></span>
      </div>
    </div>
  </div>
"""

def header(active):
    items = []
    for key, href, label in NAV:
        attr = ' aria-current="page"' if key == active else ''
        items.append(f'<li><a class="main-nav__link" href="{href}"{attr}>{label}</a></li>')
    nav_html = "\n          ".join(items)
    return f"""
  <header class="site-header" role="banner">
    <div class="container site-header__inner">
      <a href="/" class="brand" aria-label="Inicio – {SITE_NAME}">
        <img src="/img/crest.svg" alt="" class="brand__crest" width="56" height="56" fetchpriority="high">
        <span class="brand__text">
          <span class="brand__title">Residencia Universitaria<br>San Ildefonso</span>
          <span class="brand__subtitle">Alcalá de Henares</span>
        </span>
      </a>
      <button class="nav-toggle" type="button" aria-controls="primary-nav" aria-expanded="false" aria-label="Abrir menú de navegación">
        <span class="nav-toggle__bar"></span>
        <span class="nav-toggle__bar"></span>
        <span class="nav-toggle__bar"></span>
      </button>
      <nav id="primary-nav" class="main-nav" aria-label="Navegación principal">
        <ul class="main-nav__list">
          {nav_html}
        </ul>
      </nav>
    </div>
  </header>
"""

def breadcrumb(items):
    """items: list of (label, href|None)"""
    lis = []
    for i, (lbl, href) in enumerate(items):
        if href and i < len(items) - 1:
            lis.append(f'<li><a href="{href}">{lbl}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{lbl}</li>')
    return f"""
        <nav class="breadcrumb" aria-label="Migas de pan">
          <ol>
            {"".join(lis)}
          </ol>
        </nav>
"""

def footer():
    return f"""
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div>
          <h3>{SITE_NAME}</h3>
          <p>{ADDR_STREET}<br>{ADDR_POSTAL} {ADDR_LOCALITY}<br>{ADDR_REGION} · España</p>
          <p>
            <a href="tel:{PHONE_RAW}">{PHONE_FMT}</a><br>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </p>
        </div>
        <div>
          <h3>La Residencia</h3>
          <ul>
            <li><a href="/residencia.html">Historia y ubicación</a></li>
            <li><a href="/residencia.html#instalaciones">Instalaciones</a></li>
            <li><a href="/habitaciones.html">Habitaciones</a></li>
            <li><a href="/servicios.html">Servicios</a></li>
          </ul>
        </div>
        <div>
          <h3>Información</h3>
          <ul>
            <li><a href="/contacto.html#solicitud">Solicitud de plaza</a></li>
            <li><a href="/habitaciones.html#tarifas">Tarifas</a></li>
            <li><a href="/contacto.html">Contacto</a></li>
            <li><a href="/contacto.html#faq">Preguntas frecuentes</a></li>
          </ul>
        </div>
        <div>
          <h3>Grupo CRUSA</h3>
          <ul>
            <li><a href="https://crusa.es/" rel="noopener noreferrer external">CRUSA · Campus Village</a></li>
            <li><a href="https://portacoeli.es/" rel="noopener noreferrer external">Hospedería Porta Coeli</a></li>
            <li><a href="https://www.uah.es/" rel="noopener noreferrer external">Universidad de Alcalá</a></li>
            <li><a href="https://www.fgua.es/" rel="noopener noreferrer external">Fundación General UAH</a></li>
          </ul>
        </div>
      </div>
      <div class="site-footer__bottom">
        <span>© 2026 {SITE_NAME}. Gestionada por CRUSA · Universidad de Alcalá.</span>
        <nav class="footer-legal" aria-label="Legal">
          <a href="/aviso-legal.html">Aviso legal</a>
          <a href="/politica-privacidad.html">Privacidad</a>
          <a href="/politica-cookies.html">Cookies</a>
        </nav>
      </div>
    </div>
  </footer>

  <aside id="cookies" class="cookies" role="region" aria-label="Aviso de cookies" hidden>
    <div class="cookies__inner">
      <p>Usamos cookies técnicas necesarias para el funcionamiento del sitio. No usamos cookies de seguimiento ni publicidad. Más información en nuestra <a href="/politica-cookies.html">política de cookies</a>.</p>
      <div class="cookies__actions">
        <button class="btn btn--accent" type="button" id="cookies-accept">Aceptar</button>
        <button class="btn btn--ghost" type="button" id="cookies-reject">Rechazar</button>
      </div>
    </div>
  </aside>

  <script src="/js/main.js" defer></script>
</body>
</html>
"""

def breadcrumb_jsonld(items):
    """items: lista de (label, url_relativa) — última url se ignora (current page)"""
    elements = []
    for i, (label, url) in enumerate(items, 1):
        el = {
            "@type": "ListItem",
            "position": i,
            "name": label,
        }
        if url:
            el["item"] = SITE_URL + url
        elements.append(el)
    import json as _json
    return _json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }, ensure_ascii=False)

def page(slug, body, extra_jsonld=""):
    title, desc, nav_key = PAGES[slug]
    html = head(slug, title, desc, extra_jsonld) + topbar() + header(nav_key) + body + footer()
    fname = f"index.html" if slug == "index" else f"{slug}.html"
    open(os.path.join(ROOT, fname), "w").write(html)
    print(f"✓ {fname}")

# =============== Páginas ===============

# ---------- INDEX ----------
INDEX_BODY = f"""
  <main id="main">
    <section class="hero" aria-labelledby="hero-title">
      <div class="container hero__inner">
        <div>
          <span class="hero__eyebrow">Alojamiento universitario · Alcalá de Henares</span>
          <h1 class="hero__title" id="hero-title">Vivir, estudiar y crecer en el Colegio de San Ildefonso</h1>
          <p class="hero__lead">
            La Residencia San Ildefonso, gestionada por CRUSA en el corazón
            histórico de Alcalá de Henares, ofrece alojamiento universitario
            con habitaciones de baño privado, comedor propio y servicios 24 h
            en un edificio Patrimonio de la Humanidad.
          </p>
          <div class="hero__actions">
            <a class="btn btn--accent btn--lg" href="/contacto.html#solicitud">Solicitar plaza</a>
            <a class="btn btn--ghost btn--lg" href="/residencia.html">Conocer la Residencia</a>
          </div>
        </div>
        <aside class="hero__card" aria-label="Datos de contacto rápido">
          <h2>Contacto rápido</h2>
          <ul>
            <li><strong>Dirección</strong> · {ADDR_STREET}, {ADDR_LOCALITY}</li>
            <li><strong>Teléfono</strong> · <a href="tel:{PHONE_RAW}">{PHONE_FMT}</a></li>
            <li><strong>Email</strong> · <a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <a class="btn btn--primary" href="/contacto.html#solicitud">Reservar plaza</a>
        </aside>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="accesos-title">
      <div class="container">
        <h2 class="section__title" id="accesos-title">Acceso rápido</h2>
        <div class="grid grid--4">
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">①</div>
            <h3 class="feature__title">Solicitud de plaza</h3>
            <p class="feature__text">Solicita tu habitación para el próximo curso académico.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">②</div>
            <h3 class="feature__title">Tarifas</h3>
            <p class="feature__text">Consulta los precios mensuales y los regímenes de pensión.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">③</div>
            <h3 class="feature__title">Servicios</h3>
            <p class="feature__text">Comedor, lavandería, wifi, conserjería 24 h y mucho más.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">④</div>
            <h3 class="feature__title">Cómo llegar</h3>
            <p class="feature__text">A 5 min andando de la estación de Cercanías de Alcalá.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="sobre-title">
      <div class="container">
        <h2 class="section__title" id="sobre-title">Una residencia con cinco siglos de historia</h2>
        <div class="grid grid--2">
          <div>
            <p>
              La Residencia San Ildefonso se aloja en el <strong>Colegio Mayor
              de San Ildefonso</strong>, fundado por el Cardenal Cisneros en
              1499 como núcleo originario de la Universidad de Alcalá y
              declarado <a href="https://whc.unesco.org/es/list/876" rel="noopener noreferrer external">Patrimonio de la Humanidad</a> por la UNESCO en 1998.
            </p>
            <p>
              Situada en el <strong>Patio de los Filósofos</strong> de la
              manzana cisneriana, ofrece alojamiento a estudiantes
              universitarios en un entorno único, a pocos minutos andando del
              campus, la estación de Cercanías y el casco histórico.
            </p>
            <p>
              Forma parte del grupo <a href="https://crusa.es/" rel="noopener noreferrer external">CRUSA</a>,
              que también gestiona la <a href="https://portacoeli.es/" rel="noopener noreferrer external">Hospedería Porta Coeli</a>
              en Sigüenza y la Ciudad Residencial Universitaria · Campus
              Village junto al campus de la UAH.
            </p>
            <p><a class="btn btn--primary" href="/residencia.html">Conoce su historia</a></p>
          </div>
          <div class="info-block">
            <h3>La Residencia en cifras</h3>
            <dl>
              <dt>Habitaciones</dt><dd>41 habitaciones (individuales y dobles) con baño privado</dd>
              <dt>Año de fundación</dt><dd>Colegio fundado en 1499 por el Cardenal Cisneros</dd>
              <dt>Reconocimiento</dt><dd>Patrimonio de la Humanidad UNESCO (1998)</dd>
              <dt>Gestión</dt><dd>CRUSA — sociedad de la Universidad de Alcalá</dd>
            </dl>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="servicios-title">
      <div class="container">
        <h2 class="section__title" id="servicios-title">Servicios destacados</h2>
        <p class="section__intro">
          Una experiencia residencial completa: comedor propio, salas de
          estudio, biblioteca, wifi en todo el edificio y conserjería las 24 h.
        </p>
        <div class="grid grid--3">
          <article class="card">
            <div class="card__media card__media--photo">
              <img src="/img/comedor.webp" alt="Comedor de la Residencia"
                   width="800" height="500" loading="lazy" decoding="async">
            </div>
            <div class="card__body">
              <h3 class="card__title">Comedor propio</h3>
              <p class="card__text">Pensión completa o media pensión con menús elaborados en cocina propia.</p>
              <a class="card__link" href="/servicios.html#restauracion">Ver detalles</a>
            </div>
          </article>
          <article class="card">
            <div class="card__media card__media--photo">
              <img src="/img/biblioteca.webp" alt="Biblioteca de la Residencia"
                   width="800" height="500" loading="lazy" decoding="async">
            </div>
            <div class="card__body">
              <h3 class="card__title">Estudio y biblioteca</h3>
              <p class="card__text">Salas de estudio, biblioteca de consulta y zonas de trabajo en grupo.</p>
              <a class="card__link" href="/servicios.html#estudio">Ver detalles</a>
            </div>
          </article>
          <article class="card">
            <div class="card__media card__media--photo">
              <img src="/img/fachada.webp" alt="Fachada del Colegio Mayor de San Ildefonso"
                   width="800" height="500" loading="lazy" decoding="async">
            </div>
            <div class="card__body">
              <h3 class="card__title">Conserjería 24 h</h3>
              <p class="card__text">Atención y seguridad las 24 horas del día, todos los días del año.</p>
              <a class="card__link" href="/servicios.html#seguridad">Ver detalles</a>
            </div>
          </article>
          <article class="card">
            <div class="card__media" aria-hidden="true">Wi-Fi</div>
            <div class="card__body">
              <h3 class="card__title">Conectividad</h3>
              <p class="card__text">Wifi en todo el edificio incluida en el precio del alojamiento.</p>
              <a class="card__link" href="/servicios.html#conectividad">Ver detalles</a>
            </div>
          </article>
          <article class="card">
            <div class="card__media" aria-hidden="true">Limpieza</div>
            <div class="card__body">
              <h3 class="card__title">Limpieza y lavandería</h3>
              <p class="card__text">Limpieza de habitación y servicio de lavandería incluidos.</p>
              <a class="card__link" href="/servicios.html#limpieza">Ver detalles</a>
            </div>
          </article>
          <article class="card">
            <div class="card__media" aria-hidden="true">Vending</div>
            <div class="card__body">
              <h3 class="card__title">Otros servicios</h3>
              <p class="card__text">Mantenimiento, vending y atención al residente durante todo el curso.</p>
              <a class="card__link" href="/servicios.html">Ver todos</a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="cta" aria-labelledby="cta-title">
      <div class="container cta__inner">
        <div>
          <h2 id="cta-title">¿Quieres vivir tu etapa universitaria en Alcalá?</h2>
          <p>Solicita información sin compromiso o reserva una visita guiada por nuestras instalaciones.</p>
        </div>
        <a class="btn btn--accent btn--lg" href="/contacto.html#solicitud">Contactar con la Residencia</a>
      </div>
    </section>
  </main>
"""
INDEX_EXTRA = _json.dumps({
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": f"{SITE_URL}#website",
    "url": SITE_URL,
    "name": SITE_NAME,
    "inLanguage": "es-ES",
    "publisher": {
        "@type": "Organization",
        "@id": f"{SITE_URL}#crusa",
        "name": "Ciudad Residencial Universitaria, S.A. (CRUSA)",
        "taxID": "A-80991714",
        "url": "https://crusa.es/",
        "parentOrganization": {
            "@type": "EducationalOrganization",
            "name": "Universidad de Alcalá",
            "url": "https://www.uah.es/",
        },
    },
}, ensure_ascii=False)
page("index", INDEX_BODY, INDEX_EXTRA)

# ---------- RESIDENCIA ----------
RES_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("La Residencia",None)])}
        <h1>La Residencia</h1>
        <p class="page-header__lead">
          Más de cinco siglos de vocación universitaria en el Colegio Mayor de
          San Ildefonso, Alcalá de Henares.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Historia y ubicación</h2>
        <div class="grid grid--2">
          <div>
            <p>
              La Residencia San Ildefonso se aloja en el <strong>Colegio Mayor
              de San Ildefonso</strong>, fundado en 1499 por el cardenal
              <strong>Francisco Jiménez de Cisneros</strong> con autorización
              del papa Alejandro VI. La primera piedra se colocó el 14 de marzo
              de 1500 y el edificio se inauguró el 26 de julio de 1508 con la
              llegada de los siete primeros colegiales procedentes de
              Salamanca.
            </p>
            <p>
              Su célebre <strong>fachada plateresca</strong>, obra de Rodrigo
              Gil de Hontañón (1537–1553), fue concebida como un gran retablo
              de piedra y es una de las imágenes más reconocibles de la
              ciudad. En su interior se conservan los patios de Santo Tomás de
              Villanueva, de los Filósofos y Trilingüe, así como el
              <strong>Paraninfo</strong>, sede de la entrega anual del
              <em>Premio Cervantes</em>.
            </p>
            <p>
              El conjunto está declarado <strong>Patrimonio de la Humanidad</strong>
              por la UNESCO desde 1998. La Residencia ocupa un edificio
              independiente situado en el <strong>Patio de los Filósofos</strong>,
              dentro de la manzana cisneriana.
            </p>
          </div>
          <div class="info-block">
            <h3>Datos clave</h3>
            <dl>
              <dt>Ubicación</dt>
              <dd>{ADDR_STREET}, {ADDR_POSTAL} {ADDR_LOCALITY}</dd>
              <dt>Edificio</dt>
              <dd>Patio de los Filósofos · 2 plantas</dd>
              <dt>Reconocimiento</dt>
              <dd>UNESCO Patrimonio de la Humanidad (1998)</dd>
              <dt>Gestión</dt>
              <dd>CRUSA · Universidad de Alcalá</dd>
              <dt>Capacidad</dt>
              <dd>41 habitaciones</dd>
            </dl>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt" id="instalaciones" aria-labelledby="inst-title">
      <div class="container">
        <h2 class="section__title" id="inst-title">Instalaciones</h2>
        <p class="section__intro">
          La Residencia dispone de espacios diseñados para el estudio, el
          descanso y la vida social, integrados en un edificio histórico.
        </p>
        <div class="grid grid--3">
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">H</div>
            <h3 class="feature__title">Habitaciones</h3>
            <p class="feature__text">41 habitaciones individuales y dobles con baño completo privado.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">C</div>
            <h3 class="feature__title">Comedor</h3>
            <p class="feature__text">Comedor propio con desayuno, comida y cena en cocina propia.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">B</div>
            <h3 class="feature__title">Biblioteca</h3>
            <p class="feature__text">Sala de lectura silenciosa para uso exclusivo de residentes.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">S</div>
            <h3 class="feature__title">Salas de estudio</h3>
            <p class="feature__text">Espacios reservados para el trabajo individual o en grupo.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">P</div>
            <h3 class="feature__title">Patios históricos</h3>
            <p class="feature__text">Acceso al Patio de los Filósofos y zonas comunes del Colegio.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">L</div>
            <h3 class="feature__title">Lavandería</h3>
            <p class="feature__text">Servicio de lavandería incluido en el precio del alojamiento.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="galeria-title">
      <div class="container">
        <h2 class="section__title" id="galeria-title">Galería</h2>
        <p class="section__intro">
          Fotografías del Colegio Mayor de San Ildefonso y la Universidad de
          Alcalá. Imágenes bajo licencia Creative Commons (Wikimedia Commons).
        </p>
        <div class="gallery" role="list">
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="/img/fachada.webp" alt="Fachada plateresca del Colegio Mayor de San Ildefonso"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="/img/patio.webp" alt="Patio de los Filósofos del Colegio Mayor"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="/img/paraninfo.webp" alt="Paraninfo, sede del Premio Cervantes"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="/img/habitacion.webp" alt="Habitación individual con baño completo privado"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="/img/comedor.webp" alt="Comedor con pensión completa o media pensión"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="/img/biblioteca.webp" alt="Biblioteca de la Residencia"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Universidad_de_Alcal%C3%A1_de_Henares,_Espa%C3%B1a_(13).JPG?width=800"
                 alt="Vista del conjunto universitario de Alcalá de Henares"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
          <div class="gallery__item gallery__item--photo" role="listitem">
            <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Alcal%C3%A1_de_Henares_Universidad_Patio_del_Colegio_Triling%C3%BCe_.jpg?width=800"
                 alt="Patio Trilingüe del Colegio Mayor"
                 width="800" height="600" loading="lazy" decoding="async">
          </div>
        </div>
        <p class="form__note mt-md">
          Las imágenes de habitaciones, comedor y biblioteca son
          representaciones provisionales; las del Colegio Mayor proceden de
          <a href="https://commons.wikimedia.org/wiki/Category:Colegio_Mayor_de_San_Ildefonso_(Alcal%C3%A1_de_Henares)" rel="noopener noreferrer external">Wikimedia Commons</a>
          (Creative Commons). Todas se sustituirán por material propio o
          cedido por la <a href="https://www.fgua.es/" rel="noopener noreferrer external">FGUA</a> y
          <a href="https://www.uah.es/" rel="noopener noreferrer external">UAH</a> tras la sesión fotográfica.
        </p>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="grupo-title">
      <div class="container">
        <h2 class="section__title" id="grupo-title">Forma parte del grupo CRUSA</h2>
        <p class="section__intro">
          La Residencia San Ildefonso es uno de los alojamientos gestionados
          por <a href="https://crusa.es/" rel="noopener noreferrer external">CRUSA</a>
          (Ciudad Residencial Universitaria, S.A.), la sociedad de la
          Universidad de Alcalá para el alojamiento de estudiantes y
          visitantes.
        </p>
        <div class="grid grid--3">
          <article class="card">
            <div class="card__media" aria-hidden="true">San Ildefonso</div>
            <div class="card__body">
              <h3 class="card__title">Residencia San Ildefonso</h3>
              <p class="card__text">Alojamiento universitario en el casco histórico de Alcalá, en el propio Colegio Mayor de San Ildefonso.</p>
              <a class="card__link" href="/">Ver Residencia</a>
            </div>
          </article>
          <article class="card">
            <div class="card__media" aria-hidden="true">Campus Village</div>
            <div class="card__body">
              <h3 class="card__title">CRUSA · Campus Village</h3>
              <p class="card__text">Más de 140 viviendas con habitaciones individuales y dobles, zonas deportivas y comunes, junto al campus de la UAH.</p>
              <a class="card__link" href="https://crusa.es/" rel="noopener noreferrer external">Visitar crusa.es</a>
            </div>
          </article>
          <article class="card">
            <div class="card__media" aria-hidden="true">Porta Coeli</div>
            <div class="card__body">
              <h3 class="card__title">Hospedería Porta Coeli</h3>
              <p class="card__text">Hospedería universitaria en Sigüenza (Guadalajara), restauración de un palacete barroco con cafetería y centro de convenciones.</p>
              <a class="card__link" href="https://portacoeli.es/" rel="noopener noreferrer external">Visitar portacoeli.es</a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="cta">
      <div class="container cta__inner">
        <div>
          <h2>Visítanos en persona</h2>
          <p>Concierta una visita guiada y descubre la Residencia y su entorno histórico.</p>
        </div>
        <a class="btn btn--accent btn--lg" href="/contacto.html#visita">Reservar visita</a>
      </div>
    </section>
  </main>
"""
# Article con mentions: enumera las entidades canónicas para que los LLMs
# las identifiquen sin ambigüedad (Wikipedia/Wikidata/UNESCO como @id).
RES_ARTICLE_JSONLD = _json.dumps({
    "@context": "https://schema.org",
    "@type": "Article",
    "@id": f"{SITE_URL}/residencia.html#article",
    "headline": "La Residencia Universitaria San Ildefonso",
    "description": "Historia, ubicación e instalaciones de la Residencia San Ildefonso, alojada en el histórico Colegio Mayor de San Ildefonso (Alcalá de Henares).",
    "inLanguage": "es-ES",
    "url": f"{SITE_URL}/residencia.html",
    "image": f"{SITE_URL}/img/fachada.webp",
    "isPartOf": {"@id": f"{SITE_URL}#website"},
    "publisher": {"@id": f"{SITE_URL}#crusa"},
    "about": {
        "@type": "TouristAttraction",
        "name": "Colegio Mayor de San Ildefonso",
        "sameAs": [
            "https://es.wikipedia.org/wiki/Colegio_Mayor_de_San_Ildefonso",
            "https://www.wikidata.org/wiki/Q5142854",
        ],
        "containedInPlace": {
            "@type": "Place",
            "name": "Universidad de Alcalá — sitio UNESCO",
            "sameAs": "https://whc.unesco.org/es/list/876",
        },
    },
    "mentions": [
        {"@type": "Person", "name": "Francisco Jiménez de Cisneros",
         "sameAs": "https://es.wikipedia.org/wiki/Francisco_Jim%C3%A9nez_de_Cisneros"},
        {"@type": "Person", "name": "Rodrigo Gil de Hontañón",
         "sameAs": "https://es.wikipedia.org/wiki/Rodrigo_Gil_de_Honta%C3%B1%C3%B3n"},
        {"@type": "EducationalOrganization", "name": "Universidad de Alcalá",
         "sameAs": "https://www.uah.es/"},
        {"@type": "Organization", "name": "Fundación General de la Universidad de Alcalá",
         "sameAs": "https://www.fgua.es/"},
        {"@type": "Organization", "name": "Ciudad Residencial Universitaria (CRUSA)",
         "sameAs": "https://crusa.es/"},
        {"@type": "Place", "name": "Patrimonio de la Humanidad UNESCO (1998)",
         "sameAs": "https://whc.unesco.org/es/list/876"},
        {"@type": "CreativeWork", "name": "Premio Cervantes",
         "sameAs": "https://es.wikipedia.org/wiki/Premio_Miguel_de_Cervantes"},
    ],
}, ensure_ascii=False)
RES_EXTRA = (
    breadcrumb_jsonld([("Inicio","/"),("La Residencia","/residencia.html")])
    + "</script>\n  <script type=\"application/ld+json\">"
    + RES_ARTICLE_JSONLD
)
page("residencia", RES_BODY, RES_EXTRA)

# ---------- HABITACIONES ----------
HAB_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("Habitaciones",None)])}
        <h1>Habitaciones y tarifas</h1>
        <p class="page-header__lead">
          Habitaciones individuales y dobles con baño completo privado,
          calefacción, wifi y limpieza incluida.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Modalidades de habitación</h2>
        <div class="grid grid--2">
          <article class="card">
            <div class="card__media" aria-hidden="true">Individual</div>
            <div class="card__body">
              <h3 class="card__title">Habitación individual</h3>
              <p class="card__text">
                Habitación individual con cama, escritorio, armario y baño
                completo privado. Calefacción, televisión y aire acondicionado.
              </p>
              <ul class="card__list">
                <li>Baño completo privado</li>
                <li>Calefacción central</li>
                <li>Wifi incluido</li>
                <li>Limpieza semanal</li>
              </ul>
              <p class="card__price">Desde 365 €/mes</p>
            </div>
          </article>
          <article class="card">
            <div class="card__media" aria-hidden="true">Doble</div>
            <div class="card__body">
              <h3 class="card__title">Habitación doble</h3>
              <p class="card__text">
                Habitación doble compartida por dos residentes, con dos camas,
                dos escritorios y baño completo privado en la habitación.
              </p>
              <ul class="card__list">
                <li>Baño completo privado</li>
                <li>Ideal para estancias Erasmus</li>
                <li>Wifi y calefacción</li>
                <li>Cambio de sábanas y toallas</li>
              </ul>
              <p class="card__price">Desde 270 €/mes/persona</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--alt" id="tarifas" aria-labelledby="tarifas-title">
      <div class="container">
        <h2 class="section__title" id="tarifas-title">Tarifas</h2>
        <p class="section__intro">
          Precios mensuales orientativos por residente. Incluyen agua, luz,
          calefacción, wifi, limpieza de habitación y lavandería. Las opciones
          de pensión se suman al alojamiento.
        </p>
        <div class="rates-wrapper">
          <table class="rates">
            <caption>Tarifas mensuales — orientativas. Confirmar al solicitar plaza.</caption>
            <thead>
              <tr>
                <th scope="col">Concepto</th>
                <th scope="col">Importe</th>
                <th scope="col">Notas</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">Habitación individual</th>
                <td class="price">365 €/mes</td>
                <td>Baño privado, agua, luz, wifi, limpieza y lavandería incluidas</td>
              </tr>
              <tr>
                <th scope="row">Habitación doble (por persona)</th>
                <td class="price">270 €/mes</td>
                <td>Compartida; mismas prestaciones</td>
              </tr>
              <tr>
                <th scope="row">Pensión completa</th>
                <td class="price">+ 300 €/mes</td>
                <td>Desayuno, comida y cena de lunes a viernes</td>
              </tr>
              <tr>
                <th scope="row">Media pensión</th>
                <td class="price">+ 170 €/mes</td>
                <td>Desayuno y comida o cena de lunes a viernes</td>
              </tr>
              <tr>
                <th scope="row">Fianza</th>
                <td class="price">300 €</td>
                <td>Pago único al ingresar; reembolsable al finalizar la estancia</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="form__note mt-md">
          Para estancias cortas, profesorado visitante o programas Erasmus,
          consulta condiciones específicas en la sección de
          <a href="/contacto.html">contacto</a>.
        </p>
      </div>
    </section>

    <section class="section" aria-labelledby="proceso-title">
      <div class="container">
        <h2 class="section__title" id="proceso-title">Proceso de solicitud</h2>
        <div class="grid grid--4">
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">1</div>
            <h3 class="feature__title">Solicitud</h3>
            <p class="feature__text">Rellena el formulario y aporta la documentación universitaria.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">2</div>
            <h3 class="feature__title">Valoración</h3>
            <p class="feature__text">El equipo de admisiones valora la solicitud según los criterios.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">3</div>
            <h3 class="feature__title">Reserva</h3>
            <p class="feature__text">Se formaliza la plaza con el pago de la fianza.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">4</div>
            <h3 class="feature__title">Bienvenida</h3>
            <p class="feature__text">Acto de bienvenida y entrega de habitación al inicio del curso.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="cta">
      <div class="container cta__inner">
        <div>
          <h2>¿Te interesa una de las habitaciones?</h2>
          <p>Inicia tu solicitud o resuelve dudas con el equipo de admisiones.</p>
        </div>
        <a class="btn btn--accent btn--lg" href="/contacto.html#solicitud">Solicitar plaza</a>
      </div>
    </section>
  </main>
"""
page("habitaciones", HAB_BODY, breadcrumb_jsonld([("Inicio","/"),("Habitaciones","/habitaciones.html")]))

# ---------- SERVICIOS ----------
SERV_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("Servicios",None)])}
        <h1>Servicios</h1>
        <p class="page-header__lead">
          Servicios incluidos en el precio del alojamiento, pensados para
          acompañar al residente durante todo el curso académico.
        </p>
      </div>
    </section>

    <section class="section" id="restauracion" aria-labelledby="rest-title">
      <div class="container">
        <h2 class="section__title" id="rest-title">Restauración</h2>
        <div class="grid grid--2">
          <div>
            <p>
              La Residencia cuenta con <strong>comedor propio y cocina
              propia</strong>. Ofrece <strong>pensión completa</strong>
              (desayuno, comida y cena) o <strong>media pensión</strong>
              (desayuno + comida o cena), de lunes a viernes en el periodo
              lectivo.
            </p>
            <p>
              Los menús se elaboran diariamente buscando una alimentación
              equilibrada y se adaptan, con previo aviso, a necesidades
              dietéticas concretas.
            </p>
          </div>
          <div class="info-block">
            <h3>Régimen de comidas</h3>
            <dl>
              <dt>Pensión completa</dt><dd>Desayuno, comida y cena (L–V)</dd>
              <dt>Media pensión</dt><dd>Desayuno + comida o cena (L–V)</dd>
              <dt>Fines de semana</dt><dd>Consultar disponibilidad</dd>
            </dl>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt" id="estudio" aria-labelledby="est-title">
      <div class="container">
        <h2 class="section__title" id="est-title">Estudio y biblioteca</h2>
        <div class="grid grid--3">
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">B</div>
            <h3 class="feature__title">Biblioteca</h3>
            <p class="feature__text">Sala de lectura silenciosa para uso exclusivo de residentes.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">S</div>
            <h3 class="feature__title">Salas de estudio</h3>
            <p class="feature__text">Espacios habilitados para el trabajo individual.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">G</div>
            <h3 class="feature__title">Trabajo en grupo</h3>
            <p class="feature__text">Áreas comunes para reuniones y trabajos conjuntos.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="cultura" aria-labelledby="cul-title">
      <div class="container">
        <h2 class="section__title" id="cul-title">Vida residencial</h2>
        <p class="section__intro">
          Por su ubicación dentro del Colegio Mayor de San Ildefonso, los
          residentes disfrutan de un entorno académico privilegiado y de la
          oferta cultural y deportiva de la <a href="https://www.uah.es/" rel="noopener noreferrer external">Universidad de Alcalá</a>
          y la <a href="https://www.fgua.es/" rel="noopener noreferrer external">Fundación General UAH</a>.
        </p>
        <div class="grid grid--3">
          <article class="card"><div class="card__media" aria-hidden="true">Cultura</div>
            <div class="card__body"><h3 class="card__title">Actividades culturales</h3>
            <p class="card__text">Acceso a conferencias, exposiciones y conciertos organizados en el campus.</p></div></article>
          <article class="card"><div class="card__media" aria-hidden="true">Deporte</div>
            <div class="card__body"><h3 class="card__title">Deporte UAH</h3>
            <p class="card__text">Posibilidad de inscripción en las competiciones y servicios deportivos universitarios.</p></div></article>
          <article class="card"><div class="card__media" aria-hidden="true">Idiomas</div>
            <div class="card__body"><h3 class="card__title">Idiomas y formación</h3>
            <p class="card__text">Cursos de idiomas y extensión universitaria a través de la FGUA.</p></div></article>
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="serv2-title">
      <div class="container">
        <h2 class="section__title" id="serv2-title">Servicios generales</h2>
        <div class="grid grid--4">
          <article class="feature" id="conectividad">
            <div class="feature__icon" aria-hidden="true">W</div>
            <h3 class="feature__title">Wifi</h3>
            <p class="feature__text">Conexión wifi incluida en todas las dependencias.</p>
          </article>
          <article class="feature" id="seguridad">
            <div class="feature__icon" aria-hidden="true">24</div>
            <h3 class="feature__title">Atención y seguridad 24 h</h3>
            <p class="feature__text">Conserjería y vigilancia las 24 horas, todos los días del año.</p>
          </article>
          <article class="feature" id="limpieza">
            <div class="feature__icon" aria-hidden="true">L</div>
            <h3 class="feature__title">Limpieza y lavandería</h3>
            <p class="feature__text">Limpieza periódica de la habitación y servicio de lavandería incluidos.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">R</div>
            <h3 class="feature__title">Sábanas y toallas</h3>
            <p class="feature__text">Servicio de cambio de ropa de cama y toallas.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">M</div>
            <h3 class="feature__title">Mantenimiento</h3>
            <p class="feature__text">Servicio de mantenimiento técnico interno.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">V</div>
            <h3 class="feature__title">Vending</h3>
            <p class="feature__text">Máquinas de café, bebidas y snacks en zonas comunes.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">TV</div>
            <h3 class="feature__title">Televisión y antena</h3>
            <p class="feature__text">Televisión y aire acondicionado en la habitación.</p>
          </article>
          <article class="feature">
            <div class="feature__icon" aria-hidden="true">E</div>
            <h3 class="feature__title">Escritorio</h3>
            <p class="feature__text">Escritorio de trabajo en cada habitación.</p>
          </article>
        </div>
      </div>
    </section>
  </main>
"""
page("servicios", SERV_BODY, breadcrumb_jsonld([("Inicio","/"),("Servicios","/servicios.html")]))

# ---------- CONTACTO ----------
CONT_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("Contacto",None)])}
        <h1>Contacto y solicitud de plaza</h1>
        <p class="page-header__lead">
          Resolvemos tus dudas y te acompañamos en el proceso de admisión.
        </p>
      </div>
    </section>

    <section class="section" id="solicitud" aria-labelledby="form-title">
      <div class="container">
        <div class="contact-grid">
          <div>
            <h2 class="section__title" id="form-title">Formulario de contacto</h2>
            <p class="section__intro">
              Completa el formulario y nos pondremos en contacto contigo en un
              plazo máximo de 48 horas laborables.
            </p>
            <!--
              Formulario gestionado por Web3Forms (250 envíos/mes gratuitos).
              Sustituye TU_ACCESS_KEY_AQUI por la clave obtenida en
              https://web3forms.com tras registrarte con sanildefonso@crusa.es.
            -->
            <form class="form" action="https://api.web3forms.com/submit" method="POST">
              <input type="hidden" name="access_key" value="TU_ACCESS_KEY_AQUI">
              <input type="hidden" name="from_name" value="{SITE_NAME}">
              <input type="hidden" name="subject" value="Nueva consulta · {SITE_NAME}">
              <input type="hidden" name="redirect" value="{SITE_URL}/gracias.html">

              <div class="form__row form__row--2">
                <div class="form__field">
                  <label for="nombre">Nombre <span aria-hidden="true">*</span></label>
                  <input type="text" id="nombre" name="nombre" autocomplete="given-name" required>
                </div>
                <div class="form__field">
                  <label for="apellidos">Apellidos <span aria-hidden="true">*</span></label>
                  <input type="text" id="apellidos" name="apellidos" autocomplete="family-name" required>
                </div>
              </div>
              <div class="form__row form__row--2">
                <div class="form__field">
                  <label for="email">Correo electrónico <span aria-hidden="true">*</span></label>
                  <input type="email" id="email" name="email" autocomplete="email" required>
                </div>
                <div class="form__field">
                  <label for="telefono">Teléfono</label>
                  <input type="tel" id="telefono" name="telefono" autocomplete="tel" inputmode="tel">
                </div>
              </div>
              <div class="form__row form__row--2">
                <div class="form__field">
                  <label for="motivo">Motivo</label>
                  <select id="motivo" name="motivo">
                    <option value="solicitud">Solicitud de plaza</option>
                    <option value="visita">Reservar visita</option>
                    <option value="erasmus">Estancia Erasmus / corta</option>
                    <option value="grupos">Grupos / congresos</option>
                    <option value="otros">Otros</option>
                  </select>
                </div>
                <div class="form__field">
                  <label for="curso">Curso académico</label>
                  <select id="curso" name="curso">
                    <option>2026/27</option>
                    <option>2027/28</option>
                    <option>Estancia corta</option>
                  </select>
                </div>
              </div>
              <div class="form__field">
                <label for="mensaje">Mensaje</label>
                <textarea id="mensaje" name="mensaje" placeholder="Cuéntanos en qué podemos ayudarte"></textarea>
              </div>

              <!-- Honeypot anti-spam -->
              <div class="form__honeypot" aria-hidden="true">
                <label for="botcheck">No rellenar</label>
                <input type="checkbox" id="botcheck" name="botcheck" tabindex="-1" autocomplete="off">
              </div>

              <label class="form__check">
                <input type="checkbox" name="rgpd" required>
                <span>He leído y acepto la <a href="/politica-privacidad.html">política de privacidad</a> y el tratamiento de mis datos para gestionar mi consulta.</span>
              </label>

              <div>
                <button class="btn btn--primary btn--lg" type="submit">Enviar consulta</button>
              </div>
              <p class="form__note">Te responderemos al correo que indiques en un plazo máximo de 48 h laborables.</p>
            </form>
          </div>

          <aside aria-labelledby="aside-title">
            <h2 class="section__title" id="aside-title">Dónde estamos</h2>
            <div class="info-block">
              <h3>Dirección</h3>
              <p>
                {ADDR_STREET}<br>
                {ADDR_POSTAL} {ADDR_LOCALITY}<br>
                {ADDR_REGION} · España
              </p>
              <h3>Horario de atención</h3>
              <dl>
                <dt>Lunes a viernes</dt><dd>09:00 – 14:00 y 16:00 – 19:00</dd>
                <dt>Conserjería</dt><dd>24 horas, todos los días del año</dd>
              </dl>
              <h3>Contacto directo</h3>
              <p>
                <a href="tel:{PHONE_RAW}">{PHONE_FMT}</a><br>
                <a href="mailto:{EMAIL}">{EMAIL}</a>
              </p>
            </div>

            <div class="info-block mt-md" id="visita">
              <h3>Cómo llegar</h3>
              <p>
                A 5 minutos andando de la <strong>estación de Cercanías de
                Alcalá de Henares</strong> (líneas C-2 y C-7). Líneas urbanas
                de autobús con parada cerca de la Plaza de San Diego.
              </p>
              <p>
                <a href="https://maps.google.com/?q=Plaza+San+Diego,+Alcalá+de+Henares" rel="noopener noreferrer external">Abrir en Google Maps ↗</a>
              </p>
            </div>

            <div class="map mt-md" id="map">
              <button class="map__facade" type="button" id="map-trigger"
                      aria-label="Cargar mapa interactivo con la ubicación de la Residencia">
                <span class="map__pin" aria-hidden="true">📍</span>
                <span class="map__facade-body">
                  <strong>Cargar mapa interactivo</strong>
                  <span class="map__facade-addr">Plaza San Diego, s/n · Alcalá de Henares</span>
                  <small class="map__facade-note">Al pulsar se cargará un mapa desde Google. Puede transferirse información a Google conforme a su <a href="https://policies.google.com/privacy" rel="noopener noreferrer external">política de privacidad</a>.</small>
                </span>
              </button>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <section class="section section--band faq" id="faq" aria-labelledby="faq-title">
      <div class="container">
        <h2 class="section__title" id="faq-title">Preguntas frecuentes</h2>
        <div class="grid grid--2">
          <details>
            <summary>¿Qué documentación necesito para solicitar plaza?</summary>
            <p>DNI o pasaporte, justificante de matrícula o admisión universitaria y, si procede, expediente académico del curso anterior.</p>
          </details>
          <details>
            <summary>¿Aceptan estudiantes Erasmus o de intercambio?</summary>
            <p>Sí. La Residencia acoge habitualmente estudiantes de intercambio durante el curso académico.</p>
          </details>
          <details>
            <summary>¿Se puede visitar la Residencia antes de solicitar plaza?</summary>
            <p>Sí, organizamos visitas con cita previa. Indícalo en el formulario o llámanos al {PHONE_FMT}.</p>
          </details>
          <details>
            <summary>¿Está incluida la limpieza?</summary>
            <p>Sí, la limpieza de las habitaciones y la lavandería están incluidas en el precio del alojamiento.</p>
          </details>
          <details>
            <summary>¿Cuánto es la fianza?</summary>
            <p>La fianza al ingresar es de 300 €, reembolsable al finalizar la estancia conforme a la normativa interna.</p>
          </details>
          <details>
            <summary>¿Puedo elegir el régimen de comidas?</summary>
            <p>Sí, puedes optar por pensión completa, media pensión o solo alojamiento.</p>
          </details>
        </div>
      </div>
    </section>
  </main>
"""
FAQ_JSONLD = _json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": "¿Qué documentación necesito para solicitar plaza?",
         "acceptedAnswer": {"@type": "Answer", "text": "DNI o pasaporte, justificante de matrícula o admisión universitaria y, si procede, expediente académico del curso anterior."}},
        {"@type": "Question", "name": "¿Aceptan estudiantes Erasmus o de intercambio?",
         "acceptedAnswer": {"@type": "Answer", "text": "Sí. La Residencia acoge habitualmente estudiantes de intercambio durante el curso académico."}},
        {"@type": "Question", "name": "¿Se puede visitar la Residencia antes de solicitar plaza?",
         "acceptedAnswer": {"@type": "Answer", "text": f"Sí, organizamos visitas con cita previa. Indícalo en el formulario o llama al {PHONE_FMT}."}},
        {"@type": "Question", "name": "¿Está incluida la limpieza?",
         "acceptedAnswer": {"@type": "Answer", "text": "Sí, la limpieza de las habitaciones y la lavandería están incluidas en el precio del alojamiento."}},
        {"@type": "Question", "name": "¿Cuánto es la fianza?",
         "acceptedAnswer": {"@type": "Answer", "text": "La fianza al ingresar es de 300 €, reembolsable al finalizar la estancia conforme a la normativa interna."}},
        {"@type": "Question", "name": "¿Puedo elegir el régimen de comidas?",
         "acceptedAnswer": {"@type": "Answer", "text": "Sí, puedes optar por pensión completa, media pensión o solo alojamiento."}},
    ],
}, ensure_ascii=False)

CONT_EXTRA = breadcrumb_jsonld([("Inicio","/"),("Contacto","/contacto.html")]) + "</script>\n  <script type=\"application/ld+json\">" + FAQ_JSONLD
page("contacto", CONT_BODY, CONT_EXTRA)

# ---------- GRACIAS ----------
GRA_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("Mensaje recibido",None)])}
        <h1>Mensaje recibido</h1>
        <p class="page-header__lead">Gracias por contactar con la Residencia San Ildefonso.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <p>Hemos recibido tu mensaje correctamente. Te responderemos al correo electrónico que nos has facilitado en un plazo máximo de <strong>48 horas laborables</strong>.</p>
        <p>Si tu consulta es urgente, puedes llamarnos al <a href="tel:{PHONE_RAW}">{PHONE_FMT}</a> o escribirnos a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        <p><a class="btn btn--primary mt-md" href="/">Volver al inicio</a></p>
      </div>
    </section>
  </main>
"""
page("gracias", GRA_BODY)

# ---------- 404 ----------
ERR_BODY = f"""
  <main id="main">
    <section class="section error-page">
      <div class="container">
        <p class="error-page__code">404</p>
        <h1>Página no encontrada</h1>
        <p class="lead">La dirección que has solicitado no existe o ha sido movida.</p>
        <p class="btn-group">
          <a class="btn btn--primary" href="/">Volver al inicio</a>
          <a class="btn btn--accent" href="/contacto.html">Contactar</a>
        </p>
      </div>
    </section>
  </main>
"""
page("404", ERR_BODY)

# ---------- AVISO LEGAL ----------
LEG_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("Aviso legal",None)])}
        <h1>Aviso legal</h1>
        <p class="page-header__lead">Información legal del sitio web residenciasanildefonso.es.</p>
      </div>
    </section>
    <section class="section">
      <div class="container prose">
        <h2>1. Datos del titular</h2>
        <p>
          En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de
          la Sociedad de la Información y de Comercio Electrónico (LSSICE),
          se informa al usuario de los datos identificativos del titular del
          sitio web:
        </p>
        <ul>
          <li><strong>Titular:</strong> Ciudad Residencial Universitaria, S.A. (CRUSA), sociedad anónima unipersonal participada por la Universidad de Alcalá.</li>
          <li><strong>CIF:</strong> A-80991714</li>
          <li><strong>Domicilio social:</strong> {ADDR_STREET}, {ADDR_POSTAL} {ADDR_LOCALITY} ({ADDR_REGION}), España.</li>
          <li><strong>Teléfono (Residencia):</strong> <a href="tel:{PHONE_RAW}">{PHONE_FMT}</a></li>
          <li><strong>Teléfono (CRUSA):</strong> <a href="tel:+34911817101">+34 911 81 71 01</a></li>
          <li><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="mailto:info@crusa.es">info@crusa.es</a></li>
          <li><strong>Sitio web:</strong> <a href="/">{SITE_URL}</a></li>
        </ul>

        <h2>2. Objeto</h2>
        <p>
          El presente sitio web tiene como finalidad ofrecer información sobre
          los servicios de alojamiento universitario de la Residencia
          Universitaria San Ildefonso, así como facilitar el contacto y la
          solicitud de plaza.
        </p>

        <h2>3. Condiciones de uso</h2>
        <p>
          El acceso y la navegación por este sitio atribuyen la condición de
          usuario, e implican la aceptación plena y sin reservas de las
          presentes condiciones. El usuario se compromete a hacer un uso
          adecuado de los contenidos y servicios y a no emplearlos para
          incurrir en actividades ilícitas.
        </p>

        <h2>4. Propiedad intelectual e industrial</h2>
        <p>
          Todos los contenidos del sitio (textos, imágenes, logotipos,
          diseños y código) son titularidad de su autor o cuentan con la
          correspondiente autorización. Queda prohibida su reproducción total
          o parcial sin autorización expresa.
        </p>

        <h2>5. Exclusión de garantías y responsabilidad</h2>
        <p>
          El titular no se hace responsable de los daños y perjuicios que
          pudieran derivarse de interferencias, omisiones, interrupciones,
          virus informáticos, averías telefónicas o desconexiones en el
          funcionamiento operativo de este sistema electrónico.
        </p>

        <h2>6. Legislación aplicable</h2>
        <p>
          La relación entre el titular y el usuario se regirá por la
          normativa española vigente. Cualquier controversia se someterá a los
          juzgados y tribunales de la ciudad de Alcalá de Henares.
        </p>
      </div>
    </section>
  </main>
"""
page("aviso-legal", LEG_BODY)

# ---------- POLÍTICA DE PRIVACIDAD ----------
PRIV_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("Política de privacidad",None)])}
        <h1>Política de privacidad</h1>
        <p class="page-header__lead">Información sobre el tratamiento de datos personales conforme al RGPD y la LOPDGDD.</p>
      </div>
    </section>
    <section class="section">
      <div class="container prose">
        <h2>1. Responsable del tratamiento</h2>
        <p>
          El responsable del tratamiento de tus datos personales es <strong>Ciudad
          Residencial Universitaria, S.A. (CRUSA)</strong>, con CIF <strong>A-80991714</strong>
          y domicilio social en {ADDR_STREET}, {ADDR_POSTAL} {ADDR_LOCALITY}
          ({ADDR_REGION}), España. Puedes contactar con el responsable en
          <a href="mailto:{EMAIL}">{EMAIL}</a> o por escrito a la dirección
          indicada.
        </p>

        <h2>2. Datos que recogemos</h2>
        <p>Recogemos los datos que nos facilitas a través del formulario de contacto:</p>
        <ul>
          <li>Nombre y apellidos</li>
          <li>Correo electrónico</li>
          <li>Teléfono (opcional)</li>
          <li>Contenido del mensaje y datos sobre la consulta</li>
        </ul>

        <h2>3. Finalidad y base legal</h2>
        <p>
          Tratamos tus datos con la finalidad de gestionar tu consulta o tu
          solicitud de plaza. La base legal del tratamiento es el
          consentimiento que nos otorgas al enviar el formulario, conforme al
          artículo 6.1.a) del RGPD.
        </p>

        <h2>4. Conservación</h2>
        <p>
          Conservamos tus datos durante el tiempo necesario para resolver tu
          consulta y, posteriormente, durante los plazos legales aplicables.
        </p>

        <h2>5. Destinatarios</h2>
        <p>
          No cedemos datos a terceros salvo obligación legal. Para gestionar
          el envío del formulario utilizamos el servicio Web3Forms, que actúa
          como encargado del tratamiento.
        </p>

        <h2>6. Derechos</h2>
        <p>
          Tienes derecho a acceder, rectificar y suprimir tus datos, así como
          a otros derechos reconocidos por el RGPD. Puedes ejercerlos
          escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>.
        </p>
        <p>
          Si consideras que tus derechos no han sido atendidos, puedes
          presentar una reclamación ante la Agencia Española de Protección de
          Datos (<a href="https://www.aepd.es" rel="noopener noreferrer external">www.aepd.es</a>).
        </p>

        <h2>7. Seguridad</h2>
        <p>
          Aplicamos las medidas técnicas y organizativas necesarias para
          garantizar la confidencialidad e integridad de tus datos, en
          cumplimiento del RGPD y la LOPDGDD.
        </p>
      </div>
    </section>
  </main>
"""
page("politica-privacidad", PRIV_BODY)

# ---------- POLÍTICA DE COOKIES ----------
COOK_BODY = f"""
  <main id="main">
    <section class="page-header">
      <div class="container">
        {breadcrumb([("Inicio","/"),("Política de cookies",None)])}
        <h1>Política de cookies</h1>
        <p class="page-header__lead">Información sobre las cookies que utiliza este sitio web.</p>
      </div>
    </section>
    <section class="section">
      <div class="container prose">
        <h2>1. ¿Qué son las cookies?</h2>
        <p>
          Las cookies son pequeños archivos que el navegador almacena en tu
          dispositivo cuando visitas un sitio web. Se utilizan para recordar
          preferencias o información de uso.
        </p>

        <h2>2. Cookies utilizadas en este sitio</h2>
        <p>
          Este sitio <strong>no utiliza cookies de seguimiento, analítica ni
          publicidad</strong>. Solo utiliza un dato técnico de almacenamiento
          local del navegador (<code>localStorage</code>) para recordar tu
          preferencia respecto al aviso de cookies.
        </p>
        <ul>
          <li><strong>rsi-cookies-v1</strong> — Almacena si has aceptado o rechazado el aviso de cookies. No contiene datos personales. Se conserva en tu navegador hasta que la borres manualmente.</li>
        </ul>

        <h2>3. Servicios de terceros</h2>
        <p>
          Este sitio carga las fuentes web desde Google Fonts. Para más
          información, consulta la
          <a href="https://policies.google.com/privacy" rel="noopener noreferrer external">política de privacidad de Google</a>.
        </p>

        <h2>4. Cómo configurar las cookies</h2>
        <p>
          Puedes configurar o eliminar las cookies y el almacenamiento local
          desde los ajustes de tu navegador:
        </p>
        <ul>
          <li><a href="https://support.google.com/chrome/answer/95647" rel="noopener noreferrer external">Google Chrome</a></li>
          <li><a href="https://support.mozilla.org/es/kb/proteccion-mejorada-rastreo-firefox-escritorio" rel="noopener noreferrer external">Mozilla Firefox</a></li>
          <li><a href="https://support.apple.com/es-es/guide/safari/sfri11471/mac" rel="noopener noreferrer external">Safari</a></li>
          <li><a href="https://support.microsoft.com/es-es/microsoft-edge" rel="noopener noreferrer external">Microsoft Edge</a></li>
        </ul>
      </div>
    </section>
  </main>
"""
page("politica-cookies", COOK_BODY)

print("Done.")
