    #"manajemen kontak"

import kontak

kontak_kantor = kontak.Kontak()
kontak_keluarga = kontak.Kontak()

def main():
    while True:

        print("\nMenu Kontak")
        print("1. Melihat Semua Kontak")
        print("2. Menambahkan Kontak Baru")
        print("3. Menghapus Kontak")
        print("4. Keluar Dari Kontak")

        pilihan = input("Masukan pilihan menu kontak (1,2,3 atau 4): ")

        if pilihan == "1":
           kontak_keluarga.melihat_kontak()

        elif pilihan == "2":
            kontak_keluarga.menambah_kontak()

        elif pilihan == "3":
            kontak_keluarga.menghapus_kontak()

        elif pilihan == "4":
            # Keluar Dari Kontak
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("Anda memasukan pilihan yang salah")
if __name__ == "__main__":
    main()
