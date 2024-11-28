print("Sistem Manajemen Stok Barang Toko")

stokBarang = 100
def kurangiStok(jumlah):
    global stokBarang

    if jumlah > stokBarang:
        print("Stok tidak cukup!")
        return
    else:
        stokBarang -= jumlah
        return stokBarang

while True:
    masukkan = int(input("Masukkan jumlah barang yang ingin dikurangi : "))
    print (f"{masukkan} barang telah terjual. " "Stok total :", kurangiStok (masukkan))
    konfirmasi = input("Apakah Anda ingin melanjutkan transaksi? (ya/tidak) : ")
    if konfirmasi == ("ya"):
        True
    else:
        print("Transaksi selesai. Terima kasih!")
        break