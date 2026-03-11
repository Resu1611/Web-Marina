# Directiva: Re-enmarcado Hero y Botón Borgoña

## Objetivo
Optimizar la visibilidad de la modelo en la versión móvil levantando todo el bloque de texto hacia el techo de la pantalla, invirtiendo la dirección del gradiente oscuro, y consolidando el Botón de Llamada a la Acción (CTA) hacia un color primario agresivo pero elegante (Borgoña `#7A1B1B`) con animación constante. 

## Entradas
- `src/App.tsx`.
- `src/index.css`.

## Salidas
- CSS ampliado con `@utility animate-pulse-shadow`.
- `<Hero>` refactorizado.
- Función de Ancla `#formulario-contacto` funcional.

## Lógica y Pasos a Inyectar

1.  **Animaciones CSS Personalizadas (`index.css`):**
    Para lograr el `animate-pulse-shadow`, no podemos depender del pulse de opacidad de Tailwind. Debemos inyectar:
    ```css
    @utility animate-pulse-shadow {
      animation: pulse-shadow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    @keyframes pulse-shadow {
      0% { box-shadow: 0 0 0 0 rgba(122, 27, 27, 0.4); }
      70% { box-shadow: 0 0 0 15px rgba(122, 27, 27, 0); }
      100% { box-shadow: 0 0 0 0 rgba(122, 27, 27, 0); }
    }
    ```

2.  **Inversión de Gradiente del Hero:**
    Cambiar la dirección `to-t` por `to-b` en la Capa 2 protectora:
    `bg-gradient-to-b from-[#111111] via-[#111111]/95 md:via-[#111111]/80 to-transparent`

3.  **Desplazamiento de Masa de Texto:**
    Sustituir la clase responsiva del contenedor `z-10`:
    `mt-auto pt-32 pb-12` -> `mt-[12vh] pt-12 pb-12`
    Esto ancla el texto en la zona del 12% vertical, bajando tras el Sticky Header.

4.  **Botón Primario Borgoña:**
    El botón actual se reemplaza por el siguiente bloque con sombra difuminada `#8B1C24/10` y pulso:
    ```tsx
          <a 
            href="#formulario-contacto" 
            onClick={scrollToReserva}
            className="inline-flex items-center justify-center gap-3 bg-[#7A1B1B] text-white px-8 md:px-10 py-3.5 md:py-4 mt-2 md:mt-8 rounded-full font-sans font-medium text-base md:text-lg transition-all duration-300 shadow-xl shadow-[#8B1C24]/10 animate-pulse-shadow hover:bg-[#5A1414] hover:-translate-y-1 hover:scale-[1.02] w-full sm:w-auto"
          >
            Agendar Cita
          </a>
    ```

5.  **Refactorización Formulario:**
    El ID `reserva` desaparece en favor de `formulario-contacto`. El método `scrollToReserva` ahora ubica `document.getElementById('formulario-contacto')`.

## Trampas Conocidas y Reglas Borde
- *Pulse Shadow Tailwind:* Es obligatorio declararlo como `@utility` en Tailwind v4 en el root o no lo compilará al inyectar clase.
- *Overflow y Márgenes:* Mover el texto a `mt-[12vh]` en móviles choca visualmente con el `justify-center` de desktops, de tal forma que debemos usar `md:mt-0` explícito en Tailwind para apagar ese comportamiento en pantallas grandes y mantener el centrado natural flex.
