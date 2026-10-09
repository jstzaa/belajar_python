print("=== Sistem Nilai Mahasiswa ===")

namaMhs = input("Nama Mahasiswa: ")
nilaiTugas = int(input("Nilai Tugas: "))
nilaiUTS = int(input("Nilai UTS: "))
nilaiUAS = int(input("Nilai UAS: "))

total_nilai = nilaiTugas + nilaiUTS + nilaiUAS

avg_nilai = total_nilai / 3

print("\n=== Hasil Perhitungan ===")
print(f"Nama: {namaMhs}")
print(f"Total nilai: {total_nilai}")
print(f"Rata-rata: {avg_nilai}")

print("\n=== Hasil Perhitungan ===")
print(f"Lulus: {avg_nilai >= 70}")
print(f"Nilai UAS lebih besar dari UTS?: {nilaiUAS > nilaiUTS}")
print(f"Nilai tugas == UTS?: {nilaiTugas == nilaiUTS}")