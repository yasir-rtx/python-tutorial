data_int = 10
print("Data :", data_int, "{ Bertipe", type(data_int), "}")

data_float = 21.7
print("Data :", data_float, "{ Bertipe", type(data_float), "}")

data_str = "\"Dream\""
print("Data :", data_str, "{ Bertipe", type(data_str), "}")

data_bool = True
print("Data :", data_bool, "{ Bertipe", type(data_bool), "}")

# Karena Python dibangun dari bahasa pemograman C, 
# maka python dapat menggunakan tipe data C dengan cara meng-import nya terlebih dahulu.

from ctypes import c_char, c_double # syntax  untuk import tipe data C

data_double = c_double(100.5)
print("Data :", data_double, "{ Bertipe", type(data_double), "}")