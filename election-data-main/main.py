import csv

# CLASS DEFINITIONS

# Represents a single Member of Parliament
class MP:
    def __init__(self, first_name, surname, gender, party, votes):
        # Create full name by joining first and surname
        self.name = f"{first_name} {surname}"
        self.gender = gender
        self.party = party
        self.votes = votes

# Represents a political party
class Party:
    def __init__(self, name):
        self.name = name
        self.total_votes = 0
        self.mps = []  # List of MP objects in this party

    def add_mp(self, mp):
        self.mps.append(mp)
        self.total_votes += mp.votes  # Adds MP's votes to party total

# Represents a single constituency
class Constituency:
    def __init__(self, name, region, country, mp):
        self.name = name
        self.region = region
        self.country = country
        self.mp = mp  # The MP who won this seat



# DATA LOADING FUNCTION

# Reads the election data CSV and builds objects from it
def load_custom_csv_fixed(file_path):
    constituencies = []  # List to hold all constituencies
    parties = {}         # Dictionary to store party objects by name

    with open(file_path, 'r', encoding='latin1') as file:
        # Skip first two rows that are not headers
        next(file)
        next(file)

        # Read the actual header row
        headers = next(file).strip().split(',')
        reader = csv.DictReader(file, fieldnames=headers)

        for row in reader:
            try:
                # Extract basic MP/seat info from row
                fname = row['Member first name']
                sname = row['Member surname']
                gender = row['Member gender']
                const_name = row['Constituency name']
                region = row['Region name']
                country = row['Country name']

                # Find the party with the highest vote count in this row
                winning_party = None
                max_votes = 0
                for party in ['Con', 'Lab', 'Lib Dem', 'Green', 'SNP', 'PC', 'DUP', 'SF', 'SDLP', 'UUP', 'APNI']:
                    votes = row.get(party, '').replace(',', '')  # Remove commas from numbers
                    if votes.isdigit():
                        v = int(votes)
                        if v > max_votes:
                            max_votes = v
                            winning_party = party

                # Skip if no valid winning party found
                if not winning_party:
                    continue

                # Create MP object
                mp = MP(fname, sname, gender, winning_party, max_votes)

                # Create Party object if not already in dictionary
                if winning_party not in parties:
                    parties[winning_party] = Party(winning_party)
                parties[winning_party].add_mp(mp)

                # Create Constituency object and store
                constituencies.append(Constituency(const_name, region, country, mp))

            except Exception as e:
                print(f"Row error: {e}")  # Show errors during data reading

    return constituencies, parties


# MENU SYSTEM


# Command-line menu for user interaction
def menu(constituencies, parties):
    while True:
        print("\n--- Voting Analysis Menu ---")
        print("1. Search by Candidate Name")
        print("2. Search by Party")
        print("3. Search by Constituency")
        print("4. Show Party Vote Totals and Percentages")
        print("5. Save Statistics to File")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Search MPs by name
            name = input("Enter candidate name: ").lower()
            for c in constituencies:
                if name in c.mp.name.lower():
                    print(f"{c.mp.name} ({c.mp.party}) - {c.name} ({c.mp.votes} votes)")

        elif choice == "2":
            # Search by party
            party_name = input("Enter party name (e.g., Lab): ").strip()
            if party_name in parties:
                p = parties[party_name]
                print(f"{party_name} - Total Votes: {p.total_votes}, MPs: {len(p.mps)}")
            else:
                print("Party not found.")

        elif choice == "3":
            # Search by constituency
            seat = input("Enter constituency name: ").lower()
            found = False
            for c in constituencies:
                if seat in c.name.lower():
                    print(f"{c.name} - MP: {c.mp.name} ({c.mp.party}), Votes: {c.mp.votes}")
                    found = True
            if not found:
                print("Constituency not found.")

        elif choice == "4":
            # Show vote totals and percentage by party
            total_votes = sum(p.total_votes for p in parties.values())
            for name, p in parties.items():
                percent = (p.total_votes / total_votes) * 100 if total_votes else 0
                print(f"{name}: {p.total_votes} votes ({percent:.2f}%)")

        elif choice == "5":
            # Save statistics to text file
            save_statistics(parties, constituencies)

        elif choice == "0":
            break  # Exit the program

        else:
            print("Invalid input.") 



# FILE OUTPUT FUNCTION


# Save voting stats to "statistics.txt"
def save_statistics(parties, constituencies):
    try:
        with open("statistics.txt", "w", encoding='utf-8') as f:
            # Write party stats
            f.write("Party Statistics:\n")
            total_votes = sum(p.total_votes for p in parties.values())
            for name, p in parties.items():
                percent = (p.total_votes / total_votes) * 100 if total_votes else 0
                f.write(f"{name}: {p.total_votes} votes ({percent:.2f}%)\n")

            # Write constituency summary
            f.write("\nConstituency Summary:\n")
            for c in constituencies:
                f.write(f"{c.name} - {c.mp.name} ({c.mp.party}) - {c.mp.votes} votes\n")

        print("Statistics saved to statistics.txt.")

    except Exception as e:
        print(f"Error writing file: {e}")  # Catch any write errors


# MAIN PROGRAM ENTRY POINT


if __name__ == "__main__":
    cons, parties = load_custom_csv_fixed("election_data.csv")
    if cons and parties:
        menu(cons, parties)
    else:
        print("Could not load data")
