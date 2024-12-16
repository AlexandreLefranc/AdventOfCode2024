puzzle = []
with open("./input.example.txt", "r") as f:
    for line in f:
        line = line.strip()
        line_list = [i for i in line]
        puzzle.append(line_list)

def process_position_direction(row_i, col_i, dir):
    x_step = 0
    y_step = 0

    if "E" in dir:
        x_step = 1
    if "N" in dir:
        y_step = -1
    if "W" in dir:
        x_step = -1
    if "S" in dir:
        y_step = 1

    try:
        if row_i + 3 * y_step < 0:
            return 0
        if col_i + 3 * x_step < 0:
            return 0

        if (    puzzle[row_i + 0 * y_step][col_i + 0 * x_step] == "X"
            and puzzle[row_i + 1 * y_step][col_i + 1 * x_step] == "M"
            and puzzle[row_i + 2 * y_step][col_i + 2 * x_step] == "A"
            and puzzle[row_i + 3 * y_step][col_i + 3 * x_step] == "S"):
            return 1
        else:
            return 0
    except IndexError:
        return 0

def process_position(row_i, col_i):
    position_count = 0
    position_count += process_position_direction(row_i, col_i, "E")
    position_count += process_position_direction(row_i, col_i, "NE")
    position_count += process_position_direction(row_i, col_i, "N")
    position_count += process_position_direction(row_i, col_i, "NW")
    position_count += process_position_direction(row_i, col_i, "W")
    position_count += process_position_direction(row_i, col_i, "SW")
    position_count += process_position_direction(row_i, col_i, "S")
    position_count += process_position_direction(row_i, col_i, "SE")
    return position_count


count = 0
for col_i in range(len(puzzle)):
    for row_i in range(len(puzzle[col_i])):
        count += process_position(row_i, col_i)

print(count)

# Part 2
def process_position_part2(row_i, col_i):
    if puzzle[row_i][col_i] != "A":
        return 0
    
    if (row_i == 0
        or col_i == 0
        or row_i == len(puzzle) - 1
        or col_i == len(puzzle[row_i]) - 1):
        return 0
    
    first_diagonal = "".join([
        puzzle[row_i + 1][col_i + 1],
        puzzle[row_i - 1][col_i - 1]
    ])

    second_diagonal = "".join([
        puzzle[row_i + 1][col_i - 1],
        puzzle[row_i - 1][col_i + 1]
    ])
    
    if (
        ("M" in first_diagonal and "S" in first_diagonal)
        and ("M" in second_diagonal and "S" in second_diagonal)
        ):
        return 1
    else:
        return 0

count = 0
for col_i in range(len(puzzle)):
    for row_i in range(len(puzzle[col_i])):
        count += process_position_part2(row_i, col_i)

print(count)