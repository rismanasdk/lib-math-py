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


def matriks_ordo(m: list) -> tuple:
    """
    Mengembalikan ordo matriks dalam bentuk (baris, kolom)
    """
    return (len(m), len(m[0]))


def matriks_apakah_persegi(m: list) -> bool:
    """
    Cek apakah jumlah baris sama dengan jumlah kolom
    """
    return len(m) == len(m[0])


def matriks_minor(m: list, baris_hapus: int, kolom_hapus: int) -> list:
    """
    Minor matriks = matriks setelah satu baris dan satu kolom dihapus
    """
    return [
        baris[:kolom_hapus] + baris[kolom_hapus + 1:]
        for i, baris in enumerate(m)
        if i != baris_hapus
    ]


def matriks_kofaktor_elemen(m: list, baris: int, kolom: int) -> float:
    """
    Kofaktor elemen Aij = (-1)^(i+j) * determinan minor
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Kofaktor hanya berlaku untuk matriks persegi")
    return ((-1) ** (baris + kolom)) * determinan_nxn(matriks_minor(m, baris, kolom))


def matriks_kofaktor(m: list) -> list:
    """
    Matriks kofaktor berisi kofaktor dari setiap elemen matriks
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Matriks kofaktor hanya berlaku untuk matriks persegi")
    n = len(m)
    if n == 1:
        return [[1]]
    return [[matriks_kofaktor_elemen(m, i, j) for j in range(n)] for i in range(n)]


def matriks_adjoin(m: list) -> list:
    """
    Adjoin matriks = transpose dari matriks kofaktor
    """
    return matriks_transpose(matriks_kofaktor(m))


def matriks_apakah_nol(m: list) -> bool:
    """
    Matriks nol jika semua elemennya bernilai 0
    """
    return all(elemen == 0 for baris in m for elemen in baris)


def matriks_apakah_skalar(m: list) -> bool:
    """
    Matriks skalar jika berbentuk diagonal dan elemen diagonalnya sama
    """
    if not matriks_apakah_persegi(m) or not matriks_apakah_diagonal(m):
        return False
    nilai_diagonal = m[0][0]
    return all(m[i][i] == nilai_diagonal for i in range(len(m)))


def matriks_apakah_segitiga_atas(m: list) -> bool:
    """
    Matriks segitiga atas jika semua elemen di bawah diagonal utama = 0
    """
    if not matriks_apakah_persegi(m):
        return False
    n = len(m)
    return all(m[i][j] == 0 for i in range(n) for j in range(i))


def matriks_apakah_segitiga_bawah(m: list) -> bool:
    """
    Matriks segitiga bawah jika semua elemen di atas diagonal utama = 0
    """
    if not matriks_apakah_persegi(m):
        return False
    n = len(m)
    return all(m[i][j] == 0 for i in range(n) for j in range(i + 1, n))


def matriks_apakah_ortogonal(m: list) -> bool:
    """
    Matriks ortogonal jika A * transpose(A) = I
    """
    if not matriks_apakah_persegi(m):
        return False
    hasil = matriks_kali_matriks(m, matriks_transpose(m))
    identitas = matriks_identitas(len(m))
    return all(
        math.isclose(hasil[i][j], identitas[i][j], abs_tol=1e-9)
        for i in range(len(m))
        for j in range(len(m))
    )


def matriks_apakah_singular(m: list) -> bool:
    """
    Matriks singular jika determinannya = 0
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Singular hanya berlaku untuk matriks persegi")
    return math.isclose(determinan_nxn(m), 0, abs_tol=1e-9)


def row_echelon_form(m: list) -> list:
    """
    Mengubah matriks ke bentuk eselon baris (row echelon form)
    """
    matriks = [baris[:] for baris in m]
    baris_n, kolom_n = len(matriks), len(matriks[0])
    pivot_baris = 0

    for kolom in range(kolom_n):
        if pivot_baris >= baris_n:
            break

        pivot = None
        for baris in range(pivot_baris, baris_n):
            if not math.isclose(matriks[baris][kolom], 0, abs_tol=1e-12):
                pivot = baris
                break

        if pivot is None:
            continue

        matriks[pivot_baris], matriks[pivot] = matriks[pivot], matriks[pivot_baris]
        nilai_pivot = matriks[pivot_baris][kolom]
        matriks[pivot_baris] = [elemen / nilai_pivot for elemen in matriks[pivot_baris]]

        for baris in range(pivot_baris + 1, baris_n):
            faktor = matriks[baris][kolom]
            matriks[baris] = [
                matriks[baris][j] - faktor * matriks[pivot_baris][j]
                for j in range(kolom_n)
            ]

        pivot_baris += 1

    return matriks


def reduced_row_echelon_form(m: list) -> list:
    """
    Mengubah matriks ke bentuk eselon baris tereduksi (RREF)
    """
    matriks = row_echelon_form(m)
    baris_n, kolom_n = len(matriks), len(matriks[0])

    for baris in range(baris_n - 1, -1, -1):
        pivot_kolom = None
        for kolom in range(kolom_n):
            if not math.isclose(matriks[baris][kolom], 0, abs_tol=1e-12):
                pivot_kolom = kolom
                break

        if pivot_kolom is None:
            continue

        for baris_atas in range(baris):
            faktor = matriks[baris_atas][pivot_kolom]
            matriks[baris_atas] = [
                matriks[baris_atas][j] - faktor * matriks[baris][j]
                for j in range(kolom_n)
            ]

    return matriks


def operasi_baris_tukar(m: list, baris1: int, baris2: int) -> list:
    """
    Operasi baris elementer: menukar dua baris
    """
    hasil = [baris[:] for baris in m]
    hasil[baris1], hasil[baris2] = hasil[baris2], hasil[baris1]
    return hasil


def operasi_baris_kali(m: list, baris: int, skalar: float) -> list:
    """
    Operasi baris elementer: mengalikan satu baris dengan skalar
    """
    if skalar == 0:
        raise ValueError("Skalar tidak boleh 0")
    hasil = [b[:] for b in m]
    hasil[baris] = [elemen * skalar for elemen in hasil[baris]]
    return hasil


def operasi_baris_tambah_kelipatan(m: list, baris_tujuan: int, baris_sumber: int, skalar: float) -> list:
    """
    Operasi baris elementer: baris tujuan ditambah kelipatan baris sumber
    """
    hasil = [baris[:] for baris in m]
    hasil[baris_tujuan] = [
        hasil[baris_tujuan][j] + skalar * hasil[baris_sumber][j]
        for j in range(len(hasil[0]))
    ]
    return hasil


def matriks_pangkat(m: list, pangkat: int) -> list:
    """
    Pangkat matriks persegi A^n dengan n bilangan bulat >= 0
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Pangkat matriks hanya berlaku untuk matriks persegi")
    if pangkat < 0:
        raise ValueError("Pangkat harus lebih besar atau sama dengan 0")

    hasil = matriks_identitas(len(m))
    basis = [baris[:] for baris in m]
    n = pangkat

    while n > 0:
        if n % 2 == 1:
            hasil = matriks_kali_matriks(hasil, basis)
        basis = matriks_kali_matriks(basis, basis)
        n //= 2

    return hasil


