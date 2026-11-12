daftar_barang = [
    {"kode": "B001", "nama": "Keyboard", "harga": 450000, "stok": 12},
    {"kode": "B002", "nama": "Mouse", "harga": 150000, "stok": 5},
    {"kode": "B003", "nama": "Monitor", "harga": 1200000, "stok": 2}
]

def cari(kode_cari):
    for barang in daftar_barang:
        if barang["kode"] == kode_cari:
            return barang
    return None

def kurangi_stok(kode, jumlah):
    barang_ditemukan = cari(kode)
    
    if barang_ditemukan is not None:
        if barang_ditemukan["stok"] >= jumlah:
            barang_ditemukan["stok"] -= jumlah
            print(f"> Berhasil! Stok {barang_ditemukan['nama']} dikurangi {jumlah}. Sisa stok: {barang_ditemukan['stok']}")
        else:
            print(f"> Gagal! Stok {barang_ditemukan['nama']} tidak mencukupi (Sisa: {barang_ditemukan['stok']}).")
    else:
        print("> Gagal! Kode barang tidak ditemukan.")

while True:
    print("\n=== MENU GUDANG ===")
    print("1. Lihat Daftar Barang")
    print("2. Kurangi Stok Barang")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        print("\n-- DAFTAR BARANG --")
        for b in daftar_barang:
            print(f"[{b['kode']}] {b['nama']} - Stok: {b['stok']}")
            
    elif pilihan == "2":
        print("\n-- KURANGI STOK --")
        input_kode = input("Masukkan kode barang: ")
        input_jumlah = int(input("Masukkan jumlah yang dikurangi: "))
        
        kurangi_stok(input_kode, input_jumlah)
        
    elif pilihan == "3":
        print("Keluar dari program. Terima kasih!")
        break
        
    else:
        print("> Pilihan tidak valid, silakan coba lagi.")