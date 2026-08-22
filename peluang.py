import math
from itertools import combinations, permutations



def faktorial(n: int) -> int:
    """
    n! = n * (n-1) * (n-2) * ... * 1
    """
    if n < 0:
        raise ValueError("n tidak boleh negatif")
    if n == 0:
        return 1
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil


def permutasi(n: int, r: int) -> int:
    """
    Permutasi r dari n objek (urutan penting): P(n,r) = n! / (n-r)!
    """
    if r > n:
        raise ValueError("r tidak boleh lebih besar dari n")
    if n < 0 or r < 0:
        raise ValueError("n dan r tidak boleh negatif")
    return faktorial(n) // faktorial(n - r)


def permutasi_siklis(n: int) -> int:
    """
    Permutasi siklis (melingkar) = (n-1)!
    """
    if n < 1:
        raise ValueError("n harus lebih besar dari 0")
    return faktorial(n - 1)


def permutasi_dengan_pengulangan(n: int, pengulangan: list) -> int:
    """
    Permutasi dengan elemen berulang: n! / (k1! * k2! * ... * km!)
    pengulangan -> list berisi jumlah masing-masing elemen yang sama/berulang
    """
    penyebut = 1
    for k in pengulangan:
        penyebut *= faktorial(k)
    return faktorial(n) // penyebut




def kombinasi(n: int, r: int) -> int:
    """
    Kombinasi r dari n objek (urutan tidak penting): C(n,r) = n! / (r!(n-r)!)
    """
    if r > n:
        raise ValueError("r tidak boleh lebih besar dari n")
    if n < 0 or r < 0:
        raise ValueError("n dan r tidak boleh negatif")
    return faktorial(n) // (faktorial(r) * faktorial(n - r))



def peluang_kejadian(banyak_kejadian_diharapkan: int, banyak_ruang_sampel: int) -> float:
    """
    P(A) = n(A) / n(S)
    """
    if banyak_ruang_sampel == 0:
        raise ValueError("Ruang sampel tidak boleh 0")
    if banyak_kejadian_diharapkan > banyak_ruang_sampel:
        raise ValueError("Kejadian diharapkan tidak boleh lebih besar dari ruang sampel")
    return banyak_kejadian_diharapkan / banyak_ruang_sampel


def peluang_komplemen(peluang_a: float) -> float:
    """
    P(A') = 1 - P(A)
    """
    if not (0 <= peluang_a <= 1):
        raise ValueError("Peluang harus di antara 0 dan 1")
    return 1 - peluang_a


def frekuensi_harapan(peluang: float, banyak_percobaan: int) -> float:
    """
    F(A) = P(A) * banyak percobaan
    """
    if not (0 <= peluang <= 1):
        raise ValueError("Peluang harus di antara 0 dan 1")
    return peluang * banyak_percobaan


def peluang_gabungan(peluang_a: float, peluang_b: float, peluang_irisan: float = 0) -> float:
    """
    P(A∪B) = P(A) + P(B) - P(A∩B)
    Jika kejadian saling lepas (mutually exclusive), peluang_irisan = 0
    """
    return peluang_a + peluang_b - peluang_irisan


def peluang_saling_lepas(peluang_a: float, peluang_b: float) -> float:
    """
    Untuk kejadian saling lepas (tidak mungkin terjadi bersamaan): P(A∪B) = P(A) + P(B)
    """
    return peluang_a + peluang_b


def peluang_kejadian_bebas(peluang_a: float, peluang_b: float) -> float:
    """
    Untuk kejadian saling bebas (independent): P(A∩B) = P(A) * P(B)
    """
    return peluang_a * peluang_b


def peluang_bersyarat(peluang_irisan_a_b: float, peluang_b: float) -> float:
    """
    P(A|B) = P(A∩B) / P(B)
    Peluang A terjadi dengan syarat B sudah terjadi
    """
    if peluang_b == 0:
        raise ValueError("P(B) tidak boleh 0")
    return peluang_irisan_a_b / peluang_b


