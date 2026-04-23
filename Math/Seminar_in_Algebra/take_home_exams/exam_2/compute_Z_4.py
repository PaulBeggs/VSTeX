def generate_elts():
    # Matches your order: 0, 1, 2, 0+a, 1+a, 2+a, 0+2a...
    return [(a, b) for b in range(3) for a in range(3)]

def add_mod3(e1, e2):
    return ((e1[0] + e2[0]) % 3, (e1[1] + e2[1]) % 3)

def mul_mod3(e1, e2):
    a, b = e1
    c, d = e2
    # Since a^2 = -1, (a+ba)(c+da) = ac + ad(a) + bc(a) - bd
    real_part = (a * c - b * d) % 3
    alpha_part = (a * d + b * c) % 3
    return (real_part, alpha_part)

def elt_to_latex(a, b):
    # Formats the tuple directly to LaTeX without string parsing
    if a == 0 and b == 0: return "0"
    if a == 0 and b == 1: return "$\\alpha$"
    if a == 0 and b == 2: return "$2\\alpha$"
    
    if b == 0: return f"${a}$"
    if b == 1: return f"${a} + \\alpha$"
    
    return f"${a} + {b}\\alpha$"

def generate_latex_table(op_symbol, op_func, elts):
    lines = []
    # Setup LaTeX array alignment: 1 col for the outer elements, a vertical line, 9 cols for inner
    align = "c|" + "c" * len(elts)
    lines.append(f"\\begin{{array}}{{{align}}}")
    
    # Header Row
    header = [op_symbol] + [elt_to_latex(*e) for e in elts]
    lines.append(" & ".join(header) + " \\\\")
    lines.append("\\hline")
    
    # Generate the table rows
    for e1 in elts:
        row = [elt_to_latex(*e1)] # Outer left element
        for e2 in elts:
            res = op_func(e1, e2)
            row.append(elt_to_latex(*res))
        lines.append(" & ".join(row) + " \\\\")
        
    lines.append("\\end{array}")
    return "\n".join(lines)


elements = generate_elts()

addition_table_latex = generate_latex_table("+", add_mod3, elements)
multiplication_table_latex = generate_latex_table("\\cdot", mul_mod3, elements)

print("Addition Table:")
print(addition_table_latex)
print("\nMultiplication Table:")
print(multiplication_table_latex)