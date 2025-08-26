from decimal import Decimal, getcontext


getcontext().prec = 10 

def secant_method(f, a, b, tol=Decimal('0.00'), max_iter=100):
    a, b = Decimal(a), Decimal(b) 
    tol = Decimal(tol)

    for i in range(max_iter):

        f_a = f(a)
        f_b = f(b)


        if f_a == f_b:
            print("Error: f(a) and f(b) terlalu dekat atau sama.")
            return None

        c = b - (f_b * (a - b)) / (f_a - f_b)
        f_c = f(c)

# CESSS
        print(f"\n\nIterasi {i+1}")
        print(f"a = {a}")
        print(f"b = {b}")
        # print(f"a-b = {a-b}")
        print(f"f(a) = {f_a}")
        print(f"f(b) = {f_b}")
        # print(f"f(a) = f({a}) = 2({a})^3 + 3({a})^2 + 5({a}) + 15 = {f_a}")
        # print(f"f(b) = f({b}) = 2({b})^3 + 3({b})^2 + 5({b}) + 15 = {f_b}")

        print(f"f(a) = f({a}) = {6*a**5} + {3*a**4} + {1*a**6} + 3 = {f_a}")
        print(f"f(b) = f({b}) = {6*b**5} + {3*b**4} + {1*b**6} + 3 = {f_b}")

        # c_calculation = f"c = {b} - (({f_b} * ({a} - {b})) / ({f_a} - {f_b}))"
        # c_calculation = f"c = b - ((f(b) * (a - b)) / (f(a) - f(b))) = {b} - (({f_b} * ({a} - {b})) / ({f_a} - {f_b}))"
        c_calculation_result = f"c = {b} - (({f_b} * ({a} - {b})) / ({f_a} - {f_b})) \n= {c}"
        print(c_calculation_result)
        # print(c_calculation + c_calculation_result)

        
        # f_c_calculation = f"f(c) = {f_c}"
        f_c_calculation = f"f(c) = ({6*c**5} + {3*c**4} + {1*c**6} + 3) \n= {f_c}"
        # f_c_calculation = f"f(c) = f({c}) = 2({c})^3 + 3({c})^2 + 5({c}) + 15 \n= ({2*c**3} + {3*c**2} + {5*c} + 15) \n= {f_c}"
        print(f_c_calculation)


        if abs(f_c) < tol:
            print(f"\nAkar ditemukan: x = {c}, setelah {i+1} iterasi dengan f(c) mendekati nol dalam toleransi.")
            return c
        
        a, b = b, c 
        # print(f"\nUpdate nilai: a = {a}, b = {b}\n")

    print("Akar tidak ditemukan dalam iterasi maksimum.")
    return None

f = lambda x: Decimal(6) * x**5 + Decimal(3) * x**4 + Decimal(1) * x**6 + Decimal(3)

secant_method(f, a=0, b=-5)
