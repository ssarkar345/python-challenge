# Dependencies
import os
import csv
# path to csv
election_csv= os.path.join(".","Resources","election_data.csv")
#Lists for columns
ballots=[]
candidates=[]
# open and read csv
with open(election_csv) as electiondata:
    election_reader=csv.reader(electiondata)
    #Skip header
    header=next(electiondata)
    #Creating Lists of each column to perform functions
    for row in election_reader:
        ballots.append(row[0])
        candidates.append(row[2])

print("Election Results")
print("------------")
# The total votes will be the length of a list of ballots
totalvotes= len(ballots)
print(f"Total Votes: {totalvotes}")
print("------------")
#unique list of ballot names
unique=[]
for name in candidates:
    if name not in unique:
        unique.append(name)
# number of times each name showed up divided by len of list 1 is percentage of votes
charles= candidates.count(unique[0])
charlesp=(charles/totalvotes)*100
charlesv=charlesp*totalvotes
diana=candidates.count(unique[1])
dianap=(diana/totalvotes)*100
dianav=dianap*totalvotes
raymon=candidates.count(unique[2])
raymonp=(raymon/totalvotes)*100
raymonv=raymonp*totalvotes
# Getting the winner
votes=[charlesv,dianav,raymonv]
if max(votes)==charlesv:
    winner="Charles Casper Stockham"
if max(votes)==dianav:
    winner="Diana DeGette"
else:
    winner="Raymon Anthony Doane"
print(f"{unique[0]}: {charlesp}% ({charlesv})")
print(f"{unique[1]}: {dianap}% ({dianav})")
print(f"{unique[2]}: {raymonp}% ({raymonv})")

print("------------")
print(f"Winner: {winner}")

# Create path for output file
electionresults= os.path.join(".","Analysis","ElectionResults.txt")
with open(electionresults,"w") as file:
    file.write("Election Results \n")
    file.write("-----------------\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write("------------------\n")
    file.write(f"{unique[0]}: {charlesp}% ({charlesv})\n")
    file.write(f"{unique[1]}: {dianap}% ({dianav})\n")
    file.write(f"{unique[2]}: {raymonp}% ({raymonv})\n")
    file.write("-------------------\n")
    file.write(f"Winner: {winner}\n")
