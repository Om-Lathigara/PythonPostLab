with open(r"C:\Users\aumla\Downloads\example.txt", 'r') as f1, \
     open(r"C:\Users\aumla\Downloads\ex1.txt", 'r') as f2, \
     open(r"D:\MARWADI\YEAR2\SEM3\PYTHON\13\merged.txt", 'w') as fout:
    fout.write(f1.read())
    fout.write("\n")
    fout.write(f2.read())
