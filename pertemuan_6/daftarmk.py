# Nama: Fahriza Kurniawan
# NPM: 267006111119
# Kelas: E

mata_kuliah = ["Algoritma", "Basis Data", "Jaringan"]

# --- BAGIAN 1: Menampilkan Daftar Awal ---
print("Daftar Mata Kuliah:")

i = 0
while i < len(mata_kuliah):
    print(f"{i+1} . {mata_kuliah[i]}")
    i += 1

print(f"Jumlah mata kuliah: {len(mata_kuliah)}")

# --- BAGIAN 2: Menambahkan Mata Kuliah ---
mk_baru = input("Mata kuliah ditambah: ")

mata_kuliah.append(mk_baru)

print("Daftar terbaru:")
i = 0
while i < len(mata_kuliah):
    print(f"{i+1} . {mata_kuliah[i]}")
    i += 1

# --- BAGIAN 3: Menghapus Mata Kuliah ---
mk_hapus = input("Mata kuliah dihapus: ")

mata_kuliah.remove(mk_hapus)

print("Daftar akhir:")
i = 0
while i < len(mata_kuliah):
    print(f"{i+1} . {mata_kuliah[i]}")
    i += 1