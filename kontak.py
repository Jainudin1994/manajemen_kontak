"berisi kelas kontak untuk menjalankan program kontak "

import dokumen


class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

    def melihat_kontak(self):
        # Melihat Semua Kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("Kontak Masih Kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan Kontak
        nama = input("Masukan nama kontak: ")
        HP = input("Masukan HP kontak: ")
        email = input("Masukan email kontak: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak Baru Berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukan nomor kontak yang dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak yang dimaksud sudah dihapus!")
            except:
                print("keyword yang anda masukan salah!")
    def keluar_kontak(self):
        dokumen.menyimpan_kontak(isi=self.kontak)