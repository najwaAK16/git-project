# Nama : Najwa Aidatul Karomah
# NIM : 2505051
# Kelas : C

# NO 1
print("===== Soal NO 1 =====")
import numpy as np

suhu_c = np.array([27, 31, 34, 39, 28, 22, 21, 33, 26, 34]) #suhu dalam celcius
suhu_f = (suhu_c * 9/5) + 32 #konversi suhu ke dalam fahrenheit

print("Suhu dalam Celcius: ", suhu_c)
print("Suhu dalam Fahrenheit: ", suhu_f)