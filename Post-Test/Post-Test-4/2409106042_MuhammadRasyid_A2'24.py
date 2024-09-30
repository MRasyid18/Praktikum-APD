print("""
Silahkan login
""")

nama = "rasyid"
NIM = "42"

attempts = 0
while attempts < 3: 
    input_nama = input("Masukkan username(Nama Panggian): ")
    input_NIM= input("Masukkan Password(NIM): ")

    if input_nama== nama and input_NIM == NIM:
        print("Login berhasil")
        nama = input("Masukkan nama: ")
        NIM = input("Masukkan NIM: ")
        jumlah_pinjaman = int(input("Masukkan jumlah pinjaman: "))
        lama_cicilan = int(input("Masukkan lama cicilan dalam tahun: "))

        if lama_cicilan == 1 :
            bunga_perbulan = (0.07/12) * jumlah_pinjaman
            cicilan_perbulan = (jumlah_pinjaman + bunga_perbulan) / 12
        elif lama_cicilan == 2 :
            bunga_perbulan = (0.13/12) * jumlah_pinjaman
            cicilan_perbulan = (jumlah_pinjaman + bunga_perbulan) / 24
        elif lama_cicilan == 3 :
            bunga_perbulan = (0.19/12) * jumlah_pinjaman
            cicilan_perbulan = (jumlah_pinjaman + bunga_perbulan) / 36

        print(f"Nama : {nama}")
        print(f"NIM : {NIM}")
        print(f"Jumlah pinjaman : Rp. {jumlah_pinjaman:,.0f}")
        print(f"Lama cicilan dalam tahun : {lama_cicilan}")
        print(f"total cicilan perbulan : Rp. {cicilan_perbulan:,.0f}")
        menu = int(input("Pilih menu (1. Lanjutkan program/2. Berhentikan program): "))
        if menu == 1:
            pass
        elif menu == 2:
            break

    else : 
        print("Username atau password salah.")
        attempts += 1
    if attempts == 3:
        print("Login Gagal.")
