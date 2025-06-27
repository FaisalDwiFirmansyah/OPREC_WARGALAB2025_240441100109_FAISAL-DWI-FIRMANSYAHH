produk = [
    {
    laptop : 5500000,
    smarthphone : 3000000,
    tablet : 2000000,
    smarthwatch : 1500000,
    headphone : 500000
}

]
nama = input("Masukkan nama anda: ")
umur = int(input("Masukkan umur anda"))
member = input("Apakah anda memiliki kartu member? (ya/tidak)")
produk_dibeli = input("Masukkan Gadget yang ingin dibeli: ")
jumlah_unit = int(input("Masukkan jumlah unit: "))
harga = int(input("Masukkan jumlah harga"))
penawaran = input("Apakah anda ingin melakukan penawaran? (ya/tidak)")

tambah_produk = input("Apakah anda ingin menambah produk? (ya/tidak)")
tambah_produk.append(produk)

total_harga = harga + harga



def cek_penawaran(produk):
    if umur < 17 and harga > 3000000:
        print("Maaf, anda belum cukup umur uuntuk membeli produk ini")


def hitung_diskon(produk):
    if member == ya and total_harga > 10000000:
        diskon : 10%
    elif member == ya and total_harga > 5000000:
        diskon : 5%
    else:
        print("Maaf anda belum mendapatkan diskon")


def menu(produk):

    print("====STRUK PEMBELIAN====\n")
    while True:
    print("Nama Pembeli: {nama}")
    print("Produk dibeli: {produk_dibeli}")
    print("Jumlah Unit: {jumlah_unit}")
    print("Harga/unit: {harga}")
    print("Subtotal: {total_harga}")
    print("Diskon: {diskon}")
    print("Total Akhir: {}")


menu()