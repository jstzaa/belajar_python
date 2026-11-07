nilai = [
    [90, 60, 70],
    [90, 60, 70],
    [90, 60, 70],
    [90, 60, 70],
]

print(nilai)
print(nilai[1])
print(len(nilai))
print(len(nilai[1]))

buku = {"kode" : "B01", "judul" : "Laut Bercerita", "stok": 5}

print(buku["judul"])
print(buku.get("stok"))
print(len(buku))

buku["stok"] = 10
buku["penulis"] = "Leila S"
print(buku)
buku.pop("penulis")
print(buku)

perpus = [
    {"kode" : "B01", "judul" : "Laut Bercerita", "stok": 5},
    {"kode" : "B01", "judul" : "Filosofi Teras", "stok": 5},
    {"kode" : "B01", "judul" : "Madilog", "stok": 5},
]

print(perpus[0]["judul"])