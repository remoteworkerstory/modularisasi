"""
Program meghitung luas segitiga
luas_segitiga = alas * tinggi /2
"""
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi /2
print(f'Segitiga dengan alas = {alas}, tinggi = {tinggi} \nmemiliki luas = {luas_segitiga}')

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f' menghitung segitiga dengan fungsi {hitung_luas_segitiga(10, 6)}')
print(f' menghitung segitiga dengan fungsi {hitung_luas_segitiga(20, 16)}')

print('alas = ')
alas = input()

print('tinggi = ')
tinggi = input()


print(f'Segitiga dengan alas = {alas}, tinggi = {tinggi} \nmemiliki luas = {luas_segitiga}')
