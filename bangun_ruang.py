import math

def kubus_volume(sisi: int):
    return sisi ** 3

def kubus_luas_permukaan(sisi: int):
    return 6 * sisi ** 2

def kubus_diagonal_sisi(sisi: int):
    return sisi * math.sqrt(2)

def kubus_diagonal_ruang(sisi: int):
    return sisi * math.sqrt(3)

def balok_volume(panjang: int, lebar: int, tinggi: int):
    return panjang * lebar * tinggi

def balok_luas_permukaan(panjang: int, lebar: int, tinggi: int):
    return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

def balok_diagonal_ruang(panjang: float, lebar: float, tinggi: float) -> float:
    return math.sqrt((panjang ** 2) + (lebar ** 2) + (tinggi ** 2))

def tabung_silinder_volume(radius: int, tinggi: int) -> float:
    return 3.14 * (radius ** 2) * tinggi

def tabung_silinder_luas_permukaan(radius: int, tinggi: int) -> float:
    return (2 * 3.14 * radius) * (radius + tinggi)

def tabung_luas_selimut(radius: int, tinggi: int) -> float:
    return 2 * 3.14 * radius * tinggi

def tabung_luas_alas(radius: int) -> float:
    return 3.14 * radius ** 2

def kerucut_volume(radius: float, tinggi: float):
    return 1/3 * 3.14 * (radius ** 2) * tinggi

def kerucut_luas_permukaan(radius: float, garis_pelukis: float):
    return (3.14 * (radius ** 2)) + (3.14 * radius * garis_pelukis)

def kerucut_luas_selimut(radius: float, garis_pelukis: float):
    return 3.14 * radius * garis_pelukis

def kerucut_garis_pelukis(radius: float, tinggi: float):
    return math.sqrt(radius ** 2 + tinggi ** 2)

def bola_volume(radius: float):
    return (4/3) * 3.14 * (radius ** 3)

def bola_luas_permukaan(radius: float):
    return 4 * 3.14 * (radius ** 2)

def prisma_segi_n_volume(luas_alas: float, tinggi: float) -> float:
    """
    Rumus umum volume prisma (berlaku untuk semua bentuk alas).
    """
    return luas_alas * tinggi


def prisma_segi_n_luas_permukaan(luas_alas: float, keliling_alas: float, tinggi: float) -> float:
    """
    Rumus umum luas permukaan prisma (berlaku untuk semua bentuk alas).
    """
    return (2 * luas_alas) + (keliling_alas * tinggi)


def prisma_segitiga_volume(alas: float, tinggi_segitiga: float, tinggi_prisma: float) -> float:
    """
    alas, tinggi_segitiga -> dimensi segitiga alasnya
    tinggi_prisma -> tinggi prisma itu sendiri
    """
    luas_alas = 0.5 * alas * tinggi_segitiga
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segitiga_luas_permukaan(sisi1: float, sisi2: float, sisi3: float, alas: float, tinggi_segitiga: float, tinggi_prisma: float) -> float:
    """
    sisi1, sisi2, sisi3 -> ketiga sisi segitiga (buat keliling)
    alas, tinggi_segitiga -> buat luas alas
    """
    luas_alas = 0.5 * alas * tinggi_segitiga
    keliling_alas = sisi1 + sisi2 + sisi3
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)

def prisma_segiempat_volume(panjang: float, lebar: float, tinggi_prisma: float) -> float:
    luas_alas = panjang * lebar
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segiempat_luas_permukaan(panjang: float, lebar: float, tinggi_prisma: float) -> float:
    luas_alas = panjang * lebar
    keliling_alas = 2 * (panjang + lebar)
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)

def prisma_segilima_volume(sisi: float, tinggi_prisma: float) -> float:
    n = 5
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segilima_luas_permukaan(sisi: float, tinggi_prisma: float) -> float:
    n = 5
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    keliling_alas = n * sisi
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)

