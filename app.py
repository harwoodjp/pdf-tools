import fire

from functions.extract import extract_text
from functions.split import split_to_png
from functions.ocr import ocr_my_pdf

class App:
	def extract(self, input_file, output_dir):
		""" Paginates and writes text from INPUT_FILE to OUTPUT_DIR """
		extract_text(input_file, output_dir)

	def split(self, input_file, output_dir):
		""" Paginates and writes PNGs from INPUT_FILE to OUTPUT_DIR """		
		try:
			split_to_png(input_file, output_dir)
			print(f"Split {input_file} to {output_dir}")
		except:
			print("Error occured during split")			

	def ocr(self, input_file, output_file):
		""" Generates text mapping for INPUT_FILE and writes out to OUTPUT_FILE """
		try:
			ocr_my_pdf(input_file, output_file)
			print(f"Applied OCR {input_file} to {output_file}")
		except:
			print("Error occured during ocr")			

if __name__ == "__main__":
	fire.Fire(App)

# cindex ~/Projects/pdf-deconstruction/output/Leavingthe20thCentury/txts/ 
# csearch "(?i)(chicago)"
# open ~/.csearchindex
