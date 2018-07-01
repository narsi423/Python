# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = 'Info*.txt'

# Save all file matches: csv_files
txt_files = glob.glob(pattern)

if 'Info2.txt' in txt_files:
    print("Avaialble")
else:
    print("Not there")
# Print the file names
print(txt_files)

# Load the second file into a DataFrame: csv2
txt2 = pd.read_csv(txt_files[1])

# Print the head of csv2
print(txt2.head())