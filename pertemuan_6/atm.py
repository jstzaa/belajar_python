# Nama: Fahriza Kurniawan
# NPM: 267006111119
# Kelas: E

print("=== Simulasi Sistem ATM ===")

pin_sistem = 1234
kesempatan = 3
saldo = 500000
riwayat_transaksi = []

while kesempatan > 0:
    pinInsert = int(input("Masukkan PIN Anda: "))
    if pinInsert == pin_sistem:
        print("Login Berhasil!")
        break
    else:
        kesempatan -= 1
        print(f"PIN salah! sisa kesempatan: {kesempatan}")


if kesempatan == 0:
    print("Kartu diblokir!")
else:
    while True:
        print("\nMenu ATM")
        print("1. Tarik Tunai")
        print("2. Riwayat Transaksi")
        print("3. Keluar")

        pilihan = int(input("Pilih menu (1/2/3): "))

        if pilihan == 1:
            penarikan = int(input("Input nominal penarikan: "))
            if penarikan > saldo:
                print("Saldo tidak mencukupi!")
                continue
            else:
                saldo -= penarikan
                riwayat_transaksi.append(f"Tarik tunai: Rp{penarikan}")
                print(f"Sisa saldo: {saldo}")
        elif pilihan == 2:
            if len(riwayat_transaksi) == 0:
                print("Belum ada transaksi")
            else:
                for i in riwayat_transaksi:
                    print(i)
        elif pilihan == 3:
            print("Terima kasih sudah menggunakan ATM kami")
            break
        else:
            print("Input invalid")
