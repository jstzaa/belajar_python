# Nama: Fahriza Kurniawan
# NPM: 267006111119
# Kelas: E

print("=== SISTEM ONGKOS KIRIM PAKET ===")

jnsLayanan = input("Masukkan jenis layanan(reguler/kilat): ")
brtPaket = int(input("Berat paket (kg): "))
asuransi = input("Pakai asuransi paket? (y/n): ")
biayaPenanganan = 0
biayaAsuransi = 0
tarif = 0
ongKir = 0

if brtPaket > 0:
    if jnsLayanan == 'reguler':
        tarif = 5000
        ongKir = tarif * brtPaket
    elif jnsLayanan == 'kilat':
        tarif = 9000
        ongKir = tarif * brtPaket
    else:
        tarif = 6000
        ongKir = tarif * brtPaket
        print("Info layanan tidak dikenali, dianggap sebagai layanan lain dengan tarif 6000/kg")

    if brtPaket > 5:
        biayaPenanganan = 5000

    if asuransi == 'y':
        biayaAsuransi = 3000
    
else:
    print('Program error')
    exit()

print("=== RINCIAN BIAYA PENGIRIMAN ===")
print(f'Layanan: {jnsLayanan}')
print(f'Berat Paket: {brtPaket} kg')
print(f'Ongkos Kirim: {ongKir}')
print(f'Biaya Penanganan: {biayaPenanganan}')
print(f'Biaya asuransi: {biayaAsuransi}')
print("-------------------------- +")
print("Total", biayaPenanganan + ongKir + biayaAsuransi)
