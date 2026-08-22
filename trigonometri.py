import math

def sin_derajat(sudut: float) -> float:
    return math.sin(math.radians(sudut))


def cos_derajat(sudut: float) -> float:
    return math.cos(math.radians(sudut))


def tan_derajat(sudut: float) -> float:
    return math.tan(math.radians(sudut))

def csc_derajat(sudut: float) -> float:
    """
    Cosecant = 1/sin
    """
    nilai_sin = sin_derajat(sudut)
    if nilai_sin == 0:
        raise ValueError("Cosecant tidak terdefinisi (sin = 0)")
    return 1 / nilai_sin


def sec_derajat(sudut: float) -> float:
    """
    Secant = 1/cos
    """
    nilai_cos = cos_derajat(sudut)
    if nilai_cos == 0:
        raise ValueError("Secant tidak terdefinisi (cos = 0)")
    return 1 / nilai_cos


def cot_derajat(sudut: float) -> float:
    """
    Cotangent = 1/tan
    """
    nilai_tan = tan_derajat(sudut)
    if nilai_tan == 0:
        raise ValueError("Cotangent tidak terdefinisi (tan = 0)")
    return 1 / nilai_tan

def arcsin_derajat(nilai: float) -> float:
    if not (-1 <= nilai <= 1):
        raise ValueError("Nilai harus di antara -1 dan 1")
    return math.degrees(math.asin(nilai))


def arccos_derajat(nilai: float) -> float:
    if not (-1 <= nilai <= 1):
        raise ValueError("Nilai harus di antara -1 dan 1")
    return math.degrees(math.acos(nilai))


def arctan_derajat(nilai: float) -> float:
    return math.degrees(math.atan(nilai))

def derajat_ke_radian(derajat: float) -> float:
    return math.radians(derajat)


def radian_ke_derajat(radian: float) -> float:
    return math.degrees(radian)

def aturan_sinus_sisi(sisi_diketahui: float, sudut_depan_sisi_diketahui: float,
                       sudut_depan_sisi_dicari: float) -> float:
    """
    a/sin(A) = b/sin(B)  ->  mencari sisi b
    """
    sin_a = sin_derajat(sudut_depan_sisi_diketahui)
    if sin_a == 0:
        raise ValueError("sin(sudut) tidak boleh 0")
    return (sisi_diketahui / sin_a) * sin_derajat(sudut_depan_sisi_dicari)


def aturan_sinus_sudut(sisi_a: float, sudut_a: float, sisi_b: float) -> float:
    """
    Mencari sudut B dari a/sin(A) = b/sin(B)
    """
    sin_a = sin_derajat(sudut_a)
    hasil = (sisi_b * sin_a) / sisi_a
    if not (-1 <= hasil <= 1):
        raise ValueError("Tidak ada solusi segitiga yang valid (nilai sin di luar rentang)")
    return arcsin_derajat(hasil)



def aturan_cosinus_sisi(sisi_b: float, sisi_c: float, sudut_a: float) -> float:
    """
    a² = b² + c² - 2bc*cos(A)  ->  mencari sisi a
    """
    cos_a = cos_derajat(sudut_a)
    a_kuadrat = sisi_b ** 2 + sisi_c ** 2 - 2 * sisi_b * sisi_c * cos_a
    if a_kuadrat < 0:
        raise ValueError("Tidak ada solusi segitiga yang valid")
    return math.sqrt(a_kuadrat)


def aturan_cosinus_sudut(sisi_a: float, sisi_b: float, sisi_c: float) -> float:
    """
    Mencari sudut A dari cos(A) = (b² + c² - a²) / (2bc)
    """
    nilai_cos = (sisi_b ** 2 + sisi_c ** 2 - sisi_a ** 2) / (2 * sisi_b * sisi_c)
    if not (-1 <= nilai_cos <= 1):
        raise ValueError("Tidak ada solusi segitiga yang valid (bukan segitiga sah)")
    return arccos_derajat(nilai_cos)



def luas_segitiga_dua_sisi_sudut(sisi_a: float, sisi_b: float, sudut_c: float) -> float:
    """
    Luas = 1/2 * a * b * sin(C)
    """
    return 0.5 * sisi_a * sisi_b * sin_derajat(sudut_c)



