// Residencia San Ildefonso — JS mínimo: hero shuffle + navegación móvil + cookies + PWA
(function () {
  "use strict";
  // Activar CSS diferido (CSP-safe, sustituye al onload inline)
  document.querySelectorAll('link[media="print"]').forEach(function (link) { link.media = "all"; });


  // ---------- Service Worker (PWA básico §26) ----------
  // Registro tras 'load' para no competir con el critical path.
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("/sw.js").catch(function () { /* silencioso */ });
    });
  }

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
      // §30H — bloquea scroll del body al abrir nav móvil (evita scroll-through en iOS)
      document.body.style.overflow = open ? "hidden" : "";
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

  // ---------- Validación inline en formularios (mensajes ES) ----------
  // Mensajes específicos en español por campo y por tipo de validez.
  // Se disparan al perder el foco (blur) y al intentar enviar.
  // Se limpian al teclear (input) para no acosar mientras escribe.
  const VALIDATION_MESSAGES = {
    nombre: {
      valueMissing: "Indícanos tu nombre, por favor."
    },
    email: {
      valueMissing: "Indícanos tu correo electrónico.",
      typeMismatch: "Comprueba el correo (ejemplo: nombre@dominio.es)."
    },
    mensaje: {
      valueMissing: "Cuéntanos brevemente en qué podemos ayudarte."
    },
    captcha: {
      valueMissing: "Resuelve la suma para verificar que no eres un bot.",
      badInput:     "Escribe solo el número resultado de la suma.",
      rangeOverflow: "Comprueba el resultado: parece demasiado alto.",
      rangeUnderflow: "Comprueba el resultado: no puede ser negativo."
    },
    rgpd: {
      valueMissing: "Para enviar, debes aceptar la política de privacidad."
    }
  };
  document.querySelectorAll("form.form [name]").forEach(function (field) {
    const msgs = VALIDATION_MESSAGES[field.name];
    if (!msgs) return;
    field.addEventListener("blur", function () { field.checkValidity(); });
    field.addEventListener("invalid", function () {
      const v = field.validity;
      let msg = "";
      if (v.valueMissing && msgs.valueMissing)        msg = msgs.valueMissing;
      else if (v.typeMismatch && msgs.typeMismatch)   msg = msgs.typeMismatch;
      else if (v.badInput && msgs.badInput)           msg = msgs.badInput;
      else if (v.rangeOverflow && msgs.rangeOverflow) msg = msgs.rangeOverflow;
      else if (v.rangeUnderflow && msgs.rangeUnderflow) msg = msgs.rangeUnderflow;
      if (msg) field.setCustomValidity(msg);
    });
    field.addEventListener("input", function () { field.setCustomValidity(""); });
  });

  // ---------- Feedback de envío en formularios ----------
  // Al pasar la validación HTML5 y dispararse submit, deshabilita el botón
  // y cambia su texto a "Enviando…" para evitar doble envío y dar feedback
  // visible. Si el servidor redirige a contacto.php?error=1 la página se
  // recarga y el botón vuelve a su estado inicial.
  document.querySelectorAll("form.form").forEach(function (form) {
    form.addEventListener("submit", function () {
      const btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.dataset.labelOriginal = btn.textContent;
        btn.textContent = "Enviando…";
      }
    });
  });

  // ---------- Banner de cookies (LSSI/RGPD) ----------
  const KEY    = "rsi-cookies-v1";
  const banner = document.getElementById("cookies");

  // Botón "Configurar cookies" (footer): revoca el consentimiento previo,
  // borra la preferencia guardada y vuelve a mostrar el banner. Cumple §16B
  // "Permitir retirar el consentimiento igual de fácil que darlo".
  const cookiesConfigBtn = document.getElementById("cookies-config");
  if (cookiesConfigBtn && banner) {
    cookiesConfigBtn.addEventListener("click", function () {
      try { localStorage.removeItem(KEY); } catch (e) {}
      banner.hidden = false;
      banner.scrollIntoView({ behavior: "smooth", block: "end" });
    });
  }

  if (!banner) return;

  let stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}
  if (stored === "accepted" || stored === "rejected") {
    banner.hidden = true;
    return;
  }
  banner.hidden = false;

  function setChoice(value) {
    try { localStorage.setItem(KEY, value); } catch (e) {}
    banner.hidden = true;
  }
  const btnAccept = document.getElementById("cookies-accept");
  const btnReject = document.getElementById("cookies-reject");
  if (btnAccept) btnAccept.addEventListener("click", function () { setChoice("accepted"); });
  if (btnReject) btnReject.addEventListener("click", function () { setChoice("rejected"); });
}());
