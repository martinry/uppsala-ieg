#!/usr/bin/env python
__author__ = "Martin Rydén"
__copyright__ = "Copyright 2016, Martin Rydén"
__license__ = "MIT"
__version__ = "1.0.1"
__email__ = "pemryd@gmail.com"

import time
from Bio import SeqIO

fasta_file = input("ITSx ITS2 fasta file: ")
positions_file = input("Positions file: ")

suggestion = fasta_file.split(".")
suggestion = ".".join(suggestion[:-1])
out_file = str(suggestion) + ".filtered.fna"
print("Outfile name: %s" %out_file)

tstart = time.time()
print("\nReading files...")
fasta = SeqIO.index(fasta_file, "fasta")

print("Processing...")

no58S = "5.8S: Not found"
noLSU = "LSU: Not found"

with open(out_file, "w") as fh:
    with open(positions_file, "r") as pos:
        for p in pos:
            p = p.split("\t")
            if((no58S not in p) and (noLSU not in p)):
                try:
                    name, sequence = fasta[p[0]].id, str(fasta[p[0]].seq)
                except KeyError:
                    pass
                fh.write(">%s\n"%name)
                fh.write("%s\n"%sequence)
fh.close()


tend = time.time()
time_tot = (tend-tstart)
print("\nTime elapsed: %s seconds." % round(time_tot, 2))

