import os
os.system('cls')
# ===CASTING DATA===

print("===============INTEGER===============")
data_int = 6
# Buat variabel untuk menampung hasil casting
var_float = float(data_int)
var_str   = str(data_int)
var_bool  = bool(data_int)
print("Value :", var_float, "{ Tipe:", type(var_float),"}")
print("Value :", var_str, "{ Tipe:", type(var_str),"}")
print("Value :", var_bool, "{ Tipe:", type(var_bool),"}")
print("=====================================\n")

print("================FLOAT================")
data_float = 6.8
# Buat variabel untuk menampung hasil casting
var_int   = int(data_float)
var_str   = str(data_float)
var_bool  = bool(data_float)
print("Value :", var_int, "{ Tipe:", type(var_int),"}")
print("Value :", var_str, "{ Tipe:", type(var_str),"}")
print("Value :", var_bool, "{ Tipe:", type(var_bool),"}")
print("=====================================\n")

print("===============BOOLEAN===============")
data_bool = True
# Buat variabel untuk menampung hasil casting
var_float = float(data_bool)
var_str   = str(data_bool)
var_int  = int(data_bool)
print("Value :", var_float, "{ Tipe:", type(var_float),"}")
print("Value :", var_str, "{ Tipe:", type(var_str),"}")
print("Value :", var_int, "{ Tipe:", type(var_int),"}")
print("=====================================\n")

print("================STRING===============")
data_str = ""
# Buat variabel untuk menampung hasil casting
# var_float = float(data_str) Program akan error jika value string != angka
# var_int   = int(data_str) Program akan error jika value string != angka
var_bool  = bool(data_str) #value akan jadi false jika value variabel kosong, selainnya akan bernilai true
# print("Value :", var_float, "{ Tipe:", type(var_float),"}")
# print("Value :", var_int, "{ Tipe:", type(var_int),"}")
print("Value :", var_bool, "{ Tipe:", type(var_bool),"}")
print("=====================================\n")
