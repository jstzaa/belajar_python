print("=== Sistem Pendataan Gym ===")
umur = int(input("Masukkan umur Anda (tahun): "))
if umur >= 16 and umur < 100:
    kelas = str(input("Pilihan Kelas (yoga / boxing / zumba): "))
    if kelas == "yoga":
        biaya_kelas = 300000
    elif kelas == "boxing":
        biaya_kelas = 400000
    elif kelas == "zumba":
        biaya_kelas = 250000
    else:
        print("Info: Kelas tidak dikenali, dialihkan ke Kelas Reguler.")
        kelas = "Reguler"
        biaya_kelas = 200000

    loker = str(input("Apakah Anda ingin menyewa loker? (ya / tidak): "))
    if loker == "ya" or loker == "y":
        print("Info: Fasilitas loker ditambahkan.")
        biaya_loker = 50000 
    else:
        biaya_loker = 0

else :
    print("Error: Maaf, usia minimal mendaftar adalah 15 tahun")
    exit()

biaya_total = biaya_kelas + biaya_loker

print("\n=== Rincian Tagihan Gym ===")
print(f"Kelas yang dipilih: {kelas}")
print(f"Biaya Kelas: Rp. {biaya_kelas}")
print(f"Biaya Loker: Rp. {biaya_loker}")
print("--------------------------- +")
print(f"Total Bayar: Rp. {biaya_total}")