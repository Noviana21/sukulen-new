import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# 1. Judul dan Deskripsi Web
st.title("🌿 Klasifikasi Morfologi Daun Sukulen")
st.write("Unggah gambar daun sukulen untuk memprediksi apakah daun tersebut masuk ke dalam kelas **Daun Bulat** atau **Daun Runcing** menggunakan arsitektur VGG16.")

# 2. Memuat Model (Pastikan file .keras ada di folder yang sama dengan app.py)
@st.cache_resource
def load_vgg_model():
    return load_model('model_vgg16_terbaik.keras') # GANTI DENGAN NAMA FILE MODEL ANDA!

model = load_vgg_model()

# 3. Fitur Upload Gambar
uploaded_file = st.file_uploader("Unggah File Gambar (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan gambar yang diunggah user ke layar
    img = Image.open(uploaded_file)
    st.image(img, caption='Gambar yang diunggah', use_column_width=True)
    
    st.write("Memproses gambar...")
    
    # =========================================================
    # NORMALISASI
    # =========================================================
    # a. Resize ke 224x224
    img_resized = img.resize((224, 224)) 
    # b. Ubah ke array matematika
    img_array = image.img_to_array(img_resized) 
    # c. Normalisasi piksel (Rescaling 1./255)
    img_array = img_array / 255.0 
    # d. Tambahkan dimensi batch agar sesuai dengan input model (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0) 

    # 4. Tombol Prediksi
    if st.button("Prediksi Bentuk Daun"):
        pred = model.predict(img_array)
        prob = pred[0][0] # Mengambil nilai probabilitas (skalar tunggal dari Sigmoid)
        
        # Penentuan Kelas dan Hitung Akurasi
        if prob > 0.5:
            kelas = "Daun Runcing"
            akurasi = prob * 100
        else:
            kelas = "Daun Bulat"
            akurasi = (1 - prob) * 100
            
        # =========================================================
        # LOGIKA DETEKSI "BUKAN SUKULEN"
        # =========================================================
        # Jika model kurang yakin (di bawah 50%), berikan peringatan
        if akurasi < 50.0:
            st.warning(f"⚠️ **Peringatan!** Model kebingungan menebak gambar ini (Keyakinan hanya {akurasi:.2f}%).")
            st.error("Kemungkinan besar gambar yang diunggah **BUKAN daun sukulen**, atau kualitas gambar terlalu buruk/blur.")
        else:
            # Jika yakin (di atas 65%), tampilkan hasil normal
            st.success(f"**Hasil Prediksi:** {kelas}")
            st.info(f"**Tingkat Keyakinan Model:** {akurasi:.2f}%")