import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Data
texts = ["Saya sangat senang hari ini!",
         "Saya merasa sedih karena kehilangan kucing kesayangan saya.",
         "Tolong jangan mengganggu saya lagi!",
         "Aku sangat takut dengan film horor ini."]

labels = ["senang", "sedih", "marah", "takut"]

# Konversi label menjadi numerik
label_to_id = {label: idx for idx, label in enumerate(labels)}
id_to_label = {idx: label for label, idx in label_to_id.items()}
y = [label_to_id[label] for label in labels]

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(texts, y, test_size=0.2, random_state=42)

# Ekstraksi fitur dengan TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Latih model SVM
svm = SVC(kernel='linear')
svm.fit(X_train_tfidf, y_train)

# Prediksi dan evaluasi
y_pred = svm.predict(X_test_tfidf)
report = classification_report(y_test, y_pred, target_names=labels)

# Streamlit app
st.title("Sistem Pendeteksi Emosi dalam Teks")

st.write("Masukkan teks yang ingin Anda analisis emosi:")

user_input = st.text_area("Teks:")

if st.button("Deteksi Emosi"):
    if user_input:
        user_input_tfidf = vectorizer.transform([user_input])
        prediction = svm.predict(user_input_tfidf)
        predicted_emotion = id_to_label[prediction[0]]
        st.write(f"Emosi yang terdeteksi: **{predicted_emotion}**")
    else:
        st.write("Silakan masukkan teks untuk dianalisis.")

st.write("Laporan Evaluasi Model:")
st.text(report)
