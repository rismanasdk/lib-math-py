import math

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

def poligon_beraturan_keliling(jumlah_sisi: int, sisi: float) -> float:
    return jumlah_sisi * sisi


def poligon_beraturan_luas(jumlah_sisi: int, sisi: float) -> float:
    return (jumlah_sisi * sisi ** 2) / (4 * math.tan(math.pi / jumlah_sisi))


def poligon_beraturan_apotema(jumlah_sisi: int, sisi: float) -> float:
    return sisi / (2 * math.tan(math.pi / jumlah_sisi))


def poligon_beraturan_sudut_dalam(jumlah_sisi: int) -> float:
    """
    Hasil dalam derajat
    """
    return ((jumlah_sisi - 2) * 180) / jumlah_sisi


def segilima_keliling(sisi: float) -> float:
    return poligon_beraturan_keliling(5, sisi)


def segilima_luas(sisi: float) -> float:
    return poligon_beraturan_luas(5, sisi)


def segienam_keliling(sisi: float) -> float:
    return poligon_beraturan_keliling(6, sisi)


def segienam_luas(sisi: float) -> float:
    return poligon_beraturan_luas(6, sisi)

def segitujuh_keliling(sisi: float) -> float:
    return poligon_beraturan_keliling(7, sisi)


def segitujuh_luas(sisi: float) -> float:
    return poligon_beraturan_luas(7, sisi)



def segidelapan_keliling(sisi: float) -> float:
    return poligon_beraturan_keliling(8, sisi)


def segidelapan_luas(sisi: float) -> float:
    return poligon_beraturan_luas(8, sisi)


def segisembilan_keliling(sisi: float) -> float:
    return poligon_beraturan_keliling(9, sisi)


def segisembilan_luas(sisi: float) -> float:
    return poligon_beraturan_luas(9, sisi)


def segisepuluh_keliling(sisi: float) -> float:
    return poligon_beraturan_keliling(10, sisi)


def segisepuluh_luas(sisi: float) -> float:
    return poligon_beraturan_luas(10, sisi)

def segduabelas_keliling(sisi: float) -> float:
    return poligon_beraturan_keliling(12, sisi)


def segduabelas_luas(sisi: float) -> float:
    return poligon_beraturan_luas(12, sisi)