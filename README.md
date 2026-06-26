# Residencia Universitaria San Ildefonso — Sitio web

Sitio estático en HTML5 + CSS para `residenciasanildefonso.es`, construido
siguiendo el estándar interno **ELIAWEB v4** (mayo 2026).

## Estructura

```
/
├── index.html
├── residencia.html
├── habitaciones.html
├── servicios.html
├── contacto.html
├── gracias.html
├── 404.html
├── aviso-legal.html
├── politica-privacidad.html
├── politica-cookies.html
├── robots.txt
├── sitemap.xml
├── .htaccess
├── .cursorrules
├── css/
│   └── style.css            # Único CSS con cascade layers
├── js/
│   └── main.js              # Navegación móvil + banner cookies
├── img/
│   ├── crest.svg            # Escudo institucional
│   ├── favicon.ico
│   ├── favicon-32.png
│   ├── apple-touch-icon.png
│   ├── og-image.webp        # Imagen Open Graph 1200×630
│   ├── og-image.jpg         # Fallback JPG
│   ├── hero.webp            # Hero principal
│   └── hero.jpg
├── fonts/                   # (vacío — fuentes vía Google Fonts)
└── php/                     # (reservado, no se usa)
```

## Cumplimiento del estándar

- HTML5 semántico, un único `<h1>` por página, jerarquía sin saltos.
- CSS con `@layer reset, base, layout, components, utilities, motion, print;`
  y **sin `!important`** en ninguna regla.
- Mobile first con breakpoints en `600px`, `900px` y `1200px`.
- Variables CSS en `:root` para colores, tipografía y `--space-xs/sm/md/lg/xl`.
- BEM para todos los componentes.
- Tipografía fluida con `clamp()`. Tamaño mínimo body 16px.
- `<head>` completo en cada página: title, description, canonical, OG, Twitter,
  favicons, preload de fuentes y `application/ld+json` con `LodgingBusiness`.
- NAP idéntico (nombre + dirección + teléfono) en footer y JSON-LD.
- Interlinking: header, footer y CTAs cruzadas; sin páginas huérfanas.
- Formulario de contacto con **Web3Forms**, honeypot y casilla RGPD.
- Banner de cookies con Aceptar/Rechazar y persistencia en `localStorage`.
- Páginas legales: aviso legal, política de privacidad, política de cookies.
- 404 personalizada con diseño del sitio.
- `.htaccess`: HTTPS forzado, redirección a `www`, caché, gzip,
  cabeceras de seguridad (HSTS, X-Frame-Options, Referrer-Policy,
  Permissions-Policy), bloqueo de archivos sensibles.
- `robots.txt` + `sitemap.xml`.

## Tareas pendientes antes del despliegue

1. **Web3Forms**: registrar `sanildefonso@crusa.es` en
   <https://web3forms.com> y sustituir `TU_ACCESS_KEY_AQUI` en
   `contacto.html` por la clave real (250 envíos/mes gratis).
2. **Imágenes reales**: sustituir los placeholders generados
   (`hero.*`, `og-image.*`) por fotografías reales de la Residencia
   comprimidas en <https://squoosh.app/>.
3. **Geolocalización**: revisar `latitude` / `longitude` del JSON-LD
   en cada `<head>` (valor actual aproximado de la Plaza San Diego).
4. **Google Search Console**: verificar propiedad y enviar
   `sitemap.xml`. Crear/actualizar **Google Business Profile** con NAP
   idéntico al del sitio.
5. **PageSpeed**: validar > 90 en móvil tras subir imágenes finales.
6. **Despliegue**: configurar **cPanel → Git Version Control** apuntando
   al repositorio para auto-deploy en cada push a `main`.

## Datos verificados (mayo 2026)

- **Dirección**: Plaza San Diego, s/n · 28801 Alcalá de Henares (Madrid)
- **Teléfono Residencia**: +34 91 878 81 46
- **Teléfono CRUSA**: +34 911 81 71 01
- **Email Residencia**: sanildefonso@crusa.es
- **Email CRUSA**: info@crusa.es
- **Titular / gestión**: Ciudad Residencial Universitaria, S.A. (CRUSA),
  sociedad anónima unipersonal participada por la Universidad de Alcalá
- **CIF**: A-80991714 (verificado en portacoeli.es/aviso-legal y registros mercantiles)
- **Ubicación**: Patio de los Filósofos del Colegio Mayor de San Ildefonso
- **Capacidad**: 41 habitaciones (individuales y dobles) con baño privado
- **Tarifas orientativas**:
  - Individual: 365 €/mes
  - Doble: 270 €/mes/persona
  - Pensión completa: +300 €/mes (L–V)
  - Media pensión: +170 €/mes (L–V)
  - Fianza: 300 €
- **Patrimonio**: el Colegio de San Ildefonso es Patrimonio de la Humanidad
  UNESCO desde 1998.

Fuentes: páginas de la Universidad de Alcalá, Uniscopio, CampusHabit y
Residenciasuniversitarias.es.