def prisma_segienam_volume(sisi: float, tinggi_prisma: float) -> float:
    luas_alas = (3 * math.sqrt(3) / 2) * sisi ** 2
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segienam_luas_permukaan(sisi: float, tinggi_prisma: float) -> float:
    luas_alas = (3 * math.sqrt(3) / 2) * sisi ** 2
    keliling_alas = 6 * sisi
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)

def prisma_trapesium_volume(sisi_sejajar1: float, sisi_sejajar2: float, tinggi_trapesium: float, tinggi_prisma: float) -> float:
    luas_alas = 0.5 * (sisi_sejajar1 + sisi_sejajar2) * tinggi_trapesium
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_trapesium_luas_permukaan(sisi_sejajar1: float, sisi_sejajar2: float, sisi_miring1: float, sisi_miring2: float, tinggi_trapesium: float, tinggi_prisma: float) -> float:
    luas_alas = 0.5 * (sisi_sejajar1 + sisi_sejajar2) * tinggi_trapesium
    keliling_alas = sisi_sejajar1 + sisi_sejajar2 + sisi_miring1 + sisi_miring2
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)

def limas_segi_n_volume(luas_alas: float, tinggi: float) -> float:
    """
    Rumus umum volume limas (berlaku untuk semua bentuk alas).
    """
    return (1/3) * luas_alas * tinggi


def limas_segi_n_luas_permukaan(luas_alas: float, jumlah_luas_sisi_tegak: float) -> float:
    """
    Rumus umum luas permukaan limas.
    jumlah_luas_sisi_tegak -> total luas semua segitiga sisi tegak (bukan cuma satu)
    """
    return luas_alas + jumlah_luas_sisi_tegak

def limas_segitiga_volume(alas: float, tinggi_segitiga: float, tinggi_limas: float) -> float:
    luas_alas = 0.5 * alas * tinggi_segitiga
    return limas_segi_n_volume(luas_alas, tinggi_limas)


def limas_segitiga_luas_permukaan(alas: float, tinggi_segitiga: float, sisi1: float, sisi2: float, sisi3: float, tinggi_sisi_tegak1: float, tinggi_sisi_tegak2: float, tinggi_sisi_tegak3: float) -> float:
    """
    tinggi_sisi_tegak(1,2,3) -> tinggi segitiga tiap sisi tegak (beda-beda kalau limasnya gak beraturan)
    """
    luas_alas = 0.5 * alas * tinggi_segitiga
    jumlah_luas_sisi_tegak = (0.5 * sisi1 * tinggi_sisi_tegak1) + (0.5 * sisi2 * tinggi_sisi_tegak2) + (0.5 * sisi3 * tinggi_sisi_tegak3)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)

def limas_segiempat_volume(sisi: float, tinggi_limas: float) -> float:
    luas_alas = sisi ** 2
    return limas_segi_n_volume(luas_alas, tinggi_limas)


def limas_segiempat_luas_permukaan(sisi: float, tinggi_limas: float) -> float:
    luas_alas = sisi ** 2
    tinggi_sisi_tegak = math.sqrt(tinggi_limas ** 2 + (sisi / 2) ** 2)
    jumlah_luas_sisi_tegak = 4 * (0.5 * sisi * tinggi_sisi_tegak)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)

def limas_segilima_volume(sisi: float, tinggi_limas: float) -> float:
    n = 5
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return limas_segi_n_volume(luas_alas, tinggi_limas)

def limas_segilima_luas_permukaan(sisi: float, tinggi_limas: float) -> float:
    n = 5
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    apotema_alas = sisi / (2 * math.tan(math.pi / n))
    tinggi_sisi_tegak = math.sqrt(tinggi_limas ** 2 + apotema_alas ** 2)
    jumlah_luas_sisi_tegak = n * (0.5 * sisi * tinggi_sisi_tegak)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)

def limas_segienam_volume(sisi: float, tinggi_limas: float) -> float:
    luas_alas = (3 * math.sqrt(3) / 2) * sisi ** 2
    return limas_segi_n_volume(luas_alas, tinggi_limas)

