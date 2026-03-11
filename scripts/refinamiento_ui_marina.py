import os

def update_css():
    css_path = 'src/index.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    css_additions = """
@utility scrollbar-hide {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  &::-webkit-scrollbar {
    display: none;
  }
}

html {
  scroll-behavior: smooth;
}
"""
    if "scrollbar-hide" not in content:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write(css_additions)
        print("- src/index.css actualizado con 'scrollbar-hide' y 'scroll-behavior: smooth'")
    else:
        print("- src/index.css ya contenía las utilidades.")

def update_app():
    app_tsx_content = """import React, { useEffect, useRef, useState, ReactNode } from 'react';
import { CheckCircle2, Star, ShieldCheck, Heart, Sparkles, MessageCircle, Play, CalendarClock, ChevronRight, Menu, X } from 'lucide-react';

// Wrapper component for fade-in-up intersection observer animation
const FadeInUp = ({ children, delay = 0, className = '' }: { children: ReactNode, delay?: number, className?: string }) => {
  const [isVisible, setIsVisible] = useState(false);
  const domRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    
    const currentRef = domRef.current;
    if (currentRef) observer.observe(currentRef);
    return () => {
      if (currentRef) observer.unobserve(currentRef);
    };
  }, []);

  return (
    <div
      ref={domRef}
      className={`transition-all duration-1000 ease-out ${
        isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-12'
      } ${className}`}
      style={{ transitionDelay: `${delay}ms` }}
    >
      {children}
    </div>
  );
};

