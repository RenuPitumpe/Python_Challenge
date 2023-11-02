import csv

totalMonths = 0
netTotal = 0
previousProfitLoss = 0
profitLossChanges = []
dates = []

with open('C:/Users/Dilrukshi/Desktop/Python_Challenge/PyBank/Resources/budget_data.csv', 'r') as file:
    csvReader = csv.reader(file)

    for row in csvReader:
      # print(row)

      # header = next(csv_reader)
      # print(header)

      date = row[0]
      # print(date)

      if row[0] == 'Date' and row[1] == 'Profit/Losses':
        continue

      profitLoss = int(row[1])
      # print(profitLoss)

      totalMonths = totalMonths + 1
      # print(total_months)
      netTotal = netTotal + profitLoss

      if totalMonths > 1:
            profitLossChange = profitLoss - previousProfitLoss
            profitLossChanges.append(profitLossChange)
            dates.append(date)

      previousProfitLoss = profitLoss

averageChange = sum(profitLossChanges) / (totalMonths - 1)
greatestIncrease = max(profitLossChanges)
greatestDecrease = min(profitLossChanges)

greatestIncreaseDate = dates[profitLossChanges.index(greatestIncrease)]
greatestDecreaseDate = dates[profitLossChanges.index(greatestDecrease)]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChange:.2f}")
print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})")

# Export to a text file
fileOutput = "C:/Users/Dilrukshi/Desktop/Python_Challenge/PyBank/analysis/financial_analysis.txt"
with open(fileOutput, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {totalMonths}\n")
    output_file.write(f"Total: ${netTotal}\n")
    output_file.write(f"Average Change: ${averageChange:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})\n")
