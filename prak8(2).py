# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:40:12 2024

@author: Lenovo
"""

def pangkat_rekursif(angka, pangkat):
    if pangkat == 0:
        return 1
    elif pangkat < 0:
        return 1 / pangkat_rekursif(angka, -pangkat)
    else:
        return angka * pangkat_rekursif(angka, pangkat - 1)

print("Ini merupakan program pemangkatan negatif dan positif, tekan Enter untuk berhenti")

while True:
    angka_input = input("Masukkan Angka: ")
    if angka_input == "":
        print("Program Selesai")
        break
    angka = int(angka_input)

    pangkat_input = input("Masukkan Pangkatnya: ")
    if pangkat_input == "":
        print("Program Selesai")
        break
    pangkat = int(pangkat_input)
    
    hasil = pangkat_rekursif(angka, pangkat)
    print("Hasilnya adalah:", hasil)