def limas_segienam_luas_permukaan(sisi: float, tinggi_limas: float) -> float:
    n = 6
    luas_alas = (3 * math.sqrt(3) / 2) * sisi ** 2
    apotema_alas = sisi / (2 * math.tan(math.pi / n))
    tinggi_sisi_tegak = math.sqrt(tinggi_limas ** 2 + apotema_alas ** 2)
    jumlah_luas_sisi_tegak = n * (0.5 * sisi * tinggi_sisi_tegak)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)

def limas_trapesium_volume(sisi_sejajar1: float, sisi_sejajar2: float,
                             tinggi_trapesium: float, tinggi_limas: float) -> float:
    luas_alas = 0.5 * (sisi_sejajar1 + sisi_sejajar2) * tinggi_trapesium
    return limas_segi_n_volume(luas_alas, tinggi_limas)


def limas_trapesium_luas_permukaan(sisi_sejajar1: float, sisi_sejajar2: float, sisi_miring1: float, sisi_miring2: float, tinggi_trapesium: float, tinggi_limas: float,tinggi_sisi_tegak1: float, tinggi_sisi_tegak2: float, tinggi_sisi_tegak3: float, tinggi_sisi_tegak4: float) -> float:
    """
    tinggi_sisi_tegak(1-4) -> tinggi segitiga tiap sisi tegak (beda-beda karena
    trapesium punya 4 sisi dengan panjang yang berbeda-beda, jadi limasnya
    otomatis gak beraturan)
    Urutan sisi: 1=sejajar1, 2=sejajar2, 3=miring1, 4=miring2
    """
    luas_alas = 0.5 * (sisi_sejajar1 + sisi_sejajar2) * tinggi_trapesium
    jumlah_luas_sisi_tegak = (0.5 * sisi_sejajar1 * tinggi_sisi_tegak1) + (0.5 * sisi_sejajar2 * tinggi_sisi_tegak2) + (0.5 * sisi_miring1 * tinggi_sisi_tegak3) + (0.5 * sisi_miring2 * tinggi_sisi_tegak4)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)

def setengah_bola_volume(radius: float) -> float:
    return (2/3) * 3.14 * (radius ** 3)


def setengah_bola_luas_permukaan_dengan_alas(radius: float) -> float:
    return 3 * 3.14 * (radius ** 2)


def setengah_bola_luas_permukaan_tanpa_alas(radius: float) -> float:
    return 2 * 3.14 * (radius ** 2)

def prisma_segitujuh_volume(sisi: float, tinggi_prisma: float) -> float:
    n = 7
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segitujuh_luas_permukaan(sisi: float, tinggi_prisma: float) -> float:
    n = 7
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    keliling_alas = n * sisi
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)


def prisma_segidelapan_volume(sisi: float, tinggi_prisma: float) -> float:
    n = 8
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segidelapan_luas_permukaan(sisi: float, tinggi_prisma: float) -> float:
    n = 8
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    keliling_alas = n * sisi
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)


def prisma_segisembilan_volume(sisi: float, tinggi_prisma: float) -> float:
    n = 9
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segisembilan_luas_permukaan(sisi: float, tinggi_prisma: float) -> float:
    n = 9
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    keliling_alas = n * sisi
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)


def prisma_segisepuluh_volume(sisi: float, tinggi_prisma: float) -> float:
    n = 10
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return prisma_segi_n_volume(luas_alas, tinggi_prisma)


def prisma_segisepuluh_luas_permukaan(sisi: float, tinggi_prisma: float) -> float:
    n = 10
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    keliling_alas = n * sisi
    return prisma_segi_n_luas_permukaan(luas_alas, keliling_alas, tinggi_prisma)

def limas_segitujuh_volume(sisi: float, tinggi_limas: float) -> float:
    n = 7
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return limas_segi_n_volume(luas_alas, tinggi_limas)


def limas_segitujuh_luas_permukaan(sisi: float, tinggi_limas: float) -> float:
    n = 7
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    apotema_alas = sisi / (2 * math.tan(math.pi / n))
    tinggi_sisi_tegak = math.sqrt(tinggi_limas ** 2 + apotema_alas ** 2)
    jumlah_luas_sisi_tegak = n * (0.5 * sisi * tinggi_sisi_tegak)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)


