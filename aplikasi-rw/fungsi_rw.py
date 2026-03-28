import json
import os
import qrcode

def baca_data():
    try:
        with open('data_warga.json', 'r') as f:
            return json.load(f)
    except:
        return {"warga": []}

# FUNGSI BARU: Membaca data keuangan
def baca_keuangan():
    try:
        with open('data_keuangan.json', 'r') as f:
            return json.load(f)
    except:
        return {"saldo": 0, "transaksi": []}

def simpan_data(data):
    with open('data_warga.json', 'w') as f:
        json.dump(data, f, indent=4)

def menu_admin():
    while True:
        os.system('clear')
        # Menampilkan ringkasan saldo di header
        keuangan = baca_keuangan()
        saldo_skrg = keuangan.get('saldo', 0)
        
        print("=== KELOLA WARGA RUKUN WARGA ===")
        print(f"Saldo Kas Saat Ini: Rp {saldo_skrg:,}")
        print("-" * 30)
        print("1. Daftar Warga")
        print("2. Tambah Warga (Kirim WA)")
        print("3. Cari NIK/Nama")
        print("4. Tampilkan QR Code")
        print("5. Laporan Kas Keuangan") # MENU BARU
        print("6. Kembali")
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

            pesan = f"Halo Pak/Bu {n}, Anda telah terdaftar di Sistem RW-HASBIH."
            os.system(f"termux-open-url 'https://api.whatsapp.com/send?phone={hp}&text={pesan}'")
            print("\n[SUKSES] Data disimpan & WA dibuka!")
            input("Enter...")

        elif pilih == '3':
            c = input("Cari Nama/NIK: ").lower()
            found = False
            for w in warga:
                if c in w.get('nama','').lower() or c in w.get('nik',''):
                    print(f"- {w['nama']} ({w['nik']})")
                    found = True
            if not found: print("Data tidak ditemukan.")
            input("\nEnter...")

        elif pilih == '4':
            ni = input("Masukkan NIK untuk QR: ")
            for w in warga:
                if w.get('nik') == ni:
                    qr = qrcode.QRCode()
                    qr.add_data(f"RW-HASBIH\n{w['nama']}\nNIK:{w['nik']}")
                    qr.print_ascii()
            input("\nEnter...")

        # LOGIKA BARU: Menampilkan rincian transaksi
        elif pilih == '5':
            print("\n--- LAPORAN TRANSAKSI TERAKHIR ---")
            transaksi = keuangan.get('transaksi', [])
            if not transaksi:
                print("Belum ada catatan transaksi.")
            for t in transaksi:
                print(f"[{t['tanggal']}] {t['ket']}: Rp {t['jumlah']:,}")
            input("\nEnter untuk kembali...")

        elif pilih == '6':
            break
