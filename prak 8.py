# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:16:12 2024

@author: Lenovo
"""
def jumlah_rekursif(angka):
    if not angka:
        return 0
    return angka[0] + jumlah_rekursif(angka[1:])
jumlah = int(input("Masukkan Jumlah: "))
angka = []
for i in range(1, jumlah + 1):
    num = int(input(f"Masukkan bilangan ke-{i}: "))
    angka.append(num)
hasil = jumlah_rekursif(angka)
print(f"Hasil dari penjumlahan adalah: {hasil}")