def limas_segidelapan_volume(sisi: float, tinggi_limas: float) -> float:
    n = 8
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return limas_segi_n_volume(luas_alas, tinggi_limas)


def limas_segidelapan_luas_permukaan(sisi: float, tinggi_limas: float) -> float:
    n = 8
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    apotema_alas = sisi / (2 * math.tan(math.pi / n))
    tinggi_sisi_tegak = math.sqrt(tinggi_limas ** 2 + apotema_alas ** 2)
    jumlah_luas_sisi_tegak = n * (0.5 * sisi * tinggi_sisi_tegak)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)


def limas_segisembilan_volume(sisi: float, tinggi_limas: float) -> float:
    n = 9
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return limas_segi_n_volume(luas_alas, tinggi_limas)


def limas_segisembilan_luas_permukaan(sisi: float, tinggi_limas: float) -> float:
    n = 9
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    apotema_alas = sisi / (2 * math.tan(math.pi / n))
    tinggi_sisi_tegak = math.sqrt(tinggi_limas ** 2 + apotema_alas ** 2)
    jumlah_luas_sisi_tegak = n * (0.5 * sisi * tinggi_sisi_tegak)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)


def limas_segisepuluh_volume(sisi: float, tinggi_limas: float) -> float:
    n = 10
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    return limas_segi_n_volume(luas_alas, tinggi_limas)


def limas_segisepuluh_luas_permukaan(sisi: float, tinggi_limas: float) -> float:
    n = 10
    luas_alas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
    apotema_alas = sisi / (2 * math.tan(math.pi / n))
    tinggi_sisi_tegak = math.sqrt(tinggi_limas ** 2 + apotema_alas ** 2)
    jumlah_luas_sisi_tegak = n * (0.5 * sisi * tinggi_sisi_tegak)
    return limas_segi_n_luas_permukaan(luas_alas, jumlah_luas_sisi_tegak)

def kerucut_terpancung_volume(radius_besar: float, radius_kecil: float, tinggi: float) -> float:
    return (1/3) * 3.14 * tinggi * (radius_besar ** 2 + radius_besar * radius_kecil + radius_kecil ** 2)


def kerucut_terpancung_garis_pelukis(radius_besar: float, radius_kecil: float, tinggi: float) -> float:
    return math.sqrt((radius_besar - radius_kecil) ** 2 + tinggi ** 2)


def kerucut_terpancung_luas_permukaan(radius_besar: float, radius_kecil: float, tinggi: float) -> float:
    garis_pelukis = kerucut_terpancung_garis_pelukis(radius_besar, radius_kecil, tinggi)
    luas_selimut = 3.14 * (radius_besar + radius_kecil) * garis_pelukis
    luas_alas_besar = 3.14 * radius_besar ** 2
    luas_alas_kecil = 3.14 * radius_kecil ** 2
    return luas_selimut + luas_alas_besar + luas_alas_kecil

def limas_terpancung_segiempat_volume(sisi_besar: float, sisi_kecil: float, tinggi: float) -> float:
    luas_alas_besar = sisi_besar ** 2
    luas_alas_kecil = sisi_kecil ** 2
    return (tinggi / 3) * (luas_alas_besar + luas_alas_kecil + math.sqrt(luas_alas_besar * luas_alas_kecil))


def limas_terpancung_segiempat_luas_permukaan(sisi_besar: float, sisi_kecil: float, tinggi_sisi_tegak: float) -> float:
    """
    tinggi_sisi_tegak -> tinggi trapesium pada tiap sisi tegak (dihitung terpisah/manual)
    """
    luas_alas_besar = sisi_besar ** 2
    luas_alas_kecil = sisi_kecil ** 2
    luas_selimut = 4 * (0.5 * (sisi_besar + sisi_kecil) * tinggi_sisi_tegak)
    return luas_alas_besar + luas_alas_kecil + luas_selimut

