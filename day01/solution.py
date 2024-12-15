# Input loading
left_list = []
right_list = []

with open("./input.txt", "r") as f:
    for line in f:
        row = line.strip().split()
        left_list.append(int(row[0]))
        right_list.append(int(row[1]))

# Solution part 1
left_list.sort()
right_list.sort()

total = 0
for (left, right) in zip(left_list, right_list):
    total += abs(left - right)

print(total)

# Solution part 2

right_list_count = {}
for value in right_list:
    if right_list_count.get(value):
        right_list_count[value] += 1
    else:
        right_list_count[value] = 1

similarity_score = 0
for left_value in left_list:
    value_count = right_list_count.get(left_value)
    if value_count:
        similarity_score += left_value * value_count

print(similarity_score)