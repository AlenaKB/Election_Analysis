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
counties_names = []
county_votes ={}
#create a dictionary for counties and votes cast in each of them
counties_dict = {}
#create an empty string that will hold the largest turnout variable
largest_turnout = ""
county_percentage = 0
votes_by_county = 0
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
      if county_name not in counties_names:
        counties_names.append(county_name)
        counties_dict[county_name] = 0
      counties_dict[county_name] += 1
      #declare a variable for votes each county received
   
    #iterate through the votes each county received
    
      
      # if votes_by_county not in counties_dict:
      #   counties_dict[county_name] = votes_by_county
      #   votes_by_county += 1 
    
      #   # getting the percentage of votes each county received
      # county_percentage = float(votes_by_county) / float(total_votes) * 100
      # percent_count = (f"{county_name}: {county_percentage:.1f}% ({votes_by_county:,})\n")
      #find the number of votes for each county
      
with open(file_to_save, "w") as txt_file:
  election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    )
  print(election_results, end = '')
  txt_file.write(election_results)
  # county_results = (f"\n"
  #   f"County Votes:\n"
  #   f"{county_name}: {county_percentage:.1f}% ({votes_by_county:,})\n")
  #   # print out the ocunty results
  for key in counties_dict:
    county_vote = counties_dict[key]
    county_percentage = int(county_vote) / int(total_votes) * 100

    county_results = (
        f"{key}: {county_percentage: .1f}% ({county_vote:,})\n"
    )
    print(county_results,end="")
 
    txt_file.write(county_results)
    if(county_vote > votes_by_county):
      votes_by_county = county_vote
      largest_turnout = key
  #get the largest turnout for counties
  #largest_turnout = max(counties_dict, key=counties_dict.get) 
  
  # print the result in the output file
  turnout = (
    f"-------------------------\n"
    f"Largest County Turnout Is: {largest_turnout}\n"
    f"-------------------------\n")
  print(turnout)
  txt_file.write(turnout)  
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
  txt_file.write(winning_candidate_summary)
  # write the results in the election_results
  
  

      

