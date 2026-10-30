print("=== Simulasi Pengiriman Paket Khusus ===")

total_gedung = int(input("Masukkan jumlah gedung yang harus dikunjungi: "))
gedung_renovasi = int(input("Gedung nomor berapa yang sedang direnovasi? (Ketik 0 jika tidak ada): "))

for gedung in range(1, total_gedung + 1):
    print("\n--- Memasuki Gedung", gedung, "---")
    
    for lantai in range(1, 4):
        if lantai == 2:
            print("Lantai 2 dikunci (Area Terlarang), kurir melompat ke lantai berikutnya.")
            continue
            
        if gedung == gedung_renovasi:
            print("BAHAYA! Gedung sedang direnovasi. Kurir membatalkan pengiriman dan keluar gedung!")
            break
            
        print("Paket sukses diantar ke Lantai", lantai)
        
    else:
        print("Status: Pengiriman di Gedung", gedung, "tuntas 100% tanpa kendala.")

total_jarak = total_gedung * 15

print("\n=== Laporan Akhir ===")
if total_jarak >= 75:
    print("Total Jarak:", total_jarak, "KM. Kurir kelelahan dan butuh istirahat panjang.")
elif total_jarak >= 30:
    print("Total Jarak:", total_jarak, "KM. Hari yang cukup melelahkan namun sukses.")
else:
    print("Total Jarak:", total_jarak, "KM. Rute pendek, kurir bisa langsung pulang.")