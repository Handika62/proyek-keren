import json
import os
import getpass
import qrcode

ADMIN_USER = "hasbih"
ADMIN_PASS = "12345"

def tampilkan_header(judul):
    os.system('clear')
    print("="*40)
    print(f"   {judul}   ")
    print("="*40)

def baca_data():
    try:
        with open('data_warga.json', 'r') as f:
            return json.load(f)
    except:
        return {"warga": []}

def simpan_data(data):
    with open('data_warga.json', 'w') as f:
        json.dump(data, f, indent=4)

def menu_pompa():
    while True:
        tampilkan_header("UNIT BISNIS: SOLUSI POMPA AIR")
        print("1. SOP Pengecekan Mesin Mati")
        print("2. Daftar Harga Jasa Service")
        print("3. Kembali ke Menu Utama")
        print("-" * 40)
        pilih = input("Pilih (1-3): ")
        
        if pilih == '1':
            print("\n[SOP] PENGECEKAN MESIN MATI:")
            print("1. Cek Arus Listrik (Steker & Kabel)")
            print("2. Cek Kapasitor (Ganti jika lemah)")
            print("3. Cek Otomatis/Pressure Switch")
            print("4. Cek Gulungan/Spul (Gunakan Multitester)")
            input("\nTekan Enter...")
        elif pilih == '2':
            print("\nDAFTAR ESTIMASI HARGA:")
            print("- Service Ringan  : Rp 75.000")
            print("- Ganti Kapasitor : Rp 125.000")
            print("- Gulung Dinamo   : Rp 350.000+")
            print("- Bongkar Pasang  : Rp 150.000")
            input("\nTekan Enter...")
        elif pilih == '3': break

def menu_admin():
    while True:
        tampilkan_header("HALAMAN ADMIN - KELOLA WARGA")
        print("1. Lihat Daftar Seluruh Warga")
        print("2. Form Pendaftaran Warga Baru")
        print("3. Cari Warga (Nama/NIK)")
        print("4. Tampilkan QR Code Warga")
        print("5. Logout & Kembali")
        pilih = input("\nPilih (1-5): ")
        data = baca_data(); warga = data.get('warga', [])

        if pilih == '1':
            for i, w in enumerate(warga, 1):
                print(f"{i}. {w['nama']} | NIK: {w.get('nik')}")
            input("\nEnter...")
        elif pilih == '2':
            nama = input("Nama: "); nik = input("NIK: "); kk = input("KK: ")
            warga.append({"nama": nama, "nik": nik, "no_kk": kk})
            simpan_data(data); input("[SUKSES] Simpan. Enter...")
        elif pilih == '3':
            cari = input("Nama/NIK: ").lower()
            hasil = [w for w in warga if cari in w.get('nama','').lower() or cari in w.get('nik','')]
            for h in hasil: print(f"- {h['nama']} (NIK: {h['nik']})")
            input("\nEnter...")
        elif pilih == '4':
            nik_qr = input("NIK: ")
            w_qr = [w for w in warga if w.get('nik') == nik_qr]
            if w_qr:
                qr = qrcode.QRCode(); qr.add_data(f"RW-HASBIH\n{w_qr[0]['nama']}")
                qr.print_ascii()
            else: print("Data tak ditemukan.")
            input("\nEnter...")
        elif pilih == '5': break

while True:
    tampilkan_header("SISTEM DIGITAL KELUARGA HASBIH")
    print("1. Akses Menu Admin (RW)")
    print("2. Unit Bisnis (Solusi Pompa Air)")
    print("3. Keluar")
    p = input("\nPilih (1-3): ")
    if p == '1':
        u = input("Username: "); pw = getpass.getpass("Password: ")
        if u == ADMIN_USER and pw == ADMIN_PASS: menu_admin()
    elif p == '2':
        menu_pompa()
    elif p == '3': break
