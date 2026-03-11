import os

def update_app():
    file_path = 'src/App.tsx'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Reemplazar la anchura de los videos del carrusel en móvil
    old_video_class = 'className="snap-center shrink-0 min-w-[78vw] md:min-w-0 md:w-full"'
    new_video_class = 'className="snap-center shrink-0 w-[75vw] sm:w-[320px] md:w-full md:min-w-0"'
    
    if old_video_class in content:
        content = content.replace(old_video_class, new_video_class)
        print("- Carrusel de videos redimensionado para móvil.")
    else:
        print("  (Aviso) La clase del video no se encontró o ya fue actualizada.")

    # 2. Reemplazar el Header completo por el estilo "Cápsula Flotante" (PatientFlow style)
    old_header = """      {/* Sticky Header Glassmorphism */}
      <header className={`fixed top-0 left-0 w-full z-50 transition-all duration-300 ${
        isScrolled ? 'bg-[#F4F0EA]/95 backdrop-blur-md shadow-sm py-3 md:py-4' : 'bg-transparent py-4 md:py-6'
      }`}>
        <div className="max-w-7xl mx-auto px-4 md:px-6 flex justify-between items-center">
          <div className="flex items-center">
            <img src="/marina-logo.png" alt="Marina Essence Logo" className="h-8 md:h-10 w-auto object-contain" />
          </div>
          
          <nav className="hidden md:flex items-center gap-8 text-sm uppercase tracking-widest font-medium text-gray-700">
            <a href="#servicios" className="hover:text-[#7A1B1B] transition-colors relative group">
              Servicios
              <span className="absolute -bottom-1 left-0 w-0 h-[1px] bg-[#7A1B1B] transition-all duration-300 group-hover:w-full"></span>
            </a>
            <a href="#metodo" className="hover:text-[#7A1B1B] transition-colors relative group">El Método</a>
            <a href="#resultados" className="hover:text-[#7A1B1B] transition-colors relative group">Resultados</a>
            <button onClick={scrollToReserva} className="bg-[#7A1B1B] text-white px-6 py-2.5 rounded-full hover:bg-[#5A1414] transition-all shadow-md hover:shadow-lg">
              Reservar
            </button>
          </nav>
          
          <div className="flex items-center gap-3 md:hidden">
            <button onClick={scrollToReserva} className="bg-[#7A1B1B] text-white px-4 py-1.5 text-xs tracking-wide rounded-full font-medium transition-all shadow-md">
              Reservar
            </button>
            <button className="text-gray-800 p-1" onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
              {mobileMenuOpen ? <X size={24}/> : <Menu size={24}/>}
            </button>
          </div>
        </div>
        
        {/* Mobile menu simple fallback */}
        {mobileMenuOpen && (
          <div className="md:hidden absolute top-full left-0 w-full bg-[#F4F0EA] border-b border-[#7A1B1B]/10 shadow-lg py-4 px-6 flex flex-col gap-4 animate-fade-in-up">
            <a href="#servicios" onClick={()=>setMobileMenuOpen(false)} className="text-gray-800 uppercase text-sm tracking-widest font-medium">Servicios</a>
            <a href="#metodo" onClick={()=>setMobileMenuOpen(false)} className="text-gray-800 uppercase text-sm tracking-widest font-medium">El Método</a>
            <a href="#resultados" onClick={()=>setMobileMenuOpen(false)} className="text-gray-800 uppercase text-sm tracking-widest font-medium">Resultados</a>
          </div>
        )}
      </header>"""

    new_header = """      {/* Sticky Header Cápsula (PatientFlow Style) */}
      <div className="fixed top-0 left-0 w-full z-50 flex justify-center p-3 md:p-4 pointer-events-none transition-all duration-300">
        <header className={`pointer-events-auto w-full transition-all duration-500 ease-in-out ${
          isScrolled 
            ? 'max-w-5xl bg-white/95 backdrop-blur-lg shadow-[0_8px_32px_rgba(122,27,27,0.12)] border border-[#7A1B1B]/10 rounded-full py-2.5 px-4 md:px-6 mt-0' 
            : 'max-w-7xl bg-transparent py-2 md:py-4 px-2 md:px-6 mt-0 border border-transparent'
        }`}>
          <div className="flex justify-between items-center relative">
            <div className="flex items-center">
              <img src="/marina-logo.png" alt="Marina Essence Logo" className={`w-auto object-contain transition-all duration-300 ${isScrolled ? 'h-7 md:h-9' : 'h-8 md:h-10'}`} />
            </div>
            
            <nav className="hidden md:flex items-center gap-8 text-sm uppercase tracking-widest font-medium text-gray-700">
              <a href="#servicios" className="hover:text-[#7A1B1B] transition-colors relative group">
                Servicios
                <span className="absolute -bottom-1 left-0 w-0 h-[1px] bg-[#7A1B1B] transition-all duration-300 group-hover:w-full"></span>
              </a>
              <a href="#metodo" className="hover:text-[#7A1B1B] transition-colors relative group">El Método</a>
              <a href="#resultados" className="hover:text-[#7A1B1B] transition-colors relative group">Resultados</a>
              <button onClick={scrollToReserva} className="bg-[#7A1B1B] text-white px-7 py-2.5 rounded-full hover:bg-[#5A1414] transition-all shadow-md hover:shadow-lg flex items-center gap-2">
                Reservar
              </button>
            </nav>
            
            <div className="flex items-center gap-2 md:hidden">
              <button onClick={scrollToReserva} className="bg-[#7A1B1B] text-white px-4 py-2 text-xs tracking-wide rounded-full font-medium transition-all shadow-md">
                Reservar
              </button>
              <button className={`p-1.5 rounded-full transition-colors ${isScrolled ? 'text-gray-800 hover:bg-gray-100' : 'text-gray-800'}`} onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
                {mobileMenuOpen ? <X size={22}/> : <Menu size={22}/>}
              </button>
            </div>
            
            {/* Mobile menu drop-down en Cápsula */}
            {mobileMenuOpen && (
              <div className="md:hidden absolute top-[calc(100%+0.8rem)] left-0 w-full min-w-[280px] bg-white/95 backdrop-blur-xl border border-[#7A1B1B]/10 rounded-3xl shadow-[0_15px_40px_-5px_rgba(122,27,27,0.15)] py-6 px-6 flex flex-col gap-5 animate-fade-in-up origin-top">
                <a href="#servicios" onClick={()=>setMobileMenuOpen(false)} className="text-gray-800 uppercase text-sm tracking-widest font-medium flex items-center gap-2"><ChevronRight className="w-4 h-4 text-[#7A1B1B]"/> Servicios</a>
                <a href="#metodo" onClick={()=>setMobileMenuOpen(false)} className="text-gray-800 uppercase text-sm tracking-widest font-medium flex items-center gap-2"><ChevronRight className="w-4 h-4 text-[#7A1B1B]"/> El Método</a>
                <a href="#resultados" onClick={()=>setMobileMenuOpen(false)} className="text-gray-800 uppercase text-sm tracking-widest font-medium flex items-center gap-2"><ChevronRight className="w-4 h-4 text-[#7A1B1B]"/> Resultados</a>
              </div>
            )}
          </div>
        </header>
      </div>"""

    if old_header in content:
        content = content.replace(old_header, new_header)
        print("- Header cápsula inyectado exitosamente.")
    else:
        print("  (Aviso) El header antiguo no se encontró exactamente como se esperaba.")

    # Guardar cambios
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("- Modificaciones de la Fase 3 completadas.")

if __name__ == "__main__":
    print("Ejecutando script de Refinamiento Fase 3...")
    update_app()
