import random
import datetime
from costumer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin: "))
    trial = 0

    print("selamat datang di ATM")
    print("\n1 - cek saldo \t 2 - debet \t 3 - simpan \t 4 - ganti pin \t 5 - keluar")

    selectmenu = int(input("\nSilahkan pilih menu: "))

    if selectmenu == 1:
        print("\nSaldo anda sekarang: Rp" + str(atm.checkBalance()) + "\n")
    elif selectmenu == 2:
        nominal = float(input("Masukkan nominal saldo: "))
        verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut? y/n " + str(nominal) + " ")

        if verify_withdraw == "y":
            print("Saldo awal anda adalah Rp." + str(atm.checkBalance()) + "")
        else:
            break
        if nominal < atm.checkBalance():
            atm.withdrawBalance(nominal)
            print("Transaksi debet berhasil!")
            print("Saldo sisa sekarang: Rp." + str(atm.checkBalance()) + "")
        else:
            print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
            print("silahkan lakukan penambahan nominal saldo")
    elif selectmenu == 3:
        nominal = float(input("Masukkan nominal saldo: "))
        verify_deposit = input ("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut? y/n" + str(nominal) + " ")

        if verify_deposit == "y":
            atm.depositBalance(nominal)
            print("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n")
        else:
            break
    elif selectmenu == 4:
        verify_pin = int(input("Masukkan pin anda: "))

        while verify_pin != int(atm.checkPin()):
            print("pin anda salah. silahkan masukkan pin: ")
        
        updated_pin = int(input("silahkan masukkan pin baru: "))
        print("pin anda berhasil diganti!")

        verify_newpin = int(input("coba masukkan pin baru: "))

        if verify_newpin == updated_pin:
            print("pin baru anda sukses!")
        else:
            print("maaf, pin anda salah!")
    elif selectmenu == 5:
        print("resi tercetak otomatis saat anda keluar. \n harap simpan tanda terima ini |n sebagai bukti transaksi anda")
        print("no. rekord: ", random.randint(100000, 1000000))
        print("tanggal: ", datetime.datetime.now())
        print("saldo akhir: ", atm.checkBalance())
        print("Terima kasih telang menggunakan atm")
        exit()
    else:
        print("Error. maaf, menu tidak tersedia")

    while(id != int(atm.checkPin()) and trial < 3):
        id = int(input("pin anda salah. silahkan coba lagi: "))
        trial += 1

    if trial == 3:
        print("error. silahkan ambil kartu dan coba lagi")
        exit()
    
