# main.py

import os
import csv

# Initializing file paths.
csv_file_path = os.path.join("Resources", "election_data.csv") # Input.
analysis_file_path = os.path.join("analysis", "analysis.txt") # Output.

# Open and read csv.
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header.
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    voter_id = list()
    voter_county = list()
    voter_candidate = list()

    for row in csv_reader:
      voter_id.append(row[0])
      voter_county.append(row[1])
      voter_candidate.append(row[2])

    data = {
      "voter_id": voter_id,
      "voter_county": voter_county,
      "voter_candidate": voter_candidate
    }
    # Decided to not use list comprehensions here. Would be inefficient to got over the whole dataset 3 times give it's size.

    # Total number of votes.
    total_num_votes = len(data["voter_id"])

    # Creating dict of votes per candidate.
    set_of_candidates = set(data["voter_candidate"]) # Getting list if unique candidates.
    set_of_candidates_total_votes = dict()
    for candidate in set_of_candidates:
      set_of_candidates_total_votes.update({ f"{candidate}": len([c for c in data["voter_candidate"] if c == candidate])})

    # Candidate most voted for.
    candidate_most_voted = max(set_of_candidates_total_votes, key=set_of_candidates_total_votes.get)

    # Creating dict for percentage of votes per candidate.
    set_of_candidates_percentage_votes = dict()
    for key, value in set_of_candidates_total_votes.items():
        percentage = value * 100 / sum(set_of_candidates_total_votes.values())
        set_of_candidates_percentage_votes.update({ f"{key}": percentage})

    # Formatted output string.
    #   - Could use `set_of_candidates_percentage_votes["Khan"][:6]` but round seems more appropriate
    output = f"""
Election Results
-------------------------
Total Votes: {total_num_votes}
-------------------------
Khan: {round(set_of_candidates_percentage_votes["Khan"], 3)}% ({set_of_candidates_total_votes["Khan"]})
Correy: {round(set_of_candidates_percentage_votes["Correy"], 3)}% ({set_of_candidates_total_votes["Correy"]})
Li: {round(set_of_candidates_percentage_votes["Li"], 3)}% ({set_of_candidates_total_votes["Li"]})
O"Tooley: {round(set_of_candidates_percentage_votes["O'Tooley"], 3)}% ({set_of_candidates_total_votes["O'Tooley"]})
-------------------------
Winner: {candidate_most_voted}
-------------------------
    """

    # Open, write and close output file.
    analysis_file = open(analysis_file_path, "a")
    analysis_file.write(output)
    analysis_file.close()