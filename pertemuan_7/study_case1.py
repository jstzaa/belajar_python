# Nama: Fahriza Kurniawan
# NPM: 267006111119
# Kelas: E

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

i = 0
while i < len(matriks):
    j = 0
    total_baris = 0
    
    while j < len(matriks[i]):
        total_baris += matriks[i][j]
        j += 1
        
    print(f"Jumlah baris ke-{i+1} = {total_baris}")
    i += 1