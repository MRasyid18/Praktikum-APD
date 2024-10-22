data_login = {
    1: {'username': 'rasyid', 'password': 'gg', 'status': 'ibu kos'},
    2: {'username': 'ID', 'password': 'password', 'status': 'ibu kos/penghuni'}
}

data_fasilitas = {
    1: {'fasilitas': 'kamar berAC', 'harga': 1500000},
    2: {'fasilitas': 'kamar biasa', 'harga': 1000000},
    3: {'fasilitas': 'tambah kasur', 'harga': 50000}
}

def fitur_pendaftaran():
    print(
        """
===========================
|    KOST PUTRA RASYID    |
===========================
|    1. Register          |
|    2. Login             |
|    3. Keluar            |
===========================
"""
    )

def register():
    print("SILAHKAN REGISTER \nMasukkan nama, password, dan status.")
    new_username = input("Masukkan username: ")
    new_password = input("Masukkan password: ")
    new_status = input("Masukkan status (ibu kos/penghuni): ")
    
    new_id = len(data_login) + 1
    data_login[new_id] = {'username': new_username, 'password': new_password, 'status': new_status}
    print("Register berhasil! Silakan login.")

def login():
    print("Silahkan Login \nMasukkan nama dan password.")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    for i in data_login:
        if data_login[i]['username'] == username and data_login[i]['password'] == password:
            print(f"Login berhasil sebagai {data_login[i]['username']}, Status: {data_login[i]['status']}")
            setting_menu_status(data_login[i]['status'].lower(), i)
            return
    print("Login gagal! Username atau password salah.")

def setting_menu_status(status, user_id):
    if status == 'ibu kos':
        setting_ibu_kos_menu()
    elif status == 'penghuni':
        setting_penghuni_menu()

def setting_ibu_kos_menu():
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
            for kamar_id, kamar in data_fasilitas.items():
                print(f"ID: {kamar_id}, Nama: {kamar['fasilitas']}, Harga: Rp{kamar['harga']}")


        elif menu_ibu_kos == '2':
            new_id = len(data_fasilitas) + 1
            nama_kamar = input("Masukkan nama kamar: ")
            harga_kamar = int(input("Masukkan harga kamar: "))
            data_fasilitas[new_id] = {'fasilitas': nama_kamar, 'harga': harga_kamar}
            print("Kamar berhasil ditambahkan.")


        elif menu_ibu_kos == '3':
            id_kamar = int(input("Masukkan ID kamar yang ingin dihapus: "))
            if id_kamar in data_fasilitas:
                kamar = data_fasilitas.pop(id_kamar)
                print(f"Kamar {kamar['fasilitas']} berhasil dihapus.")
            else:
                print("Fasilitas tidak ditemukan.")


        elif menu_ibu_kos == '4':
            print("Data penghuni:")
            for peng_id, penghuni in data_login.items():
                print(f"ID: {peng_id}, Nama: {penghuni['username']}, Status: {penghuni['status']}")


        elif menu_ibu_kos == '5':
            register()


        elif menu_ibu_kos == '6':
            id_penghuni = int(input("Masukkan ID penghuni yang ingin dihapus: "))
            if id_penghuni in data_login:
                penghuni = data_login.pop(id_penghuni)
                print(f"Penghuni {penghuni['username']} berhasil dihapus.")
            else:
                print("ID penghuni tidak ditemukan.")


        elif menu_ibu_kos == '7':
            print("Keluar dari menu ibu kos.")
            break

def setting_penghuni_menu():
    while True:
        print(
            """
            =====================================
            |    Menu Penghuni                  |
            =====================================
            |    1. Lihat Kamar                 |
            |    2. Pesan Kamar                 |
            |    3. Keluar                      |
            =====================================
            """
        )
        menu_penghuni = input("Pilih Menu: ")

        if menu_penghuni == '1':
            print("Kamar yang Tersedia:")
            for kamar_id, kamar in data_fasilitas.items():
                print(f"ID: {kamar_id}, Nama: {kamar['fasilitas']}, Harga: Rp{kamar['harga']}")


        elif menu_penghuni == '2':
            id_kamar = int(input("Masukkan ID kamar yang ingin dipesan: "))
            if id_kamar in data_fasilitas:
                print(f"Kamar {data_fasilitas[id_kamar]['fasilitas']} berhasil dipesan!")
            else:
                print("ID kamar tidak ditemukan.")

                
        elif menu_penghuni == '3':
            print("Keluar dari menu penghuni.")
            break

def pilihan():
    while True:
        fitur_pendaftaran()
        pilihan = input("Pilih Menu: ")

        if pilihan == '1':
            register()
        elif pilihan == '2':
            login()
        elif pilihan == '3':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

pilihan()
