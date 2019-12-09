#the data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received voted
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#assign a variable for the file to load and the path
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
#open the election results and read the file
file_to_save = os.path.join("analysis", "election_results.txt")
with open(file_to_save, "w") as txt_file:
  txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")
total_votes = 0
# candidate options
candidate_options = []
# create an empty dictionary 
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#create a list for counties       
counties = []
#create a dictionary for counties and votes cast in each of them
counties_dict = {}
#create an empty string that will hold the largest turnout variable
largest_turnout = ""
with open(file_to_load) as election_data:
  #to do: read and analyze data here
    file_reader = csv.reader(election_data)
    # read and print the header row
    headers = next(file_reader)
    for row in file_reader:
      total_votes += 1
      candidate_name = row[2]
      # if the candidate name is not matching any existing name
      if candidate_name not in candidate_options:
        #add it to the list
        candidate_options.append(candidate_name)
      # begin tracking candidate's vote count
        candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1  
      county_name = row[1]  
      # getting county's name and vote cast in the dictionary
      if county_name not in counties:
        counties.append(county_name)
        counties_dict[county_name] = 0
      counties_dict[county_name] += 1
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
    #print the candidate results
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
  # write the results in the election_results
  txt_file.write(winning_candidate_summary)
  #initiate a varibale for votes each county received
  votes_by_county = row[0]
  #iterate through the votes each county received
  for county_name, votes_by_county in counties_dict.items():
    votes_by_county = counties_dict[county_name] 
    #find the number of votes for each county
    if county_name not in counties_dict:
      counties_dict[county_name] += 1
    # print out the results   
    county_results = (f"{county_name} county has {votes_by_county} vote count\n" )
    #print the results
    print(county_results)
    txt_file.write(county_results)
     # get the county with the largest turnout 
  largest_turnout = max(counties_dict, key=counties_dict.get) 
  # print the result in the output file
  print(f"The county with the largest turnout is: {largest_turnout}\n")
  txt_file.write(f"The county with the largest turnout is: {largest_turnout}")

      

