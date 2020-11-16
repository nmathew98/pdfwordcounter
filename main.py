import pdftotext
import os
import datetime

# Find all PDFs in directory
files = []
for file in os.listdir("pdfs"):
	if file.endswith(".pdf"):
		files.append(os.path.join("pdfs", file))

# Words we are looking for
keys = []
with open("search.txt", "r") as f:
	for line in f:
		keys.extend(line.strip().split("\n"))

for file in files:
	# Create a dictionary with the keys we are looking for
	dictionary = {key: 0 for key in keys}
	with open(file, "rb") as f:
		pdf = pdftotext.PDF(f)

	for page in pdf:
		for key in keys:
			dictionary[key] += page.lower().strip().count(key.lower())

	# Print occurences to a file
	with open('occurences.txt', 'a') as f:
		print(f"File: {file} [{len(pdf)} pages]; Date: {datetime.date.today()}", file=f)
		total_occurences = 0
		for k, v in dictionary.items():
			print(f"{k}: {v}", file=f)
			total_occurences += v
		print(f"Total matched words: {total_occurences}", file=f)
		print("", file=f)