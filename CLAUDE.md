# LECTURA OBLIGATORIA AL ABRIR CHAT — WEB SAN ILDEFONSO

## NORMA 0 — VERIFICAR ANTES DE ACTUAR
Antes de preparar, editar o subir NADA:
1. Descargar el /index.html EN VIVO (https://www.residenciasanildefonso.es) y comprobar su estado real (curl).
2. Comprobar si el archivo/cambio YA existe en el servidor (HTTP o listado FTP).
3. Solo entonces proponer el micro-paso. Nada de rehacer trabajo ya hecho.

## COORDENADAS
- EN VIVO (canónico): https://www.residenciasanildefonso.es · Webempresa · HTTPS forzado.
- Deploy: FTP DIRECTO (no GitHub). Host cp7027.webempresa.eu · FTPS puerto 21 ·
  user MLAA@residenciasanildefonso.es · contraseña la guarda Moody.
- Docroot remoto: /home/crusaes/public_html/sitios/residenciasanildefonso.es (chroot: la cuenta FTP entra directa ahí).
- GitHub (respaldo): github.com/Sanchotranca/ildefonso · rama BUENA = master (el viejo "sildefonso" NO existe).
- El sandbox de Cowork SÍ conecta al FTP (AUTH TLS OK, verificado 2026-07-02). Puede subir si Moody da la contraseña.
- OJO OneDrive: el sandbox bash puede leer STALE/truncado desde esta carpeta. Verificar con Read tool; para deploy, usar copia en /tmp o clon de GitHub.

## ESTADO A 2026-07-02 (noche) — FASES 1 Y 2 + AUDITORÍA v4 COMPLETADAS
- LIVE = SIN galería + tagline canónico "500 años de historia / te contemplarán". Verificado byte a byte.
- AUDITORÍA ELIAWEB v4 COMPLETA (§0-§30): ver AUDITORIA-ELIAWEB-v4-2026-07-02.md en esta carpeta.
  Corregido y desplegado (commits 598b03f y d98f1ba): offline.html sin onclick/style inline + sw cache v3;
  .htaccess redirects en 1 salto sin downgrade http; h2 oculto en section Resumen del index;
  favicon-16 real; og-image.jpg fallback. Todo verificado en vivo.
- GitHub: SOLO existe master (= producción exacta). Default branch = master.
- master↔servidor verificado archivo a archivo (clon fresco vs descarga FTP completa). Diferencias restantes,
  TODAS intencionadas: enviar.php (server=gmail provisional para prueba; repo=crusa.es definitivo),
  3 imágenes huérfanas ex-galería solo en server, basura vieja .htaccess.bak/.swap solo en server,
  y docs/tooling solo en repo (no se despliegan).
- Ramas main, claude/create-residencia-website-pP3AP y gh-pages: BORRADAS.
- sanchotranca.github.io/ildefonso: APAGADA (404). Sitio Pages eliminado.
- Las 3 imágenes de la ex-galería SIGUEN en el servidor (Moody no dio OK a borrarlas):
  /img/fachada-colegio.webp, /img/habitacion-doble.webp, /img/jardin-patio.webp. Huérfanas (nadie las referencia).
- index.html.bak en servidor: NO existe (confirmado por listado FTP).

## HALLAZGOS 2026-07-02 (2ª sesión, vía cPanel/Chrome + tests)
- display_errors=Off VERIFICADO en producción (test PHP real; log_errors=On). RESUELTO.
- ⚠️ PHP REAL = 7.4.33 (EOL, sin parches desde 2022), NO 8.2 como decía el registro del 30-06.
  Se intentó cambiar a 8.2 en wePanel (Versiones PHP → fila residenciasanildefonso.es → Modificar):
  el diálogo acepta pero NO se aplica (verificado con test PHP). Hipótesis: los dominios "(Principal)"
  heredan del principal crusa.es (7.4, NO TOCAR: negocio). PENDIENTE: Moody a mano o ticket a Webempresa.
- Lighthouse REAL 2026-07-02 (pagespeed.web.dev): móvil 100/100/100/100 + agéntica 3/3 · FCP 0,8s · LCP 0,8s · TBT 0 · CLS 0.
- Estrés: Webempresa aplica rate-limit por IP (~6s castigo) ante ráfagas → NO hacer load-testing contra
  producción (misma cuenta que crusa.es). El sitio se recupera solo; visitantes normales no afectados.
- wePanel tiene editor INI por dominio: Versiones PHP → menú de fila → "Configuración PHP".

## PENDIENTE MENOR
- Moody: borrar el token GitHub "fase2-ildefonso" (github.com/settings/personal-access-tokens) — ya no hace falta.
- La contraseña FTP se pegó en el chat 2026-07-02: cambiarla si Moody quiere.
- (Opcional futuro) borrar las 3 imágenes huérfanas de /img/ con OK explícito.
Decisiones cerradas: tagline canónico = el de LIVE; barajado aleatorio de galería CANCELADO.

## NORMAS DE TRATO
- Español. Micro-pasos con final claro. Mapa antes de ejecutar. Directo, sin paja.
- Nada de borrar/mover/publicar sin lista exacta + OK explícito de Moody.
- Dato sin fuente verificable = no existe. "No lo sé" obligatorio.
- Si algo falla: PARAR, describir el error, esperar instrucción.
- Al terminar: actualizar ESTADO & MEMORIA en Drive /Sistema-MOODY.
