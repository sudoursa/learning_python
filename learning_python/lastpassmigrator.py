import csv

with open("passpack_export.csv", "r", encoding='utf8')\
        as infile, open('final.csv', 'a', encoding='utf8') as outfile:
    fieldnames = ['\ufeff"Entry Name"', "User ID", "Password", "URL", "Notes", "Shared Notes", "Tags",
                  "Extra Fields", None]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in csv.DictReader(infile):
        writer.writerow(row)
