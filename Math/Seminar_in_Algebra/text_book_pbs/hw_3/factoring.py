def factor(mod_list):
    for m in mod_list:
        sol = ((2 * (m ** 3) % 11) + (3 * (m ** 2) % 11) + (4 * m % 11) - 5) % 11
        # sol = (m ** 2 + m  + 1) % 7
        if sol == 0:
            print(f"Found root: {m}")
        else:
            print(f"{sol=}")

# mod_list = [m for m in range(11)]
# factor(mod_list)

def find_root(factors):
    vals_to_check = [(-f, f) for f in factors]
    for pos_val, neg_val in vals_to_check:
        if pos_val ** 3 + 3 * pos_val - 8 == 0:
            print(f"Found root at {pos_val}")
        else:
            print(f"None found for {pos_val}")
        if neg_val ** 3 + 3 * neg_val - 8 == 0:
            print(f"Found root at {neg_val}")
        else:
            print(f"None found for {neg_val}")

find_root([1,2,4,8])
