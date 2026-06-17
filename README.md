# 🌿 Klasifikasi Morfologi Daun Sukulen Menggunakan Machine Learning dan Deep Learning

## 📖 Deskripsi Proyek

Repositori ini berisi kode sumber, model hasil pelatihan, dataset, serta aplikasi berbasis Streamlit yang dikembangkan untuk memenuhi tugas Ujian Akhir Semester (UAS) Mata Kuliah Machine Learning.

Penelitian ini bertujuan mengembangkan sistem klasifikasi otomatis morfologi daun tanaman sukulen berdasarkan bentuk daunnya, yaitu:

* 🌱 Daun Bulat
* 🌿 Daun Runcing

Permasalahan utama dalam identifikasi tanaman sukulen adalah tingginya kemiripan visual antar-spesies sehingga proses identifikasi secara manual sering kali membutuhkan pengalaman dan pengetahuan khusus. Padahal, bentuk morfologi daun memiliki hubungan erat dengan kemampuan penyimpanan air dan kebutuhan perawatan tanaman.

Untuk mengatasi permasalahan tersebut, penelitian ini membandingkan performa beberapa pendekatan klasifikasi citra, mulai dari Machine Learning konvensional hingga Deep Learning berbasis Transfer Learning.

---

## 🎯 Tujuan Penelitian

1. Mengembangkan sistem klasifikasi otomatis morfologi daun sukulen.
2. Membandingkan performa algoritma Machine Learning dan Deep Learning.
3. Menentukan model dengan performa terbaik berdasarkan metrik evaluasi.
4. Mengimplementasikan model terbaik ke dalam aplikasi web menggunakan Streamlit.

---

## 🗄️ Dataset

Dataset yang digunakan merupakan dataset primer yang dikumpulkan secara mandiri.

### Statistik Dataset

| Keterangan        | Jumlah       |
| ----------------- | ------------ |
| Total citra asli  | 620 gambar   |
| Faktor augmentasi | 5×           |
| Total citra akhir | 3.100 gambar |
| Daun Bulat        | 1.550 gambar |
| Daun Runcing      | 1.550 gambar |

### Tahap Preprocessing

* Center Crop (70%)
* Resize menjadi 224 × 224 piksel
* Normalisasi piksel (0–1)
* Data Augmentation:

  * Random Rotation
  * Horizontal Flip
  * Vertical Flip
  * Brightness Adjustment

### Pembagian Dataset

| Dataset    | Persentase |
| ---------- | ---------- |
| Training   | 80%        |
| Validation | 10%        |
| Testing    | 10%        |

**Link Dataset:**

> https://drive.google.com/drive/folders/1yKRZlU5ROe3XHU_Tei8M0ycNfZe76okc?usp=sharing

---

## 🧠 Metode yang Digunakan

### 1. Machine Learning (Metode UTS)

#### HOG + SVM

Tahapan:

1. Ekstraksi fitur menggunakan Histogram of Oriented Gradients (HOG)
2. Klasifikasi menggunakan Support Vector Machine (SVM)

---

### 2. Deep Learning (Metode UAS)

#### CNN Klasik

Model Convolutional Neural Network yang dibangun secara manual menggunakan TensorFlow/Keras.

#### MobileNetV2

Transfer Learning menggunakan bobot pretrained ImageNet.

#### VGG16

Transfer Learning menggunakan arsitektur VGG16 pretrained ImageNet.

#### ResNet50

Transfer Learning menggunakan arsitektur ResNet50 pretrained ImageNet.

#### CNN + SVM

Pendekatan hybrid dengan memanfaatkan CNN sebagai feature extractor dan SVM sebagai classifier akhir.

---

## 🏆 Model Terbaik

Berdasarkan hasil eksperimen, model **VGG16** memperoleh performa terbaik dan ditetapkan sebagai Champion Model.

Model ini kemudian diimplementasikan pada aplikasi Streamlit untuk melakukan klasifikasi citra daun sukulen secara langsung.

---

## 📊 Hasil Evaluasi

Evaluasi dilakukan menggunakan data testing yang tidak pernah dilihat model selama proses pelatihan (unseen data).

| Model       | Akurasi | Precision | Recall | F1-Score |
| ----------- | ------- | --------- | ------ | -------- |
| 🥇 VGG16    | 93.00%  | 0.93      | 0.93   | 0.93     |
| MobileNetV2 | 91.00%  | 0.91      | 0.91   | 0.91     |
| CNN + SVM   | 87.00%  | 0.87      | 0.87   | 0.87     |
| SVM (HOG)   | 83.39%  | 0.83      | 0.83   | 0.83     |
| CNN Klasik  | 82.00%  | 0.83      | 0.82   | 0.82     |
| ResNet50    | 53.33%  | 0.52      | 0.52   | 0.49     |

---

## 📈 Kesimpulan

Hasil penelitian menunjukkan bahwa pendekatan Deep Learning secara umum mampu memberikan performa yang lebih baik dibandingkan Machine Learning konvensional.

Model VGG16 berhasil menjadi model terbaik dengan akurasi sebesar 93.00%.

Diduga performa unggul tersebut diperoleh karena penggunaan lapisan Flatten yang mampu mempertahankan informasi spasial terkait bentuk geometri daun, seperti lengkungan dan sudut daun. Sebaliknya, ResNet50 menggunakan mekanisme Global Average Pooling yang pada dataset ini cenderung menghilangkan sebagian informasi spasial penting sehingga menghasilkan performa yang lebih rendah.

---

## 🚀 Menjalankan Aplikasi Streamlit

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/NAMA_REPOSITORY.git

cd NAMA_REPOSITORY
```

### 2. Membuat Virtual Environment (Opsional)

Windows

```bash
python -m venv env

env\Scripts\activate
```

Linux / MacOS

```bash
python3 -m venv env

source env/bin/activate
```

### 3. Install Dependency

```bash
pip install -r requirements.txt
```

### 4. Menjalankan Streamlit

```bash
streamlit run app.py
```

Aplikasi akan berjalan pada:

```text
http://localhost:8501
```


## 👨‍💻 Teknologi yang Digunakan

* Python
* TensorFlow
* Keras
* Scikit-Learn
* OpenCV
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---
