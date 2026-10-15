print("=== PENGECEKAN TIKET ROLLER COASTER ===")

umur = int(input("Masukkan umur: "))
tinggi = float(input("Masukkan tinggi: "))
harga = 50000

# Pengecekan pertama
if umur >= 12:
    if tinggi >= 150:
        print("\nSyarat terpenuhi! Anda boleh lanjut")
        member = input("Apakah sudah mempunyai member? (y/n)")

        if member == 'y':
            harga -= 10000
            print("Anda dapat diskon!")

        print("Total tiket: Rp.", harga)
        uang = float(input("Masukkan uang Anda: Rp."))

        if uang == harga:
            print("Uang Anda pas")
        elif uang > harga:
            print("Uang Anda lebih, kembalian Rp.", uang - harga)
        else:
            print("Uang Anda kurang")
    else:
        print("Maaf, tinggi Anda belum mencukupi, minimal (150cm)")
else:
    print("Maaf, wahana ini khusus untuk 15 tahun ke atas")