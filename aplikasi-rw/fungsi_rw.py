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
        print("1. Daftar Warga\n2. Tambah Warga\n3. Cari NIK\n4. QR Code\n5. Kembali")
        pilih = input("Pilih: ")
        data = baca_data(); warga = data.get('warga', [])

        if pilih == '1':
            for i, w in enumerate(warga, 1):
                print(f"{i}. {w['nama']} - {w.get('nik')}")
            input("\nEnter...")
        elif pilih == '2':
            n = input("Nama: "); ni = input("NIK: "); k = input("KK: ")
            warga.append({"nama": n, "nik": ni, "no_kk": k})
            simpan_data(data); input("Simpan Berhasil!")
        elif pilih == '3':
            c = input("Cari: ").lower()
            for w in warga:
                if c in w['nama'].lower() or c in w['nik']: print(f"- {w['nama']} ({w['nik']})")
            input("\nEnter...")
        elif pilih == '4':
            ni = input("NIK: ")
            for w in warga:
                if w['nik'] == ni:
                    qr = qrcode.QRCode(); qr.add_data(f"RW-HASBIH\n{w['nama']}"); qr.print_ascii()
            input("\nEnter...")
        elif pilih == '5': break
