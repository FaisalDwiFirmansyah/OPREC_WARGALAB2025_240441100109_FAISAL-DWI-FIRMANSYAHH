#Membuat dictionary untuk menampilkan semua gadget yang ada
produk = {
    "laptop" : 5500000,
    "smarthphone" : 3000000,
    "tablet" : 2000000,
    "smarthwatch" : 1500000,
    "headphone" : 500000
}

#Membuat inputan untuk mengetahui identitas serta produk/gadget yang akan dibeli
nama = input("Masukkan nama anda: ")
umur = int(input("Masukkan umur anda"))
produk_dibeli = input("Masukkan Gadget yang ingin dibeli: ")
jumlah_unit = int(input("Masukkan jumlah unit: "))
harga = int(input("Masukkan jumlah harga"))


tambah_produk = input("Apakah anda ingin menambah produk? (ya/tidak)")
tambah_produk.append(produk)

total_harga = harga + harga

# Menggunakan penyeleksian kondisi untuk mengecek apakah pembeli usianya diatas atau dibawah 17 tahun, dimana jika dibawah 17 tahun maka tidak akan bisa membeli gadget yang harganya ditas 3jt
if umur < 17 and harga > 3000000:
     print("Maaf, anda belum cukup umur uuntuk membeli produk ini")
else:
    

#Membuat fungsi untuk mengecek apakah pembeli ingin melakukan penawaran atau tidak
def cek_penawaran(produk):
    penawaran = input("Apakah anda ingin melakukan penawaran? (ya/tidak)")

#Membuat penyeleksian kondisi untuk mengecek apakah pembeli ingin melakukan penawaran dan jika penawaran tidak kurang dari 80& dari harga asli
    if penawaran == "ya" and harga >= 80%:
        print("Penawaran anda diterima")
    else:
        print("Penawaran ditolak. Harga asli digunakan")


# Memebuat fungsi untuk menghitung total diskon
def hitung_diskon(produk):
    member = input("Apakah anda memiliki kartu member? (ya/tidak)")
#Membuat penyeleksian kondisi dimana jika memiliki kartu member akan mendapatkan diskon, tetapi dengan total pembelian memenuhi syarat
    if member == "ya" and total_harga > 10000000:
        diskon : 10%
    elif member == "ya" and total_harga > 5000000:
        diskon : 5%
    else:
        print("Maaf anda belum mendapatkan diskon")

#Menggunakan operator aritmatika untuk menghitung total harga setelah diskon
total_setelah_diskon = harga - diskon



def transaksi(produk):

    print("====STRUK PEMBELIAN====\n")
    while True:
    print("Nama Pembeli: {nama}")
    print("Produk dibeli: {produk_dibeli}")
    print("Jumlah Unit: {jumlah_unit}")
    print("Harga/unit: {harga}")
    print("Subtotal: {total_harga}")
    print("Diskon: {diskon}")
    print("Total Akhir: {total_setelah_diskon}")






transaksi()    
