# Runbook de despliegue — residenciasanildefonso.es

Cuando esté todo listo, este es el guion completo. Está dividido en
tres bloques: lo que tiene que hacer un humano antes de pulsar deploy,
el deploy en sí, y las verificaciones post-deploy.

---

## ⏳ A. Pre-deploy (acciones humanas, ~30 min)

| # | Acción | Dónde |
|---|---|---|
| 1 | **Clave Web3Forms**: registrar `sanildefonso@crusa.es` en <https://web3forms.com>, copiar la access_key. | web3forms.com |
| 2 | Sustituir `TU_ACCESS_KEY_AQUI` por la clave real | `contacto.html` (línea con `name="access_key"`) |
| 3 | **Coordenadas GPS exactas** de la Plaza San Diego (las actuales son aproximadas: `40.482236, -3.363976`). Verificar en Google Maps. | `scripts/build.py` (`GEO_LAT`, `GEO_LON`) y regenerar con `python3 scripts/build.py`. También en `css/style.css` si se quiere mover el centro del mapa. |
| 4 | **Fotos reales** (opcional pero recomendable): seguir `img/PHOTOS.md` para descargar de fgua.es / uah.es / crusa.es y sustituir los WebP locales sin cambiar nombre. | `img/` |
| 5 | Merge de la rama de desarrollo a `main`: `git checkout main && git merge claude/create-residencia-website-pP3AP && git push origin main` | local / GitHub |

---

## 🚀 B. Deploy (en cPanel + GitHub, ~15 min la primera vez)

### Opción A — cPanel Git Version Control (recomendada por el estándar ELIAWEB v4)

1. cPanel → buscar **"Git™ Version Control"**.
2. Crear nuevo repositorio:
   - **Clone URL**: `https://github.com/sanchotranca/ildefonso.git`
   - **Repository Path**: `/home/usuario/repos/ildefonso`
   - **Repository Name**: `ildefonso`
3. Crear el archivo `.cpanel.yml` en la raíz del repo (ver más abajo) con
   la regla de despliegue a `public_html`.
4. En la pestaña **"Pull or Deploy"** → **Deploy HEAD Commit**.
5. Activar webhook GitHub → cPanel (en algunos hostings se hace solo;
   en otros hay que poner una URL de webhook en GitHub repo settings).

Contenido de `.cpanel.yml` (te lo dejo creado, ver siguiente paso):

```yaml
---
deployment:
  tasks:
    - export DEPLOYPATH=/home/usuario/public_html/
    - /bin/cp -R ./*.html $DEPLOYPATH
    - /bin/cp -R ./css $DEPLOYPATH
    - /bin/cp -R ./js $DEPLOYPATH
    - /bin/cp -R ./img $DEPLOYPATH
    - /bin/cp ./.htaccess $DEPLOYPATH
    - /bin/cp ./robots.txt $DEPLOYPATH
    - /bin/cp ./sitemap.xml $DEPLOYPATH
    - find $DEPLOYPATH -type d -exec chmod 755 {} \;
    - find $DEPLOYPATH -type f -exec chmod 644 {} \;
```

> Sustituir `usuario` por el username de cPanel.

### Opción B — GitHub Actions con FTP/SFTP

Si el cPanel no tiene Git Version Control, usar el workflow
`.github/workflows/deploy.yml` (te lo dejo creado en el repo, listo
para activar con tres secrets de GitHub).

### Opción C — Vercel / Netlify / Cloudflare Pages

Si decides no usar cPanel:

1. Login en Vercel/Netlify/CF Pages con la cuenta de GitHub.
2. Import del repo `sanchotranca/ildefonso`.
3. Framework: **Other** (es HTML puro).
4. Build command: *(vacío)*.
5. Output directory: `.`.
6. Deploy automático en cada push a `main`.
7. Conectar el dominio `residenciasanildefonso.es` con los DNS que
   indique la plataforma.
8. **Importante**: estas plataformas ignoran `.htaccess`. Si vas por
   esta vía hay que traducir las reglas a `vercel.json` /
   `_headers` + `_redirects` (Netlify) / `_headers` (Cloudflare). Lo
   puedo generar cuando elijas plataforma.

---

## ✅ C. Post-deploy (verificaciones, ~15 min)

| # | Comprobación | Cómo | Esperado |
|---|---|---|---|
| 1 | HTTPS forzado | Visitar `http://residenciasanildefonso.es` | Redirige 301 a `https://www.…` |
| 2 | www forzado | Visitar `https://residenciasanildefonso.es` | Redirige 301 a `https://www.…` |
| 3 | 404 personalizada | Visitar `/no-existe` | Página 404 con diseño del sitio |
| 4 | robots.txt accesible | `/robots.txt` | Contenido visible |
| 5 | sitemap.xml accesible | `/sitemap.xml` | XML con 8 URLs |
| 6 | Cabeceras de seguridad | <https://securityheaders.com/?q=residenciasanildefonso.es> | Grade A o A+ |
| 7 | Mozilla Observatory | <https://observatory.mozilla.org/analyze/residenciasanildefonso.es> | B mínimo, A+ con todo bien |
| 8 | SSL Labs | <https://www.ssllabs.com/ssltest/analyze.html?d=residenciasanildefonso.es> | A o A+ |
| 9 | PageSpeed Mobile | <https://pagespeed.web.dev/?url=residenciasanildefonso.es> | > 90 si se autohospedan las fuentes |
| 10 | Rich Results | <https://search.google.com/test/rich-results?url=residenciasanildefonso.es> | LodgingBusiness, BreadcrumbList, FAQ válidos |
| 11 | Mobile-Friendly | <https://search.google.com/test/mobile-friendly?url=residenciasanildefonso.es> | "Apta para móviles" |
| 12 | Formulario contacto | Enviar consulta de prueba | Llega email a `sanildefonso@crusa.es` |
| 13 | Mapa carga bajo demanda | Abrir `/contacto.html`, comprobar DevTools Network | Cero peticiones a google.com hasta clic |
| 14 | Cookies | Borrar localStorage, recargar | Banner aparece, Aceptar/Rechazar funcionan |
| 15 | Google Search Console | <https://search.google.com/search-console> | Añadir propiedad, verificar, enviar `sitemap.xml` |
| 16 | Google Business Profile | <https://business.google.com> | Actualizar URL con `https://www.residenciasanildefonso.es/` y verificar NAP |

---

## 🔄 Workflow en marcha

Una vez configurado:

```
Editar local → git commit → git push main → cPanel auto-deploy → web actualizada
```

Tiempo desde push hasta web actualizada: **< 30 segundos** con cPanel Git.
