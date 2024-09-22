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
print(f"Jumlah pinjaman : {jumlah_pinjaman}")
print(f"Lama cicilan dalam tahun : {lama_cicilan}")
print(f"total cicilan perbulan : {cicilan_perbulan}")

