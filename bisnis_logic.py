def diskon(persen: int, harga: int) -> float:
    to_diskon = persen/100
    result = to_diskon * harga
    return result

def bunga(besarPinjaman: int, jumlahPerBulan: int, sukuBunga: int) -> float:
    bunga_tiap_bulan = (besarPinjaman/jumlahPerBulan) * sukuBunga/100
    return bunga_tiap_bulan


def margin_laba_kotor(laba_kotor: float, pendapatan: float) -> float:
    if pendapatan == 0:
        raise ValueError("Pendapatan tidak boleh 0")
    return (laba_kotor / pendapatan) * 100


def margin_laba_bersih(laba_bersih: float, pendapatan: float) -> float:
    if pendapatan == 0:
        raise ValueError("Pendapatan tidak boleh 0")
    return (laba_bersih / pendapatan) * 100


def markup_pricing(harga_jual: float, biaya: float) -> float:
    if biaya == 0:
        raise ValueError("Biaya tidak boleh 0")
    return ((harga_jual - biaya) / biaya) * 100


def harga_jual_target_laba(biaya: float, target_laba_persen: float) -> float:
    return biaya * (1 + target_laba_persen / 100)


def rasio_biaya_pendapatan(total_biaya: float, pendapatan: float) -> float:
    if pendapatan == 0:
        raise ValueError("Pendapatan tidak boleh 0")
    return (total_biaya / pendapatan) * 100


def bep_unit(biaya_tetap: float, harga_jual_per_unit: float, biaya_variabel_per_unit: float) -> float:
    margin_kontribusi = harga_jual_per_unit - biaya_variabel_per_unit
    if margin_kontribusi == 0:
        raise ValueError("Margin kontribusi tidak boleh 0")
    return biaya_tetap / margin_kontribusi


def bep_value(biaya_tetap: float, rasio_margin_kontribusi_persen: float) -> float:
    rasio = rasio_margin_kontribusi_persen / 100
    if rasio == 0:
        raise ValueError("Rasio margin kontribusi tidak boleh 0")
    return biaya_tetap / rasio


def margin_kontribusi(harga_jual_per_unit: float, biaya_variabel_per_unit: float) -> float:
    return harga_jual_per_unit - biaya_variabel_per_unit


def rasio_margin_kontribusi(harga_jual_per_unit: float, biaya_variabel_per_unit: float) -> float:
    if harga_jual_per_unit == 0:
        raise ValueError("Harga jual per unit tidak boleh 0")
    return ((harga_jual_per_unit - biaya_variabel_per_unit) / harga_jual_per_unit) * 100


def bunga_sederhana(pokok: float, tingkat_bunga_persen: float, waktu: float) -> float:
    return pokok * (tingkat_bunga_persen / 100) * waktu


def bunga_majemuk(pokok: float, tingkat_bunga_persen: float, waktu: float, frekuensi: int = 1) -> float:
    return pokok * ((1 + (tingkat_bunga_persen / 100) / frekuensi) ** (frekuensi * waktu))


def future_value(nilai_sekarang: float, tingkat_bunga_persen: float, waktu: float, frekuensi: int = 1) -> float:
    return nilai_sekarang * ((1 + (tingkat_bunga_persen / 100) / frekuensi) ** (frekuensi * waktu))


def present_value(nilai_masa_depan: float, tingkat_bunga_persen: float, waktu: float, frekuensi: int = 1) -> float:
    return nilai_masa_depan / ((1 + (tingkat_bunga_persen / 100) / frekuensi) ** (frekuensi * waktu))


def anuitas(pembayaran: float, tingkat_bunga_persen: float, periode: int) -> float:
    r = tingkat_bunga_persen / 100
    if r == 0:
        return pembayaran * periode
    return pembayaran * ((1 - (1 + r) ** -periode) / r)


def perpetuitas(pembayaran: float, tingkat_bunga_persen: float) -> float:
    r = tingkat_bunga_persen / 100
    if r == 0:
        raise ValueError("Tingkat bunga tidak boleh 0")
    return pembayaran / r


