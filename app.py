import streamlit as st

# Configurar la página
st.set_page_config(page_title="Perfil del Inversor", layout="centered")

# Inicializar el estado de sesión
if "step" not in st.session_state:
    st.session_state.step = 1
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

# Función para avanzar al siguiente paso
def siguiente():
    st.session_state.step += 1

# Título principal
st.title("Evaluación del Perfil del Inversor")
st.markdown("Responde paso a paso para conocer tu perfil de inversión.")

# Paso 1: Conocimiento y experiencia
if st.session_state.step == 1:
    st.subheader("1. Conocimiento y Experiencia del Inversor")
    st.session_state.respuestas["productos"] = st.text_input("¿Con qué productos financieros estás familiarizado?")
    st.session_state.respuestas["experiencia"] = st.radio("¿Cuánto tiempo llevas invirtiendo?", ["Nunca", "Menos de 1 año", "1 a 5 años", "Más de 5 años"])
    st.session_state.respuestas["riesgos"] = st.radio("¿Comprendes los riesgos de invertir en acciones?", ["Sí", "No", "No estoy seguro"])
    st.button("Siguiente", on_click=siguiente)

# Paso 2: Situación financiera
elif st.session_state.step == 2:
    st.subheader("2. Situación Financiera del Inversor")
    st.session_state.respuestas["ingresos"] = st.radio("¿Cuál es tu nivel de ingresos anuales?", ["<20.000€", "20.000€ - 50.000€", "50.000€ - 100.000€", ">100.000€"])
    st.session_state.respuestas["activos"] = st.text_input("¿Cuáles son tus activos totales (efectivo, inmuebles, inversiones)?")
    st.session_state.respuestas["perdidas"] = st.radio("¿Qué porcentaje de tu inversión inicial podrías perder sin afectar tu situación financiera?", ["<5%", "5-10%", "10-20%", ">20%"])
    st.session_state.respuestas["liquidez"] = st.radio("¿Tienes necesidades de liquidez a corto/medio plazo?", ["Sí", "No"])
    st.session_state.respuestas["edad"] = st.number_input("¿Cuál es tu edad?", min_value=18, max_value=100)
    st.session_state.respuestas["dependientes"] = st.number_input("¿Cuántas personas dependen económicamente de ti?", min_value=0, max_value=10)
    st.session_state.respuestas["laboral"] = st.radio("¿Cuál es tu situación laboral?", ["Empleado", "Autónomo", "Desempleado", "Jubilado", "Estudiante", "Otro"])
    st.button("Siguiente", on_click=siguiente)

# Paso 3: Objetivos de inversión
elif st.session_state.step == 3:
    st.subheader("3. Objetivos de Inversión")
    st.session_state.respuestas["objetivo"] = st.radio("¿Cuál es tu principal objetivo de inversión?", ["Crecimiento de capital", "Obtener ingresos", "Preservar capital", "Especulación"])
    st.session_state.respuestas["horizonte"] = st.radio("¿Cuál es tu horizonte temporal de inversión?", ["Menos de 1 año", "1 a 3 años", "3 a 5 años", "Más de 5 años"])
    st.session_state.respuestas["rentabilidad"] = st.text_input("¿Qué rentabilidad esperas obtener?")
    st.session_state.respuestas["riesgo"] = st.radio("¿Qué nivel de riesgo estás dispuesto a asumir?", ["Bajo", "Moderado", "Alto", "Muy alto"])
    st.button("Siguiente", on_click=siguiente)

# Paso 4: Tolerancia al riesgo psicológica
elif st.session_state.step == 4:
    st.subheader("4. Tolerancia al Riesgo (Psicológica)")
    st.session_state.respuestas["reaccion"] = st.radio("¿Qué harías si tu inversión pierde un 20% en poco tiempo?", ["Vender todo", "Esperar", "Comprar más", "Consultar con asesor"])
    st.session_state.respuestas["decision"] = st.text_input("Describe una decisión financiera difícil que hayas tomado:")
    st.session_state.respuestas["autogestion"] = st.radio("¿Qué tan cómodo te sientes gestionando tus inversiones?", ["Muy incómodo", "Incómodo", "Neutral", "Cómodo", "Muy cómodo"])
    st.button("Siguiente", on_click=siguiente)

# Paso 5: Ética y sostenibilidad
elif st.session_state.step == 5:
    st.subheader("5. Ética y Sostenibilidad")
    st.session_state.respuestas["impacto"] = st.radio("¿Te interesan inversiones con impacto social o ambiental positivo?", ["Sí", "No", "Indiferente"])
    st.session_state.respuestas["exclusiones"] = st.multiselect("¿Qué industrias prefieres evitar?", ["Armamento", "Tabaco", "Petróleo", "Juegos de azar", "Ninguna"])
    st.session_state.respuestas["sostenibilidad"] = st.radio("¿Qué tan importante es que las empresas cumplan criterios ESG?", ["Nada", "Poco", "Neutral", "Importante", "Muy importante"])
    st.button("Ver resultado", on_click=siguiente)

# Resultado final
elif st.session_state.step == 6:
    st.success("Formulario completado con éxito ✅")
    st.subheader("Resumen de tus respuestas")
    for clave, valor in st.session_state.respuestas.items():
        st.write(f"**{clave.capitalize()}:** {valor}")
    
    # Botón para reiniciar
    if st.button("Volver a empezar"):
        st.session_state.step = 1
        st.session_state.respuestas = {}
