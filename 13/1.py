with open(r"C:\Users\aumla\Downloads\example.txt") as f:
    text = f.read()
lines = text.splitlines()
words = text.split()
print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))
