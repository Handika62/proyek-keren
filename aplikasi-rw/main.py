import os
import getpass
import fungsi_rw # Memanggil file fungsi_rw.py tadi

def menu_pompa():
    while True:
        os.system('clear')
        print("=== UNIT: SOLUSI POMPA AIR ===")
        print("1. SOP Perbaikan\n2. Harga Jasa\n3. Kembali")
        p = input("Pilih: ")
        if p == '1':
            print("\nSOP: Cek Stroom -> Cek Kapasitor -> Cek Otomatis.")
            input("\nEnter...")
        elif p == '2':
            print("\nJasa: Rp 75rb (Ringan), Rp 350rb+ (Gulung Dinamo).")
            input("\nEnter...")
        elif p == '3': break

while True:
    os.system('clear')
    print("===============================")
    print("   SISTEM DIGITAL HASBIH       ")
    print("===============================")
    print("1. Administrasi RW\n2. Solusi Pompa Air\n3. Keluar")
    pilih = input("Pilih Menu: ")

    if pilih == '1':
        u = input("User: "); pw = getpass.getpass("Pass: ")
        if u == "hasbih" and pw == "12345":
            fungsi_rw.menu_admin() # Memanggil fungsi dari file sebelah
    elif pilih == '2':
        menu_pompa()
    elif pilih == '3': break
