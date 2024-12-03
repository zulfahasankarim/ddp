import math

#dek fungsi modul

def lpersegi(sisi):
    hasil = sisi * sisi
    print(f'hasil perhitungan luas persegi {sisi} * {sisi}={hasil}')

def llingkaran(jari):
    hasil = 22/7 * jari*jari
    print(f'hasil perhitungan luas lingkaran {22/7} * {jari} * {jari}={hasil}')


def ljajargenjang(alas,tinggi):
    hasil = alas * tinggi
    print(f'hasil perhitungan luas jajar genjang {alas} * {tinggi}={hasil}')

def lpersegi_panjang(p,l):
    hasil = p *l
    print (f'Hasil Perhitungan Luas Persegi Panjang {p} * {l} = {hasil}cm2')

def lsegitiga(a,t):
    hasil= 1/2 *a*t
    print (f'Hasyil Perhitungan segitiga adalah {a} * {t} = {hasil}')