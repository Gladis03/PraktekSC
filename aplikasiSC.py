import streamlit as st

# Fungsi untuk memproses input pengguna
def proses_input(input_data):
    # Misalkan ini adalah fungsi sistem cerdas sederhana
    hasil = input_data.upper()  # Contoh: mengubah teks menjadi huruf besar
    return hasil

# Judul aplikasi
st.title("Aplikasi Proyek Sistem Cerdas")

# Input teks dari pengguna
input_data = st.text_input("Masukkan teks untuk diproses:")

# Tombol untuk memproses data
if st.button("Proses"):
    # Memproses input pengguna
    hasil = proses_input(input_data)
    # Menampilkan hasil
    st.write("Hasil pemrosesan:", hasil)

# Info tambahan atau deskripsi aplikasi
st.write("""
### Tentang Aplikasi Ini
Aplikasi ini merupakan contoh sederhana dari Proyek Sistem Cerdas menggunakan Streamlit.
Anda dapat memasukkan teks, dan aplikasi akan memproses teks tersebut menjadi huruf besar.
""")