def tabung_berongga_volume(radius_luar: float, radius_dalam: float, tinggi: float) -> float:
    return 3.14 * (radius_luar ** 2 - radius_dalam ** 2) * tinggi


def tabung_berongga_luas_permukaan(radius_luar: float, radius_dalam: float, tinggi: float) -> float:
    luas_selimut_luar = 2 * 3.14 * radius_luar * tinggi
    luas_selimut_dalam = 2 * 3.14 * radius_dalam * tinggi
    luas_cincin_atas_bawah = 2 * (3.14 * (radius_luar ** 2 - radius_dalam ** 2))
    return luas_selimut_luar + luas_selimut_dalam + luas_cincin_atas_bawah


def bola_berongga_volume(radius_luar: float, radius_dalam: float) -> float:
    return (4/3) * 3.14 * (radius_luar ** 3 - radius_dalam ** 3)


def bola_berongga_luas_permukaan(radius_luar: float, radius_dalam: float) -> float:
    """
    Total luas permukaan luar + dalam cangkang bola.
    """
    luas_luar = 4 * 3.14 * radius_luar ** 2
    luas_dalam = 4 * 3.14 * radius_dalam ** 2
    return luas_luar + luas_dalam

def tembereng_bola_volume(radius_bola: float, tinggi_tembereng: float) -> float:
    return (3.14 * tinggi_tembereng ** 2 / 3) * (3 * radius_bola - tinggi_tembereng)


def tembereng_bola_luas_permukaan_lengkung(radius_bola: float, tinggi_tembereng: float) -> float:
    return 2 * 3.14 * radius_bola * tinggi_tembereng


def elipsoid_volume(sumbu_a: float, sumbu_b: float, sumbu_c: float) -> float:
    return (4/3) * 3.14 * sumbu_a * sumbu_b * sumbu_c

def limas_terpancung_segitiga_volume(alas_besar: float, tinggi_segitiga_besar: float, alas_kecil: float, tinggi_segitiga_kecil: float,tinggi: float) -> float:
    luas_alas_besar = 0.5 * alas_besar * tinggi_segitiga_besar
    luas_alas_kecil = 0.5 * alas_kecil * tinggi_segitiga_kecil
    return (tinggi / 3) * (luas_alas_besar + luas_alas_kecil + math.sqrt(luas_alas_besar * luas_alas_kecil))


def limas_terpancung_segitiga_luas_permukaan(luas_alas_besar: float, luas_alas_kecil: float,
                                               jumlah_luas_sisi_tegak: float) -> float:
    """
    jumlah_luas_sisi_tegak -> total luas ke-3 trapesium sisi tegak (dihitung manual/terpisah)
    """
    return luas_alas_besar + luas_alas_kecil + jumlah_luas_sisi_tegak

def limas_terpancung_segilima_volume(sisi_besar: float, sisi_kecil: float, tinggi: float) -> float:
    n = 5
    luas_alas_besar = (n * sisi_besar ** 2) / (4 * math.tan(math.pi / n))
    luas_alas_kecil = (n * sisi_kecil ** 2) / (4 * math.tan(math.pi / n))
    return (tinggi / 3) * (luas_alas_besar + luas_alas_kecil + math.sqrt(luas_alas_besar * luas_alas_kecil))


def limas_terpancung_segilima_luas_permukaan(sisi_besar: float, sisi_kecil: float,
                                               tinggi_sisi_tegak: float) -> float:
    n = 5
    luas_alas_besar = (n * sisi_besar ** 2) / (4 * math.tan(math.pi / n))
    luas_alas_kecil = (n * sisi_kecil ** 2) / (4 * math.tan(math.pi / n))
    luas_selimut = n * (0.5 * (sisi_besar + sisi_kecil) * tinggi_sisi_tegak)
    return luas_alas_besar + luas_alas_kecil + luas_selimut

