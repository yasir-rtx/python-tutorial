import os
os.system('cls')

# Program Konversi Temperature

print("=====PROGRAM KONVERSI TEMPERATURE=====")

# Celcius
celcius = float(input("Celcius : "))

# C -> R
reamur = (4/5) * celcius
print("C -> R :", reamur, "R")

# C -> F
fahrenheit = ((9/5) * celcius) + 32
print("C -> F :", fahrenheit, "F")

# C -> K
kelvin = celcius + 273
print("C -> K :", kelvin, "K")

print("\n")



# reamur
reamur = float(input("Reamur : "))

# R -> C
celcius = (5/4) * reamur
print("R -> C :", celcius, "C")

# R -> F
fahrenheit = ((9/4) * reamur) + 32
print("R -> F :", fahrenheit, "F")

# R -> K
kelvin = ((5/4) * reamur) + 273
print("R -> K :", kelvin, "K")

print("\n")



# fahrenheit
fahrenheit = float(input("Fahrenheit : "))

# F -> C
celcius = ((5/9) * (fahrenheit - 32))
print("F -> C :", celcius, "C")

# F -> R
reamur = ((4/9) * (fahrenheit - 32))
print("F -> R :", reamur, "R")

# F -> K
kelvin = (celcius + 273)
print("F -> K :", kelvin, "K")

print("\n")



# kelvin
kelvin = float(input("Kelvin : "))

# K -> C
celcius = kelvin - 273
print("K -> C :", celcius, "C")

# K -> R
reamur = ((4/5) * (kelvin - 273))
print("K -> C :", reamur, "C")

# K -> F
fahrenheit = ((9/5) * celcius) + 32
print("K -> C :", fahrenheit, "C")