def determinan_gauss(m: list) -> float:
    """
    Determinan matriks persegi menggunakan eliminasi Gauss
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Determinan hanya berlaku untuk matriks persegi")

    matriks = [baris[:] for baris in m]
    n = len(matriks)
    det = 1
    tukar_baris = 0

    for i in range(n):
        pivot = i
        for baris in range(i, n):
            if abs(matriks[baris][i]) > abs(matriks[pivot][i]):
                pivot = baris

        if math.isclose(matriks[pivot][i], 0, abs_tol=1e-12):
            return 0

        if pivot != i:
            matriks[i], matriks[pivot] = matriks[pivot], matriks[i]
            tukar_baris += 1

        for baris in range(i + 1, n):
            faktor = matriks[baris][i] / matriks[i][i]
            for kolom in range(i, n):
                matriks[baris][kolom] -= faktor * matriks[i][kolom]

    for i in range(n):
        det *= matriks[i][i]

    return -det if tukar_baris % 2 else det


def eigen_nxn_power_iteration(m: list, iterasi: int = 100, toleransi: float = 1e-10) -> tuple:
    """
    Pendekatan nilai eigen dominan dan vektor eigen dominan untuk matriks NxN
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Eigen NxN hanya berlaku untuk matriks persegi")

    n = len(m)
    vektor = [1.0] * n
    nilai_eigen_lama = 0

    for _ in range(iterasi):
        hasil_kali = [sum(m[i][j] * vektor[j] for j in range(n)) for i in range(n)]
        panjang = vektor_panjang(hasil_kali)
        if panjang == 0:
            raise ValueError("Power iteration gagal untuk vektor nol")

        vektor_baru = [elemen / panjang for elemen in hasil_kali]
        av = [sum(m[i][j] * vektor_baru[j] for j in range(n)) for i in range(n)]
        nilai_eigen = vektor_dot_product(vektor_baru, av)

        if math.isclose(nilai_eigen, nilai_eigen_lama, abs_tol=toleransi):
            return (nilai_eigen, vektor_baru)

        vektor = vektor_baru
        nilai_eigen_lama = nilai_eigen

    return (nilai_eigen_lama, vektor)


def vektor_proyeksi_skalar(v1: list, v2: list) -> float:
    """
    Proyeksi skalar v1 pada v2 = (v1.v2) / |v2|
    """
    panjang_v2 = vektor_panjang(v2)
    if panjang_v2 == 0:
        raise ValueError("Vektor v2 tidak boleh nol")
    return vektor_dot_product(v1, v2) / panjang_v2


def vektor_komponen_terhadap(v1: list, v2: list) -> tuple:
    """
    Komponen v1 terhadap v2 berupa (komponen sejajar, komponen tegak lurus)
    """
    komponen_sejajar = vektor_proyeksi(v1, v2)
    komponen_tegak_lurus = vektor_kurang(v1, komponen_sejajar)
    return (komponen_sejajar, komponen_tegak_lurus)


def vektor_apakah_paralel(v1: list, v2: list) -> bool:
    """
    Dua vektor paralel jika sudutnya 0 atau 180 derajat
    """
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama")
    if vektor_panjang(v1) == 0 or vektor_panjang(v2) == 0:
        raise ValueError("Vektor tidak boleh nol")

    rasio = None
    for a, b in zip(v1, v2):
        if math.isclose(b, 0, abs_tol=1e-12):
            if not math.isclose(a, 0, abs_tol=1e-12):
                return False
        else:
            nilai_rasio = a / b
            if rasio is None:
                rasio = nilai_rasio
            elif not math.isclose(nilai_rasio, rasio, abs_tol=1e-9):
                return False
    return True