export default function App() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToReserva = (e: React.MouseEvent<HTMLAnchorElement | HTMLButtonElement>) => {
    e.preventDefault();
    const element = document.getElementById('reserva');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-[#F4F0EA] font-sans text-gray-800 selection:bg-[#7A1B1B] selection:text-white relative">
      
      {/* Sticky Header Glassmorphism */}
      <header className={`fixed top-0 left-0 w-full z-50 transition-all duration-300 ${
        isScrolled ? 'bg-[#F4F0EA]/95 backdrop-blur-md shadow-sm py-3 md:py-4' : 'bg-transparent py-4 md:py-6'
      }`}>
        <div className="max-w-7xl mx-auto px-4 md:px-6 flex justify-between items-center">
          <div className="flex items-center gap-1.5 md:gap-2">
            <span className="font-serif text-xl md:text-2xl font-bold text-[#7A1B1B]">Marina</span>
            <span className="font-serif text-lg md:text-xl tracking-wider text-gray-600 font-light">Essence</span>
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
      </header>

      {/* Hero Section */}
      <section className="relative px-6 pt-36 pb-20 md:pt-48 md:pb-32 max-w-7xl mx-auto flex flex-col items-center text-center overflow-hidden">
        <FadeInUp delay={100}>
          <span className="text-[#7A1B1B] font-semibold tracking-wider uppercase text-xs md:text-sm mb-6 inline-block bg-[#7A1B1B]/10 px-4 py-1.5 rounded-full">
            Especialistas en Brows, Lips, Eyes & Lashes
          </span>
        </FadeInUp>
        <FadeInUp delay={200}>
          <h1 className="font-serif text-5xl md:text-7xl lg:text-[5rem] text-gray-900 mb-6 md:mb-8 leading-tight max-w-5xl tracking-tight">
            Despierta cada mañana con tu <span className="text-[#7A1B1B] italic">mejor versión.</span>
          </h1>
        </FadeInUp>
        <FadeInUp delay={300}>
          <p className="text-base md:text-xl text-gray-600 mb-10 max-w-2xl leading-relaxed mx-auto font-light px-4">
            Realzamos tu belleza natural con técnicas avanzadas de micropigmentación. Un enfoque personalizado diseñado exclusivamente para resaltar lo que te hace única.
          </p>
        </FadeInUp>
        <FadeInUp delay={400}>
          <button onClick={scrollToReserva} className="bg-[#7A1B1B] hover:bg-[#5A1414] text-white px-6 py-4 md:px-8 md:py-4.5 rounded-full font-medium text-base md:text-lg transition-all duration-300 shadow-xl hover:shadow-[0_20px_40px_-5px_#7A1B1B40] hover:-translate-y-1 flex items-center gap-2 group mx-auto">
            <CalendarClock className="w-5 h-5 flex-shrink-0 group-hover:rotate-12 transition-transform duration-300" />
            Agenda tu Consulta de Valoración
          </button>
        </FadeInUp>
      </section>

      {/* Rediseño de la Barra de Autoridad - Inspirada en la imagen de referencia (Grid, Outline icons, White BG) */}
      <FadeInUp>
        <section className="bg-white py-16 md:py-20 px-6 border-y border-gray-100 shadow-sm relative z-10">
          <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-y-10 gap-x-6 text-center">
            
            <div className="flex flex-col items-center group">
              <div className="w-16 h-16 rounded-full bg-[#fcfaf8] flex items-center justify-center mb-4 transition-transform duration-300 group-hover:-translate-y-1">
                 <Heart className="w-8 h-8 text-[#7A1B1B] stroke-[1.5]" />
              </div>
              <h3 className="font-serif text-lg md:text-xl text-gray-900 mb-2 font-medium">+1000 Clientes</h3>
              <p className="text-xs md:text-sm text-gray-500 font-light leading-relaxed max-w-[150px] md:max-w-xs px-2">Confían su rostro a nuestros protocolos.</p>
            </div>
            
            <div className="flex flex-col items-center group">
              <div className="w-16 h-16 rounded-full bg-[#fcfaf8] flex items-center justify-center mb-4 transition-transform duration-300 group-hover:-translate-y-1">
                 <Sparkles className="w-8 h-8 text-[#7A1B1B] stroke-[1.5]" />
              </div>
              <h3 className="font-serif text-lg md:text-xl text-gray-900 mb-2 font-medium">100% Natural</h3>
              <p className="text-xs md:text-sm text-gray-500 font-light leading-relaxed max-w-[150px] md:max-w-xs px-2">Técnicas sutiles sin efecto de maquillaje pesado.</p>
            </div>
            
            <div className="flex flex-col items-center group">
              <div className="w-16 h-16 rounded-full bg-[#fcfaf8] flex items-center justify-center mb-4 transition-transform duration-300 group-hover:-translate-y-1">
                 <ShieldCheck className="w-8 h-8 text-[#7A1B1B] stroke-[1.5]" />
              </div>
              <h3 className="font-serif text-lg md:text-xl text-gray-900 mb-2 font-medium">Seguridad</h3>
              <p className="text-xs md:text-sm text-gray-500 font-light leading-relaxed max-w-[150px] md:max-w-xs px-2">Asepsia de nivel clínico en todos los procesos.</p>
            </div>
            
            <div className="flex flex-col items-center group">
              <div className="w-16 h-16 rounded-full bg-[#fcfaf8] flex items-center justify-center mb-4 transition-transform duration-300 group-hover:-translate-y-1">
                 <Star className="w-8 h-8 text-[#7A1B1B] stroke-[1.5]" />
              </div>
              <h3 className="font-serif text-lg md:text-xl text-gray-900 mb-2 font-medium">Premium</h3>
              <p className="text-xs md:text-sm text-gray-500 font-light leading-relaxed max-w-[150px] md:max-w-xs px-2">Pigmentos puros orgánicos de importación.</p>
            </div>
            
            <div className="col-span-2 lg:col-span-1 flex flex-col items-center group lg:flex">
              <div className="w-16 h-16 rounded-full bg-[#fcfaf8] flex items-center justify-center mb-4 transition-transform duration-300 group-hover:-translate-y-1">
                 <CheckCircle2 className="w-8 h-8 text-[#7A1B1B] stroke-[1.5]" />
              </div>
              <h3 className="font-serif text-lg md:text-xl text-gray-900 mb-2 font-medium">Certeza Total</h3>
              <p className="text-xs md:text-sm text-gray-500 font-light leading-relaxed max-w-[200px] md:max-w-xs px-2">Sin sorpresas. Diseño previo computarizado.</p>
            </div>
            
          </div>
        </section>
      </FadeInUp>

      {/* Timeline ("El Método Marina Essence") */}
      <section id="metodo" className="py-24 md:py-32 px-6 max-w-6xl mx-auto relative z-0">
        <FadeInUp>
          <div className="text-center mb-16">
            <h2 className="font-serif text-4xl md:text-5xl text-gray-900 mb-6">
              El Método <span className="text-[#7A1B1B] italic">Marina Essence</span>
            </h2>
            <p className="text-base md:text-lg text-gray-600 leading-relaxed max-w-2xl mx-auto px-4">
              Sabemos que cada rostro es un lienzo único. Nuestro método de tres fases está diseñado para garantizar la perfección, la sutilidad y tu satisfacción absoluta.
            </p>
          </div>
        </FadeInUp>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-12 relative">
          <div className="hidden md:block absolute top-[45px] left-[15%] right-[15%] h-[1px] bg-gradient-to-r from-transparent via-[#7A1B1B]/30 to-transparent"></div>
          
          <FadeInUp delay={100} className="relative z-10">
            <div className="flex flex-col items-center text-center group cursor-default">
              <div className="w-20 h-20 md:w-24 md:h-24 rounded-full bg-[#fcfaf8] border border-[#7A1B1B]/20 shadow-sm flex items-center justify-center mb-6 text-[#7A1B1B] text-2xl md:text-3xl font-serif transition-transform duration-500 group-hover:scale-110 group-hover:border-[#7A1B1B]">1</div>
              <h3 className="text-lg md:text-xl font-semibold mb-3">Diagnóstico Estético</h3>
              <p className="text-gray-600 font-light text-sm leading-relaxed px-4">
                Evaluamos detalladamente tus facciones anatómicas, tipo de piel, fototipo y expectativas para diseñar una hoja de ruta 100% personalizada a tu morfología.
              </p>
            </div>
          </FadeInUp>

          <FadeInUp delay={200} className="relative z-10">
            <div className="flex flex-col items-center text-center group cursor-default">
              <div className="w-20 h-20 md:w-24 md:h-24 rounded-full bg-[#7A1B1B] shadow-xl flex items-center justify-center mb-6 text-white text-2xl md:text-3xl font-serif transition-transform duration-500 group-hover:scale-110">2</div>
              <h3 className="text-lg md:text-xl font-semibold mb-3">Diseño Arquitectónico</h3>
              <p className="text-gray-600 font-light text-sm leading-relaxed px-4">
                Trazamos el tratamiento utilizando herramientas de mapeo de alta precisión. No avanzamos un milímetro sin que tú hayas aprobado el diseño previo frente al espejo.
              </p>
            </div>
          </FadeInUp>

          <FadeInUp delay={300} className="relative z-10">
            <div className="flex flex-col items-center text-center group cursor-default">
              <div className="w-20 h-20 md:w-24 md:h-24 rounded-full bg-[#fcfaf8] border border-[#7A1B1B]/20 shadow-sm flex items-center justify-center mb-6 text-[#7A1B1B] text-2xl md:text-3xl font-serif transition-transform duration-500 group-hover:scale-110 group-hover:border-[#7A1B1B]">3</div>
              <h3 className="text-lg md:text-xl font-semibold mb-3">Arte & Ejecución</h3>
              <p className="text-gray-600 font-light text-sm leading-relaxed px-4">
                Aplicamos pigmentos orgánicos de grado médico con anestesia tópica de alto confort para un proceso cien por ciento indoloro y resultados curados excepcionales.
              </p>
            </div>
          </FadeInUp>
        </div>
      </section>

      {/* Grid de Servicios */}
      <section id="servicios" className="py-24 md:py-32 px-6 bg-white border-y border-gray-100 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-[300px] md:w-[500px] h-[300px] md:h-[500px] bg-[#F4F0EA]/70 rounded-full blur-[80px] -translate-y-1/2 translate-x-1/2"></div>
        <div className="max-w-7xl mx-auto relative z-10">
          <FadeInUp>
            <div className="text-center mb-16">
              <span className="text-[#7A1B1B] font-semibold tracking-wider uppercase text-xs md:text-sm mb-4 block">Portafolio Especializado</span>
              <h2 className="font-serif text-4xl md:text-5xl text-gray-900 px-4">Nuestros Servicios Premium</h2>
            </div>
          </FadeInUp>

          {/* Tarjetas Flexibles */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <FadeInUp delay={100} className="h-full">
              <div className="group h-full bg-[#fcfaf8] p-8 rounded-[2rem] hover:bg-white hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] transition-all duration-300 border border-gray-100 flex flex-col">
                <div className="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 text-[#7A1B1B] shadow-sm transform group-hover:-rotate-6 transition-transform border border-gray-50">
                  <Sparkles className="w-7 h-7" />
                </div>
                <h3 className="font-serif text-2xl text-gray-900 mb-4 border-b border-gray-200 pb-4">Perfección en Cejas</h3>
                <ul className="space-y-4 text-gray-600 flex-grow mb-6">
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Nanoblading:</strong> Trazo ultrafino hiperrealista.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Powder Brows:</strong> Efecto maquillaje sutil empolvado.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Duración:</strong> Resultados impecables de 12 a 24 meses.</span>
                  </li>
                </ul>
                <button onClick={scrollToReserva} className="text-[#7A1B1B] font-medium text-sm flex items-center gap-1 group-hover:gap-2 transition-all mt-auto w-fit">
                  Agendar Cita <ChevronRight className="w-4 h-4"/>
                </button>
              </div>
            </FadeInUp>

            <FadeInUp delay={200} className="h-full">
              <div className="group h-full bg-[#fcfaf8] p-8 rounded-[2rem] hover:bg-white hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] transition-all duration-300 border border-gray-100 flex flex-col">
                <div className="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 text-[#7A1B1B] shadow-sm transform group-hover:-rotate-6 transition-transform border border-gray-50">
                  <Heart className="w-7 h-7" />
                </div>
                <h3 className="font-serif text-2xl text-gray-900 mb-4 border-b border-gray-200 pb-4">Labios Sensuales</h3>
                <ul className="space-y-4 text-gray-600 flex-grow mb-6">
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Aquarela Lips:</strong> Coloración translúcida saludable.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Hidralips:</strong> Nutrición y volumen visual.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Corrección:</strong> Neutralización de labios oscuros garantizada.</span>
                  </li>
                </ul>
                <button onClick={scrollToReserva} className="text-[#7A1B1B] font-medium text-sm flex items-center gap-1 group-hover:gap-2 transition-all mt-auto w-fit">
                  Agendar Cita <ChevronRight className="w-4 h-4"/>
                </button>
              </div>
            </FadeInUp>

            <FadeInUp delay={300} className="h-full">
              <div className="group h-full bg-[#fcfaf8] p-8 rounded-[2rem] hover:bg-white hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] transition-all duration-300 border border-gray-100 flex flex-col">
                <div className="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 text-[#7A1B1B] shadow-sm transform group-hover:-rotate-6 transition-transform border border-gray-50">
                  <Star className="w-7 h-7" />
                </div>
                <h3 className="font-serif text-2xl text-gray-900 mb-4 border-b border-gray-200 pb-4">Mirada Elevada</h3>
                <ul className="space-y-4 text-gray-600 flex-grow mb-6">
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Lash Lifting:</strong> Arqueo espectacular natural.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Tintura Mágica:</strong> Efecto máscara semipermanente.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Salud Integral:</strong> Enriquecido con vitaminas fortificantes (Botox).</span>
                  </li>
                </ul>
                <button onClick={scrollToReserva} className="text-[#7A1B1B] font-medium text-sm flex items-center gap-1 group-hover:gap-2 transition-all mt-auto w-fit">
                  Agendar Cita <ChevronRight className="w-4 h-4"/>
                </button>
              </div>
            </FadeInUp>

            <FadeInUp delay={400} className="h-full">
              <div className="group h-full bg-[#fcfaf8] p-8 rounded-[2rem] hover:bg-white hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] transition-all duration-300 border border-gray-100 flex flex-col">
                <div className="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 text-[#7A1B1B] shadow-sm transform group-hover:-rotate-6 transition-transform border border-gray-50">
                  <ShieldCheck className="w-7 h-7" />
                </div>
                <h3 className="font-serif text-2xl text-gray-900 mb-4 border-b border-gray-200 pb-4">Skin Care Bio</h3>
                <ul className="space-y-4 text-gray-600 flex-grow mb-6">
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Hollywood Peel:</strong> Rejuvenecimiento láser sin dolor.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Dermaplaning:</strong> Exfoliación profunda y eliminación de vello facial.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 className="w-5 h-5 text-[#7A1B1B] shrink-0 mt-0.5 opacity-80" />
                    <span className="text-sm"><strong className="text-gray-800 font-medium">Resultados Inmediatos:</strong> Piel de porcelana en 45 minutos.</span>
                  </li>
                </ul>
                <button onClick={scrollToReserva} className="text-[#7A1B1B] font-medium text-sm flex items-center gap-1 group-hover:gap-2 transition-all mt-auto w-fit">
                  Agendar Cita <ChevronRight className="w-4 h-4"/>
                </button>
              </div>
            </FadeInUp>
          </div>
        </div>
      </section>

      {/* Resultados Reales (Bento Grid) */}
      <section id="resultados" className="py-24 px-6 max-w-7xl mx-auto">
        <FadeInUp>
          <div className="text-center mb-16">
            <h2 className="font-serif text-4xl md:text-5xl text-gray-900 mb-6">Resultados Reales</h2>
            <p className="text-gray-600 max-w-2xl mx-auto">El arte de la micropigmentación no miente. Transformaciones sutiles que marcan toda la diferencia en la expresión y luminosidad del rostro.</p>
          </div>
        </FadeInUp>
        
        <div className="grid grid-cols-1 md:grid-cols-4 md:grid-rows-2 gap-4 h-[800px] md:h-[600px]">
          {/* Main Large Item */}
          <FadeInUp delay={100} className="md:col-span-2 md:row-span-2 h-full">
            <div className="relative rounded-3xl overflow-hidden group bg-gray-200 h-full w-full">
               <img src="https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?q=80&w=2000&auto=format&fit=crop" alt="Labios antes y despues" className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" />
               <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
               <div className="absolute top-4 left-4 bg-white/20 backdrop-blur-md border border-white/40 text-white text-xs uppercase tracking-widest font-semibold px-4 py-1.5 rounded-full shadow-lg">Antes y Después</div>
               <div className="absolute bottom-6 left-6 opacity-0 group-hover:opacity-100 transition-opacity duration-300 translate-y-4 group-hover:translate-y-0 text-white">
                  <p className="font-serif text-2xl mb-1">Aquarela Lips</p>
                  <p className="text-sm font-light text-white/80">Cicatrizado 30 días</p>
               </div>
            </div>
          </FadeInUp>
          
          {/* Small Top Right */}
          <FadeInUp delay={200} className="col-span-1 md:col-span-1 md:row-span-1 h-3/4 md:h-full hidden md:block">
            <div className="relative rounded-3xl overflow-hidden group bg-gray-200 h-full w-full">
               <img src="https://images.unsplash.com/photo-1620052583808-fc3472bc7b05?q=80&w=800&auto=format&fit=crop" alt="Nanoblading cejas" className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" />
               <div className="absolute top-4 left-4 bg-white/20 backdrop-blur-md border border-white/40 text-white text-[10px] uppercase tracking-widest font-semibold px-3 py-1 rounded-full">Nanoblading</div>
            </div>
          </FadeInUp>

          {/* Small Top Right 2 */}
          <FadeInUp delay={300} className="col-span-1 md:col-span-1 md:row-span-1 h-3/4 md:h-full hidden md:block">
            <div className="relative rounded-3xl overflow-hidden group bg-gray-200 h-full w-full">
               <img src="https://images.unsplash.com/photo-1588514945410-b9a35e0c5e63?q=80&w=800&auto=format&fit=crop" alt="Lash lifting" className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" />
               <div className="absolute top-4 left-4 bg-white/20 backdrop-blur-md border border-white/40 text-white text-[10px] uppercase tracking-widest font-semibold px-3 py-1 rounded-full">Lash Lifting</div>
            </div>
          </FadeInUp>
          
          {/* Rectangle Bottom */}
          <FadeInUp delay={150} className="md:col-span-2 md:row-span-1 h-[250px] md:h-full">
            <div className="relative rounded-3xl overflow-hidden group bg-gradient-to-br from-[#F4F0EA] to-[#fcfaf8] h-full w-full flex items-center justify-center text-center p-8 border border-gray-200 shadow-sm cursor-pointer hover:shadow-md transition-shadow">
               <div className="absolute font-serif text-[12rem] md:text-[15rem] text-[#7A1B1B]/5 -right-10 -bottom-10 md:-bottom-20 select-none">M</div>
               <div className="relative z-10 w-full text-left flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                  <div>
                    <h3 className="font-serif text-2xl md:text-3xl text-gray-900 mb-2">Transformación Garantizada</h3>
                    <p className="text-gray-600 font-light max-w-sm text-sm">Explora nuestra galería de éxito paciente por paciente.</p>
                  </div>
                  <button onClick={scrollToReserva} className="w-14 h-14 md:w-16 md:h-16 rounded-full bg-[#7A1B1B] text-white flex items-center justify-center hover:bg-[#5A1414] transition-colors shadow-lg group-hover:scale-110 flex-shrink-0">
                    <ChevronRight className="w-6 h-6" />
                  </button>
               </div>
            </div>
          </FadeInUp>
        </div>
      </section>

      {/* Conoce Nuestro Trabajo (Estilo Reels) - Carrusel touch infinito/snap para móviles */}
      <section className="py-24 px-0 md:px-6 bg-[#fcfaf8] border-t border-gray-100">
        <FadeInUp>
          <div className="text-center mb-12 md:mb-16 px-6">
            <h2 className="font-serif text-4xl md:text-5xl text-gray-900 mb-6">El Arte en Movimiento</h2>
            <p className="text-gray-600 max-w-2xl mx-auto px-4 text-sm md:text-base">Vívelo desde adentro. Cientos de procesos documentados paso a paso para que tengas la tranquilidad total al agendar.</p>
          </div>
        </FadeInUp>

        {/* Scroll Containera: smooth touch swipe en Mobile, Grid en Desktop */}
        <div className="max-w-6xl mx-auto flex md:grid md:grid-cols-3 gap-6 overflow-x-auto snap-x snap-mandatory scrollbar-hide px-6 md:px-0 pb-8 md:pb-0 font-sans">
          {[1, 2, 3].map((item, idx) => (
            <FadeInUp delay={idx * 200} key={item} className="snap-center shrink-0 min-w-[78vw] md:min-w-0 md:w-full">
              <div className="w-full aspect-[9/16] bg-gray-900 rounded-[2rem] relative overflow-hidden group shadow-[0_20px_40px_-15px_rgba(0,0,0,0.2)] cursor-pointer">
                <img src={
                  item === 1 ? "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=800&auto=format&fit=crop" 
                  : item === 2 ? "https://images.unsplash.com/photo-1549416554-db273cb6fb78?q=80&w=800&auto=format&fit=crop"
                  : "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=800&auto=format&fit=crop"
                } alt="Reel thumbnail" className="w-full h-full object-cover opacity-80 group-hover:scale-110 transition-transform duration-1000" loading="lazy" />
                
                {/* Overlay Vignette */}
                <div className="absolute inset-0 bg-gradient-to-b from-black/0 via-black/10 to-black/80"></div>
                
                {/* Play Button Center (Glassmorphism) */}
                <div className="absolute inset-0 m-auto w-16 h-16 md:w-20 md:h-20 bg-white/20 backdrop-blur-md border border-white/30 rounded-full flex items-center justify-center text-white opacity-80 group-hover:opacity-100 group-hover:scale-110 transition-all duration-300 shadow-[0_0_30px_rgba(0,0,0,0.3)]">
                  <Play className="w-6 h-6 md:w-8 md:h-8 ml-1" fill="currentColor" />
                </div>
                
                {/* Bottom Texts */}
                <div className="absolute bottom-6 left-6 right-6 text-white translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
                  <span className="bg-[#7A1B1B]/90 text-[10px] uppercase font-bold tracking-widest px-2.5 py-1 rounded mb-3 inline-block">Behind the Scenes</span>
                  <p className="font-serif text-base md:text-lg leading-snug drop-shadow-md">
                    {item === 1 ? "Proceso Diseño de Cejas con hilo y Mapping Facial 📐✨" 
                     : item === 2 ? "Cicatrización Perfecta de Hidralips en Tonos Peach 🍑" 
                     : "Hollywood Peel: El secreto para piel de filtro 🎥⚡"}
                  </p>
                </div>
              </div>
            </FadeInUp>
          ))}
        </div>
      </section>

      {/* Formulario de Captación Premium */}
      <section id="reserva" className="py-24 md:py-32 px-4 md:px-6">
        <FadeInUp>
          <div className="max-w-5xl mx-auto bg-[#7A1B1B] rounded-[2.5rem] p-8 md:p-16 lg:p-20 text-white shadow-[0_30px_60px_-15px_rgba(122,27,27,0.4)] relative overflow-hidden">
            {/* Decorative elements */}
            <div className="absolute top-0 right-0 w-[30rem] md:w-[40rem] h-[30rem] md:h-[40rem] bg-white opacity-[0.03] rounded-full blur-[80px] -translate-y-1/2 translate-x-1/2"></div>
            <div className="absolute bottom-0 left-0 w-[30rem] md:w-[40rem] h-[30rem] md:h-[40rem] bg-black opacity-20 rounded-full blur-[80px] translate-y-1/3 -translate-x-1/3"></div>
            
            <div className="relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16 items-center">
              <div className="text-center lg:text-left">
                <span className="uppercase text-white/70 tracking-widest text-[10px] md:text-xs font-semibold mb-4 block">Primer Paso</span>
                <h2 className="font-serif text-3xl md:text-4xl lg:text-5xl md:leading-tight mb-6">Inicia tu transformación hoy mismo</h2>
                <p className="text-white/80 text-base md:text-lg font-light leading-relaxed mb-8 max-w-lg mx-auto lg:mx-0">
                  Nuestra agenda de turnos es limitada debido a la exclusividad de nuestros procedimientos. Reserva tu lugar y un especialista se comunicará contigo.
                </p>
                <div className="hidden lg:flex items-center gap-4 text-white/60">
                  <ShieldCheck className="w-10 h-10 text-white/50 shrink-0" />
                  <p className="text-sm font-light">Tus datos están protegidos y serán tratados con absoluta confidencialidad.</p>
                </div>
              </div>

              <div className="bg-white/5 backdrop-blur-md p-6 md:p-8 rounded-[2rem] border border-white/10 shadow-2xl">
                <form className="space-y-5" onSubmit={(e) => e.preventDefault()}>
                  <div>
                    <label htmlFor="name" className="block text-xs md:text-sm font-medium text-white/90 mb-2">Nombre completo</label>
                    <input 
                      type="text" 
                      id="name" 
                      className="w-full px-4 md:px-5 py-3.5 md:py-4 rounded-xl bg-white/10 border border-white/20 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/80 transition-all font-light text-sm"
                      placeholder="Ej. María Elena"
                    />
                  </div>
                  
                  <div>
                    <label htmlFor="whatsapp" className="block text-xs md:text-sm font-medium text-white/90 mb-2">WhatsApp</label>
                    <input 
                      type="tel" 
                      id="whatsapp" 
                      className="w-full px-4 md:px-5 py-3.5 md:py-4 rounded-xl bg-white/10 border border-white/20 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/80 transition-all font-light text-sm"
                      placeholder="+52 123 456 7890"
                    />
                  </div>

                  <div>
                    <label htmlFor="service" className="block text-xs md:text-sm font-medium text-white/90 mb-2">Servicio de interés principal</label>
                    <select 
                      id="service" 
                      className="w-full px-4 md:px-5 py-3.5 md:py-4 rounded-xl bg-white/10 border border-white/20 text-white focus:outline-none focus:ring-2 focus:ring-white/80 transition-all appearance-none cursor-pointer font-light text-sm"
                    >
                      <option value="" className="text-gray-900">Selecciona para orientarte mejor...</option>
                      <option value="cejas" className="text-gray-900">Perfección en Cejas</option>
                      <option value="labios" className="text-gray-900">Labios Sensuales</option>
                      <option value="pestanas" className="text-gray-900">Mirada Elevada</option>
                      <option value="skincare" className="text-gray-900">Skin Care Avanzado</option>
                    </select>
                  </div>

                  <button 
                    type="submit" 
                    className="w-full bg-white text-[#7A1B1B] hover:bg-[#F4F0EA] py-4 rounded-xl font-semibold text-base md:text-lg transition-all duration-300 mt-2 shadow-[0_10px_20px_-10px_rgba(255,255,255,0.3)] hover:shadow-[0_15px_25px_-10px_rgba(255,255,255,0.4)]"
                  >
                    Solicitar Valoración
                  </button>
                </form>
              </div>
            </div>
          </div>
        </FadeInUp>
      </section>
      
      {/* Botón flotante WhatsApp */}
      <a href="https://wa.me/521234567890" target="_blank" rel="noopener noreferrer" className="fixed bottom-6 right-6 z-50 bg-[#25D366] text-white p-4 rounded-full shadow-[0_8px_30px_rgb(37,211,102,0.4)] hover:scale-110 transition-transform duration-300 animate-[pulse_2s_infinite] group hover:animate-none">
        <MessageCircle className="w-7 h-7 md:w-8 md:h-8 fill-current" />
        <span className="absolute flex h-full w-full top-0 left-0">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#25D366] opacity-40 group-hover:hidden"></span>
        </span>
      </a>

      {/* Footer */}
      <footer className="py-12 text-center text-gray-400 text-xs md:text-sm border-t border-gray-100 bg-white">
        <div className="flex items-center justify-center gap-2 mb-6 text-[#7A1B1B]">
           <span className="font-serif text-xl md:text-2xl font-bold">Marina</span>
           <span className="font-serif text-lg md:text-xl tracking-wider font-light">Essence</span>
        </div>
        <p>© {new Date().getFullYear()} Marina Essence Beauty MedSpa. Reservados todos los derechos.</p>
      </footer>
    </div>
  );
}
"""
    with open('src/App.tsx', 'w', encoding='utf-8') as f:
        f.write(app_tsx_content)
    print("- src/App.tsx actualizado con el rediseño y mejoras responsive")

if __name__ == "__main__":
    print("Iniciando refactorización de UI/UX Fase 2...")
    update_css()
    update_app()
    print("Refactorización Fase 2 completada.")
