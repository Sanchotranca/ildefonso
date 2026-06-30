<?php
session_start();
$n1 = rand(2, 9);
$n2 = rand(1, 9);
$_SESSION['captcha_res'] = $n1 + $n2;
?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contacto y solicitud — Residencia San Ildefonso | Alcalá</title>
  <meta name="description" content="Contacta con la Residencia San Ildefonso de Alcalá de Henares: dirección, teléfono, email y formulario para solicitar plaza o reservar visita.">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#003DA5">
  <link rel="canonical" href="https://www.residenciasanildefonso.es/contacto.html">

  <meta property="og:type" content="website">
  <meta property="og:title" content="Contacto y solicitud — Residencia San Ildefonso | Alcalá">
  <meta property="og:description" content="Contacta con la Residencia San Ildefonso de Alcalá de Henares: dirección, teléfono, email y formulario para solicitar plaza o reservar visita.">
  <meta property="og:url" content="https://www.residenciasanildefonso.es/contacto.html">
  <meta property="og:image" content="https://www.residenciasanildefonso.es/img/og-image.webp">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="Residencia San Ildefonso">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Meta geo (Bing, Yandex y bots no-Google) -->
  <meta name="geo.region" content="ES-MD">
  <meta name="geo.placename" content="Alcalá de Henares, Madrid">
  <meta name="geo.position" content="40.482236;-3.363976">
  <meta name="ICBM" content="40.482236, -3.363976">

  <link rel="icon" href="img/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="img/apple-touch-icon.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap">

  <link rel="stylesheet" href="css/style.css">

  

  <script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "LodgingBusiness",
  "@id": "https://www.residenciasanildefonso.es#residencia",
  "name": "Residencia San Ildefonso",
  "url": "https://www.residenciasanildefonso.es",
  "telephone": "+34 91 878 81 46",
  "email": "sanildefonso@crusa.es",
  "taxID": "A-80991714",
  "image": "https://www.residenciasanildefonso.es/img/og-image.webp",
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
    "streetAddress": "Plaza San Diego, s/n",
    "addressLocality": "Alcalá de Henares",
    "addressRegion": "Madrid",
    "postalCode": "28801",
    "addressCountry": "ES"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "40.482236", "longitude": "-3.363976" },
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
}</script>
  <script type="application/ld+json">{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://www.residenciasanildefonso.es/"}, {"@type": "ListItem", "position": 2, "name": "Contacto", "item": "https://www.residenciasanildefonso.es/contacto.html"}]}</script>
  <script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "¿Qué documentación necesito para solicitar plaza?", "acceptedAnswer": {"@type": "Answer", "text": "DNI o pasaporte, justificante de matrícula o admisión universitaria y, si procede, expediente académico del curso anterior."}}, {"@type": "Question", "name": "¿Aceptan estudiantes Erasmus o de intercambio?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. La Residencia acoge habitualmente estudiantes de intercambio durante el curso académico."}}, {"@type": "Question", "name": "¿Se puede visitar la Residencia antes de solicitar plaza?", "acceptedAnswer": {"@type": "Answer", "text": "Sí, organizamos visitas con cita previa. Indícalo en el formulario o llama al +34 91 878 81 46."}}, {"@type": "Question", "name": "¿Está incluida la limpieza?", "acceptedAnswer": {"@type": "Answer", "text": "Sí, la limpieza de las habitaciones y la lavandería están incluidas en el precio del alojamiento."}}, {"@type": "Question", "name": "¿Cuánto es la fianza?", "acceptedAnswer": {"@type": "Answer", "text": "La fianza al ingresar es de 300 €, reembolsable al finalizar la estancia conforme a la normativa interna."}}, {"@type": "Question", "name": "¿Puedo elegir el régimen de comidas?", "acceptedAnswer": {"@type": "Answer", "text": "Sí, puedes optar por pensión completa, media pensión o solo alojamiento."}}]}</script>
