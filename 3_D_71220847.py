awalbro = int(input("Masukkan awal deret: "))
akhirbro = int(input("Masukkan akhir deret: "))

for barisbro in range (awalbro, akhirbro):
    hasilakhirbro = barisbro %6!=0 and barisbro %8!=0
    print(barisbro, end=" ") if hasilakhirbro else print(end="")