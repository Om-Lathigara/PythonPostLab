with open(r"C:\Users\aumla\Downloads\example.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
print(lines)
