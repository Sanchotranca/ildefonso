// Residencia San Ildefonso — JS mínimo: navegación móvil + cookies
(function () {
  "use strict";

  // ---------- Navegación móvil ----------
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    var setNav = function (open) {
      nav.setAttribute("data-open", open ? "true" : "false");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Cerrar menú de navegación" : "Abrir menú de navegación");
    };
    toggle.addEventListener("click", function () {
      setNav(nav.getAttribute("data-open") !== "true");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.matches("a") && window.matchMedia("(max-width: 899px)").matches) {
        setNav(false);
      }
    });
    // Cerrar con Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.getAttribute("data-open") === "true") setNav(false);
    });
  }

  // ---------- Mapa con carga bajo demanda (facade pattern) ----------
  var mapTrigger = document.getElementById("map-trigger");
  if (mapTrigger) {
    mapTrigger.addEventListener("click", function () {
      var iframe = document.createElement("iframe");
      iframe.src = "https://www.google.com/maps?q=40.482236,-3.363976&z=17&output=embed";
      iframe.title = "Mapa: Plaza San Diego, Alcalá de Henares";
      iframe.loading = "lazy";
      iframe.referrerPolicy = "no-referrer";
      // Sandbox: lo mínimo que necesita Google Maps embed para funcionar.
      // Bloquea top-navigation, pointer-lock, modals, presentation mode.
      iframe.setAttribute("sandbox", "allow-scripts allow-same-origin allow-popups allow-forms");
      iframe.setAttribute("allowfullscreen", "");
      iframe.className = "map__frame";
      mapTrigger.replaceWith(iframe);
    });
  }

  // ---------- Banner de cookies (LSSI/RGPD) ----------
  var KEY = "rsi-cookies-v1";
  var banner = document.getElementById("cookies");
  if (!banner) return;

  var stored = null;
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
  var btnAccept = document.getElementById("cookies-accept");
  var btnReject = document.getElementById("cookies-reject");
  if (btnAccept) btnAccept.addEventListener("click", function () { setChoice("accepted"); });
  if (btnReject) btnReject.addEventListener("click", function () { setChoice("rejected"); });
})();
