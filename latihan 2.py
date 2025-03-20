from abc import ABC, abstractmethod

class TimF1(ABC):
    def __init__(self, nama_tim, kecepatan_maks):
        self.nama_tim = nama_tim
        self.kecepatan_maks = kecepatan_maks
        self.kecepatan_akhir = kecepatan_maks

    @abstractmethod
    def pit_stop(self):
        """Simulasi waktu pit stop"""
        pass

    @abstractmethod
    def gunakan_DRS(self, lawan):
        """Simulasi penggunaan DRS untuk meningkatkan kecepatan dan menyerang lawan"""
        pass

class RedBull(TimF1):
    def pit_stop(self):
        self.kecepatan_akhir -= 5
        print(f"=== Turn 1 ===")
        print(f"{self.nama_tim} melakukan pit stop dalam 2.3 detik!")
        print(f"{self.nama_tim} kecepatan turun menjadi {self.kecepatan_akhir} km/jam.")

    def gunakan_DRS(self, lawan):
        tambahan_kecepatan = 20
        self.kecepatan_akhir += tambahan_kecepatan
        lawan.kecepatan_akhir -= 5
        print(f"=== Turn 2 ===")
        print(f"{self.nama_tim} mengaktifkan DRS! Kecepatan naik menjadi {self.kecepatan_akhir} km/jam.")
        print(f"{lawan.nama_tim} Downforce! Kecepatan turun menjadi {lawan.kecepatan_akhir} km/jam.")

class Ferrari(TimF1):
    def pit_stop(self):
        self.kecepatan_akhir -= 5
        print(f"{self.nama_tim} melakukan pit stop dalam 2.7 detik!")
        print(f"{self.nama_tim} kecepatan turun menjadi {self.kecepatan_akhir} km/jam.")

    def gunakan_DRS(self, lawan):
        tambahan_kecepatan = 18
        self.kecepatan_akhir += tambahan_kecepatan
        lawan.kecepatan_akhir -= 5
        print(f"=== Turn 2 ===")
        print(f"{self.nama_tim} mengaktifkan DRS! Kecepatan naik menjadi {self.kecepatan_akhir} km/jam.")
        print(f"{lawan.nama_tim} Downforce! Kecepatan turun menjadi {lawan.kecepatan_akhir} km/jam.")

def urutkan_berdasarkan_kecepatan(tim_f1):
    return sorted(tim_f1, key=kecepatan_tim, reverse=True)

def kecepatan_tim(tim):
    return tim.kecepatan_akhir

redbull = RedBull("Red Bull Racing", 340)
ferrari = Ferrari("Scuderia Ferrari", 335)

redbull.pit_stop()
ferrari.pit_stop()

redbull.gunakan_DRS(ferrari)

tim_f1 = [redbull, ferrari]
tim_f1 = urutkan_berdasarkan_kecepatan(tim_f1)

print("\n=== Hasil Akhir Race! ===")
for i, tim in enumerate(tim_f1, 1):
    print(f"P{i}: {tim.nama_tim} dengan kecepatan akhir {tim.kecepatan_akhir} km/jam")

