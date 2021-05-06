print('''Nama : Muhammad Aris Septanugroho
Nomor Absen : 19
Kelas : X SIJA 1
Mapel : Prodas
GM    : Dayu Destamy Ariefin, S.Pd

====PROGRAM OPERATOR LOGIKA====''')

print("Masukkan Angka pertama : ")
a = int(input())

print("Masukkan Angka kedua : ")
b = int(input())

print("Masukkan Angka ketiga : ")
c = int(input())

print("# Logika Not")
print(f"not {a} < {b} = {not a < b}")
print(f"not {a} > {c} = {not a > c}")
print(f"not {a} <= {b} = {not a <= b}")
print(f"not {a} >= {c} = {not a >= c}")
print(f"not {a} == {b} = {not a == b}")
print(f"not {b} != {c} = {not b != c}")
print("")

print("# Logika And")
print(f"{a} > {b} and {a} < {c} = {a>b and a<c}")
print(f"{a} >= {b} and {a} <= {c} = {a>=b and a<=c}")
print(f"{a} == {b} and {a} == {b} = {a==b and a==b}")
print(f"{a} != {b} and {b} != {c} = {a!=b and a!=b}")
print("")


print("# Logika Or")
print(f"{a} > {b} or {a} < {c} = {a>b or a<c}")
print(f"{a} >= {b} or {a} <= {c} = {a>=b or a<=c}")
print(f"{a} == {b} or {a} == {b} = {a==b or a==b}")
print(f"{a} != {b} or {b} != {c} = {a!=b or a!=b}")
