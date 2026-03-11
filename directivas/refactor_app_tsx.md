# Directiva: Refactorización UI/UX para Landing Page de Marina Essence Beauty

## Objetivo
Elevar la experiencia de usuario (UX) e interfaz de usuario (UI) de la página principal (App.tsx), dándole un aspecto "Premium" de MedSpa utilizando principios de diseño de UI/UX Pro Max, incluyendo dinamismo, micro-interacciones, copywriting mejorado, un layout bento para "Antes y Después" y un carrusel vertical tipo "Reels".

## Entradas
- Archivo fuente: `src/App.tsx` y `src/index.css`.

## Salidas
- `src/App.tsx` actualizado con las nuevas secciones y estilos premium de Tailwind CSS.
- `src/index.css` actualizado con animaciones personalizadas si es necesario.

## Lógica y Pasos
1. **Header Sticky & Glassmorphism:** Agregar un `<header>` en la parte superior, fijo (`sticky top-0 z-50`) con un fondo `bg-white/70 backdrop-blur-md` (glassmorphism), y enlaces de anclaje básicos.
2. **Dinamismo (Fade-in-up):** Se pueden usar clases personalizadas de Tailwind (añadidas en `index.css`) `animate-fade-in-up` y opcionalmente un IntersectionObserver, o simplemente un estado inicial de animación en carga para la landing.
3. **Botón Flotante WhatsApp:** Añadir fijo en `bottom-6 right-6` con clase `animate-pulse` y un diseño llamativo.
4. **Copwriting & Beneficios:** Expandir las tarjetas de servicios actuales (`Perfección en Cejas`, `Labios Irresistibles`, `Mirada Cautivadora`, `Skin Care Avanzado`) para incluir beneficios como lista con viñetas elegantes.
5. **Timeline ("El Método Marina Essence"):** Reemplazar la sección "Tu rostro es único" o añadir un timeline de 3 pasos (Evaluación, Diseño Personalizado, Tratamiento) utilizando borders y layouts de flexbox/grid.
6. **Integración Media:**
   - *Resultados Reales:* CSS Grid asimétrico (bento grid) simulando imágenes 'Antes' y 'Después'. Usar `aspect-video` o `aspect-square`, placeholder gris con ícono de imagen, etiquetas "Antes/Después" superpuestas en las esquinas.
   - *Conoce nuestro trabajo (Reels):* Grid/Flex de 3 columnas de contenido vertical (`aspect-[9/16]`) simulando un reel de Instagram. Icono central de 'Play' que aparece o se refuerza on hover (`group-hover`).
7. **Refinamiento Estético:** Usar `py-24` para separar secciones. Colores base: `#F4F0EA` (fondo), `#7A1B1B` (burgundy text/accents). Los inputs del formulario mantendrán su funcionalidad, pero on focus tendrán `focus:ring-[#7A1B1B]`.

## Trampas Conocidas, Restricciones y Casos Borde
- *Funcionalidad de formulario:* Todo el layout del formulario y los handlers/`onSubmit` deben mantenerse como están. No destruir la lógica de React.
- *Animaciones sin librerías:* Al no poder instalar librerías externas sin instrucciones directas (como `framer-motion`), todas las micro-interacciones deben resolverse con Tailwind CSS y CSS nativo en `index.css`.
