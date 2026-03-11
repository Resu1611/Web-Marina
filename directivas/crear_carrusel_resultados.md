# Directiva: Carrusel Resultados Infinito y con Botones (Desktop)

## Objetivo
Evolucionar la sección `Resultados Reales` para que el carrusel táctil actual posea controles de avance lateral (`ChevronLeft`, `ChevronRight`) exclusivos para visualización de Desktop y simule un scroll infinito mediante la clonación del array (3x). El Botón de Agendar debe conservarse por debajo de esto.

## Entradas
- `src/App.tsx`.
- Dependencias base de `lucide-react`: Importar explicitamente `ChevronLeft` y `ChevronRight` si falta `ChevronLeft`.

## Salidas
- Nuevo componente `ResultadosCarousel` manejando estado `useRef`.
- El bloque `<section id="resultados">` que consume al componente interno.

## Lógica y Pasos a Inyectar

1.  **Imports Adicionales:**
    Asegurarse de que `ChevronLeft` esté importado de `lucide-react`.

2.  **Constante (Ya Inyectada Previamente):**
    `RESULTADOS_LIST` permanece en la zona superior (solo para lectura).

3.  **El Componente `ResultadosCarousel`:**
    Inyectar ANTES de `export default function App()`.
    - **Ref:** `const scrollRef = useRef<HTMLDivElement>(null);`
    - **Duplicado:** `const infiniteList = [...RESULTADOS_LIST, ...RESULTADOS_LIST, ...RESULTADOS_LIST];`
    - **Función de Navegación:**
      ```tsx
      const scroll = (direction: 'left' | 'right') => {
        if (scrollRef.current) {
          const scrollAmount = window.innerWidth > 768 ? 450 : 320;
          scrollRef.current.scrollBy({ left: direction === 'left' ? -scrollAmount : scrollAmount, behavior: 'smooth' });
        }
      };
      ```
    - **Render:** Estructura con un div padre (con `group relative`), los dos botones envolviendo el div central que tiene el `ref={scrollRef}` y el `overflow-x-auto snap-x scrollbar-hide`.
    - NOTA: Requerimos la utilidad `React` referenciada si no estaba, pero ya lo está usando el `App`.

4.  **Sustitución en el DOM Principal:**
    Buscar la iteración anterior del carrusel `{RESULTADOS_LIST.map...}` y sustituirla por:
    `<ResultadosCarousel />`
    Mientras se mantiene intacto el botón de CTA:
    `<div className="text-center mt-6 px-6"><button onClick={scrollToReserva}...>`

## Trampas Conocidas y Casos Borde
- *Scroll Snap Choppy:* Si se hace click rápido en los botones de "derecha" antes de que termine el movimiento de *smooth behavior*, algunos navegadores rompen el enclavamiento. React Native tiene `pagingEnabled` pero en CSS la combinación `smooth` y `mandatory` funciona con decencia razonable para una web.
- *Z-Index de Botones:* Los botones Izq/Der DEBEN tener un `z-index` adecuado (`z-20` p.ej.) y ser `absolute` en el contenedor relativo para flotar sobre las tarjetas sin cortarlas ni moverlas.
- *Keys Únicos en Map Infinito:* Al triplicar el array, los `img.id` se repiten 3 veces. Es ABSOLUTAMENTE CRÍTICO renderizar las llaves de React así: `key={`${img.id}-${idx}`}`. Si no, React arrojará graves errores en consola y arruinará el performance del render.
