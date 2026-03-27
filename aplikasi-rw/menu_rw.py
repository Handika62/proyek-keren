import json
import os

def tampilkan_menu():
    os.system('clear')
    print("===============================")
    print("   SISTEM DIGITAL RW HASBIH    ")
    print("===============================")
    print("1. Lihat Daftar Warga")
    print("2. Tambah Data Warga Baru")
    print("3. Cek Status QR Code")
    print("4. Keluar")
    print("-------------------------------")

def baca_data():
    try:
        with open('data_warga.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"warga": []}

def simpan_data(data):
    with open('data_warga.json', 'w') as f:
        json.dump(data, f, indent=4)

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        data = baca_data()
        warga = data.get('warga', [])
        print("\nDAFTAR WARGA:")
        if not warga:
            print("Belum ada data warga.")
        for i, w in enumerate(warga, 1):
            print(f"{i}. {w['nama']} (NIK: {w.get('nik', '-')}) - Blok {w['blok']}")
        input("\nTekan Enter untuk kembali...")
    
    elif pilihan == '2':
        print("\n--- TAMBAH WARGA BARU ---")
        nama = input("Nama Lengkap: ")
        nik = input("Nomor NIK   : ")
        kk = input("Nomor KK    : ")
        blok = input("Blok Rumah  : ")
        
        data = baca_data()
        data['warga'].append({
            "nama": nama,
            "nik": nik,
            "no_kk": kk,
            "blok": blok
        })
        simpan_data(data)
        print("\n[SUKSES] Data warga berhasil disimpan!")
        input("\nTekan Enter untuk kembali...")

    elif pilihan == '3':
        print("\n[INFO] Fitur QR Code sedang dalam pengembangan.")
        input("\nTekan Enter untuk kembali...")
    
    elif pilihan == '4':
        print("\nTerima kasih! Program ditutup.")
        break