def roi(keuntungan_investasi: float, biaya_investasi: float) -> float:
    if biaya_investasi == 0:
        raise ValueError("Biaya investasi tidak boleh 0")
    return (keuntungan_investasi / biaya_investasi) * 100


def npv(investasi_awal: float, arus_kas: list, tingkat_diskonto_persen: float) -> float:
    r = tingkat_diskonto_persen / 100
    return -investasi_awal + sum(kas / ((1 + r) ** periode) for periode, kas in enumerate(arus_kas, start=1))


def irr(investasi_awal: float, arus_kas: list, toleransi: float = 1e-7, iterasi_maks: int = 1000) -> float:
    rendah = -0.9999
    tinggi = 10.0

    def nilai_npv(rate):
        return -investasi_awal + sum(kas / ((1 + rate) ** periode) for periode, kas in enumerate(arus_kas, start=1))

    npv_rendah = nilai_npv(rendah)
    npv_tinggi = nilai_npv(tinggi)
    if npv_rendah * npv_tinggi > 0:
        raise ValueError("IRR tidak ditemukan pada rentang pencarian")

    for _ in range(iterasi_maks):
        tengah = (rendah + tinggi) / 2
        npv_tengah = nilai_npv(tengah)
        if abs(npv_tengah) < toleransi:
            return tengah * 100
        if npv_rendah * npv_tengah < 0:
            tinggi = tengah
            npv_tinggi = npv_tengah
        else:
            rendah = tengah
            npv_rendah = npv_tengah

    return ((rendah + tinggi) / 2) * 100


def payback_period(investasi_awal: float, arus_kas: list) -> float:
    sisa = investasi_awal
    for periode, kas in enumerate(arus_kas, start=1):
        if kas <= 0:
            sisa -= kas
            continue
        if sisa <= kas:
            return (periode - 1) + (sisa / kas)
        sisa -= kas
    raise ValueError("Modal belum kembali dalam arus kas yang diberikan")


def profitability_index(investasi_awal: float, arus_kas: list, tingkat_diskonto_persen: float) -> float:
    if investasi_awal == 0:
        raise ValueError("Investasi awal tidak boleh 0")
    r = tingkat_diskonto_persen / 100
    pv_arus_kas = sum(kas / ((1 + r) ** periode) for periode, kas in enumerate(arus_kas, start=1))
    return pv_arus_kas / investasi_awal


def diskon_tunggal(harga: float, persen_diskon: float) -> float:
    return harga * (persen_diskon / 100)


def diskon_berantai(harga: float, daftar_persen_diskon: list) -> float:
    harga_akhir = harga
    for persen in daftar_persen_diskon:
        harga_akhir *= (1 - persen / 100)
    return harga - harga_akhir


def harga_netto_setelah_diskon(harga: float, persen_diskon: float) -> float:
    return harga - diskon_tunggal(harga, persen_diskon)


def ppn(harga: float, persen_ppn: float = 11) -> float:
    return harga * (persen_ppn / 100)


def harga_setelah_pajak(harga: float, persen_pajak: float) -> float:
    return harga * (1 + persen_pajak / 100)


def harga_sebelum_pajak(harga_setelah_pajak_nilai: float, persen_pajak: float) -> float:
    return harga_setelah_pajak_nilai / (1 + persen_pajak / 100)


def current_ratio(aset_lancar: float, kewajiban_lancar: float) -> float:
    if kewajiban_lancar == 0:
        raise ValueError("Kewajiban lancar tidak boleh 0")
    return aset_lancar / kewajiban_lancar


def quick_ratio(aset_lancar: float, persediaan: float, kewajiban_lancar: float) -> float:
    if kewajiban_lancar == 0:
        raise ValueError("Kewajiban lancar tidak boleh 0")
    return (aset_lancar - persediaan) / kewajiban_lancar


