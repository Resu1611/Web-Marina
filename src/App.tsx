import React, { useEffect, useRef, useState, ReactNode } from 'react';
import { CheckCircle2, Star, ShieldCheck, Heart, Sparkles, MessageCircle, Play, CalendarClock, ChevronRight, Menu, X , ChevronLeft} from 'lucide-react';

// Wrapper component for fade-in-up intersection observer animation

// PARA AÑADIR VIDEOS: Sube el .mp4 a la carpeta 'public/videos' y añade el nombre del archivo a esta lista.
const VIDEO_LIST = [
  { id: 1, src: "/videos/reel-1.mp4", alt: "Proceso Diseño de Cejas con hilo y Mapping Facial" },
  { id: 2, src: "/videos/reel-2.mp4", alt: "Cicatrización Perfecta de Hidralips en Tonos Peach" },
  { id: 3, src: "/videos/reel-3.mp4", alt: "Hollywood Peel: El secreto para piel de filtro" }
];

// PARA AÑADIR RESULTADOS: Sube los .jpg a la carpeta 'public/resultados' y añade el archivo a esta lista.
const RESULTADOS_LIST = [
  { id: 1, src: "/resultados/media__1773195441227.jpg", alt: "Cejas Antes y Después 1" },
  { id: 2, src: "/resultados/media__1773195441245.jpg", alt: "Cejas Antes y Después 2" },
  { id: 3, src: "/resultados/media__1773195441265.jpg", alt: "Pestañas Antes y Después" },
  { id: 4, src: "/resultados/media__1773195441275.jpg", alt: "Cejas Antes y Después 3" },
  { id: 5, src: "/resultados/media__1773195441299.jpg", alt: "Cejas Antes y Después 4" }
];

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

