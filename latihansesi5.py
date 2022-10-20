# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga beserta nama barang

while(True):
    nama_barang = input ('masukan nama barang : ')
    harga_barang = int(input('masukan harga barang : Rp. '))
    persen_harga = input ('masukan persen harga : ')
    Jumlah_yang_dibeli = input ('masukan jumlah barang yang akan dibeli : ')

    harga_keuntungan = int(harga_barang) * int(persen_harga) /100
    harga_jual = int(harga_barang)+harga_keuntungan
    harga_bayar = int(harga_jual) * int( Jumlah_yang_dibeli)
    
    print ('')
    print ( nama_barang, 'Dijual dengan harga : Rp. ' ,harga_jual)
    print ('Dengan modal : Rp.' , harga_barang, '/pcs')
    print ('Dengan keuntungan : Rp.' ,harga_keuntungan, '/pcs')
    print ('')
    print ('jumlah', nama_barang, 'yang di beli : ',Jumlah_yang_dibeli)
    print ('Jumlah Barang Yang Harus Dibayar : RP.' ,harga_bayar)

    

    apakah_lanjut = input ('apakah ingin input barang lain? Y untuk ya dan N untuk no : ')
    if(apakah_lanjut != "Y"):
        break

# modal yang di keluarkan

# laba yang di dapat
# penjualan ke customer