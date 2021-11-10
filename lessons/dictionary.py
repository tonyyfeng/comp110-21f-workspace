"""Demonstrations of dictionary capabilities"""


# Declaring the type of a dictionary
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# test for existence of a key
is_duke_present: bool = "Duke" in schools
# if duke is in schools it will eval to true, otherwise, false
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Empty dictionary literal
schools = {} # Same as dict()

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}


for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")