# Inisialisasi variabel total harga tiket
running_total = 0.0

print("Masukkan umur pengunjung satu per satu.")
print("Tekan Enter langsung (kosongkan input) jika sudah selesai.")

# Perulangan untuk terus meminta input umur hingga pengguna memasukkan string kosong
while True:
    masukan_umur = input("Masukkan umur: ")

    # Jika pengguna langsung menekan enter tanpa memasukkan apapun, perulangan berhenti
    if masukan_umur == "":
        break

    # Konversi input umur menjadi integer
    umur = int(masukan_umur)

    # Menentukan harga berdasarkan kategori umur
    if umur <= 2:
        harga = 0.0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14.0
        print(f"Harga ${harga:.2f}")
    elif umur >= 65:
        harga = 18.0
        print(f"Harga ${harga:.2f}")
    else:
        harga = 23.0
        print(f"Harga ${harga:.2f}")

    # Menambahkan harga tiket ke total keseluruhan (running total)
    running_total += harga
    print(f"Running total: ${running_total:.2f}\n")

# Menampilkan total keseluruhan setelah perulangan selesai
print(f"\nTotal keseluruhan harga tiket: ${running_total:.2f}")

# Memproses pembayaran jika total harga > 0
if running_total > 0:
    masukan_uang = input("Masukkan jumlah uang yang dibayarkan: ")
    uang_dibayar = float(masukan_uang)

    # Menghitung kembalian jika uang yang dibayarkan mencukupi
    if uang_dibayar >= running_total:
        kembalian = uang_dibayar - running_total
        print(f"Uang kembalian: ${kembalian:.2f}")
    else:
        kurang = running_total - uang_dibayar
        print(f"Maaf, uang yang Anda bayarkan kurang ${kurang:.2f}")
else:
    print("Tidak ada tiket yang dipesan.")
        