def inventory_turnover(hpp: float, rata_rata_persediaan: float) -> float:
    if rata_rata_persediaan == 0:
        raise ValueError("Rata-rata persediaan tidak boleh 0")
    return hpp / rata_rata_persediaan


def receivables_turnover(penjualan_kredit_bersih: float, rata_rata_piutang: float) -> float:
    if rata_rata_piutang == 0:
        raise ValueError("Rata-rata piutang tidak boleh 0")
    return penjualan_kredit_bersih / rata_rata_piutang


def eps(laba_bersih: float, dividen_preferen: float, jumlah_saham_beredar: float) -> float:
    if jumlah_saham_beredar == 0:
        raise ValueError("Jumlah saham beredar tidak boleh 0")
    return (laba_bersih - dividen_preferen) / jumlah_saham_beredar


def roe(laba_bersih: float, ekuitas: float) -> float:
    if ekuitas == 0:
        raise ValueError("Ekuitas tidak boleh 0")
    return (laba_bersih / ekuitas) * 100


def roa(laba_bersih: float, total_aset: float) -> float:
    if total_aset == 0:
        raise ValueError("Total aset tidak boleh 0")
    return (laba_bersih / total_aset) * 100


def debt_to_equity_ratio(total_utang: float, ekuitas: float) -> float:
    if ekuitas == 0:
        raise ValueError("Ekuitas tidak boleh 0")
    return total_utang / ekuitas


def depresiasi_garis_lurus(biaya_perolehan: float, nilai_residu: float, umur_manfaat: float) -> float:
    if umur_manfaat == 0:
        raise ValueError("Umur manfaat tidak boleh 0")
    return (biaya_perolehan - nilai_residu) / umur_manfaat


def depresiasi_saldo_menurun(nilai_buku_awal: float, tarif_depresiasi_persen: float) -> float:
    return nilai_buku_awal * (tarif_depresiasi_persen / 100)


def nilai_buku(biaya_perolehan: float, akumulasi_depresiasi: float) -> float:
    return biaya_perolehan - akumulasi_depresiasi


def nilai_residu(biaya_perolehan: float, total_depresiasi: float) -> float:
    return biaya_perolehan - total_depresiasi


def rata_rata_tertimbang(nilai: list, bobot: list) -> float:
    if len(nilai) != len(bobot):
        raise ValueError("Jumlah nilai dan bobot harus sama")
    total_bobot = sum(bobot)
    if total_bobot == 0:
        raise ValueError("Total bobot tidak boleh 0")
    return sum(nilai[i] * bobot[i] for i in range(len(nilai))) / total_bobot


def elastisitas_harga(persen_perubahan_jumlah_diminta: float, persen_perubahan_harga: float) -> float:
    if persen_perubahan_harga == 0:
        raise ValueError("Persen perubahan harga tidak boleh 0")
    return persen_perubahan_jumlah_diminta / persen_perubahan_harga


def proyeksi_penjualan(penjualan_awal: float, tingkat_pertumbuhan_persen: float, periode: int) -> float:
    return penjualan_awal * ((1 + tingkat_pertumbuhan_persen / 100) ** periode)


def regresi_linear(data_x: list, data_y: list) -> tuple:
    if len(data_x) != len(data_y):
        raise ValueError("Jumlah data x dan y harus sama")
    n = len(data_x)
    if n == 0:
        raise ValueError("Data tidak boleh kosong")
    mean_x = sum(data_x) / n
    mean_y = sum(data_y) / n
    pembilang = sum((data_x[i] - mean_x) * (data_y[i] - mean_y) for i in range(n))
    penyebut = sum((data_x[i] - mean_x) ** 2 for i in range(n))
    if penyebut == 0:
        raise ValueError("Variasi data x tidak boleh 0")
    slope = pembilang / penyebut
    intercept = mean_y - slope * mean_x
    return (slope, intercept)


def prediksi_regresi_linear(data_x: list, data_y: list, x: float) -> float:
    slope, intercept = regresi_linear(data_x, data_y)
    return slope * x + intercept
