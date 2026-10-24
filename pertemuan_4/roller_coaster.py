# Nama: Fahriza Kurniawan
# NPM: 267006111119
# Kelas: E

print("=== PENGECEKAN TIKET ROLLER COASTER ===")

umur = int(input("Masukkan umur: "))
harga = 50000
diskon = 0

# Pengecekan pertama
if umur >= 12:
    tinggi = float(input("Masukkan tinggi: "))
    if tinggi >= 150:
        print("\nSyarat terpenuhi! Anda boleh lanjut")
        member = input("Apakah sudah mempunyai member? (y/n): ")

        if member == 'y':
            diskon = 10000
            harga -= diskon
            print("Anda dapat diskon: Rp", diskon)

        print("Total tiket: Rp", harga)
        uang = int(input("Masukkan uang Anda: "))

        if uang == harga:
            print("Uang Anda pas")
        elif uang > harga:
            print("Uang Anda lebih, kembalian: Rp", uang - harga)
        else:
            print("Uang Anda kurang")
    else:
        print("Maaf, tinggi Anda belum mencukupi, minimal (150cm)")
else:
    print("Maaf, wahana ini khusus untuk 12 tahun ke atas")