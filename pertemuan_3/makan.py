print(" === Kalkulator Patungan Makan === ")

# 1. INPUT & VARIABEL (Tipe Data String)
nama = input("Masukkan nama Anda: ")

# 2. INPUT & TIPE DATA (Konversi string ke angka float dan integer)
# float digunakan untuk angka desimal (uang), int untuk bilangan bulat (orang/persen)
tagihan_awal = float(input("Total tagihan (Rp): "))
persen_tip = int(input("Persentase tip/pajak (misal: 10): "))
jumlah_orang = int(input("Jumlah orang yang ikut patungan: "))

# 3. OPERATOR ARITMATIKA
# Menghitung nominal tip (Perkalian dan Pembagian)
nominal_tip = tagihan_awal * (persen_tip / 100)

# Menghitung total tagihan keseluruhan (Penjumlahan)
total_tagihan = tagihan_awal + nominal_tip

# Menghitung patungan per orang (Pembagian)
bayar_per_orang = total_tagihan / jumlah_orang

# 4. OUTPUT
print("\n === Ringkasan Tagihan === ")
# Menggabungkan string dengan variabel menggunakan koma atau operator +
print("Halo, " + nama + "!")
print("Total tagihan beserta tip adalah: Rp", total_tagihan)
print("Setiap orang harus membayar: Rp", bayar_per_orang)