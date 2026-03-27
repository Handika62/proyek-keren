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

def menu_admin():
    while True:
        tampilkan_header("HALAMAN ADMIN - KELOLA WARGA")
        print("1. Lihat Daftar Seluruh Warga")
        print("2. Form Pendaftaran Warga Baru")
        print("3. Cari Warga (Nama/NIK)")
        print("4. Tampilkan QR Code Warga")
        print("5. Logout & Kembali")
        print("-" * 40)
        
        pilih = input("Pilih Menu (1-5): ")
        data = baca_data()
        warga = data.get('warga', [])

        if pilih == '1':
            print("\nDATA WARGA TERDAFTAR:")
            for i, w in enumerate(warga, 1):
                print(f"{i}. {w['nama']} | NIK: {w.get('nik', '-')}")
            input("\nTekan Enter...")

        elif pilih == '2':
            print("\n--- FORM PENDAFTARAN ---")
            nama = input("Nama Lengkap: ")
            nik = input("NIK: ")
            kk = input("No KK: ")
            blok = input("Blok: ")
            warga.append({"nama": nama, "nik": nik, "no_kk": kk, "blok": blok})
            simpan_data(data)
            print("\n[SUKSES] Data disimpan!"); input("Enter...")

        elif pilih == '3':
            cari = input("\nMasukkan Nama atau NIK: ").lower()
            hasil = [w for w in warga if cari in w.get('nama', '').lower() or cari in w.get('nik', '')]
            print("\nHASIL PENCARIAN:")
            for h in hasil:
                print(f"- {h['nama']} | NIK: {h.get('nik')} | Blok: {h.get('blok')}")
            if not hasil: print("Data tidak ditemukan.")
            input("\nTekan Enter...")

        elif pilih == '4':
            print("\n--- TAMPILKAN QR CODE ---")
            nik_qr = input("Masukkan NIK warga: ")
            warga_pilih = [w for w in warga if w.get('nik') == nik_qr]
            
            if warga_pilih:
                w = warga_pilih[0]
                print(f"\nMenyiapkan QR Code untuk: {w['nama']}...")
                qr = qrcode.QRCode()
                qr.add_data(f"RW-HASBIH\nNama: {w['nama']}\nNIK: {w['nik']}\nBlok: {w['blok']}")
                # Menampilkan QR Code di terminal
                qr.print_ascii() 
            else:
                print("\n[!] NIK tidak ditemukan.")
            input("\nTekan Enter untuk kembali...")

        elif pilih == '5': break

# --- Main Program ---
while True:
    tampilkan_header("SISTEM DIGITAL RW HASBIH")
    print("1. Akses Menu Admin\n2. Keluar")
    p = input("\nPilih (1-2): ")
    if p == '1':
        tampilkan_header("LOGIN ADMIN")
        u = input("Username: ")
        pw = getpass.getpass("Password: ")
        if u == ADMIN_USER and pw == ADMIN_PASS:
            menu_admin()
        else:
            print("\n[!] Login Gagal!"); input("Enter...")
    elif p == '2': break
