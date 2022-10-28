import os
import PyPDF2

def extract_text(input_file, output_dir):
	print(f"Processing {input_file}")
	file = open(input_file, "rb")
	reader = PyPDF2.PdfFileReader(file)
	for i in range(0, reader.numPages):
		p = "{:04d}".format(i+1)
		output_file = f"{output_dir}/{p}.txt"
		with open(output_file, "w") as f:
			page = reader.getPage(i)
			f.write(page.extractText())
