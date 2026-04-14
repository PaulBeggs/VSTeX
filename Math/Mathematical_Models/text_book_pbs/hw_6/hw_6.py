import math

def find_ci(b_diodes, tot_n, q):
    p = 1 - q
    mu = q

    x_bar = b_diodes / tot_n
    print(f"Observed average: {x_bar}")

    var = (1 - mu) ** 2 * q + (0 - mu) ** 2 * p
    std = math.sqrt(var)
    print(std)

    left_bound =  mu - 2 * (std / math.sqrt(tot_n)) 
    right_bound =  mu + 2 * (std / math.sqrt(tot_n)) 

    return [left_bound, right_bound] 


def find_diodes(q, tolerance, check=False):
    p = 1 - q
    mu = q

    var = (1 - mu) ** 2 * q + (0 - mu) ** 2 * p
    std = math.sqrt(var)

    error = q * tolerance

    diodes = ((2 * std) / error) ** 2
    if check:
        left_bound =  mu - 2 * (std / math.sqrt(diodes)) 
        right_bound =  mu + 2 * (std / math.sqrt(diodes))
        print(f"Left bound expected: {q - error}, actual: {left_bound}")
        print(f"Right bound expected: {q + error}, actual: {right_bound}")
    return diodes


def find_win_chance(num_digits, tickets_per_week):
    win_prob = 1 / 10 ** num_digits  # 10 choices per digit
    lose_prob = 1 - win_prob
    tot_weeks = 52  # Total weeks in a year
    entries = tickets_per_week * tot_weeks
    yearly_win_prob = 1 - lose_prob ** entries
    return yearly_win_prob


def get_latex_table_for(num_digits, total_tickets):
    win_prob = 1 / 10 ** num_digits  # 10 choices per digit
    lose_prob = 1 - win_prob
    tot_weeks = 52  # Total weeks in a year
    probs = []
    ns = []
    for ticket in range(1, total_tickets):
        entries = ticket * tot_weeks
        probs.append(str(round(1 - lose_prob ** entries, 4)))
        ns.append(str(ticket))
    return " & ".join(ns), " & ".join(probs)


def get_ci_for(tickets_per_week, debug=False):
    price_per_ticket = 1
    payout_per_win = 500

    # chance of paying out for 1 ticket
    p = 1 / (10 ** 3) 

    # Expected payout for one ticket
    Ex = payout_per_win * p

    # Variance for one ticket
    Vx = (payout_per_win ** 2 * p) - Ex ** 2

    # Scale up to 1,000,000 tickets 
    mu = tickets_per_week * Ex
    var = tickets_per_week * Vx
    if var < 0:
        var = -var
    std = math.sqrt(var)
    if debug:
        print(f"{mu = }\n{var = }\n{std = }")
    left_bound = mu + 2 * std
    right_bound = mu - 2 * std
    return [left_bound, right_bound]  # returns [531606.96, 468393.04]



def main():
    print(get_ci_for(1_000_000, debug=True))
    print(get_latex_table_for(3, 10))
    print(find_win_chance(3, 50))
    print(find_diodes(0.003, .01, check=True))
    print(find_ci(30, 10000, 0.003))

if __name__ == "__main__":
    main()