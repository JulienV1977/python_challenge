# Let’s import the os module
import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline="")
csv_reader = csv.reader(csvfile, delimiter=",")
csv_headers = next(csv_reader, None)
print(f"csv header: {csv_headers}")