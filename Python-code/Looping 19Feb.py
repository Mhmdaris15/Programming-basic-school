# Buatlah program untuk mengulang menampilkan teks TKJ dengan jumlah 
# pengulangan sesuai yang diinputkan oleh user. 

'Muhammad Aris Septanugroho'
'X SIJA 1'

n = int(input('Masukkan Jumlah Pengulangan : '))
for i in range(1,n+1):
    for j in 'TKJ':
        print(i, j)

# Buatlah program pengulangan bersarang yang menggunakan 3 variabel seperti di
# bawah ini. Variabel pertama merupakan pengulangan angka dari 1 s.d. Variabel kedua
# merupakan huruf A dan B. Variabel ketiga merupakan huruf C dan D. 

Sum = int(input('Masukkan Jumlah Perulangan : '))
for i in range(1, Sum + 1):
    for j in 'AB':
        for k in 'CD':
            print(i, '-', j, '-', k)

# Buatlah program ATM untuk memasukkan pin dengan benar. Program akan terus
# berulang untuk meminta pin hingga user memasukkan pin dengan benar.
# Keterangan: yang diinputkan adalah pin, output yang dihasilkan adalah keterangan
# apakah pin benar atau salah. 

True_Pin = 907050
while True:
    Pin = int(input('Masukkan Pin Anda : '))
    if Pin == True_Pin:
        print('Pin Benar\nTerimakasih telah menggunakan ATM kami')
        break
    print('Pin Salah')