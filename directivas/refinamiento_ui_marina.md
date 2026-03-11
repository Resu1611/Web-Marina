# Directiva: Refinamiento de UI/UX y Funcionalidad para Landing Page de Marina Essence Beauty

## Objetivo
Aplicar retoques finales de usabilidad y diseño responsivo a la landing page (`App.tsx`), mejorando el comportamiento en móviles (Header Sticky y Carrusel 9:16), asegurando la navegación suave de los Call to Action (CTA), y rediseñando la barra de autoridad visualmente inspirada en el material de referencia.

## Requisitos y Observaciones
1. **Header Móvil Sticky con CTA:** El header en móviles debe conservar su posición `sticky top-0 z-50`. Debe integrar el Logo y un botón prominente (ej. "Reservar") visible en todo momento.
2. **Smooth Scroll & Funcionalidad CTA:** Todos los botones de "Reservar" y "Agenda tu valoración" deben apuntar con anclaje (`href="#reserva"` o usar un handler de React) hacia la sección del formulario. Debe haber smooth scrolling (añadir `scroll-behavior: smooth` o `html { scroll-behavior: smooth; }` en el CSS global si no existe).
3. **Barra de Autoridad Rediseñada:**
   - Cambiar métrica a *"+1000 clientes"*.
   - El rediseño debe emular un fondo claro/blanco, sin el bloque sólido rojo previo.
   - Íconos en estilo "outline" delgados color borgoña (`text-[#7A1B1B]`).
   - Títulos en negro/gris oscuro, con una pequeña descripción debajo.
   - Grilla espaciada, limpia.
4. **Carrusel Móvil de Reels (9:16):**
   - En móviles, la sección de los videos verticales debe ser desbordable horizontalmente (`overflow-x-auto`).
   - Añadir características de 'snap' (`snap-x snap-mandatory`) y ocultar la barra de desplazamiento (`scrollbar-hide`).
   - En desktop, puede mantenerse el formato de grilla original de 3 columnas horizontales.

## Entradas
- `src/App.tsx` (Componente principal).
- `src/index.css` (Para inyectar `scrollbar-hide` y `scroll-behavior`).

## Salidas
- Script Python que modifique `src/index.css` y `src/App.tsx` con las implementaciones listadas, conservando las validaciones o lógica previas (si existen).

## Trampas Conocidas, Restricciones y Casos Borde
- *Scrollbar-hide:* En Tailwind CSS se puede inyectar vía `@utility scrollbar-hide` configurando las propiedades CSS nativas para webkit, edge y firefox.
- *Smooth Scrolling:* React Router podría interferir, pero al ser una landing page pura (en `App.tsx`), un simple `<html className="scroll-smooth">` o CSS global previene saltos bruscos.
- *Layout de Carrusel Móvil:* Usar `flex flex-nowrap overflow-x-auto snap-x snap-mandatory` en el contenedor padre de los items en mobile, y `md:grid md:grid-cols-3` en desktop. Los hijos en mobile necesitarán `min-w-[80vw] snap-center`.