def peluang_kejadian_tidak_bebas(peluang_a: float, peluang_b_dengan_syarat_a: float) -> float:
    """
    Untuk kejadian tidak bebas: P(A∩B) = P(A) * P(B|A)
    """
    return peluang_a * peluang_b_dengan_syarat_a


def teorema_bayes(peluang_b_dengan_syarat_a: float, peluang_a: float, peluang_b: float) -> float:
    """
    P(A|B) = [P(B|A) * P(A)] / P(B)
    """
    if peluang_b == 0:
        raise ValueError("P(B) tidak boleh 0")
    return (peluang_b_dengan_syarat_a * peluang_a) / peluang_b


def distribusi_binomial(n: int, x: int, p: float) -> float:
    """
    P(X=x) = C(n,x) * p^x * (1-p)^(n-x)
    n -> banyak percobaan, x -> banyak keberhasilan diharapkan, p -> peluang sukses tiap percobaan
    """
    if not (0 <= p <= 1):
        raise ValueError("p harus di antara 0 dan 1")
    if x > n or x < 0:
        raise ValueError("x harus di antara 0 dan n")
    return kombinasi(n, x) * (p ** x) * ((1 - p) ** (n - x))


def ekspektasi_binomial(n: int, p: float) -> float:
    """
    Nilai harapan (mean) distribusi binomial: E(X) = n*p
    """
    return n * p


def variansi_binomial(n: int, p: float) -> float:
    """
    Variansi distribusi binomial: Var(X) = n*p*(1-p)
    """
    return n * p * (1 - p)

def distribusi_poisson(lam: float, x: int) -> float:
    """
    P(X=x) = (λ^x * e^-λ) / x!
    lam -> rata-rata kejadian (lambda), x -> banyak kejadian yang dicari peluangnya
    """
    if lam < 0:
        raise ValueError("Lambda tidak boleh negatif")
    if x < 0:
        raise ValueError("x tidak boleh negatif")
    return ((lam ** x) * math.exp(-lam)) / faktorial(x)


def distribusi_normal_pdf(x: float, mean_val: float, simpangan_baku: float) -> float:
    """
    Probability Density Function distribusi normal (kurva lonceng)
    """
    if simpangan_baku <= 0:
        raise ValueError("Simpangan baku harus lebih besar dari 0")
    eksponen = -((x - mean_val) ** 2) / (2 * simpangan_baku ** 2)
    koefisien = 1 / (simpangan_baku * math.sqrt(2 * math.pi))
    return koefisien * math.exp(eksponen)


def distribusi_normal_z_ke_peluang(z: float) -> float:
    """
    Menghitung P(Z <= z) menggunakan fungsi error (CDF distribusi normal standar)
    """
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def kombinasi_dengan_pengulangan(n: int, r: int) -> int:
    """
    Kombinasi dengan pengulangan (multiset): C(n+r-1, r)
    Contoh: memilih r item dari n jenis, boleh pilih jenis yang sama berkali-kali
    """
    if n < 0 or r < 0:
        raise ValueError("n dan r tidak boleh negatif")
    return kombinasi(n + r - 1, r)


def distribusi_hipergeometrik(N: int, K: int, n: int, x: int) -> float:
    """
    Peluang tanpa pengembalian (berbeda dari binomial yang dengan pengembalian).
    N -> total populasi
    K -> banyak item "sukses" dalam populasi
    n -> banyak sampel yang diambil
    x -> banyak sukses yang diharapkan dalam sampel
    P(X=x) = [C(K,x) * C(N-K,n-x)] / C(N,n)
    """
    if x > K or x > n or (n - x) > (N - K):
        return 0.0
    return (kombinasi(K, x) * kombinasi(N - K, n - x)) / kombinasi(N, n)


def ekspektasi_hipergeometrik(N: int, K: int, n: int) -> float:
    """
    E(X) = n * (K/N)
    """
    return n * (K / N)


