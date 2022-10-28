Optimize PDFs for web and search

Setup
* `pip install -r requirements.txt`
* Install [Tesseract]() 

Usage
* `app.py extract INPUT_FILE OUTPUT_DIR`
* `app.py split INPUT_FILE OUTPUT_DIR`
* `app.py ocr INPUT_FILE OUTPUT_FILE`

Examples
* `python app.py extract test.PDF test/text`
* `python app.py split test.PDF test/images`
* `python app.py ocr test.PDF test_ocr.PDF`

Functions
* `extract`
  * Paginates and writes text from INPUT_FILE to OUTPUT_DIR
* `split`
  * Paginates and writes PNGs from INPUT_FILE to OUTPUT_DIR
* `ocr`
  * Generates text mapping for INPUT_FILE and writes out to OUTPUT_FILE
  * Unnecessary if PDF has prior OCR