const Hero = ({ onReserveClick }: { onReserveClick: (e: React.MouseEvent<HTMLAnchorElement>) => void }) => {
  return (
    <section 
      className="bg-[80%_top] md:bg-right bg-cover bg-no-repeat relative min-h-screen flex flex-col justify-end md:justify-center overflow-hidden"
      style={{ backgroundImage: "url('/images/hero-marina.webp')" }}
    >
      <div className="absolute inset-0 z-0 bg-gradient-to-t from-[#111111] via-[#111111]/90 to-[#111111]/0 md:bg-gradient-to-r md:from-[#111111] md:via-[#111111]/80 md:to-[#111111]/0 pointer-events-none"></div>

      {/* CAPA 3: Contenido Persuasivo */}
      <div className="relative z-10 w-full max-w-7xl mx-auto pb-12 md:pb-0 px-6 md:px-16 lg:px-20">
        <FadeInUp delay={100}>
          <span className="text-gray-300 font-sans tracking-[0.2em] uppercase text-sm font-semibold mb-4 block">
            Especialistas en Brows, Lips, Eyes & Lashes
          </span>
        </FadeInUp>
        
        <FadeInUp delay={300}>
          <h1 className="font-serif text-4xl md:text-5xl lg:text-6xl text-white leading-[1.1] md:leading-[1.1] tracking-tight max-w-3xl mb-6 drop-shadow-md">
            Despierta cada mañana con tu <span className="text-[#F4F0EA] italic font-light block mt-2">mejor versión.</span>
          </h1>
        </FadeInUp>
        
        <FadeInUp delay={500}>
          <p className="text-gray-200 font-sans font-light text-sm md:text-base max-w-lg leading-relaxed mt-4 mb-8">
            Realzamos tu belleza natural con técnicas avanzadas. Olvídate del maquillaje diario y luce impecable <strong className="font-medium text-[#F4F0EA]">24/7</strong>.
          </p>
        </FadeInUp>
        
        <FadeInUp delay={700}>
          <a 
            href="#formulario-contacto" 
            onClick={onReserveClick}
            className="inline-flex items-center justify-center gap-3 bg-[#7A1B1B] text-white px-8 md:px-10 py-3.5 md:py-4 mt-2 md:mt-8 rounded-full font-sans font-medium text-base md:text-lg transition-all duration-300 shadow-xl shadow-[#8B1C24]/10 animate-pulse-shadow hover:bg-[#5A1414] hover:-translate-y-1 hover:scale-[1.02] w-full sm:w-auto"
          >
            Agendar Cita
          </a>
        </FadeInUp>
      </div>
    </section>
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
    const element = document.getElementById('formulario-contacto');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-[#F4F0EA] font-sans text-gray-800 selection:bg-[#7A1B1B] selection:text-white relative">
      
      {/* Sticky Header Cápsula (PatientFlow Style) */}
      <div className="fixed top-0 left-0 w-full z-50 flex justify-center p-3 md:p-4 pointer-events-none transition-all duration-300">
        <header className={`pointer-events-auto w-full transition-all duration-500 ease-in-out ${
          isScrolled 
            ? 'max-w-5xl bg-white/95 backdrop-blur-lg shadow-[0_8px_32px_rgba(122,27,27,0.12)] border border-[#7A1B1B]/10 rounded-full py-2.5 px-4 md:px-6 mt-0' 
            : 'max-w-7xl bg-transparent py-2 md:py-4 px-2 md:px-6 mt-0 border border-transparent'
        }`}>
          <div className="max-w-7xl mx-auto px-4 md:px-6 flex justify-between items-center relative">
          <div className="flex items-center">
            <img src="/marina-logo.png" alt="Marina Essence Logo" className={`w-auto object-contain transition-all duration-300 ${isScrolled ? 'h-7 md:h-9' : 'h-8 md:h-10 brightness-0 invert'}`} />
          </div>
          
          <nav className={`hidden md:flex items-center gap-8 text-sm uppercase tracking-widest font-medium transition-colors duration-300 ${isScrolled ? 'text-gray-700' : 'text-gray-200'}`}>
              <a href="#servicios" className="hover:text-[#7A1B1B] transition-colors relative group">
                Servicios
                <span className={`absolute -bottom-1 left-0 w-0 h-[1px] transition-all duration-300 group-hover:w-full ${isScrolled ? 'bg-[#7A1B1B]' : 'bg-white'}`}></span>
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
              <button className={`p-1.5 rounded-full transition-colors ${isScrolled ? 'text-gray-800 hover:bg-gray-100' : 'text-white'}`} onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
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
      </div>

      {/* Nuevo Hero Fullscreen Modulable */}
      <Hero onReserveClick={(e) => scrollToReserva(e as any)} />

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
              <h3 className="text-lg md:text-xl font-semibold mb-3">Diseño Facial</h3>
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

      {/* Resultados Reales (Interactive Carousel) */}
      <section id="resultados" className="py-24 px-0 md:px-6 bg-white border-t border-gray-100">
        <FadeInUp>
          <div className="text-center mb-16 px-6">
            <h2 className="font-serif text-4xl md:text-5xl text-gray-900 mb-6">Resultados Reales</h2>
            <p className="text-gray-600 max-w-2xl mx-auto">El arte de la micropigmentación no miente. Transformaciones sutiles que marcan toda la diferencia en la expresión y luminosidad del rostro.</p>
          </div>
        </FadeInUp>
        
        {/* Scroll Container de Tarjetas Interactivo Infinito */}
        <ResultadosCarousel />

        {/* CTA Button */}
        <FadeInUp delay={600}>
          <div className="text-center mt-6 px-6">
            <button onClick={scrollToReserva} className="bg-[#7A1B1B] text-white px-8 md:px-10 py-4.5 rounded-full font-medium text-base md:text-lg hover:bg-[#5A1414] transition-all duration-300 shadow-xl hover:shadow-[0_20px_40px_-5px_#7A1B1B40] hover:-translate-y-1">
              Agendar Cita Ahora
            </button>
          </div>
        </FadeInUp>
      </section>

      {/* Conoce Nuestro Trabajo (Estilo Reels) - Carrusel touch infinito/snap para móviles (OCULTADO TEMPORALMENTE) */}
      <section className="hidden py-24 px-0 md:px-6 bg-[#fcfaf8] border-t border-gray-100">
        <FadeInUp>
          <div className="text-center mb-12 md:mb-16 px-6">
            <h2 className="font-serif text-4xl md:text-5xl text-gray-900 mb-6">El Arte en Movimiento</h2>
            <p className="text-gray-600 max-w-2xl mx-auto px-4 text-sm md:text-base">Vívelo desde adentro. Cientos de procesos documentados paso a paso para que tengas la tranquilidad total al agendar.</p>
          </div>
        </FadeInUp>

        {/* Scroll Containera: smooth touch swipe en Mobile, Grid en Desktop */}
        <div className="max-w-6xl mx-auto pb-8 md:pb-0">
          <FadeInUp delay={200}>
            <VideoCarousel />
          </FadeInUp>
        </div>
      </section>

      {/* Formulario de Captación Premium */}
      <section id="formulario-contacto" className="py-24 md:py-32 px-4 md:px-6">
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
        <div className="flex items-center justify-center mb-6">
           <img src="/marina-logo.png" alt="Marina Essence Logo" className="h-10 md:h-12 w-auto object-contain opacity-90" />
        </div>
        <p>© {new Date().getFullYear()} Marina Essence Beauty MedSpa. Reservados todos los derechos.</p>
      </footer>
    </div>
  );
}
