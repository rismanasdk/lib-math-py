import math


def persamaan_linear_satu_variabel(a: float, b: float) -> float:
    """
    Bentuk: ax + b = 0
    Mencari nilai x
    """
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0 (bukan persamaan linear)")
    return -b / a

def spldv_eliminasi_substitusi(a1: float, b1: float, c1: float,
                                 a2: float, b2: float, c2: float) -> tuple:
    """
    Bentuk:
    a1*x + b1*y = c1
    a2*x + b2*y = c2
    Menggunakan metode determinan (Cramer)
    Mengembalikan (x, y)
    """
    determinan = (a1 * b2) - (a2 * b1)
    if determinan == 0:
        raise ValueError("Determinan = 0, sistem tidak punya solusi tunggal (sejajar/berimpit)")

    x = ((c1 * b2) - (c2 * b1)) / determinan
    y = ((a1 * c2) - (a2 * c1)) / determinan
    return (x, y)


def spltv_cramer(a1: float, b1: float, c1: float, d1: float,
                  a2: float, b2: float, c2: float, d2: float,
                  a3: float, b3: float, c3: float, d3: float) -> tuple:
    """
    Bentuk:
    a1*x + b1*y + c1*z = d1
    a2*x + b2*y + c2*z = d2
    a3*x + b3*y + c3*z = d3
    Menggunakan metode determinan (Cramer)
    Mengembalikan (x, y, z)
    """
    def determinan_3x3(m11, m12, m13, m21, m22, m23, m31, m32, m33):
        return (m11 * (m22 * m33 - m23 * m32)
                - m12 * (m21 * m33 - m23 * m31)
                + m13 * (m21 * m32 - m22 * m31))

    D = determinan_3x3(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    if D == 0:
        raise ValueError("Determinan = 0, sistem tidak punya solusi tunggal")

    Dx = determinan_3x3(d1, b1, c1, d2, b2, c2, d3, b3, c3)
    Dy = determinan_3x3(a1, d1, c1, a2, d2, c2, a3, d3, c3)
    Dz = determinan_3x3(a1, b1, d1, a2, b2, d2, a3, b3, d3)

    return (Dx / D, Dy / D, Dz / D)

def kuadrat_diskriminan(a: float, b: float, c: float) -> float:
    """
    Bentuk: ax² + bx + c = 0
    """
    return b ** 2 - 4 * a * c


def kuadrat_akar(a: float, b: float, c: float) -> tuple:
    """
    Rumus ABC. Mengembalikan (x1, x2).
    Jika diskriminan < 0, akar berupa bilangan kompleks (dikembalikan sebagai complex).
    """
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0 (bukan persamaan kuadrat)")

    d = kuadrat_diskriminan(a, b, c)

    if d >= 0:
        akar_d = math.sqrt(d)
        x1 = (-b + akar_d) / (2 * a)
        x2 = (-b - akar_d) / (2 * a)
    else:
        akar_d = complex(0, math.sqrt(-d))
        x1 = (-b + akar_d) / (2 * a)
        x2 = (-b - akar_d) / (2 * a)

    return (x1, x2)

def kuadrat_jenis_akar(a: float, b: float, c: float) -> str:
    """
    Menentukan jenis akar berdasarkan diskriminan.
    """
    d = kuadrat_diskriminan(a, b, c)
    if d > 0:
        return "dua akar real berbeda"
    elif d == 0:
        return "dua akar real kembar (sama)"
    else:
        return "tidak ada akar real (akar kompleks/imajiner)"


def kuadrat_sumbu_simetri(a: float, b: float) -> float:
    """
    Sumbu simetri parabola: x = -b / 2a
    """
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")
    return -b / (2 * a)


def kuadrat_titik_puncak(a: float, b: float, c: float) -> tuple:
    """
    Titik puncak (vertex) parabola. Mengembalikan (x, y).
    """
    x = kuadrat_sumbu_simetri(a, b)
    y = a * x ** 2 + b * x + c
    return (x, y)


def kuadrat_jumlah_akar(a: float, b: float) -> float:
    """
    x1 + x2 = -b/a
    """
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")
    return -b / a


def kuadrat_hasil_kali_akar(a: float, c: float) -> float:
    """
    x1 * x2 = c/a
    """
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")
    return c / a

def pertidaksamaan_linear_solusi(a: float, b: float) -> float:
    """
    Bentuk: ax + b > 0 (atau <, >=, <=)
    Mengembalikan batas nilai x (tanda pertidaksamaan harus dicek manual,
    karena kalau dibagi bilangan negatif tanda pertidaksamaan berbalik)
    """
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")
    return -b / a

def pertidaksamaan_kuadrat_akar(a: float, b: float, c: float) -> tuple:
    """
    Mencari titik-titik batas (akar) buat pertidaksamaan kuadrat.
    Interval solusi ditentukan manual berdasarkan tanda pertidaksamaan
    dan apakah parabola terbuka ke atas (a>0) atau ke bawah (a<0).
    """
    return kuadrat_akar(a, b, c)

def fungsi_linear(m: float, x: float, c: float) -> float:
    """
    Bentuk: f(x) = mx + c
    """
    return m * x + c


def fungsi_linear_gradien(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Mencari gradien (m) dari 2 titik
    """
    if x2 - x1 == 0:
        raise ValueError("Garis vertikal, gradien tidak terdefinisi")
    return (y2 - y1) / (x2 - x1)

def fungsi_kuadrat(a: float, b: float, c: float, x: float) -> float:
    """
    Bentuk: f(x) = ax² + bx + c
    """
    return a * x ** 2 + b * x + c


def fungsi_eksponen(a: float, basis: float, x: float) -> float:
    """
    Bentuk: f(x) = a * basis^x
    """
    return a * (basis ** x)


def fungsi_logaritma(nilai: float, basis: float) -> float:
    """
    Bentuk: log basis dari nilai
    """
    if nilai <= 0:
        raise ValueError("Nilai harus lebih besar dari 0")
    if basis <= 0 or basis == 1:
        raise ValueError("Basis harus lebih besar dari 0 dan tidak boleh 1")
    return math.log(nilai, basis)


def fpb(a: int, b: int) -> int:
    """
    Faktor Persekutuan Terbesar (FPB) — algoritma Euclidean
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def kpk(a: int, b: int) -> int:
    """
    Kelipatan Persekutuan Terkecil (KPK)
    """
    return abs(a * b) // fpb(a, b)

import math
from fractions import Fraction

def pertidaksamaan_linear_interval(a: float, b: float, tanda: str) -> str:
    """
    Bentuk: ax + b [tanda] 0
    tanda -> '>', '<', '>=', '<='
    Otomatis membalik tanda kalau dibagi bilangan negatif.
    """
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")

    batas = -b / a
    tanda_final = tanda

    if a < 0:
        pembalikan = {'>': '<', '<': '>', '>=': '<=', '<=': '>='}
        tanda_final = pembalikan[tanda]

    return f"x {tanda_final} {batas}"


def pertidaksamaan_kuadrat_interval(a: float, b: float, c: float, tanda: str) -> str:
    """
    Bentuk: ax² + bx + c [tanda] 0
    tanda -> '>', '<', '>=', '<='
    Menentukan interval solusi berdasarkan akar-akar dan arah parabola.
    """
    d = b ** 2 - 4 * a * c

    if d < 0:

        if a > 0:
            selalu_positif = True
        else:
            selalu_positif = False

        if tanda in ('>', '>='):
            return "semua bilangan real (x ∈ R)" if selalu_positif else "tidak ada solusi (himpunan kosong)"
        else:
            return "tidak ada solusi (himpunan kosong)" if selalu_positif else "semua bilangan real (x ∈ R)"

    akar_d = math.sqrt(d)
    x1 = (-b - akar_d) / (2 * a)
    x2 = (-b + akar_d) / (2 * a)
    x_kecil, x_besar = min(x1, x2), max(x1, x2)

    parabola_ke_atas = a > 0

    if tanda in ('>', '>='):
        if parabola_ke_atas:
            return f"x < {x_kecil} atau x > {x_besar}" if tanda == '>' else f"x <= {x_kecil} atau x >= {x_besar}"
        else:
            return f"{x_kecil} < x < {x_besar}" if tanda == '>' else f"{x_kecil} <= x <= {x_besar}"
    else:
        if parabola_ke_atas:
            return f"{x_kecil} < x < {x_besar}" if tanda == '<' else f"{x_kecil} <= x <= {x_besar}"
        else:
            return f"x < {x_kecil} atau x > {x_besar}" if tanda == '<' else f"x <= {x_kecil} atau x >= {x_besar}"

def nilai_mutlak(x: float) -> float:
    return abs(x)


def persamaan_nilai_mutlak(a: float, b: float, c: float) -> tuple:
    """
    Bentuk: |ax + b| = c
    Mengembalikan (x1, x2)
    """
    if c < 0:
        raise ValueError("Tidak ada solusi karena nilai mutlak tidak bisa negatif")
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")

    x1 = (c - b) / a
    x2 = (-c - b) / a
    return (x1, x2)


def pertidaksamaan_nilai_mutlak_kurang_dari(a: float, b: float, c: float) -> str:
    """
    Bentuk: |ax + b| < c  ->  -c < ax + b < c
    """
    if c <= 0:
        return "tidak ada solusi (himpunan kosong)"
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")

    batas1 = (-c - b) / a
    batas2 = (c - b) / a
    x_kecil, x_besar = min(batas1, batas2), max(batas1, batas2)
    return f"{x_kecil} < x < {x_besar}"


def pertidaksamaan_nilai_mutlak_lebih_dari(a: float, b: float, c: float) -> str:
    """
    Bentuk: |ax + b| > c  ->  ax+b < -c  atau  ax+b > c
    """
    if c < 0:
        return "semua bilangan real (x ∈ R)"
    if a == 0:
        raise ValueError("Koefisien 'a' tidak boleh 0")

    batas1 = (-c - b) / a
    batas2 = (c - b) / a
    x_kecil, x_besar = min(batas1, batas2), max(batas1, batas2)
    return f"x < {x_kecil} atau x > {x_besar}"


def polinomial_tambah(p1: list, p2: list) -> list:
    """
    Polinomial direpresentasikan sebagai list koefisien, dari pangkat tertinggi ke terendah.
    Contoh: 3x² + 2x + 1 -> [3, 2, 1]
    """
    panjang = max(len(p1), len(p2))
    p1_pad = [0] * (panjang - len(p1)) + p1
    p2_pad = [0] * (panjang - len(p2)) + p2
    return [a + b for a, b in zip(p1_pad, p2_pad)]


def polinomial_kurang(p1: list, p2: list) -> list:
    panjang = max(len(p1), len(p2))
    p1_pad = [0] * (panjang - len(p1)) + p1
    p2_pad = [0] * (panjang - len(p2)) + p2
    return [a - b for a, b in zip(p1_pad, p2_pad)]


def polinomial_kali(p1: list, p2: list) -> list:
    """
    Perkalian dua polinomial (distributif/konvolusi koefisien)
    """
    hasil = [0] * (len(p1) + len(p2) - 1)
    for i, a in enumerate(p1):
        for j, b in enumerate(p2):
            hasil[i + j] += a * b
    return hasil


def polinomial_evaluasi(p: list, x: float) -> float:
    """
    Menghitung nilai polinomial pada suatu x (metode Horner)
    """
    hasil = 0
    for koef in p:
        hasil = hasil * x + koef
    return hasil


def polinomial_bagi_horner(p: list, akar: float) -> tuple:
    """
    Pembagian polinomial dengan (x - akar) menggunakan metode Horner.
    Mengembalikan (hasil_bagi, sisa)
    """
    hasil_bagi = []
    sisa = p[0]
    hasil_bagi.append(sisa)
    for koef in p[1:]:
        sisa = sisa * akar + koef
        hasil_bagi.append(sisa)
    sisa_akhir = hasil_bagi.pop()
    return (hasil_bagi, sisa_akhir)

def faktor_selisih_kuadrat(a: float, b: float) -> str:
    """
    Bentuk: a²x² - b²  ->  (ax-b)(ax+b)
    Menerima nilai akar dari a² dan b² (bukan a², b² langsung)
    """
    return f"({a}x - {b})({a}x + {b})"


def faktor_trinomial(a: float, b: float, c: float) -> str:
    """
    Bentuk: ax² + bx + c
    Mencari faktor menggunakan akar-akar (rumus ABC), lalu ubah ke bentuk perkalian.
    """
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "Tidak bisa difaktorkan dalam bilangan real (diskriminan negatif)"

    akar_d = math.sqrt(d)
    x1 = (-b + akar_d) / (2 * a)
    x2 = (-b - akar_d) / (2 * a)

    return f"{a}(x - ({x1}))(x - ({x2}))"



def fungsi_kubik(a: float, b: float, c: float, d: float, x: float) -> float:
    """
    Bentuk: f(x) = ax³ + bx² + cx + d
    """
    return a * x ** 3 + b * x ** 2 + c * x + d



def komposisi_fungsi(f, g, x: float) -> float:
    """
    Menghitung (f∘g)(x) = f(g(x))
    f dan g berupa function Python (bisa pakai lambda)
    Contoh: komposisi_fungsi(lambda x: x+1, lambda x: x*2, 3) -> f(g(3)) = f(6) = 7
    """
    return f(g(x))

def fungsi_linear_invers(m: float, c: float) -> tuple:
    """
    Dari f(x) = mx + c, mencari f⁻¹(x) = (x - c)/m
    Mengembalikan (koefisien_x, konstanta) dari bentuk invers
    """
    if m == 0:
        raise ValueError("Gradien 'm' tidak boleh 0 (fungsi tidak punya invers)")
    return (1 / m, -c / m)


def fungsi_rasional_evaluasi(pembilang: list, penyebut: list, x: float) -> float:
    """
    f(x) = p(x) / q(x), p dan q berupa list koefisien polinomial
    """
    nilai_penyebut = polinomial_evaluasi(penyebut, x)
    if nilai_penyebut == 0:
        raise ValueError(f"x = {x} membuat penyebut menjadi 0 (di luar domain)")
    nilai_pembilang = polinomial_evaluasi(pembilang, x)
    return nilai_pembilang / nilai_penyebut


def fungsi_rasional_domain_terlarang(penyebut: list) -> list:
    """
    Mencari nilai x yang membuat penyebut = 0 (harus dikeluarkan dari domain).
    Hanya mendukung penyebut derajat 1 atau 2.
    """
    if len(penyebut) == 2:
        a, b = penyebut
        if a == 0:
            return []
        return [-b / a]
    elif len(penyebut) == 3:
        a, b, c = penyebut
        d = b ** 2 - 4 * a * c
        if d < 0:
            return []
        elif d == 0:
            return [-b / (2 * a)]
        else:
            akar_d = math.sqrt(d)
            return [(-b + akar_d) / (2 * a), (-b - akar_d) / (2 * a)]
    else:
        raise ValueError("Hanya mendukung penyebut derajat 1 atau 2")



def suku_ke_n_dari_fungsi(fungsi, n: int):
    """
    Menghitung Un = f(n) dari fungsi yang diberikan.
    Contoh: suku_ke_n_dari_fungsi(lambda n: 2*n + 1, 5) -> 11
    """
    return fungsi(n)


def program_linear_titik_potong(a1: float, b1: float, c1: float,
                                  a2: float, b2: float, c2: float) -> tuple:
    """
    Mencari titik potong dua garis batas (dari pertidaksamaan linear dua variabel)
    a1*x + b1*y = c1
    a2*x + b2*y = c2
    Berguna untuk mencari titik pojok daerah himpunan penyelesaian.
    """
    determinan = (a1 * b2) - (a2 * b1)
    if determinan == 0:
        raise ValueError("Kedua garis sejajar, tidak ada titik potong")

    x = ((c1 * b2) - (c2 * b1)) / determinan
    y = ((a1 * c2) - (a2 * c1)) / determinan
    return (x, y)


def program_linear_nilai_optimum(fungsi_objektif, titik_titik_pojok: list) -> dict:
    """
    Mencari nilai maksimum & minimum dari fungsi objektif di beberapa titik pojok.
    fungsi_objektif -> function (x, y) -> nilai, misal lambda x, y: 3*x + 5*y
    titik_titik_pojok -> list of tuple (x, y)
    """
    hasil = [(titik, fungsi_objektif(titik[0], titik[1])) for titik in titik_titik_pojok]
    maksimum = max(hasil, key=lambda item: item[1])
    minimum = min(hasil, key=lambda item: item[1])
    return {"maksimum": maksimum, "minimum": minimum, "semua_titik": hasil}