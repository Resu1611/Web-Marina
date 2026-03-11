import os
import re

def update_carousel_infinito():
    file_path = 'src/App.tsx'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Asegurar import de ChevronLeft
    if "ChevronLeft" not in content:
        # Busca la línea de import de lucide-react y la reemplaza añadiendo ChevronLeft al final de lo extraído
        import_pattern = re.compile(r"import \{(.*?)\} from 'lucide-react';")
        match = import_pattern.search(content)
        if match:
            current_imports = match.group(1)
            new_imports = f"import {{{current_imports}, ChevronLeft}} from 'lucide-react';"
            content = content.replace(match.group(0), new_imports)
            print("- ChevronLeft añadido a los imports de lucide-react.")
        else:
            print("  (Aviso) No se encontró la línea de import de lucide-react.")

    # 2. Inyectar el componente ResultadosCarousel antes de export default function App()
    componente_code = """
const ResultadosCarousel = () => {
  const scrollRef = useRef<HTMLDivElement>(null);
  // Triplicar el array para dar el "Efecto Infinito" a lo largo de mucho scroll
  const infiniteList = [...RESULTADOS_LIST, ...RESULTADOS_LIST, ...RESULTADOS_LIST];

  const scroll = (direction: 'left' | 'right') => {
    if (scrollRef.current) {
      const scrollAmount = window.innerWidth > 768 ? 450 : 320; // Ancho tarjeta aprox + gap
      scrollRef.current.scrollBy({ left: direction === 'left' ? -scrollAmount : scrollAmount, behavior: 'smooth' });
    }
  };

  return (
    <div className="relative max-w-7xl mx-auto w-full group">
       {/* Botón Izquierdo (Desktop) */}
       <button onClick={() => scroll('left')} className="hidden md:flex absolute -left-6 top-1/2 -translate-y-1/2 z-20 w-14 h-14 bg-white rounded-full shadow-[0_10px_30px_rgba(122,27,27,0.15)] items-center justify-center text-[#7A1B1B] hover:bg-[#F4F0EA] transition-all hover:scale-110 opacity-0 group-hover:opacity-100 focus:opacity-100 border border-gray-100">
         <ChevronLeft className="w-8 h-8 -ml-1" />
       </button>
       
       {/* Contenedor Scroll */}
       <div ref={scrollRef} className="flex overflow-x-auto snap-x snap-mandatory gap-4 px-6 pb-8 scrollbar-hide py-4">
         {infiniteList.map((img, idx) => (
           <div key={`${img.id}-${idx}`} className="snap-center shrink-0 w-[85vw] sm:w-[400px] md:w-[450px]">
             <div className="w-full bg-gray-100 rounded-2xl relative overflow-hidden shadow-[0_10px_30px_-15px_rgba(0,0,0,0.15)] cursor-pointer group/card border border-gray-50">
               <img src={img.src} alt={img.alt} className="w-full h-auto object-cover sm:aspect-[4/5] opacity-90 transition-all duration-500 group-hover/card:scale-105 group-hover/card:opacity-100" loading="lazy" />
             </div>
           </div>
         ))}
       </div>

       {/* Botón Derecho (Desktop) */}
       <button onClick={() => scroll('right')} className="hidden md:flex absolute -right-6 top-1/2 -translate-y-1/2 z-20 w-14 h-14 bg-white rounded-full shadow-[0_10px_30px_rgba(122,27,27,0.15)] items-center justify-center text-[#7A1B1B] hover:bg-[#F4F0EA] transition-all hover:scale-110 opacity-0 group-hover:opacity-100 focus:opacity-100 border border-gray-100">
         <ChevronRight className="w-8 h-8 ml-1" />
       </button>
    </div>
  );
};
"""
    if "const ResultadosCarousel =" not in content:
        parts = content.split("export default function App()")
        if len(parts) == 2:
            content = parts[0] + componente_code + "\nexport default function App()" + parts[1]
            print("- Componente ResultadosCarousel inyectado exitosamente.")
        else:
            print("  (Error) No se pudo inyectar el componente.")
    else:
        print("  (Aviso) El componente ResultadosCarousel ya existe.")

    # 3. Remover el bloque grid de FadeInUp iterativo antiguo y sustituirlo por <ResultadosCarousel />
    # Manteniendo intacto todo lo que hay alrededor
    patron_antiguo = re.compile(
        r'<div className="max-w-7xl mx-auto flex overflow-x-auto snap-x snap-mandatory gap-4 px-6 pb-12 scrollbar-hide">.*?</div>\n\s*\{\/\* CTA Button \*\/\}',
        re.DOTALL
    )
    
    nuevo_bloque = """<FadeInUp delay={200}>
          <ResultadosCarousel />
        </FadeInUp>

        {/* CTA Button */}"""
        
    if patron_antiguo.search(content):
        content = patron_antiguo.sub(nuevo_bloque, content)
        print("- Bucle antiguo borrado. Instancia de <ResultadosCarousel /> inyectada en el DOM.")
    else:
        print("  (Aviso) El patrón de la iteración antigua no hizo match. Puede que ya se haya reemplazado.")

    # Guardar cambios
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("- Transformación a Carrusel Infinito Desktop terminada.")

if __name__ == "__main__":
    update_carousel_infinito()
