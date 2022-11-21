import csv

def load_table(data):
    file = open("database/fii_table.csv", "w")
    wtr = csv.writer(file, delimiter=';', lineterminator='\n')
    for x in data:
        wtr.writerow(x)
    file.close()