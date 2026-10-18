# Project 02: Game Tebak Angka dengan Batas Kesempatan

## 📌 Deskripsi Project

Program permainan CLI interaktif di mana komputer mengacak sebuah angka dari 1 hingga 100, dan pemain bertugas menebak angka tersebut dalam batas maksimal 7 kali percobaan. Program memberikan respon real-time apakah angka tebakan pemain terlalu besar atau terlalu kecil.

---

## 🧠 Konsep Python yang Dipelajari

### 1. Modul Bawaan (`import random`)

- **`random.randint(a, b)`**: Menggenerasi angka bulat acak dalam rentang inklusif antara `a` sampai `b`.

### 2. Pengondisian Lanjutan (`if-elif-else`)

- Membandingkan nilai `tebakan` dengan `angka_rahasia` untuk menentukan petunjuk arah tebakan (terlalu kecil, terlalu besar, atau benar).

### 3. Kontrol Perulangan (`while-else`, `break`, `continue`)

- **`while percobaan < batas_kesempatan`**: Mengulang proses tebakan selama jatah kesempatan masih ada.
- **`continue`**: Melompati sisa baris di dalam loop dan langsung kembali ke awal perulangan saat terjadi kesalahan input pengguna.
- **`break`**: Menghentikan permainan secara instan begitu angka rahasia berhasil ditebak.
- **Blok `else` pada `while`**: Fitur khusus Python di mana blok `else` dieksekusi **hanya jika** loop selesai secara alami tanpa dihentikan oleh perintah `break` (menandakan pemain kehabisan kesempatan).

### 4. Penanganan Error Dasar (`try-except`)

- Menggunakan `try-except ValueError` untuk mencegah program mendadak _crash_ jika pengguna menginput karakter selain angka bulat.

---

## 🔍 Penjelasan Kode Baris demi Baris

| Baris Kode                     | Fungsi & Penjelasan                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `import random`                | Mengimpor library standar Python untuk membuat bilangan acak.                                                                           |
| `random.randint(1, 100)`       | Menghasilkan angka acak dari 1 sampai 100 dan menyimpannya di variabel `angka_rahasia`.                                                 |
| `try: tebakan = int(...)`      | Mencoba mengonversi input pengguna menjadi bilangan bulat; jika gagal (misal user mengetik huruf), eksekusi berpindah ke blok `except`. |
| `except ValueError:`           | Menangkap error tipe nilai dan menampilkan pesan peringatan tanpa menghentikan jalurnya program.                                        |
| `percobaan -= 1` & `continue`  | Mengembalikan nilai hitungan percobaan dan mengulang loop ke atas agar kesempatan pemain tidak hangus akibat kesalahan input.           |
| `if tebakan == angka_rahasia:` | Memeriksa apakah tebakan cocok dengan angka acak komputer.                                                                              |
| `while ... else:`              | Blok `else` pada akhir loop hanya berjalan jika perulangan `while` selesai hingga kesempatan ke-7 tanpa kena `break`.                   |

