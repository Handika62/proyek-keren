import os
import getpass
import time
import sys
import fungsi_rw
import keuangan

def animasi_teks(teks):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def tampilkan_logo():
    os.system('clear')
    # Logo Baru: RUKUN WARGA (RW)
    logo = """
    =============================================
     _____  _    _ _  ___    _ _   _  __          __ _    _____   _____          
    |  __ \| |  | | |/ / |  | | \ | | \ \        / // \  |  __ \ / ____|   /\    
    | |__) | |  | | ' /| |  | |  \| |  \ \  /\  / // _ \ | |__) | |  __   /  \   
    |  _  /| |  | |  < | |  | | . ` |   \ \/  \/ // ___ \|  _  /| | |_ | / /\ \  
    | | \ \| |__| | . \| |__| | |\  |    \  /\  // _/   \_| | \ \| |__| |/ ____ \ 
    |_|  \_\\\\____/|_|\_\\\\____/|_| \_|     \/  \//_/     \_|_|  \_\\\\_____/_/    \_\
                                                                                 
    =============================================
       SISTEM DIGITALISASI RUKUN WARGA (RW)
    =============================================
    """
    print(logo)
    animasi_teks(" >>> Menginisialisasi sistem... [OK]")
    animasi_teks(" >>> Menghubungkan database warga... [OK]")
    time.sleep(0.5)

def menu_pompa():
    while True:
        os.system('clear')
        print("=== UNIT: SOLUSI POMPA AIR ===")
        print("1. SOP Perbaikan\n2. Harga Jasa\n3. Kembali")
        p = input("\nPilih: ")
        if p == '1':
            print("\nSOP: Cek Arus -> Cek Kapasitor -> Cek Otomatis.")
            input("\nEnter...")
        elif p == '2':
            print("\nEstimasi: Jasa Rp 75rb - Gulung Dinamo Rp 350rb+.")
            input("\nEnter...")
        elif p == '3': break

# --- PROGRAM UTAMA ---
tampilkan_logo()

while True:
    print("\n[ MENU UTAMA RUKUN WARGA ]")
    print("1. Administrasi RW")
    print("2. Solusi Pompa Air")
    print("3. Catatan Keuangan")
    print("4. Keluar")
    pilih = input("\nPilih Menu (1-4): ")

    if pilih == '1':
        print("\n--- KEAMANAN SISTEM ---")
        u = input("User Admin: ")
        pw = getpass.getpass("Password  : ")
        if u == "admin" and pw == "12345": # Username saya ganti ke 'admin' agar umum
            fungsi_rw.menu_admin()
        else:
            print("\n[!] Login Gagal! Akses Ditolak."); time.sleep(1)
    elif pilih == '2':
        menu_pompa()
    elif pilih == '3':
        keuangan.menu_keuangan()
    elif pilih == '4':
        print("\nTerima kasih, Pak Handika. Sampai jumpa!"); break
    
    os.system('clear')
