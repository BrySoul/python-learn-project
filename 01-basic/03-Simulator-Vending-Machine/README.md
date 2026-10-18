# Project 03: Simulator Vending Machine CLI

## 📌 Deskripsi Project

Program CLI (Command Line Interface) interaktif untuk mensimulasikan operasional mesin penjual otomatis (_vending machine_). Program dapat menerima masukan pecahan uang tunai dari pengguna, memvalidasi kelayakan pecahan uang, menampilkan katalog produk beserta status stok dan harganya, memproses transaksi pembelian barang, menghitung pecahan uang kembalian secara otomatis menggunakan algoritma _greedy_, serta menyediakan fitur pembatalan (_refund_) saldo.

---

## 🧠 Konsep Python yang Dipelajari

### 1. Input/Output & Type Casting

- **`input()`**: Mengambil masukan pilihan menu, nominal uang, dan kode barang dari pengguna via terminal.
- **`int()` & `str.isdigit()`**: Memvalidasi dan mengonversi input string angka dari terminal menjadi tipe data integer (`int`) agar dapat dihitung secara matematis tanpa memicu _runtime error_.
- **`print()`**: Menampilkan menu interaktif, status saldo, katalog produk, dan rincian pecahan kembalian ke layar terminal.

### 2. Kontrol Alur (Control Flow) & Validasi

- **`while True`**: Membuat perulangan interaktif utama mesin hingga pengguna memutuskan untuk keluar dari aplikasi (`0`).
- **`if-elif-else`**: Menangani logika navigasi menu utama, pengecekan ketersediaan stok, kecukupan saldo transaksi, dan pengujian keabsahan pecahan uang.
- **Operator `in`**: Memeriksa apakah nominal uang yang dimasukkan pengguna terdaftar di dalam daftar pecahan resmi yang diterima mesin (`ACCEPTED_DENOMINATIONS`).
- **`break` & `continue`**: Mengontrol jalannya alur perulangan saat keluar aplikasi atau ketika terjadi kesalahan input dari pengguna.

### 3. Struktur Data & Iterasi

- **`dict` (Nested Dictionary)**: Mengorganisir inventaris produk secara efisien dengan kode barang (`"A1"`, `"B1"`) sebagai _key_ utama dan detail barang (`name`, `price`, `stock`) sebagai _value_ berupa dictionary internal.
- **`list` (`[]`)**: Menyimpan daftar pecahan uang kertas/logam resmi yang dapat diterima oleh sistem mesin.
- **Method `.items()`**: Mengiterasi pasangan _key_ (kode barang) dan _value_ (detail produk) secara bersamaan untuk menampilkan katalog produk secara terstruktur.

### 4. Operator Aritmatika & Algoritma Greedy

- **Floor Division (`//`)**: Menghitung jumlah lembaran/kepingan pecahan uang kembalian terbesar yang bisa dikeluarkan.
- **Modulo (`%`)**: Mengambil sisa nominal uang yang belum terpecah untuk diproses ke pecahan nominal yang lebih kecil berikutnya.
- **Pengurangan & Penjumlahan**: Menghitung akumulasi saldo masuk, pengurangan stok barang, dan kalkulasi total kembalian.

### 5. String Formatting & Manipulation (`f-string`)

- **`:<18`**: Mengatur nama produk agar rata kiri dengan lebar bidang tetap 18 karakter sehingga tampilan tabel produk rapi dan sejajar.
- **`:,`**: Mengformat angka nominal harga dan saldo agar memiliki pemisah ribuan (contoh: `10,000`).
- **`.strip()` & `.upper()`**: Membersihkan spasi liar pada input serta mengubah masukan kode barang menjadi huruf kapital agar pencarian kode tidak bersifat _case-sensitive_.

---

## 🔍 Penjelasan Kode Baris demi Baris

| Baris Kode                                                                 | Fungsi & Penjelasan                                                                               |
| :------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| `ACCEPTED_DENOMINATIONS = [1000, 2000, 5000, ...]`                         | Mengunci daftar nominal uang sah yang dapat diterima oleh mesin.                                  |
| `inventory = {"A1": {"name": "Mineral Water", "price": 5000, "stock": 5}}` | Menyimpan database produk, harga, dan stok menggunakan _nested dictionary_.                       |
| `if amount not in ACCEPTED_DENOMINATIONS:`                                 | Memeriksa apakah nominal uang yang dimasukkan pengguna sesuai dengan standar pecahan mesin.       |
| `current_balance += amount`                                                | Menambahkan uang yang dimasukkan pengguna ke dalam akumulasi saldo transaksi berjalan.            |
| `if code not in inventory:`                                                | Memvalidasi keberadaan kode barang yang diketik pengguna pada inventaris mesin.                   |
| `if inventory[code]["stock"] <= 0:`                                        | Memeriksa ketersediaan stok fisik barang sebelum memproses transaksi pembelian.                   |
| `if balance < item["price"]:`                                              | Membandingkan saldo tersimpan dengan harga barang untuk memastikan uang mencukupi.                |
| `inventory[code]["stock"] -= 1`                                            | Mengurangi jumlah stok barang sebanyak 1 unit secara langsung di dalam dictionary inventaris.     |
| `change = balance - item["price"]`                                         | Menghitung sisa nominal uang kembalian yang harus dikembalikan kepada pembeli.                    |
| `count = remaining // denom`                                               | Algoritma Greedy: Menghitung lembar pecahan terbesar yang muat ke dalam sisa kembalian.           |
| `remaining %= denom`                                                       | Algoritma Greedy: Memperbarui sisa uang kembalian yang belum dipecah menggunakan operator modulo. |
| `f"[{code}] {item['name']:<18} - IDR {item['price']:,}"`                   | Mengformat baris katalog barang agar rapi dengan rata kiri nama produk dan format ribuan harga.   |
