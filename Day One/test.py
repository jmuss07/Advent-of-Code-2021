with open("Day-1-2021.txt", "r") as f, open("out_day-1.txt", "w") as of:
    line = f.readline().strip()
    counter = 1
    increasing = 0
    while line:
        old_line = line
        new_line = f.readline().strip()
        if new_line > old_line:
            increasing += 1
        print(f"{line}, {old_line}, {new_line}, {new_line > old_line}, {increasing}", file=of)
        line = new_line
        counter += 1
