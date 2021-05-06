
'MUHAMMAD ARIS SEPTANUGROHO'
'X SIJA 1'

'LATIHAN 7.2 (TUPLE)'

# NOMOR 1
tuple_1 = ('Supriaji', 'Ardi', 'Endri', 'Kustilah')
tuple_2 = list(tuple_1)
tuple_2[3] = 'Aris'
tuple_2 = tuple(tuple_2)
print(f'Isi Tuple 1 = {tuple_1}\nIsi Tuple 2 = {tuple_2}')





# NOMOR 2 
print('Nama saya ada pada index ke- %s'%(tuple_2.index('Aris')))
print(tuple_2*2)

# NOMOR 3
tuple_1 = ('Albert', 'Xiao', 'Deng Lun', 'Kim So Hyun', 'Zhang', 'Zhou', 'Fei', 'Sin Yin')
tuple_2 = []
for i in tuple_1:
    if 'a' not in i.lower():
        tuple_2.append(i)
tuple_2 = tuple(tuple_2)
print('Isi Tuple 1 : {0}\nIsi Tuple 2 : {1}'.format(tuple_1, tuple_2))
