# app.py
import streamlit as st
from transformers import pipeline

# Inisialisasi model NLP
@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline('sentiment-analysis', model='j-hartmann/emotion-english-distilroberta-base')

model = load_model()

# Judul aplikasi
st.title("Sistem Pendeteksi Emosi dalam Teks")

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks yang ingin Anda analisis:", "")

# Tombol untuk menganalisis
if st.button("Analisis Emosi"):
    if user_input:
        # Melakukan prediksi emosi
        results = model(user_input)
        for result in results:
            st.write(f"Emosi: {result['label']} - Skor: {result['score']:.2f}")
    else:
        st.write("Harap masukkan teks terlebih dahulu.")
