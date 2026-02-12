def find_mod(a, mod):
    to_mod = a * a
    result = to_mod % mod
    if a == result:
        return a

# mod_list = []

# for val in range(7):
#     mod_list.append(find_mod(val, 6))

# print(mod_list)

def solve_sys_of_eq(nums, mod_val):
    eqs = {}
    for idx, num in enumerate(nums):
        eqs[idx] = (num ** 2 + 2 * num + 4) % mod_val
    return eqs

print(solve_sys_of_eq(range(7), 6))
    