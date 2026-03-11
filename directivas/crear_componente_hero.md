# Directiva: Refactorización Hero a Fullscreen por Capas

## Objetivo
Reemplazar el anterior Header Hero centrado y minimalista por un componente inmersivo de pantalla completa (Fullscreen) usando una arquitectura estricta por capas visuales superpuestas mediante `z-index`, `absolute` y `relative`. Además, se persigue que el Sticky Nav adapte su contraste frente a este fondo oscuro.

## Entradas
- `src/App.tsx`.
- Imagen provista de Unsplash: `https://images.unsplash.com/photo-1516975080661-422fc99101f4?q=80&w=1920&auto=format&fit=crop`.

## Salidas
- Nuevo componente funcional React `<Hero />`.
- Eliminación del código Hero anterior.
- Modificación dinámica de color del Sticky Nav de negro a blanco según posición.

## Lógica y Construcción Estricta por Capas

1.  **CAPA CERO (Base):** Contenedor padre `<section>` con clase `min-h-screen relative overflow-hidden flex flex-col justify-end md:justify-center z-0`. El overflow hidden previene problemas de márgenes, y el flex justify garantiza que en móviles el texto repose en la base, y en escritorio quede centrado a la izquierda por su margen.

2.  **CAPA UNO (Imagen):** `<img>` con `absolute inset-0 w-full h-full object-cover -z-20`. Un comentario obligatorio debe insertarse: `// TODO: Reemplazar esta URL por la imagen o video real del cliente.`

3.  **CAPA DOS (Gradiente):** `<div>` vacío usando `absolute inset-0 -z-10`. Debe ser dual y responsivo.
    *Móvil (default):* `bg-gradient-to-t from-[#1A1A1A] via-[#1A1A1A]/70 to-transparent` (Cubre el 100% en bottom).
    *Desktop (`md:`):* `md:bg-gradient-to-r md:from-[#1A1A1A] md:via-[#1A1A1A]/80 md:to-transparent` (Cubre Left, liberando el rostro).

4.  **CAPA TRES (Texto/Botón):** Contenedor relativo en `z-10` con `max-w-7xl pb-16 pt-32 px-6`.
    - Botón `Agendar mi Cita`: `bg-[#F4F0EA] text-[#1A1A1A] hover:bg-white rounded-full px-8 py-4.5 font-medium`.

## Trampas y Dependencias Modificadas
- *NavBar Oscura Invisible:* Al insertar un fondo sombrío a pantalla completa, la variante 'transparente' del `header` ya no puede mostrar texto gris oscuro `text-gray-700`. **Se sustituirán condicionalmente** (`isScrolled ? 'text-gray-700' : 'text-white'`) el texto del menú, el logo y el ícono de hamburguesa para garantizar alto contraste durante los primeros instantes del usuario. En tanto no hay SVG del logo blanco, usaremos filtros CSS temporales si la imagen PNG es oscura `invert(1)` o alternarla.
