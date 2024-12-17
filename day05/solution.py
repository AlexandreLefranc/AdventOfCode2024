# extract rules as list of 2-tuples
# extract page ordering as list of lists
rules = []
page_ordering = []
with open("./input.txt", "r") as f:
    type = "rules"
    for line in f:
        if line == "\n":
            type = "ordering"
        elif type == "rules":
            rule = line.strip().split("|")
            rules.append(tuple([int(i) for i in rule]))
        elif type == "ordering":
            line_numbers = line.strip().split(",")
            line_numbers = [int(i) for i in line_numbers]
            page_ordering.append(tuple(line_numbers))

            
def is_rule_relevent(rule, page_ordering):
    if rule[0] in page_ordering and rule[1] in page_ordering:
        return True
    return False

def is_rule_valid(rule, page_ordering:list):
    first_index = page_ordering.index(rule[0])
    second_index = page_ordering.index(rule[1])

    if first_index < second_index:
        return True
    return False

def is_page_ordering_valid(rules, page_ordering):
    for r in rules:
        if not is_rule_relevent(r, page_ordering):
            continue

        if not is_rule_valid(r, page_ordering):
            return False

    return True


# for each page ordering
    # select relevant rules
    # check relevant rules
    # append valid page ordering to a list
valid_page_ordering = []
invalid_page_ordering = []
for po in page_ordering:
    is_valid = is_page_ordering_valid(rules, po)
    
    if is_valid:
        valid_page_ordering.append(po)
    else:
        invalid_page_ordering.append(po)



def get_middle_number(page_ordering):
    if len(page_ordering) % 2 == 0:
        print("Warning! Even length of page ordering")

    middle_index = int(len(page_ordering) / 2)

    return page_ordering[middle_index]

# for each valid page ordering
    # extract middle number
    # add it up
total = 0
for po in valid_page_ordering:
    total += get_middle_number(po)

print(total)

# Part 2
import itertools

# Ugly brute force... I have been lazy to find a smart way of doing it
# Way too long, didn't wait
def find_valid_permutation(invalid_page_ordering, rules):
    permutations = itertools.permutations(invalid_page_ordering, len(invalid_page_ordering))
    n_permutations = 2** len(invalid_page_ordering)

    for i, perm in enumerate(permutations):
        # print("  ", i, "/", n_permutations)
        if is_page_ordering_valid(rules, perm):
            return perm
        
    raise Exception("No valid permutation")


total = 0
for i, po in enumerate(invalid_page_ordering):
    print(i, "/", len(invalid_page_ordering))
    valid_permutation = find_valid_permutation(po, rules)
    
    total += get_middle_number(valid_permutation)

print(total)

