print('Pembelian tiket pesawat dari Bandara Soekarno-Hatta Tanggal 20 Desember 2020 Kelas Ekonomi')
jumlah_penumpang = int(input('Masukkan Jumlah Penumpang : '))
tujuan = input('Pilih Lokasi Tujuan : \nSingapura \nTokyo \nYogyakarta \n>> ')

if tujuan == 'Singapura':
    maskapai = input('Pilih maskapai Penerbangan : \nGaruda Indonesia \nLion Air \n>>')
    if maskapai == 'Garuda Indonesia':
        harga_tiket = 2500000 * jumlah_penumpang
        print('Total Harga Tiket : Rp' + str(harga_tiket) + ',-')
    elif maskapai == 'Lion Air':
        harga_tiket = 1500000 * jumlah_penumpang
        print('Total Harga Tiket : Rp' + str(harga_tiket) + ',-')
    else:
        print('Pilihan tidak tersedia, masukkan input sesuai option!')
elif tujuan == 'Tokyo':
    maskapai = input('Pilih maskapai Penerbangan : \nJapan Airlines \nAll Nippon Airways \n>>')
    if maskapai == 'Japan Airlines':
        harga_tiket = 12400000 * jumlah_penumpang
        print('Total Harga Tiket : Rp' + str(harga_tiket) + ',-')
    elif maskapai == 'All Nippon Airways':
        harga_tiket = 29000000 * jumlah_penumpang
        print('Total Harga Tiket : Rp' + str(harga_tiket) + ',-')
    else:
        print('Pilihan tidak tersedia, masukkan input sesuai option!')
elif tujuan == 'Yogyakarta':
    maskapai = input('Pilih maskapai Penerbangan : \nCitilink \nWings Air \n>>')
    if maskapai == 'Citilink':
        harga_tiket = 605000 * jumlah_penumpang
        print('Total Harga Tiket : Rp' + str(harga_tiket) + ',-')
    elif maskapai == 'Wings Air':
        harga_tiket = 1800000 * jumlah_penumpang
        print('Total Harga Tiket : Rp' + str(harga_tiket) + ',-')
    else:
        print('Pilihan tidak tersedia, masukkan input sesuai option!')
else:
    print('Pilihan tidak tersedia, masukkan input sesuai option')