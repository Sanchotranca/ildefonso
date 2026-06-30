# Fotografías — fuentes oficiales y notas para producción

Este sitio usa, de forma temporal, **hot-linking a Wikimedia Commons**
para mostrar fotografías reales del Colegio Mayor de San Ildefonso y la
Universidad de Alcalá en el hero, las tarjetas y la galería.

> **Importante para producción**: el estándar ELIAWEB v4 exige que las
> imágenes se sirvan **localmente con dimensiones explícitas**,
> con el siguiente orden de formatos: **AVIF primero. Fallback WebP.
> Fallback final JPG.** Antes de pasar a producción definitiva hay que
> descargar cada foto, exportarla en <https://squoosh.app/> y sustituir
> el `src` actual por la ruta local (`/img/...avif` + fallback `.webp`).

## 1. Imágenes hot-linked actualmente (Wikimedia Commons · CC)

| Uso | URL `<img src>` |
|---|---|
| Hero (CSS) y card index | `https://commons.wikimedia.org/wiki/Special:FilePath/Colegio_Mayor_de_San_Ildefonso.JPG?width=...` |
| Card y galería | `https://commons.wikimedia.org/wiki/Special:FilePath/Universidad_de_Alcal%C3%A1_de_Henares,_Espa%C3%B1a_(13).JPG?width=800` |
| Card y galería | `https://commons.wikimedia.org/wiki/Special:FilePath/Universidad_de_Alcal%C3%A1_de_Henares,_Paraninfo.JPG?width=800` |
| Galería | `https://commons.wikimedia.org/wiki/Special:FilePath/Alcal%C3%A1_de_Henares_Universidad_Patio_del_Colegio_Triling%C3%BCe_.jpg?width=800` |
| Galería | `https://commons.wikimedia.org/wiki/Special:FilePath/Universidad_de_Alcal%C3%A1_(RPS_11-01-2014)_Paraninfo,_vista_sur.png?width=800` |

Páginas-fuente (con metadatos de licencia y autor):

- <https://commons.wikimedia.org/wiki/File:Colegio_Mayor_de_San_Ildefonso.JPG>
- <https://commons.wikimedia.org/wiki/File:Universidad_de_Alcal%C3%A1_de_Henares,_Espa%C3%B1a_(13).JPG>
- <https://commons.wikimedia.org/wiki/File:Alcal%C3%A1_de_Henares_Universidad_Patio_del_Colegio_Triling%C3%BCe_.jpg>
- <https://commons.wikimedia.org/wiki/Category:Paraninfo_de_la_Universidad_de_Alcal%C3%A1>
- <https://commons.wikimedia.org/wiki/Category:Colegio_Mayor_de_San_Ildefonso_(Alcal%C3%A1_de_Henares)>
- <https://commons.wikimedia.org/wiki/Category:Renaissance_facade_of_the_Colegio_Mayor_de_San_Ildefonso,_University_of_Alcal%C3%A1>

## 2. Cómo extraer fotos de fgua.es y uah.es manualmente

> Las webs `fgua.es`, `uah.es` y `crusa.es` no son accesibles desde el
> entorno de generación de este sitio (egress restringido). Para
> incorporar sus fotos hay que descargarlas manualmente desde un
> navegador y subirlas a `/img/`.

### Páginas-fuente recomendadas en fgua.es

- <https://www.fgua.es/fachada-colegio-mayor-san-ildefonso/> — encuentro sobre la fachada del Colegio (fotos de la fachada y restauración).
- <https://www.fgua.es/exposicion-fachada-san-ildefonso/> — exposición «Construcción, evolución y restauraciones (1553-2018)» (fotos antiguas y actuales).
- <https://www.fgua.es/> — portada con eventos celebrados en el Paraninfo.
- <https://www.fgua.es/contacto/> — imágenes institucionales.

### Páginas-fuente recomendadas en uah.es

- <https://www.uah.es/es/conoce-la-uah/la-universidad/edificios/Colegio-San-Ildefonso.-Rectorado/> — fotos del edificio.
- <https://www.uah.es/es/conoce-la-uah/comunicacion/> — banco de imágenes institucional (gabinete de prensa).
- <https://www.uah.es/es/vivir-la-uah/servicios/alojamiento/> — fotos generales de alojamiento.

### Páginas-fuente recomendadas en el grupo CRUSA

- <https://crusa.es/> — galería de habitaciones y zonas comunes de Campus Village.
- <https://portacoeli.es/> — fotos de la hospedería de Sigüenza (segundo establecimiento del grupo).

### Procedimiento de descarga

1. Abrir la página en un navegador con conexión normal.
2. Hacer clic derecho sobre la imagen → **«Guardar imagen como…»**.
3. Renombrar el archivo descargado con un nombre descriptivo en
   minúsculas y guiones: `fachada-plateresca.jpg`, `patio-filosofos.jpg`,
   `comedor.jpg`, `habitacion-individual.jpg`, etc.
4. Abrir <https://squoosh.app/>, arrastrar el archivo y exportar como
   **AVIF** con las dimensiones recomendadas (ver sección 3). Exportar
   también una versión **WebP** del mismo archivo como fallback.
5. Guardar ambos archivos (`nombre.avif` y `nombre.webp`) en `img/`.
6. Para `<img>`: usar `<picture>` con `<source type="image/avif">` +
   `<source type="image/webp">` + `<img src="nombre.jpg">` final.
   Para el hero CSS: `image-set(url('/img/nombre.avif') type('image/avif'), url('/img/nombre.webp') type('image/webp'))`.

### Permisos y atribución

- Las imágenes de **fgua.es / uah.es / crusa.es** son propiedad de esas
  entidades. Como gestor del sitio, CRUSA tiene derecho a reutilizarlas,
  pero conviene confirmarlo internamente y, si procede, añadir crédito
  en pie de foto.
- Las imágenes de **Wikimedia Commons** están bajo licencia Creative
  Commons. Si se mantienen en producción, hay que incluir la atribución
  al autor y la licencia indicadas en cada archivo. Recomendamos
  sustituirlas por material propio antes del lanzamiento.

## 3. Dimensiones recomendadas

| Imagen | Dimensiones | Calidad AVIF / WebP |
|---|---|---|
| Hero principal | 1600 × 900 px | 75 – 80 |
| OG image (Open Graph) | **1200 × 630 px exactos** | 75 – 80 |
| Cards / galería | 800 × 500 px | 80 |
| Tarjetas pequeñas | 600 × 400 px | 80 |

## 4. Mapeo de imágenes — qué sustituir

| Ruta actual | Lo que muestra | Sustituir por |
|---|---|---|
| `img/hero.avif` + `hero.webp` (placeholder) | Patrón generado | Foto panorámica de la fachada o del patio principal |
| `img/og-image.avif` + `og-image.webp` (placeholder) | Composición con escudo + texto | Foto representativa con texto integrado |
| `commons.wikimedia.org/.../Colegio_Mayor_de_San_Ildefonso.JPG` | Fachada plateresca | Foto propia o cesión FGUA/UAH de la fachada |
| `commons.wikimedia.org/.../Paraninfo.JPG` | Paraninfo (Premio Cervantes) | Foto del Paraninfo desde fgua.es |
| `commons.wikimedia.org/.../Patio_del_Colegio_Triling%C3%BCe.jpg` | Patio Trilingüe | Foto propia del Patio de los Filósofos |
| `gallery__item` con texto «Patio de los Filósofos», «Habitación individual», «Comedor» | Placeholders | Fotos propias / cesión CRUSA |
