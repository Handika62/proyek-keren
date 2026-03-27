import json
import os
import qrcode

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
        os.system('clear')
        print("=== KELOLA WARGA RW HASBIH ===")
        print("1. Daftar Warga")
        print("2. Tambah Warga (Kirim WA)")
        print("3. Cari NIK/Nama")
        print("4. Tampilkan QR Code")
        print("5. Kembali")
        print("-" * 30)
        
        pilih = input("Pilih: ")
        data = baca_data()
        warga = data.get('warga', [])

        if pilih == '1':
            print("\nDAFTAR WARGA:")
            for i, w in enumerate(warga, 1):
                print(f"{i}. {w['nama']} - {w.get('nik', '-')}")
            input("\nEnter untuk kembali...")

        elif pilih == '2':
            n = input("Nama Lengkap: ")
            ni = input("NIK: ")
            hp = input("WhatsApp (62...): ")
            warga.append({"nama": n, "nik": ni, "hp": hp})
            simpan_data(data)
            
            # Otomatis Buka WhatsApp
            pesan = f"Halo Pak/Bu {n}, Anda telah terdaftar di Sistem RW Hasbih."
            os.system(f"termux-open-url 'https://api.whatsapp.com/send?phone={hp}&text={pesan}'")
            print("\n[SUKSES] Data disimpan & WA dibuka!")
            input("Enter...")

        elif pilih == '3':
            c = input("Cari Nama/NIK: ").lower()
            for w in warga:
                if c in w.get('nama','').lower() or c in w.get('nik',''):
                    print(f"- {w['nama']} ({w['nik']})")
            input("\nEnter...")

        elif pilih == '4':
            ni = input("Masukkan NIK untuk QR: ")
            for w in warga:
                if w.get('nik') == ni:
                    qr = qrcode.QRCode()
                    qr.add_data(f"RW-HASBIH\n{w['nama']}")
                    qr.print_ascii()
            input("\nEnter...")

        elif pilih == '5':
            break
