with open("Day-1-2021.txt", "r") as f:
    line = int(f.readline().strip())
    increasing = 0
    while line:
        new_line = int(f.readline().strip())
        if new_line > line:
            increasing += 1
        print(f"{new_line}, {line}, {increasing}")
        line = new_line
