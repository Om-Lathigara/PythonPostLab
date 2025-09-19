with open(r"C:\Users\aumla\Downloads\example.txt") as f1, open(r"C:\Users\aumla\Downloads\ex1.txt") as f2, open("C:\Users\aumla\Downloads\merged.txt", "w") as f3:
    f3.write(f1.read())
    f3.write(f2.read())