def identitas_pythagoras_cek(sudut: float) -> float:
    """
    sin²(x) + cos²(x) harus selalu = 1
    Berguna untuk verifikasi/testing
    """
    return sin_derajat(sudut) ** 2 + cos_derajat(sudut) ** 2


def sin_jumlah_dua_sudut(sudut_a: float, sudut_b: float) -> float:
    """
    sin(A+B) = sin(A)cos(B) + cos(A)sin(B)
    """
    return sin_derajat(sudut_a) * cos_derajat(sudut_b) + cos_derajat(sudut_a) * sin_derajat(sudut_b)


def cos_jumlah_dua_sudut(sudut_a: float, sudut_b: float) -> float:
    """
    cos(A+B) = cos(A)cos(B) - sin(A)sin(B)
    """
    return cos_derajat(sudut_a) * cos_derajat(sudut_b) - sin_derajat(sudut_a) * sin_derajat(sudut_b)


def sin_selisih_dua_sudut(sudut_a: float, sudut_b: float) -> float:
    """
    sin(A-B) = sin(A)cos(B) - cos(A)sin(B)
    """
    return sin_derajat(sudut_a) * cos_derajat(sudut_b) - cos_derajat(sudut_a) * sin_derajat(sudut_b)


def cos_selisih_dua_sudut(sudut_a: float, sudut_b: float) -> float:
    """
    cos(A-B) = cos(A)cos(B) + sin(A)sin(B)
    """
    return cos_derajat(sudut_a) * cos_derajat(sudut_b) + sin_derajat(sudut_a) * sin_derajat(sudut_b)


def sin_sudut_rangkap(sudut: float) -> float:
    """
    sin(2x) = 2sin(x)cos(x)
    """
    return 2 * sin_derajat(sudut) * cos_derajat(sudut)


def cos_sudut_rangkap(sudut: float) -> float:
    """
    cos(2x) = cos²(x) - sin²(x)
    """
    return cos_derajat(sudut) ** 2 - sin_derajat(sudut) ** 2


def tan_jumlah_dua_sudut(sudut_a: float, sudut_b: float) -> float:
    """
    tan(A+B) = (tan(A) + tan(B)) / (1 - tan(A)*tan(B))
    """
    tan_a, tan_b = tan_derajat(sudut_a), tan_derajat(sudut_b)
    penyebut = 1 - tan_a * tan_b
    if penyebut == 0:
        raise ValueError("Tidak terdefinisi (penyebut = 0)")
    return (tan_a + tan_b) / penyebut


def tan_selisih_dua_sudut(sudut_a: float, sudut_b: float) -> float:
    """
    tan(A-B) = (tan(A) - tan(B)) / (1 + tan(A)*tan(B))
    """
    tan_a, tan_b = tan_derajat(sudut_a), tan_derajat(sudut_b)
    penyebut = 1 + tan_a * tan_b
    if penyebut == 0:
        raise ValueError("Tidak terdefinisi (penyebut = 0)")
    return (tan_a - tan_b) / penyebut



def tan_sudut_rangkap(sudut: float) -> float:
    """
    tan(2x) = 2tan(x) / (1 - tan²(x))
    """
    tan_x = tan_derajat(sudut)
    penyebut = 1 - tan_x ** 2
    if penyebut == 0:
        raise ValueError("Tidak terdefinisi (penyebut = 0)")
    return (2 * tan_x) / penyebut


def sin_setengah_sudut(sudut: float, tanda_positif: bool = True) -> float:
    """
    sin(x/2) = ±√((1-cos(x))/2)
    tanda_positif -> tentukan apakah hasil (+) atau (-), tergantung kuadran x/2
    """
    nilai = (1 - cos_derajat(sudut)) / 2
    hasil = math.sqrt(nilai)
    return hasil if tanda_positif else -hasil


def cos_setengah_sudut(sudut: float, tanda_positif: bool = True) -> float:
    """
    cos(x/2) = ±√((1+cos(x))/2)
    """
    nilai = (1 + cos_derajat(sudut)) / 2
    hasil = math.sqrt(nilai)
    return hasil if tanda_positif else -hasil


