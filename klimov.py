#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import sys
from datetime import datetime

def to_integer(dt_time):
    return 10000*dt_time.year + 1000*dt_time.month + dt_time.day

if len(sys.argv) == 1:
	print "Need relative path to csv at first argument!"
	exit()


results = {}
current_segment = None

with open(sys.argv[1], 'rb') as csv_file:
	reader = csv.reader(csv_file, delimiter=';', quotechar='|')
	for row in reader:

		if current_segment is None or current_segment not in results or len(row) != 0:
			cell_value = row[0]

			try:
				date_object = datetime.strptime(cell_value, '%d.%m.%y')
			except ValueError as e:
				continue

			current_segment = to_integer(date_object)
			results[current_segment] = {'counter': 0, 'date': date_object}
		else:
			results[current_segment]['counter'] += 1

for key in sorted(results):
    print "%s: %s" % (results[key]['date'].strftime('%d.%m.%Y'), results[key]['counter'])