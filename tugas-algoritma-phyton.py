harga_telur = 26000
berat = 5
ongkos = 3500
uang = 200000

total_harga_telur = harga_telur * berat
total_ongkos = ongkos * 2        #pulang pergi
total_biaya = total_harga_telur + total_ongkos
sisa_uang = uang - total_biaya

print(uang)
print(" telur ", berat, "kg ", "harga", total_harga_telur)
print("ongkos ", total_ongkos)
print("sisa uang", sisa_uang)

if sisa_uang <= 0 :
    print("uang tidak cukup")
else :
    print("uang cukup")