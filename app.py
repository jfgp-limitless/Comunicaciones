import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Domótica", layout="wide")

# Ruta base donde están los CSV
BASE_PATH = "d:/Felipe/Desktop/Comunicaciones/Code/"

def cargar_csv(nombre_archivo):
    ruta = os.path.join(BASE_PATH, nombre_archivo)
    if os.path.exists(ruta):
        return pd.read_csv(ruta)
    else:
        st.warning(f"Archivo no encontrado: {ruta}")
        return pd.DataFrame()

# Título general
st.title("📊 Monitor de Domótica - ESP32 + MQTT")

# Secciones por tópico
st.subheader("🔒 Seguridad")
df_seguridad = cargar_csv("seguridad.csv")
st.dataframe(df_seguridad)
st.line_chart(df_seguridad[['distancia']]) if 'distancia' in df_seguridad.columns else None

st.subheader("💡 Iluminación")
df_iluminacion = cargar_csv("iluminacion.csv")
st.dataframe(df_iluminacion)
st.line_chart(df_iluminacion[['lux']]) if 'lux' in df_iluminacion.columns else None

st.subheader("🔥 Incendio")
df_incendio = cargar_csv("incendio.csv")
st.dataframe(df_incendio)
if all(col in df_incendio.columns for col in ['pot', 'lux']):
    st.line_chart(df_incendio[['pot', 'lux']])
