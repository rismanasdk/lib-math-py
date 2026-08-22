import math



def matriks_tambah(m1: list, m2: list) -> list:
    """
    Penjumlahan matriks (elemen per elemen). m1, m2 -> list of list (baris x kolom)
    """
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Ukuran kedua matriks harus sama")
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]


def matriks_kurang(m1: list, m2: list) -> list:
    """
    Pengurangan matriks (elemen per elemen)
    """
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Ukuran kedua matriks harus sama")
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]


def matriks_kali_skalar(m: list, skalar: float) -> list:
    """
    Perkalian matriks dengan skalar (bilangan biasa)
    """
    return [[elemen * skalar for elemen in baris] for baris in m]


def matriks_kali_matriks(m1: list, m2: list) -> list:
    """
    Perkalian matriks (baris x kolom). Jumlah kolom m1 harus sama dengan jumlah baris m2.
    """
    baris_m1, kolom_m1 = len(m1), len(m1[0])
    baris_m2, kolom_m2 = len(m2), len(m2[0])

    if kolom_m1 != baris_m2:
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua")

    hasil = [[0] * kolom_m2 for _ in range(baris_m1)]
    for i in range(baris_m1):
        for j in range(kolom_m2):
            hasil[i][j] = sum(m1[i][k] * m2[k][j] for k in range(kolom_m1))
    return hasil


def matriks_transpose(m: list) -> list:
    """
    Transpose matriks (baris jadi kolom, kolom jadi baris)
    """
    baris, kolom = len(m), len(m[0])
    return [[m[i][j] for i in range(baris)] for j in range(kolom)]

def determinan_2x2(m: list) -> float:
    """
    Determinan matriks 2x2: |a b; c d| = ad - bc
    """
    if len(m) != 2 or len(m[0]) != 2:
        raise ValueError("Matriks harus berukuran 2x2")
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def determinan_3x3(m: list) -> float:
    """
    Determinan matriks 3x3 menggunakan aturan Sarrus
    """
    if len(m) != 3 or len(m[0]) != 3:
        raise ValueError("Matriks harus berukuran 3x3")
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def determinan_nxn(m: list) -> float:
    """
    Determinan matriks NxN menggunakan ekspansi kofaktor (rekursif).
    Cocok untuk matriks berukuran besar, tapi lebih lambat dari rumus langsung.
    """
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return determinan_2x2(m)

    det = 0
    for kolom in range(n):
        minor = [baris[:kolom] + baris[kolom + 1:] for baris in m[1:]]
        tanda = (-1) ** kolom
        det += tanda * m[0][kolom] * determinan_nxn(minor)
    return det



def invers_2x2(m: list) -> list:
    """
    Invers matriks 2x2: (1/det) * [d -b; -c a]
    """
    det = determinan_2x2(m)
    if det == 0:
        raise ValueError("Matriks tidak punya invers (determinan = 0)")
    a, b = m[0][0], m[0][1]
    c, d = m[1][0], m[1][1]
    return [[d / det, -b / det], [-c / det, a / det]]


def invers_3x3(m: list) -> list:
    """
    Invers matriks 3x3 menggunakan matriks adjoin (kofaktor transpose)
    """
    det = determinan_3x3(m)
    if det == 0:
        raise ValueError("Matriks tidak punya invers (determinan = 0)")

    def kofaktor(baris, kolom):
        minor = [r[:kolom] + r[kolom + 1:] for i, r in enumerate(m) if i != baris]
        return ((-1) ** (baris + kolom)) * determinan_2x2(minor)

    matriks_kofaktor = [[kofaktor(i, j) for j in range(3)] for i in range(3)]
    adjoin = matriks_transpose(matriks_kofaktor)
    return matriks_kali_skalar(adjoin, 1 / det)



