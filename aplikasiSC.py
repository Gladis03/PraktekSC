import streamlit as st
from transformers import pipeline

# Inisialisasi model pipeline dari transformers untuk pendeteksian emosi
@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

emotion_classifier = load_model()

# Judul aplikasi
st.title("Sistem Pendeteksi Emosi dalam Teks")

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks di sini:")

# Tombol untuk menganalisis teks
if st.button("Deteksi Emosi"):
    if user_input:
        # Prediksi emosi
        result = emotion_classifier(user_input)

        # Tampilkan hasil
        st.write("Hasil Deteksi Emosi:")
        for emotion in result:
            st.write(f"- **{emotion['label']}**: {emotion['score']:.4f}")

# Menampilkan informasi tambahan tentang aplikasi
st.write("""
### Tentang Aplikasi
Aplikasi ini menggunakan model pra-latih dari Hugging Face untuk mendeteksi emosi dalam teks.
Model yang digunakan adalah `j-hartmann/emotion-english-distilroberta-base`.
""")
