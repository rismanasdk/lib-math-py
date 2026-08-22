import math
from collections import Counter

def mean(data: list) -> float:
    """
    Rata-rata (mean)
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    return sum(data) / len(data)


def median(data: list) -> float:
    """
    Nilai tengah setelah data diurutkan
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    data_urut = sorted(data)
    n = len(data_urut)
    tengah = n // 2
    if n % 2 == 0:
        return (data_urut[tengah - 1] + data_urut[tengah]) / 2
    return data_urut[tengah]


def modus(data: list) -> list:
    """
    Nilai yang paling sering muncul. Bisa lebih dari satu (multimodal).
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    hitung = Counter(data)
    frekuensi_max = max(hitung.values())
    return [nilai for nilai, freq in hitung.items() if freq == frekuensi_max]


def jangkauan(data: list) -> float:
    """
    Range = nilai maksimum - nilai minimum
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    return max(data) - min(data)


def ragam_populasi(data: list) -> float:
    """
    Variansi populasi (dibagi n)
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    rata = mean(data)
    return sum((x - rata) ** 2 for x in data) / len(data)


def ragam_sampel(data: list) -> float:
    """
    Variansi sampel (dibagi n-1, Bessel's correction)
    """
    if len(data) < 2:
        raise ValueError("Data minimal harus 2 nilai untuk ragam sampel")
    rata = mean(data)
    return sum((x - rata) ** 2 for x in data) / (len(data) - 1)


def simpangan_baku_populasi(data: list) -> float:
    """
    Standar deviasi populasi
    """
    return math.sqrt(ragam_populasi(data))


def simpangan_baku_sampel(data: list) -> float:
    """
    Standar deviasi sampel
    """
    return math.sqrt(ragam_sampel(data))


def simpangan_rata_rata(data: list) -> float:
    """
    Mean Absolute Deviation (MAD) = rata-rata dari |x - mean|
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    rata = mean(data)
    return sum(abs(x - rata) for x in data) / len(data)


def _posisi_data(data_urut: list, persen: float) -> float:
    """
    Fungsi bantu: mencari nilai pada posisi persentase tertentu (interpolasi linear)
    """
    n = len(data_urut)
    posisi = persen * (n - 1)
    posisi_bawah = int(math.floor(posisi))
    posisi_atas = int(math.ceil(posisi))
    if posisi_bawah == posisi_atas:
        return data_urut[posisi_bawah]
    proporsi = posisi - posisi_bawah
    return data_urut[posisi_bawah] + proporsi * (data_urut[posisi_atas] - data_urut[posisi_bawah])


def kuartil(data: list, k: int) -> float:
    """
    k = 1 (Q1/kuartil bawah), 2 (Q2/median), 3 (Q3/kuartil atas)
    """
    if k not in (1, 2, 3):
        raise ValueError("k harus 1, 2, atau 3")
    if not data:
        raise ValueError("Data tidak boleh kosong")
    data_urut = sorted(data)
    return _posisi_data(data_urut, k / 4)


def desil(data: list, d: int) -> float:
    """
    d = 1 sampai 9
    """
    if not (1 <= d <= 9):
        raise ValueError("d harus di antara 1 dan 9")
    if not data:
        raise ValueError("Data tidak boleh kosong")
    data_urut = sorted(data)
    return _posisi_data(data_urut, d / 10)


def persentil(data: list, p: int) -> float:
    """
    p = 1 sampai 99
    """
    if not (1 <= p <= 99):
        raise ValueError("p harus di antara 1 dan 99")
    if not data:
        raise ValueError("Data tidak boleh kosong")
    data_urut = sorted(data)
    return _posisi_data(data_urut, p / 100)


def jangkauan_interkuartil(data: list) -> float:
    """
    IQR = Q3 - Q1
    """
    return kuartil(data, 3) - kuartil(data, 1)

def distribusi_frekuensi(data: list) -> dict:
    """
    Menghitung frekuensi kemunculan tiap nilai unik.
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    return dict(Counter(data))


def distribusi_frekuensi_relatif(data: list) -> dict:
    """
    Frekuensi relatif = frekuensi / total data (dalam persen)
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    total = len(data)
    hitung = Counter(data)
    return {nilai: (freq / total) * 100 for nilai, freq in hitung.items()}


def distribusi_frekuensi_kumulatif(data: list) -> dict:
    """
    Frekuensi kumulatif (menaik) berdasarkan nilai yang sudah diurutkan.
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    nilai_unik = sorted(set(data))
    hitung = Counter(data)
    kumulatif = 0
    hasil = {}
    for nilai in nilai_unik:
        kumulatif += hitung[nilai]
        hasil[nilai] = kumulatif
    return hasil


def koefisien_kemiringan_pearson(data: list) -> float:
    """
    Skewness (Pearson's first coefficient) = 3*(mean - median) / simpangan_baku
    > 0 -> condong kanan, < 0 -> condong kiri, = 0 -> simetris
    """
    sb = simpangan_baku_sampel(data)
    if sb == 0:
        raise ValueError("Simpangan baku = 0, tidak bisa menghitung kemiringan")
    return 3 * (mean(data) - median(data)) / sb


def z_score(nilai: float, rata_rata: float, simpangan_baku: float) -> float:
    """
    Mengukur seberapa jauh sebuah nilai dari rata-rata (dalam satuan simpangan baku)
    """
    if simpangan_baku == 0:
        raise ValueError("Simpangan baku tidak boleh 0")
    return (nilai - rata_rata) / simpangan_baku


def koefisien_variasi(data: list) -> float:
    """
    CV = (simpangan baku / mean) * 100%
    Berguna untuk membandingkan variabilitas antar dataset dengan skala berbeda
    """
    rata = mean(data)
    if rata == 0:
        raise ValueError("Mean tidak boleh 0")
    return (simpangan_baku_sampel(data) / rata) * 100

def korelasi_pearson(data_x: list, data_y: list) -> float:
    """
    Koefisien korelasi Pearson (r), rentang -1 sampai 1
    """
    if len(data_x) != len(data_y):
        raise ValueError("Panjang data_x dan data_y harus sama")
    n = len(data_x)
    if n < 2:
        raise ValueError("Minimal 2 pasang data")

    mean_x, mean_y = mean(data_x), mean(data_y)
    numerator = sum((data_x[i] - mean_x) * (data_y[i] - mean_y) for i in range(n))
    denom_x = math.sqrt(sum((x - mean_x) ** 2 for x in data_x))
    denom_y = math.sqrt(sum((y - mean_y) ** 2 for y in data_y))

    if denom_x == 0 or denom_y == 0:
        raise ValueError("Tidak bisa menghitung korelasi (variansi = 0)")

    return numerator / (denom_x * denom_y)


def regresi_linear(data_x: list, data_y: list) -> tuple:
    """
    Regresi linear sederhana: y = mx + c
    Mengembalikan (m, c) menggunakan metode least squares
    """
    if len(data_x) != len(data_y):
        raise ValueError("Panjang data_x dan data_y harus sama")
    n = len(data_x)
    if n < 2:
        raise ValueError("Minimal 2 pasang data")

    mean_x, mean_y = mean(data_x), mean(data_y)
    numerator = sum((data_x[i] - mean_x) * (data_y[i] - mean_y) for i in range(n))
    denominator = sum((x - mean_x) ** 2 for x in data_x)

    if denominator == 0:
        raise ValueError("Tidak bisa menghitung regresi (semua data_x sama)")

    m = numerator / denominator
    c = mean_y - m * mean_x
    return (m, c)


def regresi_linear_prediksi(m: float, c: float, x: float) -> float:
    """
    Memprediksi nilai y dari model regresi linear y = mx + c
    """
    return m * x + c

def rata_rata_tertimbang(data: list, bobot: list) -> float:
    """
    Weighted Mean = Σ(x*w) / Σw
    """
    if len(data) != len(bobot):
        raise ValueError("Panjang data dan bobot harus sama")
    if sum(bobot) == 0:
        raise ValueError("Total bobot tidak boleh 0")
    return sum(x * w for x, w in zip(data, bobot)) / sum(bobot)


def rata_rata_geometrik(data: list) -> float:
    """
    Geometric Mean = ⁿ√(x1*x2*...*xn)
    Hanya untuk data positif.
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    if any(x <= 0 for x in data):
        raise ValueError("Semua data harus bernilai positif")
    hasil_kali = 1
    for x in data:
        hasil_kali *= x
    return hasil_kali ** (1 / len(data))


def rata_rata_harmonik(data: list) -> float:
    """
    Harmonic Mean = n / Σ(1/x)
    Hanya untuk data positif (tidak boleh 0).
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    if any(x == 0 for x in data):
        raise ValueError("Data tidak boleh mengandung nilai 0")
    return len(data) / sum(1 / x for x in data)

def mean_data_berkelompok(titik_tengah: list, frekuensi: list) -> float:
    """
    Mean dari data berkelompok.
    titik_tengah -> nilai tengah tiap kelas interval
    frekuensi -> frekuensi tiap kelas
    """
    if len(titik_tengah) != len(frekuensi):
        raise ValueError("Panjang titik_tengah dan frekuensi harus sama")
    total_frekuensi = sum(frekuensi)
    if total_frekuensi == 0:
        raise ValueError("Total frekuensi tidak boleh 0")
    return sum(tt * f for tt, f in zip(titik_tengah, frekuensi)) / total_frekuensi


def median_data_berkelompok(tepi_bawah_kelas_median: float, frekuensi_kumulatif_sebelum: int,
                              frekuensi_kelas_median: int, panjang_kelas: float,
                              total_frekuensi: int) -> float:
    """
    Median = TepiBawah + ((n/2 - F) / f) * panjang_kelas
    tepi_bawah_kelas_median -> tepi bawah kelas yang memuat median
    frekuensi_kumulatif_sebelum -> frekuensi kumulatif sebelum kelas median (F)
    frekuensi_kelas_median -> frekuensi kelas median itu sendiri (f)
    """
    if frekuensi_kelas_median == 0:
        raise ValueError("Frekuensi kelas median tidak boleh 0")
    return tepi_bawah_kelas_median + (((total_frekuensi / 2) - frekuensi_kumulatif_sebelum) / frekuensi_kelas_median) * panjang_kelas


def modus_data_berkelompok(tepi_bawah_kelas_modus: float, selisih_frekuensi_sebelum: float,
                             selisih_frekuensi_sesudah: float, panjang_kelas: float) -> float:
    """
    Modus = TepiBawah + (d1 / (d1+d2)) * panjang_kelas
    selisih_frekuensi_sebelum (d1) -> frekuensi kelas modus - frekuensi kelas sebelumnya
    selisih_frekuensi_sesudah (d2) -> frekuensi kelas modus - frekuensi kelas sesudahnya
    """
    total_selisih = selisih_frekuensi_sebelum + selisih_frekuensi_sesudah
    if total_selisih == 0:
        raise ValueError("Total selisih frekuensi tidak boleh 0")
    return tepi_bawah_kelas_modus + (selisih_frekuensi_sebelum / total_selisih) * panjang_kelas



def momen_ke_n(data: list, n: int) -> float:
    """
    Momen ke-n terhadap mean = Σ(x-mean)ⁿ / total_data
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")
    rata = mean(data)
    return sum((x - rata) ** n for x in data) / len(data)


def kurtosis(data: list) -> float:
    """
    Kurtosis = momen ke-4 / (simpangan baku)⁴ - 3 (excess kurtosis)
    > 0 -> leptokurtik (puncak lebih runcing), < 0 -> platikurtik (lebih datar)
    """
    sb = simpangan_baku_populasi(data)
    if sb == 0:
        raise ValueError("Simpangan baku = 0, tidak bisa menghitung kurtosis")
    m4 = momen_ke_n(data, 4)
    return (m4 / (sb ** 4)) - 3

def kovariansi(data_x: list, data_y: list) -> float:
    """
    Covariance = Σ(x-mean_x)(y-mean_y) / (n-1)
    Mengukur arah hubungan linear antar 2 variabel (positif/negatif)
    """
    if len(data_x) != len(data_y):
        raise ValueError("Panjang data_x dan data_y harus sama")
    n = len(data_x)
    if n < 2:
        raise ValueError("Minimal 2 pasang data")
    mean_x, mean_y = mean(data_x), mean(data_y)
    return sum((data_x[i] - mean_x) * (data_y[i] - mean_y) for i in range(n)) / (n - 1)