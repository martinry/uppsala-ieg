# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:33:22 2017

@author: Martin
"""
import collections

new_otus = collections.defaultdict(list)

with open('unique_renamed_otus.txt') as data:
    for d in data:
        d = d.strip("\n") # remove newline char
        line = d.split("\t") # split line at tab char
        
        for acc in line[1:]: # go through accession names
            size = acc
            size = size.split("=") # example: size=42; we split at = and ; to get size
            size = size[1].split(";")
            size = size[0]  # get the actual value in the list
            
            accession_names = []
            
            for i in range(1, int(size)+1): # count from 1 to size
                n = ("0000", str(i))        # acc names are 7-digit. we add four 0s for margin
                n = ''.join(n)              # and its iteration no. so it remains unique
                k = (acc, str(n))
                k = (''.join(k))
                accession_names.append(k)   # join and put into a list
                      
            new_otus[line[0]].append(accession_names)   # add into a dict, that looks like
                                                        # denovoX  [[accY00001, accY00002], [accZ00001, accZ00002]...]

fw = open("output.txt", "w")    # create output file
for k,v in new_otus.items():    # iterate through dict
    v = (list(a for b in v for a in b)) # since we have a list of lists [[] [] []...],
    v = '\t'.join(v)                    # we flatten and join so it can be written as a string
    fw.write(k + '\t' + v)
    fw.write("\n")
fw.close()

