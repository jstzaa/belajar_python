print('==========================================================')
print('======    SELAMAT DATANG DI PROGRAM INPUT NILAI    =======')
print('==========================================================')

nama = input('Masukkan nama: ')
kelas = input('Masukkan kelas: ')
npm = input('Masukkan NPM: ')
programStudi = input('Masukkan program studi: ')
nilai1 = float(input('Masukkan Nilai 1: '))
nilai2 = float(input('Masukkan Nilai 2: '))
nilai3 = float(input('Masukkan Nilai 3: '))
average = (nilai1 + nilai2 + nilai3) / 3

print('')
print(f"Nama: {nama}")
print(f"Kelas: {kelas}")
print(f"Kelas: {npm}")
print(f"Program Studi: {programStudi}")
print(f"Rata-rata nilai: {average}")