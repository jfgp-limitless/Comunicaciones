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

st.title("📊 Monitor de Domótica - ESP32 + MQTT")

# 🔒 Seguridad
st.subheader("🔒 Seguridad")
df_seguridad = cargar_csv("seguridad.csv")
st.dataframe(df_seguridad)
if all(col in df_seguridad.columns for col in ['puerta', 'buzzer']):
    st.line_chart(df_seguridad[['puerta', 'buzzer']])

# 💡 Iluminación
st.subheader("💡 Iluminación")
df_iluminacion = cargar_csv("iluminacion.csv")
st.dataframe(df_iluminacion)
if all(col in df_iluminacion.columns for col in ['lux', 'pot']):
    st.line_chart(df_iluminacion[['lux', 'pot']])
if 'led' in df_iluminacion.columns:
    st.line_chart(df_iluminacion[['led']])

# 🌡️ Clima
st.subheader("🌡️ Clima")
df_clima = cargar_csv("clima.csv")
st.dataframe(df_clima)
if all(col in df_clima.columns for col in ['temperatura', 'humedad']):
    st.line_chart(df_clima[['temperatura', 'humedad']])

# 🔥 Incendio
st.subheader("🔥 Incendio")
df_incendio = cargar_csv("incendio.csv")
st.dataframe(df_incendio)
cols_incendio = [col for col in ['lux', 'temperatura', 'humedad', 'buzzer'] if col in df_incendio.columns]
if cols_incendio:
    st.line_chart(df_incendio[cols_incendio])

# 💬 Chat General
st.subheader("💬 Chat General")
df_chat = cargar_csv("chatgeneral.csv")
st.dataframe(df_chat)
if 'mensaje' in df_chat.columns:
    for index, row in df_chat.iterrows():
        st.write(f"🗨️ {row['mensaje']}")
