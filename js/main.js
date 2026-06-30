// Residencia San Ildefonso — JS mínimo: hero shuffle + navegación móvil + cookies
(function () {
  "use strict";

  // ---------- Hero — barajar franjas fotográficas (Fisher-Yates) ----------
  // Las imágenes viven en atributos data-bg / data-pos (sin style="" en el HTML).
  const heroImgs = Array.from(document.querySelectorAll('.hero__strip-img'));
  if (heroImgs.length) {
    const bgs = heroImgs.map(function (el) {
      return {
        bg:  el.dataset.bg  || '',
        pos: el.dataset.pos || 'center center'
      };
    });
    for (let i = bgs.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = bgs[i]; bgs[i] = bgs[j]; bgs[j] = tmp;
    }
    heroImgs.forEach(function (el, k) {
      el.style.backgroundImage    = "url('" + bgs[k].bg + "')";
      el.style.backgroundPosition = bgs[k].pos;
    });
  }

  // ---------- Navegación móvil ----------
  const toggle = document.querySelector(".nav-toggle");
  const nav    = document.querySelector(".main-nav");
  if (toggle && nav) {
    const setNav = function (open) {
      nav.setAttribute("data-open",     open ? "true" : "false");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label",
        open ? "Cerrar menú de navegación" : "Abrir menú de navegación");
    };
    toggle.addEventListener("click", function () {
      setNav(nav.getAttribute("data-open") !== "true");
    });
    nav.addEventListener("click", function (e) {
      // 899px ÷ 16 = 56.1875em — coincide con el breakpoint del CSS
      if (e.target.matches("a") && window.matchMedia("(max-width: 56.1875em)").matches) {
        setNav(false);
      }
    });
    // Cerrar con Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.getAttribute("data-open") === "true") setNav(false);
    });
  }

  // ---------- Mapa con carga bajo demanda (facade pattern) ----------
  const mapTrigger = document.getElementById("map-trigger");
  if (mapTrigger) {
    mapTrigger.addEventListener("click", function () {
      const iframe = document.createElement("iframe");
      iframe.src = "https://www.google.com/maps?q=40.482236,-3.363976&z=17&output=embed";
      iframe.title = "Mapa: Plaza San Diego, Alcalá de Henares";
      iframe.loading = "lazy";
      iframe.referrerPolicy = "no-referrer";
      // Sandbox: mínimo necesario para Google Maps embed.
      iframe.setAttribute("sandbox", "allow-scripts allow-same-origin allow-popups allow-forms");
      iframe.setAttribute("allowfullscreen", "");
      iframe.className = "map__frame";
      mapTrigger.replaceWith(iframe);
    });
  }

  // ---------- Bann