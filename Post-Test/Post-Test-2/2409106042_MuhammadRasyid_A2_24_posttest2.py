nama = input("Masukkan nama =")
Nim = input("Masukkan NIM =")
Harga = int(input("Masukkan Harga beras ="))

Diskon = {
    "Diskon_mawar" : 11/100,
    "Diskon_sania" : 14/100,
    "Diskon_maknyus" : 17/100
}

Diskon_mawar = Harga * Diskon["Diskon_mawar"]
Diskon_sania = Harga * Diskon["Diskon_sania"]
Diskon_maknyus = Harga * Diskon["Diskon_maknyus"]

mawar = Harga - Diskon_mawar
sania = Harga - Diskon_sania
maknyus = Harga - Diskon_maknyus

print(f"{nama} dengan nim {Nim} ingin membeli beras seharga {Harga}")
print(f"Jika dia membeli beras Mawar ia harus membayar {mawar}  Setelah mendapat diskon 11%")
print(f"Jika dia membeli beras sania ia harus membayar {sania} setelah mendapat diskon 14%")
print(f"Jika dia membeli beras maknyus ia harus membayar {maknyus} setelah mendapat diskon 17%")