#STUDI KASUS 4(DATA BUKU) MATERI DICTIONARY

#Buat dictionary (key:value) untuk menyimpan data buku (judul, penulis, tahun terbit)
buku = {
    "judul" : "Hacker Sejati",
    "penulis" : "Asta",
    "tahun_terbit" : 2026,
}

#Untuk menampilkan menu yang mau dilakukan oleh user
print("========== Data Buku ==========")
print("------------- Menu ------------ ")
print("1. Tampilkan Data Buku")
print("2. Tambahkan Data Penerbit ke Dictionary")
print("3. Ubah data penulis di Dictionary")
print("4. Hapus data penerbit dari Dictionary")
print("5. Keluar")
print("")

#Program perulangan untuk menampilkan menu dan melakukan perintah sesuai pilihan user
while True:

    #User menginput pilihan menu yang mau dilakukan
    pilihan = int(input("Masukkan nomor menu yang ingin dilakukan 1/2/3/4/5: "))

    #Conditional statement if, elif, else untuk mengeksekusi perintah sesuai pilihan user
    #Menu 1 untuk meanmpilkan data buku saat ini
    if pilihan == 1:
        print("Data Buku Saat ini:")

        #Nested if untuk mengecek apakah key "penerbit" sudah ada di dictionary buku atau belum
        if "penerbit" in buku:
            print(buku["judul"], "ditulis oleh", buku["penulis"], "dan diterbitkan pada tahun", buku["tahun_terbit"], "oleh penerbit", buku["penerbit"])
        else:
            print(buku["judul"], "ditulis oleh", buku["penulis"], "dan diterbitkan pada tahun", buku["tahun_terbit"])
        print("")

    #Menu 2 untuk menambahkan data penerbit ke dictionary buku
    elif pilihan == 2:
        penerbit = input("Masukkan nama penerbit buku: ")
        buku["penerbit"] = penerbit #Menambahkan key "penerbit" dan value penerbit ke dictionary buku
        print("Data penerbit berhasil ditambahkan ke Dictionary.")
        print("")

    #Menu 3 untuk mengubah data penulis di dictionary buku
    elif pilihan == 3:
        penulis = input("Masukkan nama penulis baru: ")
        buku["penulis"] = penulis #Mengubah value dari key "penulis" di dictionary buku
        print("Data penulis di Dictionary berhasil diubah.")
        print("")

    #Menu 4 untuk menghapus data penerbit dari dictionary buku
    elif pilihan == 4:
        penerbit = input("Apakah anda ingin menghapus data penerbit? (Ya/Tidak): ")
        if penerbit == "Ya":
            del buku["penerbit"] #Disini saya pakai perintah del untuk menghapus key "penerbit" dan value nya dari dictionary buku
            print("Data penerbit berhasil dihapus dari Dictionary.")
            print("")
        else:
            print("Penghapusan data penerbit dibatalkan.")
            print("")

    #Menu 5 untuk keluar dari program
    elif pilihan == 5:
        print("Anda telah keluar dari program.")
        print("")
        print("Data buku saat ini setelah dilakukan perubahan:")

        #Nested if untuk mengecek apakah key "penerbit" sudah ada di dictionary buku atau belum (sama kayak di menu 1)
        if "penerbit" in buku:
            print(buku["judul"], "ditulis oleh", buku["penulis"], "dan diterbitkan pada tahun", buku["tahun_terbit"], "oleh penerbit", buku["penerbit"])
        else:
            print(buku["judul"], "ditulis oleh", buku["penulis"], "dan diterbitkan pada tahun", buku["tahun_terbit"])
        break

    else:
        print("Pilihan menu tidak tersedia. Silahkan masukkan nomor menu yang benar yap.")




