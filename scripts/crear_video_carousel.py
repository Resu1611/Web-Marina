import os
import re

def create_video_carousel():
    file_path = 'src/App.tsx'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inyectar la constante VIDEO_LIST justo después de los imports
    video_list_code = """
// PARA AÑADIR VIDEOS: Sube el .mp4 a la carpeta 'public/videos' y añade el nombre del archivo a esta lista.
const VIDEO_LIST = [
  { id: 1, src: "/videos/reel-1.mp4", alt: "Proceso Diseño de Cejas con hilo y Mapping Facial" },
  { id: 2, src: "/videos/reel-2.mp4", alt: "Cicatrización Perfecta de Hidralips en Tonos Peach" },
  { id: 3, src: "/videos/reel-3.mp4", alt: "Hollywood Peel: El secreto para piel de filtro" }
];
"""
    if "const VIDEO_LIST" not in content:
        # Insert after imports but before components
        parts = content.split("const FadeInUp =")
        if len(parts) == 2:
            content = parts[0] + video_list_code + "\nconst FadeInUp =" + parts[1]
            print("- Constante VIDEO_LIST añadida exitosamente.")
        else:
            print("  (Aviso) No se encontró el punto de inserción para VIDEO_LIST.")
    else:
        print("  (Aviso) VIDEO_LIST ya existe en el archivo.")

    # 2. Inyectar el Componente Modular VideoCarousel justo antes de 'export default function App()'
    video_carousel_component = """
const VideoCarousel = () => {
  return (
    <div className="flex overflow-x-auto snap-x snap-mandatory gap-4 pb-4 scrollbar-hide px-6 md:px-0">
      {VIDEO_LIST.map((video) => (
        <div key={video.id} className="snap-center shrink-0 w-[80vw] max-w-[300px]">
          <video
            src={video.src}
            className="aspect-[9/16] object-cover w-full h-full rounded-2xl bg-gray-900 border border-gray-100 shadow-sm"
            autoPlay
            muted
            loop
            playsInline
            aria-label={video.alt}
          />
        </div>
      ))}
    </div>
  );
};
"""
    if "const VideoCarousel =" not in content:
        parts = content.split("export default function App()")
        if len(parts) == 2:
            content = parts[0] + video_carousel_component + "\nexport default function App()" + parts[1]
            print("- Componente VideoCarousel inyectado exitosamente.")
        else:
            print("  (Aviso) No se encontró el punto de inserción para el componente VideoCarousel.")
    else:
        print("  (Aviso) El componente VideoCarousel ya existe.")

    # 3. Reemplazar la grilla estática antigua con el uso de <VideoCarousel />
    # Buscamos el bloque a reemplazar utilizando expresiones regulares dada la variabilidad del código anterior.
    # El bloque antiguo iniciaba con <div className="max-w-6xl mx-auto flex md:grid md:grid-cols-3...
    
    old_section_pattern = re.compile(
        r'<div className="max-w-6xl mx-auto flex md:grid md:grid-cols-3 gap-6 overflow-x-auto snap-x snap-mandatory scrollbar-hide px-6 md:px-0 pb-8 md:pb-0 font-sans">.*?</div>\s*</section>',
        re.DOTALL
    )
    
    new_section = """<div className="max-w-6xl mx-auto pb-8 md:pb-0">
          <FadeInUp delay={200}>
            <VideoCarousel />
          </FadeInUp>
        </div>
      </section>"""
      
    if old_section_pattern.search(content):
        content = old_section_pattern.sub(new_section, content)
        print("- Sección 'El Arte en Movimiento' reemplazada por el componente VideoCarousel.")
    else:
        print("  (Aviso) No se pudo encontrar el bloque estático antiguo para reemplazar. Es posible que el código ya haya sido modificado.")


    # Guardar cambios
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("- Modificación estructural del carrusel de videos (VideoCarousel) completada.")

if __name__ == "__main__":
    print("Ejecutando script de refactorización para VideoCarousel...")
    create_video_carousel()
