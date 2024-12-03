import math

def lkubus(sisi):
    hasil = 6 * sisi *sisi
    print(f'hasil luas kubus 6*{sisi}*{sisi}={hasil}')

def ltabung(jari, tinggi):
    luas = 2 * 3.14 * jari * (jari + tinggi)
    print(f"Luas Tabung = 2 dikalikan 3,14 x {jari} x ({jari} + {tinggi}) = {luas}")

def lbalok(panjang, lebar, tinggi):
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print(f"Lyuas Balok adalah 2 x ({panjang} x {lebar} + {panjang} x {tinggi} + {lebar} x {tinggi}) = {luas}")

def llimas(la,t):
    hasil = 1/3 *la*t
    print(f'hasil luas limas adalah = 1/3*{la}*{t}={hasil}')

def lprisma(la,lst):
    hasil = 2*la+lst
    print(f'hasil luas prisma adalah = 2 * {la} + {lst} = {hasil}')
