# Nama: Fahriza Kurniawan
# NPM: 267006111119
# Kelas: E

print('=== Simulasi Pelayanan Apotek ===')

jumlah_pasien = int(input('Berapa jumlah pasien yang harus dilayani?: '))
pasien_error = int(input('Pasien nomor berapa saat sistem kasir mati? (Ketik 0 jika tidak ada): '))
pendapatan_apotek = 0

for pasien in range(1, jumlah_pasien + 1):
    if pasien == pasien_error:
        print('\nINFO: Sistem kasir mati. Pelayanan dihentikan (Break)!')
        break
    else:
        print(f'\n--- Melayani Pasien Ke-{pasien} ---')

    total_obat = 0

    for obat in range(1, 4):
        if obat == 2:
            print('Obat 2 stok kosong. Obat dilewati (Continue).')
            continue
        else:
            print(f'Obat {obat} diserahkan (Harga Rp 10.000)')
            total_obat += 10000
    else:
        print(f'Status: Semua obat Pasien {pasien} telah diproses.')

    print('\n--- Total Tagihan Pasien ---')
    print(f'Total tagihan: {total_obat}')
    uang_bayar = 50000

    if uang_bayar > total_obat:
        print(f'Kembalian : Rp {uang_bayar - total_obat}')
    elif uang_bayar == total_obat:
        print('Uang pas. Terima kasih!')
    else:
        print(f'Kurang bayar : Rp {total_obat - uang_bayar}')

    pendapatan_apotek += total_obat

print('\n=== Laporan Tutup Apotek ===')
print(f'Pendapatan apotek: {pendapatan_apotek}')