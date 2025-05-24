    #"manajemen kontak"

kontak1 = {"nama" : "Albi", "HP" : "0822905322", "email" : "Albi@gmail.com"}
kontak2 = {"nama" : "Arsyila", "HP" : "0822905323", "email" : "Arsyila@gmail.com"}
kontak = [kontak1, kontak2]

while True:

    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == "1":
        # Melihat Semua Kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
            else:
                print("Kontak Masih Kosong!")

    elif pilihan == "2":
        # Menambahkan Kontak
        nama = input("Masukan nama kontak: ")
        HP = input("Masukan HP kontak: ")
        email = input("Masukan email kontak: ")
        kontak_baru = {"nama" : nama, "HP" : HP, "email" : email}
        kontak.append(kontak_baru)
        print("Kontak Baru Berhasil ditambahkan!")

    elif pilihan == "3":
        # Menghapus Kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
            else:
                print("Kontak Masih Kosong")
                continue

        i_hapus = int(input("Masukan nomor kontak yang dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah dihapus!")
    elif pilihan == "4":
        # Keluar Dari Kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")
