# Lib Matematika Python

Kumpulan fungsi Python untuk menghitung rumus matematika

## Daftar Rumus Tersedia
- **Bisnis Logic**
- **Barisan Deret**
- **Bangun Datar**

### 1. Bangun Datar (`bangun_datar.py`)
- **Persegi**:
    - Keliling (`4 * sisi`)
    - Luas (`sisi * sisi`)
- **Persegi Panjang**: 
    - Keliling (`2 * (panjang + lebar)`)
    - Luas (`panjang * lebar`)
- **Segitiga**: 
    - Keliling (`sisi 1 + sisi 2 + sisi 3`)
    - Luas (`1/2 * alas * tinggi`)
- **Lingkaran**:
    - Keliling (`2 * 3.14 * jari jari`)
    - Luas (`3.14 * jari jari ** 2`)
- **Trapesium**:
    - Keliling (`a + b + c + d`)
    - Luas (`1/2 * (sisi sejajar 1 + sisi sejajar 2) * tinggi`)
- **Jajar Genjang**:
    - Keliling (`2 * (sisi 1 + sisi 2)`)
    - Luas (`alas * tinggi`)
- **Belah Ketupat**: 
    - Keliling (`4 * sisi`)
    - Luas (`1/2 * diagonal 1 * diagonal 2`)
- **Layang-Layang**: 
    - Keliling (`2 * (sisi 1 + sisi 2)`)
    - Luas (`1/2 * diagonal 1 * diagonal 2`)

### 2. Bangun Ruang (`bangun_ruang.py`)
```segera```

### 3. Aritmatika & Bilangan (`baris_deret.py`)
- **Barisan Aritmatika**:
    - Rumus (`a + (suku N - 1) * perbedaan`)
- **Deret Aritmatika**:
    - Rumus (`jumlah suku N/2 * (2 * suku pertama + (jumlah suku N - 1) * perbedaan)`)
- **Barisan Geometri**:
    - Rumus (`suku pertama * rasio ** (suku N - 1)`)
- **Deret Geometri**:
    - Rumus rasio(+) (`suku pertama * (rasio ** suku N - 1) / (rasio -1)`)
    - Rumus rasio(-) (`suku pertama * (1 - rasio ** suku N) / (1 - rasio)`)
- **Deret Geometri**:
    - Rumus rasio == 1 (`suku pertama * jumlah suku N`)
    - Rumus rasio > 1 (`suku pertama * (rasio ** jumlah suku N - 1) / (rasio - 1)`)
    - Rumus rasio < 1 (`suku pertama * (1 - rasio ** jumlah suku N) / (1 - rasio)`)
- **Deret Geometri Infinity**:
    - Syarat (`-1 < rasio < 1`, kalau di luar itu -> error/divergen)
    - Rumus (`suku pertama / (1 - rasio)`)
- **Deret Fibonacci**:
    - Rumus (`N = U_{n-1} + U_{n-2}`)
- **Bilangan Asli**:
    - Syarat (`Hanya bisa bilangan positif, akan menghasilkan error jika negarif atau kurang dari 1`)
    - Rumus (`suku N * (suku N + 1) / 2`)
- **Bilangan Kuadrat**:
    - Syarat (`Hanya bisa bilangan positif, akan menghasilkan error jika negarif atau kurang dari 1`)
    - Rumus (`suku N * (suku N + 1) * (2 * suku N + 1) / 6`)
- **Pangkat Tiga**:
    - Syarat (`Hanya bisa bilangan positif, akan menghasilkan error jika negarif atau kurang dari 1`)
    - Rumus (`(suku N * (suku N + 1) / 2) ** 2`)

### 4. Bisnis & Logika (`bisnis_logic.py`)
- **Diskon**: Menghitung nilai potongan
- **Bunga**: Menghitung bunga tunggal per bulan

## Cara Penggunaan

Import fungsi dari file modul yang sesuai:

```python
# Contoh import dari file bangun_datar
from rumus_bangun_datar import persegi_l, lingkaran_k

# Contoh import dari file bisnis
from bisnis_logic import diskon

print(persegi_l(5))       # Output: 25
print(lingkaran_k(7))     # Output: 43.96...
print(diskon(10, 50000))  # Output: 5000.0   
```

## License 
Repository ini berada dibawah [MIT LICENSE](LICENSE).