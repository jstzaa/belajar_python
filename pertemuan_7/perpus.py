perpus = [
    {"kode": "001", "judul": "Python Dasar", "status": "tersedia"},
    {"kode": "002", "judul": "Basis Data", "status": "tersedia"},
    {"kode": "003", "judul": "Jaringan", "status": "dipinjam"}
]

cari = input("masukan kode yang ingin anda cari: ")
i = 0
while i < len(perpus):
    if perpus[i]["kode"] == cari:
        if perpus[i]["status"] == "tersedia":
            # Accept | XReject | + line - line
            print("kode", perpus[i]["kode"], "judul", perpus[i]["judul"], "status", perpus[i]["status"])
            print("buku ditemukan, mengubah status nya dari tersedia -> dipinjam")
            perpus[i]["status"] = "dipinjam"
            print(perpus[i]["kode"], perpus[i]["judul"], perpus[i]["status"])
        else:
            print("buku sudah dipinjam")
            print(perpus[i]["kode"], perpus[i]["judul"], perpus[i]["status"])
        break
    i += 1
else:
    print("kode yang anda cari tidak ada")