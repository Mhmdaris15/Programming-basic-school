"Muhammad Aris Septanugroho"
"X SIJA 1"
"Pemrograman Dasar"

# NOMOR 1 
month = "Januari Februari Maret April Mei Juni Juli Agustus September Oktober November Desember"
month = month.split(" ")
print(f"{month} \nSekarang Bulan {month[5]}")

# NOMOR 2
drive = []
for i in range(5):
    temp = int(input("Masukkan angka : "))
    drive.append(temp)
print("Isi List :", drive)

# NOMOR 3
drive2 = []
for j in range(0,10):
    if j % 4 == 0:
        continue
    else:
        drive2.append(j)
drive2.reverse()
print(drive2)