import json

FILE_DATA = "data_uang.json"

# =============================
# Fungsi load dan save data
# =============================
def load_data():
    try:
        with open(FILE_DATA, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "saldo": 0,
            "pemasukan": 0,
            "pengeluaran": 0
        }

def save_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)

data = load_data()

# =============================
# Fungsi tambah pemasukan
# =============================
def tambah_pemasukan():
    global data
    jumlah = int(input("Masukkan jumlah pemasukan: Rp "))

    data["saldo"] += jumlah
    data["pemasukan"] += jumlah

    save_data(data)
    print("✅ Pemasukan berhasil ditambahkan!")

# =============================
# Fungsi tambah pengeluaran
# =============================
def tambah_pengeluaran():
    global data
    jumlah = int(input("Masukkan jumlah pengeluaran: Rp "))

    if jumlah > data["saldo"]:
        print("⚠️ Saldo tidak cukup!")
    else:
        data["saldo"] -= jumlah
        data["pengeluaran"] += jumlah
        save_data(data)
        print("✅ Pengeluaran berhasil dicatat!")

# =============================
# Fungsi lihat saldo
# =============================
def lihat_saldo():
    print("\n===== SALDO SAAT INI =====")
    print(f"Saldo : Rp {data['saldo']}")
    print("=========================\n")

# =============================
# Menu laporan
# =============================
def laporan():
    print("\n===== LAPORAN KEUANGAN =====")
    print(f"Total Pemasukan   : Rp {data['pemasukan']}")
    print(f"Total Pengeluaran : Rp {data['pengeluaran']}")
    print(f"Sisa Saldo        : Rp {data['saldo']}")
    print("===========================\n")

# =============================
# Menu utama
# =============================
def menu():
    while True:
        print("=== APLIKASI UANG SAKU ===")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Lihat Saldo")
        print("4. Laporan")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_pemasukan()
        elif pilihan == "2":
            tambah_pengeluaran()
        elif pilihan == "3":
            lihat_saldo()
        elif pilihan == "4":
            laporan()
        elif pilihan == "5":
            print("Terima kasih! 👋")
            break
        else:
            print("❌ Pilihan tidak valid!")

menu()
