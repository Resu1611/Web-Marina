import os
import re

def update_hero_fullscreen():
    file_path = 'src/App.tsx'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ajustar los colores del NavBar (Cápsula) dependiendo del Hero oscuro
    
    # a. Clase del logo
    content = content.replace(
        "className={`w-auto object-contain transition-all duration-300 ${isScrolled ? 'h-7 md:h-9' : 'h-8 md:h-10'}`}",
        "className={`w-auto object-contain transition-all duration-300 ${isScrolled ? 'h-7 md:h-9' : 'h-8 md:h-10 brightness-0 invert'}`}"
    )
    # b. Clases de Enlaces Desktop
    content = content.replace(
        """<nav className="hidden md:flex items-center gap-8 text-sm uppercase tracking-widest font-medium text-gray-700">""",
        """<nav className={`hidden md:flex items-center gap-8 text-sm uppercase tracking-widest font-medium transition-colors duration-300 ${isScrolled ? 'text-gray-700' : 'text-gray-200'}`}>"""
    )
    # c. Underline de los enlaces
    content = content.replace(
        """<span className="absolute -bottom-1 left-0 w-0 h-[1px] bg-[#7A1B1B] transition-all duration-300 group-hover:w-full"></span>""",
        """<span className={`absolute -bottom-1 left-0 w-0 h-[1px] transition-all duration-300 group-hover:w-full ${isScrolled ? 'bg-[#7A1B1B]' : 'bg-white'}`}></span>"""
    )
    # d. Color del icono hamburguesa móvil
    content = content.replace(
        """<button className={`p-1.5 rounded-full transition-colors ${isScrolled ? 'text-gray-800 hover:bg-gray-100' : 'text-gray-800'}`}\""",
        """<button className={`p-1.5 rounded-full transition-colors ${isScrolled ? 'text-gray-800 hover:bg-gray-100' : 'text-white'}`}\"""
    )


    # 2. Inyectar Componente `Hero` antes de que se inyectara ResultadosCarousel
    hero_code = """
const Hero = () => {
  return (
    <section className="relative min-h-[100dvh] w-full flex flex-col justify-end md:justify-center overflow-hidden z-0 bg-[#1A1A1A]">
      
      {/* CAPA 1: Imagen Absoluta (Fondo) */}
      <img 
        // TODO: Reemplazar esta URL por la imagen o video real del cliente
        src="https://images.unsplash.com/photo-1516975080661-422fc99101f4?q=80&w=1920&auto=format&fit=crop" 
        alt="Tratamiento estético premium" 
        className="absolute inset-0 w-full h-full object-cover object-[70%_30%] md:object-center -z-20 scale-105 animate-[pulse_20s_infinite_alternate]" 
        loading="eager"
      />

      {/* CAPA 2: Gradiente Adaptativo (Overlay) */}
      {/* Móvil: Abajo hacia Arriba. Desktop: Izquierda a Derecha. */}
      <div className="absolute inset-0 -z-10 bg-gradient-to-t from-[#0d0d0d] via-[#1A1A1A]/70 to-transparent md:bg-gradient-to-r md:from-[#0d0d0d] md:via-[#1A1A1A]/80 md:to-transparent"></div>

      {/* CAPA 3: Contenido Persuasivo */}
      <div className="relative z-10 w-full max-w-7xl mx-auto pb-12 pt-32 px-6 md:px-16 lg:px-20 -mt-20 md:mt-0">
        <FadeInUp delay={100}>
          <span className="text-white/70 font-sans tracking-[0.2em] uppercase text-xs font-semibold mb-4 block">
            Especialistas en Brows, Lips, Eyes & Lashes
          </span>
        </FadeInUp>
        
        <FadeInUp delay={300}>
          <h1 className="font-serif text-4xl sm:text-5xl md:text-6xl lg:text-[4.5rem] text-white leading-[1.1] md:leading-[1.1] tracking-tight max-w-3xl mb-6 drop-shadow-md">
            Despierta cada mañana con tu <span className="text-[#F4F0EA] italic font-light block mt-2">mejor versión.</span>
          </h1>
        </FadeInUp>
        
        <FadeInUp delay={500}>
          <p className="text-gray-200 font-sans font-light text-base md:text-lg lg:text-xl max-w-lg leading-relaxed mt-4 mb-8">
            Realzamos tu belleza natural con técnicas avanzadas. Olvídate del maquillaje diario y luce impecable <strong className="font-medium text-[#F4F0EA]">24/7</strong>.
          </p>
        </FadeInUp>
        
        <FadeInUp delay={700}>
          <a 
            href="https://wa.me/521234567890" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="inline-flex items-center justify-center gap-3 bg-[#F4F0EA] text-[#1A1A1A] px-8 md:px-10 py-3.5 md:py-4 mt-2 md:mt-8 rounded-full font-semibold text-base md:text-lg transition-all duration-300 shadow-[0_20px_40px_-5px_rgba(244,240,234,0.3)] hover:shadow-[0_25px_50px_-12px_rgba(255,255,255,0.5)] hover:bg-white hover:-translate-y-1 hover:scale-[1.02] group w-full sm:w-auto"
          >
            Agendar mi Cita por WhatsApp
            <ChevronRight className="w-5 h-5 text-[#1A1A1A] group-hover:translate-x-1 transition-transform" />
          </a>
        </FadeInUp>
      </div>
    </section>
  );
};
"""
    if "const Hero =" not in content:
        # Inyectar al final, justo antes de ResultadosCarousel (o export default function app si no lo encuentra por alguna razón)
        insert_marker = "const ResultadosCarousel =" if "const ResultadosCarousel =" in content else "export default function App()"
        parts = content.split(insert_marker)
        if len(parts) == 2:
            content = parts[0] + hero_code + "\n" + insert_marker + parts[1]
            print("- Componente Hero inyectado exitosamente en el source file.")
        else:
            print("  (Error) No se pudo inyectar el componente Hero.")
    else:
        print("  (Aviso) El componente Hero ya existe en el archivo.")

    # 3. Eliminar Hero antiguo y poner <Hero />
    # El archivo tenía <section className="relative px-6 pt-36 pb-20 md:pt-48 md:pb-32 max-w-7xl mx-auto flex flex-col items-center text-center overflow-hidden">
    # y acababa antes de la Barra de Autoridad.
    hero_antiguo_pattern = re.compile(
        r'\{\/\* Hero Section \*\/\}.*?\{\/\* Rediseño de la Barra de Autoridad',
        re.DOTALL
    )
    
    nuevo_bloque_hero = """{/* Nuevo Hero Fullscreen Modulable */}
      <Hero />

      {/* Rediseño de la Barra de Autoridad"""
      
    if hero_antiguo_pattern.search(content):
        content = hero_antiguo_pattern.sub(nuevo_bloque_hero, content)
        print("- Hero Centrado Antiguo eliminado. <Hero /> inyectado en el render de App.")
    else:
        print("  (Aviso) No se pudo reemplazar Hero antiguo.")

    # Guardar cambios
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("- Refactorización UI de Hero Completa.")

if __name__ == "__main__":
    update_hero_fullscreen()
