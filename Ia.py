import streamlit as st
import google.generativeai as genai

# Configuración básica de la página
st.set_page_config(page_title="GastroPost IA", page_icon="🍔")

# Traemos la API key desde los secretos de Streamlit
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# Usamos el modelo flash porque es rápido y no gasta saldo
modelo = genai.GenerativeModel('gemini-2.5-flash')

# Interfaz en la pantalla
st.title("🍔 GastroPost IA")
st.write("Armá tu posteo para Instagram en segundos. Ideal para emprendimientos de comida.")

st.markdown("### ¿Qué cocinaste hoy?")
# Aca el usuario escribe el plato. Le puse un ejemplo local.
plato_usuario = st.text_input("Ejemplo: Empanadas jujeñas cortadas a cuchillo, promo por docena...")

# Si tocan el boton, arranca la IA
if st.button("Cocinar Posteo 🚀"):
    
    if plato_usuario:
        with st.spinner('Pensando la mejor publicidad...'):
            try:
                # Armamos el prompt con las instrucciones completas
                prompt = f"""
                Actúas como un experto en marketing digital gastronómico y copywriting. 
                A partir del siguiente plato: "{plato_usuario}", tenés que devolver de forma estructurada: 
                1. [POSTEO]: Un texto atractivo y persuasivo para Instagram (usá emojis). 
                2. [HASHTAGS]: Cinco hashtags clave. 
                3. [FOTO]: Una breve idea de cómo debería armar la escena para sacarle la foto al plato.
                """
                
                # Mandamos todo a Gemini
                respuesta = modelo.generate_content(prompt)
                
                # Imprimimos el resultado
                st.success("¡Acá tenés tu posteo listo!")
                st.write(respuesta.text)
                
            except Exception as e:
                st.error("Che, hubo un error de conexión con la IA. Probá de nuevo.")
    else:
        st.warning("¡Tenés que escribir un plato primero para que te arme el post!")

st.markdown("---")
st.caption("Desarrollado para el trabajo final de IA.")