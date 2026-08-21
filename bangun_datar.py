def persegi_keliling(sisi: int):
    return 4 * sisi

def persegi_luas(sisi: int):
    return sisi * sisi

def persegi_panjang_keliling(panjang: int, lebar: int):
    return 2 * (panjang + lebar)

def persegi_panjang_luas(panjang: int, lebar: int):
    return panjang * lebar

def jajar_genjang_keliling(sisi1: int, sisi2: int):
    return 2 * (sisi1 + sisi2)

def jajar_genjang_luas(alas: int, tinggi: int):
    return alas * tinggi

def segitiga_keliling(sisi1: int, sisi2: int, sisi3: int):
    return sisi1 + sisi2 + sisi3

def segitiga_luas(alas: int, tinggi: int) -> float:
    return 1/2 * alas * tinggi

def belah_ketupat_keliling(sisi: int):
    return 4 * sisi

def belah_ketupat_luas(diagonal1: int, diagonal2: int) -> float:
    return 1/2 * diagonal1 * diagonal2

def layang_layang_keliling(sisi1: int, sisi2: int):
    return 2 * (sisi1 + sisi2)

def layang_layang_luas(diagonal1: int, diagonal2: int) -> float:
    return 1/2 * diagonal1 * diagonal2

def trapesium_keliling(a: int, b: int, c: int, d: int):
    return a + b + c + d

def trapesium_luas(sisi_sejajar1: int, sisi_sejajar2: int, tinggi: int) -> float:
    return 1/2 * (sisi_sejajar1 + sisi_sejajar2) * tinggi

def lingkaran_keliling(jari_jari: int) -> float:
    return 2 * 3.14 * jari_jari

def lingkaran_luas(jari_jari: int) -> float:
    return 3.14 * jari_jari ** 2
