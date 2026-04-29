class Mahasiswa:
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim
        self.__nilai_tugas = 0
        self.__nilai_uts = 0
        self.__nilai_uas = 0
        self.__nilai_akhir = 0

    # VALIDASI NILAI
    def __validasi_nilai(self, nilai):
        if 0 <= nilai <= 100:
            return True
        return False

    # SET NILAI
    def set_nilai(self, tugas, uts, uas):
        if (
            self.__validasi_nilai(tugas)
            and self.__validasi_nilai(uts)
            and self.__validasi_nilai(uas)
        ):
            self.__nilai_tugas = tugas
            self.__nilai_uts = uts
            self.__nilai_uas = uas
            self.hitung_nilai_akhir()
            print(f"Nilai {self.__nama} berhasil disimpan.\n")
        else:
            print("Error: Nilai harus di antara 0 - 100.\n")

    # HITUNG NILAI AKHIR
    # tugas = 30%
    # uts   = 30%
    # uas   = 40%
    def hitung_nilai_akhir(self):
        self.__nilai_akhir = (
            (self.__nilai_tugas * 0.30)
            + (self.__nilai_uts * 0.30)
            + (self.__nilai_uas * 0.40)
        )

    # GET NILAI AKHIR
    def get_nilai_akhir(self):
        return self.__nilai_akhir

    # GET GRADE
    # A >= 85
    # B >= 70
    # C >= 60
    # D < 60
    def get_grade(self):
        if self.__nilai_akhir >= 85:
            return "A"
        elif self.__nilai_akhir >= 70:
            return "B"
        elif self.__nilai_akhir >= 60:
            return "C"
        else:
            return "D"

    # UPDATE NILAI
    def update_nilai(self, jenis, nilai):
        if not self.__validasi_nilai(nilai):
            print("Error: Nilai harus di antara 0 - 100.\n")
            return

        jenis = jenis.lower()

        if jenis == "tugas":
            self.__nilai_tugas = nilai
        elif jenis == "uts":
            self.__nilai_uts = nilai
        elif jenis == "uas":
            self.__nilai_uas = nilai
        else:
            print("Jenis nilai tidak valid. Gunakan: tugas / uts / uas\n")
            return

        self.hitung_nilai_akhir()
        print(f"Nilai {jenis} milik {self.__nama} berhasil diupdate.\n")

    # CEK KELULUSAN
    def is_lulus(self):
        if self.__nilai_akhir >= 60:
            return "Lulus"
        else:
            return "Tidak Lulus"

    # GET NAMA
    def get_nama(self):
        return self.__nama

    # GET NIM
    def get_nim(self):
        return self.__nim

    # INFO MAHASISWA
    def info(self):
        print("======================================")
        print(f"Nama         : {self.__nama}")
        print(f"NIM          : {self.__nim}")
        print(f"Nilai Tugas  : {self.__nilai_tugas}")
        print(f"Nilai UTS    : {self.__nilai_uts}")
        print(f"Nilai UAS    : {self.__nilai_uas}")
        print(f"Nilai Akhir  : {self.__nilai_akhir:.2f}")
        print(f"Grade        : {self.get_grade()}")
        print(f"Status       : {self.is_lulus()}")
        print("======================================\n")


# PROGRAM UTAMA
mahasiswa1 = Mahasiswa("Audit", "231001")
mahasiswa2 = Mahasiswa("Doni", "231002")
mahasiswa3 = Mahasiswa("Salsa", "231003")

# input nilai mahasiswa
mahasiswa1.set_nilai(85, 80, 90)
mahasiswa2.set_nilai(70, 75, 80)
mahasiswa3.set_nilai(55, 60, 58)

# simpan ke dalam list
data_mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3]

# TAMPILKAN SELURUH DATA
print("========== DATA SELURUH MAHASISWA ==========\n")

for mhs in data_mahasiswa:
    mhs.info()

# UPDATE SALAH SATU NILAI
print("========== UPDATE NILAI ==========\n")

# update nilai UAS mahasiswa Audit
mahasiswa3.update_nilai("uas", 85)

# TAMPILKAN HASIL SETELAH UPDATE
print("========== DATA SETELAH UPDATE ==========\n")

for mhs in data_mahasiswa:
    mhs.info()

# BONUS 1 : MAHASISWA DENGAN NILAI TERTINGGI
tertinggi = data_mahasiswa[0]

for mhs in data_mahasiswa:
    if mhs.get_nilai_akhir() > tertinggi.get_nilai_akhir():
        tertinggi = mhs

print("========== MAHASISWA NILAI TERTINGGI ==========\n")
print(f"Nama         : {tertinggi.get_nama()}")
print(f"NIM          : {tertinggi.get_nim()}")
print(f"Nilai Akhir  : {tertinggi.get_nilai_akhir():.2f}")
print(f"Grade        : {tertinggi.get_grade()}\n")

# BONUS 2 : URUTKAN BERDASARKAN NILAI AKHIR
print("========== URUTAN NILAI TERTINGGI ==========\n")

urut = sorted(
    data_mahasiswa,
    key=lambda x: x.get_nilai_akhir(),
    reverse=True
)

for mhs in urut:
    print(
        f"{mhs.get_nama()} - "
        f"{mhs.get_nim()} - "
        f"Nilai Akhir: {mhs.get_nilai_akhir():.2f} - "
        f"Grade: {mhs.get_grade()}"
    )