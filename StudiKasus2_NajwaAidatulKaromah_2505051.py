# Nama : Najwa Aidatul Karomah
# NIM : 2505051
# Kelas : C

print("===== Soal NO 2 =====")
import numpy as np

# data nilai ujian 30 siswa
nilai_ujian = np.array([
    66, 77, 91, 97, 81, 86, 95, 82, 91, 73,
    79, 87, 84, 94, 90, 84, 78, 86, 87, 76,
    88, 86, 85, 93, 81, 76, 90, 92, 89, 91
])

nilai_urut = np.sort(nilai_ujian)[::-1] 

lima_tertinggi = nilai_urut[:5] 

print("Nilai ujian semua siswa :", nilai_ujian)
print("Nilai dari terbesar ke terkecil :", nilai_urut)
print("5 nilai tertinggi :", lima_tertinggi)