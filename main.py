import csv

def barbat(path: str):
    file = open(path)
    dct = {}
    print("Alege un numar, barbat SIGMA:")
    nr = input()
    for line in csv.reader(file):
        dct[line[0]] = line[1]

    for key, value in dct.items():
        if key == nr:
            print(f"{key}: {value}")
    print("FII SIGMA!")

barbat("Set of rules to be a MAN.csv")