class Mahasiswa :
    def __init__(self,nama,nim,nilai_tugas,nilai_uts,nilai_uas) :
        self.__nama = nama
        self.__nim = nim
        self.__nilai_tugas = nilai_tugas
        self.__nilai_uts = nilai_uts
        self.__nilai_uas = nilai_uas
        self.__nilai_akhir = []
        self.__grade = []
        
        self.__data = []
    
    def set_add_data(self) :
        for number,nama in enumerate(self.__nama,start=1) :
            self.__data.append({
                f"nama_mahasiswa_{number}" : nama
            })
        
        for index_list,nim in enumerate(self.__nim,start=0) :
            self.__data[index_list]["nim_mahasiswa"] = nim
        
        for index_list,tugas in enumerate(self.__nilai_tugas,start=0) :
            self.__data[index_list]["nilai_tugas"] = tugas
        
        for index_list,uts in enumerate(self.__nilai_uts,start=0) :
            self.__data[index_list]["nilai_uts"] = uts
        
        for index_list,uas in enumerate(self.__nilai_uas,start=0) :
            self.__data[index_list]["nilai_uas"] = uas
              
        return self.__data
        
    
    def set_nilai(self,nilai_tugas,nilai_uts,nilai_uas) :
        pass
    
    def hitung_nilai_akhir(self) :
        for index_list,data in enumerate(self.__data,start=0) :
            self.__nilai_akhir.append(((self.__data[index_list]["nilai_tugas"]) * 0.3) + ((self.__data[index_list]["nilai_uts"]) * 0.3) + ((self.__data[index_list]["nilai_uas"]) * 0.4))
            self.__data[index_list]["nilai_akhir"] = self.__nilai_akhir[index_list]
            
            if(self.__data[index_list]["nilai_akhir"] >= 85) :
                self.__grade.append("A")
            elif ((self.__data[index_list]["nilai_akhir"] >= 70) and (self.__data[index_list]["nilai_akhir"] < 85)) :
                self.__grade.append("B")
            elif ((self.__data[index_list]["nilai_akhir"] >= 60) and (self.__data[index_list]["nilai_akhir"] < 70)) :
                self.__grade.append("C")
            else :
                self.__grade.append("D")
            
            self.__data[index_list]["grade"] = self.__grade[index_list]
        
        return self.__data 
    
    def get_grade(self) :
        return self.__grade
    
    
    def update_nilai(self,jenis:str,nilai:list) :
        if len(nilai) == len(self.__data) :
            if (jenis == 'tugas') or (jenis == 'uts') or (jenis == 'uas') :
                for index_list, data in enumerate(self.__data,start=0) :
                    self.__data[index_list][f"nilai_{jenis}"] = int(nilai[index_list])
                return True
            else :
                return "Jenis nilai tidak valid!"
        else :
            if(len(self.__data) != 0) :
                return f"Data nilai yg di masukkan tidak valid, anda harus menginputkan {len(self.__data)} nilai!"
            else :
                return f"Anda masih belum memasukkan data mahasiswa"

    
    def is_lulus(self) :
        pass
    
    def info(self) :
        return self.__data
    
    def get_nama(self) :
        return self.__nama
    
    def get_nim(self) :
        return self.__nim
    
    def mahasiswa_nilai_tertinggi(self) :
        return max(self.__data, key=lambda nilai_akhir:nilai_akhir["nilai_akhir"])
    
    def mengurutkan_mahasiswa(self) :
        return sorted(self.__data, key=lambda nilai_akhir:nilai_akhir["nilai_akhir"],reverse=True)

nama_mahasiswa = []
nim_mahasiswa = []
tugas_mahasiswa = []
uts_mahasiswa = []
uas_mahasiswa = []

mahasiswa = Mahasiswa(nama_mahasiswa,nim_mahasiswa,tugas_mahasiswa,uts_mahasiswa,uas_mahasiswa)



print("~ SELAMAT DATANG DI SISTEM DOSEN ~\n")

while True :
    print("\nKetik 1, untuk menambahkan data mahasiswa")
    print("Ketik 2, untuk menampilkan seluruh data mahasiswa")
    print("Ketik 3, untuk update salah satu nilai mahasiswa")
    print("Ketik 4, untuk menampilkan data mahasiswa dengan nilai tertinggi")
    print("Ketik 5, untuk melihat data mahasiswa berdasarkan nilai akhir")
    print("Ketik exit, untuk keluar dari sistem\n")
    
    inputan = input("Masukkan: ").lower()
    
    if inputan == 'exit' :
        print("\nAnda keluar dari sistem")
        break
    
    if inputan == "1" :
        while True :
            nama = input("nama_mahasiswa : ")
            nama_mahasiswa.append(nama)
            
            nim  = input("nim_mahasiswa  : ")
            nim_mahasiswa.append(nim)
            
            tugas = int(input("nilai_tugas    : "))
            tugas_mahasiswa.append(tugas)
            
            uts = int(input("nilai_uts      : "))
            uts_mahasiswa.append(uts)
            
            uas = int(input('nilai uas      : '))
            uas_mahasiswa.append(uas)
            
            
            confirm = input("mau tambah data mahasiswa lagi ? (y/n) : ")
            if confirm == 'n' :
                mahasiswa = Mahasiswa(nama_mahasiswa,nim_mahasiswa,tugas_mahasiswa,uts_mahasiswa,uas_mahasiswa)
                mahasiswa.set_add_data()
                mahasiswa.hitung_nilai_akhir()
                print("Data mahasiswa berhasil di tambahkan~")
                break
            
    if inputan == "2" :
        info = mahasiswa.info()
    
        print("Daftar Semua Mahasiswa : \n")
        if not info :
            print("Daftar mahasiswa masih kosong")
        else :
            for m in info :
                print(f"{m}")
            print("")
    
    if inputan == "3" :
        jenis = input("Masukkan jenis nilai yg diupdate   : ")
        nilai = input("Masukkan nilai dengan pemisah koma : ").split(",")
        
        if mahasiswa.update_nilai(jenis,nilai) == True:
            print("Data nilai mahasiswa berhasil di update : ")
            for m in mahasiswa.info() :
                print(f"{m}")
                
            print("")
        else :
            print(mahasiswa.update_nilai(jenis,nilai))
    
    if inputan == "4" : 
        if len(mahasiswa.info()) == 0 :
            print("Daftar mahasiswa masih kosong")
        else :
            print("Mahasiswa dengan nilai tertinggi : ")
            print(mahasiswa.mahasiswa_nilai_tertinggi())
            
    if inputan == "5" : 
        if len(mahasiswa.info()) == 0 :
            print("Daftar mahasiswa masih kosong")
        else :
            print("mahasiswa dengan nilai tertinggi : ")
            for i in mahasiswa.mengurutkan_mahasiswa() :
                print(f"{i}")