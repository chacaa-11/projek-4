catatan = []
favorit_mapel = set()

def tambah_catatan():
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()
    while True:
        durasi_input = input("Durasi belajar (menit): ").strip()
        if durasi_input.isdigit():
            durasi = int(durasi_input)
            break
        else:
            print("Masukkan angka untuk durasi (contoh: 30). Coba lagi.")

    catatan.append({
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi
    })
    print("Catatan tersimpan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    print("\nDaftar Catatan Belajar:")
    for i, c in enumerate(catatan, 1):
        mapel = c.get('mapel', '')
        topik = c.get('topik', '')
        durasi = c.get('durasi', 0)
        print(f"{i}. Mapel: {mapel} | Topik: {topik} | Durasi: {durasi} menit")
    print(f"Total catatan: {len(catatan)}")
    input("\nTekan Enter untuk kembali ke menu...")

def total_waktu():
    if not catatan:
        print("Belum ada catatan belajar.")
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    total = sum(c.get('durasi', 0) for c in catatan)
    jam = total // 60
    menit = total % 60
    
    print("\n=== Total Waktu Belajar ===")
    print(f"Total durasi: {total} menit")
    print(f"             = {jam} jam {menit} menit")
    input("\nTekan Enter untuk kembali ke menu...")

def filter_per_mapel():
    if not catatan:
        print("Belum ada catatan belajar.")
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    mapel_unik = set(c.get('mapel', '') for c in catatan)
    print("\nMapel yang tersedia:")
    mapel_list = sorted(list(mapel_unik))
    for i, m in enumerate(mapel_list, 1):
        print(f"{i}. {m}")
    
    try:
        pilih = int(input("Pilih nomor mapel: "))
        if 1 <= pilih <= len(mapel_list):
            mapel_terpilih = mapel_list[pilih - 1]
            catatan_filter = [c for c in catatan if c.get('mapel', '') == mapel_terpilih]
            
            print(f"\n=== Catatan untuk mapel: {mapel_terpilih} ===")
            total_mapel = 0
            for i, c in enumerate(catatan_filter, 1):
                topik = c.get('topik', '')
                durasi = c.get('durasi', 0)
                print(f"{i}. Topik: {topik} | Durasi: {durasi} menit")
                total_mapel += durasi
            
            print(f"Total durasi: {total_mapel} menit")
        else:
            print("Pilihan tidak valid")
    except ValueError:
        print("Masukkan angka yang valid")
    
    input("\nTekan Enter untuk kembali ke menu...")

def toggle_mapel_favorit():
    if not catatan:
        print("Belum ada catatan belajar.")
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    mapel_unik = set(c.get('mapel', '') for c in catatan)
    print("\nMapel yang tersedia:")
    for m in sorted(mapel_unik):
        status = "★ " if m in favorit_mapel else "☆ "
        print(f"{status}{m}")
    
    mapel_input = input("Masukkan nama mapel untuk toggle favorit: ").strip()
    if mapel_input in mapel_unik:
        if mapel_input in favorit_mapel:
            favorit_mapel.remove(mapel_input)
            print(f"'{mapel_input}' dihapus dari favorit.")
        else:
            favorit_mapel.add(mapel_input)
            print(f"'{mapel_input}' ditambahkan ke favorit.")
    else:
        print("Mapel tidak ditemukan.")
    
    input("\nTekan Enter untuk kembali ke menu...")

def lihat_mapel_favorit():
    if not favorit_mapel:
        print("Belum ada mapel favorit.")
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    print("\n=== Mapel Favorit ===")
    total_favorit = 0
    for mapel in sorted(favorit_mapel):
        catatan_mapel = [c for c in catatan if c.get('mapel', '') == mapel]
        durasi_mapel = sum(c.get('durasi', 0) for c in catatan_mapel)
        print(f"★ {mapel}: {len(catatan_mapel)} catatan ({durasi_mapel} menit)")
        total_favorit += durasi_mapel
    
    print(f"Total waktu belajar mapel favorit: {total_favorit} menit")
    input("\nTekan Enter untuk kembali ke menu...")

def submenu_pengembangan():
    while True:
        print("\n=== Pengembangan Mandiri ===")
        print("1. Filter catatan per mapel")
        print("2. Toggle mapel favorit")
        print("3. Lihat mapel favorit")
        print("4. Kembali ke menu utama")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            filter_per_mapel()
        elif pilihan == "2":
            toggle_mapel_favorit()
        elif pilihan == "3":
            lihat_mapel_favorit()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("5. Pengembangan mandiri")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "5":
        submenu_pengembangan()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")