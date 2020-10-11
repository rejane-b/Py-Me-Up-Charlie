import csv

# Populate candidate list
candidates = {
    "Khan":0,
    "Correy":0,
    "Li":0,
    "O'Tooley":0
}

# Initialize variables
total_votes=0

# Count the votes
with open('Resources/election_data.csv', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)
    data.pop(0)
    total_votes=len(data)
    for item in data:
        if item[2]=="Khan":
            candidates["Khan"]+=1
        if item[2]=="Correy":
            candidates["Correy"]+=1
        if item[2] == "Li":
            candidates["Li"] += 1
        if item[2]=="O'Tooley":
            candidates["O'Tooley"]+=1


print("Election Results")
print("-------------------------")
print("Total Votes:",total_votes)
print("-------------------------")

# Determine the winner
winner = ""
winner_votes=0
for key in candidates.keys():
    percent = (candidates[key]*100)/total_votes
    print(f"{key}: {round(percent,2)}% ({candidates[key]})")
    if candidates[key] > winner_votes:
        winner = key
        winner_votes = candidates[key]

print("-------------------------")
print("Winner:",winner)
print("-------------------------")