def matriks_identitas(n: int) -> list:
    """
    Membuat matriks identitas ukuran n x n
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matriks_nol(baris: int, kolom: int) -> list:
    """
    Membuat matriks nol ukuran baris x kolom
    """
    return [[0] * kolom for _ in range(baris)]



def spl_cramer_matriks(matriks_koefisien: list, matriks_konstanta: list) -> list:
    """
    Menyelesaikan sistem persamaan linear pakai metode Cramer berbasis matriks.
    matriks_koefisien -> matriks NxN
    matriks_konstanta -> list nilai konstanta (n elemen)
    """
    n = len(matriks_koefisien)
    det_utama = determinan_nxn(matriks_koefisien)
    if det_utama == 0:
        raise ValueError("Determinan = 0, sistem tidak punya solusi tunggal")

    hasil = []
    for kolom_ganti in range(n):
        matriks_baru = [baris[:] for baris in matriks_koefisien]
        for baris in range(n):
            matriks_baru[baris][kolom_ganti] = matriks_konstanta[baris]
        det_baru = determinan_nxn(matriks_baru)
        hasil.append(det_baru / det_utama)
    return hasil



def vektor_tambah(v1: list, v2: list) -> list:
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama")
    return [v1[i] + v2[i] for i in range(len(v1))]


def vektor_kurang(v1: list, v2: list) -> list:
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama")
    return [v1[i] - v2[i] for i in range(len(v1))]


def vektor_kali_skalar(v: list, skalar: float) -> list:
    return [elemen * skalar for elemen in v]


def vektor_panjang(v: list) -> float:
    """
    Panjang/magnitudo vektor = √(x² + y² + ... )
    """
    return math.sqrt(sum(elemen ** 2 for elemen in v))


def vektor_dot_product(v1: list, v2: list) -> float:
    """
    Perkalian titik (dot product): v1·v2 = Σ(x1*x2)
    """
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama")
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def vektor_cross_product(v1: list, v2: list) -> list:
    """
    Perkalian silang (cross product), hanya untuk vektor 3D
    """
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product hanya berlaku untuk vektor 3D")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]


def vektor_sudut_antar(v1: list, v2: list) -> float:
    """
    Sudut antara 2 vektor (dalam derajat): cos(θ) = (v1·v2) / (|v1|*|v2|)
    """
    panjang1, panjang2 = vektor_panjang(v1), vektor_panjang(v2)
    if panjang1 == 0 or panjang2 == 0:
        raise ValueError("Vektor tidak boleh nol")
    nilai_cos = vektor_dot_product(v1, v2) / (panjang1 * panjang2)
    nilai_cos = max(-1, min(1, nilai_cos))  
    return math.degrees(math.acos(nilai_cos))


def vektor_proyeksi(v1: list, v2: list) -> list:
    """
    Proyeksi vektor v1 pada v2 (hasil vektor)
    """
    panjang2_kuadrat = vektor_dot_product(v2, v2)
    if panjang2_kuadrat == 0:
        raise ValueError("Vektor v2 tidak boleh nol")
    skalar = vektor_dot_product(v1, v2) / panjang2_kuadrat
    return vektor_kali_skalar(v2, skalar)


def vektor_normalisasi(v: list) -> list:
    """
    Mengubah vektor menjadi vektor satuan (panjang = 1), arah tetap sama
    """
    panjang = vektor_panjang(v)
    if panjang == 0:
        raise ValueError("Vektor nol tidak bisa dinormalisasi")
    return [elemen / panjang for elemen in v]


def vektor_jarak(v1: list, v2: list) -> float:
    """
    Jarak antara 2 titik/vektor = panjang dari vektor selisihnya
    """
    return vektor_panjang(vektor_kurang(v1, v2))

def invers_nxn(m: list) -> list:
    """
    Invers matriks NxN menggunakan eliminasi Gauss-Jordan.
    Lebih efisien untuk matriks besar dibanding metode kofaktor.
    """
    n = len(m)
    augmented = [m[i][:] + matriks_identitas(n)[i] for i in range(n)]

    for i in range(n):
        if augmented[i][i] == 0:
            for k in range(i + 1, n):
                if augmented[k][i] != 0:
                    augmented[i], augmented[k] = augmented[k], augmented[i]
                    break
            else:
                raise ValueError("Matriks tidak punya invers (singular)")

        pivot = augmented[i][i]
        augmented[i] = [elemen / pivot for elemen in augmented[i]]

        for k in range(n):
            if k != i:
                faktor = augmented[k][i]
                augmented[k] = [augmented[k][j] - faktor * augmented[i][j] for j in range(2 * n)]

    return [baris[n:] for baris in augmented]



def eliminasi_gauss(matriks_koefisien: list, matriks_konstanta: list) -> list:
    """
    Menyelesaikan SPL dengan eliminasi Gauss (lebih efisien dari Cramer untuk n besar).
    """
    n = len(matriks_koefisien)
    augmented = [matriks_koefisien[i][:] + [matriks_konstanta[i]] for i in range(n)]

    for i in range(n):
        if augmented[i][i] == 0:
            for k in range(i + 1, n):
                if augmented[k][i] != 0:
                    augmented[i], augmented[k] = augmented[k], augmented[i]
                    break
            else:
                raise ValueError("Sistem tidak punya solusi tunggal")

        for k in range(i + 1, n):
            faktor = augmented[k][i] / augmented[i][i]
            augmented[k] = [augmented[k][j] - faktor * augmented[i][j] for j in range(n + 1)]

    solusi = [0] * n
    for i in range(n - 1, -1, -1):
        solusi[i] = (augmented[i][n] - sum(augmented[i][j] * solusi[j] for j in range(i + 1, n))) / augmented[i][i]
    return solusi

def spl_dengan_invers(matriks_koefisien: list, matriks_konstanta: list) -> list:
    """
    Menyelesaikan Ax = b dengan x = A⁻¹b
    """
    n = len(matriks_koefisien)
    if n == 2:
        a_invers = invers_2x2(matriks_koefisien)
    elif n == 3:
        a_invers = invers_3x3(matriks_koefisien)
    else:
        a_invers = invers_nxn(matriks_koefisien)

    hasil = matriks_kali_matriks(a_invers, [[k] for k in matriks_konstanta])
    return [baris[0] for baris in hasil]



def rank_matriks(m: list) -> int:
    """
    Mencari rank matriks (banyak baris tak-nol setelah eliminasi baris/row echelon form)
    """
    matriks = [baris[:] for baris in m]
    baris_n, kolom_n = len(matriks), len(matriks[0])
    rank = 0

    for kolom in range(kolom_n):
        pivot_ditemukan = False
        for baris in range(rank, baris_n):
            if matriks[baris][kolom] != 0:
                matriks[rank], matriks[baris] = matriks[baris], matriks[rank]
                pivot_ditemukan = True
                break

        if pivot_ditemukan:
            for baris in range(rank + 1, baris_n):
                if matriks[baris][kolom] != 0:
                    faktor = matriks[baris][kolom] / matriks[rank][kolom]
                    matriks[baris] = [matriks[baris][j] - faktor * matriks[rank][j] for j in range(kolom_n)]
            rank += 1

    return rank


def trace_matriks(m: list) -> float:
    """
    Trace = jumlah elemen diagonal utama (hanya untuk matriks persegi)
    """
    n = len(m)
    if len(m[0]) != n:
        raise ValueError("Trace hanya berlaku untuk matriks persegi")
    return sum(m[i][i] for i in range(n))


def matriks_apakah_simetris(m: list) -> bool:
    """
    Matriks simetris jika m == transpose(m)
    """
    return m == matriks_transpose(m)


def matriks_apakah_diagonal(m: list) -> bool:
    """
    Matriks diagonal jika semua elemen non-diagonal = 0
    """
    n = len(m)
    for i in range(n):
        for j in range(len(m[0])):
            if i != j and m[i][j] != 0:
                return False
    return True


def matriks_apakah_identitas(m: list) -> bool:
    """
    Cek apakah matriks adalah matriks identitas
    """
    n = len(m)
    return m == matriks_identitas(n)



def eigenvalue_2x2(m: list) -> tuple:
    """
    Mencari nilai eigen matriks 2x2 dari persamaan karakteristik:
    λ² - trace(m)*λ + det(m) = 0
    """
    if len(m) != 2 or len(m[0]) != 2:
        raise ValueError("Matriks harus berukuran 2x2")

    tr = trace_matriks(m)
    det = determinan_2x2(m)
    diskriminan = tr ** 2 - 4 * det

    if diskriminan < 0:
        akar_d = complex(0, math.sqrt(-diskriminan))
    else:
        akar_d = math.sqrt(diskriminan)

    lambda1 = (tr + akar_d) / 2
    lambda2 = (tr - akar_d) / 2
    return (lambda1, lambda2)


def eigenvector_2x2(m: list, eigenvalue: float) -> list:
    """
    Mencari vektor eigen (belum dinormalisasi) untuk suatu nilai eigen tertentu.
    Dari (A - λI)v = 0
    """
    a, b = m[0][0] - eigenvalue, m[0][1]
    c, d = m[1][0], m[1][1] - eigenvalue

    if b != 0:
        return [1, -a / b]
    elif c != 0:
        return [-d / c, 1]
    else:
        return [1, 0]


def vektor_2d_sudut_terhadap_sumbu_x(v: list) -> float:
    """
    Sudut vektor 2D terhadap sumbu-x positif (dalam derajat)
    """
    if len(v) != 2:
        raise ValueError("Fungsi ini hanya untuk vektor 2D")
    return math.degrees(math.atan2(v[1], v[0]))