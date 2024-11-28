def luasPersegipanjang(p, l):
    luas = p * l
    return luas

p = float(input("Masukkan panjang : "))
l = float(input("Masukkan lebar : "))
luas = luasPersegipanjang(p, l)
print(f"Luas persegi panjang adalah : {luas}")