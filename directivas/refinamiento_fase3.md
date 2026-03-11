# Directiva: Refinamiento de Cabecera y Reducción de Videos (Fase 3)

## Objetivo
Resolver un problema de dimensionamiento en el carrusel de videos para la versión móvil, reduciendo su anchura máxima, y rediseñar el Header pegajoso ("Sticky") para simular una "cápsula" flotante (estilo PatientFlow), preservando el esquema de colores de la marca (mantiene logos en crema/blanco y elementos granates).

## Entradas
- `src/App.tsx`.

## Salidas
- Script Python que modifique `src/App.tsx` para aplicar las mejoras.

## Lógica y Pasos Recomendados

### 1. Dimensionamiento de videos en Móvil
En la sección del "Arte en Movimiento" (Reels), el contenedor interno que envuelve el `.aspect-[9/16]` está ocupando demasiado ancho. 
Modificar la clase:
- **Antes:** `className="snap-center shrink-0 min-w-[78vw] md:min-w-0 md:w-full"`
- **Ahora:** `className="snap-center shrink-0 w-[75vw] sm:w-[320px] md:w-full md:min-w-0"`
Esto forzará a que no ocupe un porcentaje excesivo de la pantalla, dejando un margen visible lateral para invitar al swipe iterativo.

### 2. Header Estilo "Cápsula Flotante"
Transformar el `<header>` que ocupa el 100% de la pantalla base a un contenedor envuelto, que cuando se haga el scroll (isScrolled===true), se transforme en una barra encapsulada (pill-shaped) flotando ligeramente (margin-top y max-width reducidos).
- Envolver el elemento lógico `<header>` en un div padre fijo: `fixed top-0 left-0 w-full z-50 flex justify-center p-4 pointer-events-none`.
- El header mismo recibe `pointer-events-auto w-full transition-all duration-500 ease-in-out`.
- Su variante dinámica (`isScrolled`): 
  - *True:* `max-w-5xl bg-white/95 backdrop-blur-lg shadow-[0_8px_32px_rgba(122,27,27,0.12)] border border-[#7A1B1B]/10 rounded-full py-2.5 px-4 md:px-6`
  - *False:* `max-w-7xl bg-transparent py-2 md:py-4 px-2 md:px-6 border-transparent`
- Adaptar el menú móvil absoluto (`mobileMenuOpen`) para que caiga elegantemente debajo de la burbuja (p.e. `top-[calc(100%+0.5rem)] rounded-3xl`).

## Trampas Conocidas, Restricciones y Casos Borde
- *Eventos Puntero (pointer-events):* Si se envuelve en un contenedor fijo de padding global, hay que usar `pointer-events-none` en el padre y `pointer-events-auto` en el hijo (`header`) para que el usuario pueda hacer click en áreas de la pantalla a los lados del header.
- *Logo Dark:* Ya que el logo insertado es oscuro (letras de Marina son burgundy), la burbuja DEBE ser clara en todo momento.
- *Menú Móvil Desconectado:* Al hacer el header redondeado, un dropdown rectangular cortaría la UI de forma brusca, por lo que el dropdown debe también redondearse fuertemente (`rounded-3xl`).