def variansi_hipergeometrik(N: int, K: int, n: int) -> float:
    """
    Var(X) = n * (K/N) * ((N-K)/N) * ((N-n)/(N-1))
    """
    if N == 1:
        raise ValueError("N harus lebih besar dari 1")
    return n * (K / N) * ((N - K) / N) * ((N - n) / (N - 1))


def distribusi_geometrik(p: float, x: int) -> float:
    """
    Peluang sukses pertama terjadi tepat pada percobaan ke-x.
    P(X=x) = (1-p)^(x-1) * p
    """
    if not (0 < p <= 1):
        raise ValueError("p harus di antara 0 (tidak termasuk) dan 1")
    if x < 1:
        raise ValueError("x harus minimal 1")
    return ((1 - p) ** (x - 1)) * p


def ekspektasi_geometrik(p: float) -> float:
    """
    E(X) = 1/p
    """
    if p <= 0:
        raise ValueError("p harus lebih besar dari 0")
    return 1 / p


def variansi_geometrik(p: float) -> float:
    """
    Var(X) = (1-p)/p²
    """
    if p <= 0:
        raise ValueError("p harus lebih besar dari 0")
    return (1 - p) / (p ** 2)

def distribusi_multinomial(n: int, hasil_x: list, peluang_p: list) -> float:
    """
    Generalisasi binomial untuk >2 kemungkinan hasil.
    P = n! / (x1! * x2! * ... * xk!) * (p1^x1 * p2^x2 * ... * pk^xk)
    hasil_x -> list banyak kejadian tiap kategori
    peluang_p -> list peluang tiap kategori (harus berjumlah 1)
    """
    if len(hasil_x) != len(peluang_p):
        raise ValueError("Panjang hasil_x dan peluang_p harus sama")
    if sum(hasil_x) != n:
        raise ValueError("Total hasil_x harus sama dengan n")
    if abs(sum(peluang_p) - 1) > 1e-9:
        raise ValueError("Total peluang_p harus berjumlah 1")

    koefisien = permutasi_dengan_pengulangan(n, hasil_x)
    hasil_peluang = 1
    for x, p in zip(hasil_x, peluang_p):
        hasil_peluang *= p ** x
    return koefisien * hasil_peluang



def ekspektasi_diskrit(nilai_x: list, peluang_p: list) -> float:
    """
    E(X) = Σ(x * P(x)) — untuk distribusi diskrit apa pun (custom)
    """
    if len(nilai_x) != len(peluang_p):
        raise ValueError("Panjang nilai_x dan peluang_p harus sama")
    return sum(x * p for x, p in zip(nilai_x, peluang_p))


def variansi_diskrit(nilai_x: list, peluang_p: list) -> float:
    """
    Var(X) = Σ((x - E(X))² * P(x)) — untuk distribusi diskrit apa pun (custom)
    """
    e_x = ekspektasi_diskrit(nilai_x, peluang_p)
    return sum(((x - e_x) ** 2) * p for x, p in zip(nilai_x, peluang_p))

def odds_mendukung(peluang_a: float) -> str:
    """
    Odds in favor = P(A) : P(A')
    """
    if not (0 <= peluang_a <= 1):
        raise ValueError("Peluang harus di antara 0 dan 1")
    komplemen = 1 - peluang_a
    if komplemen == 0:
        return "tidak terhingga (peluang A = 1)"
    return f"{peluang_a} : {komplemen}"


def odds_ke_peluang(odds_a: float, odds_b: float) -> float:
    """
    Konversi odds (a:b) menjadi peluang: P(A) = a / (a+b)
    """
    if odds_a + odds_b == 0:
        raise ValueError("Total odds tidak boleh 0")
    return odds_a / (odds_a + odds_b)



def ruang_sampel_kombinasi(items: list, r: int) -> list:
    """
    Menghasilkan daftar aktual semua kombinasi (bukan cuma hitungan)
    """
    return list(combinations(items, r))


def ruang_sampel_permutasi(items: list, r: int) -> list:
    """
    Menghasilkan daftar aktual semua permutasi (bukan cuma hitungan)
    """
    return list(permutations(items, r))