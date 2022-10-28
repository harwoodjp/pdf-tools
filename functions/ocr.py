from ocrmypdf import ocr, PriorOcrFoundError

def ocr_my_pdf(input_file, output_file):
  try:
    print(f"Processing: {input_file}")
    ocr(
      input_file,
      output_file,
      force_ocr=True
    )
    return output_file
  except PriorOcrFoundError:
    print(f"Skipping {input_file}")    
    return input_file
