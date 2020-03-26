# Let’s import the os module
import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#Lists to store data
date = []
profit_losses = []
total_months = 0
amount_PandL = 0
average_changes = 0

# Open and read CSV files
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Read the header row first
csv_header = next(csvreader)



