import json
import random
import math
import datetime
import os

FILE_STOK = "stok_minimarket.json"

# --- FUNGSI DATABASE (BACA & TULIS JSON) ---

def muat_stok():
    if not os.path.exists(FILE_STOK):
        return []
    with open(FILE_STOK, "r") as file:
        return json.load(file)

def simpan_stok(data):
    with open(FILE_STOK, "w") as file:
        json.dump(data, file, indent=4)

# --- FUNGSI PENCARI (PRODUSEN SINYAL) ---

def cari_barang(data_stok, kode):
    i = 0
    while i < len(data_stok):
        if data_stok[i]["kode"] == kode:
            return i  # Kembalikan angka (indeks) kalau ketemu
        i += 1
    return "tidak ada"  # Sinyal gagal pengganti -1

# --- FUNGSI FITUR UTAMA ---

def lihat_barang():
    data = muat_stok()
    if len(data) == 0:
        print("\nStok masih kosong! Silakan tambah barang dulu.")
        return

    print("\n--- KATALOG MINIMARKET ---")
    i = 0
    while i < len(data):
        brg = data[i]
        print(f"Kode: {brg['kode']} | {brg['nama']} | Stok: {brg['stok']} | Harga: Rp{brg['harga']}")
        i += 1

def tambah_barang():
    data = muat_stok()
    kode = input("Masukkan kode barang (ex: M01): ")

    # Cek dulu apakah kode sudah dipakai
    if cari_barang(data, kode) != "tidak ada":
        print("ERROR: Kode barang sudah ada di sistem!")
        return

    nama = input("Nama barang: ")
    stok = int(input("Jumlah stok: "))
    harga = int(input("Harga satuan: "))

    barang_baru = {
        "kode": kode,
        "nama": nama,
        "stok": stok,
        "harga": harga
    }

    data.append(barang_baru)
    simpan_stok(data)
    print(f"Barang {nama} berhasil ditambahkan ke database JSON!")

def hapus_barang():
    data = muat_stok()
    kode = input("Masukkan kode barang (ex: M01): ")
    i = cari_barang(data, kode)

    if i != "tidak ada":
        del data[i]
        simpan_stok(data)
        print(f"Barang {kode} berhasil dihapus dari database JSON!")
        return


def fitur_kasir():
    data = muat_stok()
    if len(data) == 0:
        print("Kasir tutup, barang masih kosong.")
        return

    kode_beli = input("\nMasukkan kode barang yang dibeli: ")
    i = cari_barang(data, kode_beli)

    # Satpam 1: Cek keberadaan barang
    if i == "tidak ada":
        print("ERROR: Barang tidak ditemukan di rak.")
        return

    jumlah_beli = int(input("Berapa banyak? "))

    # Satpam 2: Cek apakah stok cukup
    if data[i]["stok"] < jumlah_beli:
        print(f"ERROR: Stok tidak cukup! Sisa stok cuma {data[i]['stok']}.")
        return

    # --- RUANG VIP (Proses Transaksi Aman) ---

    # Potong stok di memori
    data[i]["stok"] -= jumlah_beli
    simpan_stok(data)  # Langsung simpan pemotongan stok ke file JSON

    # Perhitungan Uang
    subtotal = data[i]["harga"] * jumlah_beli
    pajak = subtotal * 0.11  # Pajak PPN 11%
    total_bayar = subtotal + math.ceil(pajak)  # Pembulatan pajak ke atas pakai math

    # Cetak Struk (Pakai datetime & random)
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    no_resi = random.randint(1000, 9999)  # Bikin ID TRX acak 4 digit

    print(f"\n========================================")
    print(f"            STRUK PEMBELIAN             ")
    print(f" Waktu: {waktu}")
    print(f" No TRX: INV-{no_resi}")
    print(f"----------------------------------------")
    print(f" {data[i]['nama']} (x{jumlah_beli})")
    print(f" Subtotal : Rp{subtotal}")
    print(f" PPN (11%) : Rp{math.ceil(pajak)}")
    print(f"----------------------------------------")
    print(f" TOTAL BAYAR : Rp{total_bayar}")
    print(f"========================================\n")

# --- MENU UTAMA ---

print("=== SISTEM MINIMARKET ===")
while True:
    print("\n[ MENU KASIR ]")
    print("1. Lihat Stok Barang")
    print("2. Tambah Barang Masuk")
    print("3. Kasir (Beli Barang)")
    print("4. Hapus Stok")
    print("5. Tutup Toko")

    pilih = input("Pilih menu (1-5): ")

    if pilih == "5":
        print("Sistem dimatikan. Data aman di JSON.")
        break
    elif pilih == "1":
        lihat_barang()
    elif pilih == "2":
        tambah_barang()
    elif pilih == "3":
        fitur_kasir()
    elif pilih == "4":
        hapus_barang()
    else:
        print("Pilihan tidak valid.")