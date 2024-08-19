#!/usr/bin/python3

import csv

with open('popular_baby_names.txt', 'r') as txt_file:
     lines = txt_file.readlines()

with open('Popular_Baby_Names.csv', 'w', newline='') as csv_file:
     writer = csv.writer(csv_file)
     for line in lines:
          writer.writerow(line.strip().split())
