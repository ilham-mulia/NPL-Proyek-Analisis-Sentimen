
# 📱 Sentiment Analysis of Google Play Reviews - Genshin Impact

Proyek ini bertujuan untuk **mengambil ulasan dari aplikasi *Genshin Impact* di Google Play Store**, lalu melakukan **analisis sentimen** terhadap ulasan tersebut menggunakan metode **TextBlob + TF-IDF + Machine Learning (SVM dan Random Forest)**.

---

## 📌 Tujuan Proyek

- Mengambil data ulasan aplikasi dari Google Play Store secara otomatis.
- Melabeli sentimen ulasan sebagai **positif**, **negatif**, atau **netral**.
- Mengekstrak fitur menggunakan **TF-IDF**.
- Membangun dan mengevaluasi model machine learning untuk klasifikasi sentimen.
- Melakukan inference untuk melihat hasil prediksi model.
- Menyajikan visualisasi distribusi sentimen.

---

## 🗂️ Struktur Proyek

```bash
.
├── data_playstore.csv           # Hasil scraping ulasan Google Play
├── sentiment_analysis.ipynb     # Notebook utama analisis sentimen
├── requirements.txt             # Daftar dependensi Python
├── README.md                    # Penjelasan proyek ini
```

---

## ⚙️ Tools & Library

- Python
- [google-play-scraper](https://pypi.org/project/google-play-scraper/)
- pandas, numpy, seaborn, matplotlib
- TextBlob, nltk
- scikit-learn (TF-IDF, SVM, Random Forest, dll)

---

## 🚀 Langkah-langkah Analisis

### 1. Scraping Data Google Play
Menggunakan `google-play-scraper` untuk mengambil 3.000 ulasan terbaru dari aplikasi `com.miHoYo.GenshinImpact`.

### 2. Pembersihan & Pelabelan Sentimen
Label ditentukan berdasarkan skor polaritas dari `TextBlob`:
- `> 0.1` → **positif**
- `< -0.1` → **negatif**
- lainnya → **netral**

### 3. Ekstraksi Fitur
Menggunakan `TfidfVectorizer` untuk mengubah teks menjadi vektor numerik.

### 4. Split Data
Data dibagi menjadi 80% training dan 20% testing.

### 5. Pelatihan Model
Dilakukan beberapa skema pelatihan model:
- **Random Forest**
- **SVM**
- Model dievaluasi dengan **akurasi** dan **classification report**

### 6. Inference
Contoh prediksi model terhadap input manual.

### 7. Visualisasi
Distribusi label ditampilkan menggunakan `seaborn.countplot`.
