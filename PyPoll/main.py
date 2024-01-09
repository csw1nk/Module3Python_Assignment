import csv  
csvfile = 'Resources/election_data.csv'
# used a reference article for code here: https://www.geeksforgeeks.org/dictionary-counter-python-find-winner-election/
# setting variables for my vote tallies, candidates and eventual winner
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# using csv library to open the file as read then start tallying the votes in column A or index 0 
with open(csvfile, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) #skipping the headerrow

    for row in csv_reader: #looping through each row in the file
        total_votes += 1  #for the total votes variable above we are iterating +1 for each row
        candidate = row[2]  #we are extracting the candidates name in each row in the third column
        #then we need to count each vote for each candidate
        if candidate in candidates: #we created a dictionary for candidates above now we are checking if the candidate is already in the candidate dictionary
            candidates[candidate] += 1 #if yes, then we add one vote to that candidate
        else:
            candidates[candidate] = 1 #this is error handling saying if not just add to dictionary with 1 vote

# creating percentages of votes to candidates and determine the winner
for candidate, votes in candidates.items(): #.items return a list of pairs found this in reference code article: https://www.geeksforgeeks.org/dictionary-counter-python-find-winner-election/
    if votes > max_votes: #checking if current candidate vote count is greater than the loop or previous value
        max_votes = votes #setting max votes to highest vote count
        winner = candidate #setting winner to candidate with highest vote counts through loop
    percentage = (votes / total_votes) * 100 #calculating the percentage
    candidates[candidate] = (votes, percentage) #updating the dictionary

# Print the election results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate, (votes, percentage) in candidates.items(): #this is looping through each candidate and presenting their results
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("----------------------------")
print(f"Winner: {winner}")#finally setting the winner
print("----------------------------")

# #writing results to analysis folders, similar to PyBank with headers of Metric and Value
output_csv_file = 'analysis/election_results.csv'
headers = ["Metric", "Value"]
with open(output_csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    #writing out the total votes and its value
    writer.writerow(["Total Votes", total_votes])
    # writing each candidates vote count using looping for each candidate - candidate name and how much votes is the .items function
    for candidate, (votes, _) in candidates.items():
        writer.writerow([candidate, votes])
    # write out the winner
    writer.writerow(["Winner", winner])

#checking that results printed correctly to folder
print(f"Results written to: {output_csv_file} successfully")