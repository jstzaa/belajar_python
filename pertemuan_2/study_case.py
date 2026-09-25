#==========================================================
#============    STUDY CASE INPUT OUTPUT    ===============
#==========================================================

namaPenyewa = input('Nama Penyewa: ')
umurPenyewa = int(input('Umur Penyewa: '))
lamaPenyewaan = int(input('Lama Penyewaan (jam): '))
uangPembayaran = float(input('Uang Pembayaran: '))

namaTempat = 'Bike Rental Bandung'
jenisSepeda = 'Sepeda Gunung'
sepedaTersedia = True
hargaSewa = 25000.0

print('')
print('===== INFORMASI / DATA PENYEWAAN SEPEDA =====')
print('Nama Tempat: ', namaTempat)
print('Jenis Sepeda: ', namaTempat)
print('Sepeda Tersedia: ', sepedaTersedia)
print('Harga Sewa / Jam: ', hargaSewa)

print('')
print('===== DATA PENYEWA =====')
print(f"Nama Penyewa : {namaPenyewa}")
print(f"Umur Penyewa : {umurPenyewa}")
print(f"Lama Penyewaan : {lamaPenyewaan}")
print(f"Uang Pembayaran : {uangPembayaran}")

print('')
print('===== TIPE DATA MASING-MASING VARIABLE =====')
print('namaTempat : ', type(namaTempat))
print('jenisSepeda : ', type(jenisSepeda))
print('sepedaTersedia : ', type(sepedaTersedia))
print('hargaSewa : ', type(hargaSewa))
print('namaPenyewa : ', type(namaPenyewa))
print('umurPenyewa : ', type(umurPenyewa))
print('lamaPenyewaan : ', type(lamaPenyewaan))
print('uangPembayaran : ', type(uangPembayaran))