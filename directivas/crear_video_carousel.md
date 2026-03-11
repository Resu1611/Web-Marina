# Directiva: Componente Modular VideoCarousel (Reels)

## Objetivo
Implementar un carrusel móvil deslizable de videos verticales (formato Reels 9:16) en la sección "Conoce nuestro trabajo" de la landing. Este componente debe ser modular, optimizado para gestos (swipe) en iOS/Android y fácil de mantener (mediante una constante de videos).

## Entradas
- `src/App.tsx` (se insertarán el componente `VideoCarousel` y la constante `VIDEO_LIST`).
- Videos futuros en `public/videos/`.

## Salidas
- Código de React modular.
- Refactorización de la UI de videos estáticos (actual) al nuevo sistema `VideoCarousel`.

## Lógica y Construcción Estricta

### 1. La Fuente de Datos
Definir un array llamado `VIDEO_LIST` fuera del ciclo de vida del componente React. 
**Regla OBLIGATORIA:** Agregar el comentario exacto de mantenimiento: `// PARA AÑADIR VIDEOS: Sube el .mp4 a la carpeta 'public/videos' y añade el nombre del archivo a esta lista.`

### 2. El Componente Nativo `<video>` (Para móviles)
Al mapear el array `VIDEO_LIST`, es **CRÍTICO** para el funcionamiento en la web de móviles (especialmente Safari iOS y Chrome Android) que las etiquetas `<video>` tengan los siguientes atributos exactos por política de auto-play:
`autoPlay`, `muted`, `loop`, `playsInline`. (Cualquier omisión pausará los videos o forzará la pantalla completa).

Atributos CSS: `aspect-[9/16] object-cover w-full h-full rounded-2xl` aseguran simetría.

### 3. Comportamiento del Carrusel
Padre: Flexbox con overflow horizontal controlado.
Clases Tailwind: `flex overflow-x-auto snap-x snap-mandatory gap-4 pb-4 scrollbar-hide`
Hijos: Enclavamiento magnético al centro en el swipe de pantalla.
Clases Tailwind: `snap-center shrink-0 w-[80vw] max-w-[300px]`

## Trampas Conocidas, Restricciones y Casos Borde
- *Políticas de Reproducción:* Si el video NO tiene el atributo `muted`, iOS y navegadores Chromium prevendrán categóricamente el `autoPlay` para ahorrar batería y evitar sonido intrusivo a los usuarios.
- *Pantalla Completa Automática iOS:* Si NO se incluye `playsInline`, Safari iOS podría interceptar cada video y reproducirlos de forma odiosa a pantalla completa en lugar de correr silenciosamente en el layout. ESTA REGLA ES ABSOLUTA.
- *Renderizado Roto de `FadeInUp` con Snap:* Evitar envolver cada "snap child" del carrusel en un IntersectionObserver (FadeInUp) individual porque rompería las coordenadas de `scroll-snap-type` nativo del navegador causando saltos o desalineamientos. Englobar el *padre completo* de ser necesario.
