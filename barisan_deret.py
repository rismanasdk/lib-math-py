def barisan_aritmatika(suku_pertama: int, perbedaan: int, suku_N):
    return suku_pertama + (suku_N - 1) * perbedaan

def deret_aritmatika(jumlah_suku_N: int, suku_pertama: int, perbedaan: int) -> float:
    return jumlah_suku_N/2 * (2 * suku_pertama + (jumlah_suku_N - 1) * perbedaan)

def barisan_geometri(suku_pertama: int, rasio: int, suku_N) -> float:
    return suku_pertama * rasio ** (suku_N - 1)

def deret_geometri(jumlah_suku_N: int, suku_pertama: int, rasio: int) -> float:
    """
    Menghitung jumlah n suku pertama deret geometri.
    - rasio == 1  -> semua suku sama, tinggal dikali n
    - rasio > 1   -> pakai rumus rasio positif
    - rasio < 1   -> pakai rumus rasio negatif/pecahan 
    """
    if rasio == 1:
        hasil_akhir = suku_pertama * jumlah_suku_N
    elif rasio > 1:
        hasil_akhir = suku_pertama * (rasio ** jumlah_suku_N - 1) / (rasio - 1)
    else:
        hasil_akhir = suku_pertama * (1 - rasio ** jumlah_suku_N) / (1 - rasio)
    return hasil_akhir


def deret_geometri_infinity(suku_pertama: float, rasio: float) -> float:
    """
    Menghitung jumlah tak hingga deret geometri.
    Syarat konvergen: -1 < rasio < 1 (di luar itu deret gak punya jumlah tak hingga).
    """
    if not (-1 < rasio < 1):
        raise ValueError(
            "Rasio harus di antara -1 dan 1 (tidak termasuk keduanya) supaya deret konvergen."
        )
    return suku_pertama / (1 - rasio)

def barisan_fibonacci(suku_N: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if suku_N <= 0:
        return 0
    if suku_N == 1:
        return 1
    if suku_N in memo:
        return memo[suku_N]
    memo[suku_N] = barisan_fibonacci(suku_N - 1, memo) + barisan_fibonacci(suku_N - 2, memo)
    return memo[suku_N]

def deret_bilangan_asli(suku_N: int) -> float:
    """
    Hanya bilangan positif
    """
    if suku_N < 1:
        raise ValueError("Tidak bisa kurang dari 1 atau negatif")
    else:
        return suku_N * (suku_N + 1) / 2

def deret_bilangan_kuadrat(suku_N: int) -> float:
    """
    Hanya bilangan positif
    """
    if suku_N < 1:
        raise ValueError("Tidak bisa kurang dari 1 atau negatif")
    else:
        return suku_N * (suku_N + 1) * (2 * suku_N + 1) / 6

def deret_pangkat_tiga(suku_N: int) -> float:
    """
    Hanya bilangan positif
    """
    if suku_N < 1:
        raise ValueError("Tidak bisa kurang dari 1 atau negatif")
    else:
        return (suku_N * (suku_N + 1)/2) ** 2