def tan_setengah_sudut(sudut: float) -> float:
    """
    tan(x/2) = sin(x) / (1+cos(x))
    """
    penyebut = 1 + cos_derajat(sudut)
    if penyebut == 0:
        raise ValueError("Tidak terdefinisi (penyebut = 0)")
    return sin_derajat(sudut) / penyebut


def sin_kali_cos(sudut_a: float, sudut_b: float) -> float:
    """
    sin(A)cos(B) = 1/2 * [sin(A+B) + sin(A-B)]
    """
    return 0.5 * (sin_derajat(sudut_a + sudut_b) + sin_derajat(sudut_a - sudut_b))


def cos_kali_cos(sudut_a: float, sudut_b: float) -> float:
    """
    cos(A)cos(B) = 1/2 * [cos(A-B) + cos(A+B)]
    """
    return 0.5 * (cos_derajat(sudut_a - sudut_b) + cos_derajat(sudut_a + sudut_b))


def sin_kali_sin(sudut_a: float, sudut_b: float) -> float:
    """
    sin(A)sin(B) = 1/2 * [cos(A-B) - cos(A+B)]
    """
    return 0.5 * (cos_derajat(sudut_a - sudut_b) - cos_derajat(sudut_a + sudut_b))



def sin_tambah_sin(sudut_a: float, sudut_b: float) -> float:
    """
    sin(A) + sin(B) = 2 * sin((A+B)/2) * cos((A-B)/2)
    """
    return 2 * sin_derajat((sudut_a + sudut_b) / 2) * cos_derajat((sudut_a - sudut_b) / 2)


def sin_kurang_sin(sudut_a: float, sudut_b: float) -> float:
    """
    sin(A) - sin(B) = 2 * cos((A+B)/2) * sin((A-B)/2)
    """
    return 2 * cos_derajat((sudut_a + sudut_b) / 2) * sin_derajat((sudut_a - sudut_b) / 2)


def cos_tambah_cos(sudut_a: float, sudut_b: float) -> float:
    """
    cos(A) + cos(B) = 2 * cos((A+B)/2) * cos((A-B)/2)
    """
    return 2 * cos_derajat((sudut_a + sudut_b) / 2) * cos_derajat((sudut_a - sudut_b) / 2)


def cos_kurang_cos(sudut_a: float, sudut_b: float) -> float:
    """
    cos(A) - cos(B) = -2 * sin((A+B)/2) * sin((A-B)/2)
    """
    return -2 * sin_derajat((sudut_a + sudut_b) / 2) * sin_derajat((sudut_a - sudut_b) / 2)

def tinggi_dari_sudut_elevasi(jarak_horizontal: float, sudut_elevasi: float) -> float:
    """
    Mencari tinggi objek dari jarak horizontal & sudut elevasi (pandang ke atas)
    tinggi = jarak_horizontal * tan(sudut_elevasi)
    """
    return jarak_horizontal * tan_derajat(sudut_elevasi)


def jarak_dari_sudut_depresi(tinggi: float, sudut_depresi: float) -> float:
    """
    Mencari jarak horizontal dari tinggi objek & sudut depresi (pandang ke bawah)
    jarak = tinggi / tan(sudut_depresi)
    """
    tan_sudut = tan_derajat(sudut_depresi)
    if tan_sudut == 0:
        raise ValueError("Sudut depresi tidak boleh 0")
    return tinggi / tan_sudut


def fungsi_sin_nilai(amplitudo: float, periode_faktor: float, x: float,
                      pergeseran_fase: float = 0, pergeseran_vertikal: float = 0) -> float:
    """
    Bentuk umum: f(x) = amplitudo * sin(periode_faktor*(x - pergeseran_fase)) + pergeseran_vertikal
    """
    return amplitudo * sin_derajat(periode_faktor * (x - pergeseran_fase)) + pergeseran_vertikal


def fungsi_periode(periode_faktor: float) -> float:
    """
    Periode fungsi trigonometri = 360° / periode_faktor (dalam derajat)
    """
    if periode_faktor == 0:
        raise ValueError("Faktor periode tidak boleh 0")
    return 360 / periode_faktor