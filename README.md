# Lib Matematika Python

Kumpulan fungsi Python untuk menghitung rumus matematika

## Daftar Rumus Tersedia
- **Bisnis Logic**
- **Barisan Deret**
- **Bangun Datar**

### 1. Bangun Datar (`bangun_datar.py`)
- **Persegi**: Keliling, Luas
- **Persegi Panjang**: Keliling, Luas
- **Segitiga**: Keliling, Luas
- **Lingkaran**: Keliling, Luas
- **Trapesium**: Keliling, Luas
- **Jajar Genjang**: Keliling, Luas
- **Belah Ketupat**: Keliling, Luas
- **Layang-Layang**: Keliling, Luas

### 2. Bangun Ruang (`bangun_ruang.py`)
```segera```

### 3. Aritmatika & Bilangan (`baris_deret.py`)
- **Deret Aritmatika**: Jumlah n suku pertama

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

## License 
Repository ini berada dibawah [MIT LICENSE](LICENSE).