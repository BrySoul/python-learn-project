#===================================================
#Project 01 : Kalkulator Interaktif & Struk Belanja
#===================================================

print("=" * 45)
print(" PROGRAM GENERATOR STRUK BELANJA ")
print("=" * 45)

#1. Input Informasi Toko & Kasir
nama_toko = input("Masukkan nama toko : ")
nama_kasir = input("Masukkan nama kasir : ")

#2. Inisiasi tempat Menyimpan Data
daftar_barang = []

#3. Perulangan Input Barang
while True:
    nama_barang = input("\nNama barang (ketik 'selesai' untuk menghitung): ")

    #Mengecek apakah user ingin menghentikan input
    if nama_barang.lower() == 'selesai':
        break

    #Mengambil input jumlah dan harga
    jumlah = int(input(f"Jumlah {nama_barang}: "))
    harga_satuan = float(input(f"Harga satuan {nama_barang}: Rp "))

    #Menghitung subtotal per item
    subtotal = jumlah * harga_satuan

    #Save data to the list in tuple
    daftar_barang.append((nama_barang, jumlah, harga_satuan, subtotal))

#Calculate total Item & Disc
total_belanja = sum(item[3] for item in daftar_barang)

#disc rule: disc 10% if total >= Rp 100rb
diskon = 0.0
if total_belanja >= 100000:
    diskon = total_belanja * 0.10

total_bayar = total_belanja - diskon

#Print struk
print("\n" + "=" *45)
print(f"{nama_toko.upper():^45}")
print(f"Kasir: {nama_kasir}")
print("=" *45)
print(f"{'No':<3} {'Barang' :<15} {'Qty' :<10} {'Subtotal' :>10}")
print("=" *45)

#Print
for index, (barang, qty, harga, sub) in enumerate(daftar_barang, start=1):
    print(f"{index:<3} {barang:<15} {qty:<5} {harga:>10,.0f} {sub:>10,.0f}")

print("-" * 45)
print(f"{'Total Belanja':<33}: Rp {total_belanja:>9,.0f}")
print(f"{'Diskon (10%)':<33}: Rp {diskon:>9,.0f}")
print(f"{'Total Bayar':<33}: Rp {total_bayar:>9,.0f}")
print("=" * 45)
print(f"{'TERIMA KASIH TELAH BERBELANJA!':^45}")
print("=" * 45)