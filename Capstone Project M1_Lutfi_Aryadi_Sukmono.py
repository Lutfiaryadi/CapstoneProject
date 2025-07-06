from tabulate import tabulate

# =============================
# Data Product
# =============================

product_list = [
    ['OP1', 'One Piece', 'Monkey D Luffy', 135000, 3],
    ['OP2', 'One Piece', 'Roronoa Zoro', 115000, 4],
    ['DS1', 'Demon Slayer', 'Kamado Tanjiro', 115000, 6],
    ['DS2', 'Demon Slayer', 'Agatsuma Zenitsu', 110000, 4],
    ['JK1', 'Jujutsu Kaisen', 'Gojo Satoru', 115000, 4],
]

header_items = ['Product Code', 'Anime Title', 'Character', 'Price', 'Stock']

cart = []

# =============================
# Pengantar
# =============================

print("Welcome to Kidoo's Store!")
print("Temukan Action Figure Anime Kesukaanmu!")
input("Tekan Enter untuk masuk ke menu utama..\n")

# =============================
# Main Program
# =============================

while True:
    print("= Pilih Role =")
    print("1. Penjual")
    print("2. Pembeli")
    print("3. Keluar")
    role = input("Pilih (1-3): ")

    if role == "1":
        # Menu Penjual
        while True:
            print("\n== MENU ==")
            print("1. Tampilkan Produk")
            print("2. Tambah Produk")
            print("3. Update Produk")
            print("4. Hapus Produk")
            print("5. Kembali ke Menu")
            pilih_penjual = input("Pilih (1-5): ")

            if pilih_penjual == "1":
                if len(product_list) > 0:
                    print(tabulate(product_list, headers=header_items, tablefmt="grid"))
                else:
                    print("Belum ada produk.")

            elif pilih_penjual == "2":
                kode = input("Masukkan Product Code: ").strip().upper()
                sudah_ada = False
                for p in product_list:
                    if p[0] == kode:
                        sudah_ada = True
                        break
                if sudah_ada:
                    print("Produk sudah ada.")
                else:
                    anime = input("Anime Title: ")
                    karakter = input("Character: ")
                    harga = int(input("Price: "))
                    stok = int(input("Stock: "))
                    product_list.append([kode, anime, karakter, harga, stok])
                    print("Produk berhasil ditambahkan.")

            elif pilih_penjual == "3":
                if len(product_list) > 0:
                    print(tabulate(product_list, headers=header_items, tablefmt="grid"))
                    kode = input("Masukkan Product Code yang mau diupdate: ").strip().upper()
                    ada = False
                    for p in product_list:
                        if p[0] == kode:
                            ada = True
                            print(f"Produk: {p}")
                            print("1. Product Code")
                            print("2. Anime Title")
                            print("3. Character")
                            print("4. Price")
                            print("5. Stock")
                            kolom = int(input("Kolom yang mau diubah (1-5): "))
                            if kolom >=1 and kolom <=5:
                                nilai_baru = input("Masukkan nilai baru: ")
                                if kolom == 1:
                                    nilai_baru = nilai_baru.strip().upper() 
                                if kolom == 4 or kolom == 5:
                                    nilai_baru = int(nilai_baru)
                                p[kolom-1] = nilai_baru
                                print("Produk berhasil diupdate.")
                            break
                    if not ada:
                        print("Produk tidak ditemukan.")
                else:
                    print("Belum ada produk.")

            elif pilih_penjual == "4":
                if len(product_list) > 0:
                    print(tabulate(product_list, headers=header_items, tablefmt="grid"))
                    kode = input("Masukkan Product Code yang mau dihapus: ").strip().upper()
                    hapus = False
                    for p in product_list:
                        if p[0] == kode:
                            product_list.remove(p)
                            hapus = True
                            print("Produk berhasil dihapus.")
                            break
                    if not hapus:
                        print("Produk tidak ditemukan.")
                else:
                    print("Belum ada produk.")

            elif pilih_penjual == "5":
                break

            else:
                print("Masukkan pilihan yang benar.")

    elif role == "2":
        # Menu Pembeli
        while True:
            print("\n== MENU ==")
            print("1. Tampilkan Produk")
            print("2. Beli")
            print("3. Lihat Keranjang")
            print("4. Checkout & Bayar")
            print("5. Kembali ke Menu")
            pilih_pembeli = input("Pilih (1-5): ")

            if pilih_pembeli == "1":
                if len(product_list) > 0:
                    print(tabulate(product_list, headers=header_items, tablefmt="grid"))
                else:
                    print("Belum ada produk.")

            elif pilih_pembeli == "2":
                if len(product_list) > 0:
                    print(tabulate(product_list, headers=header_items, tablefmt="grid"))
                    kode = input("Masukkan Product Code yang mau dibeli: ").strip().upper()
                    ada = False
                    for p in product_list:
                        if p[0] == kode:
                            ada = True
                            qty = int(input("Jumlah yang mau dibeli: "))
                            if qty <= p[4]:
                                cart.append([p[0], p[1], p[2], p[3], qty])
                                print("Produk ditambahkan ke keranjang.")
                            else:
                                print("Stok tidak cukup.")
                            break
                    if not ada:
                        print("Produk tidak ditemukan.")
                else:
                    print("Belum ada produk.")

            elif pilih_pembeli == "3":
                if len(cart) > 0:
                    print(tabulate(cart, headers=header_items, tablefmt="grid"))
                else:
                    print("Keranjang kosong.")

            elif pilih_pembeli == "4":
                if len(cart) > 0:
                    total = 0
                    print("\n== List Belanjaan ==")
                    print(tabulate(cart, headers=header_items, tablefmt="grid"))
                    for c in cart:
                        total += c[3] * c[4]
                    print(f"Total yang harus dibayar: Rp {total:,}")
                    konfirmasi = input("Bayar sekarang? (Y/N): ").upper()
                    if konfirmasi == "Y":
                        print("Pembayaran berhasil. Terima kasih belanja di Kidoo's Store!")
                        cart.clear()
                    else:
                        print("Checkout dibatalkan.")
                else:
                    print("Keranjang kosong.")

            elif pilih_pembeli == "5":
                break

            else:
                print("Masukkan pilihan yang benar.")

    elif role == "3":
        print("Terima kasih sudah berkunjung ke Kidoo's Store.")
        break

    else:
        print("Masukkan pilihan yang benar.")