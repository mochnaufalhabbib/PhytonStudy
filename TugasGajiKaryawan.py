
print("PROGRAM HITUNG GAJIH KARYAWAN")
nama = input("masukan nama :")
jabatan = int(input("masukan jabatan :"))
pendidikan = input("masukan pendidikan :")
jam_kerja = int(input("masukan jam Kerja :"))
GajiPokok = 300000
TjnJabatan = 0
TjnPendidikan = 0
HonorLembur = 0
if jabatan == 1:
    tjn_jabatan = 0.05 * GajiPokok
elif jabatan == 2:
    tjn_jabatan = 0.10 * GajiPokok
elif jabatan == 3:
    tjn_jabatan = 0.15 * GajiPokok
else:
    print("Golongan jabatan tidak ada")
if pendidikan == "SMA":
    tjn_pendidikan = 0.025 * GajiPokok
elif pendidikan == "D1":
    tjn_pendidikan = 0.5 * GajiPokok
elif pendidikan == "D3":
    tjn_pendidikan = 0.20 * GajiPokok
elif pendidikan == "S1":
    tjn_pendidikan = 0.30 * GajiPokok
else:
    print("pendidikan tidak ada")
if jam_kerja > 8:
    honor_Lembur = (jam_kerja -8) * 3500
else:
    honor_Lembur = 0
total = GajiPokok + tjn_pendidikan + tjn_jabatan +honor_Lembur
print("==============================")
print("Karyawan yang bernama    :", nama)
print("Honor yang di terima")
print(" Tunjangan jabatan       :", TjnJabatan)
print(" Tunjangan Pendidikan    :", TjnPendidikan)
print(" Honor Lembur            :", HonorLembur)
print("                         -----------------+")
print("                         ", total )
print("==============================")
print("Total Gaji")
print(total)