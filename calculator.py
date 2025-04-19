# funsi kalkulator
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error, tidak bolah ada angka 0"
    else:
        return x / y

# menjalankan dan masukan angka
def calculator():
    print("Selamat datang di kalkulator sederhana")
    print("Pilih operator:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    while True:
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan in ["1", "2", "3", "4"]:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == "1":
                hasil = {"angka1": angka1, "operator":"+", "angka2": angka2, "hasil": tambah(angka1, angka2)}
            if pilihan == "2":
                hasil = {"angka1": angka1, "operator":"-", "angka2": angka2, "hasil": kurang(angka1, angka2)}
            if pilihan == "3":
                hasil = {"angka1": angka1, "operator":"*", "angka2": angka2, "hasil": kali(angka1, angka2)}
            if pilihan == "4":
                hasil = {"angka1": angka1, "operator":"/", "angka2": angka2, "hasil": bagi(angka1, angka2)}
          
            print(f"{hasil['angka1']} {hasil['operator']} {hasil['angka2']} = {hasil['hasil']}")
        
        konfirmasiExit = input("Apakah anda ingin keluar? (y/n): ")
        if konfirmasiExit.lower() == "y":
            break

#jalankan
calculator()