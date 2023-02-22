namabro = input("Masukkan Nama Lengkap Anda: ")
prodibro = input("Masukkan Prodi Anda: ")
nilaibro = input("Masukkan Nilai (dalam huruf) yang Anda Dapat: ")

try:
    hasilbro = nilaibro
    if hasilbro == "A":
        print("Nilai anda adalah 4.0, tbl tbl serem bgt lohh")
    elif hasilbro == "A-":
        print("Nilai anda adalah 3.75, kamur keren!")
    elif hasilbro == "B+":
        print("Nilai anda adalah 3.25, lumayan")
    elif hasilbro == "B":
        print("Nilai anda adalah 3.0, bagus banh")
    elif hasilbro == "B-":
        print("Nilai anda adalah 3.75, kurang semangat belaljar nihh")
    elif hasilbro == "C+":
        print("Nilai anda adalah 2.25, dih")
    elif hasilbro == "C":
        print("Nilai anda adalah 2.0, belajar kek")
    elif hasilbro == "D":
        print("Nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?")
    elif hasilbro == "E":
        print("Nilai anda adalah 0, niat kuliah nggak sih???")
    else:
        print("Nilai yang anda masukkan tidak valid")

except:
    print("Nilai yang anda masukkan tidak valid")
