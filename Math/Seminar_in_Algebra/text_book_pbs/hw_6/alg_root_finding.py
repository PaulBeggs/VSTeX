def confirm_field(n):
    for c in range(n):
        has_root = any((x ** 3 + x ** 2 + c) % n == 0 for x in range(n))
        
        if not has_root:
            print(f"{c = } works! x^3 + x^2 + {c} is irreducible over Z_{n}.")
        else:
            print(f"{c = } fails. It has at least one root.")

confirm_field(3)