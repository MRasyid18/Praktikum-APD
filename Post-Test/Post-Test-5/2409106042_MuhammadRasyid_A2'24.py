people = [[1, 'rasyid', 'gg', 'ibu kos'], [2, 'ID', 'password', 'penghuni']]

create = [[1, 'Kamar berAC', 1500000], [2, 'Kamar biasa', 1000000], [3, 'Tambahan Kasur', 50000]]

while True:
    print( 
"""
===========================
|    KOST PUTRA RASYID    |
===========================
|    1. Login             |           
|    2. Register          |          
|    3. Keluar            |
===========================
"""
)
    pilihan = input("Pilih Menu: ")
    
    if pilihan == '1':
        print(" SILAHKAN LOGIN \nSilahkan Masukkan Nama dan Password")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        ID = None
        for i in people:
            if i[1] == username and i[2] == password:
                ID = i
                break

        if ID:
            print(f"Login berhasil sebagai {ID[1]}, {ID[3]})")
            if ID[3].lower() == 'ibu kos':

                while True:
                    print(
                    """
                    ===========================
                    |    Menu Ibu Kos        |
                    ===========================
                    |    1. Lihat Kamar      |
                    |    2. Tambah Kamar     |
                    |    3. Hapus Kamar      |
                    |    4. Lihat Penghuni   |
                    |    5. Tambah Penghuni  |
                    |    6. Hapus Penghuni   |
                    |    7. Keluar           |
                    ===========================
                    """
                    )
                    menu_ibu_kos = input("Pilih Menu: ")

                    if menu_ibu_kos == '1':  
                        print("Kamar yang Tersedia:")
                        for kamar in create:
                            print(f"ID: {kamar[0]}, Nama: {kamar[1]}, Harga: Rp{kamar[2]}")

                    elif menu_ibu_kos == '2':  
                        new_id = len(create) + 1
                        nama_kamar = input("Masukkan nama kamar: ")
                        harga_kamar = int(input("Masukkan harga kamar: "))
                        create.append([new_id, nama_kamar, harga_kamar])
                        print("Kamar berhasil ditambahkan!")

                    elif menu_ibu_kos == '3': 
                        id_kamar = int(input("Masukkan ID kamar yang ingin dihapus: "))
                        for kamar in create:
                            if kamar[0] == id_kamar:
                                create.remove(kamar)
                                print(f"Kamar {kamar[1]} berhasil dihapus.")
                                break
                        else:
                            print("ID kamar tidak ditemukan.")

                    elif menu_ibu_kos == '4':  
                        print("Data Penghuni:")
                        for person in people:
                            print(f"ID: {person[0]}, Nama: {person[1]}, Status: {person[3]}")

                    elif menu_ibu_kos == '5':  
                        new_id = len(people) + 1
                        new_username = input("Masukkan username: ")
                        new_password = input("Masukkan password: ")
                        new_status = input("Masukkan status (ibu kos/penghuni): ")
                        people.append([new_id, new_username, new_password, new_status])
                        print("Penghuni berhasil ditambahkan!")

                    elif menu_ibu_kos == '6':  
                        id_penghuni = int(input("Masukkan ID penghuni yang ingin dihapus: "))
                        for person in people:
                            if person[0] == id_penghuni:
                                people.remove(person)
                                print(f"Penghuni {person[1]} berhasil dihapus.")
                                break
                        else:
                            print("ID penghuni tidak ditemukan.")

                    elif menu_ibu_kos == '7': 
                        print("Keluar dari menu ibu kos.")
                        break

                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")

            elif ID[3].lower() == 'penghuni':
                while True:
                    print(
                    """
                    =====================================
                    |    Menu Penghuni                  |
                    =====================================
                    |    1. Lihat Kamar                 |
                    |    2. Pesan Kamar                 |
                    |    (ID = 1 untuk kamar ber ac,    |
                    |    ID = 2 untuk kamar biasa       |
                    |    ID = 3 untuk menambahkan kasur)|
                    |    3. Keluar                      |
                    =====================================
                    """
                    )
                    menu_penghuni = input("Pilih Menu: ")

                    if menu_penghuni == '1':
                        print("Kamar yang Tersedia:")
                        for kamar in create:
                            print(f"ID: {kamar[0]}, Nama: {kamar[1]}, Harga: Rp{kamar[2]}")

                    elif menu_penghuni == '2':
                        id_kamar = int(input("Masukkan ID kamar yang ingin dipesan: "))
                        for kamar in create:
                            if kamar[0] == id_kamar:
                                print(f"Kamar {kamar[1]} berhasil dipesan!")
                                break
                        else:
                            print("ID kamar tidak ditemukan.")

                    elif menu_penghuni == '3':
                        print("Keluar dari menu penghuni.")
                        break

                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")

        else:
            print("Login gagal! Username atau password salah.")

    elif pilihan == '2':  
        print(" SILAHKAN REGISTER \nSilahkan Masukkan Nama, Password, dan Status")
        new_username = input("Masukkan username: ")
        new_password = input("Masukkan password: ")
        new_status = input("Masukkan status (ibu kos/penghuni): ")
        
        new_id = len(people) + 1
        people.append([new_id, new_username, new_password, new_status])
        print("Register berhasil! Silakan login.")

    elif pilihan == '3':  
        print("Terima kasih! Sampai jumpa.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
