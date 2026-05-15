import streamlit as st
from ai_logic import generar_reto, corregir_comando, obtener_pista
 
# Configuración inicial
st.set_page_config(page_title="Linux Quest", page_icon="🐧")
 
st.title("🐧 Linux Quest")
st.subheader("Aprende comandos Linux jugando")
 
# Inicializar estado
defaults = {
    "puntos": 0, "turno": 0, "fallos": 0,
    "reto": None, "resultado": None, "pista": None,
    "juego_terminado": False, "retos_usados": [], "nivel": "fácil"
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v
 
TURNOS_MAX = 25
PUNTOS_MAX = TURNOS_MAX * 10
 
# --- JUEGO TERMINADO ---
if st.session_state["juego_terminado"]:
    puntos = st.session_state["puntos"]
    st.balloons()
    st.write("## 🏁 ¡Juego terminado!")
    st.write(f"### 🏆 Puntuación final: {puntos} / {PUNTOS_MAX}")
    if puntos >= 200:
        st.success("🌟 ¡Increíble! Eres un maestro de Linux.")
    elif puntos >= 150:
        st.success("😎 ¡Muy bien! Tienes buen nivel.")
    elif puntos >= 100:
        st.info("👍 Nada mal, sigue practicando.")
    else:
        st.warning("💪 Aún hay margen de mejora, ¡inténtalo de nuevo!")
 
    if st.button("🔄 Jugar de nuevo"):
        for key in list(defaults.keys()):
            st.session_state.pop(key, None)
        st.rerun()
 
# --- JUEGO EN CURSO ---
else:
    # Selector de nivel solo al inicio
    if st.session_state["turno"] == 0:
        nivel = st.selectbox("Selecciona dificultad", ["fácil", "medio", "difícil"])
        st.session_state["nivel"] = nivel
    else:
        st.write(f"**Dificultad:** {st.session_state['nivel']}")
 
    # Barra de progreso
    st.progress(st.session_state["turno"] / TURNOS_MAX,
                text=f"Turno {st.session_state['turno']} de {TURNOS_MAX}")
 
    # Generar reto si no hay uno activo
    if st.session_state["reto"] is None:
        reto = generar_reto(st.session_state["nivel"], st.session_state["retos_usados"])
        st.session_state["reto"] = reto
        st.session_state["retos_usados"].append(reto)
        st.session_state["fallos"] = 0
        st.session_state["resultado"] = None
        st.session_state["pista"] = None
 
    # Mostrar reto
    st.write("## 📋 Reto")
    st.info(st.session_state["reto"])
 
    # Pista automática si falló 2 veces
    if st.session_state["fallos"] >= 2 and st.session_state["pista"] is None:
        st.session_state["pista"] = obtener_pista(st.session_state["reto"])
        st.rerun()
 
    # Botón pedir pista manual
    if st.button("💡 Pedir pista (-3 pts)"):
        if st.session_state["pista"] is None:
            st.session_state["pista"] = obtener_pista(st.session_state["reto"])
            st.session_state["puntos"] = max(0, st.session_state["puntos"] - 3)
            st.rerun()
 
    # Mostrar pista si existe
    if st.session_state["pista"]:
        st.warning(f"💡 Pista: {st.session_state['pista']}")
 
    # Respuesta del usuario
    respuesta = st.text_input("Escribe el comando Linux:", key=f"inp_{st.session_state['turno']}")
 
    if st.button("✅ Comprobar"):
        if respuesta.strip():
            correcto, explicacion = corregir_comando(st.session_state["reto"], respuesta)
            st.session_state["resultado"] = (correcto, explicacion)
 
            if correcto:
                st.session_state["puntos"] += 10
                st.session_state["turno"] += 1
                if st.session_state["turno"] >= TURNOS_MAX:
                    st.session_state["juego_terminado"] = True
                else:
                    st.session_state["reto"] = None
                st.rerun()
            else:
                st.session_state["fallos"] += 1
                st.session_state["puntos"] = max(0, st.session_state["puntos"] - 5)
                st.rerun()
 
    # Mostrar resultado del intento
    if st.session_state["resultado"]:
        correcto, explicacion = st.session_state["resultado"]
        if correcto:
            st.success(explicacion)
        else:
            st.error(explicacion)
 
    # Puntuación siempre visible
    st.write("---")
    st.write(f"### 🏆 Puntuación: {st.session_state['puntos']} / {PUNTOS_MAX}")
    st.write(f"❌ Fallos en este reto: {st.session_state['fallos']}")