#!/usr/bin/env python
import time
import sys
import os


fasta = input("Fasta file: ")
name = input("Name file: ")
otu = input("OTU list file: ")

outName1 = fasta.strip()
outName2 = outName1.split(".")
numWords = sum(1 for word in outName2)

# Suggest outfile name based on fasta file name format
if(numWords > 3 and not (outName2[1] == "TSC") and not (outName2[2] == "TSC")):
    outName3 = ("%s.%s.%s.OTU.map" % (outName2[0],outName2[1],outName2[2]))
elif(numWords > 2 and not (outName2[1] == "TSC")):
    outName3 = ("%s.%s.OTU.map" % (outName2[0],outName2[1]))
else:
    outName3 = ("%s.OTU.map" % outName2[0])

print("\nSuggested outfile name: %s" % outName3)
choice = input("Keep (y) or specify new (n): ")

tries = 2

while choice not in ["y", "yes", "Y", "n", "no", "N"]:
    if(tries > 0):
        choice = input("Answer y or n. %s tries left." % (tries))
        tries -= 1
    else:
        print("\nPlease restart application.")
        sys.exit()

if choice in ["n", "no", "N"]:
    outName3 = input("Please specify a new filename: ")
        
# Choose directory
print("\nCurrent output path: %s\n" % os.getcwd())
pChoice = input("Use current path (y) or specify new (n): ")

while pChoice not in ["y", "yes", "Y", "n", "no", "N"]:
    if(pTries > 0):
        pChoice = input("Answer y or n. %s tries left." % (tries))
        pTries -= 1
    else:
        print("\nPlease restart application.")
        sys.exit()

if pChoice in ["y", "yes", "Y"]:
    outPath = os.getcwd()
    outName3 = ("%s/%s" % (outPath,outName3))

if pChoice in ["n", "no", "N"]:
    outPath = input("Output file path: ")
    try:
        if outPath[-1]=="/":
            outName3 = ("%s/%s" % (outPath,outName3))
    except IndexError:
        pass

print("\nOutfile path: %s" % outName3)


time.sleep(1)

start = time.time()

print("\nMatching FASTA + OTU items, please wait...")

# Convert name table to dictionary
name = open(name, 'r')
name_data = {}
for line in name:
    line = line.strip()
    columns = line.split()
    source = {}
    name_data[columns[0]] = columns[2]

# Formatting and skipping seq lines
with open(fasta) as file:
    letters = file.read().splitlines()
    letters = letters[::2]
    letters = [letter.replace('>','') for letter in letters]

# Combine fasta and otu list
def combine_ids(letters):
    with open(otu) as file:
        for line in file:
            id, space, numbers_str = line.lstrip().partition('\t')
            num1 = numbers_str.rstrip().partition('\t')
            try:
                numbers = list(map(int, (num1[2]).split(',')))
            except ValueError:
                continue # skip invalid lines
            for n in numbers:
                try:
                    yield letters[n], id
                except IndexError:
                    pass

final = dict(combine_ids(letters))

print("Matching completed.\n")
print("Matching OTU + name items, please wait...")

# Combine otu list with name file according to 'final' dictionary
complete = {}
for key in final.keys() & name_data.keys():
    complete.setdefault(final[key], []).append(name_data[key])

print("Matching completed.\n")
print("Writing to file...")

# Write to file
fh = open(outName3, "w")
for key, value in sorted(complete.items()):   
    fh.write(key)
    fh.write('\t')
    newVal = ('\t'.join(value))
    newVal = newVal.split(',')
    newVal = ('\t'.join(newVal))
    fh.write(newVal)
    fh.write("\n")
fh.close()

end = time.time()
print("All done.")

lb = 0
hb = 0
with open(outName3) as st:
    for line in st:
        if "OTULB" in line:
            lb += 1
        if "OTUHB" in line:
            hb += 1
            
print("\nHigh abundance OTUs: %s" % hb)
print("Low abundance OTUs: %s" % lb)

time_tot = (end-start)
file_size = os.path.getsize(outName3)
file_size = round((file_size / 1000000),2)

print("\nFile size: %s mb" % file_size)
print("Time elapsed: %s seconds." % round(time_tot, 2))

