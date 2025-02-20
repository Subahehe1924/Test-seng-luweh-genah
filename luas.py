import os

os.system("cls")
#luas persegi panjang
def luas_persegi_panjang(panjang,lebar):
    return panjang * lebar

panjang = int(input("masukkan panjang : "))
lebar = int(input("masukkan lebar : "))

hasil= luas_persegi_panjang(panjang,lebar)
print(f"luas persegi panjang : {hasil}")
print(30*"=")

#luas segitiga
def luas_segitiga(alas,tinggi):
    return (alas * tinggi)/2

alas = int(input("masukkan alas : "))
tinggi = int(input("masukkan tinggi : "))

hasil = luas_segitiga(alas,tinggi)
print(f"Luas Segitiga : {hasil}")
print(30*"=")

#luas lingkaran
def luas_lingkaran(diameter):
    jari_jari = diameter / 2
    hasil = (22/7) * (jari_jari**2)
    return hasil

diameter = int(input("Masukkan Diameter : "))

hasil = luas_lingkaran(diameter)
print(f"Luas Lingkaran : {hasil}")
print(30*"=")

def luas_persegi(sisi):
    return sisi * sisi

sisi = int(input("masukkan panjang sisi : ")
           
hasil = luas_persegi(sisi)
print(f"Luas Persegi Adalah : {hasil}")
print(30*"=")

def luas_trapesium(a,b,t):
    return ((1/2) * (a + b)) * t

a = int(input("masukkan sisi sejajar(pendek) : ")
b = int(input("masukkan sisi sejajar(panjang) : ")
t = int(input("masukkan tinggi : ")

hasil = luas_trapesium(a,b,t)
print(f"Hasil Trapesium Adalah : {hasil}")
print(30*"=")
