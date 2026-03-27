import json
import os

def tampilkan_menu():
    os.system('clear')
    print("===============================")
    print("   SISTEM DIGITAL RW HASBIH    ")
    print("===============================")
    print("1. Lihat Daftar Warga")
    print("2. Cek Status QR Code")
    print("3. Keluar")
    print("-------------------------------")

def baca_data():
    try:
        # Menyesuaikan path jika file ada di folder yang sama
        with open('data_warga.json', 'r') as f:
            data = json.load(f)
            return data['warga']
    except FileNotFoundError:
        print("\n[!] File data_warga.json tidak ditemukan!")
        print("Pastikan file tersebut ada di folder yang sama.")
        return []

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == '1':
        warga = baca_data()
        if warga:
            print("\nDAFTAR WARGA:")
            for i, w in enumerate(warga, 1):
                print(f"{i}. {w['nama']} - Blok {w['blok']}")
        input("\nTekan Enter untuk kembali...")
    
    elif pilihan == '2':
        print("\n[INFO] Fitur QR Code sedang dalam pengembangan.")
        input("\nTekan Enter untuk kembali...")
    
    elif pilihan == '3':
        print("\nTerima kasih! Program ditutup.")
        break
    else:
        print("\nPilihan tidak valid.")
        input("\nTekan Enter untuk mencoba lagi...")

