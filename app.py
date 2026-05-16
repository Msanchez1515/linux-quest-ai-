import streamlit as st
from ai_logic import generar_reto, corregir_comando, obtener_pista
 
st.set_page_config(page_title="Linux Quest", page_icon="🐧", layout="centered")
 
# ── CSS: fondo galaxia + fuente pixel + pingüinos ──────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
 
html, body, [data-testid="stAppViewContainer"] {
    background-color: #050A1A !important;
}
[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(circle, #ffffff 1px, transparent 1px),
        radial-gradient(circle, #ffffff 1px, transparent 1px),
        radial-gradient(circle, #aaaaff 1px, transparent 1px);
    background-size: 200px 200px, 350px 350px, 150px 150px;
    background-position: 0 0, 100px 100px, 50px 50px;
    animation: starscroll 60s linear infinite;
}
@keyframes starscroll {
    from { background-position: 0 0, 100px 100px, 50px 50px; }
    to   { background-position: 200px 200px, 300px 300px, 200px 200px; }
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { background: #0A1428 !important; }
 
h1, h2, h3, .stMarkdown p, label, .stSelectbox label {
    font-family: 'Press Start 2P', monospace !important;
    color: #00FF88 !important;
}
h1 { font-size: 1.2rem !important; line-height: 1.8 !important; }
h2 { font-size: 0.9rem !important; }
h3 { font-size: 0.8rem !important; }
p, label { font-size: 0.65rem !important; color: #7FFFD4 !important; }
 
.stButton > button {
    font-family: 'Press Start 2P', monospace !important;
    background: transparent !important;
    color: #00FF88 !important;
    border: 2px solid #00FF88 !important;
    border-radius: 0 !important;
    font-size: 0.6rem !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.1s !important;
}
.stButton > button:hover {
    background: #00FF88 !important;
    color: #050A1A !important;
}
.stTextInput > div > div > input {
    font-family: 'Press Start 2P', monospace !important;
    background: #0A1428 !important;
    color: #00FF88 !important;
    border: 2px solid #00FF88 !important;
    border-radius: 0 !important;
    font-size: 0.7rem !important;
}
.stSelectbox > div > div {
    font-family: 'Press Start 2P', monospace !important;
    background: #0A1428 !important;
    color: #00FF88 !important;
    border: 2px solid #00FF88 !important;
    border-radius: 0 !important;
}
.stProgress > div > div > div {
    background: #00FF88 !important;
}
.stAlert {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 0.6rem !important;
    border-radius: 0 !important;
    background: #0A1428 !important;
    border-left: 4px solid #00FF88 !important;
}
 
/* Pingüinos pixel art */
.pingüino-container {
    display: flex;
    justify-content: center;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)
 
# ── Pingüinos en SVG pixel art ─────────────────────────────────────────────
PINGUINO_FELIZ = """
<div class="pingüino-container">
<svg width="120" height="140" viewBox="0 0 120 140">
  <style>
    @keyframes bounce {
      0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)}
    }
    @keyframes twinkle { 0%,100%{opacity:1} 50%{opacity:0} }
    .pingu { animation: bounce 0.6s ease-in-out infinite; }
  </style>
  <g class="pingu">
    <!-- cuerpo -->
    <rect x="30" y="60" width="60" height="64" rx="4" fill="#111"/>
    <!-- barriga -->
    <rect x="40" y="72" width="40" height="44" rx="4" fill="#F5F5DC"/>
    <!-- cabeza -->
    <rect x="26" y="18" width="68" height="50" rx="4" fill="#111"/>
    <!-- mejillas felices -->
    <rect x="30" y="44" width="14" height="8" rx="4" fill="#FF8FAB" opacity="0.7"/>
    <rect x="76" y="44" width="14" height="8" rx="4" fill="#FF8FAB" opacity="0.7"/>
    <!-- ojos felices (arcos) -->
    <rect x="38" y="30" width="14" height="4" fill="#FFD700"/>
    <rect x="68" y="30" width="14" height="4" fill="#FFD700"/>
    <rect x="38" y="34" width="4" height="8" fill="#FFD700"/>
    <rect x="48" y="34" width="4" height="8" fill="#FFD700"/>
    <rect x="68" y="34" width="4" height="8" fill="#FFD700"/>
    <rect x="78" y="34" width="4" height="8" fill="#FFD700"/>
    <!-- sonrisa -->
    <rect x="44" y="52" width="32" height="4" fill="#FF8C00"/>
    <rect x="44" y="52" width="4" height="8" fill="#FF8C00"/>
    <rect x="72" y="52" width="4" height="8" fill="#FF8C00"/>
    <!-- auriculares -->
    <rect x="14" y="22" width="12" height="18" rx="4" fill="#FF4444"/>
    <rect x="94" y="22" width="12" height="18" rx="4" fill="#FF4444"/>
    <rect x="18" y="16" width="84" height="10" rx="4" fill="#CC2222"/>
    <!-- pies -->
    <rect x="22" y="118" width="22" height="10" rx="2" fill="#FF8C00"/>
    <rect x="76" y="118" width="22" height="10" rx="2" fill="#FF8C00"/>
    <!-- alitas arriba celebrando -->
    <rect x="4" y="58" width="26" height="8" rx="2" fill="#111"/>
    <rect x="4" y="46" width="8" height="20" rx="2" fill="#111"/>
    <rect x="90" y="58" width="26" height="8" rx="2" fill="#111"/>
    <rect x="108" y="46" width="8" height="20" rx="2" fill="#111"/>
  </g>
  <!-- estrellitas -->
  <rect x="2" y="10" width="6" height="6" fill="#FFD700" opacity="0.9"><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/></rect>
  <rect x="112" y="15" width="6" height="6" fill="#FFD700" opacity="0.9"><animate attributeName="opacity" values="0;1;0" dur="0.8s" repeatCount="indefinite"/></rect>
  <rect x="58" y="2" width="6" height="6" fill="#00FF88" opacity="0.9"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>
  <!-- texto -->
  <text x="60" y="138" text-anchor="middle" font-family="monospace" font-size="9" fill="#00FF88">¡CORRECTO! +10</text>
</svg>
</div>
"""
 
PINGUINO_TRISTE = """
<div class="pingüino-container">
<svg width="120" height="140" viewBox="0 0 120 140">
  <style>
    @keyframes shake {
      0%,100%{transform:translateX(0)} 25%{transform:translateX(-4px)} 75%{transform:translateX(4px)}
    }
    .pingu { animation: shake 0.5s ease-in-out 1; }
  </style>
  <g class="pingu">
    <!-- cuerpo -->
    <rect x="30" y="60" width="60" height="64" rx="4" fill="#111"/>
    <!-- barriga -->
    <rect x="40" y="72" width="40" height="44" rx="4" fill="#F5F5DC"/>
    <!-- cabeza -->
    <rect x="26" y="18" width="68" height="50" rx="4" fill="#111"/>
    <!-- ojos tristes -->
    <rect x="38" y="34" width="14" height="4" fill="#FFD700"/>
    <rect x="38" y="30" width="4" height="8" fill="#FFD700"/>
    <rect x="48" y="30" width="4" height="8" fill="#FFD700"/>
    <rect x="68" y="34" width="14" height="4" fill="#FFD700"/>
    <rect x="68" y="30" width="4" height="8" fill="#FFD700"/>
    <rect x="78" y="30" width="4" height="8" fill="#FFD700"/>
    <!-- boca triste -->
    <rect x="44" y="58" width="32" height="4" fill="#FF8C00"/>
    <rect x="44" y="50" width="4" height="12" fill="#FF8C00"/>
    <rect x="72" y="50" width="4" height="12" fill="#FF8C00"/>
    <!-- lágrimas -->
    <rect x="42" y="42" width="4" height="10" fill="#7FFFD4" opacity="0.8"/>
    <rect x="74" y="42" width="4" height="10" fill="#7FFFD4" opacity="0.8"/>
    <rect x="42" y="52" width="4" height="4" fill="#7FFFD4" opacity="0.5"/>
    <rect x="74" y="52" width="4" height="4" fill="#7FFFD4" opacity="0.5"/>
    <!-- auriculares -->
    <rect x="14" y="22" width="12" height="18" rx="4" fill="#FF4444"/>
    <rect x="94" y="22" width="12" height="18" rx="4" fill="#FF4444"/>
    <rect x="18" y="16" width="84" height="10" rx="4" fill="#CC2222"/>
    <!-- pies -->
    <rect x="22" y="118" width="22" height="10" rx="2" fill="#FF8C00"/>
    <rect x="76" y="118" width="22" height="10" rx="2" fill="#FF8C00"/>
    <!-- alitas caídas -->
    <rect x="4" y="72" width="26" height="8" rx="2" fill="#111"/>
    <rect x="90" y="72" width="26" height="8" rx="2" fill="#111"/>
  </g>
  <!-- texto -->
  <text x="60" y="138" text-anchor="middle" font-family="monospace" font-size="9" fill="#FF4444">INCORRECTO -5</text>
</svg>
</div>
"""
 
PINGUINO_PENSANDO = """
<div class="pingüino-container">
<svg width="130" height="140" viewBox="0 0 130 140">
  <style>
    @keyframes think {
      0%,100%{transform:rotate(-3deg)} 50%{transform:rotate(3deg)}
    }
    @keyframes bubble { 0%,100%{opacity:0.4} 50%{opacity:1} }
    .pingu { animation: think 1s ease-in-out infinite; transform-origin: 60px 90px; }
  </style>
  <g class="pingu">
    <!-- cuerpo -->
    <rect x="30" y="60" width="60" height="64" rx="4" fill="#111"/>
    <!-- barriga -->
    <rect x="40" y="72" width="40" height="44" rx="4" fill="#F5F5DC"/>
    <!-- cabeza -->
    <rect x="26" y="18" width="68" height="50" rx="4" fill="#111"/>
    <!-- ojos pensando (mirando arriba) -->
    <rect x="38" y="26" width="14" height="10" rx="2" fill="#FFD700"/>
    <rect x="42" y="24" width="6" height="6" fill="#111"/>
    <rect x="68" y="26" width="14" height="10" rx="2" fill="#FFD700"/>
    <rect x="72" y="24" width="6" height="6" fill="#111"/>
    <!-- boca neutral -->
    <rect x="48" y="54" width="24" height="4" fill="#FF8C00"/>
    <!-- mano en mentón -->
    <rect x="4" y="66" width="26" height="8" rx="2" fill="#111"/>
    <rect x="4" y="58" width="8" height="16" rx="2" fill="#111"/>
    <rect x="4" y="58" width="16" height="8" rx="2" fill="#111"/>
    <!-- ala derecha normal -->
    <rect x="90" y="72" width="26" height="8" rx="2" fill="#111"/>
    <!-- auriculares -->
    <rect x="14" y="22" width="12" height="18" rx="4" fill="#FF4444"/>
    <rect x="94" y="22" width="12" height="18" rx="4" fill="#FF4444"/>
    <rect x="18" y="16" width="84" height="10" rx="4" fill="#CC2222"/>
    <!-- pies -->
    <rect x="22" y="118" width="22" height="10" rx="2" fill="#FF8C00"/>
    <rect x="76" y="118" width="22" height="10" rx="2" fill="#FF8C00"/>
  </g>
  <!-- burbuja de pensamiento -->
  <circle cx="100" cy="50" r="4" fill="#7FFFD4" opacity="0.6"><animate attributeName="opacity" values="0.3;1;0.3" dur="1.2s" repeatCount="indefinite"/></circle>
  <circle cx="110" cy="36" r="6" fill="#7FFFD4" opacity="0.7"><animate attributeName="opacity" values="0.5;1;0.5" dur="1.2s" repeatCount="indefinite" begin="0.2s"/></circle>
  <circle cx="118" cy="20" r="10" fill="#7FFFD4" opacity="0.8"><animate attributeName="opacity" values="0.6;1;0.6" dur="1.2s" repeatCount="indefinite" begin="0.4s"/></circle>
  <text x="118" y="24" text-anchor="middle" font-family="monospace" font-size="8" fill="#050A1A">?</text>
  <!-- texto -->
  <text x="60" y="138" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFD700">PISTA... -3pts</text>
</svg>
</div>
"""
 
# ── Estado ─────────────────────────────────────────────────────────────────
defaults = {
    "puntos": 0, "turno": 0, "fallos": 0,
    "reto": None, "resultado": None, "pista": None,
    "juego_terminado": False, "retos_usados": [], "nivel": "fácil",
    "mostrar_pinguino": None
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v
 
TURNOS_MAX = 25
PUNTOS_MAX = TURNOS_MAX * 10
 
# ── Título ─────────────────────────────────────────────────────────────────
st.markdown("<h1>🐧 LINUX QUEST</h1>", unsafe_allow_html=True)
st.markdown("<p>APRENDE COMANDOS LINUX JUGANDO</p>", unsafe_allow_html=True)
 
# ── JUEGO TERMINADO ─────────────────────────────────────────────────────────
if st.session_state["juego_terminado"]:
    puntos = st.session_state["puntos"]
    st.balloons()
    st.markdown(PINGUINO_FELIZ, unsafe_allow_html=True)
    st.markdown(f"<h2>🏁 JUEGO TERMINADO</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3>🏆 PUNTUACIÓN: {puntos} / {PUNTOS_MAX}</h3>", unsafe_allow_html=True)
    if puntos >= 200:
        st.success("🌟 ¡INCREÍBLE! ERES UN MAESTRO DE LINUX.")
    elif puntos >= 150:
        st.success("😎 ¡MUY BIEN! TIENES BUEN NIVEL.")
    elif puntos >= 100:
        st.info("👍 NADA MAL, SIGUE PRACTICANDO.")
    else:
        st.warning("💪 ¡INTÉNTALO DE NUEVO!")
 
    if st.button("🔄 JUGAR DE NUEVO"):
        for key in list(defaults.keys()):
            st.session_state.pop(key, None)
        st.rerun()
 
# ── JUEGO EN CURSO ──────────────────────────────────────────────────────────
else:
    if st.session_state["turno"] == 0:
        nivel = st.selectbox("DIFICULTAD", ["fácil", "medio", "difícil"])
        st.session_state["nivel"] = nivel
    else:
        st.markdown(f"<p>DIFICULTAD: {st.session_state['nivel'].upper()}</p>", unsafe_allow_html=True)
 
    st.progress(st.session_state["turno"] / TURNOS_MAX,
                text=f"TURNO {st.session_state['turno']} DE {TURNOS_MAX}")
 
    # Generar reto si no hay uno
    if st.session_state["reto"] is None:
        reto = generar_reto(st.session_state["nivel"], st.session_state["retos_usados"])
        st.session_state["reto"] = reto
        st.session_state["retos_usados"].append(reto)
        st.session_state["fallos"] = 0
        st.session_state["resultado"] = None
        st.session_state["pista"] = None
        st.session_state["mostrar_pinguino"] = None
 
    # Pingüino según estado
    if st.session_state["mostrar_pinguino"] == "feliz":
        st.markdown(PINGUINO_FELIZ, unsafe_allow_html=True)
    elif st.session_state["mostrar_pinguino"] == "triste":
        st.markdown(PINGUINO_TRISTE, unsafe_allow_html=True)
    elif st.session_state["mostrar_pinguino"] == "pensando":
        st.markdown(PINGUINO_PENSANDO, unsafe_allow_html=True)
 
    # Reto
    st.markdown(f"<h2>📋 RETO</h2>", unsafe_allow_html=True)
    st.info(st.session_state["reto"])
 
    # Pista automática si falla 2 veces
    if st.session_state["fallos"] >= 2 and st.session_state["pista"] is None:
        st.session_state["pista"] = obtener_pista(st.session_state["reto"])
        st.session_state["mostrar_pinguino"] = "pensando"
        st.rerun()
 
    # Botón pista manual
    if st.button("💡 PEDIR PISTA (-3 PTS)"):
        if st.session_state["pista"] is None:
            st.session_state["pista"] = obtener_pista(st.session_state["reto"])
            st.session_state["puntos"] = max(0, st.session_state["puntos"] - 3)
            st.session_state["mostrar_pinguino"] = "pensando"
            st.rerun()
 
    if st.session_state["pista"]:
        st.warning(f"💡 PISTA: {st.session_state['pista']}")
 
    # Input
    respuesta = st.text_input("ESCRIBE EL COMANDO:", key=f"inp_{st.session_state['turno']}")
 
    if st.button("✅ COMPROBAR"):
        if respuesta.strip():
            correcto, explicacion = corregir_comando(st.session_state["reto"], respuesta)
            st.session_state["resultado"] = (correcto, explicacion)
 
            if correcto:
                st.session_state["puntos"] += 10
                st.session_state["mostrar_pinguino"] = "feliz"
                st.session_state["turno"] += 1
                if st.session_state["turno"] >= TURNOS_MAX:
                    st.session_state["juego_terminado"] = True
                else:
                    st.session_state["reto"] = None
                st.rerun()
            else:
                st.session_state["fallos"] += 1
                st.session_state["puntos"] = max(0, st.session_state["puntos"] - 5)
                st.session_state["mostrar_pinguino"] = "triste"
                st.rerun()
 
    # Resultado
    if st.session_state["resultado"]:
        correcto, explicacion = st.session_state["resultado"]
        if correcto:
            st.success(explicacion)
        else:
            st.error(explicacion)
 
    # Puntuación
    st.markdown("---")
    st.markdown(f"<h3>🏆 PUNTOS: {st.session_state['puntos']} / {PUNTOS_MAX}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p>❌ FALLOS EN ESTE RETO: {st.session_state['fallos']}</p>", unsafe_allow_html=True)