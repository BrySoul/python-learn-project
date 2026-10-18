# ===================================================
# PROJECT 02: GAME TEBAK ANGKA DENGAN BATAS KESEMPATAN
# ===================================================

import random

print("=" * 45)
print(" Game Tebak Angka (1 - 100) ")
print("=" * 45)

#Komputer memilih angka acak
angka_rahasia = random.randint(1, 100)
batas_kesempatan = 7
percobaan = 0

print(f"Saya telah memilih nagka rahasia antara 1 sampai 100.")
print(f"Kamu memiliki {batas_kesempatan} kali kesempatan tebakan!\n")

#Perulangan game
while percobaan < batas_kesempatan:
    percobaan += 1
    sisa_kesempatan = batas_kesempatan - percobaan

    #Input tebakan pengguna
    try:
        tebakan = int(input(f"[-] Percobaan ke-{percobaan} | Masukkan tebakanmu: "))
    except ValueError:
        print(" [!] Input tidak valid! Harap masukkan angka bulat.\n")
        percobaan -= 1
        continue

    #Validasi jangkauan angka
    if tebakan < 1 or tebakan > 100:
        print(" [!] Angka harus di antara 1 sampai 100!\n")
        percobaan -= 1
        continue

    #Logika Pengecekan Tebakan
    if tebakan == angka_rahasia:
        print("\n" + "=" *45)
        print(f" SELAMAT! Tebakanmu BENAR ({angka_rahasia})!")
        print(f" Kamu berhasil menebak dalam {percobaan} kali percobaan.")
        print("=" * 45)
        break
    elif tebakan < angka_rahasia:
        print(f" Terlalu KECIL! (Sisa kesempatan: {sisa_kesempatan}\n)")
    else:
        print(f" Terlalu BESAR! (Sisa kesempatan: {sisa_kesempatan}\n)")

#Hasil jika kesempatan habis
else:
    print("\n" + "=" * 45)
    print("GAME OVER! Kesempatanmu telah habis.")
    print(f" Angka rahasia yang benar adalah: {angka_rahasia}")
    print("=" * 45)