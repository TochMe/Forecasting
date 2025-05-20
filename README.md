# Forecasting
### Deskripsi

Ini adalah website dashboard yang dibuat sebagai bagian dari proyek skripsi mahasiswa BINUS University. Website ini dibangun menggunakan Python dan Streamlit.

### ⚙️ Cara Menjalankan

1. **Download** semua file project ini ke komputer Anda.

2. **Buka folder** project ini menggunakan **Visual Studio Code (VSC)**.

3. Pastikan Anda sudah menginstal:

   * Python (disarankan versi 3.10 atau lebih baru)
   * Streamlit (`pip install streamlit`)
   * Plotly dan library pendukung lain jika diperlukan

4. Jalankan perintah berikut di terminal VSC:

```bash
streamlit run app.py
```

Jika perintah `streamlit` tidak dikenali, coba gunakan:

```bash
python -m streamlit run app.py
```

Jika belum menginstall streamlit:
---

### 🛠️ Instalasi Streamlit

Pastikan Python sudah terpasang di komputer Anda. Jika belum, Anda bisa unduh dari [python.org](https://www.python.org/downloads/).

Untuk meng-install **Streamlit**, Anda bisa langsung menjalankan perintah berikut:

```bash
pip install streamlit
```

---

### 🧪 (Opsional) Menggunakan Virtual Environment

Disarankan menggunakan **virtual environment** agar instalasi library terisolasi dari sistem utama.

Jalankan perintah berikut di folder project Anda (di terminal atau terminal VSC):

```bash
# Membuat virtual environment
python -m venv env

# Mengaktifkan virtual environment
env\Scripts\activate        # untuk Windows
source env/bin/activate     # untuk Mac/Linux

# Install streamlit di dalam virtual environment
pip install streamlit
```

Setelah aktif, jalankan project dengan:

```bash
streamlit run app.py
```

---


📝 Catatan
- Website ini berjalan secara lokal dan akan terbuka otomatis di browser.
- Pastikan semua dependensi sudah terinstal agar website bisa berjalan dengan lancar.