def limas_terpancung_segienam_volume(sisi_besar: float, sisi_kecil: float, tinggi: float) -> float:
    luas_alas_besar = (3 * math.sqrt(3) / 2) * sisi_besar ** 2
    luas_alas_kecil = (3 * math.sqrt(3) / 2) * sisi_kecil ** 2
    return (tinggi / 3) * (luas_alas_besar + luas_alas_kecil + math.sqrt(luas_alas_besar * luas_alas_kecil))


def limas_terpancung_segienam_luas_permukaan(sisi_besar: float, sisi_kecil: float,
                                               tinggi_sisi_tegak: float) -> float:
    n = 6
    luas_alas_besar = (3 * math.sqrt(3) / 2) * sisi_besar ** 2
    luas_alas_kecil = (3 * math.sqrt(3) / 2) * sisi_kecil ** 2
    luas_selimut = n * (0.5 * (sisi_besar + sisi_kecil) * tinggi_sisi_tegak)
    return luas_alas_besar + luas_alas_kecil + luas_selimut

def torus_volume(radius_pusat: float, radius_tabung: float) -> float:
    """
    radius_pusat (R) -> jarak dari pusat torus ke pusat tabung donat
    radius_tabung (r) -> jari-jari tabung donat itu sendiri
    """
    return 2 * (3.14 ** 2) * radius_pusat * (radius_tabung ** 2)


def torus_luas_permukaan(radius_pusat: float, radius_tabung: float) -> float:
    return 4 * (3.14 ** 2) * radius_pusat * radius_tabung


def tetrahedron_volume(sisi: float) -> float:
    return (sisi ** 3 * math.sqrt(2)) / 12


def tetrahedron_luas_permukaan(sisi: float) -> float:
    return math.sqrt(3) * sisi ** 2


def oktahedron_volume(sisi: float) -> float:
    return (math.sqrt(2) / 3) * sisi ** 3


def oktahedron_luas_permukaan(sisi: float) -> float:
    return 2 * math.sqrt(3) * sisi ** 2


def dodekahedron_volume(sisi: float) -> float:
    return ((15 + 7 * math.sqrt(5)) / 4) * sisi ** 3


def dodekahedron_luas_permukaan(sisi: float) -> float:
    return 3 * math.sqrt(25 + 10 * math.sqrt(5)) * sisi ** 2


def ikosahedron_volume(sisi: float) -> float:
    return (5 * (3 + math.sqrt(5)) / 12) * sisi ** 3


def ikosahedron_luas_permukaan(sisi: float) -> float:
    return 5 * math.sqrt(3) * sisi ** 2


def zona_bola_luas_permukaan(radius_bola: float, jarak_antar_bidang: float) -> float:
    return 2 * 3.14 * radius_bola * jarak_antar_bidang

def sektor_bola_volume(radius_bola: float, tinggi_tembereng: float) -> float:
    return (2/3) * 3.14 * (radius_bola ** 2) * tinggi_tembereng


def bipiramida_volume(luas_alas: float, tinggi_satu_sisi: float) -> float:
    """
    tinggi_satu_sisi -> tinggi limas dari bidang alas ke salah satu puncak
    (dikali 2 karena bipiramida = 2 limas digabung di alasnya)
    """
    return 2 * (1/3) * luas_alas * tinggi_satu_sisi


def bipiramida_luas_permukaan(jumlah_luas_semua_sisi_tegak: float) -> float:
    """
    Bipiramida gak punya "alas" yang keliatan (ketutup di dalam),
    jadi luas permukaan = jumlah semua sisi tegak (atas + bawah)
    """
    return jumlah_luas_semua_sisi_tegak

def prismatoid_volume(luas_alas_bawah: float, luas_alas_atas: float,
                       luas_penampang_tengah: float, tinggi: float) -> float:
    """
    Rumus Simpson/Prismatoid — bisa dipakai untuk hampir semua bangun ruang
    (prisma, limas, terpancung, bola, dll) selama diketahui luas penampang tengahnya.
    """
    return (tinggi / 6) * (luas_alas_bawah + 4 * luas_penampang_tengah + luas_alas_atas)