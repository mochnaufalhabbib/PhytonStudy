angka=int(input('nilai a:'))
if 5 > 0:
    print(angka,"adalah bilangan positif")
else :
    print(angka,"adalah bilangan negatif")

#Tiket_Bus
print ("                    PENJUALAN TIKET BUS                 ")
print ("                            XYZ                         ")
print ("                 *************************              ")
(input('Nama Pembeli:'))
(input('No Handphone:'))
(input('Jurusan:'))
(input('Jumlah Beli:'))

#Harga_Tiket
customer=input('nama customer:')
no_handphone=input('no_handphone:')
jurusan=input('jurusan [SBY/BL/LMP]:')
if jurusan=="SBY":
    namajurusan="Surabaya"
    harga=300000
elif jurusan=="BL":
    namajurusan="Bali"
    harga=350000
else :
    namajurusan="Lampung"
    harga=500000
jumlah=int(input("Masukan jumlah beli"))
if jumlah>=3 :
    potongan=(jumlah*harga)*0.1
else:
    potongan=0
total=(jumlah*harga)-potongan
print("-----------------------------------")
print("       PENJUALAN TIKET BUS")
print("               XYZ")
print("-----------------------------------")
print("Nama Pembeli : "+str(customer))
print("No Handphone : "+str(no_handphone))
print("Kode Jurusan Yang Dipilih : "+str(jurusan))
print("Nama Kota Tujuan : "+str(namajurusan))
print("Harga : ",(harga))
print("Jumlah Beli : ",(jumlah))
print("-----------------------------------")
print("Potongan yang didapat: ",+(potongan))
print("total bayar: ",+(total))
uangbayar=int(input("masukan uang bayar : "))
uangkembali=uangbayar-total
print("uang kembali : ",+uangkembali)