def diskon(persen: int, harga: int) -> float:
    to_diskon = persen/100
    result = to_diskon * harga
    return result

def bunga(besarPinjaman: int, jumlahPerBulan: int, sukuBunga: int) -> float:
    bunga_tiap_bulan = (besarPinjaman/jumlahPerBulan) * sukuBunga/100
    return bunga_tiap_bulan

    
