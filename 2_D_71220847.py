platbro = input("Masukkan Plat Nomor : ")
depanbro, tengahbro, belakangnro = platbro.split( )
try:
    nomorbro = int(tengahbro)
    if nomorbro >= 0 and nomorbro <= 3000:
        print("Plat nomor tersebut diperuntuka untuk angkutan mobil")
    elif nomorbro > 3000 and nomorbro <= 4000:
        print("Plat nomor tersebut diperuntuka untuk motor")
    elif nomorbro > 4000 and nomorbro <= 5000:
        print("Plat nomor tersebut diperuntuka untuk angkutan umum")
    else:
        print("Plat nomor tidak terindikasi ketiga angkutan tersebut")

except:
    print("Plat nomor Tidak Terindikasi, harus terdapat nomor kendaraan setelah kode daerah")