def vektor_apakah_ortogonal(v1: list, v2: list) -> bool:
    """
    Dua vektor ortogonal jika dot product = 0
    """
    return math.isclose(vektor_dot_product(v1, v2), 0, abs_tol=1e-9)


def luas_jajargenjang_dari_vektor(v1: list, v2: list) -> float:
    """
    Luas jajargenjang dari dua vektor = |v1 x v2|
    """
    if len(v1) == 2 and len(v2) == 2:
        return abs(v1[0] * v2[1] - v1[1] * v2[0])
    return vektor_panjang(vektor_cross_product(v1, v2))


def luas_segitiga_dari_vektor(v1: list, v2: list) -> float:
    """
    Luas segitiga dari dua vektor = 1/2 * |v1 x v2|
    """
    return 0.5 * luas_jajargenjang_dari_vektor(v1, v2)


def triple_scalar_product(v1: list, v2: list, v3: list) -> float:
    """
    Triple scalar product = v1 . (v2 x v3)
    """
    return vektor_dot_product(v1, vektor_cross_product(v2, v3))


def volume_parallelepiped(v1: list, v2: list, v3: list) -> float:
    """
    Volume parallelepiped = |v1 . (v2 x v3)|
    """
    return abs(triple_scalar_product(v1, v2, v3))


def vektor_satuan_dari_dua_titik(titik_awal: list, titik_akhir: list) -> list:
    """
    Vektor satuan arah dari titik awal ke titik akhir
    """
    return vektor_normalisasi(vektor_kurang(titik_akhir, titik_awal))


def titik_tengah(titik1: list, titik2: list) -> list:
    """
    Titik tengah antara dua titik
    """
    if len(titik1) != len(titik2):
        raise ValueError("Dimensi kedua titik harus sama")
    return [(titik1[i] + titik2[i]) / 2 for i in range(len(titik1))]


def jarak_titik_ke_garis(titik: list, titik_garis1: list, titik_garis2: list) -> float:
    """
    Jarak titik ke garis memakai luas jajargenjang / panjang alas
    """
    arah_garis = vektor_kurang(titik_garis2, titik_garis1)
    vektor_titik = vektor_kurang(titik, titik_garis1)
    panjang_alas = vektor_panjang(arah_garis)
    if panjang_alas == 0:
        raise ValueError("Dua titik garis tidak boleh sama")
    return luas_jajargenjang_dari_vektor(vektor_titik, arah_garis) / panjang_alas


def jarak_titik_ke_bidang(titik: list, titik_bidang: list, normal_bidang: list) -> float:
    """
    Jarak titik ke bidang = |normal . (titik - titik_bidang)| / |normal|
    """
    panjang_normal = vektor_panjang(normal_bidang)
    if panjang_normal == 0:
        raise ValueError("Vektor normal tidak boleh nol")
    return abs(vektor_dot_product(normal_bidang, vektor_kurang(titik, titik_bidang))) / panjang_normal


def persamaan_garis_2d_dari_dua_titik(titik1: list, titik2: list) -> tuple:
    """
    Persamaan garis 2D dalam bentuk ax + by + c = 0
    """
    if len(titik1) != 2 or len(titik2) != 2:
        raise ValueError("Fungsi ini hanya untuk titik 2D")
    x1, y1 = titik1
    x2, y2 = titik2
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    return (a, b, c)


def persamaan_garis_3d_dari_dua_titik(titik1: list, titik2: list) -> dict:
    """
    Persamaan garis 3D parametrik: titik awal + t * vektor arah
    """
    if len(titik1) != 3 or len(titik2) != 3:
        raise ValueError("Fungsi ini hanya untuk titik 3D")
    return {
        "titik": titik1,
        "arah": vektor_kurang(titik2, titik1)
    }


def persamaan_bidang_dari_normal(titik: list, normal: list) -> tuple:
    """
    Persamaan bidang dalam bentuk ax + by + cz + d = 0
    """
    if len(titik) != 3 or len(normal) != 3:
        raise ValueError("Fungsi ini hanya untuk ruang 3D")
    a, b, c = normal
    d = -(a * titik[0] + b * titik[1] + c * titik[2])
    return (a, b, c, d)


def persamaan_bidang_dari_tiga_titik(titik1: list, titik2: list, titik3: list) -> tuple:
    """
    Persamaan bidang dari tiga titik tidak segaris
    """
    v1 = vektor_kurang(titik2, titik1)
    v2 = vektor_kurang(titik3, titik1)
    normal = vektor_cross_product(v1, v2)
    if vektor_panjang(normal) == 0:
        raise ValueError("Tiga titik tidak boleh segaris")
    return persamaan_bidang_dari_normal(titik1, normal)


def matriks_apakah_sama(m1: list, m2: list, toleransi: float = 1e-9) -> bool:
    """
    Cek kesamaan dua matriks dengan toleransi angka desimal
    """
    if matriks_ordo(m1) != matriks_ordo(m2):
        return False
    return all(
        math.isclose(m1[i][j], m2[i][j], abs_tol=toleransi)
        for i in range(len(m1))
        for j in range(len(m1[0]))
    )


def matriks_diagonal(diagonal: list) -> list:
    """
    Membuat matriks diagonal dari list elemen diagonal
    """
    n = len(diagonal)
    return [[diagonal[i] if i == j else 0 for j in range(n)] for i in range(n)]


