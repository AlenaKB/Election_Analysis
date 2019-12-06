#the data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received voted
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#assign a variable for the file to load and the path
import csv
import os
#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)
#file_to_load = "/Users/Kortney/Desktop/Election_Analysis/resources/election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")
#open the election results and read the file

file_to_save = os.path.join("analysis", "election_results.txt")
with open(file_to_save, "w") as txt_file:
  txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")
total_votes = 0
#pcandidate options
candidate_options = []
#create an empty dictionary 
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
  #to do: read and analyze data here
    file_reader = csv.reader(election_data)
    #read and print the header row
    headers = next(file_reader)
    for row in file_reader:
      total_votes += 1
      candidate_name = row[2]
      #if the candidate name is not matching any existing name
      if candidate_name not in candidate_options:
        #add it to the list
        candidate_options.append(candidate_name)
      #begine tracking candidate's vote count
        candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
  election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    )
  print(election_results, end = '')
  txt_file.write(election_results)
  #interate through the candidate list
  for candidate in candidate_votes:
    #retrieve votes fro each candidate
    votes = candidate_votes[candidate]
    #calcualet the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)
    txt_file.write(candidate_results)  
    #determine if the votes is greate than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
      winning_count = votes
      winning_percentage = vote_percentage
    #set the winningn candidate equl to candidates name
      winning_candidate = candidate
  winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
  print(winning_candidate_summary)
  txt_file.write(winning_candidate_summary)

#print(candidate_votes)
      

