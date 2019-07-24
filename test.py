import csv
import os
import re


file_path = '/home/linusxrstha/projects/Visualization/dashboard/static/csv/reviews.csv'
with open(file_path) as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		print(str(row['listing_id']))
	print('Description Remaining...')