def matriks_hadamard(m1: list, m2: list) -> list:
    """
    Perkalian Hadamard = perkalian elemen per elemen
    """
    if matriks_ordo(m1) != matriks_ordo(m2):
        raise ValueError("Ukuran kedua matriks harus sama")
    return [[m1[i][j] * m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]


def matriks_kronecker(m1: list, m2: list) -> list:
    """
    Perkalian Kronecker antara dua matriks
    """
    hasil = []
    for baris1 in m1:
        for baris2 in m2:
            baris_baru = []
            for elemen1 in baris1:
                baris_baru.extend(elemen1 * elemen2 for elemen2 in baris2)
            hasil.append(baris_baru)
    return hasil


def matriks_gabung_horizontal(m1: list, m2: list) -> list:
    """
    Menggabungkan dua matriks secara horizontal
    """
    if len(m1) != len(m2):
        raise ValueError("Jumlah baris kedua matriks harus sama")
    return [m1[i][:] + m2[i][:] for i in range(len(m1))]


def matriks_gabung_vertikal(m1: list, m2: list) -> list:
    """
    Menggabungkan dua matriks secara vertikal
    """
    if len(m1[0]) != len(m2[0]):
        raise ValueError("Jumlah kolom kedua matriks harus sama")
    return [baris[:] for baris in m1] + [baris[:] for baris in m2]


def matriks_augmented(matriks_koefisien: list, matriks_konstanta: list) -> list:
    """
    Membuat matriks augmented [A|b] untuk SPL
    """
    return matriks_gabung_horizontal(matriks_koefisien, [[nilai] for nilai in matriks_konstanta])


def matriks_norma_frobenius(m: list) -> float:
    """
    Norma Frobenius = akar jumlah kuadrat semua elemen
    """
    return math.sqrt(sum(elemen ** 2 for baris in m for elemen in baris))


def matriks_norma_maksimum_baris(m: list) -> float:
    """
    Norma maksimum baris = maksimum jumlah nilai mutlak tiap baris
    """
    return max(sum(abs(elemen) for elemen in baris) for baris in m)


def matriks_norma_maksimum_kolom(m: list) -> float:
    """
    Norma maksimum kolom = maksimum jumlah nilai mutlak tiap kolom
    """
    return max(sum(abs(m[i][j]) for i in range(len(m))) for j in range(len(m[0])))


def matriks_kondisi_2x2(m: list) -> float:
    """
    Bilangan kondisi sederhana untuk 2x2 memakai norma Frobenius
    """
    return matriks_norma_frobenius(m) * matriks_norma_frobenius(invers_2x2(m))


def dekomposisi_lu(m: list) -> tuple:
    """
    Dekomposisi LU tanpa pivot: A = L * U
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Dekomposisi LU hanya berlaku untuk matriks persegi")

    n = len(m)
    l = matriks_identitas(n)
    u = matriks_nol(n, n)

    for i in range(n):
        for k in range(i, n):
            u[i][k] = m[i][k] - sum(l[i][j] * u[j][k] for j in range(i))

        if math.isclose(u[i][i], 0, abs_tol=1e-12):
            raise ValueError("Pivot nol, LU tanpa pivot gagal")

        for k in range(i + 1, n):
            l[k][i] = (m[k][i] - sum(l[k][j] * u[j][i] for j in range(i))) / u[i][i]

    return (l, u)


def substitusi_maju(l: list, b: list) -> list:
    """
    Menyelesaikan Ly = b untuk matriks segitiga bawah
    """
    n = len(l)
    y = [0] * n
    for i in range(n):
        y[i] = (b[i] - sum(l[i][j] * y[j] for j in range(i))) / l[i][i]
    return y


def substitusi_mundur(u: list, y: list) -> list:
    """
    Menyelesaikan Ux = y untuk matriks segitiga atas
    """
    n = len(u)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(u[i][j] * x[j] for j in range(i + 1, n))) / u[i][i]
    return x


def spl_dekomposisi_lu(matriks_koefisien: list, matriks_konstanta: list) -> list:
    """
    Menyelesaikan SPL dengan dekomposisi LU
    """
    l, u = dekomposisi_lu(matriks_koefisien)
    y = substitusi_maju(l, matriks_konstanta)
    return substitusi_mundur(u, y)


def dekomposisi_cholesky(m: list) -> list:
    """
    Dekomposisi Cholesky untuk matriks simetris positif definit: A = L * transpose(L)
    """
    if not matriks_apakah_simetris(m):
        raise ValueError("Cholesky hanya berlaku untuk matriks simetris")

    n = len(m)
    l = matriks_nol(n, n)

    for i in range(n):
        for j in range(i + 1):
            jumlah = sum(l[i][k] * l[j][k] for k in range(j))

            if i == j:
                nilai = m[i][i] - jumlah
                if nilai <= 0:
                    raise ValueError("Matriks bukan positif definit")
                l[i][j] = math.sqrt(nilai)
            else:
                l[i][j] = (m[i][j] - jumlah) / l[j][j]

    return l


def gram_schmidt(vektor_vektor: list) -> list:
    """
    Ortonormalisasi Gram-Schmidt untuk kumpulan vektor
    """
    basis = []
    for v in vektor_vektor:
        w = v[:]
        for u in basis:
            proyeksi = vektor_kali_skalar(u, vektor_dot_product(w, u))
            w = vektor_kurang(w, proyeksi)
        panjang = vektor_panjang(w)
        if not math.isclose(panjang, 0, abs_tol=1e-12):
            basis.append([elemen / panjang for elemen in w])
    return basis


def dekomposisi_qr(m: list) -> tuple:
    """
    Dekomposisi QR dengan Gram-Schmidt: A = Q * R
    """
    kolom_a = matriks_transpose(m)
    kolom_q = gram_schmidt(kolom_a)
    q = matriks_transpose(kolom_q)
    r = matriks_kali_matriks(matriks_transpose(q), m)
    return (q, r)


def least_squares(matriks_koefisien: list, matriks_konstanta: list) -> list:
    """
    Solusi kuadrat terkecil: x = (A^T A)^-1 A^T b
    """
    at = matriks_transpose(matriks_koefisien)
    ata = matriks_kali_matriks(at, matriks_koefisien)
    atb = matriks_kali_matriks(at, [[nilai] for nilai in matriks_konstanta])
    hasil = matriks_kali_matriks(invers_nxn(ata), atb)
    return [baris[0] for baris in hasil]


def matriks_rotasi_2d(sudut_derajat: float) -> list:
    """
    Matriks rotasi 2D
    """
    sudut = math.radians(sudut_derajat)
    return [[math.cos(sudut), -math.sin(sudut)], [math.sin(sudut), math.cos(sudut)]]


def matriks_skala_2d(skala_x: float, skala_y: float) -> list:
    """
    Matriks skala 2D
    """
    return [[skala_x, 0], [0, skala_y]]


def matriks_refleksi_x_2d() -> list:
    """
    Matriks refleksi terhadap sumbu-x
    """
    return [[1, 0], [0, -1]]


def matriks_refleksi_y_2d() -> list:
    """
    Matriks refleksi terhadap sumbu-y
    """
    return [[-1, 0], [0, 1]]


def transformasi_vektor(m: list, v: list) -> list:
    """
    Transformasi vektor dengan matriks: hasil = A * v
    """
    hasil = matriks_kali_matriks(m, [[elemen] for elemen in v])
    return [baris[0] for baris in hasil]


def rotasi_vektor_2d(v: list, sudut_derajat: float) -> list:
    """
    Rotasi vektor 2D dengan sudut tertentu
    """
    return transformasi_vektor(matriks_rotasi_2d(sudut_derajat), v)


def matriks_rotasi_x_3d(sudut_derajat: float) -> list:
    """
    Matriks rotasi 3D terhadap sumbu-x
    """
    sudut = math.radians(sudut_derajat)
    return [[1, 0, 0], [0, math.cos(sudut), -math.sin(sudut)], [0, math.sin(sudut), math.cos(sudut)]]


def matriks_rotasi_y_3d(sudut_derajat: float) -> list:
    """
    Matriks rotasi 3D terhadap sumbu-y
    """
    sudut = math.radians(sudut_derajat)
    return [[math.cos(sudut), 0, math.sin(sudut)], [0, 1, 0], [-math.sin(sudut), 0, math.cos(sudut)]]


def matriks_rotasi_z_3d(sudut_derajat: float) -> list:
    """
    Matriks rotasi 3D terhadap sumbu-z
    """
    sudut = math.radians(sudut_derajat)
    return [[math.cos(sudut), -math.sin(sudut), 0], [math.sin(sudut), math.cos(sudut), 0], [0, 0, 1]]


def vektor_refleksi_terhadap_normal(v: list, normal: list) -> list:
    """
    Refleksi vektor terhadap bidang/garis dengan vektor normal
    """
    n = vektor_normalisasi(normal)
    skalar = 2 * vektor_dot_product(v, n)
    return vektor_kurang(v, vektor_kali_skalar(n, skalar))


def vektor_lerp(v1: list, v2: list, t: float) -> list:
    """
    Interpolasi linear vektor: (1-t)*v1 + t*v2
    """
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama")
    return [(1 - t) * v1[i] + t * v2[i] for i in range(len(v1))]


def sudut_tiga_titik(titik_a: list, titik_b: list, titik_c: list) -> float:
    """
    Sudut ABC dengan titik B sebagai pusat sudut
    """
    ba = vektor_kurang(titik_a, titik_b)
    bc = vektor_kurang(titik_c, titik_b)
    return vektor_sudut_antar(ba, bc)


def centroid(titik_titik: list) -> list:
    """
    Titik pusat/centroid dari kumpulan titik
    """
    if not titik_titik:
        raise ValueError("Daftar titik tidak boleh kosong")
    dimensi = len(titik_titik[0])
    return [sum(titik[i] for titik in titik_titik) / len(titik_titik) for i in range(dimensi)]


def koordinat_barycentric_2d(titik: list, segitiga: list) -> tuple:
    """
    Koordinat barycentric titik terhadap segitiga 2D
    """
    a, b, c = segitiga
    v0 = vektor_kurang(b, a)
    v1 = vektor_kurang(c, a)
    v2 = vektor_kurang(titik, a)
    d00 = vektor_dot_product(v0, v0)
    d01 = vektor_dot_product(v0, v1)
    d11 = vektor_dot_product(v1, v1)
    d20 = vektor_dot_product(v2, v0)
    d21 = vektor_dot_product(v2, v1)
    penyebut = d00 * d11 - d01 * d01
    if math.isclose(penyebut, 0, abs_tol=1e-12):
        raise ValueError("Segitiga tidak boleh degenerat")
    v = (d11 * d20 - d01 * d21) / penyebut
    w = (d00 * d21 - d01 * d20) / penyebut
    u = 1 - v - w
    return (u, v, w)


def titik_di_dalam_segitiga_2d(titik: list, segitiga: list) -> bool:
    """
    Cek titik di dalam segitiga memakai koordinat barycentric
    """
    u, v, w = koordinat_barycentric_2d(titik, segitiga)
    return u >= 0 and v >= 0 and w >= 0


def konversi_polar_ke_kartesius(radius: float, sudut_derajat: float) -> tuple:
    """
    Konversi koordinat polar ke kartesius
    """
    sudut = math.radians(sudut_derajat)
    return (radius * math.cos(sudut), radius * math.sin(sudut))


def konversi_kartesius_ke_polar(x: float, y: float) -> tuple:
    """
    Konversi koordinat kartesius ke polar
    """
    return (math.sqrt(x ** 2 + y ** 2), math.degrees(math.atan2(y, x)))


def matriks_apakah_anti_simetris(m: list) -> bool:
    """
    Matriks anti-simetris jika A^T = -A
    """
    if not matriks_apakah_persegi(m):
        return False
    mt = matriks_transpose(m)
    return all(math.isclose(mt[i][j], -m[i][j], abs_tol=1e-9) for i in range(len(m)) for j in range(len(m)))


def matriks_apakah_idempoten(m: list) -> bool:
    """
    Matriks idempoten jika A^2 = A
    """
    if not matriks_apakah_persegi(m):
        return False
    return matriks_apakah_sama(matriks_kali_matriks(m, m), m)


def matriks_apakah_involutori(m: list) -> bool:
    """
    Matriks involutori jika A^2 = I
    """
    if not matriks_apakah_persegi(m):
        return False
    return matriks_apakah_sama(matriks_kali_matriks(m, m), matriks_identitas(len(m)))


def matriks_apakah_nilpoten(m: list, pangkat_maks: int = None) -> bool:
    """
    Matriks nilpoten jika ada k sehingga A^k = 0
    """
    if not matriks_apakah_persegi(m):
        return False
    batas = pangkat_maks or len(m)
    hasil = matriks_identitas(len(m))
    for _ in range(batas):
        hasil = matriks_kali_matriks(hasil, m)
        if matriks_apakah_nol(hasil):
            return True
    return False


def matriks_apakah_permutasi(m: list) -> bool:
    """
    Matriks permutasi jika tiap baris dan kolom punya tepat satu angka 1
    """
    if not matriks_apakah_persegi(m):
        return False
    n = len(m)
    baris_valid = all(sum(1 for nilai in baris if nilai == 1) == 1 and sum(1 for nilai in baris if nilai != 0) == 1 for baris in m)
    kolom_valid = all(sum(1 for i in range(n) if m[i][j] == 1) == 1 and sum(1 for i in range(n) if m[i][j] != 0) == 1 for j in range(n))
    return baris_valid and kolom_valid


def matriks_apakah_toeplitz(m: list) -> bool:
    """
    Matriks Toeplitz jika elemen diagonal kiri-atas ke kanan-bawah bernilai sama
    """
    return all(m[i][j] == m[i - 1][j - 1] for i in range(1, len(m)) for j in range(1, len(m[0])))


def matriks_apakah_positif_definit_2x2(m: list) -> bool:
    """
    Matriks 2x2 positif definit jika minor utama positif
    """
    if len(m) != 2 or len(m[0]) != 2:
        raise ValueError("Fungsi ini hanya untuk matriks 2x2")
    return m[0][0] > 0 and determinan_2x2(m) > 0


def matriks_blok(m11: list, m12: list, m21: list, m22: list) -> list:
    """
    Membuat matriks blok [[m11, m12], [m21, m22]]
    """
    atas = matriks_gabung_horizontal(m11, m12)
    bawah = matriks_gabung_horizontal(m21, m22)
    return matriks_gabung_vertikal(atas, bawah)


def matriks_vandermonde(data: list, pangkat: int = None) -> list:
    """
    Matriks Vandermonde dari data x
    """
    n = pangkat if pangkat is not None else len(data)
    return [[x ** p for p in range(n)] for x in data]


def matriks_permutasi(urutan: list) -> list:
    """
    Membuat matriks permutasi dari daftar indeks tujuan
    """
    n = len(urutan)
    hasil = matriks_nol(n, n)
    for i, j in enumerate(urutan):
        hasil[i][j] = 1
    return hasil


def matriks_komutator(m1: list, m2: list) -> list:
    """
    Komutator matriks [A,B] = AB - BA
    """
    return matriks_kurang(matriks_kali_matriks(m1, m2), matriks_kali_matriks(m2, m1))


def matriks_antikomutator(m1: list, m2: list) -> list:
    """
    Antikomutator matriks {A,B} = AB + BA
    """
    return matriks_tambah(matriks_kali_matriks(m1, m2), matriks_kali_matriks(m2, m1))


def matriks_projection_dari_vektor(v: list) -> list:
    """
    Matriks proyeksi ke arah v: P = vv^T / (v^T v)
    """
    penyebut = vektor_dot_product(v, v)
    if penyebut == 0:
        raise ValueError("Vektor tidak boleh nol")
    return [[v[i] * v[j] / penyebut for j in range(len(v))] for i in range(len(v))]


def matriks_householder(v: list) -> list:
    """
    Matriks Householder: H = I - 2vv^T/(v^T v)
    """
    p = matriks_projection_dari_vektor(v)
    return matriks_kurang(matriks_identitas(len(v)), matriks_kali_skalar(p, 2))


def matriks_givens(n: int, i: int, j: int, sudut_derajat: float) -> list:
    """
    Matriks rotasi Givens ukuran n pada bidang i-j
    """
    g = matriks_identitas(n)
    sudut = math.radians(sudut_derajat)
    c = math.cos(sudut)
    s = math.sin(sudut)
    g[i][i] = c
    g[j][j] = c
    g[i][j] = -s
    g[j][i] = s
    return g


def matriks_covariance(data: list) -> list:
    """
    Matriks kovariansi, data berupa list baris observasi
    """
    if len(data) < 2:
        raise ValueError("Data minimal 2 observasi")
    jumlah_data = len(data)
    jumlah_variabel = len(data[0])
    mean = [sum(baris[j] for baris in data) / jumlah_data for j in range(jumlah_variabel)]
    return [
        [
            sum((baris[i] - mean[i]) * (baris[j] - mean[j]) for baris in data) / (jumlah_data - 1)
            for j in range(jumlah_variabel)
        ]
        for i in range(jumlah_variabel)
    ]


def matriks_correlation(data: list) -> list:
    """
    Matriks korelasi dari data observasi
    """
    cov = matriks_covariance(data)
    n = len(cov)
    simpangan = [math.sqrt(cov[i][i]) for i in range(n)]
    return [
        [
            cov[i][j] / (simpangan[i] * simpangan[j]) if simpangan[i] != 0 and simpangan[j] != 0 else 0
            for j in range(n)
        ]
        for i in range(n)
    ]


def matriks_exponential_deret(m: list, suku: int = 20) -> list:
    """
    Eksponensial matriks e^A memakai deret Taylor
    """
    if not matriks_apakah_persegi(m):
        raise ValueError("Eksponensial matriks hanya untuk matriks persegi")
    n = len(m)
    hasil = matriks_identitas(n)
    pangkat = matriks_identitas(n)
    faktorial = 1
    for k in range(1, suku):
        pangkat = matriks_kali_matriks(pangkat, m)
        faktorial *= k
        hasil = matriks_tambah(hasil, matriks_kali_skalar(pangkat, 1 / faktorial))
    return hasil


def matriks_pseudoinverse_left(m: list) -> list:
    """
    Pseudoinverse kiri untuk kolom independen: A+ = (A^T A)^-1 A^T
    """
    mt = matriks_transpose(m)
    return matriks_kali_matriks(invers_nxn(matriks_kali_matriks(mt, m)), mt)


def matriks_pseudoinverse_right(m: list) -> list:
    """
    Pseudoinverse kanan untuk baris independen: A+ = A^T(AA^T)^-1
    """
    mt = matriks_transpose(m)
    return matriks_kali_matriks(mt, invers_nxn(matriks_kali_matriks(m, mt)))


def vektor_cross_2d_skalar(v1: list, v2: list) -> float:
    """
    Cross product 2D versi skalar
    """
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError("Fungsi ini hanya untuk vektor 2D")
    return v1[0] * v2[1] - v1[1] * v2[0]


def sudut_berarah_2d(v1: list, v2: list) -> float:
    """
    Sudut berarah dari v1 ke v2 dalam derajat
    """
    return math.degrees(math.atan2(vektor_cross_2d_skalar(v1, v2), vektor_dot_product(v1, v2)))


def orientasi_tiga_titik_2d(a: list, b: list, c: list) -> float:
    """
    Orientasi tiga titik 2D, positif berlawanan arah jarum jam
    """
    return vektor_cross_2d_skalar(vektor_kurang(b, a), vektor_kurang(c, a))


def titik_proyeksi_ke_garis(titik: list, garis_a: list, garis_b: list) -> list:
    """
    Proyeksi titik ke garis yang melalui dua titik
    """
    arah = vektor_kurang(garis_b, garis_a)
    ap = vektor_kurang(titik, garis_a)
    t = vektor_dot_product(ap, arah) / vektor_dot_product(arah, arah)
    return vektor_tambah(garis_a, vektor_kali_skalar(arah, t))


def titik_refleksi_terhadap_garis(titik: list, garis_a: list, garis_b: list) -> list:
    """
    Refleksi titik terhadap garis
    """
    proyeksi = titik_proyeksi_ke_garis(titik, garis_a, garis_b)
    return vektor_kurang(vektor_kali_skalar(proyeksi, 2), titik)


def titik_proyeksi_ke_bidang(titik: list, titik_bidang: list, normal_bidang: list) -> list:
    """
    Proyeksi titik ke bidang
    """
    n = vektor_normalisasi(normal_bidang)
    jarak_bertanda = vektor_dot_product(vektor_kurang(titik, titik_bidang), n)
    return vektor_kurang(titik, vektor_kali_skalar(n, jarak_bertanda))


def titik_refleksi_terhadap_bidang(titik: list, titik_bidang: list, normal_bidang: list) -> list:
    """
    Refleksi titik terhadap bidang
    """
    proyeksi = titik_proyeksi_ke_bidang(titik, titik_bidang, normal_bidang)
    return vektor_kurang(vektor_kali_skalar(proyeksi, 2), titik)


def perpotongan_dua_garis_2d(a1: list, a2: list, b1: list, b2: list) -> list:
    """
    Titik potong dua garis 2D
    """
    r = vektor_kurang(a2, a1)
    s = vektor_kurang(b2, b1)
    penyebut = vektor_cross_2d_skalar(r, s)
    if math.isclose(penyebut, 0, abs_tol=1e-12):
        raise ValueError("Garis sejajar atau berimpit")
    t = vektor_cross_2d_skalar(vektor_kurang(b1, a1), s) / penyebut
    return vektor_tambah(a1, vektor_kali_skalar(r, t))


def perpotongan_garis_bidang(garis_titik: list, garis_arah: list, bidang_titik: list, bidang_normal: list) -> list:
    """
    Titik potong garis dan bidang
    """
    penyebut = vektor_dot_product(bidang_normal, garis_arah)
    if math.isclose(penyebut, 0, abs_tol=1e-12):
        raise ValueError("Garis sejajar bidang")
    t = vektor_dot_product(bidang_normal, vektor_kurang(bidang_titik, garis_titik)) / penyebut
    return vektor_tambah(garis_titik, vektor_kali_skalar(garis_arah, t))


def sudut_antara_garis_2d(arah1: list, arah2: list) -> float:
    """
    Sudut antara dua garis 2D berdasarkan vektor arah
    """
    sudut = abs(vektor_sudut_antar(arah1, arah2))
    return min(sudut, 180 - sudut)


def sudut_antara_bidang(normal1: list, normal2: list) -> float:
    """
    Sudut antara dua bidang = sudut antara vektor normalnya
    """
    return sudut_antara_garis_2d(normal1, normal2)


def jarak_antara_dua_garis_sejajar_2d(a1: list, a2: list, b1: list) -> float:
    """
    Jarak dua garis sejajar 2D
    """
    return jarak_titik_ke_garis(b1, a1, a2)


def jarak_antara_dua_garis_skew_3d(p1: list, d1: list, p2: list, d2: list) -> float:
    """
    Jarak dua garis bersilangan 3D
    """
    normal = vektor_cross_product(d1, d2)
    panjang_normal = vektor_panjang(normal)
    if math.isclose(panjang_normal, 0, abs_tol=1e-12):
        return jarak_titik_ke_garis(p2, p1, vektor_tambah(p1, d1))
    return abs(vektor_dot_product(vektor_kurang(p2, p1), normal)) / panjang_normal


def matriks_translasi_2d(tx: float, ty: float) -> list:
    """
    Matriks translasi 2D homogen
    """
    return [[1, 0, tx], [0, 1, ty], [0, 0, 1]]


def matriks_shear_2d(shx: float, shy: float) -> list:
    """
    Matriks shear 2D homogen
    """
    return [[1, shx, 0], [shy, 1, 0], [0, 0, 1]]


def transformasi_titik_2d_homogen(m: list, titik: list) -> list:
    """
    Transformasi titik 2D dengan matriks homogen 3x3
    """
    hasil = matriks_kali_matriks(m, [[titik[0]], [titik[1]], [1]])
    w = hasil[2][0]
    if math.isclose(w, 0, abs_tol=1e-12):
        raise ValueError("Koordinat homogen tidak valid")
    return [hasil[0][0] / w, hasil[1][0] / w]


def matriks_translasi_3d(tx: float, ty: float, tz: float) -> list:
    """
    Matriks translasi 3D homogen
    """
    return [[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]]


def matriks_skala_3d(sx: float, sy: float, sz: float) -> list:
    """
    Matriks skala 3D homogen
    """
    return [[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]


def transformasi_titik_3d_homogen(m: list, titik: list) -> list:
    """
    Transformasi titik 3D dengan matriks homogen 4x4
    """
    hasil = matriks_kali_matriks(m, [[titik[0]], [titik[1]], [titik[2]], [1]])
    w = hasil[3][0]
    if math.isclose(w, 0, abs_tol=1e-12):
        raise ValueError("Koordinat homogen tidak valid")
    return [hasil[0][0] / w, hasil[1][0] / w, hasil[2][0] / w]


def konversi_silinder_ke_kartesius(radius: float, sudut_derajat: float, z: float) -> tuple:
    """
    Konversi koordinat silinder ke kartesius
    """
    x, y = konversi_polar_ke_kartesius(radius, sudut_derajat)
    return (x, y, z)


def konversi_kartesius_ke_silinder(x: float, y: float, z: float) -> tuple:
    """
    Konversi koordinat kartesius ke silinder
    """
    radius, sudut = konversi_kartesius_ke_polar(x, y)
    return (radius, sudut, z)


def konversi_bola_ke_kartesius(radius: float, theta_derajat: float, phi_derajat: float) -> tuple:
    """
    Konversi koordinat bola ke kartesius
    """
    theta = math.radians(theta_derajat)
    phi = math.radians(phi_derajat)
    x = radius * math.sin(phi) * math.cos(theta)
    y = radius * math.sin(phi) * math.sin(theta)
    z = radius * math.cos(phi)
    return (x, y, z)


def konversi_kartesius_ke_bola(x: float, y: float, z: float) -> tuple:
    """
    Konversi koordinat kartesius ke bola
    """
    radius = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    if radius == 0:
        return (0, 0, 0)
    theta = math.degrees(math.atan2(y, x))
    phi = math.degrees(math.acos(z / radius))
    return (radius, theta, phi)
