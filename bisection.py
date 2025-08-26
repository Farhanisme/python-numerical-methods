from decimal import Decimal, getcontext

# Set presisi desimal
getcontext().prec = 10  # Presisi hingga 10 desimal

# Definisikan fungsi f(x)
def f(x):
    x = Decimal(x)
    return Decimal(6) * x**5 + Decimal(3) * x**4 + Decimal(1) * x**6  + Decimal(3)

# Metode Regula Falsi dengan tampilan perhitungan per iterasi
def BISECTION(a, b, tolerance=Decimal("0.00001"), max_iterations=50):
    a = Decimal(a)
    b = Decimal(b)
    iteration = 1

    while iteration <= max_iterations:
        # Hitung nilai f(a) dan f(b)
        fa = f(a)
        fb = f(b)
        # CESS
        # Menghitung nilai c dengan formula Regula Falsi
        c = (a+b)/2
        fc = f(c)
        
        # Menampilkan hasil perhitungan iterasi ini
        print(f"\nIterasi {iteration}")
        print(f"a = {a}")
        print(f"b = {b}")
        # print(f"a-b = {a-b}")
        # print(f"c = b - ( ((f(b) * (a - b)) / (f(a) - f(b)) ) = {b} - ( ({fb} * ({a} - {b})) / ({fa} - {fb}) ) = {c}")
        print(f"f(a) = 6({a})^5 + 3({a})^4 + 1({a})^6 + 3")
        print(f"f(a) = ({6*a**5} + {3*a**4} + {1*a**6} + 3)")
        print(f"f(a) = {fa}")

        print(f"f(b) = 6({b})^5 + 3({b})^4 + 1({b})^6 + 3")
        print(f"f(b) = ({6*b**5} + {3*b**4} + {1*b**6} + 3)")
        print(f"f(b) = {fb}")
        print(f"c = {c}")
        print(f"f(c) = f({c}) = 6({c})^5 + 3({c})^4 + 1({c})^6 + 3")
        print(f"f(c) = ({6*c**5} + {3*c**4} + {1*c**6} + 3) \n= {fc}")

        # Memeriksa tanda untuk menentukan nilai a atau b pada iterasi berikutnya
        if fa * fc < 0:
            print("f(a) * f(c) < 0, maka b = c")
            b = c
        else:
            print("f(a) * f(c) > 0, maka a = c")
            a = c

        # Cek apakah fc sudah cukup dekat ke 0 atau sesuai toleransi
        if abs(fc) < tolerance:
            print(f"\nSolusi ditemukan pada iterasi ke-{iteration}: x ≈ {c} dengan f(c) ≈ {fc}")
            return c
        
        iteration += 1
        print("")  # Pemisah antar iterasi

    print("\nSolusi tidak ditemukan dalam batas iterasi yang ditentukan.")
    return None

# Panggil fungsi dengan nilai awal dan toleransi yang diberikan
BISECTION(a=0, b=-5, tolerance=Decimal("0.00001"))

