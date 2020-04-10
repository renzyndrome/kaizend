import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
args = parser.parse_args()

output_filename = input("Enter filename of the CSV output file: ")

with open(args.filename, "r") as file:
    reader = csv.DictReader(file)
    with open(output_filename, mode='w') as csv_file:
        line_count = 0
        for row in reader:
            if line_count == 0:
                writer = csv.DictWriter(csv_file, fieldnames=row)
                writer.writeheader()
                line_count += 1

            if row["Categories"]:
                writer.writerow(row)
            line_count += 1
print(f'Successful! Please check {output_filename} for the result')
