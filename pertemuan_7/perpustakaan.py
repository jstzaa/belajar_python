perpus = [
    {"kode": "001", "judul": "Python Dasar", "status": "tersedia"},
    {"kode": "002", "judul": "Basis Data", "status": "tersedia"},
    {"kode": "003", "judul": "Jaringan", "status": "dipinjam"}
]

def tampilkan():
    i = 0
    while i < len(perpus):
        print(perpus[i]["kode"],
              perpus[i]["judul"],
              perpus[i]["status"])
        i += 1

def cari(kode):
    i = 0
    while i < len(perpus):
        if perpus[i]["kode"] == kode:
            return i
        i += 1
    return - 1

def pinjam(kode):
    i = cari(kode)
    if i == -1:
        print("Kode tidak ada.")
        return
    if perpus[i]["status"] == "dipinjam":
        print("Buku sedang dipinjam.")
        return
    perpus[i]["status"] = "dipinjam"
    print("Berhasil dipinjam.")

while True:
    print("1.Lihat 2.Pinjam 0.Keluar")
    pilih = input("Pilih: ")
    if pilih == "0":
        break
    if pilih == "1":
        tampilkan()
    if pilih == "2":
        kode = input("Kode buku: ")
        pinjam(kode)