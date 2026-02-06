catatan = []

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
        return

    print("\nDaftar Catatan Belajar:")
    for i, c in enumerate(catatan, 1):
        mapel = c.get('mapel', '')
        topik = c.get('topik', '')
        durasi = c.get('durasi', 0)
        print(f"{i}. Mapel: {mapel} | Topik: {topik} | Durasi: {durasi} menit")
    print(f"Total catatan: {len(catatan)}")

def total_waktu():
    pass

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
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
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")