def persegi_k(s: int):
    return 4 * s

def persegi_l(s: int):
    return s * s

def persegi_pk(p: int, l: int):
    kel = 2 * (p + l)
    return kel

def persegi_pl(p: int, l: int):
    return p * l

def jajar_genjang_k(a: int, b: int, c: int, d:int):
    return a + b + c + d

def jajar_genjang_l(a: int, t: int):
    return a * t

def segitiga_k(a: int, b: int, c: int):
    return a + b + c

def segitiga_l(a: int, t: int) -> float:
    return 1/2 * a * t

def belah_ketupat_k(a: int, b: int, c: int, d: int):
    return a + b + c + d

def belah_ketupat_l(d1: int, d2: int) -> float:
    return 1/2 * d1 * d2

def layang_k(a: int, b: int, c: int, d: int):
    return a + b + c + d

def layang_l(d1: int, d2: int) -> float:
    return 1/2 * d1 * d2

def trapesium_k(a: int, b: int, c: int, d: int):
    return a + b + c + d

def trapesium_l(a: int, b: int, t: int):
    return (a + b) / 2 * t

def lingkaran_k(r: int) -> float:
    return 2 * 3.14 * r

def lingkaran_l(r: int) -> float:
    return 3.14 * r ** 2
