#the data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received voted
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#assign a variable for the file to load and the path
import csv
import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
file_to_load = "/Users/Kortney/Desktop/Election_Analysis/resources/election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")
#open the election results and read the file

file_to_save = os.path.join("analysis", "election_results.txt")
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")
with open(file_to_load) as election_data:
  #to do: read and analyze data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)  

