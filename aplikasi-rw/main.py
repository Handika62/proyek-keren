import os
import getpass
import fungsi_rw
import keuangan # TAMBAHKAN INI

def menu_pompa():
    # ... (kode pompa air tetap sama seperti sebelumnya) ...
    pass

while True:
    os.system('clear')
    print("===============================")
    print("   SISTEM DIGITAL HASBIH       ")
    print("===============================")
    print("1. Administrasi RW")
    print("2. Solusi Pompa Air")
    print("3. Catatan Keuangan") # MENU BARU
    print("4. Keluar")
    pilih = input("\nPilih Menu: ")

    if pilih == '1':
        u = input("User: "); pw = getpass.getpass("Pass: ")
        if u == "hasbih" and pw == "12345":
            fungsi_rw.menu_admin()
    elif pilih == '2':
        # (panggil fungsi menu_pompa di sini)
        pass 
    elif pilih == '3':
        keuangan.menu_keuangan() # MEMANGGIL FILE KEUANGAN
    elif pilih == '4': break
