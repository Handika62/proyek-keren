import json
import os

def baca_keuangan():
    try:
        with open('data_keuangan.json', 'r') as f:
            return json.load(f)
    except:
        return {"transaksi": []}

def simpan_keuangan(data):
    with open('data_keuangan.json', 'w') as f:
        json.dump(data, f, indent=4)

def menu_keuangan():
    while True:
        os.system('clear')
        print("=== CATATAN KEUANGAN HASBIH ===")
        print("1. Catat Pemasukan/Pengeluaran")
        print("2. Lihat Laporan Keuangan")
        print("3. Kembali")
        pilih = input("\nPilih: ")
        data = baca_keuangan(); trans = data['transaksi']

        if pilih == '1':
            ket = input("Keterangan (misal: Service Pompa): ")
            jml = int(input("Jumlah (Rp): "))
            tipe = input("Tipe (Masuk/Keluar): ").capitalize()
            trans.append({"ket": ket, "jml": jml, "tipe": tipe})
            simpan_keuangan(data)
            input("\n[BERHASIL] Catatan disimpan!")
        elif pilih == '2':
            total = 0
            print("\nDAFTAR TRANSAKSI:")
            for t in trans:
                print(f"- {t['ket']}: Rp {t['jml']} ({t['tipe']})")
                if t['tipe'] == "Masuk": total += t['jml']
                else: total -= t['jml']
            print("-" * 30)
            print(f"SALDO AKHIR: Rp {total}")
            input("\nEnter...")
        elif pilih == '3': break
