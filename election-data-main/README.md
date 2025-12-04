
# UK General Election Voting Analysis Program

# Overview

This Python project was created as part of the assessment for the COMP10082 Programming Strand. It reads official UK General Election 2024 results (CSV format), and enables users to investigate data about Members of Parliament (MPs), political parties and constituencies.

The program provides a menu-based interface and lets users:

- Search for candidates
- Investigate individual parties and their total votes
- Search on a constituency basis
- See the percentage of vote share per party
- Store summary statistics to a file

# Object-Oriented Design

# MP Class
Encapsulates an MP's:
- Full name (first + surname)
- Sex
- Party
- Number of votes received

# Party Class
Tracks:
- Party name
- Total number of votes received
- MPs belonging to party

# Constituency Class
Stores:
- Constituency name
- Region and Country
- Winning MP (object)

# File Handling

- **Input**: `election_data.csv` (from House of Commons Library dataset)
- **Output**: `statistics.txt` (auto-generated summary of party and constituency stats)

The program includes error handling in case there are missing or corrupted files, or invalid user selections.

# Testing Table

| Test Case                        | Input              | Expected Output                                    | Actual Output | Pass? |
|----------------------------------|--------------------|----------------------------------------------------|---------------|--------|
| Search by candidate name         | "Stephen Kinnock"  | Returns Aberafan Maesteg, party, votes             | ✅ Correct     | ✅     |
| Search by party                  | "Lab"              | Shows Lab MP count and vote total                  | ✅ Correct     | ✅     |
| Search by invalid constituency   | "Random Town"      | "Constituency not found."                          | ✅ Correct     | ✅     |
| Show party vote percentages      | Option 4           | Percentages per party printed                      | ✅ Correct     | ✅     |
| Save statistics to file          | Option 5           | `statistics.txt` is created                        | ✅ Correct     | ✅     |
| CSV File Missing                 | Remove CSV         | "Could not load data."                             | ✅ Correct     | ✅     |
| Vote field contains commas       | Votes = "1,234"    | Fixes correctly as 1234                           | ✅ Correct     | ✅     |

# Use Case Descriptions

- User selects option from menu
- System loads constituency data
- User searches data by name, party or seat
- System retrieves MP details or stores summary stats

# How to Run

1. Make sure Python 3 is installed.
2. Place `main.py` and `election_data.csv` in the same folder.
3. Open your Terminal and navigate to the folder.
4. Run the application:

```bash
cd ~/Documents/VotingProject
python3 main.py
```
