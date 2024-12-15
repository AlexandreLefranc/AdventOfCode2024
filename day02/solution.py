input = []
with open("./input.txt", "r") as f:
    for line in f:
        input.append([int(i) for i in line.strip().split()])


def is_report_safe(report):
    diffs = [report[i] - report[i + 1] for i, _ in enumerate(report[:-1])]
    
    sign = 1 if diffs[0] >= 0 else -1
    for diff in diffs:
        current_sign = 1 if diff >= 0 else -1
        if sign != current_sign:
            return False
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True

def is_problem_dampener_safe(report:list):
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        report_tmp = report[:]
        report_tmp.pop(i)
        if is_report_safe(report_tmp):
            return True
    
    return False

safe_reports = 0
for report in input:
    if is_problem_dampener_safe(report):
        safe_reports += 1

print(safe_reports)
