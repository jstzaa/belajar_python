while True:
    nama = input("Masukkan nama: ")
    if nama == "stop":
        break

angka = [1, 2, 3, 4, 5]
i = 0
while i < len(angka):
    print(angka[i])
    i += 1

angka.append(int(input("Masukkan angka: ")))
print(angka)

angka.pop(0)
print(angka)