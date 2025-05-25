    #"manajemen kontak"

class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # Melihat Semua Kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak Masih Kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan Kontak
        nama = input("Masukan nama kontak: ")
        HP = input("Masukan HP kontak: ")
        email = input("Masukan email kontak: ")
        kontak_baru = {"nama": nama, "HP": HP, "email": email}
        self.kontak.append(kontak_baru)
        print("Kontak Baru Berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukan nomor kontak yang dihapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak yang dimaksud sudah dihapus!")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:

    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == "1":
       kontak_kantor.melihat_kontak()

    elif pilihan == "2":
        kontak_kantor.menambah_kontak()

    elif pilihan == "3":
        kontak_kantor.menghapus_kontak()

    elif pilihan == "4":
        # Keluar Dari Kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")
