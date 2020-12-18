import os
os.system('cls')

data = input("Inputkan sesuatu : ")
print("Your input : ", data)

# value dari input akan selalu bertipe string
# untuk itu value perlu di-casting 
# syntax untuk casting dari input :
variabel = int(input("Input sesuatu (harus angka) : "))
print("Your input : ", variabel, "{ Tipe data :", type(variabel), "}")