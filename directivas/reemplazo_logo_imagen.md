# Directiva: Reemplazo de Logotipo Tipográfico por Imagen

## Objetivo
Reemplazar el texto "Marina Essence" (letras) en el Sticky Header y en el Footer de la landing page (`App.tsx`) por el logo de imagen proporcionado (`marina-logo.png`).

## Entradas
- `src/App.tsx` (Componente de la landing).
- Imagen: `/public/marina-logo.png` (Ya añadida a la carpeta `public`).

## Salidas
- Script Python que modifique `src/App.tsx` para inyectar la etiqueta `<img>` en reemplazo de los tags de texto (`<span>`) que conformaban el logo anterior.

## Lógica y Pasos
1.   Localizar la caja del logo en el Header de `App.tsx` (dentro de `<header>`). Reemplazar:
```jsx
<div className="flex items-center gap-1.5 md:gap-2">
  <span className="font-serif text-xl md:text-2xl font-bold text-[#7A1B1B]">Marina</span>
  <span className="font-serif text-lg md:text-xl tracking-wider text-gray-600 font-light">Essence</span>
</div>
```
por:
```jsx
<div className="flex items-center">
  <img src="/marina-logo.png" alt="Marina Essence Logo" className="h-8 md:h-10 w-auto object-contain" />
</div>
```

2.   Localizar la caja del logo en el Footer de `App.tsx` (dentro de `<footer>`). Reemplazar la misma estructura de texto por:
```jsx
<div className="flex items-center justify-center mb-6">
  <img src="/marina-logo.png" alt="Marina Essence Logo" className="h-10 md:h-12 w-auto object-contain opacity-90" />
</div>
```

## Trampas Conocidas, Restricciones y Casos Borde
-   *Ruta de imagen:* En Vite / CRA, los archivos en `public/` se referencian desde la raíz `/`. Por tanto, `src="/marina-logo.png"` es la ruta correcta.
-   *Tamaño de imagen:* Usar altura controlada (`h-8` a `h-10` en móviles y escritorio, y mantener `w-auto`) para evitar deformaciones en el header sticky.
