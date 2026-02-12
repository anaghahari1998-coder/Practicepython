# Data can be saved as .txt/.xml/.bin/.csv
# Data(output) can be saved as a txt file.
# can be opened in 3 modes(read, write and append)
# Read---just to watch("r" --- used to read the data)
# Write---new file creation("w" --- used for file creation)
# Append---update the existing file("a" --- used to append the data

# 1. Write to a file (creates or overwrites)
file = open("contacts.txt", "w")
file.write("Name: Alice, Phone: 1234567890\n")
file.write("Name: Bob, Phone: 9876543210\n")
file.close()  # Important: close the file!

# 2. Read and display contacts
file = open("contacts.txt", "r")
print("Contact List:")
for line in file:
    print(line.strip())
file.close()

# To append the data, this can be used to either append the data and add to the file or create a new file with this data
file = open("contacts.txt", "a")
file.write("Name: Charlie, Phone: 5551234567\n")
file.close()

