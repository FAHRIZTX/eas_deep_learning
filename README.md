# Predict Risk Factors for Cardiovascular Heart Disease

Oleh:
Kelompok - 8
1. Muhammad Ikraam Fahriono (1462100013)
2. Rika Yulianto (1462100048)
3. Nifil Afrisma (1462100050)
4. Mochamad Fikri Dwi Fardian (1462100220)

Dosen Pengampu:
Bapak Andrey Kartika Widhy Hapantenda, S.Kom., M.Kom.

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Convolutional Neural Network.
Adapun variabel yang digunakan untuk membuat model guna memprediksi Risiko Penyakit Jantung Kardiovaskular:

| Variabel    | Deskripsi                                                                 |
|-------------|---------------------------------------------------------------------------|
| age         | Usia partisipan dalam hari                                                |
| gender      | Jenis kelamin partisipan (1: Pria, 2: Wanita)                             |
| height      | Tinggi badan partisipan dalam sentimeter                                  |
| weight      | Berat badan partisipan dalam kilogram                                     |
| ap_hi       | Tekanan darah sistolik (mmHg)                                             |
| ap_lo       | Tekanan darah diastolik (mmHg)                                            |
| cholestrol  | Tingkat kolesterol (1: normal, 2: di atas normal, 3: jauh di atas normal) |
| gluc        | Tingkat glukosa (1: normal, 2: di atas normal, 3: jauh di atas normal)    |
| smoke       | Status merokok (0: Tidak, 1: Ya)                                          |
| alco        | Konsumsi alkohol (0: Tidak, 1: Ya)                                        |
| active      | Aktivitas fisik (0: Tidak, 1: Ya)                                         |
| cardio      | Diagnosis penyakit kardiovaskular (0: Tidak ada, 1: Ada)                  |


---
## Requirements

- Python Version `>= 3.9`

## Installation

```bash
$ git clone https://github.com/FAHRIZTX/eas_deep_learning.git
$ cd eas_deep_learning
$ python -m pip install -r requirements.txt
$ python app.py
```

### Akses melalui Website

1. Anda akan diberikan URL untuk membuka website berupa [http://localhost:5000](http://localhost:5000) atau [http://127.0.0.1:5000](http://127.0.0.1:5000)
2. Buka URL dengan browser, coba masukkan data yang ingin di prediksi.
3. Anda akan diberikan data hasil prediksi.


---

## Folder, file, dan kegunaannya

-   templates/
    -   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route untuk API
-   HeartDataCNNModel.h5 --> Model CNN yang sudah di-training
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Regresi Linier
-   Dockerfile --> File untuk menjalankan via Docker
  
