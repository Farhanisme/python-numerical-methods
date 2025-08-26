from decimal import Decimal, getcontext

# Tentukan presisi perhitungan (jumlah desimal lebih tinggi untuk akurasi)
getcontext().prec = 10

def f(x):
    # Fungsi utama f(x) = 6x^5 + 3x^4 + x^6 + 3
    term1 = Decimal(6) * x**5
    term2 = Decimal(3) * x**4
    term3 = Decimal(1) * x**6
    term4 = Decimal(3)
    fx = term1 + term2 + term3 + term4
    print(f"  f(x) = 6({x})^5 + 3({x})^4 + 1({x})^6 + 3 = {term1} + {term2} + {term3} + {term4} = {fx}")
    return fx

def f_prime(x):
    # Turunan f(x) yaitu f'(x) = 30x^4 + 12x^3 + 6x^5
    term1 = Decimal(30) * x**4
    term2 = Decimal(12) * x**3
    term3 = Decimal(6) * x**5
    fpx = term1 + term2 + term3
    print(f"  f'(x) = 30({x})^4 + 12({x})^3 + 6({x})^5 = {term1} + {term2} + {term3} = {fpx}")
    return fpx

def newton_raphson(a, tolerance=Decimal('0.00000000000000001'), max_iterations=100):
    iteration = 1
    a = Decimal(a)  # Konversi a ke tipe Decimal
    
    while iteration <= max_iterations:
        print(f"\nIterasi {iteration}:")
        
        # Evaluasi f(a) dan f'(a) dengan substitusi rinci
        print(f"  a = {a}")
        fa = f(a)
        fpa = f_prime(a)
        
        # Hitung nilai b menggunakan rumus Newton-Raphson
        b = a - (fa / fpa)
        
        # Cetak substitusi rumus Newton-Raphson
        print(f"  b = a - (f(a) / f'(a)) = {a} - ({fa} / {fpa}) = {b}")
        
        # Evaluasi f(b) dengan substitusi rinci
        fb = f(b)
        print(f" f(b) = {fb}")

        print(f" |b-a| = {a} - {b} = {abs(b - a)}")
        
        # Cek kondisi penghentian
        if fb == 0:
            print("\nIterasi dihentikan, f(b) = 0")
            return b
        elif fb == tolerance:
            print("\nIterasi dihentikan, f(b) = nT")
            return b
        elif tolerance > fb > 0:
            print("\nIterasi dihentikan, nT < f(b) < 0")
            return b
        elif abs(b - a) < tolerance:
            print(f"\nIterasi dihentikan, b - a < nT: {b} - {a} < {tolerance}")
            return b
        
        # Pembaruan nilai a untuk iterasi berikutnya
        a = b
        iteration += 1
        print(f"\nIterasi belum mencapai syarat penghentian, nilai a sekarang adalah nilai b sebelumnya = {a}\n")

    # Jika batas iterasi tercapai
    print("\nBatas iterasi maksimum tercapai.")
    print(f"Akar aproksimasi: b = {b}")
    return b

# Parameter awal
a = -5
tolerance = Decimal('0.000000000000000000000000000000000000000000001')

# Panggil fungsi
newton_raphson(a, tolerance)
