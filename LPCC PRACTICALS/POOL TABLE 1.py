#GENERATE POOL TABLE
import re
file = open("INPUT CODE 3.txt")
lines = file.readlines()
tlines = []
for line in lines:
    tlines.append(line.split())
#print(tlines)

def isLit(s):
    pattern = r"^='(\d+)'$"
    return (re.match(pattern, s))

lit_count = 1
ad_c = 1

pool_tab = []

pool_tab.append("#"+str(lit_count))

for line in tlines:
    if(isLit(line[-1])):
        lit_count += 1
    elif(line[0] == 'LTORG'):
        ad_c +=1
        pool_tab.append("#"+str(lit_count))

if(ad_c != len(pool_tab)):
    pool_tab.pop()
print(pool_tab)
# Initialize variables
'''literal_table = []  # Store literals and their assigned addresses
pool_table = []  # Store pool start indices

# Function to add literal to the literal table and update the pool table
def add_literal(literal):
    global literal_table

    # Check if literal is already in the literal table
    if literal not in [l["literal"] for l in literal_table]:
        # Add the new literal to the literal table with a placeholder for address
        literal_table.append({"literal": literal, "address": None})

# Function to end a literal pool and assign addresses to literals
def end_literal_pool(current_location):
    global pool_table

    # Add current pool start index
    pool_table.append(len(literal_table))

    # Assign addresses to literals in the current pool
    for i in range(pool_table[-1], len(literal_table)):
        literal_table[i]["address"] = current_location
        current_location += 1

    return current_location

# Function to parse assembly code and generate the literal and pool tables
def parse_assembly_code(file_path):
    global literal_table, pool_table
    location_counter = 0

    # Open the text file containing assembly code
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            words = line.split()  # Split line into words

            if "LTORG" in words or "END" in words:
                # End the current literal pool
                location_counter = end_literal_pool(location_counter)

            # Identify literals in the line
            for word in words:
                if word.startswith("="):
                    # Add literal to the literal table
                    add_literal(word)
            
            # Increment the location counter for each line
            location_counter += 1

    return location_counter

# File path to the assembly code text file
assembly_code_file = "INPUT CODE 3.txt"  # Replace with your file path

# Parse the assembly code to generate the literal and pool tables
parse_assembly_code(assembly_code_file)

# Display the literal table
print("Literal Table:")
for idx, entry in enumerate(literal_table):
    print(f"{idx}: Literal = {entry['literal']}, Address = {entry['address']}")

# Display the pool table
print("Pool Table:")
print(pool_table)'''

