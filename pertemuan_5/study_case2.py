# Nama: Fahriza Kurniawan
# NPM: 267006111119
# Kelas: E

print("=== Simulasi Tabungan Liburan ===")
lama_minggu = int(input("Berapa minggu Anda ingin menabung?: "))
total_uang = 0
print("\n--- Mulai Menabung ---")

for minggu in range(1, lama_minggu + 1):
    if minggu == 3:
        print("\n[ Darurat: Di minggu ke-3 celengan terpaksa dibongkar. Program berhenti! ]")
        break
        
    print("\n[ Memasuki Minggu ke-", minggu, "]")
    
    for hari in range(1, 4):
        if hari == 2:
            print("  - Hari ke- 2 (Libur, jadwal menabung dilewati)")
            continue
            
        print("  - Hari ke-", hari)
        
        for sesi in range(1, 3):
            print("    -> Sesi", sesi, ", - Memasukkan uang Rp 5.000")
            total_uang += 5000
            
else:
    print("\nStatus: Misi menabung selama", lama_minggu, "minggu telah tuntas!")
    
print("\n=== Hasil Tabungan ===")

if total_uang >= 200000:
    print("Uang Anda Rp", total_uang, "- Keren! Bisa dipakai liburan ke luar kota.")
elif total_uang >= 50000:
    print("Uang Anda Rp", total_uang, "- Lumayan! Bisa dipakai jalan-jalan di dalam kota.")
else:
    print("Uang Anda Rp", total_uang, "- Uang belum banyak, jajan di sekitar rumah saja.")