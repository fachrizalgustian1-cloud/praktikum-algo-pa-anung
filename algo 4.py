print("Program Perulangan Angka Menurun")
#Fachrizal gustian anwar
#065002600001
for i in range(7, 0, -1):
    print(str(i) * i)
    
    
print("Program Penentu Jumlah Hari dalam Bulan (While Loop)")

status = "y"
while status.lower() == "y":
    # Input tahun dan bulan
    tahun = int(input("\nMasukkan Tahun (contoh: 2026): "))
    bulan = int(input("Masukkan Bulan (1-12): "))
    
    # Validasi angka bulan
    if 1 <= bulan <= 12:
        # Pengecekan tahun kabisat untuk bulan Februari (bulan 2)
        if bulan == 2:
            # Tahun kabisat: habis dibagi 4 dan tidak habis dibagi 100, atau habis dibagi 400
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                jumlah_hari = 29
                keterangan = "Tahun Kabisat"
            else:
                jumlah_hari = 28
                keterangan = "Bukan Tahun Kabisat"
            print(f"Bulan 2 (Februari) tahun {tahun} ({keterangan}) memiliki {jumlah_hari} hari.")
            
        # Bulan dengan 31 hari (Januari, Maret, Mei, Juli, Agustus, Oktober, Desember)
        elif bulan in [1, 3, 5, 7, 8, 10, 12]:
            print(f"Bulan ke-{bulan} pada tahun {tahun} memiliki 31 hari.")
            
        # Bulan dengan 30 hari (April, Juni, September, November)
        else:
            print(f"Bulan ke-{bulan} pada tahun {tahun} memiliki 30 hari.")
    else:
        print("!- Error: Masukkan angka bulan antara 1 sampai 12 dengan benar -! ")
        
    # Konfirmasi perulangan while
    status = input("\nApakah Anda ingin menghitung lagi? (y/n): ")

print("\nTerima kasih telah menggunakan program ini!")