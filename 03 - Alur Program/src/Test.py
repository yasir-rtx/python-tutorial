import time #Library waktu

start_time = time.time()

for i in range(1,1000):
    a = 10
for i in range(1,1000):
    b = 10
for i in range(1,1000):
    c = 10

#Menampilkan waktu yang dibutuhkan untuk mengeksekusi program
print(time.time() - start_time, "second")

#waktu yang dibutuhkan (saat pembelajaran ini) tanpa di-compile adalah 0.004999876022338867 second
#waktu yang dibutuhkan (saat pembelajaran ini) setelah di-compiile adalah 0.0 second 