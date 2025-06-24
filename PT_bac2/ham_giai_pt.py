import math

def giai_pt_bac_2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            x = -c / b
            return f"Phương trình có một nghiệm: x = {x:.2f}"
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm."
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép: x₁ = x₂ = {x:.2f}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có 2 nghiệm phân biệt:\n\nx₁ = {x1:.2f}\n\nx₂ = {x2:.2f}"
