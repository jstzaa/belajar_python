print("=== Simulasi Tabungan Liburan ===")
lama_hari = int(input("Berapa hari Anda ingin menabung: "))
total_uang = 0
print("\n--- Mulai Menabung ---")

for hari in range(1, lama_hari + 1):
    print(f'Hari ke: {hari}')
    total_uang += int(input("Masukkan Nominal Uang: "))
else:
    print(f'\nStatus: Misi menabung selama {hari} hari telah tuntas')
print('\n=== Hasil Tabungan ===')

if total_uang >= 200000:
    print(f'Uang Anda Rp{total_uang} - Keren! Bisa dipakai liburan ke luar kota.')
elif total_uang >= 50000:
    print(f'Uang Anda Rp{total_uang} - Lumayan! Bisa dipakai liburan di dalam kota.')
else:
    print(f'Uang Anda Rp{total_uang} - Uang Tidak Cukup! Jajan di dekat rumah saja.')