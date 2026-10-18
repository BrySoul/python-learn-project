# Project 01: Kalkulator Interaktif & Generator Struk Belanja

## 📌 Deskripsi Project

Program CLI (Command Line Interface) interaktif untuk menerima masukan data toko, nama kasir, serta daftar barang belanjaan beserta harga dan kuantitasnya. Program secara otomatis menghitung subtotal per barang, total belanja keseluruhan, mengaplikasikan potongan diskon berdasarkan syarat nominal tertentu, dan mencetak struk belanja dengan tata letak yang rapi.

---

## 🧠 Konsep Python yang Dipelajari

### 1. Input/Output & Type Casting

- **`input()`**: Mengambil masukan teks dari pengguna via terminal.
- **`int()` & `float()`**: Mengonversi tipe data string bawaan `input()` menjadi angka bulat (`int`) dan desimal (`float`) agar dapat dihitung secara matematis.
- **`print()`**: Menampilkan output teks ke layar terminal.

### 2. Kontrol Alur (Control Flow)

- **`while True`**: Membuat perulangan tidak terbatas sampai pengguna memutuskan berhenti.
- **`if nama_barang.lower() == 'selesai': break`**: Menghentikan perulangan secara paksa menggunakan `break` ketika input memenuhi kondisi tertentu, dipadu dengan method `.lower()` agar pencocokan string tidak sensitif terhadap huruf besar/kecil.
- **`if-else`**: Menentukan logika bisnis pemberian diskon 10% jika `total_belanja >= 100000`.

### 3. Struktur Data & Iterasi

- **`list` (`[]`)**: Digunakan sebagai wadah dinamis (`daftar_barang`) untuk menampung banyak item.
- **`tuple` (`()`)**: Menyimpan kelompok data satu barang `(nama_barang, jumlah, harga_satuan, subtotal)` secara tidak dapat diubah (_immutable_).
- **`append()`**: Menambahkan tuple barang baru ke dalam list.
- **`enumerate()`**: Mengambil indeks perulangan sekaligus isi itemnya untuk mencetak nomor urut otomatis mulai dari angka 1.
- **Generator Expression & `sum()`**: Menjumlahkan total harga secara ringkas (`sum(item[3] for item in daftar_barang)`).

### 4. Advanced String Formatting (`f-string`)

- **`:<15`**: Mengatur teks rata kiri dengan lebar bidang 15 karakter.
- **`:>10`**: Mengatur teks/angka rata kanan dengan lebar bidang 10 karakter.
- **`:^45`**: Mengatur teks berada di tengah-tengah (_center_) bidang selebar 45 karakter.
- **`:, .0f`**: Mengformat angka desimal menjadi format ribuan dengan pemisah koma tanpa angka di belakang koma.

---

## 🔍 Penjelasan Kode Baris demi Baris

| Baris Kode                                   | Fungsi & Penjelasan                                                                                        |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `nama_toko = input(...)`                     | Menyimpan nama toko yang diketik pengguna ke variabel `nama_toko`.                                         |
| `daftar_barang = []`                         | Membuka list kosong di memori untuk menampung semua transaksi.                                             |
| `while True:`                                | Membuka blok loop input interaktif tanpa batas.                                                            |
| `if nama_barang.lower() == 'selesai': break` | Mengubah string ke huruf kecil lalu menghentikan perulangan jika bernilai `'selesai'`.                     |
| `subtotal = jumlah * harga_satuan`           | Melakukan perkalian aritmatika dasar untuk menghitung harga total barang tersebut.                         |
| `daftar_barang.append(...)`                  | Memasukkan gabungan data item dalam satu tuple ke dalam list utama.                                        |
| `sum(item[3] for item in daftar_barang)`     | Mengambil elemen indeks ke-3 (subtotal) dari setiap tuple di dalam list lalu menjumlahkannya.              |
| `enumerate(..., start=1)`                    | Menghasilkan pasangan `(1, item1)`, `(2, item2)`, dst., untuk nomor struk.                                 |
| `f"{barang:<15} {qty:<5}"`                   | Menjamin kolom nama barang selalu selebar 15 spasi dan kuantitas selebar 5 spasi agar tabel struk sejajar. |

---

## 🚀 Cara Menjalankan Program

Buka terminal di direktori project dan jalankan:

```bash
python main.py
```
