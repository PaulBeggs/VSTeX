import random
import string
import pyperclip

def generate_identifier(length=7):
    """Generate a random identifier of a given length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

matrix = [
[(44, 57, 27), (38, 49, 23), (37, 48, 22), (35, 45, 21), (38, 50, 23), (33, 42, 20), (35, 46, 21), (31, 41, 19), (30, 39, 18), (30, 39, 18), (30, 40, 18), (28, 36, 17), (28, 37, 17), (21, 28, 13), (23, 30, 14), (21, 28, 13)],
[(43, 56, 26), (38, 48, 22), (41, 54, 25), (36, 48, 22), (41, 51, 24), (36, 30, 18), (35, 45, 21), (30, 37, 18), (34, 44, 21), (30, 39, 18), (30, 40, 19), (27, 36, 16), (28, 35, 17), (22, 30, 14), (24, 32, 15), (20, 26, 12)],
[(39, 46, 23), (41, 35, 22), (43, 53, 25), (34, 44, 21), (40, 50, 24), (36, 28, 18), (33, 38, 19), (33, 28, 16), (34, 43, 20), (31, 40, 19), (29, 38, 18), (30, 37, 17), (28, 22, 14), (21, 25, 12), (23, 28, 14), (23, 19, 11)],
[(43, 33, 23), (47, 43, 40), (43, 32, 22), (42, 33, 20), (37, 43, 21), (39, 28, 18), (37, 26, 17), (35, 26, 17), (29, 33, 16), (31, 25, 15), (28, 32, 16), (30, 25, 16), (36, 25, 17), (28, 20, 14), (25, 18, 12), (30, 21, 15)],
[(60, 43, 30), (53, 39, 27), (65, 46, 32), (72, 51, 35), (44, 32, 20), (58, 42, 28), (49, 34, 23), (44, 31, 21), (34, 24, 16), (33, 23, 15), (32, 24, 16), (35, 32, 30), (39, 28, 20), (42, 29, 20), (29, 20, 13), (33, 23, 16)],
[(54, 38, 26), (44, 30, 21), (63, 45, 31), (64, 46, 32), (53, 39, 28), (60, 44, 30), (41, 29, 19), (39, 27, 18), (38, 26, 18), (44, 31, 21), (43, 31, 21), (35, 25, 18), (39, 27, 18), (39, 27, 19), (36, 26, 18), (48, 34, 24)],
[(72, 51, 35), (52, 36, 25), (54, 37, 25), (54, 40, 29), (57, 53, 50), (52, 39, 28), (52, 36, 24), (69, 50, 34), (67, 48, 33), (49, 34, 23), (63, 45, 31), (60, 43, 29), (42, 30, 20), (45, 32, 22), (39, 27, 19), (43, 31, 21)],
[(54, 38, 26), (53, 37, 26), (72, 51, 35), (72, 52, 36), (62, 47, 34), (60, 43, 30), (52, 36, 24), (53, 38, 26), (59, 42, 29), (41, 28, 19), (55, 40, 27), (54, 39, 27), (42, 29, 20), (40, 28, 19), (44, 31, 21), (44, 31, 22)],
[(58, 41, 28), (51, 35, 24), (53, 38, 26), (61, 43, 30), (52, 37, 25), (58, 42, 28), (48, 34, 23), (40, 27, 19), (50, 35, 24), (55, 40, 27), (55, 39, 27), (46, 32, 22), (43, 31, 21), (41, 29, 20), (33, 23, 15), (37, 26, 18)],
[(52, 36, 25), (55, 40, 27), (40, 28, 19), (50, 35, 24), (49, 34, 24), (40, 28, 18), (40, 28, 18), (47, 33, 22), (48, 33, 23), (51, 36, 25), (49, 34, 23), (46, 32, 22), (61, 44, 30), (59, 42, 29), (41, 30, 21), (44, 31, 21)],
[(50, 35, 24), (56, 40, 28), (50, 35, 24), (68, 49, 33), (67, 48, 33), (50, 35, 24), (64, 46, 31), (57, 41, 27), (41, 30, 21), (66, 48, 33), (66, 48, 33), (40, 28, 19), (53, 38, 26), (54, 39, 28), (45, 41, 38), (39, 29, 22)],
[(55, 39, 27), (48, 33, 22), (49, 35, 24), (58, 42, 29), (61, 44, 30), (66, 48, 32), (53, 38, 26), (55, 40, 29), (44, 39, 36), (58, 42, 30), (58, 41, 28), (45, 31, 22), (37, 26, 17), (50, 36, 25), (43, 32, 23), (33, 23, 16)],
[(45, 32, 22), (39, 27, 18), (53, 38, 26), (48, 34, 23), (55, 40, 28), (59, 43, 29), (64, 46, 31), (49, 35, 24), (45, 33, 24), (46, 32, 22), (48, 34, 23), (45, 32, 22), (44, 31, 21), (47, 33, 23), (59, 42, 29), (57, 41, 29)],
[(46, 32, 22), (51, 36, 25), (46, 32, 22), (46, 32, 22), (44, 33, 24), (46, 33, 23), (55, 40, 27), (52, 38, 26), (45, 32, 22), (39, 27, 18), (59, 42, 30), (39, 27, 18), (45, 31, 21), (61, 44, 30), (56, 40, 28), (53, 38, 26)],
[(53, 37, 26), (44, 31, 21), (40, 28, 19), (60, 43, 30), (44, 31, 22), (36, 24, 17), (43, 31, 22), (39, 27, 19), (61, 44, 30), (61, 44, 30), (49, 34, 24), (50, 35, 25), (45, 32, 22), (47, 33, 23), (52, 38, 26), (51, 36, 25)],
[(52, 37, 25), (45, 32, 22), (59, 43, 30), (56, 40, 28), (51, 36, 24), (43, 31, 23), (46, 43, 40), (43, 31, 23), (54, 39, 26), (54, 39, 27), (44, 31, 21), (45, 32, 21), (51, 36, 25), (51, 37, 25), (44, 31, 21), (35, 24, 16)],
]

# Prepare lists to store the commands.
definecolor_commands = []
draw_commands_by_row = []  # list of tuples: (row_number, list of draw commands for that row)

# Process each row (from top to bottom).
for r, row in enumerate(matrix):
    row_draw_commands = []
    for c, rgb in enumerate(row):
        ident = generate_identifier()
        definecolor_commands.append(
            f"\\definecolor{{{ident}}}{{RGB}}{{{rgb[0]}, {rgb[1]}, {rgb[2]}}}"
        )
        draw_command = (
            f"\\draw[fill={ident}] ({15 - c}, 16, {16 - r}) -- "
            f"({15 - c+1}, 16, {16 - r}) -- "
            f"({15- c+1}, 16, {15 - r}) -- "
            f"({15- c}, 16, {15 - r}) -- cycle;"
        )
        row_draw_commands.append(draw_command)
    # Save draw commands for this row (row numbers are 1-indexed for clarity).
    draw_commands_by_row.append((r + 1, row_draw_commands))

# Build the final output list.
output = []
output.append("% Define color commands\n")
for cmd in definecolor_commands:
    output.append(cmd + "\n")

output.append("\n% Draw commands\n")
for row_num, cmds in draw_commands_by_row:
    output.append(f"\n% Row {row_num}\n")
    for cmd in cmds:
        output.append(cmd + "\n")

# Copy the entire output to clipboard.
final_output = "".join(output)
pyperclip.copy(final_output)
# print(final_output)
