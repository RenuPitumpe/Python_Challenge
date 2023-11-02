import os
import csv
csv_file = os.path.join("./Resources/election_data.csv")

totalVotes = 0
candidates = {}
winnerName = ""
winnerVotes = 0

with open(csv_file, "r") as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)
    # print(header)

    for row in csv_reader:

        totalVotes = totalVotes + 1

        candidateName = row[2]
        # print(candidateName)
        # print(candidates)

        if candidateName in candidates:
            candidates[candidateName] += 1
        else:
            candidates[candidateName] = 1

results = []

for candidate, votes in candidates.items():
    percentage = (votes / totalVotes) * 100
    results.append((candidate, percentage, votes))
    if votes > winnerVotes:
        winnerName = candidate
        winnerVotes = votes

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winnerName}")
print("-------------------------")

output_file = "election_results.txt"
with open(output_file, "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {totalVotes}\n")
    f.write("-------------------------\n")
    for candidate, percentage, votes in results:
        f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winnerName}\n")
    f.write("-------------------------")