</head>
<body>
  <a class="skip-link" href="#main">Saltar al contenido principal</a>

  <header class="site-header" role="banner">
    <div class="container site-header__inner">
      <a href="index.html" class="brand" aria-label="Inicio – Residencia San Ildefonso">
        <img src="img/logo-san-ildefonso.jpg" alt="Residencia Universitaria San Ildefonso" class="brand__crest" width="90" height="61" fetchpriority="high">
        <span class="brand__text">
          <span class="brand__title">Residencia San Ildefonso</span>
        </span>
      </a>
      <button class="nav-toggle" type="button" aria-controls="primary-nav" aria-expanded="false" aria-label="Abrir menú de navegación">
        <span class="nav-toggle__bar"></span>
        <span class="nav-toggle__bar"></span>
        <span class="nav-toggle__bar"></span>
      </button>
      <nav id="primary-nav" class="main-nav" aria-label="Navegación principal">
        <ul class="main-nav__list">
          <li><a class="main-nav__link" href="index.html">Inicio</a></li>
          <li><a class="main-nav__link" href="residencia.html">La Residencia</a></li>
          <li><a class="main-nav__link" href="contacto.html" aria-current="page">Contacto</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="page-header">
      <div class="container">
        
        <nav class="breadcrumb" aria-label="Migas de pan">
          <ol>
            <li><a href="index.html">Inicio</a></li><li aria-current="page">Contacto</li>
          </ol>
        </nav>

        <h1>Contacto y reservas</h1>
        <p class="page-header__lead">
          Cuéntenos qué necesita. Le respondemos antes de 48 horas.
        </p>
      </div>
    </section>

    <section class="section" id="solicitud" aria-labelledby="form-title">
      <div class="container">
        <div class="contact-grid">
          <div>
            <h2 class="section__title" id="form-title">Formulario de contacto</h2>
            <p class="section__intro">
              Fechas, número de personas, motivo. Con eso es suficiente.
            </p>
            <form class="form" action="enviar.php" method="POST">

              <div class="form__row form__row--2">
                <div class="form__field">
                  <label for="nombre">Nombre <span aria-hidden="true">*</span></label>
                  <input type="text" id="nombre" name="nombre" autocomplete="given-name" required>
                </div>
                <div class="form__field">
                  <label for="apellidos">Apellidos</label>
                  <input type="text" id="apellidos" name="apellidos" autocomplete="family-name">
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
                    <option value="reserva">Reservar habitación</option>
                    <option value="disponibilidad">Consultar disponibilidad</option>
                    <option value="congreso">Congreso / curso / evento</option>
                    <option value="grupos">Grupo de profesores / investigadores</option>
                    <option value="tribunal">Tribunal / evaluación universitaria</option>
                    <option value="otros">Otros</option>
                  </select>
                </div>
                <div class="form__field">
                  <label for="fechas">Fechas aproximadas</label>
                  <input type="text" id="fechas" name="fechas" placeholder="Ej: 10-15 julio 2026">
                </div>
              </div>

              <div class="form__field">
                <label for="mensaje">Mensaje <span aria-hidden="true">*</span></label>
                <textarea id="mensaje" name="mensaje" placeholder="Cuéntenos en qué podemos ayudarle" required></textarea>
              </div>

              <!-- Honeypot anti-spam (oculto) -->
              <div class="form__honeypot" aria-hidden="true">
                <label for="botcheck">No rellenar</label>
                <input type="checkbox" id="botcheck" name="botcheck" tabindex="-1" autocomplete="off">
              </div>

              <!-- CAPTCHA matemático -->
              <div class="form__field form__field--captcha">
                <label for="captcha">Verificación: ¿Cuánto es <strong><?php echo $n1; ?> + <?php echo $n2; ?></strong>? <span aria-hidden="true">*</span></label>
                <input type="number" id="captcha" name="captcha" min="0" max="18" required autocomplete="off" inputmode="numeric" placeholder="Escribe el resultado">
              </div>

              <label class="form__check">
                <input type="checkbox" name="rgpd" required>
                <span>He leído y acepto la <a href="politica-privacidad.html">política de privacidad</a> y el tratamiento de mis datos para gestionar mi consulta.</span>
              </label>

              <div>
                <button class="btn btn--primary btn--lg" type="submit">Enviar consulta</button>
              </div>
              <p class="form__note">Le responderemos al correo indicado en un plazo máximo de 48 h laborables.</p>
            </form>
          </div>

          <aside aria-labelledby="aside-title">
            <h2 class="section__title" id="aside-title">Dónde estamos</h2>
            <div class="info-block">
              <h3>Dirección</h3>
              <p>
                Plaza San Diego, s/n<br>
                28801 Alcalá de Henares<br>
                Madrid · España
              </p>
              <h3>Horario de atención</h3>
              <dl>
                <dt>Lunes a viernes</dt><dd>09:00 – 14:00 y 16:00 – 19:00</dd>
                <dt>Conserjería</dt><dd>24 horas, todos los días del año</dd>
              </dl>
              <h3>Contacto directo</h3>
              <p>
                <a href="tel:+34918788146">91 878 81 46</a><br>
                <a href="tel:+34918826936">91 882 69 36</a><br>
                <a href="mailto:sanildefonso@crusa.es">sanildefonso@crusa.es</a>
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
            <summary>¿Cómo realizo una reserva?</summary>
            <p>Puede reservar por teléfono llamando al 91 878 81 46 / 91 882 69 36, por email a sanildefonso@crusa.es, o a través del formulario de esta página.</p>
          </details>
          <details>
            <summary>¿Cuáles son los precios por noche?</summary>
            <p>Habitación individual: 35,00 € / noche. Habitación doble: 45,00 € / noche. Para grupos o estancias prolongadas, consulte condiciones especiales.</p>
          </details>
          <details>
            <summary>¿Están incluidos wifi y limpieza?</summary>
            <p>Sí. Todas las habitaciones incluyen wifi, calefacción, televisión y aire acondicionado y limpieza diaria sin coste adicional.</p>
          </details>
          <details>
            <summary>¿Disponen de comedor?</summary>
            <p>Sí, la Residencia cuenta con comedor propio en planta baja disponible para los huéspedes.</p>
          </details>
          <details>
            <summary>¿Aceptan grupos o congresos?</summary>
            <p>Sí. La Residencia atiende congresos, cursos, tribunales, profesores visitantes y eventos universitarios. Contacte con nosotros para condiciones especiales de grupo.</p>
          </details>
          <details>
            <summary>¿Cómo se llega desde Madrid?</summary>
            <p>A 25 km de Madrid por la Autovía A-2 (~30 min), y a 15 km del Aeropuerto de Barajas. Cercanías C2 y C7 con parada en Alcalá de Henares, y autobuses 223 y 824.</p>
          </details>
        </div>
      </div>
    </section>
  </main>

      <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-main">
        <div class="footer-col">
          <h3>Residencia San Ildefonso</h3>
          <p>Plaza San Diego, s/n<br>28801 Alcalá de Henares<br>Madrid · España</p>
          <p>
            <a href="tel:+34918788146">91 878 81 46</a><br>
            <a href="tel:+34918826936">91 882 69 36</a><br>
            <a href="mailto:sanildefonso@crusa.es">sanildefonso@crusa.es</a>
          </p>
        </div>
        <div class="footer-col">
          <h3>Universidad de Alcalá</h3>
          <ul>
            <li><a href="https://crusa.es/" rel="noopener noreferrer external">CRUSA</a> · Residencia Campus externo</li>
            <li><a href="https://portacoeli.es/" rel="noopener noreferrer external">Hospedería Porta Coeli</a> – Sigüenza</li>
            <li><a href="https://www.uah.es/" rel="noopener noreferrer external">Universidad de Alcalá</a></li>
            <li><a href="https://www.fgua.es/" rel="noopener noreferrer external">Fundación General UAH</a></li>
          </ul>
        </div>
        <div class="footer-col footer-col--logo">
          <a href="index.html" class="footer__logo-link" aria-label="Inicio">
            <img src="img/logo-san-ildefonso-transparent.png" alt="Residencia San Ildefonso" class="footer__logo" width="150" height="102">
          </a>
        </div>
        <div class="footer-col footer-col--logo">
          <a href="https://www.uah.es/" class="footer__logo-link footer__logo-link--uah" rel="noopener noreferrer external" aria-label="Universidad de Alcalá">
            <img src="img/logo-uah-blanco.png" alt="Universidad de Alcalá" class="footer__logo" width="150" height="102">
          </a>
        </div>
      </div>
      <div class="site-footer__bottom">
        <span>© 2026 Residencia Universitaria San Ildefonso UAH.</span>
        <nav class="footer-legal" aria-label="Legal">
          <a href="aviso-legal.html">Aviso legal</a>
          <a href="politica-privacidad.html">Privacidad</a>
          <a href="politica-cookies.html">Cookies</a>
        </nav>
      </div>
    </div>
  </footer>

  <aside id="cookies" class="cookies" role="region" aria-label="Aviso de cookies" hidden>
    <div class="cookies__inner">
      <p>Usamos cookies técnicas necesarias para el funcionamiento del sitio. No usamos cookies de seguimiento ni publicidad. Más información en nuestra <a href="politica-cookies.html">política de cookies</a>.</p>
      <div class="cookies__actions">
        <button class="btn btn--accent" type="button" id="cookies-accept">Aceptar</button>
        <button class="btn btn--ghost" type="button" id="cookies-reject">Rechazar</button>
      </div>
    </div>
  </aside>

  <script src="js/main.js" defer></script>
</body>
</html>
                                                                                                                                                                                                                                                                                                              